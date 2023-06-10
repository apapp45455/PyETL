import os
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = 'https://www.w3schools.com/action_page.php'

data_str = """_hid_0: 564328
_hid_1: 352167
_hid_2: 57483
1A: Apple
2A: Dog
cars: fiat
subject1: Car Loan
subject2: fff
subject3: fasdf"""


data = {row.split(": ")[0]: row.split(": ")[1] for row in data_str.split("\n")}
# data = {}
# for row in data_str.split("\n"):
#     data[row.split(": ")[0]] = row.split(": ")[1]

res = requests.post(url, headers=headers, data=data)
print(res.text)
