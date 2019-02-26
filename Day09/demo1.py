# 列表numbers中存储了一组数，numbers = [ 1, 5, -12, 37, 6,93, 100 ]，
# 将这组数按照奇数偶数分别存储到两个列表even和odd中。
numbers = [ 1, 5, -12, 37, 6,93, 100 ]
even = []
odd = []
for i in numbers:
    if (numbers[i]%2==0):
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
print(even , odd)
