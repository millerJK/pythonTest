#使用range便捷创建列表
list(range(5))
print(list(range(5)))
print(list(range(1,6)))

#---------------------------------------
L=[];
for  x in range(5):
    L.append(x*x)
print(L)

L = [x * x for x in range(5)]  #简写方式
print(L)

#----------------------------------------

L = [x * x for x in range(0, 11) if x % 2 == 0]
print(L)

# 大写转换为小写
L = ["Micheal", "Jack", "Miller"]
print([s.lower() for s in L])
