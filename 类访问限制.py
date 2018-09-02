class Student(object):

    # self 参数使用 __ 表示私有参，外部是不可以调用属性值进行修改
    def __init__(self, name, score):
        self.__name = name;
        self.__score = score;

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
        print(self.__name, self.__score)

    def getScore(self):
        if (self.__score >= 90):
            return 'A';
        elif (self.__score >= 80):
            return 'B';
        else:
            return 'C';


student = Student("jack", 89);
student.toString()
print(student.get_name())
student.set_name("是")
student.set_score(1000)
student.toString()
