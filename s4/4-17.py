import matplotlib.pyplot as plt
import numpy as np
import FinanceDataReader as fdr
import datetime

start = datetime.datetime(2019,12,1)
end = datetime.datetime(2019,12,16)

gs_apple = fdr.DataReader('AAPL',start, end)

gs_amazon = fdr.DataReader('AMZN',start, end)

print(gs_apple)
print(gs_amazon)

fig = plt.figure('chart test')
fig.set_size_inches(10,6,forward=True)

plt.plot(gs_apple.index, gs_apple['Close'],'b', label='apple')
plt.plot(gs_amazon.index, gs_amazon['Close'],'r', label='amazon')

plt.legend(loc='upper right')
plt.title('apple&amazon')
plt.xlabel('date')
plt.ylabel('Close')

plt.show()
