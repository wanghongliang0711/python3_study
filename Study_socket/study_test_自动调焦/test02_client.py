"""
@author: wanghongliang
@file: test01_client.py
@time: 2021/7/14 9:55 
"""
import socket


def main():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    tcp_socket.connect(("192.168.1.7", 9999))


    tcp_socket.send("GetImageName\r\n".encode("utf-8"))

    file_name = tcp_socket.recv(1024).decode("utf-8")
    print(file_name)
    fp = open("new_" + file_name, 'wb')
    while True:
        recv_data = tcp_socket.recv(1024 * 1024 * 100)
        print(len(recv_data))
        if len(recv_data) == 0:
            break
        fp.write(recv_data)
    fp.close()

    # over_meg = tcp_socket.recv(1024).decode("utf-8")
    # print(over_meg)

    tcp_socket.close()



if __name__ == '__main__':
    main()
