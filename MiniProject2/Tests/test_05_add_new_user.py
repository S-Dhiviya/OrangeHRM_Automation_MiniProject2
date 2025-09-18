# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing Admin page to use methods in it.
from Pages.admin_page import AdminPage
# To reuse data from Utils folder like valid credentials and employee name
from Utils.config import *



# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestAddUser:

    # test_add_user() creates a new user and validates login of new user
    def test_add_user(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        login_page.login(valid_email,valid_password)

        # Navigates to Admin menu
        admin_page=AdminPage(self.driver)
        admin_page.click_element(admin_page.ADMIN_MENU)

        try:
            # Adds new user details and check successfully saved or not
            # [username,password,employee name is stored in config.py]
            admin_page.add_user(User_role,Status,Employee_name, username, password, password)
            print("User created successfully")
        except Exception as e:
            print(f"User cannot be created or already exists:{e}")

        # Clicks logout
        login_page.logout()

        # Login with newly created user
        login_page = LoginPage(self.driver)
        login_page.login(username,password)

        # Checks navigation to Dashboard page
        dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        login_page.wait_for_url(dashboard_url)
        assert dashboard_url in login_page.get_current_url()
        print("New user logins to the portal")


     # test_add_invalid_user() creates a new user with invalid details
    @pytest.mark.negative
    def test_add_invalid_user(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        login_page.login(valid_email, valid_password)

        # Navigates to Admin menu
        admin_page = AdminPage(self.driver)
        admin_page.click_element(admin_page.ADMIN_MENU)

        # Adds new user details and check successfully saved or not
        admin_page.add_user(User_role, Status, Employee_name_invalid, invalid_username, password, password)
        print("User cannot be created or already exists")


