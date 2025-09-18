# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from Pages.base_page import BasePage


# InfoPage inherits BasePage. InfoPage contains locators and methods to interact with locators.
class InfoPage(BasePage):

    #LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # MyInfo icon locator
    MYINFO_ICON=(By.XPATH, '(//li[@class="oxd-main-menu-item-wrapper"])[6]//following-sibling::span')

    # MENU_ITEMS contains the menu items under My Info, and it is stored as Dictionary{Key:Value} pair
    My_Info_Menu={

    "PERSONAL_DETAILS":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[1]'),
    "CONTACT_DETAILS":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[2]'),
    "EMERGENCY_CONTACTS":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[3]'),
    "DEPENDENTS":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[4]'),
    "IMMIGRATION":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[5]'),
    "JOB":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[6]'),
    "SALARY":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[7]'),
    "REPORT_TO":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[8]'),
    "QUALIFICATIONS":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[9]'),
    "MEMEBERSHIPS":(By.XPATH,'(//div[@class="orangehrm-tabs-wrapper"])[10]')
    }


    # METHOD TO INTERACT WITH THE ELEMENTS
    # get_myinfo_menu_name() retrieves each menu name under My Info
    def get_myinfo_menu_name(self, name):
            return self.My_Info_Menu.get(name)

