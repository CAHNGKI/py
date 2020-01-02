import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup as bs
import os.path
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'

savename ='C:\\Users\\moon2\\Desktop\\file\\py\\s4\\weather.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename,'r',encoding='utf-8').read()
soup = bs(xml, 'html.parser')

info ={}
for location in soup.find_all('location'):
    loc = location.find('city').string
    tmp = location.find_all('tmn')
    if not (loc in info):
        info[loc] = []
    for tmn in tmp:
        info[loc].append(tmn.string)

with open('C:\\Users\\moon2\\Desktop\\file\\py\\s4\\weather.txt','wt') as f:
    for loc in sorted(info.keys()):
        f.write(str(loc+'\n'))
        for n in info[loc]:
            f.write('\t'+str(n)+'\n')
