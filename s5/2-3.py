import sqlite3


conn = sqlite3.connect('C:/Users/moon2/Desktop/file/py/s5/databases/sqlite1.db')#isolation_level=None : auto commit

c = conn.cursor()

#데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id=?",('niceman',1))

#데이터 수정2
c.execute("UPDATE users SET username = :name WHERE id= :id",{'name':'goodman','id':2})


#데이터 수정3
c.execute("UPDATE users SET username ='%s' WHERE id='%s'" %('cuteboy',3))
#데이터 삭제1
c.execute("DELETE FROM users WHERE id=?",(4,))

#데이터 삭제2
c.execute("DELETE FROM users WHERE id= :id",{'id': 5})

#데이터 삭제3
c.execute("DELETE FROM users WHERE id='%s'" %(6,))

for user in c.execute("SELECT * FROM users"):
    print(user)

conn.commit()

conn.close()
