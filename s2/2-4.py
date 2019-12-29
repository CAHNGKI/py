from bs4 import BeautifulSoup as bs
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

fp = open("C:/Users/moon2/Desktop/file/py/s2/food_list.html", encoding="utf-8")

soup = bs(fp, 'html.parser')

print(soup.select("li:nth-of-type(4)")[1].string)
print(soup.select_one("#ac-list > li:nth-of-type(4)").string)
print(soup.select("#ac-list >li[data-lo='cn']")[0].string)
print(soup.select("#ac-list > li.alcohol.high")[0].string)

param ={"data-lo": "cn", "class":"alcohol"}
print(soup.find("li",param).string)
print(soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print(ac.string)
