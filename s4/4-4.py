import simplejson as json

data = {}
data['people'] =[]
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'seoul',
    'grade': [95, 77, 89, 90]
})

data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'busan',
    'grade': [85, 67, 82, 100]
})

data['people'].append({
    'name':'moon',
    'website':'daum.net',
    'from':'ulsan',
    'grade': [95, 87, 99, 92]
})

with open('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\member1.json','w') as outfile:
    json.dump(data, outfile)
with open('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\member1.json','r') as infile:
    r = json.load(infile)
    #print(type(r))
    #print(r)
    for p in r['people']:
        print(p['name'])
        print(p['website'])
        print(p['from'])
        grade =''
        for g in p['grade']:
            grade = grade + ' ' +str(g)
        print(grade)
