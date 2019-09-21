init python:

    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight
        
        if xscale > yscale:
            maxscale = xscale
        else:
            maxscale = yscale
        
        return im.FactorScale(img, maxscale, maxscale)

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight
        
        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale
        
        return im.FactorScale(img, minscale, minscale)

    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0

    class GalleryItem:
        def __init__(self, name, images, thumb, thumb_hover, locked="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.thumb_hover = thumb_hover
            self.locked = locked
            self.refresh_lock()
        
        def num_images(self):
            return len(self.images)
        
        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not img in gallery_photos.storage:
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme

    class Gallery_photos(store.object):
        def __init__(self,):
            self.storage = []
        
        def add1(self, img): 
            self.storage.append(img)

    class addgimage(Action):
        
        def __init__(self, img):
            self.img = img
        
        def __call__(self):
            gallery_photos.storage.append(self.img)
            renpy.restart_interaction()

    gallery_photos = Gallery_photos()
    gallery_items = []
    gallery_items.append(GalleryItem("1", ["img1_garage_card"], "thumb1_garage_card","thumb1_hover_garage_card" ))
    gallery_items.append(GalleryItem("2", ["img2_garage_entrance_card"], "thumb2_garage_entrance_card", "thumb2_hover_garage_entrance_card"))
    gallery_items.append(GalleryItem("3", ["img3_home_entrance_card"], "thumb3_home_entrance_card", "thumb3_hover_home_entrance_card"))
    gallery_items.append(GalleryItem("4", ["img4_mc_room_card",], "thumb4_mc_room_card", "thumb4_hover_mc_room_card" ))
    gallery_items.append(GalleryItem("5", ["img5_sex_shop_card"], "thumb5_sex_shop_card", "thumb5_hover_sex_shop_card" ))
    gallery_items.append(GalleryItem("6", ["img6_exit_school_corridor_card"], "thumb6_exit_school_corridor_card", "thumb6_hover_exit_school_corridor_card" ))
    gallery_items.append(GalleryItem("7", ["img7_school_corridor1_card"], "thumb7_school_corridor1_card", "thumb7_hover_school_corridor1_card" ))
    gallery_items.append(GalleryItem("8", ["img8_mc_classroom_card"], "thumb8_mc_classroom_card", "thumb8_hover_mc_classroom_card" ))
    gallery_items.append(GalleryItem("9", ["img9_school_corrior2_card"], "thumb9_school_corrior2_card", "thumb9_hover_school_corrior2_card" ))
    gallery_items.append(GalleryItem("10", ["img10_mom_office_card"], "thumb10_mom_office_card", "thumb10_hover_mom_office_card" ))
    gallery_items.append(GalleryItem("11", ["img11_mom_office_card2"], "thumb11_mom_office_card2", "thumb11_hover_mom_office_card2" ))

    gallery_items.append(GalleryItem("12", ["img12_sec_card"], "thumb12_sec_card", "thumb12_hover_sec_card" ))
    gallery_items.append(GalleryItem("13", ["img13_sec_card"], "thumb13_sec_card", "thumb13_hover_sec_card" ))
    gallery_items.append(GalleryItem("14", ["img14_sec_card"], "thumb14_sec_card", "thumb14_hover_sec_card" ))
    gallery_items.append(GalleryItem("15", ["img15_sec_card"], "thumb15_sec_card", "thumb15_hover_sec_card" ))
    gallery_items.append(GalleryItem("16", ["img16_sec_card"], "thumb16_sec_card", "thumb16_hover_sec_card" ))
    gallery_items.append(GalleryItem("17", ["img17_sec_card"], "thumb17_sec_card", "thumb17_hover_sec_card" ))
    gallery_items.append(GalleryItem("18", ["img18_sec_card"], "thumb18_sec_card", "thumb18_hover_sec_card" ))
    gallery_items.append(GalleryItem("19", ["img19_sec_card"], "thumb19_sec_card", "thumb19_hover_sec_card" ))
    gallery_items.append(GalleryItem("20", ["img20_sec_card"], "thumb20_sec_card", "thumb20_hover_sec_card" ))
    gallery_items.append(GalleryItem("21", ["img21_sec_card"], "thumb21_sec_card", "thumb21_hover_sec_card" ))
    gallery_items.append(GalleryItem("22", ["img22_sec_card"], "thumb22_sec_card", "thumb22_hover_sec_card" ))
    gallery_items.append(GalleryItem("23", ["img23_sec_card"], "thumb23_sec_card", "thumb23_hover_sec_card" ))
    gallery_items.append(GalleryItem("24", ["img24_sec_card"], "thumb24_sec_card", "thumb24_hover_sec_card" ))
    gallery_items.append(GalleryItem("25", ["img25_sec_card"], "thumb25_sec_card", "thumb25_hover_sec_card" ))

    gallery_items.append(GalleryItem("26", ["img26_sec_card"], "thumb26_sec_card", "thumb26_hover_sec_card" ))
    gallery_items.append(GalleryItem("27", ["img27_sec_card"], "thumb27_sec_card", "thumb27_hover_sec_card" ))
    gallery_items.append(GalleryItem("28", ["img28_sec_card"], "thumb28_sec_card", "thumb28_hover_sec_card" ))
    gallery_items.append(GalleryItem("29", ["img29_sec_card"], "thumb29_sec_card", "thumb29_hover_sec_card" ))
    gallery_items.append(GalleryItem("30", ["img30_sec_card"], "thumb30_sec_card", "thumb30_hover_sec_card" ))
    gallery_items.append(GalleryItem("31", ["img31_sec_card"], "thumb31_sec_card", "thumb31_hover_sec_card" ))
    gallery_items.append(GalleryItem("32", ["img32_sec_card"], "thumb32_sec_card", "thumb32_hover_sec_card" ))
    gallery_items.append(GalleryItem("33", ["img33_sec_card"], "thumb33_sec_card", "thumb33_hover_sec_card" ))
    gallery_items.append(GalleryItem("34", ["img34_sec_card"], "thumb34_sec_card", "thumb34_hover_sec_card" ))
    gallery_items.append(GalleryItem("35", ["img35_sec_card"], "thumb35_sec_card", "thumb35_hover_sec_card" ))

    gallery_items.append(GalleryItem("36", ["img36_sec_card"], "thumb36_sec_card", "thumb36_hover_sec_card" ))
    gallery_items.append(GalleryItem("37", ["img37_sec_card"], "thumb37_sec_card", "thumb37_hover_sec_card" ))
    gallery_items.append(GalleryItem("38", ["img38_sec_card"], "thumb38_sec_card", "thumb38_hover_sec_card" ))
    gallery_items.append(GalleryItem("39", ["img39_sec_card"], "thumb39_sec_card", "thumb39_hover_sec_card" ))
    gallery_items.append(GalleryItem("40", ["img40_sec_card"], "thumb40_sec_card", "thumb40_hover_sec_card" ))
    gallery_items.append(GalleryItem("41", ["img41_sec_card"], "thumb41_sec_card", "thumb41_hover_sec_card" ))
    gallery_items.append(GalleryItem("42", ["img42_sec_card"], "thumb42_sec_card", "thumb42_hover_sec_card" ))
