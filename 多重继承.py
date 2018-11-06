class Animal(object):
    pass

# 大类:   哺乳动物
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#类似于接口（在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。）
class RunnableMixIn(object):
    def run(self):
        print('Running...')

#类似于接口
class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

# 各种动物:
class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, RunnableMixIn):
    pass

class Parrot(Bird, FlyableMixIn):
    pass

class Ostrich(Bird):
    pass

parrpt = Parrot();
parrpt.fly();

