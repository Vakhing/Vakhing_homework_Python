import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Vakhing_homework_Python.lesson_10.Pages.main_shop_page import MainShopPage
from Vakhing_homework_Python.lesson_10.Pages.products_page import ProductsPage
from Vakhing_homework_Python.lesson_10.Pages.cart_page import CartPage
from Vakhing_homework_Python.lesson_10.Pages.order_page import OrderPage


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    with allure.step("Открытие страницы интернет-магазина"):
        browser.get('https://www.saucedemo.com/')
    yield browser
    browser.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет корректность работы интернет-магазина")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_internet_shop(browser):
    main_shop_page = MainShopPage(browser)
    with allure.step("Авторизация"):
        main_shop_page.authorization()

    products_page = ProductsPage(browser)
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    with allure.step("Добавление вещей в корзину"):
        products_page.add_products(items_to_add)
    with allure.step("Переход в корзину"):
        products_page.go_to_cart()

    cart_page = CartPage(browser)
    with allure.step("Получаем список товаров в корзине и сверяем его с ожидаемыми товарами"):
        items_in_cart = cart_page.get_products()
        assert set(items_in_cart) == set(items_to_add), "Состав корзины не совпадает с ожидаемым"
    with allure.step("Нажатие кнопки оформления заказа"):
        cart_page.push_checkout()

    order_page = OrderPage(browser)
    with allure.step("Заполнение формы покупателя"):
        order_page.fill_form("Black", "Cat", "707")

    with allure.step("Сравнение полученной итоговой цены товаров и ожидаемой"):
        actual_price = order_page.check_total_price()
        expected_price = "Total: $58.29"
        assert actual_price == expected_price
