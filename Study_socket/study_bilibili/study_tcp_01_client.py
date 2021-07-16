"""
@author: wanghongliang
@file: study_tcp_01_client.py
@time: 2021/7/13 9:09 
"""
import socket
import time


def main():
    # 1. 创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    tcp_socket.connect(("192.168.1.7", 8009))
    time.sleep(5)
    # 3. 发送数据/接收数据
    tcp_socket.send("测试001".encode("gbk"))
    recv_data = tcp_socket.recv(1024)
    print(recv_data)

    # 4. 关闭套接字
    tcp_socket.close()




if __name__ == '__main__':
    main()

