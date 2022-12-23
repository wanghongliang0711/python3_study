class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print(addr)
print("%d" % addr)  # 十进制
print("%x" % addr)  # 十六进制


# ss = 99
# print(id(ss))