from collections.abc import Iterable

print(isinstance("abc", Iterable))


for i, value in enumerate(['a', 'b', 'c']):
    print(i, value);


name = {"Micheal": 23, "jack": 21, "Miller": 34}
keys = [1, 2, 3]
for i, value in enumerate(name):
    print(i, value)
    print(i, keys[i])
