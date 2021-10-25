"""
@author: blake.wang
@file: subModule1.py
@time: 2021/10/25 15:43 
"""
import logging


module_logger = logging.getLogger("main.sub1")


def eat(food):
    module_logger.info("eat1 " + str(food))


def sleep(time):
    module_logger.info("sleep1 " + str(time))


