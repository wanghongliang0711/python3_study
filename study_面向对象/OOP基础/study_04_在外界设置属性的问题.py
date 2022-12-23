class Cat:

    def eat(self):
        # 哪一个对象调用的方法， self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)

# 创建猫对象
tom = Cat()

# .属性名 利用赋值语句就可以了 不推荐使用
# tom.name = "Tom"

tom.eat()
tom.drink()

tom.name = "Tom"

# https://www.bilibili.com/video/av14184325?p=372