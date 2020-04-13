#工厂函数指python自带的函数
#例如int(),tuple(),str()这类
#fromkeys()可以在字典内批量导入键和值
#注意：当只导入键时值默认为none
dict1 = {}
print(dict1.fromkeys((1,2,3),'number'))
#一次只能设置一个值，因为所有的键都会被替换为设置的值且无法自动排序
print(dict1.fromkeys((1,2,3),('number1','number2','number3')))
#keys() 访问字典键的引用
#其实就是访问字典里面的键
dict1 = dict.fromkeys(range(20),'草')
for eachkey in dict1.keys():
    print(eachkey)
#valuse()则是访问字典里面的值
for eachvalues in dict1.values():
    print(eachvalues)
#items则是访问字典里面的键和值
for eachitems in dict1.items():
    print(eachitems)
#字典的访问是从0开始访问的，从1开始就会报错
print(dict1[19])
#get()也可以访问字典，但访问一个不存在的键时会返回一个空值
print(dict1.get(20))
#get可以加两个参数，第二个参数表示找不到键时返回的值
print(dict1.get(24,"找不到对象"))
#使用in和not in也可以判断字典中有没有键
print(20 in dict1)
#使用clear()方法可以清空字典
dict2 = dict1.clear()
print(dict2)
#接下来是赋值为空字典和clear()的区别
#这个是赋值为空列表
dict3 = {'id':'zhishixiang'}
dict4 = dict3
dict4 = {}
print(dict3,dict4)
#这个是clear()
dict4 = dict3
dict4.clear()
print(dict3,dict4)
#copy()指的是深拷贝
dict3 = {'id':'zhishixiang'}
dict4 = dict3.copy()
dict4.clear()
print(dict3,dict4)
#赋值的区别是和第二个值指向同一个地址，拷贝则是新建一个地址
#赋值相当于快捷方式，拷贝相当于复制粘贴
#深拷贝是赋值，浅拷贝是拷贝
dict5 = dict3
print(id(dict3))
print(id(dict4))
print(id(dict5))
#pop()指弹出键对应的值
#注意：该操作会删除原来的值
print(dict3.pop("id"))
print(dict3)
#popitem()则是弹出对应的键和值
#注意：因为字典没有顺序这一概念，所以不指定参数就会随机弹出一个键值
#setdefault()类似于get,但当不指定对应值时会自动添加none值
dict3.setdefault('qq')
print(dict3)
dict3.setdefault('location',"Guangzhou")
print(dict3)
#update()可以用于更新字典
#指的是合并字典的值
qq = {'qq':1015256551}
dict3.update(qq)
print(dict3)