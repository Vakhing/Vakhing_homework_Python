import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    """
    Конструктор класса ProductsPage.
    """
    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 4)

    def add_to_cart(self, item_name: str):
        with allure.step("Добавление вещей в корзину"):
            item_xpath = f"//div[@class='inventory_item' and .//div[text()='{item_name}']]//button"
            self.wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath))).click()

    def add_products(self, items: list[str]):
        """
        Цикл, описывающий добавление товаров в корзину
        """
        for item in items:
            self.add_to_cart(item)

    def go_to_cart(self):
        with allure.step("Перейти в корзину"):
            self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()