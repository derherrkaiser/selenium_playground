from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVER_PATH = '/Users/jankaiser/PycharmProjects/selenium_playground/chromedriver'
driver = webdriver.Safari()
driver.get('http://jankaiser.me')

h1 = driver.find_elements(By.TAG_NAME, "li")
for hit in h1:
    print(hit.text)
