#比较单个列表
list1 = [123]
list2 = [234]
print(list1 < list2)
#当多个列表比较时只会比较第一个数
list1 = [123,999]
list2 = [456,111]
print(list1 < list2)
#数组相加时会自动合并
print(list1+list2)
#不知道怎么说了，自己体会
print(list1 * 3)
list1 *= 3
print(list1)
#判断数组内是否有某值
players = ["mc_niconi","zhishixiang","class_666","Qimu","tyzhsh"]
print("zhishixiang" in players)
print("gao_cai_sheng" in players)
print("ijjzlxjcpasijd" not in players)
#套娃
numbers = [1,2,[3,4],5]
print(numbers[2][0])
