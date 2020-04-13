#在python中任何值都是对象
#说得好像学了python我就有对象一样o(╥﹏╥)o
#在方法中你甚至可以直接返回一个对象
def FuncX(x):
    def FuncY(y):
        return x * y
    return FuncY
print(type(FuncX(1)))
#以下是闭包的用法
#在以下语句中，8是给FuncX的参数,5是给FuncY的参数
#我也不怎么懂，以后再慢慢看
i = FuncX(8)
print(i(5))
#你也可以这样调用
print(FuncX(8)(5))
#在变量中更高一级的变量对于第一级的变量来说相当于全局变量，因此当下一级新建一个变量时上级的变量会被屏蔽
#下一级的变量将成为局部变量，因此无法读取上一级创建的变量
#下属不可以啵上司嘴
"""
def Func1():
    x = 5
    def Func2():
        x *= x
        return x
    return Func2()
print(Func1()
"""
#当变量存放在栈内时会出现这个错误，但如果变量存放在容器类型就不会出现这个错误
def Func1():
    x = [5]
    def Func2():
        x[0] *= x[0]
        return x[0]
    return Func2()
print(Func1())
#添加nonlocal参数可以声明x在方法内不是局部变量，也可以避免这个问题
#不要使用global参数
def Func1():
    x = 5
    def Func2():
        nonlocal x
        x *= x
        return x
    return Func2()
print(Func1())