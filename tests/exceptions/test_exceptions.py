import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.exceptions_page import ExceptionsPage

pytestmark = [pytest.mark.exceptions]


class TestExceptions:

    @pytest.mark.exception_tc01
    def test_no_such_element_exception(self, driver):
        """
        1. Open web page
        2. Click add button
        3. Verify Row 2 is displayed
        :param driver:
        """
        exceptions_page = ExceptionsPage(driver=driver)
        exceptions_page.open_webpage()
        exceptions_page.click_add_button()
        assert exceptions_page.is_row_two_displayed(), "Error. Row 2 is not displayed"

    @pytest.mark.exception_tc02
    def test_element_not_interactable_exception(self, driver):
        """
        1. Open web page
        2. Click add button
        3. Wait for second row to load
        4. Type text into the second input field
        5. Click save button
        6. Verify text is saved
        :param driver:
        :return:
        """
        exceptions_page = ExceptionsPage(driver=driver)
        exceptions_page.open_webpage()
        exceptions_page.add_to_list_of_favorite_foods(text="Hot Dogs")
        assert exceptions_page.is_saved_confirmation_message_displayed(), \
            "Error. Saved confirmation message was not found on the page."

    @pytest.mark.parametrize("text, confirmation_msg", [
        pytest.param("Hot Dogs", "Row 1 was saved", marks=pytest.mark.exception_tc03),
        pytest.param("Ice Cream", "Row 1 was saved", marks=pytest.mark.exception_tc06)
    ])
    def test_invalid_element_state(self, text, confirmation_msg, driver):
        """
        1. Open webpage
        2. Clear input field
        3. Type text into the input field
        4. verify text changed
        :param driver:
        :return:
        """
        exceptions_page = ExceptionsPage(driver=driver)
        exceptions_page.open_webpage()
        exceptions_page.edit_row_one_input(text=text)
        assert exceptions_page.is_saved_confirmation_message_displayed(), \
            "Error. Saved confirmation message was not found"
        assert exceptions_page.get_text_from_confirmation_msg() == confirmation_msg, \
            (f"Error. Saved confirmation returned unexpected message. Expected {confirmation_msg}. "
             f"Actual: {exceptions_page.get_text_from_confirmation_msg()}")

    @pytest.mark.exception_tc04
    def test_stale_element_reference(self, driver):
        """
        1. Open page
        2. Push add button
        3. Verify instruction text element is no longer displayed
        :param driver:
        :return:
        """
        pass

    @pytest.mark.exception_tc05
    def test_time_out(self, driver):
        """
        1. Open page
        2. Click add button
        3. Wait 3 seconds for the second input field to be displayed
        :param driver:
        :return:
        """
        pass
