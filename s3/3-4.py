import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")


r = requests.get('http://api.github.com/events')
jar = requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain="httpbin.org",path='/cookies')


r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)


payload ={'key1':'value1', 'key2':'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
print(r.text)
