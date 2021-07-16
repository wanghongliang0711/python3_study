"""
@author: wanghongliang
@file: test01_client.py
@time: 2021/7/14 9:55 
"""
import socket, requests


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server.bind(("", 9999))

    tcp_server.listen(128)

    while True:
        # 等待 链接
        print("等待一个新的客户端的到来。。。。")
        client_socket, client_addr = tcp_server.accept()
        print("client_addr: ", client_addr)

        recv_data = client_socket.recv(1024)
        print(recv_data)
        print(recv_data.decode("utf-8"))
        print("------")


        client_socket.send("D:\\图片\\1.PNG".encode("utf-8"))
        #
        # recv_data = client_socket.recv(1024)
        # print(recv_data.decode("utf-8"))
        # client_socket.send("D:\\图片\\111.PNG".encode("utf-8"))

        client_socket.close()

    tcp_server.close()



if __name__ == '__main__':
    main()
