#range可列出一个数字到另一个数字之间的全部数字
#0到5
range(5)
#用列表输出0到5
list(range(5))
#列出3到5
list(range(3,5))
#用for循环输出0到4
#提示：for循环输出不包含终数
for i in range(0,4):
    print(i)
#设置步进为2，打印出0到10
for i in range(0,10,2):
    print(i)
##Javascript的for循环在python中需要配合range才能实现相同的功能