import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB, Query

# 파일 db 생성
db = TinyDB('C:/Users/moon2/Desktop/file/py/s5/databases/databases.db', default_table='users')

#메모리 db 생성
#db= TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users =db.table('users')
todos = db.table('todos')

#users 테이블 출력
#for item in users:
    #print(item['username'], ' : ', item['phone'])

#for item in todos:
    #print(item['title'], ' : ', item['completed'])

# 연결관계 출력
"""
for item in users:
    print(item['username'])
    for todo in todos:
        if todo['userId'] == item['id']:
            print(todo['title'])
"""
#쿼리 객체 사용 조회
Users = Query()
Todos = Query()

#(아래 수정, 삭제를 여기에 코드 먼저 삽임)
user_3 = users.search(Users.id == 3)
#print(user_3)

#수정
users.update({'username':'kim'}, Users.id == 3)

#삭제
users.remove(Users.id ==3)
