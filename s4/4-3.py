import simplejson as json

data = {}
data['people'] =[]
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'seoul'
})

data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'busan'
})

data['people'].append({
    'name':'moon',
    'website':'daum.net',
    'from':'ulsan'
})
#dict(json) -> str
e =json.dumps(data, indent = 4)
#print(type(e))
#print(e)

#str -> dict(json)
d = json.loads(e)
#print(type(d))
#print(d)

with open('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\member.json','w') as outfile:
    outfile.write(e)
with open('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\member.json','r') as infile:
    r = json.loads(infile.read())
    #print(type(r))
    #print(r)
    for p in r['people']:
        print(p['name'])
        print(p['website'])
        print(p['from'])
        print('')
