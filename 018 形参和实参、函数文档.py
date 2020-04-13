#def MyFirstFunction(name)中name是形参，因为这是个变量，不包含任何值
#MyFirstFunction(Minecraft)中Minecraft是实参，因为这是个具体的参数值
#在函数中用单引号括起来的字符串为函数的函数文档
def alert(alert):
    '打印出字符'
    print(alert)
#使用alert.__doc__输出函数文档
print(alert.__doc__)
#__doc__将不会换行，使用help()才会
def huanhan(name):
    '这是第一行\n这是第二行\n这是第三行'
help(huanhan)
#方法可以根据关键字索引
def Saysome(words,name):
    print(words+"——"+name)
Saysome(name = "你爸爸",words = "你妈死了")
#方法中可以添加默认值，即使不输入参数也可以输出值
def Normal(name = "dcs"):
    print(name+"你妈死了")
Normal()
#在形参前面加星号时输入的多个参数将会变为列表
#当加星号时方法有且只有一个形参
#若想添加多个形参，请手动添加关键字索引
def Multiple(*numbers):
    print("你一共输入了",len(numbers),"个参数")
Multiple("1123","13123213")
