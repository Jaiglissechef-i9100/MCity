init -2 python:

    import renpy.store as store
    import renpy.exports as renpy 
    from operator import attrgetter 

    inv_page = 0 
    item = None
    nsb = None
    outfit = None
    nsb1 = None

    def item_use():
        item.use()

screen inventory_screen:
    key "hide_windows" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        unhovered Hide("display_Item_Name")
        action [SetVariable("inv_page", 0),Hide("inventory_screen"),Hide("display_Item_Name"), Hide("displayTextScreen"), Play ("sound", "sfx/zipper.mp3")]
    imagebutton:
        xalign 0.5
        yalign 0.5
        focus_mask True
        idle Transform("images/game_gui/icons/inventory.png", zoom=.7)
        hover Transform("images/game_gui/icons/inventory.png", zoom=.7)
        action Show("inventory_screen")

    modal True

    vbox xpos 1120 ypos 288 spacing 20:
        frame:
            style "frame_gui1"
            text "$"+str(inventory.money) size 30

    $ x = 700
    $ y = 294
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'))
    $ next_inv_page = inv_page + 1
    $ prev_inv_page = inv_page - 1
    if next_inv_page > int(len(inventory.items)/12):
        $ next_inv_page = 0
    if prev_inv_page < int(len(inventory.items)/12):
        $ prev_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*12 and i+1>inv_page*12:
            $ x += 137
            if i%4==0:
                $ y += 133
                $ x = 750
            $ pic = item.image

            $ pich = item.hover_i

            if item.note==True:
                imagebutton idle pic hover pich xpos x ypos y action [Hide("display_Item_Name"),  SetVariable("item", item), Show("note_view")] hovered [ Play ("sound", "sfx/click.wav"), Show("display_Item_Name", my_tt_ypos=y, my_tt_xpos=x, displayText1 = [item.name]),] unhovered [Hide("display_Item_Name")] at inv_eff
            if item.note==False:
                imagebutton idle pic hover pich xpos x ypos y action [Show("display_Item_Name", my_tt_ypos=y, my_tt_xpos=x, displayText1 = [item.name]),  SetVariable("item", item), selectItem(item)] hovered [ Play ("sound", "sfx/click.wav"), Show("display_Item_Name",  my_tt_ypos=y, my_tt_xpos=x, displayText1 = [item.name]),] unhovered [Hide("display_Item_Name")] at inv_eff
            if item.selected:
                add Transform("gui/selected.png", zoom=.7) xpos x ypos y anchor (.5,.4)
        $ i += 1
    if len(inventory.items)>12:
        imagebutton idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle.png", zoom=.7) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover.png", zoom=.7) xpos 1168 ypos 500 focus_mask True action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")]
        if inv_page >0:
            imagebutton idle Transform("images/game_gui/icons/Inventory_Arrorw_Idle1.png", zoom=.7) hover Transform("images/game_gui/icons/Inventory_Arrorw_Hover1.png", zoom=.7) xpos 545 ypos 500 focus_mask True action [SetVariable('inv_page', prev_inv_page), Show("inventory_screen")]

screen display_Item_Name:
    key "hide_windows" action NullAction()
    zorder 103
    default displayText1 = ""
    vbox:
        xpos my_tt_xpos
        ypos my_tt_ypos
        anchor (0.5,2.0)
        frame:
            style "frame_gui1"
            text displayText1

screen note_view:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 1
        ypos 1
        idle item.note_image
        hover item.note_image
        action [Hide("note_view")]

init -1:
    transform inv_eff:
        zoom 0.7 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

