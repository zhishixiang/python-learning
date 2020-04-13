#pickle模块可以将对象转换为二进制并保存和读取
import pickle
#新建一个列表
my_list = [123,3.14,"繁星若尘",["套娃"]]
#将列表新建为二进制
pickle_file = open('my_list.pkl','wb')
#将my_list倒进二进制文件
pickle.dump(my_list,pickle_file)
#保存并关闭文件
pickle_file.close()
#此时可以在工作目录中找到保存好的pkl文件
#重新打开文件
pickle_file = open('my_list.pkl','rb')
#使用pickle.load方法打开pkl文件
my_list2 = pickle.load(pickle_file)
print(my_list2)