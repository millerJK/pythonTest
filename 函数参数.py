# 位置参数
def test(name):
    print("你好, %s" %  name)


test("小米")


# 多次方
def power(x, y):
    total = 1;
    for num in range(y):
        total *= x;
    return total;


print(power(2, 3));


# 默认参数 :  默认参数存在就不需要重载
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
    print("--------start--------")
    for c in args:
        print(c)
    print("--------end--------")

calc(1, 2, 3, 4);
numbs = list(range(5))
calc(*numbs)
calc(numbs[0],numbs[1],numbs[2])
numbss = tuple(range(5));
calc(*numbss)
calc(*{1, 2, 3, 4})


# 关键字参数：允许传入0个或任意个参数名的参数，这些关键字参数在函数内部自动组装为一个dict 字典
def person(name, age, **kwargs):
    print(name, age, kwargs);


person("周星驰", 12)
person("周星驰", 23, hello=12);
extra = {"city": "北京", "job": "engineer"};
person("周星驰", 23, city=extra["city"], job=extra["job"])
person("周星驰",23,**extra);

