#bif指将序列的每一个元素做为函数的参数进行运算加工，直到可迭代的所有元素都加工完毕后返回加工后的元素构成新序列
#fliter()过滤器 可以过滤出不需要的内容
#fliter有两个参数，第一个是筛选条件，第二个是可迭代的参数
#fliter将会过滤任何非true的内容
print(list(filter(None,[1,0,2.32,True,False])))
#输出一个数组中的全部奇数
def odd(x):
    return x % 2
temp = range(0,10)
show = filter(odd,temp)
print(list(show))
#突然明白了点什么，再补充一下
#fliter第一个参数相当于一个漏斗，第二个参数相当于输入漏斗的物品
#在上面的内容中,temp的每个数输入odd时，都会计算一次，如果为奇数则输入1，偶数则输出0
#由于fliter会踢出0，而0对应的是偶数，所以偶数都会被踢出，自然只剩下奇数
#可以使用lambda来精简
print(list(filter(lambda x : x % 2,range(10))))
#map()为映射
#map有两个参数，map会把右侧所有可迭代的参数都输入左侧进行运算，最后输出结果
print(list(map(lambda x:x * 2,range(10))))