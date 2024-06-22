from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutButton = (By.CSS_SELECTOR, "#checkout")

    def getCheckoutButton(self):
        return self.driver.find_element(*CartPage.checkoutButton)