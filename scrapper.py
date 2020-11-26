from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from name import item_name


driver = webdriver.Chrome()
driver.get(
    "https://store.kakaofriends.com/kr/products/category/subject?categorySeq=64&sort=createDatetime,desc"
)
req = driver.page_source
item_name(req)
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="mArticle"]/div[5]/div/span[2]').click()