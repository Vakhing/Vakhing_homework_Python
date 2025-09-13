from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

button_login = driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

driver.find_element(By.ID, "checkout").click()
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Black")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Cat")

index = driver.find_element(By.ID, "postal-code")
index.send_keys("707")

driver.find_element(By.ID, "continue").click()

price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
print(price)

driver.quit()
