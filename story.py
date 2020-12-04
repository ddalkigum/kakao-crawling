import re
import requests
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

kakao = []


driver = webdriver.Chrome()
driver.get("https://store.kakaofriends.com/kr/index")
driver.implicitly_wait(3)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
for number in range(1, 11):
    image = soup.select(
        f"#mArticle > main > div.today__Wrap-sc-1gh0i9h-0.fCbncI > article:nth-child({number}) > section:nth-child(2) > div.media-slider__Wrap-bw8abp-0.ksgZQS > div > div > div > div > div > img"
    )
    if image == []:
        image = soup.select(
            f"#mArticle > main > div.today__Wrap-sc-1gh0i9h-0.fCbncI > article:nth-child({number}) > section:nth-child(2) > div.media-slider__Wrap-bw8abp-0.ksgZQS > div > div > div > div > div > video"
        )
    else:
        pass
    like = soup.select(
        f"#mArticle > main > div.today__Wrap-sc-1gh0i9h-0.fCbncI > article:nth-child({number}) > section:nth-child(2) > div.contents__LikeCountWrap-sc-1b0iw5u-2.fDHkJk > span > span"
    )
    title = soup.select(
        f"#mArticle > main > div.today__Wrap-sc-1gh0i9h-0.fCbncI > article:nth-child({number}) > section:nth-child(2) > p"
    )
    content = soup.select(
        f"#mArticle > main > div.today__Wrap-sc-1gh0i9h-0.fCbncI > article:nth-child({number}) > section:nth-child(2) > div.contents__SubCopy-sc-1b0iw5u-6.dLrCHR"
    )
    kakao_contents = content[0].get_text()
    kakao_image = image[0]["src"]
    kakao_like = like[0].get_text()
    kakao_title = title[0].get_text()
    kakao_story = {
        "title": kakao_title,
        "image": kakao_image,
        "like": kakao_like,
        "contents": kakao_contents,
    }
    kakao.append(kakao_story)
driver.implicitly_wait(2)

file = open("story.csv", "w")
writer = csv.writer(file)
writer.writerow(["title", "image", "like", "contents"])
for item in kakao:
    writer.writerow(list(item.values()))
