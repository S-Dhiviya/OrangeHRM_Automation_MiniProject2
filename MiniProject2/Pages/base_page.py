# Automation Testing of HR Management Web Application
# BASE PAGE FOR ORANGE HRM PORTAL
# Page classes represents the webpage.
# Importing WebDriverWait is used to explicitly wait for elements to appear, disappear,clickable
# Explicit wait is used to wait for specific condition to occur before proceeding to next.
from selenium.webdriver.support.ui import WebDriverWait
# Importing expected_conditions like url contains,presence of element,visibility of element
from selenium.webdriver.support import expected_conditions as EC
#Importing exceptions to raise when error occurs
from selenium.common.exceptions import TimeoutException,NoSuchElementException


# BasePage class contains methods to click,find,enter text in the element and get the URL,title of page
class BasePage:


    # Constructor method used to interact with Selenium Webdriver. Driver is passed from 'setup' code
    def __init__(self, driver):
        self.driver = driver


    # Finding the element using the locator with timeout of 10 seconds using explicit wait
    def find_element(self, locator, timeout=10):
        # Explicit wait until the element is enabled else raises TimeOutException
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Timeout: Element with locator {locator} not found")


    # Find and Click the element using the locator with timeout of 15 seconds using explicit wait
    def click_element(self, locator, timeout=15):
        # This uses find_element method to locate the element and then clicks it.
        element = self.find_element(locator, timeout)
        element.click()


    # Find and Enter the text using the locator with timeout of 15 seconds using explicit wait
    def enter_text(self, locator, text, timeout=15):
        # This uses find_element method to locate the element and then types the given text.
        element = self.find_element(locator, timeout)
        # Clears the element before typing the text
        # element.clear()
        element.send_keys(text)


    # Waits for any element to load with timeout of 20 seconds using explicit wait
    def wait_for_element(self, locator, timeout=20):
        # Explicit wait until the element is located else raises NoSuchElementException
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            print("No such element is found")


    # Waits for URL navigation with timeout of 10 seconds using explicit wait
    def wait_for_url(self, url, timeout=10):
        # Raises AssertionError, if correct URL is not found
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(url))
        except AssertionError:
            print("Provided URL is incorrect")


    # Waits for text to appear with timeout of 30 seconds using explicit wait
    def wait_for_text(self,locator,timeout=30):
        # Raises AssertionError, if correct text message is not found
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except AssertionError:
            print("Text message is not found")


    # get_current_url returns the current page URL
    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            print(f"Failed to get current URL of the page:{e}")


    # get_title returns the page title
    def get_title(self):
        try:
            return self.driver.title
        except Exception as e:
            print(f"Failed to get current title of the page:{e}")



