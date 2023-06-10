import os
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
first_page_url = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
over_18_url = 'https://www.ptt.cc/ask/over18'

ss = requests.session()
print(ss.cookies)

ss.get(first_page_url, headers=headers)
print(ss.cookies)

data = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes",
}

ss.post(over_18_url, headers=headers, data=data)
print(ss.cookies)

res = ss.get(url, headers=headers)
print(res.text)
