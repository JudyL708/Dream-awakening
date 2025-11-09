################################################################################
## 初始化
################################################################################

init offset = -1
#TEST


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## 对话屏幕 ########################################################################
##
## 对话屏幕用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此屏幕必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    if depth > 0 and intro1 == True:
        use reversecardscreen
    if depth > 0 and intro2 == True:
        use depthscreen

screen reversecardscreen():
    zorder 50
    modal True
    if reversecard == False and depth > 0 and intro1 == True:    
        imagebutton:
            xalign 0.99
            yalign 0.5
            idle "images/normal1.jpg"
            hover "images/normal1.jpg"
            action SetVariable("reversecard",True)
    elif reversecard == True and depth > 0 and intro1 == True:
        imagebutton:
            xalign 0.99
            yalign 0.5
            idle "images/normal.jpg"
            hover "images/normal.jpg"
            action NullAction()
    else:
        pass

screen depthscreen():
    zorder 50
    modal True
    if depth_show == False and depth > 0 and intro2 == True:    
        imagebutton:
            xalign 0.99
            yalign 0.8
            idle "images/normal1.jpg"
            hover "images/normal1.jpg"
            action [SetVariable("depth_show",True),Show("depthcheck")]
    elif depth_show == True and depth > 0 and intro2 == True:
        imagebutton:
            xalign 0.99
            yalign 0.8
            idle "images/normal.jpg"
            hover "images/normal.jpg"
            action [SetVariable("depth_show",False),Hide("depthcheck")]
    else:
        pass

screen depthcheck():
    zorder 75
    modal True
    add "white"
    text _("当前深度值："+str(depth)) xalign 0.5 yalign 0.5 size 60
    use depthscreen

## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

    use reversecardscreen
    use depthscreen

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action
    use reversecardscreen
    use depthscreen


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。
screen quick_menu1():
    zorder 100

    text ("设置"):
        yalign 0.9
        xalign 0.9

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 50

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            textbutton _("回滚") action Rollback()
            textbutton _("历史对话") action ShowMenu('history')
            textbutton _("快进") action Skip()
            textbutton _("保存") action ShowMenu('save')
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("角色信息") action ShowMenu("charactersetting")
            textbutton _("设置") action ShowMenu('preferences')
            textbutton _("静音") action Preference("all mute", "toggle")

screen darkness():#用于转场间的界面，因为Renpy自身支持的屏幕间转场数量实在过于有限！默认转场效果必须为None，不然二者会依次执行！因此这个界面在游戏里用不到！
    add "darkness.png"
    timer 1 action [Hide("darkness"), Return(), With(dissolve)]
screen beforesave():
    add "darkness.png"
    timer 1 action [Hide("darkness"), ShowMenu("save")]
screen beforeload():
    add "darkness.png"
    timer 1 action [Hide("darkness"), ShowMenu("load")]
## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    #vbox:
        #style_prefix "navigation"

        #xpos gui.navigation_xpos
        #yalign 0.5

        #spacing gui.navigation_spacing

    if main_menu:

        imagebutton:
            action Start()
            #activate_sound "audio/sound_start.mp3"
            xalign 0.5375
            yalign 0.734
            idle "gui/main_start.png"
            hover "gui/main_start_2.png"
        imagebutton:
            action ShowMenu("load")
            #activate_sound "audio/sound_start.mp3"
            xalign 0.85
            yalign 0.734
            idle "gui/main_load.png"
            hover "gui/main_load_2.png"
        imagebutton:
            action ShowMenu("preferences")
            #activate_sound "audio/sound_start.mp3"
            xalign 0.5375
            yalign 0.867
            idle "gui/main_options.png"
            hover "gui/main_options_2.png"
        imagebutton:
            action ShowMenu("about")
            #activate_sound "audio/sound_start.mp3"
            xalign 0.85
            yalign 0.867
            idle "gui/main_about.png"
            hover "gui/main_about_2.png"

    else:

        textbutton _("历史") action ShowMenu("history")

        textbutton _("保存") action ShowMenu("save")

        textbutton _("读取游戏") action [ShowMenu("load"),With(fade)]

        textbutton _("设置") action ShowMenu("preferences")

        textbutton _("关于") action ShowMenu("about")

    if _in_replay:

        textbutton _("结束回放") action EndReplay(confirm=True)

    elif not main_menu:

        textbutton _("标题菜单") action MainMenu()


        #if renpy.variant("pc"):

            ## 退出按钮在 iOS 上是被禁止使用的，在安卓和网页上也不是必要的。
            #textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#main-menu

screen main_menu():

    ## 此语句可确保替换掉任何其他菜单屏幕。
    tag menu

    add gui.main_menu_background

    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"

    ## use 语句将其他的屏幕包含进此屏幕。标题屏幕的实际内容在导航屏幕中。
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 0
    yfill False

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。可使用屏幕标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。此屏幕旨在与一个或多个子
## 屏幕同时使用，这些子屏幕将被嵌入（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    label title


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

screen game_menu1(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        vscrollbar_xpos -300
                        vscrollbar_ypos -30

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此屏幕没有什么特别之处，因此它也可以作为一个例子来说明如何制作一个自定义屏
## 幕。

screen about():

    tag menu

    add "images/darkness.png"

    ## 此 use 语句将 game_menu 屏幕包含到了这个屏幕内。子级 vbox 将包含在
    ## game_menu 屏幕的 viewport 内。

    textbutton _("返回"):

        xalign 0.98 yalign 0.96
        style "return_button"

        action Return()

    style_prefix "about"

    vbox:
        xmaximum 1200
        xalign 0.5
        yalign 0.2

        label "[config.name!t]"
        text _("版本 [config.version!t]\n")

            ## gui.about 通常在 options.rpy 中设置。
        if gui.about:
            text "[gui.about!t]\n"

        text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个屏
## 幕都是以第三个屏幕 file_slots 来实现的。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#save https://doc.renpy.cn/zh-
## CN/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))

    textbutton _("返回"):

        xalign 0.98 yalign 0.96
        style "return_button"

        action Return()

screen aftersave():
    add "darkness.png"
    timer 0.5 action [Hide("darkness"), Return()]

screen load():

    tag menu

    use file_slots(_("读取游戏"))

    textbutton _("返回"):

        xalign 0.98 yalign 0.96
        style "return_button"

        action Return()

screen afterload():
    add "darkness.png"
    timer 0.5 action [Hide("afterload"), Return()]
screen goback():
    add "darkness.png"
    timer 0.5 action [Hide("goback"), MainMenu(confirm=False)]
screen file_slots(title):

    textbutton _("返回主菜单"):
        xalign 0.01 yalign 0.04
        action Show("goback")

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    if True == True:

        fixed:

            ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) 给出 1 到 9 之间的数字。
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("上传同步"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("下载同步"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## 设置屏幕 ########################################################################
##
## 设置屏幕允许用户配置游戏，使其更适合自己。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#preferences

screen preferences():
    modal True

    add "white.png"

    textbutton _("返回"):

        xalign 0.98 yalign 0.96
        if main_menu:
            action Return()
        else:
            action Return()
    tag menu

    use game_menu1(_("")):
        if renpy.variant("pc"):
            vbox:
                xpos 0
                ypos 0
                style_prefix "radio"
                label _("{size=+10}{color=#090909}屏幕大小{/color}")
                textbutton _("{size=+10}窗口{/size}") action Preference("display", "window")
                textbutton _("{size=+10}全屏{/size}") action Preference("display", "fullscreen")
        elif renpy.variant("web"):
            add "images/testlogo1.png":
                xpos 0
                ypos -100
                zoom 0.5
        vbox:
            if renpy.variant("small"):
                xpos -200
                ypos 450
            else:
                xpos 550
                ypos 0
            style_prefix "slider"
            label _("{color=#090909}{size=+10}时间的流速{/size}{/color}")
            bar value Preference("text speed")
            label _("{color=#090909}{size=+10}自动前进时时间的流速{/size}{/color}")
            bar value Preference("auto-forward time")
        if renpy.variant("small"):
            add "images/testlogo1.png":
                xpos 750
                ypos 50
                zoom 0.5
        vbox:
            if renpy.variant("small"):
                xpos -200
                ypos 50
            else:
                xpos 550
                ypos 500
            style_prefix "slider"
            if config.has_music:
                label _("{color=#090909}{size=+10}乐声的音量{/size}{/color}")
                hbox:
                    bar: 
                        value Preference("music volume")
            if config.has_sound:
                label _("{color=#090909}{size=+10}器声的音量{/size}{/color}")
                hbox:
                    bar: 
                        value Preference("sound volume")
            if config.has_voice:
                label _("{color=#090909}{size=+10}人声的音量（暂未实装）{/size}{/color}")
                hbox:
                    bar: 
                        value Preference("voice volume")

        vbox:
            if renpy.variant("small"):
                xpos 750
                ypos 350
            else:
                xpos 0
                ypos 500
            style_prefix "check"
            label _("{color=#090909}{size=+10}快进{/size}{/color}")
            textbutton _("{color=#090909}{size=+10}未读文本{/size}{/color}") action Preference("skip", "toggle")
            textbutton _("{color=#090909}{size=+10}选项后继续{/size}{/color}") action Preference("after choices", "toggle")
            textbutton _("{color=#090909}{size=+10}忽略转场{/size}{/color}") action InvertSelected(Preference("transitions", "toggle"))


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## 历史屏幕 ########################################################################
##
## 这是一个向用户显示对话历史的屏幕。虽然此屏幕没有什么特别之处，但它必须访问储
## 存在 _history_list 中的对话历史记录。
##
## https://doc.renpy.cn/zh-CN/history.html

screen history():

    add "images/white.png"

    tag menu

    textbutton _("返回"):

        xalign 0.98 yalign 0.96
        if main_menu:
            action Return()
        else:
            action Return()

    ## 避免预缓存此界面，因为它可能非常大。
    predict False

    use game_menu1(_(""), scroll=("viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此代码可确保如果 history_height 为 None 时仍可正常显示条目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 从 Character 对象中获取叙述角色的文字颜色，如果设置了
                        ## 的话。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            textbutton _("[historymystery]") action SetVariable("histerymistery","{color=#990000}{b}你别无选择。{/b}{/color}")


## 此代码决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xmaximum 800
    ysize gui.history_height
    xpos 100

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕（keyboard_help、mouse_help
## 和 gamepad_help）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("在没有选择的情况下推进对话。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("键盘")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("上一页")
        text _("回退至先前的对话。")

    hbox:
        label _("下一页")
        text _("向前至后来的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://doc.renpy.cn/zh-CN/self_voicing.html}机器朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至后来的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至后来的对话。")

    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导，B/右键")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认屏幕。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## skip_indicator 屏幕用于指示快进正在进行中。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://doc.renpy.cn/zh-CN/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在 vpgrid 或 vbox 中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 显示菜单，如果给定的话。如果 config.narrator_menu 设置为 True，则菜单
        ## 可能显示不正确。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## 对话气泡屏幕 ######################################################################
##
## 对话气泡屏幕用于以对话气泡的形式向玩家显示对话。对话气泡屏幕的参数与 say 屏幕
## 相同，必须创建一个 id 为 what 的可视控件，并且可以创建 id 为 namebox、who 和
## window 的可视控件。
##
## https://doc.renpy.cn/zh-CN/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 由于可能没有鼠标，我们将快捷菜单替换为一个使用更少、更大按钮的版本，这样更容
## 易触摸。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

screen charactersetting():
    add "darkness.png"
    if meetpl1:
        text ([plname]):
            xalign 0.2
            yalign 0.2
    else:
        text ("？？？"):
            xalign 0.2
            yalign 0.2
    viewport:
        xmaximum 380
        ymaximum 200
        mousewheel False
        draggable False
        pagekeys True
        side_yfill True
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        child_size (400,200)
        xpos 1400
        ypos 200
        scrollbars None
        vbox:
            if firsttest:
                text ("当前本我值："+str(The_Id))
                text ("当前自我值："+str(The_Ego))
                text ("当前超我值："+str(The_superEgo))
            else:
                text ("当前本我值：？？？")
                text ("当前自我值：？？？")
                text ("当前超我值：？？？")

    viewport:
        xmaximum 380
        ymaximum 200
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        child_size (400,200)
        xpos 1400
        ypos 500
        scrollbars None
        vbox:       
            if firsttest:
                if The_Id and The_Ego and The_Id >= 10:
                    if The_Id >= The_Ego and The_Id >= The_superEgo:
                        text ("梦境赋予了你强健的体魄")
                    elif The_Ego >= The_Id and The_Ego >= The_superEgo:
                        text ("梦境赋予了你清醒的头脑")
                    elif The_superEgo >= The_Id and The_superEgo >= The_Ego:
                        text ("梦境赋予了你敏锐的直觉")
                else:
                    if The_Id >= The_Ego and The_Id >= The_superEgo:
                        text ("你服从于欲望")
                    elif The_Ego >= The_Id and The_Ego >= The_superEgo:
                        text ("你听从于思考")
                    elif The_superEgo >= The_Id and The_superEgo >= The_Ego:
                        text ("你倾向于奉献")
            else:
                text ("……")

    viewport:
        xmaximum 380
        ymaximum 200
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        child_size (400,200)
        xpos 1400
        ypos 800
        scrollbars None
        vbox:       
            if chapter == 1:    
                text ("当前章节：第一章")
            
    textbutton("下一页"):
        xalign 1.0
        yalign 0.5
        action [Hide("charactersetting"), ShowMenu("charactersetting0")]
    textbutton("返回"):
        xalign 0.5
        yalign 0.5
        action Return()

screen charactersetting0():
    add "darkness.png"
    if meetydz1:
        text ("引导者"): 
            xalign 0.2
            yalign 0.2
    else:
        text ("该人物暂未解锁"):
            xalign 0.2
            yalign 0.2
    viewport:
        xmaximum 380
        ymaximum 200
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        child_size (400,200)
        xpos 1400
        ypos 200
        scrollbars "vertical" 
        vbox:       
            if meetydz1:    
                text ("角色简介：突兀出现的白发少年\n指引你拯救梦境主人的向导\n是个理性的人，但似乎隐藏着很深的秘密，让你无法完全相信\n")
            else:
                text ("角色简介：？？？")
            if meetydz2:    
                text ("？？？")
            else:
                pass
    viewport:
        xmaximum 380
        ymaximum 200
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        child_size (400,200)
        xpos 1400
        ypos 800
        vbox:
            if meetydz1:    
                text ("角色功能：\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
            else:
                text ("角色功能：？？？")
    viewport:
        xmaximum 380
        ymaximum 200
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        child_size (400,200)
        xpos 1400
        ypos 500
        scrollbars "vertical" 
        vbox:       
            if meetydz1:    
                text ("角色剧情：\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
            else:
                text ("角色剧情：？？？")

    textbutton("上一页"):
        xalign 0
        yalign 0.5
        action [Hide("charactersetting0"), ShowMenu("charactersetting")]
    textbutton("下一页"):
        xalign 1.0
        yalign 0.5
        action [Hide("charactersetting0"), ShowMenu("charactersetting1")]
    textbutton("返回"):
        xalign 0.5
        yalign 0.5
        action Return()

screen charactersetting1():
    add "darkness.png"
    if meethtfy1:
        text ("黑土飞鹰"): 
            xalign 0.2
            yalign 0.2
    else:
        text ("该人物暂未解锁"):
            xalign 0.2
            yalign 0.2
    viewport:
        xmaximum 380
        ymaximum 200
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        child_size (400,200)
        xpos 1400
        ypos 200
        vbox:
            if meethtfy1:    
                text ("角色简介：\n来自某个村庄，十三四岁，自称是“伟大航海家”的少女\n总是想当英雄\n顽皮跳脱，生命力旺盛\n")
            else:
                text ("角色简介：？？？")
            if meethtfy2:    
                text ("？？？")
            else:
                pass
    viewport:
        xmaximum 380
        ymaximum 200
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        child_size (400,200)
        xpos 1400
        ypos 500
        scrollbars "vertical" 
        vbox:       
            if meethtfy1:    
                text ("角色剧情：\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
            else:
                text ("角色剧情：？？？")
    viewport:
        xmaximum 380
        ymaximum 200
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        child_size (400,200)
        xpos 1400
        ypos 800
        vbox:
            if meethtfy1:    
                text ("角色功能：\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
            else:
                text ("角色功能：？？？")

    textbutton("上一页"):
        xalign 0
        yalign 0.5
        action [Hide("charactersetting1"), ShowMenu("charactersetting0")]
    textbutton("下一页"):
        xalign 1.0
        yalign 0.5
        action [Hide("charactersetting1"), ShowMenu("charactersetting2")]
    textbutton("返回"):
        xalign 0.5
        yalign 0.5
        action Return()

screen charactersetting2():
    add "darkness.png"
    if meetldx1:
        text ("露蒂莘"): 
            xalign 0.2
            yalign 0.2
    else:
        text ("该人物暂未解锁"):
            xalign 0.2
            yalign 0.2
    viewport:
        xmaximum 380
        ymaximum 200
        vscrollbar_xpos 0
        vscrollbar_ypos 0 
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        child_size (400,200)
        xpos 1400
        ypos 200
        vbox:        
            if meetldx1:    
                text ("角色简介：\n神庙中端庄的少女，拥有预知能力\n有强烈道德感，却不会干涉你的选择\n宿命论的信仰者（但你的到来或许会带来动摇）\n")
            else:
                text ("角色简介：？？？")
            if meetldx2:    
                text ("？？？")
            else:
                pass
    viewport:
        xmaximum 380
        ymaximum 200
        vscrollbar_xpos 0
        vscrollbar_ypos 0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        child_size (400,200)
        xpos 1400
        ypos 500
        vbox:        
            if meetldx1:    
                text ("角色剧情：\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
            else:
                text ("角色剧情：？？？")
    viewport:
        xmaximum 380
        ymaximum 200
        vscrollbar_xpos 0
        vscrollbar_ypos 0 
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        child_size (400,200)
        xpos 1400
        ypos 800
        vbox:        
            if meetldx1:    
                text ("角色功能：\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
            else:
                text ("角色功能：？？？")
    textbutton("上一页"):
        xalign 0
        yalign 0.5
        action [Hide("charactersetting2"), ShowMenu("charactersetting1")]
    textbutton("返回"):
        xalign 0.5
        yalign 0.5
        action Return()
