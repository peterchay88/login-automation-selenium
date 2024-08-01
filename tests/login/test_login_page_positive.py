import pytest
from page_objects.login_page import LoginPage
from page_objects.logged_in_successfully import LoggedInSuccessfully

pytestmark = [pytest.mark.positive, pytest.mark.login]


class TestPositive:

    @pytest.mark.tcid01
    def test_login_positive(self, driver):
        """
        1. Navigate to web page
        2. Type student into the username field
        3. Type Password123 into the password field
        4. Push the submit button
        5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        6. Verify that you are on the "logged in page" by confirming the logout button, page header, and url
        :param driver:
        :return:
        """
        login_page = LoginPage(driver=driver)
        login_page.open_browser()
        login_page.execute_login(username="student", password="Password123")

        logged_in_page = LoggedInSuccessfully(driver=driver)
        assert logged_in_page.current_url == logged_in_page.get_expected_url, \
            (f"Unexpected value for current url. Expected {logged_in_page.get_expected_url}. "
             f"Actual {login_page.current_url}")
        assert logged_in_page.get_header_text == "Logged In Successfully", \
            f"Unexpected value for header text. Actual {logged_in_page.get_header_text}"
        assert logged_in_page.is_logout_button_displayed, "Error logout button is not displayed"

