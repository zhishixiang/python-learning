#对象包含属性和方法
class Turtle: # Python中的类名约定以大写字母开头
#关于类的一个简单例子
#属性
    color = ' green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'
#方法
    def climb(self):
        print('我正在很努力的向前爬.....')
    def run(self):
        print("我正在飞快的向前跑......")
    def bite(self):
        print("咬死你咬死你! ! ")
    def eat(self):
        print("有得吃，真满足^_ ^")
    def sleep(self):
        print("困了，睡了,晚安，Zzzz")
#调用对象前要先引用
tt = Turtle()
#调用对象内的方法
tt.climb()
#面向对象编程有一个特征是封装，可以让数据更加安全
#在调用对象方法时只会输出结果，无法看到具体是怎么实现的
#继承指子类自动共享父类的数据和方法
class MyList(list):
    #占位符，没有任何意义
    pass
list2 = MyList()
#由于MyList继承了list类，因此可以使用list类的任何方法
list2.append(3)
list2.append(5)
list2.append(7)
#多态指不同对象对同一方法响应不同的行动
#以下的例子貌似是错的，因为没有继承关系
class A:
    def fun(self):
        print("这是A")
class B:
    def fun(self):
        print("这是B")
a = A()
b = B()
a.fun()
b.fun()