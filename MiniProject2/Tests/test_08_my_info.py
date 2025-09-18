# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing Login page to use methods in it.
from Pages.login_page import LoginPage
# Importing Info page to use methods in it.
from Pages.info_page import InfoPage
# To reuse data from Utils folder like valid credentials
from Utils.config import valid_email,valid_password


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestMyInfo:

    # test_validate_my_info() validates the presence of all the menu items under My Info
    @pytest.mark.positive
    def test_validate_my_info(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page=LoginPage(self.driver)
        login_page.login(valid_email,valid_password)

        # Creates instance of InfoPage class
        info_page=InfoPage(self.driver)
        # Navigates to My Info Page from Dashboard Page
        info_page.click_element(info_page.MYINFO_ICON)

        # Checks the My Info Page URL
        expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
        assert expected_url in  info_page.get_current_url()


        # Loops through each menu items in My Info items stored as dictionary
        for menu_name,locator in  info_page.My_Info_Menu.items():
            # element contains the locator value
            element =  info_page.find_element(locator)

            # Checks each menu in My Info is visible and enabled
            assert element.is_displayed(), f"{menu_name} is not visible"
            assert element.is_enabled(), f"{menu_name} is not enabled"
            print(f"{menu_name} is visible and clickable")

        # To open any menu item under My Info. It navigates to that particular menu page
        # Any menu under My Info can be given like "IMMIGRATION"
        info_menu= info_page.get_myinfo_menu_name("IMMIGRATION")
        info_page.click_element(info_menu)



   # test_invalid_my_info() fails since dictionary of MENU_ITEMS is accessing only its Key
    @pytest.mark.negative
    def test_invalid_my_info(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page=LoginPage(self.driver)
        login_page.login(valid_email,valid_password)

        # Creates instance of InfoPage class
        info_page=InfoPage(self.driver)
        # Navigates to My Info Page from Dashboard Page
        info_page.click_element(info_page.MYINFO_ICON)

        # Loops through each menu items in My Info items stored as dictionary
        for menu_name,locator in  info_page.My_Info_Menu.keys():
            # element contains the locator value
            element =  info_page.find_element(locator)

            # Checks each menu in My Info is visible and enabled
            assert element.is_displayed(), f"{menu_name} is not visible"
            assert element.is_enabled(), f"{menu_name} is not enabled"
            print("Error occurs provide proper access to MENU ITEMS")


