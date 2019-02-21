import random
a = []
num = 0
for i in range(1,21):#生成一个包含20个随机整数的列表
    b = random.choice(range(0,99))
    a.append(b)
    i += 1
    if i%2==0 :#偶数下标
        print(b)
print(a)