"""
@author: blake.wang
@file: demo_02.py
@time: 2022/2/24 15:16 
"""
from locust import HttpUser,task
import json


class MyBlogs(HttpUser):
    # 访问我的博客首页
    @task
    def get_blog(self):
        # 定义请求头
        data = {"username": "root", "password": "123456"}
        data_len = str(len(json.dumps(data).replace(" ", "")))
        header = {"Content-Type": "application/json;charset=UTF-8",
                  "Host": "10.87.106.29",
                  "Content-Length": "39"}

        req = self.client.post("/eis/guest/login", headers=header, json=data)

        print("req.url: ", req.url)
        print("req.text", req.text)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")




if __name__ == "__main__":
    import os
    os.system("locust -f demo_02.py --host=http://10.87.106.29")

