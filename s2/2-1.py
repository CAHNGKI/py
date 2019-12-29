from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html="""
<html>
  <body>
  <h1>python</h1>
  <p>tag selector</p>
  <p>css selector</p>
  </body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
print(h1)
p1 = soup.html.body.p
print(p1)
p2 = p1.next_sibling.next_sibling
print(p2)
p3 = p1.previous_sibling.previous_sibling
print(p3)
