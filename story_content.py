import re
import requests
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

kakao = []


driver = webdriver.Chrome()
driver.get("https://store.kakaofriends.com/kr/index")
driver.implicitly_wait(3)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")

driver.find_element_by_xpath(
    '//*[@id="mArticle"]/main/div[2]/article[3]/section[2]/div[4]/div/button'
).click()
driver.implicitly_wait(3)
driver.find_element_by_xpath(
    '//*[@id="mArticle"]/main/div[2]/article[11]/section[2]/div[4]/div/button'
).click()