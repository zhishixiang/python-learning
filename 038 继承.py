#class中可以指定一个对象继承的父类
class Parent:
    def hello(self):
        print("正在调用父类的方法")
class Child(Parent):
    pass
#现在调用父类的方法
p = Parent()
p.hello()
#由于子类继承了父类，所以子类也可以调用父类的方法
c = Child()
c.hello()
#如果子类包含和父类同名的方法，那么会默认调用子类的方法，父类不会被改变
class Child(Parent):
    def hello(self):
        print("正在调用子类的方法")
#由于子类已经包含了hello这个方法，所以子类不会继承父类的hello方法
c = Child()
c.hello()
#父类不会被改变
p = Parent()
p.hello()
#这里举的是上节课的例子
#先调用随机数
import random as r
class Fish:
    def __init__(self):
        #这里设置每条鱼的生成位置
        self.x = r.randint(1,10)
        self.y = r.randint(1,10)
    def move(self):
        self.x -= 1
        print("当前的x坐标为:",self.x,self.y)
class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("开始捕食")
            self.hungry = False
        else:
            print("不需要捕食")
#调用方法
fish = Fish()
fish.move()
fish.move()
goldfish = Goldfish()
goldfish.move()
goldfish.move()
shark = Shark()
shark.eat()
shark.eat()
#由于Shark子类重写了父类的init方法，所以父类的x和y不会被继承过来
#想要重写方法的同时也可以继承父类，有两种方法
#第一种是重新调用一次方法
class Shark(Fish):
    def __init__(self):
        self.hungry = True
        Fish.__init__(shark)
    def eat(self):
        if self.hungry:
            print("开始捕食")
            self.hungry = False
        else:
            print("不需要捕食")
shark = Shark()
shark.move()
#还有一种方法试试使用super函数
#这里使用会报错，原因未知
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("开始捕食")
            self.hungry = False
        else:
            print("不需要捕食")
shark = Shark2()
shark.move()
#python还可以继承多个父类，只需在使用class新建函数时传入多个参数即可