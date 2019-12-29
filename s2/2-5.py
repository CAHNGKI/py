from bs4 import BeautifulSoup as bs
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

fp = open("C:/Users/moon2/Desktop/file/py/s2/cars.html", encoding="utf-8")
soup = bs(fp, 'html.parser')

def car_func(selector):
    print(soup.select_one(selector).string)

car_lambda = lambda q: print(soup.select_one(q).string)

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars > #gr")
car_func("li[id='gr']")
print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)
