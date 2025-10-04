from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    """
    Конструктор класса Calculator.
    """
    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 45)

    def set_delay(self, seconds: int):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        """
        input_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys(str(seconds))

    def click_button(self, value: str):
        """
        Нажимает на кнопку калькулятора.
        """
        self._driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def get_display_value(self) -> int:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        """
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text

    def wait_for_result(self, expected_result: str):
        """
        Возвращает текущий результат с экрана калькулятора.
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_result))