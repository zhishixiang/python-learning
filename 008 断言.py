#当条件不成立时，执行自爆
#assert 4 < 3
#当条件成立时，自动跳过
#assert 3 < 4
account = int(input("请输入账号"))
password = int(input("请输入密码"))
#assert account == 123123
#assert password == 789789
if account == 123123 and password == 789789:
    print("登录成功")
else:
    print("操你妈费物东西又来盗你爹的号")
