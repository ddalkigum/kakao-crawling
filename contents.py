import re
import requests
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

link_list = []


def no_space(text):
    """

    i hate blank !!
    This function can help you from blank 

    """
    text1 = re.sub("&nbsp;| \n|\t|\r", "", text)
    text2 = re.sub("\n\n", "", text1)
    return text2


# driver = webdriver.Chrome()
# driver.get("https://store.kakaofriends.com/kr/index")
# driver.implicitly_wait(2)
"""
Top == Public use

"""
# for number in category_number:
#    driver.find_element_by_xpath('//*[@id="innerHead"]/div/button[2]').click()
#    time.sleep(1.5)
#    driver.find_element_by_xpath("/html/body/div[6]/div/div/div/ul/li[4]").click()
#    driver.implicitly_wait(2)
#    driver.find_element_by_xpath(
#        f"/html/body/div[6]/div/div/div/ul/li[4]/ul/li[{number}]"
#    ).click()
#
#
#    print(f"{category_name[number-3]} copy...")
#    driver.back()
#    driver.implicitly_wait(2)
"""
Top == function part 
Bottom == Test part
 
"""
# driver.find_element_by_xpath('//*[@id="innerHead"]/div/button[2]').click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("/html/body/div[6]/div/div/div/ul/li[4]").click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div/ul/li[4]/ul/li[3]").click()
# page_source = driver.page_source
#
# soup = BeautifulSoup(page_source, "html.parser")
# item_container = soup.find("div", {"class", "cont_list"})
# item_box = item_container.find("ul")
# item_list = item_box.find_all("li")
# for item in item_list:
#    item_link = item.find("a", {"class", "kGHQwh"})["href"]
#    link_list.append(item_link)
# print(link_list)

# for url in link_list:
#    current_url = f"https://store.kakaofriends.com{url}"

driver = webdriver.Chrome()

driver.get("https://store.kakaofriends.com/kr/products/7531")
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
detail_container = soup.find("div", {"class", "ffhpwj"})
detail_text = detail_container.get_text()
clean_text = no_space(detail_text)
print(clean_text)


//*[@id="mArticle"]/div[4]/ul/li[1]/a
//*[@id="mArticle"]/div[4]/ul/li[2]/a
//*[@id="mArticle"]/div[4]/ul/li[5]/a