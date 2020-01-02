import urllib.request as req
import simplejson as json
import os.path

url ='https://jsonplaceholder.typicode.com/comments'

savename = 'C:\\Users\\moon2\\Desktop\\file\\py\\s4\\jsonplaceholder.json'

if not os.path.exists(url):
    req.urlretrieve(url, savename)

items =json.load(open(savename, 'r', encoding='utf-8'))

for item in items:
    print(item['name'] + '   -   ' + item['email'])
