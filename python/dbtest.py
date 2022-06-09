from pymongo import MongoClient
client = MongoClient('localhost', 27017) # 해당 주소의 mongoDB 접속
db = client.dbsparta                     # client.{'접속할 DB 이름'} -> 'dbsparta'라는 db 이름으로 접속

# pymongo function -> insert / find / update / delete
# db.users -> 'users'라는 collection

# insert_one(추가할 딕셔너리)
doc = {'name':'smith','age':21}
db.users.insert_one(doc)


# find( 조건1{key:value}, 조건2{key:value}, {'_id':False})
# 전체 find({}, {'_id':False})
same_ages = list(db.users.find({'age':21}, {'_id':False}))
total_list = list(db.users.find({}, {'_id':False}))


# update_one(변경 조건{key:value}, {'$set':변경할 딕셔너리}
db.users.update_one({'name':'bobby'}, {'$set':{'age':19}})


# delete_one(삭제 조건{key:value})
db.users.delete_one({'name':'bobby'})
