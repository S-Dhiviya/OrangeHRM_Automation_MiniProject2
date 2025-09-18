# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing Class HomePage from home_page under Pages folder
from Pages.leave_page import LeavePage
# To reuse data from Utils folder like valid credentials
from Utils.config import *


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLeave:

    # test_assign_leave() is used to assign leave to employee and verify assigned leave
    def test_assign_leave(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        login_page.login(valid_email, valid_password)

        # Creates instance of LeavePage Class and clicks Leave menu
        leave_page = LeavePage(self.driver)
        leave_page.click_element(leave_page.LEAVE_MENU)

        # Checks navigation to Leave menu
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"
        assert expected_url in leave_page.get_current_url()

        # Adding entitled days for employee and assigning leave
        # Entitled days depicts total no. of leave days
        leave_page.add_entitlements(Employee_name,Leave_Type, Entitled_Days)
        leave_page.click_element(leave_page.LEAVE_MENU)
        leave_page.click_element(leave_page.ASSIGN_LEAVE)

        # Checks navigation to Assign Leave
        assign_leave_url="https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave"
        assert assign_leave_url in leave_page.get_current_url()

        # assigning_leave() assigns leave to employee including leave type,from and to date
        leave_page.assigning_leave(Employee_name,Leave_Type,From_Date,To_Date)
        print("Successfully assigned leave")

        # Checks whether leave is scheduled in employee record
        search_employee=leave_page.check_leave_list(Employee_name,Leave_Status)
        assert search_employee, "User not found in the system"
        print(f"{search_employee} leave is scheduled on the list")

