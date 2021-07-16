"""
@author: wanghongliang
@file: test01_client.py
@time: 2021/7/14 9:55 
"""
import socket,time,json


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server.bind(("", 9999))

    tcp_server.listen(128)


    # 等待 链接
    print("等待一个新的客户端的到来。。。。")
    # tcp_server.settimeout(5)
    client_socket, client_addr = tcp_server.accept()
    print("client_addr: ", client_addr)
    json_data = dict(key1="rr", key2=5)
    while True:
        try:
            client_socket.settimeout(5)  # 针对接收数据有效
            print(client_socket.send(json.dumps(json_data).encode("utf-8")))
            time.sleep(1)
            client_socket.send(json.dumps(json_data).encode("utf-8"))
            # try:
            #     client_socket.recv(1024)
            # except Exception as e:
            #     print(e)`
        except Exception as e:
            print(e)
            break

    print("==================")
    client_socket.close()

    tcp_server.close()



if __name__ == '__main__':
    main()
