screen secret_gallery:
    key "hide_windows" action NullAction()
    modal True
    zorder 106
    add "images/secret_gallery/Bonus/Black.jpg"

    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)

    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_items[i].thumb hover gallery_items[i].thumb_hover:
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxperpage):
            null

    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumbx - 70
                xalign 0.5
                yalign 0.9
                $ total = gallery_items[i].num_images()
                $ partial = gallery_items[i].num_unlocked

        for i in range(end - start + 1, maxperpage):
            null

    if gallery_page > 0:
        textbutton "Previous":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.99999
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "Next":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.99999

    textbutton "Return":
        action [Hide("secret_gallery")]
        xalign 0.5
        yalign 0.99999
    text __("{size=+6}Secret Gallery{/size}"):
        xalign 0.5
        yalign 0.0

screen gallery_closeup(images):
    key "hide_windows" action NullAction()
    zorder 106
    add images[closeup_page] at truecenter

    imagebutton idle images[closeup_page]:
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]

    if closeup_page > 0:
        textbutton "Previous":
            action SetVariable("closeup_page", closeup_page - 1)
            xalign 0.1
            yalign 0.99999

    if closeup_page < len(images) - 1:
        textbutton "Next":
            action SetVariable("closeup_page", closeup_page + 1)
            xalign 0.9
            yalign 0.99999
