import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
# requests -> 브라우저에 요청 / bs4 -> 정보 추출

# select_one('') -> 첫번째만, select('') -> 전부 list 형태로 반환
# 우클릭 -> 검사 -> 해당 태그 우클릭 -> copy -> copy selector
title = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
tr_list = soup.select("#old_content > table > tbody > tr")
for tr in tr_list:
    a_tag = tr.select_one("td.title > div > a")
    if a_tag is not None:
        print(a_tag.text)

