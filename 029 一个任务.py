a = open("E:\\2.txt")
boy = []
girl = []
count = 1
for each_line in a:
    b = open("E:\\rec1.txt","w")
    if each_line[:6] != "======":
        #字符串分割操作
        #1是分割次数，表示分割一次
        #role是左切，each_line是右切
        (role,line_spoken) = each_line.split(":",1)
        if role == "小甲鱼":
            boy.append(line_spoken)
        if role == "小客服":
            girl.append(line_spoken)
    else:
        file_name_boy = "E:\\boy_"+str(count)+".txt"
        file_name_girl = "E:\\girl_"+str(count)+".txt"
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy_file.close()
        girl.file.close()
        count += 1
        boy = []
        girl = []
a.close()