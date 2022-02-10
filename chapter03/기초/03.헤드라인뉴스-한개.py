import requests
from bs4 import BeautifulSoup

#Connection aborted 나왔을 때 쓰는 방법
header = {'User-agent' : 'Mozila/2.0'}

#Connection aborted 나왔을 때 , headers=header
# 추가해 주기
response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.cluster_text_headline.nclicks\(cls_pol\.clsart\)')

print(title.text.strip())