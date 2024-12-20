from _datetime import datetime
import os
# import requests
# import xml.etree.ElementTree as et
#
# url = "https://techcrunch.com/feed/"
#
# x = requests.get(url)
#
# y = et.fromstring(x.content)
# print(y)
# channel = y.findall("./channel/item")
# print(channel)
# abc = []
# for item in channel:
#     dict = {}
#     for child in item:
#         if child.tag == "title":
#             dict["title"] = child.text
#         abc.append(dict)
#
# print(abc)

# compr_list = [number for number in range(10) if number % 2 == 0 if number > 4]
# print(compr_list)
#
#
#
# even_odd = [ "even" if x % 2 == 0 else "odd" for x in range(10)]
# print(even_odd)
#
# FILE_NAME = "testing.txt"
#
# with open(FILE_NAME, "w", newline="") as file:
#     rider = file.read()
#
# print("Testing clear console command...")
# input("Press Enter to clear the screen.")
# os.system('cls' if os.name == 'nt' else 'clear')


test = divmod(15, 60)
print( test)