"""
@author: wanghongliang
@file: study_FTP_02_文件夹下载.py
@time: 2021/9/17 14:47
"""
import os
import shutil
from ftplib import FTP

# 创建文件夹
def make_dir(path):
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
    except Exception as e:
        print("make_dir error . message: ", e)


# 登录 ftp
def login_ftp():
    try:
        ftp = FTP()
        ftp.connect("10.87.106.137", 21)
        ftp.login("temp", "temptemp")
        return ftp
    except Exception as e:
        print("login_ftp error. message: ", e)


# 是否安装 APP
def is_install_app(ftp):
    try:
        ftp.cwd("/temp/Blake/ftp_study/app")
        app_list = ftp.nlst()
        if len(app_list) > 0:
            new_app = app_list[-1]
        else:
            print("ftp 中 一个APP也没有 ！！！")
            return False
    except Exception as e:
        print("is_install_app error. message: ", e)
        return False


# 获取路径的文件夹和文件
def get_dir_and_files(ftp, ftp_path):
    try:
        path_info = []
        folder = []
        files = []
        ftp.dir(ftp_path, path_info.append)
        for path in path_info:
            path = path.strip()
            filename = ftp_path + '/' + path.split(':')[1][3:]
            if path.startswith('-'):
                files.append(filename)
            elif path.startswith('d'):
                folder.append(filename)
        return folder, files
    except Exception as e:
        print("get_dir_and_files error. message: ", e)


def download_file(f, remote_path, local_path):
    try:
        fp = open(local_path, "wb")
        buf_size = 1024
        f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
        fp.close()
    except Exception as e:
        print("download_file error. message: ", e)


# 把 video 全部下载到本地
def download_folder(ftp, ftp_path, video_list, folder_list):
    try:
        dirs, all_file = get_dir_and_files(ftp, ftp_path)
        for one_dir in dirs:
            folder_list.append(one_dir)
            download_folder(ftp, one_dir, video_list, folder_list)
        for one_file in all_file:
            if one_file not in video_list:
                video_list.append(one_file)
    except Exception as e:
        print("download_folder error. message: ", e)


"""
ftp 下载 文件夹 已经完成
"""
def main():
    try:
        ftp = login_ftp()
        # is_install_app(ftp)
        shutil.rmtree(os.path.join(os.getcwd(),"video"), ignore_errors=True)
        make_dir(os.path.join(os.getcwd(),"video"))
        download_path = "/temp/Blake/ftp_study/video"
        if download_path.endswith("/"):
            download_path = download_path[:-1]
        video_list = []
        folder_list = []
        download_folder(ftp, download_path, video_list, folder_list)
        for one_file in video_list:
            local_path = os.path.join(os.getcwd(), "video") + one_file.replace(download_path, "", 1)
            make_dir(os.path.split(local_path)[0])
            download_file(ftp, one_file, local_path)
        for one_folder in folder_list:
            local_path = os.path.join(os.getcwd(), "video") + one_folder.replace(download_path, "", 1)
            make_dir(local_path)
    except Exception as e:
        print("Run error. message: ", e)


if __name__ == '__main__':
    main()
