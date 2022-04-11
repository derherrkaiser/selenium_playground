from selenium import webdriver
from selenium.webdriver.common.by import By

#Den Chromedriver Pfad braucht man
#DRIVER_PATH = '/Users/jankaiser/PycharmProjects/selenium_playground/chromedriver'
#SAfari Driver macht es einfacher
driver = webdriver.Safari()
#hier die URL eingeben
driver.get('http://jankaiser.me')

#Schleife mit den Suchresultaten laufen lassen
listelements = driver.find_elements(By.TAG_NAME, "ul")
for hit in listelements:
    print(hit.text)
