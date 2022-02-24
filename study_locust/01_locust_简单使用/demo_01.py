"""
@author: blake.wang
@file: demo_01.py
@time: 2022/2/24 14:52 
"""
# import requests
from locust import HttpUser,task
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class MyBlogs(HttpUser):
    # 访问我的博客首页
    @task
    def get_blog(self):
        # 定义请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        req = self.client.get("/imyalost",  headers=header, verify=False)
        print(req)
        print(req.text)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")


# class websitUser(HttpLocust):
#     task_set = MyBlogs
#     min_wait = 3000  # 单位为毫秒
#     max_wait = 6000  # 单位为毫秒


if __name__ == "__main__":
    import os
    os.system("locust -f demo_01.py --host=https://www.cnblogs.com")
