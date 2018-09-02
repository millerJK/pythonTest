# 位置参数
def test(name):
    print("你好", name)


test("小啊")


# 多次方
def power(x, y):
    total = 1;
    for num in range(y):
        total *= x;
    return total;


print(power(2, 3));


# 默认参数
def power2(x, y=2):
    total = 1;
    for num in range(y):
        total *= x;
    return total;


print(power2(2));


# 存在多个默认参数时
def student(name, age="12", sex="男"):
    print(name, age, sex);


student("阿灿");
# 通过指定默认参数值
student("acan", sex="女")


# 可变参数 (接受列表 元组 和 set 集合)
def calc(*args):
    sum = 0;
    for n in args:
        sum = sum + n * n
    print(sum)


calc(1, 2, 3, 4);
calc(*list(range(5)))
calc(*(1, 2, 3, 4))
calc(*{1, 2, 3, 4})


# 关键字参数
def person(name, age, **kwargs):
    print(name, age, kwargs);


person("周星驰", 12)
person("周星驰", 23, hello=12);
extra = {"city": "北京", "job": "engineer"};
person("周星驰", 23, city=extra["city"], job=extra["job"])
person("周星驰",23,**extra);

