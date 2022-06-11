import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


# 순위 제목 가수 크롤링
# 순위   #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# 제목   #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# 가수   #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

tr_list = soup.select("#body-content > div.newest-list > div > table > tbody > tr")
for tr in tr_list:
    rank = tr.select_one("td.number").text.split()[0]
    title = tr.select_one("td.info > a.title.ellipsis").text.strip()
    singer = tr.select_one("td.info > a.artist.ellipsis").text.strip()

    print(rank, title, singer)

