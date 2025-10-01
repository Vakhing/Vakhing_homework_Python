import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Vakhing_homework_Python.lesson_10.Pages.calculator_class import Calculator


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    with allure.step("Открытие страницы калькулятора"):
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield browser
    browser.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "с различными операциями")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(browser):
    page_object = Calculator(browser)
    with allure.step("Установка задержки {seconds} секунд"):
        page_object.set_delay(45)
    with allure.step("Нажатие кнопок"):
        page_object.click_button("7")
        page_object.click_button("+")
        page_object.click_button("8")
        page_object.click_button("=")
    with allure.step("Ожидание результата"):
        page_object.wait_for_result("15")
    with allure.step("Получение результата с экрана калькулятора"):
        result = page_object.get_display_value()
        assert result == '15'
