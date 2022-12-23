class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了 " % self.name)

    # 对象被销毁前做的最后一个方法
    def __del__(self):

        print("%s 我去了 " % self.name)


tom = Cat("Tom")
print(tom.name)


print("*" * 50)
# del关键字可以删除一个对象
del tom

print("*" * 50)