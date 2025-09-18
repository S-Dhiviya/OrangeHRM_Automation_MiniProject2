# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing Selenium Exceptions to raise when error occurs
from selenium.common import NoSuchElementException


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLoginButton:

    #test_login_fields() checks the visibility and clickability of the Login button.
    def test_login_fields(self):

        # Exception Handling
        try:
            # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
            login_page = LoginPage(self.driver)
            # Access the username and password locators from LoginPage
            USERNAME_FIELD=login_page.find_element(login_page.USERNAME_INPUT)
            PASSWORD_FIELD=login_page.find_element(login_page.PASSWORD_INPUT)

        except NoSuchElementException:
            print("Login fields are not present")

        # is_displayed()checks the visibility
        assert USERNAME_FIELD.is_displayed(), "Username field is not visible"
        # is_enabled() checks whether its clickable or not
        assert USERNAME_FIELD.is_enabled(),"Username field is not clickable"

        # is_displayed()checks the visibility
        assert PASSWORD_FIELD.is_displayed(), "Password field is not visible"
        # is_enabled() checks whether its clickable or not
        assert PASSWORD_FIELD.is_enabled(), "Password field is not clickable"