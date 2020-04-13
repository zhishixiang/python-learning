def digui(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("输入有⑤，请重新输入!")
    while(n - 2):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3
print(digui(32))
#下面的是递归解法
def fab(n):
    if n < 1:
        print("输入有误，请重新输入!")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
print(fab(40))
#全程一脸懵逼