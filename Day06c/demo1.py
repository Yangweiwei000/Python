# 新建文件夹
f=open('test.txt','w')
# 关文件
f.close()

# 向空文件写数据
f = open('test.txt','w')
f.write("hello binhe")
f.close()

# 读数据
f = open('test2.txt','w')
f.close()

# 开始读
f = open('test.txt','r')
num = f.read(12)
print(num)
f.close()

# 写到第二个文件中
f = open('test2.txt','w')
f.write(num)
f.close()