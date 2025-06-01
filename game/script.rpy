# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")



#init python:

# 游戏在此开始。

label start:
    python:
        reversecard = True
        depth_show = False
        depth = 1
        The_Id = 1
        The_Ego = 1
        The_superEgo = 1
        foresee = False
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    scene bg room
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。
    show eileen happy
    # 此处显示各行对话。
    e "这是一个{a=jump:fenmu}{plain}{color=#FFFFFF}坟墓{/color}{/plain}{/a}。（试着“挖掘一下坟墓”？）"
    e "你离开了坟墓。"
    jump start1
label start1:
    e "现在不能使用反转卡。"
    $ reversecard = False
    e "现在可以了！"
    if reversecard == True:
        e "你使用了反转卡。"
    else:
        $ reversecard = True
        e "你没有使用反转卡。"
    e "是否要测试预知能力？"
    menu:
        "是":
            $ foresee = True
        "否":
            pass
    e "现在看看能不能预知！"
    menu:
        "选这个":
            e "24"
            $ The_Id += 1
        "选那个":
            e "42"
            $ The_superEgo = 1
        "查看预知结果"if foresee:
            e "选这个：本我+1"
            e "选那个：超我+1"
    return

label fenmu:
    e "你开始挖坟。"
    # 此处为游戏结尾。
    jump start1
