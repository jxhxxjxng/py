import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}

response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.cluster_text_headline.nclicks\(cls_pol\.clsart\)')
for title in titles:
    print(title.text)