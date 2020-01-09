import sqlite3
import simplejson as json
import datetime

#db 생성
conn = sqlite3.connect('C:/Users/moon2/Desktop/file/py/s5/databases/sqlite1.db')#isolation_level=None : auto commit
#db 생성(메모리)
#conn = sqlite3.connect(":memory:")
# 날짜 생성
now = datetime.datetime.now()
nowdatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowdatetime)

#cursor 연결
c = conn.cursor()

#테이블 생성(sqlite3 datatype: text, numeric, integer, real, blob)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

#데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-0000-0000','kim.co.kr',?)",(nowdatetime,))

userlist =(
    (2, 'kim', 'kim@naver.com', '010-0000-0000','kim.co.kr',nowdatetime),
    (3, 'kim', 'kim@naver.com', '010-0000-0000','kim.co.kr',nowdatetime),
    (4, 'kim', 'kim@naver.com', '010-0000-0000','kim.co.kr',nowdatetime)
)
#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",userlist)
with open('C:/Users/moon2/Desktop/file/py/s5/data/users.json','r') as infile:
    r = json.load(infile)
    userdata = []
    for user in r:
        t=(user['id'], user['username'], user['email'], user['phone'], user['website'], nowdatetime )
        userdata.append(t)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",userdata)
#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",tuple(userdata))
#conn.execute("delete from users").rowcount

conn.commit()

conn.close()
