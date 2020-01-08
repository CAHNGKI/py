import FinanceDataReader as fdr
import datetime
import sys
import io
import pandas_datareader as web

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

start = datetime.datetime(2019,12,15)
end = datetime.datetime(2019,12,31)

#df_krx = fdr.StockListing('KRX')
#print(df_krx.head(10))
#print(df_krx.index)
#print(df_krx['Symbol'])
#print(df_krx.describe())
#print(df_krx.ix[0])

#df_app = fdr.DataReader('AAPL', start, end)
#print(df_app.head(10))
#print(df_app['Open'])
#print(df_app.ix['2019-12-30'])
#print(df_app.describe())

#df_amz = fdr.DataReader('AMZN', start, end)
#print(df_amz.head(10))
#print(df_amz['High'])
#print(df_amz.ix['2019-12-30'])
#print(df_amz.describe())

#df_gog = fdr.DataReader('GOOGL', start, end)
#print(df_amz.head(10))
#print(df_gog['Close'])
#print(df_gog.ix['2019-12-30'])
#print(df_gog.describe())
