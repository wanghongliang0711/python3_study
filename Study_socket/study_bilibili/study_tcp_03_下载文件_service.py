"""
@author: wanghongliang
@file: study_tcp_01_client.py
@time: 2021/7/13 9:09 
"""
import socket


def send_file_2_client(new_client_socket, client_addr):
    # 接收客户端 要下载的文件名
    file_name = new_client_socket.recv(1024).decode("gbk")
    print("客户端（%s）需要下载文件是: %s " % (str(client_addr), file_name))

    file_content = None
    # 打开这个文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as e:
        print("没有要下载的文件 (%s)" % file_name)

    # 发送数据给客户端
    if file_content:
        print(len(file_content))
        new_client_socket.send(file_content)


def main():
    # 1. 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息 bind
    tcp_server_socket.bind(("192.168.1.7", 8099))

    # 3. 让默认的套接字由主动变为被动  listen
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待客户端的链接 accept
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 5. 调用发送文件函数
        send_file_2_client(new_client_socket, client_addr)


        # 6. 关闭套接字
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
