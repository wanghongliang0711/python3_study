class Cat:

    def __init__(self, new_name):

        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat("Tom")
print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
# 当使用类名()创建对象时，会自动执行以下操作
# 1. 为对象在内存中分配空间 --创建对象
# 2. 为对象的属性设置初始值 --初始化方法(__init__)
