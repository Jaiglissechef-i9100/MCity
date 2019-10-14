screen scenes_gallery:
    key "hide_windows" action NullAction()
    modal True
    zorder 106
    add "images/secret_gallery/Bonus/Black.jpg"

    $ start2 = gallery_page2 * maxperpage2
    $ end2 = min(start2 + maxperpage2 - 1, len(scenes_gallery_items) - 1)

    grid maxnumx2 maxnumy2:
        xfill True
        yfill True

        for i in range(start2, end2 + 1):
            $ scenes_gallery_items[i].refresh_lock2()
            if scenes_gallery_items[i].is_locked2:
                add scenes_gallery_items[i].locked2:
                    xalign 0.5
                    yalign 0.5

            else:
                $ scenes_repeat = scenes_gallery_items[i].name
                imagebutton idle scenes_gallery_items[i].thumb hover scenes_gallery_items[i].thumb_hover:
                    action [Jump(scenes_repeat)]
                    xalign 0.5
                    yalign 0.5

        for i in range(end2 - start2 + 1, maxperpage2):
            null

    grid maxnumx2 maxnumy2:
        xfill True
        yfill True

        for i in range(start2, end2 + 1):
            hbox:
                spacing maxthumbx2 - 70
                xalign 0.5
                yalign 0.9
                $ total2 = scenes_gallery_items[i].num_images2()
                $ partial2 = scenes_gallery_items[i].num_unlocked2

        for i in range(end2 - start2 + 1, maxperpage2):
            null

    if gallery_page2 > 0:
        textbutton "Previous":
            action SetVariable("gallery_page2", gallery_page2 - 1)
            xalign 0.1
            yalign 0.99999
    if (gallery_page2 + 1) * maxperpage2 < len(scenes_gallery_items):
        textbutton "Next":
            action SetVariable("gallery_page2", gallery_page2 + 1)
            xalign 0.9
            yalign 0.99999

    textbutton "Return":
        action [Hide("scenes_gallery"), Jump("pc_icon_label")]
        xalign 0.5
        yalign 0.99999
    text "{size=+6}Scenes Gallery{/size}":
        xalign 0.5
        yalign 0.0
