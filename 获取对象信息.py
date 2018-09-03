class Student(object):
    sex = "女"
    count = 0

    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        Student.count += 1;

    def toString(self):
        print(self.name, self.age)


student = Student("马克", 12);
student.toString();
print(student.sex)
print(Student.sex)
student = Student("马克思", 45);
print(student.count)

# 类属性和实例属性之前的区别：
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。


# 获取数据类型
print(type(student));
print(type(1));
print(type([1, 2, 3, 4]));
print(type({1, 2, 3, 4}))

# 数据类型判断
print(type(1) == int)
print(isinstance(1, int))
print(isinstance("aaa", str))
print(isinstance('a', (list, int, str)))  # 判断类型是不是给出类型中的一个

print(dir(student))  # 获取一个对象所有的属性和方法
