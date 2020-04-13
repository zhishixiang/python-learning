#else表示当if语句中所有条件都不满足时执行的语句
#else还可以表示当try中没有异常时继续执行的语句
try:
    int("123")
except ValueError:
    print("出现错误！")
else:
    print("没有出错！")