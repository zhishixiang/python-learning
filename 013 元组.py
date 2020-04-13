#元组和列表用处相同，但是元组创建后无法被修改
#元组创建方法与列表不同，需要使用括号
tuple1 = (0,1,2,3,4,5,6,7,8,9)
#访问元组和访问列表的方式相同
print(tuple1[1])
#切片方式也和列表相同
print(tuple1[3: ])
#拷贝和引用也和列表一致，懒得写了自己想
#当元组被修改时会报错
#tuple1[1] = 3
#当元组只有一个值时，这个括号会被当成优先计算的函数
type1 = (1)
print(type1)
#即使没有小括号，为一个变量赋多个值时也会被默认为以元组形式添加(逗号是关键 )
type2 = 1,2,3,4,5,6,7,8
print(type(type2))
#添加空元组方法与添加空列表相同
type3 = ()
print(type(type3))
#若想要添加一个只有一个值的元组，请在值后面加一个逗号
type4 = (1,)
print(type(type4))
#元组的值无法被修改，但是可以重新赋值
numbers = (0,1,2,3,5,6,7)
numbers = numbers[ :4] + (4,) +numbers[4: ]
print(numbers)
#del可以删除元组
del numbers
print(numbers)