"""
@author: wanghongliang
@file: study_qrcode_02.py
@time: 2021/8/18 13:16 
"""
import qrcode
# 调用qrcode的make()方法传入url或者想要展示的内容
img = qrcode.make("华为P8")

img.save("华为P8.png")

# https://www.jianshu.com/p/c0073c6aa544
