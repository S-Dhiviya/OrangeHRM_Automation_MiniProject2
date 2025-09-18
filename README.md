                 ** Automation Testing of HR Management Web Application(ORANGE HRM) **
		
This project automates the testing of the web application https://opensource-demo.orangehrmlive.com by simulating user actions and validating its core functionalities. The key modules covered include login, menu accessibility, user management,forgot password link, assigning leave, initiating claims, and logout functionality. It ensures the reliability of critical components through both positive and negative test scenarios.

The test scripts are developed using Selenium with Python and Pytest, following the Page Object Model (POM) framework and adhering to Object-Oriented Programming (OOP) principles. The test data is externalized (CSV) using Data Driven framework, and common configurations are handled in config.py.The suite includes 10 detailed test cases focused on verifying page behavior, accessibility of essential elements, navigation flows, and login/logout processes.


**Project Architecture :**

**MiniProject2/**
│
├── **Data/**
│   ├── __init__.py
│   ├── login_data-1.csv
├── **Pages/**
│   ├── __init__.py
│   ├── admin_page.py
│   ├── base_page.py
│   ├── claim_page.py
│   ├── dashboard_page.py
│   ├── info_page.py
│   ├── leave_page.py
│   ├── login_page.py
│
├── **Tests/**
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_01_validate_login.py
│   ├── test_02_homeURL.py
│   ├── test_03_login_fields.py
│   ├── test_04_menu_items.py
│   ├── test_05_add_new_user.py
│   ├── test_06_validate_new_user.py
│   ├── test_07_forgot_password.py
│   ├── test_08_my_info.py
│   ├── test_09_assign_leave.py
│   ├── test_10_claim_request.py
│
├── **Utils/**
│   ├── __init__.py
│   ├── config.py
│
├── requirements.txt
├── README.md


**Tools & Technologies:**
*     Selenium WebDriver
*     Python 
*     Pytest
*     OOPS
*     Page Object Model (POM)
*     Data Driven Testing
*     Test Data(CSV file)
*     Explicit Waits
*     Exception Handling
*     Pytest HTML Reports



**Test Suite :**

Test Case 1: Validates login functionality using multiple sets of credentials using external CSV file

	* Positive case: Properly enters orangehrm login page and enters valid data and clicks logout
	* Negative case: Enters orangehrm login page and enters invalid data and displays error message
 
Test Case 2: Verify that the home URL is accessible

	* Positive case: Validates proper navigation to (https://opensource-demo.orangehrmlive.com) and asserts current URL
	* Negative case: Invalid URL navigation and displays error message

Test Case 3: Validate presence of login fields

	* Locates Username and Password else throws NoSuchElementException
	* Assert Username and Password is visible and interactable

Test Case 4: Checks visibility and clickability of main menu items after login in dashboard page[Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard]

	* Positive case: Validate menu items after login stored as dictionary are visible and interactable 
	* Negative case: Invalid access to menu items throws error message

Test Case 5:  Creating a new user and validate login using new user credentials

	* Positive case: Login as Admin and navigate to Admin menu and creates new user with valid details[User_role,Status,Employee_name, username, password, confirmpassword]
	* After new user creation,clicks logout and re-enters with new user credentials.
    * Negative case:Creates new user with invalid details like Employee name doesn't start with numbers.Displays error message.Also existing user cannot be created.
 
Test Case 6: Validate presence of the newly created user in the admin user list

	* Positive case: Navigates to Admin menu and validates new user is available in user list
	* Negative case: Navigates to Admin menu and validates not created user is available in user list

Test Case 7: Checks "Forgot Password" link functionality

	* Enters Login page and clicks "Forgot Password" link. 
	* Navigates to Forgot Password and enters username and reset link is sent to mail and displays message

Test Case 8: Validate the presence of menu items under “My Info”[Personal Details,Contact Details,Emergency Contacts,Job,Salary,Qualification,Memberships..]

	* Positive case: Validate menu items under “My Info” stored as dictionary are visible and interactable 
	* Negative case: Invalid access to menu items throws error message

Test Case 9: Assign leave to an employee and verify assignment on Leave List

	* Login as Admin and navigates to Leave menu and add entitlements(Employee_name,Leave_Type, Entitled_Days)
    * Assign leave to an employee by providing (Employee_name,Leave_Type,From_Date,To_Date) details
    * After successful leave assignment check leave is scheduled on the leave list

Test Case 10: Initiate a claim request and check the assigned claim on Claim list

	* Login as an Employee with new user credentials. Navigate to Claim menu.
	* Submit the claim (Event_Type,Currency_Type) and add expenses(Event_Type, Claim_Date, Claim_Amount)
	* After successful claim submission check claim of an employee is submitted on the claim list



**Instructions:**

1.Ensure Selenium,Python and any Browser(Chrome,Firefox,Edge) installed in your system. 

2.To create a virtual environment,

	>python -m venv venv
 
	>source venv/bin/activate(macOS)
 
	>venv\scripts\activate(Windows)

3.To install the dependencies,

	>pip install -r requirements.txt

4.To execute all the test files,

	>pytest -v -s Tests/

	>pytest pytest -v -s Tests/test_01_validate_login.py(for any specific file)

	>pytest pytest -v -s Tests/test_01_validate_login.py::test_validate_login(for specific method in a test file)



**To Generate HTML Report:**

To install pytest–html package

	>pip install pytest–html

To execute all the test files and generate html report,

	>pytest -v -s Tests/   --html=reports.html    --self-contained-html

To execute single file and generate html report,

	>pytest -v -s Tests/test_01_validate_login.py   --html=case01_report.html   --self-contained-html


**Screen Recording**:https://drive.google.com/file/d/1OzZ3XA--tmqTX2rZV14XwhWyQ-VXCugB/view?usp=sharing


