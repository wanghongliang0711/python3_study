"""
@author: blake.wang
@file: save_json.py
@time: 2023/12/11 13:54 
"""
import json

# with open结构是一种推荐的方式，它能够自动处理文件的打开和关闭，并提供更好的异常处理。


# 要保存的数据
data = {
    'name': '张三',
    'age': 30,
    'city': 'New York'
}
# 保存为JSON文件  -- 中文会被转义为 ASCII
with open('data.json', 'w') as file:
    json.dump(data, file)


# 要保存的数据
data1 = {
    'name': '张三',
    'age': 30,
    'city': '北京'
}
# 保存为JSON文件（指定编码格式）  -- 中文能正常保存
with open('data1.json', 'w', encoding='utf-8') as file:
    json.dump(data1, file, ensure_ascii=False)



# 要保存的数据
data2 = {
    'name': '张三',
    'age': 30,
    'city': '北京'
}
# 保存为JSON文件
file = open('data2.json', 'w', encoding='utf-8')
json.dump(data2, file, ensure_ascii=False)
file.close()


# 要保存的数据
data3 = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    "data3": {
    'name': 'John',
    'age': 30,
    'city': 'New York'
    }
}
# 保存为 JSON 文件，并进行换行
with open('data3.json', 'w', encoding='utf-8') as file:
    json.dump(data3, file, indent=2, ensure_ascii=False)


# 将 Python 对象转换为 JSON 字符串
data = {"name": "张三", "age": 30, "city": "北京"}
json_str = json.dumps(data, ensure_ascii=False)  # 将 Python 对象转换为 JSON 字符串，保留中文字符的原始形式
print(json_str)
json_str = json.dumps(data)  # 中文字符会被转义为 Unicode 转义序列
print(json_str)
