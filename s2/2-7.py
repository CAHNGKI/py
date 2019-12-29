from bs4 import BeautifulSoup as bs
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

url ="https://finance.naver.com/sise/"
res = req.urlopen(url).read()
soup = bs(res, 'html.parser')

top10 = soup.select("#siselist_tab_5 > tr")
j = 1
for i in top10:
    if i.find("a") is not None:
        print(j, i.select_one(".tltle").string)
        j +=1
