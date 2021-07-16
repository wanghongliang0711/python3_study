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

    while True:
        """ 一次只能为一个客户端服务，其他客户端需要排队等待 """
        print("等待一个新的客户端的到来。。。。")
        # 4. 等待客户端的链接 accept
        new_client_socket, client_addr = tcp_server_socket.accept()  # ==> tcp_socket.connect 等待客户端 connect

        print("一个新的客户端已经到来 %s" % str(client_addr))

        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)  # ==> tcp_socket.send 等待客户端 send 数据
        print("客户端送过来的请求是: %s" % recv_data.decode("gbk"))

        # 发送数据给客户端
        new_client_socket.send("hahah--ok".encode("gbk"))

        # 关闭套接字
        new_client_socket.close()
        print("已经服务完毕......")


    tcp_server_socket.close()


if __name__ == '__main__':
    main()
