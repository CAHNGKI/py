import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB, Query, where

# 파일 db 생성
db = TinyDB('C:/Users/moon2/Desktop/file/py/s5/databases/databases.db', default_table='users')

#메모리 db 생성
#db= TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users =db.table('users')
todos = db.table('todos')

Users = Query()
Todos = Query()

#다양한 조회 방법
"""
print(users.search(Users.id == 7))
print(users.search(Users['id'] == 7))
print(users.search(where('id') == 7))
print(users.search(Query()['id'] == 7))

print(users.search(where('address')['zipcode'] =='92998-3874'))
print(users.search(where('address').zipcode =='92998-3874'))

print(users.search(Users.email.exists()))
print(users.search(Users.a.exists()))
"""

#not

#print(users.search(~(Users.username == 'Bret')))

#or
#print(users.search((Users.username == 'Bret')|(Users.username == 'Antonette')))

#and
#print(users.search((Users.username == 'Bret')&(Users.id == 1)))


#기타 함수
print(len(users))
print(users.contains(Users.username == 'Bret'))
print(users.count(Users.username == 'Bret'))
