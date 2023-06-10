import os
import requests
from bs4 import BeautifulSoup

from test import load_article

load_folder = "articles"
if not os.path.exists(f"./{load_folder}"):
    os.mkdir(f"./{load_folder}")

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
for i in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    title_tag_list = soup.select('div.title')

    for title_tag in title_tag_list:
        # try:
        #     title_name = title_tag.select_one('a').text
        #     title_url = title_tag.find('a')['href']
        #     print('https://www.ptt.cc' + title_url)
        #     print(title_name)
        # except AttributeError as e:
        #     print(title_tag)
        if title_tag.select_one('a'):
            title_name = title_tag.select_one('a').text
            article_url = 'https://www.ptt.cc' + title_tag.select_one('a')['href']
            """
            1. request article page
            2. beautifulsoup object
            3. select article part
            4. load article text
            """
            try:
                load_article(
                    article_url=article_url,
                    load_path=f"./{load_folder}/{title_name}.txt",
                )
            except FileNotFoundError:
                load_article(
                    article_url=article_url,
                    load_path=f"./{load_folder}/{title_name.replace('/','-')}.txt",
                )
            except OSError:
                pass
            print(title_name)
        else:
            print('Title is empty')
    url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']  # 前往上頁
