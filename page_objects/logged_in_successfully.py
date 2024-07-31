from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfully:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def get_expected_url(self) -> str:
        """
        Returns the expected url for the web page when you log in successfully
        :return:
        """
        return self.__url

    @property
    def get_header_text(self) -> str:
        """
        Returns the header text from the web page when you log in successfully
        :return:
        """
        return self.driver.find_element(self.__header_locator).text

    @property
    def is_logout_button_displayed(self) -> bool:
        """
        Checks to see if the logout button is displayed
        :return:
        """
        return self.driver.find_element(self.__log_out_button).is_displayed()
