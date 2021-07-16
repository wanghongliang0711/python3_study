"""
@author: wanghongliang
@file: study_udp_01.py
@time: 2021/7/12 16:56 
"""
import socket

# 创建一个 udp 套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip和端口，ip一般不写，表示本机的任何一个ip
udp_socket.bind(('', 9999))

# 等待接收对方发送的数据
recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数

print(recv_data)  # (b'http://www.cmsoft.cn QQ:10865600', ('192.168.1.37', 8888))
print(recv_data[0].decode('gbk'))  # http://www.cmsoft.cn QQ:10865600

# 关闭套接字
udp_socket.close()


# https://www.bilibili.com/video/BV1Xx411R743?p=17&spm_id_from=pageDriver
