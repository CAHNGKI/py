import pandas as pd
savepath1 = 'C:\\Users\\moon2\\Desktop\\file\\py\\s4\\csv_s1.csv'
savepath2 = 'C:\\Users\\moon2\\Desktop\\file\\py\\s4\\csv_s2.csv'
#df = pd.read_csv(savepath1,skiprows=[0])

#df = pd.read_csv(savepath1,skiprows=[0],header=None)

#df = pd.read_csv(savepath1, skiprows=[0],header=None, names=['month',2013,2014,2015])

#df = pd.read_csv(savepath1 ,skiprows=[0],header=None, names=['month',2013,2014,2015], index_col=[0])


#df = pd.read_csv(savepath1 ,skiprows=[0],header=None, names=['month',2013,2014,2015], index_col=[0], na_values=['JAN'])
#print(pd.isnull(df))

#df = pd.read_csv(savepath1 ,skiprows=[0],header=None, names=['month',2013,2014,2015])
#print(list(df.index))
#print(df.rename(index={0:'aa',1:'bb'}))
#print(df.rename(index=lambda x:x*10))

df = pd.read_csv(savepath2, sep=';', skiprows=[0], header=None, names=['name','test1','test2','test3','final','grade'])

#df['grade'] = df['grade'].str.replace('C','A++')

#df['avg'] = df[['test1','test2','test3','final']].mean(axis=1)

#df['sum'] = df[['test1','test2','test3','final']].sum(axis=1)
print(df)
