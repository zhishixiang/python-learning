#创建一个数组列表
number = [1,2,3,4,5]
print(number)
#创建一个字符串列表
string = ["一","二","三","四","五"]
print(string)
#创建一个混合列表
mix = [1,"gkdgkd",3.1415,[1,2,3]]
print(mix)
#向列表添加单个元素
string.append("六")
print(string)
#向列表添加多个元素
#需要以列表形式添加
string.extend(["七","八"])
print(string)
#向数组第一位插入一个数值
#python数组是从0开始算起的
string.insert(0,"零")
print(string)