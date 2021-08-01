screen kitchen_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door1_morning_idle.png"
        hover "images/home/kitchen/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Living Room"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door2_morning_idle.png"
        hover "images/home/kitchen/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Entrance"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("entrance2_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/morning/door3_morning_idle.png"
        hover "images/home/kitchen/morning/door3_morning_hover.png"
        hovered Show("displayTextScreen", displayText = __("Bathroom"))
        action [Play ("sound", "sfx/door_open.mp3"),Jump("bathroom_day1")]
        unhovered Hide("displayTextScreen")

