from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    firstName = (By.CSS_SELECTOR, "#first-name")
    lastName = (By.CSS_SELECTOR, "#last-name")
    zipCode = (By.CSS_SELECTOR, "#postal-code")
    continueButton = (By.CSS_SELECTOR, "#continue")

    def getFirstName(self):
        return self.driver.find_element(*CheckoutPage.firstName)

    def getLastName(self):
        return self.driver.find_element(*CheckoutPage.lastName)

    def getZipCode(self):
        return self.driver.find_element(*CheckoutPage.zipCode)

    def getContinueButton(self):
        return self.driver.find_element(*CheckoutPage.continueButton)