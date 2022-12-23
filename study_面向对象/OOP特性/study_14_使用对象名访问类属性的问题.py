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
# print(Tool.count)
tool3.count = 99
print(tool3.count)  # 先在实例属性中查找，查找不到去类属性中查找，再找不到就报错
print("===> %d " % Tool.count)


