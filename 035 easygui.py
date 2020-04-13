#导入easygui包
import easygui
#可以用这个方法导入easygui的全部组件
from easygui import *
#msgbox可以弹出窗口
easygui.msgbox("这是一个窗口")
#全部导入后就可以不用easygui前缀
msgbox("这是第二个窗口")
#全部导入可能会导致函数命名重复，可以用这种方法来减少打字量 
import easygui as g
g.msgbox("这是第三个窗口")
#这是一个小游戏
"""
import easygui as g
import sys
while 1:
    g.msgbox("嗨,欢迎进入第一个界面小游戏^ ^")
    msg="请问你希望在鱼c工作室学习到什么知识呢?"
    title = '小游戏互动'
    choices = ["谈恋爱","编程",'00XX', "琴棋书画"]
    choice = g.choicebox(msg, title, choices)
    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    g.msgbox("你的选择是:"+ str(choice), "结果" )
    msg ="你希望重新开始小游戏吗?"
    title = "请选择"
    if g.ccbox(msg, title):
    # show a Continue/Cancel dialog
        pass # user chose Continue
    else:
        sys.exit(0)
    # user chose Cancel
"""
