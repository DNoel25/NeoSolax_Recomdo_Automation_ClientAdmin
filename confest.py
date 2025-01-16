import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path= r"C:\Users\neosolax\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    request.cls.driver = driver
    yield
    driver.quit()

