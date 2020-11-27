import requests
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver


pagination_number = [2, 3, 4, 5, 6, 7, 8, 9]
category_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
category_name = [
    "toy",
    "living",
    "stuff",
    "no",
    "cloths",
    "pajama",
    "travel",
    "tech",
    "accesory",
    "food",
]

driver = webdriver.Chrome()
driver.get("https://store.kakaofriends.com/kr/index")
driver.implicitly_wait(3)
item_lists = []

driver.find_element_by_xpath('//*[@id="innerHead"]/div/button[2]').click()
time.sleep(1.5)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div/ul/li[4]").click()
driver.implicitly_wait(2)
driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div/ul/li[4]/ul/li[3]").click()


def get_current_item(r):
    soup = BeautifulSoup(r, "html.parser")
    container = soup.find("div", {"class", "cont_list"})
    box = container.find("ul")
    item_list = box.find_all("li")
    for item in item_list:
        item_set = item.find("a")
        item_price = (
            item_set.find("p", {"class", "item__Price-sc-5t2pho-3"})
            .get_text()
            .strip("금액")
        )
        item_name = item_set.find("p").get_text()
        item_list = {"name": item_name, "price": item_price}
        item_lists.append(item_list)


def click_page():
    driver.implicitly_wait(2)
    for page_number in pagination_number:
        try:
            try:
                req = driver.page_source
                get_current_item(req)
                time.sleep(1)
                print("item_copy... ")
            except AttributeError:
                print("has AttributeError")
                continue
            driver.find_element_by_xpath(
                f'//*[@id="mArticle"]/div[5]/div/span[{page_number}]'
            ).click()
            print(f"page is {page_number}")
            driver.implicitly_wait(3)
        except Exception:
            print("page end")
            continue
    itemlist_to_csv(item_lists, 1)


def itemlist_to_csv(arr, number):
    file = open(f"kakao_itemlist{number}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["name", "price"])
    for item in arr:
        writer.writerow(list(item.values()))


click_page()


def move_category():
    for number in category_number:
        try:
            driver.find_element_by_xpath('//*[@id="innerHead"]/div/button[2]').click()
            time.sleep(1.5)
            driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div/ul/li[4]"
            ).click()
            driver.implicitly_wait(2)
            driver.find_element_by_xpath(
                f"/html/body/div[6]/div/div/div/ul/li[4]/ul/li[{number}]"
            ).click()
            driver.implicitly_wait(2)
            # 뒤로가기
            time.sleep(1)
            driver.back()
            driver.implicitly_wait(2)
            print(f"{category_name[number-3]} copy...")
            click_page()
            driver.implicitly_wait(2)

        except Exception:
            if number == 12:
                break
            else:
                continue
