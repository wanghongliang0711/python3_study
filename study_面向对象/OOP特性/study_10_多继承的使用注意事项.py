class A:
    def __init__(self):
        print("初始化 A")

    def test(self):
        print("A ---- test 方法")

    def demo(self):
        print("A ---- demo 方法")

class B:
    def __init__(self):
        print("初始化 B")

    def test(self):
        print("B ---- test 方法")

    def demo(self):
        print("B ---- demo 方法")

class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""

    pass

c = C()

c.test()
c.demo()

# 确定C类对象调用方法的顺序
print(C.__mro__)

