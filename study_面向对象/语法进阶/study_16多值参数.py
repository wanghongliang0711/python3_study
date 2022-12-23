# 参数名前增加一个 * 可以接收元组
# 参数名前增加两个 * 可以接收字典
# 一般给多值参数命名是，习惯使用以下两个名字
#  *args --存放元组参数， 前面有一个 *
#  **kwargs --存放字典参数， 前面有两个 *

def demo(num, *nums, **persion):
    print(num)
    print(nums)
    print(persion)

# demo(1)
demo(1, 2, 3, 4, name="王", age=18)
demo(1, name="王", age=18)
