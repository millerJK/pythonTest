# 列表遍历
classes = ['a', 'c', 'd', 'e']
for c in classes:
    print(c);

# 遍历元组
classes = ('a', 'c', 'd', 'e')
for c in classes:
    print(c);

# 字典遍历
names = {'Michael': 45, "Jack": 78, "Miller": 90}
for name in names:
    print(name)
    print(names.get(name))

# 遍历字符
name = '我是传奇';
for c in name:
    print(c);


# 1-100数字相加
sum =0
for  x in range(101):
    sum=sum+x
print(sum)




#while循环
n = 1
while n <= 100:
    print(n)
    if n == 10:
        break
    n = n + 1
print('END')


