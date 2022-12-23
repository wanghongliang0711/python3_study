def demo(*args, **kwargs):

    print(args)
    print(kwargs)

# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name":"王", "age":24}
demo(gl_nums, gl_dict)
# 输出：
# ((1, 2, 3), {'name': '王', 'age': 24})
# {}

demo(*gl_nums, **gl_dict)

demo(1, 2, 3, name = "王", age=24)




