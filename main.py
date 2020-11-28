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
    "write",
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

# driver.find_element_by_xpath('//*[@id="innerHead"]/div/button[2]').click()
# time.sleep(1.5)
# driver.find_element_by_xpath("/html/body/div[6]/div/div/div/ul/li[4]").click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div/ul/li[4]/ul/li[3]").click()


def get_current_item(r):
    """
    Get item list from each kakako category

    " r = page resource "

    """
    soup = BeautifulSoup(r, "html.parser")
    container = soup.find("div", {"class", "cont_list"})
    box = container.find("ul")
    item_list = box.find_all("li")
    for item in item_list:
        item_set = item.find("a", {"class", "item__Link-sc-5t2pho-10"})
        item_price = (
            item_set.find("p", {"class", "jXNMZp"}).get_text().strip(" 금액 원 , ")
        )
        item_name = item_set.find("p").get_text()
        item_image = item_set.find("img")["src"]
        item_list = {"name": item_name, "price": item_price, "image": item_image}
        item_lists.append(item_list)

    return item_lists


def click_page(number):
    """

    Click page number

    " number = page number "

    """
    driver.implicitly_wait(10)
    for page_number in pagination_number:
        req = driver.page_source
        get_current_item(req)
        time.sleep(1)
        print("item_copy... ")
        try:
            driver.find_element_by_xpath(
                f'//*[@id="mArticle"]/div[5]/div/span[{page_number}]'
            ).click()
            print(f"page is {page_number}")
        except Exception:
            print("end page")
            break
        driver.implicitly_wait(3)
    file = open(f"kakao_itemlist{number}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["name", "price", "image"])

    for item in item_lists:
        writer.writerow(list(item.values()))


def itemlist_to_csv(arr, number):
    """

    itemlist convert .csv file

    " arr = current item list "
    " number = csv file name + number "

    !! don't use it !!

    """
    file = open(f"kakao_itemlist{number}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["name", "price"])
    for item in arr:
        writer.writerow(list(item.values()))


def move_category():
    """

    click kakaoitem's category page

    """
    driver.implicitly_wait(2)
    for number in category_number:
        driver.find_element_by_xpath('//*[@id="innerHead"]/div/button[2]').click()
        time.sleep(1.5)
        driver.find_element_by_xpath("/html/body/div[6]/div/div/div/ul/li[4]").click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath(
            f"/html/body/div[6]/div/div/div/ul/li[4]/ul/li[{number}]"
        ).click()
        click_page(number)
        # 뒤로가기
        driver.back()
        print(f"{category_name[number-3]} copy...")
        driver.implicitly_wait(2)


move_category()
driver.quit()