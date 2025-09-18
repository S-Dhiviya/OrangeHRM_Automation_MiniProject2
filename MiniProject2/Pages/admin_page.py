# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage
# Importing TimeoutException to raise when error occurs
from selenium.common.exceptions import TimeoutException


#AdminPage inherits BasePage. AdminPage contains locators and methods to be used in test cases.
class AdminPage(BasePage):

    #LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Admin menu,add user button locators
    ADMIN_MENU= (By.XPATH, '//span[text()="Admin"]')
    ADD_USER = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')

    # Add user Section locators
    # User role(Admin,ESS) and Status(Enabled/Disabled)
    USER_ROLE = (By.XPATH, '(//div[@class="oxd-select-text-input"])[1]')
    STATUS=(By.XPATH, '(//div[@class="oxd-select-text-input"])[2]')

    # Employee name,username,password locators
    EMPLOYEE_NAME=(By.XPATH,'//input[@placeholder="Type for hints..."]')
    USERNAME=(By.XPATH,'(//div//input[@class="oxd-input oxd-input--active"])[2]')
    PASSWORD=(By.XPATH,'(//input[@type="password"])[1]')

    # Confirm password and Submit button locators
    CONFIRM_PASSWORD=(By.XPATH,'(//input[@type="password"])[2]')
    SUBMIT=(By.XPATH,'//button[@type="submit"]')

    #User Management Section
    USERNAME_SECTION=(By.XPATH,'(//input[@class="oxd-input oxd-input--active"])[2]')
    SEARCH=(By.XPATH,'//button[@type="submit"] ')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # fill_name() to fill employee name,user role,status. These elements are dropdown list
    def fill_name(self, name):
        return (By.XPATH, f'//div[@role="listbox" and contains(normalize-space(), "{name}")]')


    # get_username_locator() to get username and check the list in user record
    def get_username_locator(self, username):
        return (By.XPATH, f'//div[@class="oxd-table-card"]//div[@role="cell"][2][normalize-space()="{username}"]')


    # add_user() creating new user by providing details of employee
    def add_user(self,user_role,status,employee_name,username,password,confirm_password):

        # Clicks ADD USER and selects the given user role
        self.click_element(self.ADD_USER)
        self.click_element(self.USER_ROLE)
        role_option=self.find_element(self.fill_name(user_role))
        self.click_element(role_option)

        # Selects the given status based on test file
        self.click_element(self.STATUS)
        status_option = self.find_element(self.fill_name(status))
        self.click_element(status_option)

        # Employee name can be chosen from the available names in the webpage
        self.find_element(self.EMPLOYEE_NAME).send_keys(employee_name)
        self.AUTOFILL_NAME = self.fill_name(employee_name)
        self.click_element(self.AUTOFILL_NAME)

        # Finds username,password and enters the data
        self.find_element(self.USERNAME).send_keys(username)
        self.find_element(self.PASSWORD).send_keys(password)
        self.find_element(self.CONFIRM_PASSWORD).send_keys(confirm_password)

        # Submits Add User and Successfully Saved appears
        self.click_element(self.SUBMIT)
        # After submission moves back to Admin page
        self.wait_for_element(self.ADD_USER)

    # validate_new_user() verifies the created username is present on user list
    def validate_new_user(self,username):

        # Clicks Admin and enters the username given in config.py and clicks search
        self.click_element(self.ADMIN_MENU)
        self.find_element(self.USERNAME_SECTION).send_keys(username)
        self.click_element(self.SEARCH)

        # Searches the table of records and returns the username else raises TimeoutException
        try:
            user_record = self.find_element(self.get_username_locator(username))
            return user_record.text
        except TimeoutException:
            return None










