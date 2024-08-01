import pytest
from page_objects.login_page import LoginPage

pytestmark = [pytest.mark.negative, pytest.mark.login]


class TestNegative:

    @pytest.mark.parametrize("username, password, expected_error_msg", [
        pytest.param("incorrectUser", "Password123", "Your username is invalid!", marks=pytest.mark.negative_1),
        pytest.param("student", "incorrectPassword", "Your password is invalid!", marks=pytest.mark.negative_2)
    ])
    def test_negative_login_username(self, username, password, expected_error_msg, driver):
        login_page = LoginPage(driver)
        # open web page
        login_page.open_browser()
        # Type incorrectUser into Username field & Password123 into the password field. Click the submit button.
        login_page.execute_login(username=username, password=password)

        # Verify the error message is displayed
        assert login_page.check_if_error_msg_exists(), "Error message does not exist on page"
        # # Verify error message text is Your username is invalid!
        assert login_page.check_error_message_text() == expected_error_msg, \
            "Text in error message does not match 'Your username is invalid!'"
