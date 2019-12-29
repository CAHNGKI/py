import sys
import io
from bs4 import BeautifulSoup as bs
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

url ='https://www.wishket.com/accounts/login/'

ua = UserAgent()

with requests.Session() as s:
    s.get(url)
    login_info={
    'identification': 'moon20517',
    'password': '00000000',
    'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    response = s.post(url, data=login_info, headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})
    if response.status_code == 200 and response.ok:
        soup = bs(response.text,'html.parser')
        list = soup.select('table.table-responsive > tbody > tr')
        for i in list:
            print(i.find('th').string, i.find('td').text)
