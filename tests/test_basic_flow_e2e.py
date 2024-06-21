from time import sleep

import pytest
from utilities.BaseClass import BaseClass
from pageObjects.loginPage import LoginPage

class TestBasicFlow(BaseClass):
    def test_basic_flow(self):
        loginPage = LoginPage(self.driver)
        loginPage.fillLoginInfo("standard_user", "secret_sauce")
        loginPage.getLoginButton().click()

        sleep(3)
