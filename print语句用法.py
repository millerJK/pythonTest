print("哈哈");
print("哈哈 %s" % "你好")
print("你好","我是世界之王")
# 三个单引号不改变，不改变文本的格式
print('''
    百日依山尽，
    黄河入海流。
    欲穷千里目，
    更上一层楼。
''')

def move(x, y):
    return x, y

x, y = move(4, 5);
print("函数返回多个结果：x: %d  y:%d" %(1,2))