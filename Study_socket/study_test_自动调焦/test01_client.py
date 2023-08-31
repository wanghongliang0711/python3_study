"""
@author: wanghongliang
@file: test01_client.py
@time: 2021/7/14 9:55 
"""
import socket
import time


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.connect(("10.87.106.110", 8008))

    for i in range(10):
        tcp_socket.send("CloseLightBox\r\n".encode("utf-8"))
        recv_data = tcp_socket.recv(1024)
        print(recv_data.decode("utf-8"))

        tcp_socket.send("OpenLightBox\r\n".encode("utf-8"))
        recv_data = tcp_socket.recv(1024)
        print(recv_data.decode("utf-8"))

        tcp_socket.send("GetStdScore\r\n".encode("utf-8"))
        recv_data = tcp_socket.recv(1024)
        print(recv_data.decode("utf-8"))
        time.sleep(1)
        print("-----------------")


    tcp_socket.close()



if __name__ == '__main__':
    main()
