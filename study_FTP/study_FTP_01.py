"""
@author: wanghongliang
@file: study_FTP_01.py
@time: 2021/8/2 14:44 
"""
# https://www.cnblogs.com/lucky-heng/p/11198338.html
# https://www.cnblogs.com/rainbow-tan/p/13998528.html  下载文件夹参考这个博客
from ftplib import FTP


def upload_file(f, remote_path, local_path):
    fp = open(local_path, "rb")
    buf_size = 1024
    f.storbinary("STOR {}".format(remote_path), fp, buf_size)
    fp.close()


def download_file(f, remote_path, local_path):
    fp = open(local_path, "wb")
    buf_size = 1024
    f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
    fp.close()


def main():
    ftp = FTP()
    ftp.connect("10.87.106.137", 21)  # 第一个参数可以是ftp服务器的ip或者域名，第二个参数为ftp服务器的连接端口，默认为21
    # ftp.login(username, password)
    ftp.login("temp", "temptemp")  # 匿名登录直接使用ftp.login()
    ftp.cwd("/temp/Blake/ftp_study")  # 切换到tmp目录
    # ftp   在ftp中的名字   在电脑中地址
    upload_file(ftp, "python-3.9.0-amd64.exe", r"F:\软件\Python\python3\64\python-3.9.0-amd64.exe")

    ftp.quit()


if __name__ == '__main__':
    main()
