class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

        # 让类属性的值+1
        Tool.count += 1

# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("斧头1")
tool3 = Tool("斧头2")
# 2. 输出工具对象的总数
print(Tool.count)
print(id(Tool))
print(id(tool1))
print(id(tool2))
print(tool2.count)

def my_test(tool_class):
    print(id(tool_class))
    print(tool_class.count)


my_test(Tool)

# https://www.bilibili.com/video/av14184325?p=409
