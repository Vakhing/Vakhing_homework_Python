import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Конструктор класса CartPage.
    """
    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 4)

    def get_products(self) -> list[str]:
        with allure.step("Отображение списка добавленных товаров"):
            items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
            return [item.text for item in items]

    def push_checkout(self):
        with allure.step("Нажатие кнопки оформления заказа"):
            self._driver.find_element(By.ID, "checkout").click()