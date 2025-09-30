from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

user_name_searchbox = driver.find_element(By.ID, "username")
user_name_searchbox.send_keys("tomsmith")

password_searchbox = driver.find_element(By.ID, "password")
password_searchbox.send_keys("SuperSecretPassword!")

button_box = driver.find_element(By.TAG_NAME, "i")
button_box.click()

header = driver.find_element(By.ID, "flash")
print(header.text)

driver.quit()

sleep(10)