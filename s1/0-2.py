from bs4 import BeautifulSoup as bs
import requests, re, os
import sys
import io
from urllib.request import urlretrieve

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print('fail')
        exit()


html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = bs(html.text, 'html.parser')
html.close()

data_list = soup.findAll('div',{'class':'col_inner'})

li_list = []
for data in data_list:
    li_list.extend(data.findAll('li'))

for li in li_list:
    img = li.find('img')
    title = img['title']
    src = img['src']
    title = re.sub('[^0-9a-zA-Zㄱ-핧]','',title)
    urlretrieve(src, './image/' + title + '.jpg')
