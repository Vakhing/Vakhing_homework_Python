from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 4)

    def authorization(self, username: str = "standard_user", password: str = "secret_sauce"):

        user_field = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        user_field.send_keys(username)

        pass_field = self._driver.find_element(By.ID, "password")
        pass_field.send_keys(password)

        self._driver.find_element(By.ID, "login-button").click()
