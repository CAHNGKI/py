from pandas import Series

series1 = Series([92600, 94800, 88000, 95400,43200])

#print(series1)

#print(series1.count())
#print(series1.describe())

#print(series1[2])

series2 = Series([92600, 94800, 88000, 95400,43200], index=['2018-02-12','2018-02-13','2018-02-14','2018-02-15','2018-02-16'])
print(series2)

for data in series2.index:
    print(data)
for price in series2.values:
    print(price)

series_g1 = Series([10,20,30], index=['n1','n2','n3'])
series_g2 = Series([20,30,10], index=['n3','n2','n1'])

sum = series_g1 + series_g2
mul = series_g1 * series_g2

print(sum)
print(mul)
