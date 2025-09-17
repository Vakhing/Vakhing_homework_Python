from selenium.webdriver.common.by import By


class MainShopPage:
    def __init__(self, browser):
        self._driver = browser

    def authorization(self):
        username = self._driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = self._driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        self._driver.find_element(By.ID, "login-button").click()
