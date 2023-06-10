import requests
from bs4 import BeautifulSoup

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
            print('https://www.ptt.cc' + title_tag.select_one('a')['href'])
            print(title_name)
        else:
            print('Title is empty')
    url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
