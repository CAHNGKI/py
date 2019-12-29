import sys
import io
import requests, json

r = requests.get('http://openapi.tago.go.kr/openapi/service')
print(r.text)
