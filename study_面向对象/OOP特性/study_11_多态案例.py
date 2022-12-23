# https://www.bilibili.com/video/av14184325?p=405
'''
多态  不同的子类对象调用相同的父类方法，产生不同的执行结果
    多态可以增加代码的灵活度
    以 继承 和 重写父类方法 为前提
    是调用方法的技巧， 不会影响到类的内部设计

'''

class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)

class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()

# 1. 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)



# https://www.bilibili.com/video/av14184325?p=406
