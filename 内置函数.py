from functools import reduce

# 绝对值
print(abs(-19))
# 获取最大值
print(max(1, 2, 6, 4, 9))
print(max(1, 2, 4, 6, 9, 1, 2))


# 高阶函数

# map map()函数接收两个参数，一个是函数,函数只能接受一个参数，一个是Iterable
def fuc(x):
    return x * x;


r = map(fuc, [1, 2, 3, 4])  # map 返回的依旧是iterator
print(list(r))
print(list(map(str, [1, 2, 3, 4])))


def fuc1(x, y):
    return x * y;


print(reduce(fuc1, [1, 2, 3, 4, 5]))  # 返回一个value

# string  to  int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(content):
    def fn(x, y):
        return x * 10 + y;

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, content))


print(str2int("1234623"))


# filter   过滤      和map()类似，filter()也接收一个函数和一个序列

def is_odd(x):
    return x % 2 == 1

print(list(filter(is_odd,{1,2,4,5})))


numbers = list(sorted((1,3,2,3,4)));
print(list)
