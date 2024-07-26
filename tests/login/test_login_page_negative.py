import time
import pytest
from selenium.webdriver.common.by import By


class TestNegative:

    @pytest.mark.negative_1
    def test_negative_login_username(self, driver):
        # open web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username student into Username field
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("incorrectUser")
        # Type Password123 into the password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")
        # click the submit button
        submit_button = driver.find_element(By.ID, "submit")
        time.sleep(2)
        submit_button.click()
        time.sleep(2)
        # Verify the error message is displayed
        error_msg = driver.find_element(By.ID, "error")
        assert error_msg.is_displayed()
        # Verify error message text is Your username is invalid!
        error_msg_text = error_msg.text
        assert error_msg_text == "Your username is invalid!"

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
        error_msg.is_displayed()
        assert error_msg.text == "Your password is invalid!"

