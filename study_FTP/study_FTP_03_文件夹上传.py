"""
@author: blake.wang
@file: study_FTP_03_文件夹上传.py
@time: 2021/9/30 14:30 
"""
import os
from ftplib import FTP


# 登录 ftp
def login_ftp():
    try:
        ftp = FTP()
        ftp.connect("10.87.xxx.xxx", 21)
        ftp.login("xxx", "xxxxxx")
        return ftp
    except Exception as e:
        print("login_ftp error. message: ", e)


def upload_file(f, remote_path, local_path):
    try:
        fp = open(local_path, "rb")
        buf_size = 1024
        f.storbinary("STOR {}".format(remote_path), fp, buf_size)
        fp.close()
    except Exception as e:
        print("upload_file error. message: ", e)


def upload_dir(ftp, remote_path, local_path):
    try:
        ftp.cwd(remote_path)
        get_dir = os.listdir(local_path)
        for i in get_dir:
            sub_dir = os.path.join(local_path, i)
            if os.path.isdir(sub_dir):
                ftp.mkd(i)
                ftp_remote_path = remote_path + "/" + i
                upload_dir(ftp, ftp_remote_path, sub_dir)
            else:
                upload_file(ftp, i, sub_dir)
    except Exception as e:
        print("upload_dir error. message: ", e)


def main(app_ver, folder_path):
    try:
        ftp = login_ftp()
        root_path = "/RDrelease/ADAS_Video/xxxxxxxx-Videos/Test Report Log"
        ftp.cwd(root_path)
        app_list = ftp.nlst()
        if app_ver not in app_list:
            ftp.mkd(app_ver)
        ver_path = root_path + "/" + app_ver
        ftp.cwd(ver_path)
        folder_path_split = os.path.split(folder_path)
        ftp.mkd(folder_path_split[1])
        upload_dir(ftp, ver_path + "/" + folder_path_split[1], folder_path)
        ftp.close()
    except Exception as e:
        print("Upload_to_FTP error. message: ", e)

# main("1.2.46.12", r"F:\001-blake-Study\python\python-tool\Demo_app_tool\ADAS_Auto_Test\ADAS_Auto_Test_R04\video\case_test01\1.2.46.12_20210930_143331_case_test01")