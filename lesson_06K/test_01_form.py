from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By


def test_fill_form():

    driver = webdriver.Edge(service=EdgeService(r"C:\Users\Виктория\OneDrive\Downloads\edgedriver_win64\msedgedriver.exe"))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, "[name = 'first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name ='last-name']").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("ул. Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    green_fields = driver.find_elements(By.CSS_SELECTOR, ".alert.py-2.alert-success")
    assert len(green_fields) == 9


test_fill_form()
