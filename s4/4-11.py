import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100,4), columns=['a','b','c','d'])
#df = pd.DataFrame(np.random.randn(100,4), columns=['a','b','c','d'])

print(df)

df.to_excel('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\result_s2.xlsx',index=False)
