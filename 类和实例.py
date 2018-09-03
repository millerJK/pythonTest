class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def toString(self):
        print(self.name, self.score)

    def getScore(self):
        if (self.score >= 90):
            return 'A'
        elif (self.score >= 80):
            return 'B'
        else:
            return 'C'


bart = Student('jack', 23)
bart.toString()
print(bart.getScore())
bart.score = 24  # 可以通过调用类的属性直接修改属性值
bart.toString()
