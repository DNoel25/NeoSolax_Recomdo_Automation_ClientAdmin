from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from Pages.login_page import LoginPage

class BaseTest:
    driver = None

    @classmethod
    def setup_class(cls):
        driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe"
        service = Service(driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://demoapi1.recomdo.ai/client-admin")
        cls.driver.maximize_window()

        # Perform login once
        login_page = LoginPage(cls.driver)
        login_page.login("NewKiddoz", "Ratkiller400@")
        print("Login successful and setup complete.")

    @classmethod
    def teardown_class(cls):
        # Quit the driver once after all tests
        if cls.driver:
            cls.driver.quit()
            print("Browser closed and teardown complete.")
