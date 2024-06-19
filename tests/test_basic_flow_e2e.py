import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

class TestBasicFlow(BaseClass):
    def test_basic_flow(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
