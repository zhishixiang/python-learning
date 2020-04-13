#python变量分为局部变量和全局变量
#局部变量指方法内的变量，只能在方法内使用，无法在外部调用
def count(one,two):
    final_price =  one * two
    return final_price
three = float(input("请输入第一个数"))
four = float(input("请输入第二个数"))
result = count(three,four)
print(result)
#当在外部调用时就会报错
#print(final_price)
#全局变量可以被方法内访问
def print1():
    print(four)
print1()
#当在方法内新建一个与全局变量同名的变量时，该变量将会变为局部变量且不会改变全局变量
def function():
    four = 23
    print(four)
function()
print(four)