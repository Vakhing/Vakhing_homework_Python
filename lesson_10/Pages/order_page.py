import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    """
    Конструктор класса OrderPage.
    """
    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 4)

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполнение формы покупателя
        """
        with allure.step("Заполнение формы: ввести {first_name} имя"):
            fname_field = self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
            fname_field.send_keys(first_name)

        with allure.step("Заполнение формы: ввести {last_name} имя"):
            lname_field = self._driver.find_element(By.ID, "last-name")
            lname_field.send_keys(last_name)

        with allure.step("Заполнение формы: ввести {postal_code} почтовый индекс"):
            postal_field = self._driver.find_element(By.ID, "postal-code")
            postal_field.send_keys(postal_code)

        with allure.step("Нажать на кнопку подтверждения формы покупателя"):
            self._driver.find_element(By.ID, "continue").click()

    def check_total_price(self):
        """
        Проверка итоговой цены.
        """
        price: str = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return f'{price}'