"""
@author: wanghongliang
@file: study_qrcode_01.py
@time: 2021/8/18 13:13 
"""
import qrcode
 # 调用qrcode的make()方法传入url或者想要展示的内容
# img = qrcode.make('http://www.baidu.com')
img = qrcode.make('blake.wang;001')
 # 写入文件
with open('test.png', 'wb') as f:
    img.save(f)
