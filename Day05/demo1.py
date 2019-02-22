# 通过用户输入数字，计算阶乘。（30分）
num = int(input("请输入一个数字"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
    i += 1
print(fact)