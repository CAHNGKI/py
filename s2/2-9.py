from bs4 import BeautifulSoup as bs
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

base = ""
quote = rep.quote_plus("")
url =base + quote

res = req.urlopen(url).read()
savepath = "C:\\Users\\moon2\\Desktop\\file\\py\\s2\\img\\i"

soup = bs(res, 'html.parser')
img_list = soup.select("")

for i, img_list in enumerate(img_list, 1):
    #print(img_list['data-source'])
    filename = os.path.join(savepath, savepath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'], filename)
