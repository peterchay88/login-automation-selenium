import pytest
from page_objects.login_page import LoginPage
from page_objects.logged_in_successfully import LoggedInSuccessfully

pytestmark = [pytest.mark.positive, pytest.mark.login]


class TestPositive:

    @pytest.mark.tcid01
    def test_login_positive(self, driver):
        login_page = LoginPage(driver=driver)
        # Navigate to web page
        login_page.open_browser()
        # Type student into username field &  Password123 into password field. Then Push submit button
        login_page.execute_login(username="student", password="Password123")

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        logged_in_page = LoggedInSuccessfully(driver=driver)
        assert logged_in_page.current_url == logged_in_page.get_expected_url, \
            (f"Unexpected value for current url. Expected {logged_in_page.get_expected_url}. "
             f"Actual {login_page.current_url}")
        # After you are logged in verify that logged in successfully exists on the page
        assert logged_in_page.get_header_text == "Logged In Successfully", \
            f"Unexpected value for header text. Actual {logged_in_page.get_header_text}"
        # Verify that the log-out button exists on the page

        assert logged_in_page.is_logout_button_displayed, "Error logout button is not displayed"

