#模块是一个包含所有你定义的函数和变量的文件，其后缀名是.Py。模块可以被别的程序引入，以使用该模块中的函数等功能。
import random
secret = random.randint(1,10)
print(secret)
#os模块可以帮助python适配多个系统以便达到跨平台的操作
#os.getcwd可以返回当前的工作目录
import os
print(os.getcwd())
#os.chdir()可以改变工作目录
os.chdir("E:\\")
print(os.getcwd())
#os.listdir()可以列举出目录中的所有文件和文件夹
print(os.listdir("E:\\"))
#os.mkdir可以创建新的目录
#必须要在有前置目录时才能创建子目录
os.mkdir('E:\\有内鬼停止交易')
#可以使用os.makedirs()无中生有出前置目录(递归创建多层目录)
os.makedirs('E:\\有内鬼\\停止交易')
#os.rmdir()可以删除目录,删除非空目录时弹出异常
#os.rmdir("E:\\有内鬼")
os.rmdir("E:\\有内鬼停止交易")
#os.remove()可以删除文件
#os.removedirs()可以递归删除文件，遇到非空目录时也会异常
os.removedirs("E:\\有内鬼\\停止交易")
#os.system()可以传入系统控制台命令
os.system('echo hello world')