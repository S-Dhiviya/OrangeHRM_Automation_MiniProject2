# Test Classes contains test scripts and calling actions
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing Admin page to use methods in it.
from Pages.admin_page import AdminPage
# Importing Claim page to use methods in it.
from Pages.claim_page import ClaimPage
# To reuse data from Utils folder like valid credentials
from Utils.config import *


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestClaim:

    # test_claim_request() enters as Employee and submits claim and checks the claim submission
    # Create a new employee using test_05_add_new_user.py
    def test_claim_request(self):

        #creates an instance of the LoginPage class
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters username and password
        login_page.login(username, password)

        # creates an instance of the ClaimPage class
        claim_page = ClaimPage(self.driver)
        # Clicks CLAIM under Dashboard Page
        claim_page.click_element(claim_page.CLAIM_ICON)

        # Checks navigation of CLAIM URL
        claim_url = "https://opensource-demo.orangehrmlive.com/web/index.php/claim/viewAssignClaim"
        assert claim_url in claim_page.get_current_url()

        # submit_claim() does Submission of Claim by providing event and currency type
        claim_page.submit_claim(Event_Type,Currency_Type)
        submit_url="https://opensource-demo.orangehrmlive.com/web/index.php/claim/submitClaim"
        assert submit_url in claim_page.get_current_url()

        # adding_expenses() Adding expenses including details and submitting claim
        claim_page.adding_expenses(Expenses_Type, Claim_Date, Claim_Amount)
        print("Claim initiated successfully ")

        # Checks whether claim of that employee is present on the claim history
        search_employee = claim_page.check_claim(Employee_name)
        assert search_employee, "User not found in the system"
        print(f"{search_employee} claim is present on the list")



