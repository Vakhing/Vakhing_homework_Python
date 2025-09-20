from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 4)

    def fill_form(self, first_name: str, last_name: str, postal_code: str):

        fname_field = self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        fname_field.send_keys(first_name)

        lname_field = self._driver.find_element(By.ID, "last-name")
        lname_field.send_keys(last_name)

        postal_field = self._driver.find_element(By.ID, "postal-code")
        postal_field.send_keys(postal_code)

        self._driver.find_element(By.ID, "continue").click()

    def check_total_price(self):
        price = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return f'{price}'
