screen kitchen_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/night/door1_night_idle.png"
        hover "images/home/kitchen/night/door1_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Living Room")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/night/door2_night_idle.png"
        hover "images/home/kitchen/night/door2_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Entrance")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("entrance2_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/night/door3_night_idle.png"
        hover "images/home/kitchen/night/door3_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Bathroom")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("bathroom_night1")]
        unhovered Hide("displayTextScreen")