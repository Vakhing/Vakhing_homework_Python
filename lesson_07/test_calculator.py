import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator_class import Calculator


@pytest.fixture
def browser():

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window() 
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield browser
    browser.quit()


def test_calc(browser):
    page_object = Calculator(browser)
    page_object.set_delay(45)
    page_object.click_button("7")
    page_object.click_button("+")
    page_object.click_button("8")
    page_object.click_button("=")
    page_object.wait_for_result("15")

    result = page_object.get_display_value()
    assert result == '15'
