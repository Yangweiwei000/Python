#输入两个人的生日，比较两个人年龄大小
# print("请输入a的年龄:")
# a = input()
# print("请输入b的年龄:")
# b = input()
# if(a>b):
#     print("a的年龄大")
# elif(b>a):
#     print("b的年龄大")
# else:
#     print("a与b的年龄相等")
#.随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中

#-----------------------------分割-----------------------------
import random
A = []
for i in range(10):
    a = random.choice(range(10))
    A.append(a)
print(A)
b = random.choice(range(10))
if b in A:
    print(b)
    print("有")
else:
    print(b)
    print("没有")