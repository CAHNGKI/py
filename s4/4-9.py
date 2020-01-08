import pandas as pd
import numpy as np

savepath = 'C:\\Users\\moon2\\Desktop\\file\\py\\s4\\excel_s1.xlsx'

#df = pd.read_excel(savepath, sheet_name=0)


#print(df.head())
#print(df.tail())

#df = pd.read_excel(savepath, skiprows=[0], skipfooter=10)

#df = pd.read_excel(savepath, header=0)
#print(list(df))

#df = pd.read_excel(savepath, skiprows=[0], header=None, names=['state',2003,2004,2005])

#df = pd.read_excel(savepath, header=0, na_values='...', converters={'2003': lambda w: w if w>60000 else None})
#print(pd.isnull(df))

df = pd.read_excel(savepath, header=0)
print(df.rename(index=lambda x:x+1))
print(df.rename(index=lambda x:x+1).index)
