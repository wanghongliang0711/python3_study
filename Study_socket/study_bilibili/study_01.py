"""
@author: wanghongliang
@file: study_01.py
@time: 2021/7/12 16:38 
"""
import socket
'''
https://www.bilibili.com/video/BV1Xx411R743?p=8

socket.socket(family, type)
family: 套接字家族可以是 AF_UNIX 或者 AF_INET
AF_INET: 用于Internet 进程间通信，常用AF_INET
AF_UNIX: 同一台机器进程间通信

type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
SOCK_STREAM: 流式套接字，主要用于TCP协议
SOCK_DGRAM: 数据报套接字，主要用于UDP协议
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




s.close()


