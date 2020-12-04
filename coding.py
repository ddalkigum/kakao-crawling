import csv

my_name = ["kim", "jin", "ah", "gogo"]
arr = ["img1", "img2", "img3", "img4", "img5"]


def write_csv(args, kwargs):
    file = open("text.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow([*args, *kwargs])


write_csv(my_name, arr)