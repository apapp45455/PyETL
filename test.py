import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def load_article(article_url: str, load_path: str):
    """將文章寫入文件內，並以文章標題為檔案名，寫入資料夾article內"""
    res = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    article_tag = soup.select_one('div[id="main-content"]')
    for tag in article_tag.select('div'):
        tag.extract()
    # print(article_tag)
    article_content = article_tag.text
    with open(load_path, "w", encoding='utf-8') as f:
        f.write(article_content)
    # print(article_tag)
    # print("==========")
    # print(article_tag.select_one('div[class="article-metaline"]').extract())
    # print(article_tag)
    pass

if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/movie/M.1677860525.A.06A.html"
    load_article(article_url, "./test.txt")
