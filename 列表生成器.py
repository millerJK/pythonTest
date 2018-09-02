list(range(5))
print(list(range(5)))

L = [x * x for x in range(5)]
print(L)

L = [x * x for x in range(0, 11) if x % 2 == 0]
print(L)

# 大写转换为小写
L = ["Micheal", "Jack", "Miller"]
print([s.lower() for s in L])
