from selenium.webdriver.common.by import By

class OverviewPage:
    def __init__(self, driver):
        self.driver = driver

    finishButton  = (By.CSS_SELECTOR, "#finish")

    def getFinishButton(self):
        return self.driver.find_element(*OverviewPage.finishButton)