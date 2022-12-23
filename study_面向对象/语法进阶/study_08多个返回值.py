def measure():
    """测量温度和湿度"""
    print("测量开始。。。")
    temp = 39
    wetness = 50
    print("测量结束。。。")
    #元祖可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    # 如果函数返回的类型是元祖，向括号可以省略
    # return (temp, wetness)
    return temp, wetness
result = measure()
print(result)

print(result[0])
print(result[1])

# 可以一次接受返回结果
#注意： 使用多个变量接受结果时，变量的个数应该和元祖中元素的个数保持一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)



