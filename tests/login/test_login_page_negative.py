import pytest
from page_objects.login_page import LoginPage

pytestmark = [pytest.mark.negative, pytest.mark.login]


class TestNegative:

    @pytest.mark.parametrize("username, password, expected_error_msg", [
        pytest.param("incorrectUser", "Password123", "Your username is invalid!", marks=pytest.mark.negative_1),
        pytest.param("student", "incorrectPassword", "Your password is invalid!", marks=pytest.mark.negative_2)
    ])
    def test_negative_login_username(self, username, password, expected_error_msg, driver):
        """
        This test confirms the correct error state if you enter the wrong username or password
        when trying to log in
        1. Open web page
        2. Type defined username for test into the username field
        3. Type defined password for test into the password field
        4. Check if login error exists. Confirm that the error message is correct for the test.
        :param username:
        :param password:
        :param expected_error_msg:
        :param driver:
        :return:
        """
        login_page = LoginPage(driver)
        login_page.open_browser()
        login_page.execute_login(username=username, password=password)
        assert login_page.check_if_error_msg_exists(), "Error message does not exist on page"
        assert login_page.check_error_message_text() == expected_error_msg, \
            "Text in error message does not match 'Your username is invalid!'"
