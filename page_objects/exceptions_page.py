from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __edit_button = (By.ID, "edit_btn")
    __add_button = (By.ID, "add_btn")
    __second_row_input = (By.XPATH, "//div[@id='row2']/input[@class='input-field']")
    __first_row_input = (By.XPATH, "//div[@id='row1']/input[@class='input-field']")
    __row_one_save_button = (By.XPATH, "//div[@id='row1']/button[@id='save_btn']")
    __row_two_save_button = (By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
    __remove_button = (By.ID, "remove_btn")
    __saved_confirmation_message = (By.ID, "confirmation")
    __instructions_text = (By.ID, "instructions")

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

    def click_edit_button(self):
        """
        This Method clicks the edit button on the exceptions page
        :return:
        """
        super()._click(locator=self.__edit_button)

    def click_row_one_save_button(self):
        """
        This Method clicks the save button on row one on the exceptions page
        :return:
        """
        super()._click(locator=self.__row_one_save_button)

    def click_row_two_save_button(self):
        """
        This Method clicks the save button on row two on the exceptions page
        :return:
        """
        super()._click(locator=self.__row_two_save_button)

    def is_row_two_displayed(self) -> bool:
        """
        This method checks to see if row 2 on the exceptions page is displayed
        :return:
        """
        return super()._is_displayed(locator=self.__second_row_input, time=6)

    def is_saved_confirmation_message_displayed(self) -> bool:
        """
        This method checks to see if the saved confirmation message when a user adds to the list
        of favorite foods appears on the page
        :return:
        """
        return super()._is_displayed(locator=self.__saved_confirmation_message)

    def clear_text_in_row_one_input(self):
        """
        This method clears the text in the row 1 input field
        :return:
        """
        super()._clear_text(locator=self.__first_row_input)

    def get_text_from_confirmation_msg(self) -> str:
        """
        This method returns the text in the saved confirmation message on the exceptions page
        :return:
        """
        return super()._get_element_text(locator=self.__saved_confirmation_message)

    def get_value_from_row_one_input(self) -> str:
        """
        This method returns the text in the row one input field on the exceptions page
        :return:
        """
        return super()._get_attribute(locator=self.__first_row_input, attribute="value")

    def check_if_instructions_element_is_gone(self) -> WebElement:
        """
        This method checks to see if the instructions text on the exceptions page is
        still showing or not
        :return:
        """
        return super()._wait_until_element_is_not_visible(locator=self.__instructions_text)

    def add_to_list_of_favorite_foods(self, text: str):
        """
        This method will do the following:
        Click Add button, Wait for second row to load, type into second input field, and push save
        :return:
        """
        self.click_add_button()
        super()._type_into_element(locator=self.__second_row_input, text=text, time=6)
        self.click_row_two_save_button()

    def edit_row_one_input(self, text: str):
        """
        This method will do the following:
        Click the edit button, clear the row one input field, enter new text in, and click save
        :param text: New text to be entered
        :return:
        """
        self.click_edit_button()
        super()._clear_text(locator=self.__first_row_input)
        super()._type_into_element(locator=self.__first_row_input, text=text)
        self.click_row_one_save_button()
