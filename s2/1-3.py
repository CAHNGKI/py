import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

api ="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?"
values = {
    'ctxCd': '1001'
}
params = urlencode(values)

url = api + params
print(url)
