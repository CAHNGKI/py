import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

payload ={'key1':'value1', 'key2':'value2'}

#r = requests.put('http://httpbin.org/put', data=payload)

#r = requests.put('http://jsonplaceholder.typicode.com/post/1', data = payload)

#r = requests.delete('http://jsonplaceholder.typicode.com/post/1')
