ss = s1, s2 = 100, 200
print(ss)
print(s1)
print(s2)


import time, datetime
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))

ss = "Total: 14 items"
print(ss.split(" "))


s1 = [1, 2, 3]
s2 = [1, 2, 3]
print(id(s1))
print(id(s2))
if s1 == s2:
    print("s1 == s2")
if s1 is s2:
    print("s1 is s2")

print(dir(s1))  # 查看内置的属性和方法

for i in range(100):
    if i == 4:
        print(i)
        break
else:
    print("else")


from test_message import send_message
send_message.send("888")




