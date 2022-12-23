class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0  # 类属性

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name  # 实例属性

        # 让类属性的值+1
        Tool.count += 1

# 创建工具对象
tool1 = Tool("斧头")
print(id(tool1))

tool2 = Tool("wang")
print(id(tool2))
# 调用类方法
Tool.show_tool_count()
tool1.show_tool_count()
