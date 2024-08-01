from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __edit_button = (By.ID, "edit_btn")
    __add_button = (By.ID, "add_btn")
    __second_row_input = (By.XPATH, "//div[@id='row2']/input[@class='input-field']")
    __save_button = (By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
    __remove_button = (By.ID, "remove_btn")
    __saved_confirmation_message = (By.ID, "confirmation")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_webpage(self):
        """
        This method opens the exceptions web page
        :return:
        """
        super()._open_web_page(url=self.__url)

    def click_add_button(self):
        """
        This Method clicks the add button on the exceptions page
        :return:
        """
        super()._click(locator=self.__add_button)

    def is_row_two_displayed(self) -> bool:
        """
        This method checks to see if row 2 on the exceptions page is displayed
        :return:
        """
        return super()._is_displayed(locator=self.__second_row_input, time=6)

    def add_to_list_of_favorite_foods(self, text):
        """
        This method will do the following:
        Click Add button, Wait for second row to load, type into second input field, and push save
        :return:
        """
        super()._click(locator=self.__add_button)
        super()._type_into_element(locator=self.__second_row_input, text=text, time=6)
        super()._click(locator=self.__save_button)

    def is_saved_confirmation_message_displayed(self) -> bool:
        """
        This method checks to see if the saved confirmation message when a user adds to the list
        of favorite foods appears on the page
        :return:
        """
        return super()._is_displayed(locator=self.__saved_confirmation_message)
