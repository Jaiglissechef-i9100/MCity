init python:

    def MaxScale2(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight
        
        if xscale > yscale:
            maxscale2 = xscale
        else:
            maxscale2 = yscale
        
        return im.FactorScale(img, maxscale2, maxscale2)

    def MinScale2(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight
        
        if xscale < yscale:
            minscale2 = xscale
        else:
            minscale2 = yscale
        
        return im.FactorScale(img, minscale2, minscale2)

    maxnumx2 = 3
    maxnumy2 = 3
    maxthumbx2 = config.screen_width / (maxnumx2 + 1)
    maxthumby2 = config.screen_height / (maxnumy2 + 1)
    maxperpage2 = maxnumx2 * maxnumy2
    gallery_page2 = 0
    closeup_page2 = 0

    class Scenes_GalleryItem:
        def __init__(self, name, images, thumb, thumb_hover, locked2="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.thumb_hover = thumb_hover
            self.locked2 = locked2
            self.refresh_lock2()
        
        def num_images2(self):
            return len(self.images)
        
        def refresh_lock2(self):
            self.num_unlocked2 = 0
            lockme2 = False
            for img in self.images:
                if not img in scenes_gallery_photos.storage:
                    lockme2 = True
                else:
                    self.num_unlocked2 += 1
            self.is_locked2 = lockme2

    class Scenes_Gallery_photos(store.object):
        def __init__(self,):
            self.storage = []
        
        def add1(self, img): 
            self.storage.append(img)

    class addgimage_scenes(Action):
        
        def __init__(self, img):
            self.img = img
        
        def __call__(self):
            scenes_gallery_photos.storage.append(self.img)
            renpy.restart_interaction()

    scenes_gallery_photos = Scenes_Gallery_photos()
    scenes_gallery_items = []
    scenes_gallery_items.append(Scenes_GalleryItem("sara_pad_lose_v1", ["img1_sara_evening_pad_lose"], "thumb1_idle_sara_evening_pad_lose","thumb1_hover_sara_evening_pad_lose" ))
    scenes_gallery_items.append(Scenes_GalleryItem("sara_pad_win_v1", ["img2_sara_evening_pad_win"], "thumb2_idle_sara_evening_pad_win","thumb2_hover_sara_evening_pad_win" ))
    scenes_gallery_items.append(Scenes_GalleryItem("sara_night_visit_v1", ["img3_sara_night_visit_v1"], "thumb3_idle_sara_night_visit_v1","thumb3_hover_sara_night_visit_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("sara_botlle_game_v1", ["img4_sara_botlle_game_v1"], "thumb4_idle_sara_botlle_game_v1","thumb4_hover_sara_botlle_game_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("celia_toilet_kiss_v1", ["img5_celia_toilet_kiss_v1"], "thumb5_idle_celia_toilet_kiss_v1","thumb5_hover_celia_toilet_kiss_v1 " ))
    scenes_gallery_items.append(Scenes_GalleryItem("celia_toilet_fuck_v1", ["img6_celia_toilet_fuck_v1"], "thumb6_idle_celia_toilet_fuck_v1","thumb6_hover_celia_toilet_fuck_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("celia_vibrator_classroom_v1", ["img7_celia_vibrator_classroom_v1"], "thumb7_idle_celia_vibrator_classroom_v1","thumb7_hover_celia_vibrator_classroom_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("caroline_ass_cosplay_v1", ["img8_caroline_ass_cosplay_v1"], "thumb8_idle_caroline_ass_cosplay_v1","thumb8_hover_caroline_ass_cosplay_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("violet_blowjob_v1", ["img9_violet_blowjob_v1"], "thumb9_idle_violet_blowjob_v1","thumb9_hover_violet_blowjob_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("caroline_visit_bjfjhj_v1", ["img10_caroline_visit_bjfjhj_v1"], "thumb10_idle_caroline_visit_bjfjhj_v1","thumb10_hover_caroline_visit_bjfjhj_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("mom_car_v1", ["img11_mom_car_v1"], "thumb11_idle_mom_car_v1","thumb11_hover_mom_car_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("ml_work_hj_v1", ["img12_mom_work_hj_v1"], "thumb12_idle_mom_work_hj_v1","thumb12_hover_mom_work_hj_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("ml_room_fj_v1", ["img13_ml_room_fj_v1"], "thumb13_idle_ml_room_fj_v1","thumb13_hover_ml_room_fj_v1 " ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR2_ES3_rep", ["img14_MLR2_ES3_rep"], "thumb14_idle_MLR2_ES3_rep","thumb14_hover_MLR2_ES3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR2_NS2_rep", ["img15_MLR2_NS2_rep"], "thumb15_idle_MLR2_NS2_rep","thumb15_hover_MLR2_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR2_weekend_rep", ["img16_MLR2_weekend_rep"], "thumb16_idle_MLR2_weekend_rep","thumb16_hover_MLR2_weekend_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR2_AS1_rep", ["img17_CR2_AS1_rep"], "thumb17_idle_CR2_AS1_rep","thumb17_hover_CR2_AS1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR2_AS2_rep", ["img18_CR2_AS2_rep"], "thumb18_idle_CR2_AS2_rep","thumb18_hover_CR2_AS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR2_NS2_rep", ["img19_CR2_NS2_rep"], "thumb19_idle_CR2_NS2_rep","thumb19_hover_CR2_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Z_ES2_rep", ["img20_Z_ES2_rep"], "thumb20_idle_Z_ES2_rep","thumb20_hover_Z_ES2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Z_ES3_rep", ["img21_Z_ES3_rep"], "thumb21_idle_Z_ES3_rep","thumb21_hover_Z_ES3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Z_ES4_rep", ["img22_Z_ES4_rep"], "thumb22_idle_Z_ES4_rep","thumb22_hover_Z_ES4_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_NS2_rep", ["img23_SR2_NS2_rep"], "thumb23_idle_SR2_NS2_rep","thumb23_hover_SR2_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_ES1_rep", ["img24_SR2_ES1_rep"], "thumb24_idle_SR2_ES1_rep","thumb24_hover_SR2_ES1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_NS3_rep", ["img25_SR2_NS3_rep"], "thumb25_idle_SR2_NS3_rep","thumb25_hover_SR2_NS3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_NS4_rep", ["img26_SR2_NS4_rep"], "thumb26_idle_SR2_NS4_rep","thumb26_hover_SR2_NS4_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR3_week_rep", ["img27_CR3_week_rep"], "thumb27_idle_CR3_week_rep","thumb27_hover_CR3_week_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR3_week2_rep", ["img28_CR3_week2_rep"], "thumb28_idle_CR3_week2_rep","thumb28_hover_CR3_week2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR3_AS8_rep", ["img29_CR3_AS8_rep"], "thumb29_idle_CR3_AS8_rep","thumb29_hover_CR3_AS8_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR3_AS9_rep", ["img30_CR3_AS9_rep"], "thumb30_idle_CR3_AS9_rep","thumb30_hover_CR3_AS9_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR3_NS2_rep", ["img31_CR3_NS2_rep"], "thumb31_idle_CR3_NS2_rep","thumb31_hover_CR3_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR3_NS3_rep", ["img32_CR3_NS3_rep"], "thumb32_idle_CR3_NS3_rep","thumb32_hover_CR3_NS3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR3_NS5_rep", ["img33_CR3_NS5_rep"], "thumb33_idle_CR3_NS5_rep","thumb33_hover_CR3_NS5_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("LiR1_NS1_rep", ["img34_LiR1_NS1_rep"], "thumb34_idle_LiR1_NS1_rep","thumb34_hover_LiR1_NS1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("LiR1_NS2_rep", ["img35_LiR1_NS2_rep"], "thumb35_idle_LiR1_NS2_rep","thumb35_hover_LiR1_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("LiR1_MS6_rep", ["img36_LiR1_MS6_rep"], "thumb36_idle_LiR1_MS6_rep","thumb36_hover_LiR1_MS6_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("LiR1_NS4_rep", ["img37_LiR1_NS4_rep"], "thumb37_idle_LiR1_NS4_rep","thumb37_hover_LiR1_NS4_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("LiR1_MS9_rep", ["img38_LiR1_MS9_rep"], "thumb38_idle_LiR1_MS9_rep","thumb38_hover_LiR1_MS9_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("LiR1_NS5_rep", ["img39_LiR1_NS5_rep"], "thumb39_idle_LiR1_NS5_rep","thumb39_hover_LiR1_NS5_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR3_B_event_rep", ["img40_MLR3_B_event_rep"], "thumb40_idle_MLR3_B_event_rep","thumb40_hover_MLR3_B_event_rep" ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR3_b_house_shower_rep", ["img41_MLR3_b_house_shower_rep"], "thumb41_idle_MLR3_b_house_shower_rep","thumb41_hover_MLR3_b_house_shower_rep" ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR3_AS3_rep", ["img42_MLR3_AS3_rep"], "thumb42_idle_MLR3_AS3_rep","thumb42_hover_MLR3_AS3_rep" ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR3_NS1_rep", ["img43_MLR3_NS1_rep"], "thumb43_idle_MLR3_NS1_rep","thumb43_hover_MLR3_NS1_rep" ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR3_NS2_rep", ["img44_MLR3_NS2_rep"], "thumb44_idle_MLR3_NS2_rep","thumb44_hover_MLR3_NS2_rep" ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_AS1_rep", ["img45_CeR2_AS1_rep"], "thumb45_idle_CeR2_AS1_rep","thumb45_hover_CeR2_AS1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_AS2_rep", ["img46_CeR2_AS2_rep"], "thumb46_idle_CeR2_AS2_rep","thumb46_hover_CeR2_AS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_AS3_rep", ["img47_CeR2_AS3_rep"], "thumb47_idle_CeR2_AS3_rep","thumb47_hover_CeR2_AS3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_ES2_rep", ["img48_CeR2_ES2_rep"], "thumb48_idle_CeR2_ES2_rep","thumb48_hover_CeR2_ES2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_NS1_rep", ["img49_CeR2_NS1_rep"], "thumb49_idle_CeR2_NS1_rep","thumb49_hover_CeR2_NS1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_NS1a_rep", ["img50_CeR2_NS1a_rep"], "thumb50_idle_CeR2_NS1a_rep","thumb50_hover_CeR2_NS1a_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_NS2_rep", ["img51_CeR2_NS2_rep"], "thumb51_idle_CeR2_NS2_rep","thumb51_hover_CeR2_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_NS3_rep", ["img52_CeR2_NS3_rep"], "thumb52_idle_CeR2_NS3_rep","thumb52_hover_CeR2_NS3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CeR2_We_rep", ["img53_CeR2_We_rep"], "thumb53_idle_CeR2_We_rep","thumb53_hover_CeR2_We_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Ne_ES1_rep", ["img54_Ne_ES1_rep"], "thumb54_idle_Ne_ES1_rep","thumb54_hover_Ne_ES1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Ne_ES2_rep", ["img55_Ne_ES2_rep"], "thumb55_idle_Ne_ES2_rep","thumb55_hover_Ne_ES2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR4_MS1_rep", ["img56_CR4_MS1_rep"], "thumb56_idle_CR4_MS1_rep","thumb56_hover_CR4_MS1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR4_NS1_rep", ["img57_CR4_NS1_rep"], "thumb57_idle_CR4_NS1_rep","thumb57_hover_CR4_NS1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR4_NS1a_rep", ["img58_CR4_NS1a_rep"], "thumb58_idle_CR4_NS1a_rep","thumb58_hover_CR4_NS1a_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR4_NS3_rep", ["img59_CR4_NS3_rep"], "thumb59_idle_CR4_NS3_rep","thumb59_hover_CR4_NS3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR4_NS3a_rep", ["img60_CR4_NS3a_rep"], "thumb60_idle_CR4_NS3a_rep","thumb60_hover_CR4_NS3a_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR4_We_rep", ["img61_CR4_We_rep"], "thumb61_idle_CR4_We_rep","thumb61_hover_CR4_We_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Ci_S1_rep", ["img62_Ci_S1_rep"], "thumb62_idle_Ci_S1_rep","thumb62_hover_Ci_S1_rep " ))
