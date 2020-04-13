#python方法执行后默认会返回none值
def Hello():
    print("Hello World!")
Hello()
temp = Hello()
print(type(temp))
#python可以返回多个值
#可以不加括号只加逗号，默认返回元组
def back():
    return[1,"hello",3.14]
print(back())