from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser):
        self._driver = browser

    def check_products(self):
        item_1 = self._driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']").text
        item_2 = self._driver.find_element(By.XPATH, "//*[text()='Sauce Labs Bolt T-Shirt']").text
        item_3 = self._driver.find_element(By.XPATH, "//*[text()='Sauce Labs Onesie']").text
        return f"{item_1}/{item_2}/{item_3}"                              

    def push_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()