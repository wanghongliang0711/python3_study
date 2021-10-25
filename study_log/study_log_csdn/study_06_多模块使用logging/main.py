"""
@author: blake.wang
@file: main.py
@time: 2021/10/25 15:32 
"""
import logging, time
from logging.handlers import RotatingFileHandler
import subModule
import subModule1


logger = logging.getLogger("main")
logger.setLevel(level = logging.INFO)

# 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1*1024 K
rHandler = RotatingFileHandler("log_04.txt",maxBytes = 1*1024, backupCount = 3)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)

logger.addHandler(rHandler)


logger.info("start main log....")
subModule.eat("dog")
subModule1.sleep(11)
subModule1.eat("cat1")
subModule.sleep("10")
logger.info("end main log....")