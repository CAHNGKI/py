import pickle

bfilename = 'C:/Users/moon2/Desktop/file/py/s4/test.bin'
tfilename = 'C:/Users/moon2/Desktop/file/py/s4/test.txt'

data1 = 77
data2 = 'hello world'
data3 = ['car','apple','house']

with open(bfilename,'wb') as f:
    pickle.dump(data1,f)
    pickle.dump(data2,f)
    pickle.dump(data3,f)

with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))

with open(bfilename,'rb') as f:
    b = pickle.load(f)
    print(type(b), b)
    b = pickle.load(f)
    print(type(b), b)
    b = pickle.load(f)
    print(type(b), b)

with open(tfilename,'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), str(i), line)
