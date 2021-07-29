"""
@author: wanghongliang
@file: study_02_将日志写入到文件.py
@time: 2021/7/29 13:20 
"""
# https://blog.csdn.net/pansaky/article/details/90710751
import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

handler = logging.FileHandler("log_02.txt")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")

