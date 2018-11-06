from collections.abc import Iterable

#只要用isInstance进行判断返回为true 就代表该种类型可以使用for 循环
print(isinstance("abc", Iterable))
print(isinstance([1,2,3], Iterable)) # list是否可迭代


for i, value in enumerate(['a', 'b', 'c']):
    print(i, value);


name = {"Micheal": 23, "jack": 21, "Miller": 34}
keys = [1, 2, 3]
for i, value in enumerate(name):
    print(i, value)
    print(i, keys[i])
