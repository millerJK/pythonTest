class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    #和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self,并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别
    def toString(self):
        print(self.name,self.score)

    def getScore(self):
        if (self.score >= 90):
            return 'A'
        elif (self.score >= 80):
            return 'B'
        else:
            return 'C'


bart = Student('jack', 23)
print(bart)
bart.toString()
print(bart.getScore())
bart.score = 24  # 可以通过调用类的属性直接修改属性值
bart.toString()
