#花括号{}不只是代表字典，还代表集合
#创建集合的方式和创建列表类似
num1 = {1,2,3,4,5}
print(type(num1))
#集合中不存在重复的值，遇到重复的值时会只保留一个值
#集合具有唯一性
num2 = {1,2,3,4,5,4,3,2,1}
print(num2)
#集合不支持索引，所以无法筛选出具体位置中的值
#使用set函数也可以创建一个集合
set1 = set([1,2,3,4,5,5,4,3,2,1])
print(set1)
#使用for循环筛选出列表中的重复值
num1 = [1,2,3,3,1,3,1,2,3,4,1,2]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)
#使用集合筛选列表中的重复值
#注意：集合得到的值是无序的
num1 = list(set(num1))
#集合可以使用add()和remove()修改元素
#注意：add是从右开始的
num2 = {1,2,3,4,5,6}
num2.add(7)
num2.remove(4)
print(num2) 
#frozenset()可以冻结集合使集合无法被修改
num3 = frozenset([1,2,3,4,5,6,7])
#num3.add(8)