#判断所输入的手机号，是否正确
# 用户输入


while 1:
    a = int(input("请输入您的电话号码:"))# 转为int

    try:
        if a < 10000000000:
            print("您的号码缺少")
        elif a > 19000000000:
            print("请输入正确的号码格式")
        else:
            print("格式正确")
            break
    except ValueError:
        print("请输入数字")