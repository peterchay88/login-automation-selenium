from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
import logging as logger


class LoggedInSuccessfully(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def get_expected_url(self) -> str:
        """
        Returns the expected url for the web page when you log in successfully
        :return:
        """
        logger.info(f"Returning expected URL: {self.__url}")
        return self.__url

    @property
    def get_header_text(self) -> str:
        """
        Returns the header text from the web page when you log in successfully
        :return:
        """
        logger.info(f"Header Text: {super()._get_element_text(locator=self.__header_locator)}")
        return super()._get_element_text(locator=self.__header_locator)

    @property
    def is_logout_button_displayed(self) -> bool:
        """
        Checks to see if the logout button is displayed
        :return:
        """
        logger.info(f"Is the logout button displayed: {super()._is_displayed(locator=self.__log_out_button)}")
        return super()._is_displayed(locator=self.__log_out_button)
