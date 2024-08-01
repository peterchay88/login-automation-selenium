import time
import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage


class TestNegative:

    @pytest.mark.negative_1
    def test_negative_login_username(self, driver):
        login_page = LoginPage(driver)
        # open web page
        login_page.open_browser()
        # Type incorrectUser into Username field & Password123 into the password field. Click the submit button.
        login_page.execute_login(username="incorrectUser", password="Password123")

        # Verify the error message is displayed
        assert login_page.check_if_error_msg_exists(), "Error message does not exist on page"
        # # Verify error message text is Your username is invalid!
        assert login_page.check_error_message_text() == "Your username is invalid!", \
            "Text in error message does not match 'Your username is invalid!'"

    @pytest.mark.negative_2
    def test_negative_login_password(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("incorrectPassword")

        submit_button = driver.find_element(By.ID, value="submit")
        submit_button.click()
        time.sleep(2)

        error_msg = driver.find_element(By.ID, "error")
        error_msg._is_displayed()
        assert error_msg.text == "Your password is invalid!"
