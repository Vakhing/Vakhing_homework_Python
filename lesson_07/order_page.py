from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, browser):
        self._driver = browser

    def fill_form(self):
        first_name = self._driver.find_element(By.ID, "first-name")
        first_name.send_keys("Black")

        last_name = self._driver.find_element(By.ID, "last-name")
        last_name.send_keys("Cat")

        index = self._driver.find_element(By.ID, "postal-code")
        index.send_keys("707")

        self._driver.find_element(By.ID, "continue").click()

    def check_total_price(self):
        price = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return f'{price}'
