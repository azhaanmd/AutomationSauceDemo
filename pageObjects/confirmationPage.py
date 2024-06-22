from selenium.webdriver.common.by import By

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    completeText  = (By.CSS_SELECTOR, ".complete-text")

    def getCompleteText(self):
        return self.driver.find_element(*ConfirmationPage.completeText)