"""
@author: wanghongliang
@file: study_04_日志回滚_按大小.py
@time: 2021/7/29 13:51 
"""
# https://www.cnblogs.com/andy9468/p/8378492.html

import time, re
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler


"""
注意：filehanlder.suffix的格式必须这么写，才能自动删除旧文件，如果设定是天，
就必须写成“%Y-%m-%d.log”，写成其他格式会导致删除旧文件不生效。 
    这个可以直接看源码：
        if self.when == 'S':
            self.interval = 1 # one second
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(\.\w+)?$"
        elif self.when == 'M':
            self.interval = 60 # one minute
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}(\.\w+)?$"
这个配置在源码里能看出来，但是在官方文档并没有说明这一点！！！！！！！！！！

TimedRotatingFileHandler的构造函数定义如下:
TimedRotatingFileHandler(filename [,when [,interval [,backupCount]]])
filename 是输出日志文件名的前缀，比如log/myapp.log
when 是一个字符串的定义如下：
“S”: Seconds
“M”: Minutes
“H”: Hours
“D”: Days
“W”: Week day (0=Monday)
“midnight”: Roll over at midnight
interval 是指等待多少个单位when的时间后，Logger会自动重建文件，当然，这个文件的创建
取决于filename+suffix，若这个文件跟之前的文件有重名，则会自动覆盖掉以前的文件，所以
有些情况suffix要定义的不能因为when而重复。
backupCount 是保留日志个数。默认的0是不会自动删除掉日志。若设3，则在文件的创建过程中
库会判断是否有超过这个3，若超过，则会从最先创建的开始删除。
"""
logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

# interval 是指等待多少个单位when的时间后，Logger会自动重建文件
# timefilehandler = TimedRotatingFileHandler("log_05.txt", when='M', interval=1, backupCount=1)
timefilehandler = TimedRotatingFileHandler("log_05.txt", when='S', interval=60*60*24, backupCount=1)  # 一天
# 设置后缀名称，跟strftime的格式一样
# timefilehandler.suffix= "%Y-%m-%d_%H-%M-%S.log"
# timefilehandler.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$"
# timefilehandler.extMatch = re.compile(timefilehandler.extMatch)
""" timefilehandler.suffix 设置后删除失败，原因：
https://blog.csdn.net/qgf1099062139/article/details/83619280

fh = logging.handlers.TimedRotatingFileHandler("log", when='S', interval=1, backupCount=3)
fh.suffix = "%Y-%m-%d_%H-%M-%S.log"
fh.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$"
fh.extMatch = re.compile(fh.extMatch)
"""

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
timefilehandler.setFormatter(formatter)

logger.addHandler(timefilehandler)

while True:
    logger.info("test")
    time.sleep(10)
################################
#
# # logging初始化工作
# logging.basicConfig()
#
# # myapp的初始化工作
# myapp = logging.getLogger('myapp')
# myapp.setLevel(logging.INFO)
#
# # 添加TimedRotatingFileHandler
# # 定义一个1秒换一次log文件的handler
# # 保留3个旧log文件
# timefilehandler = logging.handlers.TimedRotatingFileHandler("myapp.log", when='S', interval=1, backupCount=3)
# # 设置后缀名称，跟strftime的格式一样
# timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
#
# formatter = logging.Formatter('%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s')
# timefilehandler.setFormatter(formatter)
# myapp.addHandler(timefilehandler)
#
# while True:
#     time.sleep(0.1)
#     myapp.info("test")
