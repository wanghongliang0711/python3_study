"""
@author: wanghongliang
@file: study_11_多线程版UDP聊天器.py
@time: 2021/7/22 11:04 
"""
import socket
import threading


def recv_msg(udp_socket):
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    # 发送数据
    while True:
        send_data = input("输入要发送的数据: ")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("", 8008))

    # 3. 获取对方的ip
    dest_ip = "192.168.1.19"
    dest_post = 8009

    # 创建2个线程，去执行相应的功能
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket, ))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_post))

    t_recv.start()
    t_send.start()

"""
使用  网络调试助手  进行验证
"""


if __name__ == '__main__':
    main()
