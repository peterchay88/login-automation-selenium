from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find_web_element(self, locator: tuple) -> WebElement:
        """
        This method uses the protected _find method to find a web element on the page by its ID, ClASS, XPATH, ETC.
        For a list of supported types please reference Selenium BY documentation
        :param locator:
        :return:
        """
        return self._driver.find_element(*locator)

    def _type_into_element(self, locator: tuple, text: str, time: int = 10):
        """
        This method will type into a web page element
        :param locator: tuple of the locator type and the value
        :param text:
        :param time:
        :return:
        """
        self._wait_until_element_is_visible(locator, time)
        self._find_web_element(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        """
        This method clicks an element that is found on the web page
        :param locator:
        :param time:
        :return:
        """
        self._wait_until_element_is_visible(locator, time)
        self._find_web_element(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        """
        This method acts as a wrapper for the selenium external wait
        :param locator:
        :param time:
        :return:
        """
        wait = WebDriverWait(self._driver, time)
        wait.until(EC.visibility_of_element_located(locator))

    @property
    def current_url(self) -> str:
        """
        Returns the current url of the web driver
        :return:
        """
        return self._driver.current_url

    def _is_displayed(self, locator: tuple, time: int = 10) -> bool:
        """
        This method checks to see if the element on the page is displayed
        :param locator:
        :return:
        """
        try:
            self._wait_until_element_is_visible(locator, time)
            return self._find_web_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_web_page(self, url: str):
        """
        This method opens a web page at the url passed in the argument
        :return:
        """
        self._driver.get(url)

    def _get_element_text(self, locator: tuple, time: int = 10) -> str:
        """
        Returns the header text from the web page when you log in successfully
        :return:
        """
        self._wait_until_element_is_visible(locator, time)
        return self._find_web_element(locator).text


