from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")
    __login_error = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_browser(self):
        """
        This method opens a web page
        :return:
        """
        super()._open_web_page(self.__url)

    def execute_login(self, username: str, password: str):
        """
        This method attempts to log in via the username and password passed as arguments. Once the username and
        password are entered then we click the submit
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

    def check_if_error_msg_exists(self) -> bool:
        """
        This method checks to see if the error message exists after a bad login attempt
        :return:
        """
        return super()._is_displayed(locator=self.__login_error)

    def check_error_message_text(self) -> str:
        """
        This method checks the text of the error message
        :return:
        """
        return super()._get_element_text(locator=self.__login_error)

