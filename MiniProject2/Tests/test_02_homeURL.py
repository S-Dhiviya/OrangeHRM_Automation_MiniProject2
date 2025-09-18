# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing base page to use methods in it.
from Pages.base_page import BasePage


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestHomeURL:

        # test_valid_url() checks whether the url navigates to the ORANGE HRM portal and checks the current url
        @pytest.mark.positive
        def test_valid_url(self):
            # This line creates an instance of the BasePage class, and passes the WebDriver instance (self.driver) to it.
            base_page = BasePage(self.driver)
            assert base_page.get_current_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            print("Properly navigated to OrangeHRM portal")

        # test_invalid_url() fails since the current url doesn't match the given url
        @pytest.mark.negative
        def test_invalid_url(self):
            # This line creates an instance of the BasePage class, and passes the WebDriver instance (self.driver) to it.
            base_page = BasePage(self.driver)
            assert base_page.get_current_url() == "https://opensource-demo.oranglive.com/web/index.php/auth/login", "Incorrect URL"









