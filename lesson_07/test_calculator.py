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
    page_object.set_time()
    as_is = page_object.set_values()
    to_be = page_object.wait_for_result()

    assert as_is == to_be
