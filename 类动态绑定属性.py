class Student(object):
    # 动态绑定属性，可以绑定任何动态属性，如果要使用的话使用__slots__
    __slots__ = ('name', 'age')


student = Student()
student.age = 12
print(student.age)

student.sex = "男"
print(student.sex)
