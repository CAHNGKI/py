import urllib.request as req
import simplejson as json
import os.path

url = "https://api.github.com/repositories"

savename = 'C:\\Users\\moon2\\Desktop\\file\\py\\s4\\repo.json'

if not os.path.exists(url):
    req.urlretrieve(url, savename)

items =json.load(open(savename, 'r', encoding='utf-8'))

for item in items:
    print(item['full_name'] + '   -   ' + item['owner']['url'])
