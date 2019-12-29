import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)


url = "https://ppss.kr/wp-content/uploads/2016/09/%EA%B0%9C-1-549x365.jpg"
savepath ="C:/Users/moon2/Desktop/file/py/s2/img/test.jpg"

f = req.urlopen(url).read()
savefile = open(savepath, 'wb')
savefile.write(f)
savefile.close()
