from bs4 import BeautifulSoup as bs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html= """
<html><body>
<div id="main">
  <h1>list</h1>
  <ul class="lecs">
    <li>java</li>
    <li>python</li>
    <li>ML</li>
    <li>bluetooth</li>
  </ul>
</div>
</body></html>
"""

soup = bs(html,'html.parser')
h1 = soup.select_one("div#main > h1 ")
#print(h1.string)
list_li = soup.select("div#main > ul.lecs > li")

for i in list_li:
    print(i.string)
