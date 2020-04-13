#递归≈套娃，指在函数中调用自己
def recursion():
    return recursion()
#直接运行的话你会发现根本停不下来，因为没有传参
#recursion()
#python3中为了防止电脑爆炸，设置了递归的深度为100层
#但仍然可以通过某些神奇的办法调节深度
import sys
sys.setrecursionlimit(10000)
#recursion()
#一个简单的例子
def jieceng(x):
    result = x
    for i in range(1,x):
        result *= i
    return result
y = int(input('请输入一个数字'))
result = jieceng(y)
print("%d 的阶乘是 %d"%(y,result))
#下面的是递归版本
def digui(x):
    if x == 1:
        return 1
    else:
        return x * digui(x-1)
number = int(input("请输入一个整数"))
result2 = digui(number)
print(("%d 的阶乘是 %d")%(number,result2))
#一脸懵逼中