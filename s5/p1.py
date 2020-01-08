import simplejson as json
from tinydb import TinyDB

db = TinyDB('C:/Users/moon2/Desktop/file/py/s5/databases/databases2.db', default_table='albums')

albums =db.table('albums')
photos =db.table('phtos')

with open('C:/Users/moon2/Desktop/file/py/s5/data/albums.json','r') as infile:
    r = json.loads(infile.read())
    for u in r:
        albums.insert(u)
with open('C:/Users/moon2/Desktop/file/py/s5/data/photos.json','r') as infile:
    r = json.loads(infile.read())
    for t in r:
        photos.insert(t)

for item in albums:
    print(item['title'])
    for photo in photos:
        if photo['albumId'] == item['id']:
            print(photo['url'])
