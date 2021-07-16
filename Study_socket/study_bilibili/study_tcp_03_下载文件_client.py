"""
@author: wanghongliang
@file: study_tcp_01_client.py
@time: 2021/7/13 9:09 
"""
import socket


def main():
    # 1. 创建套接字 socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    tcp_socket.connect(("192.168.1.7", 8099))
    # tcp_socket.connect_ex(("192.168.1.7", 8009))

    # 3. 想下载的文件名
    download_file_name = "1.jpg"

    # 4. 将文件名发送给服务器
    tcp_socket.send(download_file_name.encode("gbk"))

    # 5. 接收文件中的数据
    recv_data = tcp_socket.recv(180073, socket.MSG_WAITALL)  # 100M  1024==>1K   1024*1024==>1M
    #
    if recv_data:
        print(len(recv_data))
        # 6. 保存接收数据到新文件中
        with open("new_123456789" + download_file_name, "wb") as f:
            f.write(recv_data)

    # fp = open("new_1" + download_file_name, 'wb')
    # while True:
    #     recv_data = tcp_socket.recv(1024*1024*100)
    #     print(len(recv_data))
    #     if len(recv_data) == 0:
    #         break
    #     fp.write(recv_data)
    # fp.close()

    # recvd_size = 0  # 定义已接收文件的大小
    # filesize = 180073
    # fp = open("new_123456789" + download_file_name, 'wb')
    # while True:
    #     data = tcp_socket.recv(1024)
    #     print(len(data))

    # while not recvd_size == filesize:
    #     if filesize - recvd_size > 1024:
    #         data = tcp_socket.recv(1024)
    #         print(len(data))
    #         recvd_size += len(data)
    #     else:
    #         data = tcp_socket.recv(filesize - recvd_size)
    #         print(len(data))
    #         recvd_size = filesize
    #     fp.write(data)
    # fp.close()
    # 7. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
