#lambda也可以定义函数，但方式比def精简，用完即扔
def ds(x):
    return 2 * x + 1
print(ds(5))
lambda x : 2 * x + 1
#使用lambda函数也很简单
g = lambda x : 2 * x + 1
print(g(2))
#lambda也可以设置多个参数
add = lambda x, y : x + y
print(add(4,7))