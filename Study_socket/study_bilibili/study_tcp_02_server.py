"""
@author: wanghongliang
@file: study_tcp_01_client.py
@time: 2021/7/13 9:09 
"""
import socket


def main():
    # 1. 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息 bind
    tcp_server_socket.bind(("192.168.1.7", 8009))

    # 3. 让默认的套接字由主动变为被动  listen
    tcp_server_socket.listen(128)

    """
    监听套接字 负责 等待所有新的客户端进行连接
    accept产生的新的套接字用来 为客户端服务
    """
    print("===== 1 ====")
    # 4. 等待客户端的链接 accept
    new_client_socket, client_addr = tcp_server_socket.accept()

    print("===== 2 ====")
    print("client_addr: ", client_addr)
    print("new_client_socket: ", new_client_socket)

    # 接收客户端发送过来的请求
    recv_data = new_client_socket.recv(1024)
    print(recv_data.decode("gbk"))

    # 发送数据给客户端
    new_client_socket.send("hahah--ok".encode("gbk"))

    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()



if __name__ == '__main__':
    main()

