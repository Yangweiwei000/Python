import random
a = []
c = []
d = []

for i in range(1,51):#生成一个包含50个随机整数的列表
    b = random.choice(range(-10, 10))#随机整数的范围是从-10到10
    i += 1
    a.append(b)
    if b>=0:
        c.append(b)#正数存为一个新的子列表
    elif b<0:
        d.append(b)#负数存为另一个新的子列表
print(a)
print(c)
print(d)