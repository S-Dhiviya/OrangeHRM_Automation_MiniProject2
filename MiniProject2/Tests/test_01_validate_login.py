# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing CSV and OS for utilizing CSV file[CSV File is stored under Data folder]
import csv
import os
# Importing Login page to use methods in it.
from Pages.login_page import LoginPage
# To utilize datetime functionality
from datetime import datetime


# get_login_data() locates the CSV file and reads the data
def get_login_data():
    login_data = []
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the correct path to the CSV file
    data_file = os.path.join(current_dir, '../Data', 'login_data-1.csv')


    # Read the CSV file
    with open(data_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Ensure each row is treated as a dictionary
            username = row['Username']
            password = row['Password']
            login_data.append((username, password))
    return login_data


# update_csv() reads the CSV file and updates the result in the CSV file.
def update_csv(username,password,result):
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the correct path to the CSV file
    data_file = os.path.join(current_dir, '../Data', 'login_data-1.csv')
    updated_rows = []


    # Read the CSV file
    with open(data_file, newline='') as file:
        reader = csv.DictReader(file)
        #fieldnames contains list of column headers in CSV file(like Username,Password,Name of Tester)
        fieldnames = reader.fieldnames

        # Loops through each row data
        for row in reader:

            # Checks if username and password match between CSV file and login_data list in get_login_data()
            if row['Username'].strip().lower()==username.strip().lower() and row['Password'].strip().lower()==password.strip().lower():
                # Evaluates the current date and stores in 'Date' column
                row['Date'] = datetime.now().strftime("%Y-%m-%d")
                # Evaluates the result and stores in 'Test Result' column
                row['Test Result']=result

            #updated_rows contains updated data of Date and Test Result of all the matching data of username and password from CSV
            updated_rows.append(row)


    # To write back all the updated data to CSV file
    with open(data_file, 'w', newline='') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        # To write the header row
        writer.writeheader()
        # Writes each rows data
        writer.writerows(updated_rows)


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLogin:

    # Parameters username and password are used in test function and get_login_data() method is called.
    # This runs multiple times with different sets of username and password
    @pytest.mark.parametrize("username, password", get_login_data())
    # test_validate_login() opens the login and checks valid data and updates the result as PASS/FAIL in CSV
    def test_validate_login(self, username, password):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # Calls login method from LoginPage
        login_page.login(username, password)

        # After entering valid data it should navigate to Dashboard Page
        dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        login_page.wait_for_url(dashboard_url)
        current_url = login_page.get_current_url()

        # If URL matches then updates the result as Passed in CSV file and clicks logout in webpage
        if dashboard_url in current_url:
            update_csv(username, password, "Passed")
            login_page.logout()

        # Else updates the result as Failed in CSV file
        else:
            update_csv(username, password, "Failed")
            assert False, f"Login failed for username: {username}"
            print("Invalid Credentials")


