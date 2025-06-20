﻿# 游戏的脚本可置于此文件中。

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

#【剧情1】【节点1】
    menu:
        "是":
            jump functions
        "否":
            pass
        "是否测试特殊功能？"
    "早上六点的地铁站人挤人。"
    "售货员""你叫【玩家名字】，对吧？"
    "售货员查过了你的身份证，将票递给你。"
    "今天又是平凡的一天，你挤进地铁，前往【玩家设定上的日常生活】。"
    "坐进咖啡厅，你点了一杯咖啡。窗外铁灰色的天空让等咖啡制作的时间更加无聊，为了打发时间，你开始看路上的车流，试图辨认每一辆车的款式。"
    "就在你昏昏欲睡的时候，一阵刺耳的声音让我瞬间清醒，那声音像是钥匙插进锁孔和玻璃瓶破碎的声音，极其尖锐直穿耳膜。"
    "你下意识转头去看，不知怎么的，整个咖啡厅突然被分成了两半。"
    "靠内的一侧却变成了古希腊风格的神庙。神庙一侧立着一个巨大的男人塑像，那人身穿袍子端正地坐在高台的王座上，手里把玩着一道闪电。"
    "另一侧，有一根圆形的立柱，头发松松挽起的女神靠在柱子上。"
    "疑惑之际，男女神的脸上各出现了一道裂痕！"
    "神庙开始扩散。未及反应，白色的砖石就扩散到了我脚下，瞬间，神庙的支柱开始崩解，两座神像裂成了无数碎块。而裂了一半的立柱则轰然倾斜，靠到了咖啡店原有的梁柱上，形成了一个三角结构。奇怪的是，咖啡店里的人们面色如常，移动不懂，完全没有意识到危险的降临。"
    menu:
        "你连忙跑向了打开的咖啡店门":
            jump id1
        "你立刻躲到了三角结构中":
            jump ego1
        "你赶紧去帮助咖啡馆里的人和店员。":
            jump superego1
#三个选择
label id1:
    "你连忙跑到了外面，摇摇欲坠的建筑如影随形，你拼命向前跑着，身后的一切都被正在倒塌的神庙吞噬。"
    "你脚下的地面突然开裂，你来不及躲避，掉入裂缝。"
label ego1:
    "神庙忽然不再开裂了，你连忙乘机跑出了咖啡店。"
    "然而刚一出门，背后立刻传来剧烈的声响。"
label superego1:
    "然而他们都不动弹。你焦急不已，没看到自己头顶上的天花板也已经开裂，大小石块纷纷砸下来。你感觉头顶被人敲了一记，眼前一黑，失去了知觉。"
return#加一个return（返回主界面）以防止可能地出错，我加了一个额外的选项让玩家选择是否开始测试功能
label functions:
    while True:
        $ yourname = renpy.input(_("你的名字是什么？"))
        $ yourname = yourname.strip()
        if yourname != "":
            menu:
                "是":
                    jump start1
                "否":
                    pass
                "你的名字是[yourname]，不错吧？"
        else:
            "不要这么害羞嘛……"
label start1:
    e "这是一个{a=jump:fenmu}{plain}{color=#FFFFFF}坟墓{/color}{/plain}{/a}。（试着“挖掘一下坟墓”？）"
    e "你离开了坟墓。"
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
