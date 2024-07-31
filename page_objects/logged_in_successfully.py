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
        return self.__url

    @property
    def get_header(self) -> str:
        return self.driver.find_element(self.__header_locator).text

    @property
    def is_logout_button_displayed(self) -> bool:
        return self.driver.find_element(self.__log_out_button).is_displayed()
