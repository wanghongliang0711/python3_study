"""
@author: wanghongliang
@file: test03.py
@time: 2021/7/14 19:35 
"""
import requests, time

while True:
    print(requests.get("http://127.0.0.1:7890/").text)
    time.sleep(0.1)
