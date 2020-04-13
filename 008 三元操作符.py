#复杂
small = 0
x , y = 4 , 5
if x < y:
    small = x
if y < x:
    small = y
#简化
small = x if x < y else y