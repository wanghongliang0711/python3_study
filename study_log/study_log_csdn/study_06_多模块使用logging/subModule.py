"""
@author: blake.wang
@file: subModule.py
@time: 2021/10/25 15:36 
"""
import logging


module_logger = logging.getLogger("main.sub")


def eat(food):
    module_logger.info("eat " + str(food))


def sleep(time):
    module_logger.info("sleep " + str(time))

# eat("1")