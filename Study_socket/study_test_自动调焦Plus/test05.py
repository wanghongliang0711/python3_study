"""
@author: wanghongliang
@file: test05.py
@time: 2021/7/14 19:37 
"""
import requests, time

while True:
    print(requests.get("http://127.0.0.1:7890/dev-api33").text)
    time.sleep(0.1)