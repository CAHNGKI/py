from bs4 import BeautifulSoup as bs
import requests as reqs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = reqs.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = bs(html.text, 'html.parser')
html.close()

data_list = soup.findAll('div',{'class':'col_inner'})

for data1 in data_list:
    data2 = data1.findAll('a',{'class':'title'})

    title_list =[]
    for i in data2:
        title_list.append(i.text)
    print(title_list)
