# 输出的成绩是ABCDE五档。其中，100——90输出A，
# 89——80输出B，79——70输出C，69——60输出D，
# 60分以下的输出E\
a = int(input("请输入成绩:"))
def sc(a):
    if(a>=90 and a<=100):
        print("A")
    elif(a>=80 and a<=89):
        print("B")
sc(a)