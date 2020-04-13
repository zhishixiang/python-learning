#在方法内使用global时局部变量将会变为全局变量
num = 10
def temp():
    global num
    num = 100
    print(num)
temp()
print(num)
#内嵌函数(套娃)
def func1():
    print("func1正在被调用")
    def func2():
        print("func2正在被调用")
    func2()
func1()