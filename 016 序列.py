#迭代是指重复反馈过程的活动
#list() 将字符串分片存储为列表
a = list()
print(a)
b = "I love FishC.com"
b = list(b)
print(b)
#list还可以将元组变成列表
#斐波那契数列
c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
c = list(c)
print(c)
#tuple() 将可迭代的列表转换为元组
#len() 返回一个列表的长度(包含几个值)
print(len(c))
#max() 返回参数里面的最大值
#数字和英文都是根据ASCII码排序
#如果为汉字则根据国标unicode排序
#只能为同一类型的参数排序，不能排序混合参数
print(max(1,2,3,4,5,6,7,8,9))
print(max(b))
#min() 返回参数的最小值 懒得举例了
#sum(iterable[,start=0]) 返回序列iterable和可选参数start的总和
#只能用于整数和浮点数
tuple1 = (2.1,3.1,5.2,5.6)
print(sum(tuple1)) 
#sorted() 给列表排序
print(sorted(tuple1))
#reversed() 把列表倒过来
#如果没有加list则返回列表的对象
print(reversed(tuple1))
print(list(reversed(tuple1)))
#enumerate() 以列表内的元组的形式返回列表每个值的位置
#不加list时也会返回列表的对象
print(list(enumerate(tuple1)))
#zip() 拼合列表
a = [1,2,3,4,5,6]
b = [7,8,9,10,11,12]
print(list(zip(a,b)))