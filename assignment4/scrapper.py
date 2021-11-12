import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://coinmarketcap.com/currencies/bitcoin/news/'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver.exe', options=options)
driver.get(url)
button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/div/main/button')
for i in range(4):
    button.click()
    time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
divs = soup.find('div', {'class': 'wav26n-1 gWmJSZ'})
tags = divs.find_all('a')

counter = 0
for i in tags:
    print(i.text)
    print('----------------------------------------------')
    counter = counter + 1
    if counter == 20:
        break

driver.close()
