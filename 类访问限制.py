class Student(object):

    # self 参数使用 __ 表示私有属性，外部是不可以直接调用属性的，只能通过get set 的方法修改属性
    #  __age__ 不是私有属性，对象还可以直接调用属性进行赋值  __name 才是私有属性
    def __init__(self, name, score, age):
        self.__name = name;
        self.__score = score;
        self.__age__ = age

    def get_name(self):
        return self.__name;

    def get_score(self):
        return self.__score;

    def set_name(self, name):
        self.__name = name;

    def set_score(self, score):
        if score <= 100 and score > 0:
            self.__score = score;
        else:
            raise ValueError("数值不正确");

    def toString(self):
        print(self.__name, self.__score, self.__age__)

    def getScore(self):
        if (self.__score >= 90):
            return 'A';
        elif (self.__score >= 80):
            return 'B';
        else:
            return 'C';


student = Student("jack", 89, 23);
student.toString()
print(student.get_name())
student.set_name("是")
student.set_score(100)
student.toString()
student.__age__ = 12;
student.toString()
