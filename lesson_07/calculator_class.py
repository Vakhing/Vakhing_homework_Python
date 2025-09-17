from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 45)

    def set_time(self):
        input_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys("45")

    def set_values(self):

        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        field_with_values = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        print(field_with_values)
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait_for_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result_field = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        print(result_field)
