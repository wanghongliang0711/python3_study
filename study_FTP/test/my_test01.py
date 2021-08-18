"""
@author: wanghongliang
@file: my_test01.py
@time: 2021/8/3 14:45 
"""
from PIL import ImageGrab

# 截取windows屏幕
im = ImageGrab.grab()
im.save('path-to-save.png', 'png')
