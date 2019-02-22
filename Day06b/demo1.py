# 新建一个文件
f = open('test.txt','w')
f.close()

# 使用write 向文件写入数据
f = open('test.txt','w')
f.write('hello wangaohua')
f.close()

# 读数据
f = open('test2.txt','w')
f.close()

# 开始读
f = open('test.txt','r')
num = f.read(16)
print(num)
f.close()

# 写到第二个文件中
f = open('test2.txt','w')
f.write(num)
f.close()
