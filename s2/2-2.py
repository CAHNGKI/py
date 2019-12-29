from bs4 import BeautifulSoup as bs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html ="""
<html><body>
  <ul>
    <li> <a href="http://www.naver.com">naver</a></li>
    <li> <a href="http://www.daum.net">daum</a></li>
    <li> <a href="http://www.daum.com">daum</a></li>
    <li> <a href="http://www.google.com">google</a></li>
    <li> <a href="http://www.tistory">tistory</a></li>
  </ul>
  </body></html>
"""

soup = bs(html, 'html.parser')

links = soup.find_all("a")
#print(links)
a = soup.find_all("a", string="daum")
#print(a)
b = soup.find_all("a", limit=3)
#print(b)

for i in links:
    #print(i)
    txt = i.string
    href = i.attrs['href']
    #print(txt, href)
