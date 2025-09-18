# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing dashboard page to use methods in it.
from Pages.dashboard_page import DashboardPage
# To reuse data from Utils folder like valid credentials
from Utils.config import valid_email,valid_password


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestMenuIcons:

    #test_menu_items() checks the visibility and clickability of Menu items in Dashboard after login.
    def test_menu_items(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        login_page.login(valid_email,valid_password)

        # Checks whether login navigates to dashboard page url
        dashboard_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        assert dashboard_url in login_page.get_current_url()
        print("Logged in successfully")

        # Creates instance of DashboardPage class to access the menu items
        dashboard_menu=DashboardPage(self.driver)
        # Loops through each menu items stored as dictionary
        for menu_name,locator in dashboard_menu.MENU_ITEMS.items():
            # element contains the locator value
            element = dashboard_menu.find_element(locator)

            # Checks each menu is visible and enabled
            assert element.is_displayed(), f"{menu_name} is not visible"
            assert element.is_enabled(), f"{menu_name} is not enabled"
            print(f"{menu_name} is visible and clickable")


    # test_invalid_menu() fails since dictionary of MENU_ITEMS is accessing only its Key
    @pytest.mark.negative
    def test_invalid_menu(self):

        login_page = LoginPage(self.driver)
        login_page.login(valid_email, valid_password)

        dashboard_menu = DashboardPage(self.driver)
        # Loops through each menu items stored as dictionary
        for menu_name, locator in dashboard_menu.MENU_ITEMS.keys():
            # element contains the locator value
            element = dashboard_menu.find_element(locator)

            # Checks each menu is visible and enabled
            assert element.is_displayed(), f"{menu_name} is not visible"
            assert element.is_enabled(), f"{menu_name} is not enabled"
            print("Error occurs provide proper access to MENU ITEMS")









