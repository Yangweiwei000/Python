# 1.用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.判断手机号码是否是由数字组成的(总分15分，5分能够判断是否为数字，5分判断是否为有效号段，5分实现)

#输入手机号
p = input("请输入手机号:")
list = [185,137,176,189,157,158]
try:
    #判断是否为纯数字
    int(p)
    #判断手机号长度
    if (len(p)==11):
        #通过异常判断手机号是否为数字
        head = p[0:3]
        bool = False
        for i in list:
            if (int(head)==(i)):
                bool = True
                break
        if (bool):
            print("有效手机号")
        else:
            print("无效手机号")
    else:
        print("输入的不是有效手机号")
except ValueError:
    print("输入的不是有效手机号")