import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

url1 = "https://ssl.pstatic.net/tveta/libs/1257/1257021/436088e6af2ae456fe45_20191224095048162.png"

savepath1 = "C:/Users/moon2/Desktop/file/py/s2/img/test1.jpg"

req.urlretrieve(url1, savepath1)

url2 ="https://tvetamovie.pstatic.net/libs/1266/1266390/024da6e3aae42ace947f_20191216152409822.mp4-pBASE-v0-f96833-20191216154754206.mp4"
savepath2 ="C:/Users/moon2/Desktop/file/py/s2/img/test1.mp4"

req.urlretrieve(url2, savepath2)
