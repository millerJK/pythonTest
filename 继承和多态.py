class Animal(object):
    def run(self):
        print("开始进行策马奔腾.....")


class Cat(Animal):
    pass


class Pig(Cat):
    pass


class Dog(Animal):
    def run(self):
        print("Dog is running .............")


class Duck(object):
    def run(self):
        print("stupid mother fuck")


cat = Cat();
cat.run();

pig = Pig();
pig.run();

dog = Dog();
dog.run();

a = list();
b = tuple();
c = int();
d = str();
e = dict();
f = set();

print(a);
print(b);
print(c);
print(d);
print(e);
print(f);

# 判断对象是否属于某种类型
print(isinstance(f, set))
print(isinstance(d, str))
