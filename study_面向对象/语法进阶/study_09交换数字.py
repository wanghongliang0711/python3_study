a = 6
b = 100

# 解法1： -使用其他变量
# c = a
# a = b
# b = c

# 解法2： -不使用其他变量
# a = a + b
# b = a - b
# a = a - b


# 解法3 -Python 专有
# a, b = (b, a)
# 右面是元组， 只是省略了括号
a, b = b, a

print(a)
print(b)



