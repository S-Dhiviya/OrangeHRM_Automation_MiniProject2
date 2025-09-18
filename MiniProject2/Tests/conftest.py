# conftest.py is used to define fixtures that can be reused across multiple test files.
#To import pytest modules
import pytest
#Importing Webdriver module from Selenium library
from selenium import webdriver
# Importing ChromeDriverManager and Service from Selenium library
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Fixtures are functions in pytest used to prepare environment for test execution.Scope by default it is "function".
#Scope="class" defines set up and tear down for each class
@pytest.fixture(scope="class")
# request is a built-in pytest fixture that gives you access to the test context. setup is fixture name
def setup(request):

    # Creates Webdriver instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # get() navigates to orange hrm portal and opens in Chrome Browser
    driver.get("https://opensource-demo.orangehrmlive.com")
    #This is used to view the Chrome Browser in maximized window
    driver.maximize_window()

    # request.cls.driver = driver lets self.driver to be used inside test class methods.
    request.cls.driver = driver
    # yield is used for setup and teardown logic
    yield
    # Closes the Chrome Window and ends the WebDriver session
    driver.quit()