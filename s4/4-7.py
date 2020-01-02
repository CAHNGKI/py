import pandas as pd
savepath2 = 'C:\\Users\\moon2\\Desktop\\file\\py\\s4\\csv_s2.csv'
df = pd.read_csv(savepath2, sep=';', skiprows=[0], header=None, names=['name','test1','test2','test3','final','grade'])

#df['grade'] = df['grade'].str.replace('C','A++')

df['avg'] = df[['test1','test2','test3','final']].mean(axis=1)

df['sum'] = df[['test1','test2','test3','final']].sum(axis=1)
print(df)

#df.to_csv('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\result_s1.csv')
df.to_csv('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\result_s1.csv',index=False)
