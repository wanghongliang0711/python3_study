"""
@author: wanghongliang
@file: study_01.py
@time: 2021/7/28 14:44 
"""
# https://blog.csdn.net/pansaky/article/details/90710751
# https://blog.csdn.net/weixin_39759107/article/details/110773969
"""
python中日志等级从高到低依次为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
默认的日志等级为：WARNING，即在显示日志时，低于WARNING的日志不显示
"""
import logging

# logging.info('this is the info message')
# logging.debug('this is the debug message')
# logging.warning('this is the warning message')
# logging.error('this is the error message')
# logging.critical('this is the critical message')

""" print
WARNING:root:this is the warning message
ERROR:root:this is the error message
CRITICAL:root:this is the critical message
"""

# logging.basicConfig(filename='test.log',level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d %X')

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)


logger.info('this is the info message')

logging.debug('this is the debug message')
logging.warning('this is the warning message')
logging.error('this is the error message')
logging.critical('this is the critical message')


