# 切片方便数据获取

# 针对列表
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0])  # 获取单个数据，从下标0开始

# 获取前三个数据
r = []
for i in L:
    r.append(i)
print(r)

print(L[:4])  # 获取前三个元素
print(L[1:4])
print(L[-2:])
print(L[:])  #甚至什么都不写，只写[:]就可以原样复制一个list
print(L[::-1]) #倒叙


# 针对元组

L = (1, 2, 3, 4, 5, 6)
print(L[::])  # 正序
print(L[::-1])  # 倒序

# 针对字符串
S = "abcdef"
print(S[0:3])
print(S[::-1])
