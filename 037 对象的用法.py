#新建一个对象
class Ball:
    def setName(self,name):
        self.name = name
    def kick(self):
        print("我叫%s,该死的，谁踢我。。。" % self.name)
#调用对象
a = Ball()
a.setName("球A")
b = Ball()
b.setName("球B")
c = Ball()
c.setName("土豆")
a.kick()
b.kick()
c.kick()
#__init__指当对象创建时立刻做某事
#看不懂
#重写一遍方法
class Ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print("我叫%s,该死的，谁踢我。。。" % self.name)
a = Ball("土豆")
a.kick()
#先暂时这样理解：__init__指的是直接传进Ball的参数都会被传入__init__
#以后理解了再来改
#在变量前加两个下划线可以隐藏变量，这样在方法外部就无法直接访问变量
class Person:
    __name = "zhishixiang"
    def getName(self):
        return self.__name
p = Person()
#p.name
print(p.getName())
#隐藏的变量可以通过另一种方法访问
print(p._Person__name)