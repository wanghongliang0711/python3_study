"""
@author: wanghongliang
@file: study_04_日志回滚_按大小.py
@time: 2021/7/29 13:51 
"""
import logging, time
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)

"""             第一次                                第二次
log_04.txt      2021-07-29 14:21:59,397 - __main__   2021-07-29 14:27:06
log_04.txt.1    2021-07-29 14:21:57,387 - __main__   2021-07-29 14:27:04
log_04.txt.2    2021-07-29 14:21:53,384 - __main__   2021-07-29 14:27:00
log_04.txt.3    2021-07-29 14:20:03,099 - __main__   2021-07-29 14:21:59
"""

#定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
# rHandler = RotatingFileHandler("log_04.txt",maxBytes = 1*1024,backupCount = 3)
rHandler = RotatingFileHandler("log_04.txt",maxBytes = 100, backupCount = 3)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(rHandler)
logger.addHandler(console)

logger.info("Start print log Start print log Start print log Start print log")
time.sleep(2)
logger.debug("Do something")
time.sleep(2)
logger.warning("Something maybe fail. Something maybe fail. Something maybe fail. Something maybe fail.")
time.sleep(2)
logger.info("Finish Finish Finish Finish Finish Finish")