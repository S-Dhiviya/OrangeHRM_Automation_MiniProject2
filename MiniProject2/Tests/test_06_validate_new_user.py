# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing Selenium Exceptions to raise when error occurs
from selenium.common import TimeoutException
# Importing Login page to use methods in it.
from Pages.login_page import LoginPage
# Importing Admin page to use methods in it.
from Pages.admin_page import AdminPage
# To reuse data from Utils folder like valid credentials
from Utils.config import valid_email,valid_password,username,invalid_username


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestValidateUser:

    # test_valid_new_user() enters valid data and validates whether new user created is present or not in ADMIN User list
    def test_validate_new_user(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters valid data
        login_page.login(valid_email,valid_password)

        # Creates an instance of the AdminPage class
        admin_page=AdminPage(self.driver)
        # validate_new_user() clicks Admin menu and enters username and clicks Search
        # Searches the table row whether the username is present on the list
        search_user = admin_page.validate_new_user(username)

        # Checks the username and returns user found or not
        assert search_user, "User not found in the system"
        print(f"User {search_user}is present on the list")


    # test_invalid_new_user() enters valid data and checks invalid new user is present on User list
    # This test fails and throws TimeoutException
    @pytest.mark.negative
    def test_invalid_new_user(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters valid data
        login_page.login(valid_email, valid_password)

        # Creates an instance of the AdminPage class
        admin_page = AdminPage(self.driver)

        # validate_new_user() clicks Admin menu and enters invalid username and clicks Search
        # Exception Handling
        try:
            # Searches the table row whether the invalid username is present on the list
            admin_page.validate_new_user(invalid_username)
        except TimeoutException:
            print("No records of user is found")