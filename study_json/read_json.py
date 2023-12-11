"""
@author: blake.wang
@file: read_json.py
@time: 2023/12/11 14:05 
"""
import json

# with open结构是一种推荐的方式，它能够自动处理文件的打开和关闭，并提供更好的异常处理。


# 读取JSON文件  --- 为指定编码，只能读取 ASCII格式的数据，不然中文会出错
with open('data.json', 'r') as file:
    data = json.load(file)
# 使用读取的数据
print(data)


# 读取JSON文件（指定编码格式）
with open('data1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# 使用读取的数据
print(data)


# 读取JSON文件
file = open('data2.json', 'r', encoding='utf-8')
data = json.load(file)
file.close()
# 使用读取的数据
print(data)


# 读取JSON文件（指定编码格式）
with open('data3.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# 使用读取的数据
print(data)


# 解析 JSON 字符串为 Python 对象
json_str = '{"name": "John1", "age": 301, "city": "中国"}'
# 解析 JSON 字符串为 Python 对象
data = json.loads(json_str)
print(data)




