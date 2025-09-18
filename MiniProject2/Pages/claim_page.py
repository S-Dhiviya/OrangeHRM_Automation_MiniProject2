# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from Pages.base_page import BasePage


# ClaimPage inherits BasePage. ClaimPage contains locators and methods to interact with locators.
class ClaimPage(BasePage):

    #LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Claim icon,Submit Claim locators
    CLAIM_ICON = (By.XPATH, '(//li[@class="oxd-main-menu-item-wrapper"])[11]//span')
    SUBMIT_CLAIM_ICON=(By.XPATH,'//a[text()="Submit Claim"]')

    # Submit Claim Section
    # Event and Currency Dropdown, Create button locators
    EVENT_DROPDOWN = (By.XPATH, '(//div[@class="oxd-select-text-input"])[1]')
    CURRENCY_DROPDOWN = (By.XPATH, '(//div[@class="oxd-select-text-input"])[2]')
    CREATE_BUTTON = (By.XPATH, '//button[@type="submit"]')

    #Adding Expenses Section
    # Add expenses,type,date,amount locators
    ADD_EXPENSES = (By.XPATH, '(//button[@class="oxd-button oxd-button--medium oxd-button--text"])[1]')
    EXPENSES_TYPE = (By.XPATH, '//div[@class="oxd-select-text-input"]')
    CLAIM_DATE = (By.XPATH, '//input[@placeholder="yyyy-dd-mm"]')
    CLAIM_AMOUNT = (By.XPATH, '//label[text()="Amount"]//following::input')

    # Save and submit claim locators
    SAVE_CLAIM = (By.XPATH, '//button[@type="submit"]')
    SUBMIT_CLAIM=(By.XPATH,'(//button[@type="button"])[10]')

    # Employee Claims Section locators
    EMPLOYEE_CLAIMS = (By.XPATH, '//a[text()="Employee Claims"]')
    EMPLOYEE_NAME = (By.XPATH, '//input[@placeholder="Type for hints..."]')
    SEARCH_CLAIM = (By.XPATH, '//button[@type="submit"]')
    CLAIM_CONTAINER = (By.XPATH, '//div[@class="oxd-table"]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # fill_name() is used to fill the employee name
    def fill_name(self, employee_name):
        return (By.XPATH, f'//div[@role="listbox" and contains(normalize-space(), "{employee_name}")]')


    # get_option() is used to choose Event and Currency type from the available options
    def get_option(self, option_name):
        return (By.XPATH, f'//div[@role="option"]/span[text()="{option_name}"]')


    #get_employee_name() is used to fill the employee name in Claim List
    def get_employee_name(self, employee_name):
        return (By.XPATH, f'//div[contains(text(),"{employee_name}")]')


    # submit_claim() submission of claim by filling event, currency type and clicks creates
    def submit_claim(self,event,currency):

        # Clicks Submit Claim icon and fills the event type(Accommodation,Medical,Travel)
        self.click_element(self.SUBMIT_CLAIM_ICON)
        self.find_element(self.EVENT_DROPDOWN).send_keys(event)
        self.EVENTS_CLAIM = self.get_option(event)
        self.click_element(self.EVENTS_CLAIM)

        # Fills the Currency type(Indian,Euro,Algerian,..)
        self.find_element(self.CURRENCY_DROPDOWN).send_keys(currency)
        self.CURRENCY_CLAIM = self.get_option(currency)
        self.click_element(self.CURRENCY_CLAIM)

        # Clicks Create and navigates to adding expenses
        self.click_element(self.CREATE_BUTTON)


    # adding_expenses() by filling expense type,claim date and amount
    def adding_expenses(self, expense_type, claim_date, claim_amount):

        # Clicks Add Expenses and a dialog box appears
        self.click_element(self.ADD_EXPENSES)

        # Fills the expenses type(Accommodation,Medical,Travel)
        self.find_element(self.EXPENSES_TYPE).send_keys(expense_type)
        self.EXPENSES = self.get_option(expense_type)
        self.click_element(self.EXPENSES)

        # Locates the claim date and amount and fills the value
        self.find_element(self.CLAIM_DATE).send_keys(claim_date)
        self.find_element(self.CLAIM_AMOUNT).send_keys(claim_amount)

        # Clicks Save and Submit Claim Button
        self.click_element(self.SAVE_CLAIM)
        self.click_element(self.SUBMIT_CLAIM)


    #  check_claim() is used to check whether claim is initiated or not to the employee
    def check_claim(self,employee_name):

        # Clicks Employee Claims icon
        self.click_element(self.EMPLOYEE_CLAIMS)

        # Fills the Employee Name
        self.find_element(self.EMPLOYEE_NAME).send_keys(employee_name)
        self.AUTOFILL_NAME = self.fill_name(employee_name)
        self.click_element(self.AUTOFILL_NAME)

        # Clicks Search and locates the employee record
        self.click_element(self.SEARCH_CLAIM)
        self.find_element(self.CLAIM_CONTAINER)

        # Finds the employee name in the claim list record
        locator = self.get_employee_name(employee_name)
        self.wait_for_element(locator)
        employee_record = self.find_element(locator)

        # If employee name is not found on claim list then it raises AssertionError
        if employee_record is None:
            raise AssertionError(f"Claim for employee '{employee_name}' not found.")
        return employee_record.text


