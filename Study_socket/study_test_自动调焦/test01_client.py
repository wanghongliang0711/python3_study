"""
@author: wanghongliang
@file: test01_client.py
@time: 2021/7/14 9:55 
"""
import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.connect(("192.168.1.7", 9999))

    tcp_socket.send("GetImage\r\n".encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("utf-8"))

    tcp_socket.send("GetImageName\r\n".encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("utf-8"))



    tcp_socket.close()



if __name__ == '__main__':
    main()
