"""
@author: wanghongliang
@file: test02.py
@time: 2021/7/14 19:30 
"""
import time, socket
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')
data = "11"

@app.route('/')
def hello():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(("192.168.1.7", 9999))
    tcp_socket.send("GetImage\r\n".encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("utf-8"))
    tcp_socket.close()
    return "pass"
    # return data


@app.route('/dev-api', methods=['GET'])
def hello1():
    global data
    data = "22"
    time.sleep(1.5)
    res = {"data" : data}
    return res

@app.route('/dev-api33', methods=['GET'])
def hello2():
    global data

    data = "33"
    time.sleep(1)
    res = {"data": data}
    return res


if __name__ == '__main__':
    app.run('0.0.0.0', '7890')
