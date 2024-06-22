from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    addToCartButton = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    shoppingCartLink = (By.CSS_SELECTOR, ".shopping_cart_link")

    def getAddToCartButton(self):
        return self.driver.find_element(*InventoryPage.addToCartButton)

    def getShoppingCartButton(self):
        return self.driver.find_element(*InventoryPage.shoppingCartLink)