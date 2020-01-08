import sys
import io
from pandas import Series, DataFrame

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

r_data = {'city':['서울','대구','부산','대전'], 'total1':[55000,49000,52000,50000],'total2':[65000,59000,72000,40000]}
i_data =['a','b','c','d']

d_frame = DataFrame(r_data, index=i_data)

print(type(d_frame))
print(d_frame)
print(d_frame.index)
print(d_frame.values)
print(d_frame['city']) #columns
print(d_frame.ix['b']) #rows

for e in d_frame.values:
    print(e)

for e in d_frame.values:
    for i,z in enumerate(e):
        print(i, z)
