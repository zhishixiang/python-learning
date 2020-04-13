#break可以用来跳出循环，进行下一步操作
password = input("请输入密码")
while True:
    if password == "123123":
        break
    else:
        password = input("密码错误，请重新输入")
print("密码正确")
