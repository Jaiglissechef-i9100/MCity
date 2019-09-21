image splash1 = "images/splashscreen/splash1.jpg"
image splash2 = "images/splashscreen/splash2.jpg"
image splash3 = "images/splashscreen/splash3.jpg"

label splashscreen:
    scene black
    $ renpy.pause(1, hard = True)

    show splash1 with dissolve
    $ renpy.pause(2, hard = True)
    hide splash1 with dissolve

    show splash2 with dissolve
    $ renpy.pause(2, hard = True)
    hide splash2 with dissolve

    show splash3 with dissolve
    $ renpy.pause(2, hard = True)
    hide splash3 with dissolve

    return