import simplejson as json
from tinydb import TinyDB, Query, where

# 파일 db 생성
db = TinyDB('C:/Users/moon2/Desktop/file/py/s5/databases/databases1.db')

#db.insert({'name':'moon', 'email':'test@google.com'}) #json {}
#db.insert_multiple([{'name':'kim', 'email':'test2@google.com'}, {'name':'choi', 'email':'test1@google.com'}])#jsonarry [{},{}]

sql = Query()

el = db.get(sql.name =='kim')

print(el)
print(el.doc_id)

#데이서 수정
db.update({'email': 'test111@google.com'}, doc_ids=[2])

#데이터 수정 및 추가
db.upsert({'email': 'test111@naver.com', 'login':True}, sql.name =='choi')

#데이터 삭제
db.remove(doc_ids=[2])
db.remove(sql.name =='kim')

#전체 조회
print(db.all())
