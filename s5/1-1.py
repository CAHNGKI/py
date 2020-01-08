import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB

# 파일 db 생성
db = TinyDB('C:/Users/moon2/Desktop/file/py/s5/databases/databases.db', default_table='users')

#메모리 db 생성
#db= TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users =db.table('users')
todos = db.table('todos')

#테이블 데이터 삽입
#users.insert({'name':'moon', 'email':'test@google.com'})
#todos.insert({'name':'homework', 'complete':False})

#테이블 데이터 전체 삽입1

with open('C:/Users/moon2/Desktop/file/py/s5/data/users.json','r') as infile:
    r = json.loads(infile.read())
    for u in r:
        users.insert(u)

with open('C:/Users/moon2/Desktop/file/py/s5/data/todos.json','r') as infile:
    r = json.loads(infile.read())
    for t in r:
        todos.insert(t)

#전체 데이터 출력
#print(users.all())
#print(todos.all())
#print(db.tables())

#전체 데이터 삭제
#todos.purge() #db.purge_table('users')
#users.purge() #db.purge_table('todos')

#db.purge_tables()
db.close()
