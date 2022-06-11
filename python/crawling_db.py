import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
# requests -> 브라우저에 요청 / bs4 -> 정보 추출

# select_one('') -> 첫번째만, select('') -> 전부 list 형태로 반환
# 우클릭 -> 검사 -> 해당 태그 우클릭 -> copy -> copy selector
tr_list = soup.select("#old_content > table > tbody > tr")

for tr in tr_list:
    rank_tag = tr.select_one("td > img")
    title_tag = tr.select_one("td.title > div > a")
    rating_tag = tr.select_one("td.point")
    if title_tag is not None:
        rank = rank_tag["alt"]
        title = title_tag.text
        rating = rating_tag.text

        doc = {
            'rank': rank,
            'title': title,
            'rating': rating
        }
        db.movie.insert_one(doc)


print("-----영화제목 '매트릭스'의 평점 가져오기-----")
matrix = db.movie.find_one({'title':"매트릭스"}, {'_id':False})
matrix_rating = matrix['rating']
print(matrix_rating)

print("\n-----'매트릭스'의 평점과 같은 평점의 영화 제목들 가져오기-----")
movie_list = list(db.movie.find({"rating":matrix_rating}, {'_id':False}))
for m in movie_list:
    print(m["title"])

print("\n-----'매트릭스' 영화의 평점 0으로 만들기-----")
db.movie.update_one({'title':"매트릭스"}, {'$set':{'rating':'0'}})
print(matrix)


