from selenium.webdriver.common.by import By
import pytest


class TestPositive:

    @pytest.mark.tcid01
    def test_login_positive(self, driver):
        # Navigate to web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username student into username field
        username_locator = driver.find_element(by=By.XPATH, value="//input[@id='username']")
        username_locator.send_keys("student")
        # Type password Password123 into password field
        password_locator = driver.find_element(by=By.NAME, value="password")
        password_locator.send_keys("Password123")
        # Push submit button
        submit_locator = driver.find_element(by=By.XPATH, value="//button[@class='btn']")
        submit_locator.click()
        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        current_url = driver.current_url
        assert current_url == "https://practicetestautomation.com/logged-in-successfully/"
        # After you are logged in verify that logged in successfully exists on the page
        header_selector = driver.find_element(by=By.XPATH, value="//h1[@class='post-title']")
        text = header_selector.text
        assert text == "Logged In Successfully"
        # Verify that the log-out button exists on the page
        log_out_selector = driver.find_element(by=By.XPATH, value="//a[@class='wp-block-button__link has-text-color "
                                                                  "has-background has-very-dark-gray-background-color']")
        assert log_out_selector.is_displayed()