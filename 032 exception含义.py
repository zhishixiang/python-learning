#exception可以让python脚本在遇到错误时可以自动处理，防止客户捣乱
file_name = input('请输入想打开的文件名')
f = open(file_name)
print('文件的内容是：')
for each_line in f:
    print(each_line)
