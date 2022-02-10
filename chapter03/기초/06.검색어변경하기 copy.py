import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요")

#f스트링 - 문자열 기호 앞에 f를 쓰고 변수가 들어가는 자리에 {}
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") #결과는 리스트
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url) 