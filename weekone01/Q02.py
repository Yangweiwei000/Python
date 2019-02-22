# 2. 编写程序，生成一个包含50个随机整数的列表，随机整数的范围是从-10到10，然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表。（15分：生成随机列表5分，得出正负数新列表各5分）
import random
# 空列表
list = []
# 生成一个包含50个随机整数的列表随机整数的范围是从-10到10
for i in range(50):
    num = random.choice(range(-10,11))
    list.append(num)
# 生成随机列表
print(list)
z = []
f = []
#分开正负列表
for i in list:
    if(i>0):
        z.append(i)
    elif(i<0):
        f.append(i)

print(z)
print(f)