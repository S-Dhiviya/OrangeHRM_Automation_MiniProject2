# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing Login page to use methods in it.
from Pages.login_page import LoginPage
# To reuse data from Utils folder like valid credentials
from Utils.config import username


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestForgotPassword:

    # test_forgot_password_link() once clicked forgot password it asks for username
    # Link indicating that password reset instructions is sent to registered email
    def test_forgot_password_link(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)

        #forgot_password() opens the forgot password link and enters the username and clicks reset password
        message_text = login_page.forgot_password(username)
        # Reset message sent to the user
        print(f"Reset message in test: {message_text}")



