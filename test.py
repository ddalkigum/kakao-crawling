import requests
from bs4 import BeautifulSoup

arr = []

r = requests.get(
    "https://store.kakaofriends.com/kr/products/category/subject?categorySeq=64&sort=createDatetime,desc"
)
soup = BeautifulSoup(r.text, "html.parser")
container = soup.find("div", {"class", "cont_list"})
box = container.find("ul")
item_list = box.find_all("li")
for i in item_list:
    img = i.find("img")
    img_source = img.attrs["href"]
