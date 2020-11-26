from bs4 import BeautifulSoup
import requests

item_lists = []


def item_name(url):
    soup = BeautifulSoup(url, "html.parser")
    container = soup.find("div", {"class", "cont_list"})
    box = container.find("ul")
    item_list = box.find_all("li")
    for item in item_list:
        item_name = item.find("p").get_text()
        item_lists.append(item_name)
    print("Item name scrapping.... ")
    print(item_lists)