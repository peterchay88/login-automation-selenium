from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_web_page(self):
        """
        This method opens a web page
        :return:
        """
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        """
        This method attempts to log in via the username and password passed as arguments
        :param username: Username used during login
        :param password: Password used during login
        :return:
        """
        # Type into the username field
        super()._type_into_element(locator=self.__username_field, text=username)
        # Type into the password field
        super()._type_into_element(locator=self.__password_field, text=password)
        # Push submit button
        super()._click(locator=self.__submit_button)

