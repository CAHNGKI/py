from bs4 import BeautifulSoup as bs
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

url ="https://finance.naver.com/"
res = req.urlopen(url).read()
soup = bs(res, 'html.parser')

top = soup.select("#_topItems4 > tr")

for j,i in enumerate(top,1):
    print(j, i.find("a").string, i.find("td").string)
