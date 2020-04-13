#python中的format指的是翻译
#format的几种用法
#在字符串中指定位置并使用format添加字符(位置也是从零开始算起)
print("{0} love {1}.{2}".format("I","FichC","com"))
#位置可以任意指定一个值来替代数字
print("{a} love {b}.{c}".format(a="I",b="FichC",c="com"))
#位置可以混合使用数字或者指定值，但当第一个位置是指定值时后面的位置就不能使用数字
#print("{a} love {b}.{0}".format(a="I",b="FichC","com"))
#转义字符 当一个位置参数被花括号括起来时将会输出为字符串
print("{{0}}".format("不打印"))
#%c 转换ASCII码
print("%c"% 97)
print("%c %c %c"%(97,98,99))
#%s 格式化字符串(相当于占位符)
print("I love %s"%"FishC.com")
#%o 格式化八进制
#%x 格式化十六进制
#%X 格式化大写十六进制
#懒得写了，还是去看论坛吧