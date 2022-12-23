class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了 " % self.name)

    # 对象被销毁前做的最后一个方法
    def __del__(self):

        print("%s 我去了 " % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫 [%s] " % self.name


tom = Cat("Tom")
print(tom) #默认输出 <__main__.Cat object at 0x000001B9E43B8208> __str__会改变输出



