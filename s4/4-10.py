import pandas as pd
import numpy as np

savepath = 'C:\\Users\\moon2\\Desktop\\file\\py\\s4\\excel_s1.xlsx'

df = pd.read_excel(savepath, header=0)
#df['State'] = df['State'].str.replace(' ','|')


df['avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)

df['sum'] = df[['2003','2004','2005']].sum(axis=1).round(2)

#print(df[['2003','2004','2005']].max(axis=0))
#print(df[['2003','2004','2005']].min(axis=0))

#print(df.describe())
df.to_excel('C:/Users/moon2/Desktop/file/py/s4/result_s1.xlsx',index=None)
