#关于拷贝和引用（指针既视感）
list1 = [9,8,6,4,5,6,7,8]
#下面是引用
list2 = list1
#下面是拷贝
list3 = list1[:]
#引用的值会随着被引用的值一起改变，拷贝则不会
list1.sort()
print(list1)
print(list2)
print(list3)
