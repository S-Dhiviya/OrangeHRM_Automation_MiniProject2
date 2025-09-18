# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from Pages.base_page import BasePage


# LoginPage inherits BasePage. LoginPage contains locators and methods to interact with locators.
class LoginPage(BasePage):

    # LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Username and password box,login button locator using XPATH
    USERNAME_INPUT = (By.XPATH, '//input[@name="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')

    # Profile menu and logout button locator
    PROFILE_MENU=(By.XPATH,'//span[@class="oxd-userdropdown-tab"]')
    LOGOUT_BUTTON=(By.XPATH,'//span[@class="oxd-userdropdown-tab"]//following::li[4]')

    # Forgot password, username locator
    FORGOT_PASSWORD=(By.XPATH,'//div[@class="orangehrm-login-forgot"]')
    REGISTERED_USERNAME=(By.XPATH,'//input[@class="oxd-input oxd-input--active"]')

    # Reset Password Section
    RESET_PASSWORD=(By.XPATH,'//button[@type="submit"]')
    RESET_CONTAINER=(By.XPATH,'//div[@class="orangehrm-card-container"]')
    RESET_MESSAGE=(By.XPATH,'(//p[@class="oxd-text oxd-text--p"])[1]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # login() is used to find username and password and enter the valid data and to click login button
    def login(self, username, password):

        # self.USERNAME_INPUT,self.PASSWORD_INPUT are locators. username,password are the text to be entered.
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)

        #Clicks the login button after locating the self.LOGIN_BUTTON
        self.click_element(self.LOGIN_BUTTON)


    # login_error_message() prints error message if user enters invalid data
    def login_error_message(self):
        return "Invalid login credentials"


    # logout() locates the profile menu and clicks logout under dashboard after login
    def logout(self):
        self.click_element(self.PROFILE_MENU)
        self.click_element(self.LOGOUT_BUTTON)


    # forgot_password() clicks forgot password and enters username and link to reset password is sent to email
    def forgot_password(self,username):

        # Clicks forgot password link and enters the username and clicks reset password
        self.click_element(self.FORGOT_PASSWORD)
        self.find_element(self.REGISTERED_USERNAME).send_keys(username)
        self.click_element(self.RESET_PASSWORD)

        # Navigates to reset dialog box and mail is sent to user
        self.find_element(self.RESET_CONTAINER)
        self.wait_for_text(self.RESET_MESSAGE)
        message=self.find_element(self.RESET_MESSAGE)
        return message.text


