from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # locators and webelements
    username = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    loginButton = (By.CSS_SELECTOR, "#login-button")

    def getUserName(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def fillLoginInfo(self, name="", password=""):
        self.getUserName().send_keys(name)
        self.getPassword().send_keys(password)
        return

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.loginButton)
