def test(name):
    if name == '小明':
        print("欢迎您")
    else:
        print("不知道您在说什么")


test("阿花")


# 写架构的时候，在定义方法的时候先定义方法，暂不实现方法可以使用pass
def firstBlood(strs):
    pass


print(firstBlood("哈哈"))


# 函数返回多个值
def move(x, y):
    return x, y


x, y = move(4, 5);
print("函数返回多个结果：x: %d  y:%d" %(1,2))
