"""
@author: wanghongliang
@file: study_udp_01.py
@time: 2021/7/12 16:56 
"""
import socket

# 创建一个 udp 套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 从键盘获取数据
send_data = input("请输入要发送的数据： ")

# 可以使用套接字收发数据
# udp_socket.sendto(b"wang", ("对方ip", 对方端口))
# udp_socket.sendto(b"wang2", ("10.87.106.15", 8888))
# udp_socket.sendto(send_data.encode('utf-8'), ("10.87.106.15", 8888))
udp_socket.sendto(send_data.encode('gbk'), ("10.87.106.15", 8888))

# 关闭套接字
udp_socket.close()

