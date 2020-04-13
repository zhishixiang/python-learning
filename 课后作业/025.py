dict1 = {}
dict1.fromkeys((1,2,3),('one','two','three'))
dict1.fromkeys((1,3),('数字'))
print(dict1)
def login():
    print("|---新建用户:N/n---|")
    print("|---登录账号:E/e---|")
    print("|---退出登录:Q/q---|")
    operate = input("请输入指令代码")
    print(operate)
    if operate == "N" or operate == "n":
        global regpasswd
        newuser = input("请输入新用户名")
        newpasswd = input("请输入新密码")
        correctpasswd = input("请再次确认密码")
        if newpasswd != correctpasswd:
            print("密码不一致，请重试")
            login()
        print("注册成功，请登录")
        regpasswd = {newuser:newpasswd}
        login()
    elif operate == "E" or operate == "e":
        user = input("请输入账号")
        passwd = input("请输入密码")
        auth = regpasswd.get(user)
        if passwd != auth:
            print("密码错误，请重试")
            login()
        elif passwd == auth:
            print("登录成功！")
    elif operate == "Q" or operate == "q":
        print("感谢使用")
        assert True
    else:
        print("你输入了一个错误的值，请重试!")
        login()
login()