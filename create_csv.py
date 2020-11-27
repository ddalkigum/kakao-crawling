import csv

file = open("kakao_itemlist.csv", mode="w")
writer = csv.writer(file)
writer.writerow(["company", "title", "url"])
for job in temp:
    writer.writerow(list(job.values()))