import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from main_shop_page import MainShopPage
from products_page import ProductsPage
from cart_page import CartPage
from order_page import OrderPage


@pytest.fixture
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    browser.get('https://www.saucedemo.com/')
    yield browser
    browser.quit()


def test_internet_shop(browser):
    main_shop_page = MainShopPage(browser)
    main_shop_page.authorization()

    products_page = ProductsPage(browser)
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    products_page.add_products(items_to_add)
    products_page.go_to_cart()

    cart_page = CartPage(browser)
    items_in_cart = cart_page.get_products()
    assert set(items_in_cart) == set(items_to_add), "Состав корзины не совпадает с ожидаемым"
    cart_page.push_checkout()

    order_page = OrderPage(browser)
    order_page.fill_form("Black", "Cat", "707")
    
    actual_price = order_page.check_total_price()
    expected_price = "Total: $58.29"
    assert actual_price == expected_price
