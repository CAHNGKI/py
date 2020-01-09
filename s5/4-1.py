import FinanceDataReader as fdr
import pandas as pd
import datetime
import sqlite3

#pandas, pandas_datareader 설치

try:
    with sqlite3.connect('C:/Users/moon2/Desktop/file/py/s5/databases/sqlite2.db') as conn:
        #조회 시작 & 마감 날짜
        start = datetime.datetime(2019, 12, 1)
        end = datetime.datetime(2019, 12, 31)

        #google정보 호출
        gs = fdr.DataReader('090430', start, end)
        #출력
        print(gs)

        #인덱스 출력
        print(gs.index)
        #column 출력
        print(gs['Open'])
        #row 출력
        print(gs.ix['2019-12-02'])

        #index to column
        gs['Date'] = gs.index
        #index 재설정
        gs.index = range(1, (len(gs.index)+1))
        print(gs)

        #pandas to database(to sql)
        gs.to_sql('amole', conn, if_exists="replace",index =True, index_label='id') #fail, replace, append

        conn.commit()

        #pandas read database(read sql) 전체 조회
        df = pd.read_sql(('SELECT * FROM amole'), conn, index_col ='id')
        print(df)
        #pandas read database(read sql) 전체 조회
        df = pd.read_sql('SELECT * FROM amole WHERE id =? or id =?', conn, params=(3,7),index_col ='id')
        print(df)
finally:
    print('complete')
