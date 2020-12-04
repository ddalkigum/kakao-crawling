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


def write_csv(number, args, kwargs):
    """
    wrtie csv file
    need fix( save )
    """
    file = open(f"detail_page{number}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow([*args, *kwargs])


def get_lastpage(src):
    """
    get last page from each category
    """
    time.sleep(1)
    soup = BeautifulSoup(src, "html.parser")
    pagination = soup.find("div", {"class", "list__ListFooter-sc-1wem0pv-8"})
    last_page = pagination.find_all("span", {"class", "hcZclE"})[-1].get_text()
    return last_page


def get_detail_contents(src):
    """
    get detail description and photo
    """
    image_arr = []
    text_arr = []
    soup = BeautifulSoup(src, "html.parser")
    detail_container = soup.find("div", {"class", "ffhpwj"})
    detail_text = detail_container.find_all("div", {"class", "byMKtG"})

    for t in detail_text:
        text = t.get_text()
        clean_text = no_space(text)
        text_arr.append(clean_text)
    image_list = detail_container.find_all("img")
    for image in image_list:
        image_arr.append(image["src"])
    return image_arr, text_arr


# driver = webdriver.Chrome()
# driver.get("https://store.kakaofriends.com/kr/index")
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//*[@id="innerHead"]/div/button[2]').click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("/html/body/div[6]/div/div/div/ul/li[4]").click()
# time.sleep(1)
# driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div/ul/li[4]/ul/li[3]").click()
# page_src = driver.page_source

driver = webdriver.Chrome()
driver.get(
    "https://store.kakaofriends.com/kr/products/category/subject?categorySeq=64&sort=createDatetime,desc"
)

page_src = driver.page_source
page_number = int(get_lastpage(page_src))
for i in range(1, page_number):
    if i == 1:
        print("page 1 scrapping ...")
        for j in range(1, 40):
            driver.implicitly_wait(2)
            driver.find_element_by_xpath(
                f'//*[@id="mArticle"]/div[4]/ul/li[{j}]/a'
            ).click()
            detail_src = driver.page_source
            get_detail_contents(detail_src, i)
            driver.back()
    else:
        driver.implicitly_wait(2)
        print(f"page {i-1} scrapping... ")
        next_page = driver.find_element_by_xpath(
            f'//*[@id="mArticle"]/div[5]/div/div[{i}]'
        ).click()
        for j in range(1, 40):
            driver.implicitly_wait(2)
            driver.find_element_by_xpath(
                f'//*[@id="mArticle"]/div[4]/ul/li[{j}]/a'
            ).click()
            detail_src = driver.page_source
            get_detail_contents(detail_src)
            driver.back()


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

# soup = BeautifulSoup(page_source, "html.parser")
# item_container = soup.find("div", {"class", "cont_list"})
# item_box = item_container.find("ul")
# item_list = item_box.find_all("li")
# for item in item_list:
#   item_link = item.find("a", {"class", "kGHQwh"})["href"]
#   link_list.append(item_link)
# print(link_list)
# for url in link_list:
#   current_url = f"https://store.kakaofriends.com{url}"
