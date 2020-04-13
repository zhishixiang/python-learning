#当字符串被切片时将会切出字符串中的字符
str1 = "192.168.15.1"
print(str1[ :5])
#更改字符串的方式和更改元组一样
str1 = str1[ :3]+"111111"+str1[3: ]
print(str1)
#capitalize 将第一个字符改为大写
str2 = "xiaoxie"
print(str2.capitalize())
#casefold 将所有字符改为小写
str3 = "DAXIE"
print(str3.casefold())
#center(width) 将字符串居中(指往字符串左右侧添加空格)
str4 = "juzhong"
print(str4.center(40))
#count(sub,[start[end]])  返回sub在字符串中出现的次数(可指定范围)
str5 = "kskskskskskskkskskskskksks"
print(str5.count("k"))
#endswitch(sub,[start[end]]) 检查字符串是否以sub结束(可指定范围)
str6 = "12121212121212121"
print(str6.endswith("1"))
#expandtabs() 将字符串中的\t转换为空格，默认参数为8
str7 = "1\t2\t3\t"
print(str7.expandtabs())
#find(sub,[start[end]]) 检测字符串中是否有sub，若没有啧返回-1，有则返回第一个sub值的位置(可指定范围)
str8 = "1234567"
print(str8.find("8"))
#index() 与find相似，但如果没找到值会返回一个异常值
#懒得写了，自己去论坛看