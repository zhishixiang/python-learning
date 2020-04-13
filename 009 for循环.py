#有点难理解for循环，回来再写行注释
#for循环的真正用法是遍历列表的每个值并赋值到另一个变量中
#下面的例句中，for第一次运行会遍历一次favourite，然后赋值第一个值给i
#之后再执行一次代码块，执行完毕后会赋值下一个值给i，然后再执行一次代码块
#当所有值遍历完毕后将跳出循环
favourite = "starrymc"
for i in favourite:
    print(i,end=" ")
member = ["你妈死了","小费物","操你妈","你吗被我纱了"]
for each in member:
    print(each,len(each))