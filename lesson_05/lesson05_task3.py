from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

searchbox = driver.find_element(By.TAG_NAME, "input")
searchbox.click()
searchbox.send_keys("Sky")
searchbox.clear()
searchbox.send_keys("Pro")

driver.quit()

sleep(10)