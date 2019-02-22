# 判断101-200之间有多少个素数，并输出所有素数。
sum = 0
for i in range(100,201):
    if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%13!=0 and i%11!=0 and i%17!=0 and i%19!=0):
        sum += 1
        print(i)
print(sum)