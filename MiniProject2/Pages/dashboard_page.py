# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage


#DashboardPage inherits BasePage. DashboardPage contains locators and methods to interact with locators.
class DashboardPage(BasePage):

    # LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # MENU_ITEMS contains the menu items under Dashboard, and it is stored as Dictionary{Key:Value} pair
    MENU_ITEMS={

    "ADMIN_MENU":(By.XPATH,'//span[text()="Admin"]'),
    "PIM_MENU":(By.XPATH,'//span[text()="PIM"]'),
    "LEAVE_MENU":(By.XPATH,'//span[text()="Leave"]'),
    "TIME_MENU":(By.XPATH,'//span[text()="Time"]'),
    "RECRUITMENT_MENU":(By.XPATH,'//span[text()="Recruitment"]'),
    "MYINFO_MENU":(By.XPATH,'//span[text()="My Info"]'),
    "PERFORMANCE_MENU":(By.XPATH,'//span[text()="Performance"]'),
    "DASHBOARD_MENU":(By.XPATH,'//span[text()="Dashboard"]')
    }

    # METHOD TO INTERACT WITH THE ELEMENTS
    # get_menu_name() retrieves each menu name
    def get_menu_name(self,name):
        return self.MENU_ITEMS.get(name)
