from urllib import response
import requests
from bs4 import BeautifulSoup

# response = 네이버 서버에 대화를 시도
response =  requests.get("https://www.naver.com")

# naver에서 response를 줌
html = response.text

# html의 번역선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn 하나인 놈 한 개 찾아내기
word = soup.select_one('#NM_set_home_btn')

# text 요소만 출력
print(word.text)