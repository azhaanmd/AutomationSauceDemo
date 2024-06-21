import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None


@pytest.fixture(scope="class")
def browserSetup(request):
    global driver
    chrome_service_obj = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service_obj)
    driver.get("https://www.saucedemo.com")
    request.cls.driver = driver
