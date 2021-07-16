"""
@author: wanghongliang
@file: test04.py
@time: 2021/7/14 19:37 
"""
import requests, time

while True:
    print(requests.get("http://127.0.0.1:7890/dev-api").text)
    time.sleep(0.1)

