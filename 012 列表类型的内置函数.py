#count 检查一个数在列表里出现了几次
number = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2]
print(number.count(1))
#index 检索数组中的某个值第一次出现在哪个位置
print(number.index(2))
#限定范围
number2 = [1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2]
print(number2.index(2,4,8))
#reverse 来过倒组数把
number3 = [1,2,3,4,5,6,7,8,9]
number3.reverse()
print(number3)
#sort 根据指定参数对数组排序，默认从小到大
number4 = [1,6,3,5,3,2,3,5,6,12,431,321,321,21,45,32,65]
number4.sort()
print(number4)
#从大到小排序
number4.sort(reverse=True)
print(number4)