from time import sleep

import pytest
from utilities.BaseClass import BaseClass
from pageObjects.loginPage import LoginPage
from pageObjects.inventoryPage import InventoryPage
from pageObjects.cartPage import CartPage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.overviewPage import OverviewPage
from pageObjects.confirmationPage import ConfirmationPage

class TestBasicFlow(BaseClass):
    def test_basic_flow(self):
        loginPage = LoginPage(self.driver)
        loginPage.fillLoginInfo("standard_user", "secret_sauce")
        loginPage.getLoginButton().click()

        #select an element to add to cart
        inventoryPage = InventoryPage(self.driver)
        inventoryPage.getAddToCartButton().click()
        inventoryPage.getShoppingCartButton().click()

        #proceed to checkout
        cartPage = CartPage(self.driver)
        cartPage.getCheckoutButton().click()

        #fill checkout form
        checkoutPage = CheckoutPage(self.driver)
        checkoutPage.getFirstName().send_keys("Test")
        checkoutPage.getLastName().send_keys("Test2")
        checkoutPage.getZipCode().send_keys("Test3")
        checkoutPage.getContinueButton().click()

        #overview details
        overviewPage = OverviewPage(self.driver)
        overviewPage.getFinishButton().click()

        #confirmation message validation
        confirmationPage = ConfirmationPage(self.driver)
        confirmationMessage = confirmationPage.getCompleteText().text
        assert "dispatched" in confirmationMessage


        sleep(3)
