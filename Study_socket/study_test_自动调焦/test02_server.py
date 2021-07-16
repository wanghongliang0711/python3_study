"""
@author: wanghongliang
@file: test01_client.py
@time: 2021/7/14 9:55 
"""
import socket


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
        print(recv_data.decode("utf-8"))
        # client_socket.send("D:\\图片\\1.PNG\r\n".encode("utf-8"))
        data_len = client_socket.send("111.PNG".encode("utf-8"))
        print("data_len: ", data_len)

        file_content = None
        # 打开这个文件，读取数据
        try:
            f = open("111.PNG", "rb")
            file_content = f.read()
            f.close()
        except Exception as e:
            print("没有要下载的文件 (%s)" % "111.PNG")
        if file_content:
            print(len(file_content))
            data_len = client_socket.send(file_content)
            print("data_len_file: ", data_len)

        # print("发送 传输结束信息")
        # client_socket.send("picture over".encode("utf-8"))
        client_socket.close()

    tcp_server.close()



if __name__ == '__main__':
    main()
