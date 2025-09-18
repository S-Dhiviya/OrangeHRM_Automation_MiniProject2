# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# Importing Keys to use delete and select all
from selenium.webdriver.common.keys import Keys
# ActionChains for click and move to element
from selenium.webdriver.common.action_chains import ActionChains
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from Pages.base_page import BasePage


# LeavePage inherits BasePage. LeavePage contains locators and methods to interact with locators.
class LeavePage(BasePage):

    #LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Leave menu locator using XPATH
    LEAVE_MENU = (By.XPATH, '(//li[@class="oxd-main-menu-item-wrapper"])[3]//following-sibling::span')

    # Entitlement Section locator to add leave days to an employee
    ENTITLEMENTS=(By.XPATH,'//span[contains(text(),"Entitlements")]')
    ADD_ENTITLEMENTS= (By.XPATH,'(//ul[@class ="oxd-dropdown-menu"]//li)[1]')
    ENTITLEMENT_DAYS=(By.XPATH,'(//input[@class="oxd-input oxd-input--active"])[2]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"] ')
    CONFIRM_BUTTON=(By.XPATH,'(//button[@type="button"])[6]')

    # Assigning leave Section
    # Assign Leave,Employee name,Leave type locators
    ASSIGN_LEAVE = (By.XPATH, '(//li[@class="oxd-topbar-body-nav-tab"])[3]')
    EMPLOYEE_NAME = (By.XPATH, '//input[@placeholder="Type for hints..."]')
    LEAVE_TYPE = (By.XPATH, '//div[@class="oxd-select-text-input"]')

    # From and To Date locators
    FROM_LABEL = (By.XPATH, '//label[text()="From Date"]')
    TO_LABEL = (By.XPATH, '//label[text()="To Date"]')
    FROM_DATE = (By.XPATH, '(//input[@placeholder="yyyy-dd-mm"])[1]')
    TO_DATE = (By.XPATH, '(//input[@placeholder="yyyy-dd-mm"])[2]')

    # Comments,Assign and OK button locators
    COMMENTS = (By.XPATH, '//textarea[@class="oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical"]')
    ASSIGN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.oxd-toast-content")
    OK_BUTTON=(By.XPATH,'//button[normalize-space()="Ok"]')

    # Leave List Section locators
    LEAVE_LIST=(By.XPATH, '//a[text()="Leave List"]')
    LEAVE_STATUS=(By.XPATH,'(//div[@class="oxd-multiselect-wrapper"]//child::div)[2]')
    SEARCH = (By.XPATH, '//button[@type="submit"] ')
    LEAVE_CONTAINER = (By.XPATH, '//div[@class="oxd-table"]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # fill_name() is used to fill the employee name
    def fill_name(self,employee_name):
        return (By.XPATH, f'//div[@role="listbox"]//span[contains(text(), "{employee_name}")]')


    # get_option() is used to choose Leave Type from the available options
    def get_option(self, option_name):
        return (By.XPATH, f'//div[@role="option"]//span[text()="{option_name}"]')


    # fill_leave_status() is used to choose Leave Status from the available options
    def fill_leave_status(self, leave_status):
        return (By.XPATH, f'//div[@role="listbox"]//span[text()="{leave_status}"]')


    #get_employee_name() is used to fill the employee name in Leave List
    def get_employee_name(self, employee_name):
        return (By.XPATH, f'//div[contains(text(),"{employee_name}")]')


    # add_entitlements() assign leave days to an employee
    # Shows Leave Balance of an employee while assigning leave
    def add_entitlements(self,employee_name,leave_type,entitled_days):

        # Clicks Entitlement icon and selects Add_Entitlements
        self.click_element(self.ENTITLEMENTS)
        self.click_element(self.ADD_ENTITLEMENTS)

        # Fills the employee name and selects the available name
        self.find_element(self.EMPLOYEE_NAME).send_keys(employee_name)
        self.AUTOFILL_NAME = self.fill_name(employee_name)
        self.click_element(self.AUTOFILL_NAME)

        # Fills the leave type and chooses the leave type
        self.find_element(self.LEAVE_TYPE).send_keys(leave_type)
        self.AUTOFILL_LEAVE_TYPE = self.get_option(leave_type)
        self.click_element(self.AUTOFILL_LEAVE_TYPE)

        # Enters the Entitled days and Clicks Save and Confirm Button
        self.find_element(self.ENTITLEMENT_DAYS).send_keys(entitled_days)
        self.click_element(self.SAVE_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)


    # assigning_leave() used to assign leave by including dates and leave_type
    def assigning_leave(self,employee_name,leave_type,from_date,to_date):

        # Fills and selects the available employee name
        self.find_element(self.EMPLOYEE_NAME).send_keys(employee_name)
        self.AUTOFILL_NAME=self.fill_name(employee_name)
        self.click_element(self.AUTOFILL_NAME)

        # Fills and selects the Leave Type
        self.find_element(self.LEAVE_TYPE).send_keys(leave_type)
        self.AUTOFILL_LEAVE_TYPE=self.get_option(leave_type)
        self.click_element(self.AUTOFILL_LEAVE_TYPE)

        # Locates and Selects From Date
        self.find_element(self.FROM_LABEL)
        from_date_input = self.find_element(self.FROM_DATE)
        from_date_input.click()
        from_date_input.send_keys(from_date)

        # Locates and Selects To Date using ActionChains
        actions=ActionChains(self.driver)
        self.find_element(self.TO_LABEL)
        to_date_input=self.find_element(self.TO_DATE)

        # Since from date is filled in both fields action chains is used to delete the value
        # Fills the To Date
        to_date_input.send_keys(Keys.COMMAND + "a")
        to_date_input.send_keys(Keys.DELETE)
        actions.move_to_element(to_date_input).click().send_keys(to_date).perform()

        # Locates and Click the Assign Button
        self.find_element(self.COMMENTS)
        self.find_element(self.ASSIGN_BUTTON)
        self.click_element(self.ASSIGN_BUTTON)
        self.wait_for_text(self.SUCCESS_MESSAGE)
        # Optional:time.sleep(2)


        # Optional if there is insufficient balance days
        # self.wait_for_element(self.OK_BUTTON)
        # self.click_element(self.OK_BUTTON)


    # check_leave_list() navigates to Leave List menu and checks the Leave is assigned or not
    def check_leave_list(self,employee_name,leave_status):

        # Navigates to Leave List menu
        self.click_element(self.LEAVE_MENU)
        self.click_element(self.LEAVE_LIST)

        # Fills the Leave Status
        self.click_element(self.LEAVE_STATUS)
        self.AUTOFILL_STATUS = self.fill_leave_status(leave_status)
        self.click_element(self.AUTOFILL_STATUS)

        # Fills the Employee Name and Searches the Records
        self.find_element(self.EMPLOYEE_NAME).send_keys(employee_name)
        self.AUTOFILL_NAME=self.fill_name(employee_name)
        self.click_element(self.AUTOFILL_NAME)
        self.click_element(self.SEARCH)

        # Checks whether employee name is present in the leave list record
        self.find_element(self.LEAVE_CONTAINER)
        locator = self.get_employee_name(employee_name)
        self.wait_for_element(locator)
        employee_record = self.find_element(locator)

        # If employee name is not found on leave list then it raises AssertionError
        if employee_record is None:
            raise AssertionError(f"Leave to employee '{employee_name}' not assigned.")
        return employee_record.text










