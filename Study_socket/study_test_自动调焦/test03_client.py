"""
@author: wanghongliang
@file: test01_client.py
@time: 2021/7/14 9:55 
"""
import socket, time, json


def main():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.connect(("192.168.1.7", 9999))
    # time.sleep(1)
    time_cum = 0
    while True:
        msg = tcp_socket.recv(1024).decode("utf-8")  # 粘包现象
        print(msg)
        print(json.loads(msg))
        time_cum += 1
        if time_cum == 10:
            break
    time.sleep(10)
    msg = tcp_socket.recv(1024).decode("utf-8")
    print(msg)
    tcp_socket.close()


if __name__ == '__main__':
    main()
