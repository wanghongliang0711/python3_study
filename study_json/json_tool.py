"""
@author: blake.wang
@file: json_tool.py
@time: 2023/12/11 14:15 
"""
import json


class JSONTool:
    @staticmethod
    def read_json(file_path):
        """
        读取 JSON 文件并返回解析后的 Python 对象
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def write_json(file_path, data):
        """
        将 Python 对象写入 JSON 文件
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

# 示例用法
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

JSONTool.write_json('output.json', data)
loaded_data = JSONTool.read_json('output.json')

# 打印读取的数据
print(loaded_data)
