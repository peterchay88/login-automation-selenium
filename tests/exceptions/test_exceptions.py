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

    @pytest.mark.exception_tc03
    def test_invalid_element_state(self, driver):
        # Open webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Clear input field
        edit_btn = driver.find_element(By.ID, "edit_btn")
        edit_btn.click()

        input_field = driver.find_element(By.XPATH, "//div[@id='row1']/input[@class='input-field']")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(input_field))
        input_field.clear()
        # Type text into the input field
        new_text = "this is a test"
        input_field.send_keys(new_text)

        save_btn = driver.find_element(By.ID, "save_btn")
        save_btn.click()
        # verify text changed
        assert input_field.get_attribute("value") == new_text, \
            f"Error unexpected value. Expected {new_text}. Actual {input_field.get_attribute('value')}"

    @pytest.mark.exception_tc04
    def test_stale_element_reference(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_btn = driver.find_element(By.ID, "add_btn")
        add_btn.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.invisibility_of_element_located((By.ID, "instructions")),
                          "Error! instructions element still located on the page")

    @pytest.mark.exception_tc05
    def test_time_out(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click add button
        add_btn = driver.find_element(By.ID, "add_btn")
        add_btn.click()
        # Wait 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input[@class='input-field']")),
                   "Error, row 2 is not visible yet")
