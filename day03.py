#分别输入两个字符串，输入两个字符串的拼接字符串
# print("请输入第一个字符串:")
# var1 = input()
# print("请输入第二个字符串:")
# var2 = input()
# var2 = var1 + var2
# print("拼接后的结果为:" + var2)

# 输入一个数字，将接收到的值转换为int类型，并打印该变量的类型
# print("请输入一个数字:")
# var3 = float(input())
# print(type(int(var3)))

#函数
#abs返回绝对值
# print(abs(56))
#ceil向上取整
# import math
# print(math.ceil(4.1))
#exp返回e的x次幂
# import math
# print(math.exp(1))
#fabs返回数字的绝对值
# print(math.fabs(-10))
#floor向下取整
# print(math.floor(9.8))
#max返回给定参数的最大值
# print(max(89,56))
#min返回给定参数的最小值
# print(min(1,2,3,5,6,8))
#modf返回整数部分与小数部分
# print(math.modf(56.23))
#pow返回x**y的值 x的y次方
# print(pow(2,3))
#sqrt返回x的平方根
# print(math.sqrt(64))

#随机数函数
# import random
# print(random.choice(range(3)))
#random随机生成0-1范围之间的数
# print(random.random())
#shuffle将序列的所有元素随机排序
# list1 = [1,2,3,4]
# random.shuffle(list1)
# print(list1)
#uniform生成一个随机小数 范围在[x,y]中
# print(random.uniform(5,10))
#randint 生成一个范围内的随机整数
# print(random.randint(1,5))

#Python 字符串运算符
# a = "hello"
# b = "Python"
# print("a+b的拼接结果:" , a + b)
# print("a*2的输出结果:" , a * 2)
# print("a[1]的输出结果:", a[1])
# print("a[1:4]的输出结果:", a[1:4])

# 判断
# if("H" in a):
#     print("H在变量a中")
# else:
#     print("H不在变量a中")

# if("M" not in a):
#     print("M不在变量a中")
# else:
#     print("M在变量a中")

#str常用函数
# find 检测str1是否包含在str2中 如果是，返回下标 不是返回-1
# str1 = "hello world i am dajiba"
# print(str1.find("dajiba",0,50))#参数1检索的数据参数2开始的位置参数3结束的位置
# index 与find方法一样
# str1 = "hello world i am dajiba"
# print(str1.index("dajiba",0,30))
# count 检查str2在str1出现的次数
# str1 = "hello world i am dajiba"
# print(str1.count("i",0,25))
# replace 替换
# str1 = "hello world i am dajiba"
# print(str1.replace("l","*",3))
# spilt 切割 分割后的结果装在数组里
# str1 = "hello world i am dajiba"
# print(str1.split("o",2))
# capitalize 将字符串第一个变为大写其他的变成小写
# str1 = "hello World I am Dajiba"
# print(str1.capitalize())
# startswith 检查是否以x开头 返回值为True或者False
# str1 = "hello World I am Dajiba"
# print(str1.startswith("hello"))
# endswith 检查是否为x结尾 返回值为True或者False
# str1 = "hello World I am Dajiba"
# print(str1.endswith("ba"))
# lower 将大写转为小写
# str1 = "hello World I am Dajiba"
# print(str1.lower())
# upper 将小写转为大写
# str1 = "hello World I am Dajiba"
# print(str1.upper())
# ljust 将字符串从左边把长度填充到x
# s1 = "lkj"
# print(s1.ljust(10))
# rjust  将字符串从右边把长度填充到x
# a="Hello"
# print(a.rjust(10))

#list 列表
a = ['a','b','c']
# b = [1,2,3]
# c = ["abc","def","ghi"]
# print(a+b+c)
#检索列表  根据下标
# print(a[2])
#del删除列表元素
# del a[1]
# print(a)
#更新
# a[0] = 1
# print(a)

#元组
# tup1 = ('google','skdjajd',56,852)
# tup2 = (1,2,3,4,5,6,7,8)
# tup3 = "a","b","c","d"
# print(type(tup1))
# print(tup2[2])

#字典
# dic = {'name':'张三','sex':'男','age':'16'}
# print(dic['name'])
# print(dic['sex'])
# print(dic['age'])

#set 集合
# set1 = [1,2,3,5,2,5,1,5,8,9]
# 去重
# set1 = set(set1)
# print(set1)

# while
# i = 0
# sum = 0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

# 例如：打印
# *
# * *
# * * *
# * * * *
# * * * * *
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("* ",end="")
#         j += 1
#     print("")
#     i += 1


# name = ['abb','ana','lisa','zenan']
# for i in name:
#     if i == 'lisa':
#         print("包含lisa")
#         break
#     print(i)
# print("循环结束")

# name = ['abb','ana','lisa','zenan']
# for i in range(len(name)):
#     print(i,name[i])
# \

#实现100-200里面所有的质数字,打印这些质数并且求出个数
# i = 100
# sum = 0
# while i<200:
#     if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i%17!=0 and i%19!=0 and i%13!=0):
#         print(i)
#         sum += 1
#     i += 1
#
# print("个数为:" , sum)
# i = 10
# a = [1,2,2,3,5,5,8,6,4,4]
# for i in range(len(a)):
#     print(a[i])

# name=['Anna','Lucy','Jacob','Bunny']
# for i in name:
#     if i == "name[i]":
#         break
#     print(i)
# print("循环结束")

# 输入一个数a，求1+2!+3!+...+a!的和
# sum = 0
# fact = 1
# num = int(input('请输入一个数:'))
# for i in range(1,num+1):
#     fact = fact*i
#     sum += fact
# print(fact,sum)

# 函数 调用函数
# def ii():
#     print("-----------------")
#     print("|人生苦短及时行乐|")
#     print("-----------------")
# ii()

# 返回值

# def fact(a,b):
#     c = a+b
#     return (c)
# print(fact(12,15))

# 电脑随机生成1~100随机数，，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
import random
a = random.choice(range(1,100))
print(a)
while 1:
    #用户输入一个数
    b = int(input("请输入一个数: "))
    #判断
    if a>b:
        print("您输入的小了")
    elif a<b:
        print("您输入的数大了")
    else:
        print("恭喜你猜对了")
        #跳出
        break

