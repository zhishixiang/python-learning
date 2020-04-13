#打开一个不存在的文件时会出现FileNotFound的异常
#f = open("我是一个文件.txt")
#print(f.read())
#f.close()
#使用try语句时可以检测抛出的异常
try:
    f = open("这是个不存在的文件.txt")
    print(f.read)
    sum = 1 + '1'
    f.close()
#使用except可以决定当某个异常出现时执行什么指令
#except还可以添加一个变量存放错误原因
#变量需要使用str()方法转换为字符
except OSError as error:
    print("出现错误!\n错误的原因是"+str(error))
#except可以检测多个错误
#只有第一个出现的语句会触发except
except TypeError:
    print("不合法的运算!请重试！")
#当出现的错误不在下方的except时将会抛出异常并终止运行
#只使用except不指定类型时出现任何异常都会触发except
#不推荐上面的做法
#except可以添加多个参数表示捕获多个错误
except(OSError,TypeError):
    print("程序出现错误!")
#在上面的例子中，由于sum = 1 + '1'在f.close之上，因此当检测到错误时f.close就不会执行，文件就无法保存。
#finally可以指定当检测到错误时仍然要执行的指令
"""
finally:
    f.close()
    """
#raise可以手动引发异常，后面还可以指定一个参数表示异常的名字
#可以指定错误的具体
raise FileNotFoundError('找不到文件 "你妈" ，可能是 你妈 不存在')
