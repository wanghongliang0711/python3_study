def sun_numbers(num):

    # 1. 出口
    if num == 1:
        return 1

    # 2. 数字的累加 num + (1...num-1)
    temp = sun_numbers(num - 1)
    return num + temp

result = sun_numbers(3)
print(result)
