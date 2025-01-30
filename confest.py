from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from Pages.login_page import LoginPage


class MainTestRunner:
    driver = None

    @classmethod
    def setup(cls):
        """ Initialize WebDriver and login once """
        if cls.driver is None:
            driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe"
            service = Service(driver_path)
            cls.driver = webdriver.Chrome(service=service)
            cls.driver.get("https://demoapi2.recomdo.ai/client-admin")
            cls.driver.maximize_window()

            # Perform login
            login_page = LoginPage(cls.driver)
            login_page.login("abans_client", "Porsche9000#")
            print("Login successful.")

    @classmethod
    def teardown(cls):
        """ Quit WebDriver after all tests """
        if cls.driver:
            cls.driver.quit()
            print("Browser closed.")

    @classmethod
    def get_driver(cls):
        """ Return the active WebDriver instance """
        return cls.driver
