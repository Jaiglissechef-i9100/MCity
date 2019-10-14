default can_gallery_scenes_ml_unlocked = True
default can_gallery_scenes_caroline_unlocked = True
default can_gallery_scenes_celia_unlocked = True
default can_gallery_scenes_sara_unlocked = True

default CR2_rep = True
default MLR2_rep = True
default Z_rep = True
default SR2_rep = True

default CR3_rep = True
default LiR1_rep = True

default MLR3_rep = True
label gallery_label:
    if renpy.loadable("patch.rpy"):
        $ Linda_name = "Mom"
        $ Liza2_name = "Auntie"
    else:
        $ Mom_name = "Linda"
        $ Liza2_name = "Liza"
    if can_gallery_scenes_sara_unlocked == True and Sara_points >= 2:
        $ scenes_gallery_photos.add1("img1_sara_evening_pad_lose")
        $ scenes_gallery_photos.add1("img2_sara_evening_pad_win")
        $ scenes_gallery_photos.add1("img3_sara_night_visit_v1")
        $ scenes_gallery_photos.add1("img4_sara_botlle_game_v1")
        $ can_gallery_scenes_sara_unlocked = False
    if can_gallery_scenes_celia_unlocked == True and Celia_points >= 2:
        $ scenes_gallery_photos.add1("img5_celia_toilet_kiss_v1")
        $ scenes_gallery_photos.add1("img6_celia_toilet_fuck_v1")
        $ scenes_gallery_photos.add1("img7_celia_vibrator_classroom_v1")
        $ can_gallery_scenes_celia_unlocked = False
    if can_gallery_scenes_caroline_unlocked == True and Caroline_points >= 2:
        $ scenes_gallery_photos.add1("img8_caroline_ass_cosplay_v1")
        $ scenes_gallery_photos.add1("img9_violet_blowjob_v1")
        $ scenes_gallery_photos.add1("img10_caroline_visit_bjfjhj_v1")
        $ can_gallery_scenes_caroline_unlocked = False
    if can_gallery_scenes_ml_unlocked == True and ml_points >= 2:
        $ scenes_gallery_photos.add1("img11_mom_car_v1")
        $ scenes_gallery_photos.add1("img12_mom_work_hj_v1")
        $ scenes_gallery_photos.add1("img13_ml_room_fj_v1")
        $ can_gallery_scenes_ml_unlocked = False

    if CR2_rep == True and Caroline_points >= 3:
        $ scenes_gallery_photos.add1("img17_CR2_AS1_rep")
        $ scenes_gallery_photos.add1("img18_CR2_AS2_rep")
        $ scenes_gallery_photos.add1("img19_CR2_NS2_rep")
        $ CR2_rep = False

    if MLR2_rep == True and ml_points >= 3:
        $ scenes_gallery_photos.add1("img14_MLR2_ES3_rep")
        $ scenes_gallery_photos.add1("img15_MLR2_NS2_rep")
        $ scenes_gallery_photos.add1("img16_MLR2_weekend_rep")
        $ MLR2_rep = False
    if Z_rep == True and Z_points >= 2:
        $ scenes_gallery_photos.add1("img20_Z_ES2_rep")
        $ scenes_gallery_photos.add1("img21_Z_ES3_rep")
        $ scenes_gallery_photos.add1("img22_Z_ES4_rep")
        $ Z_rep = False

    if SR2_rep == True and Sara_points >=3:
        $ scenes_gallery_photos.add1("img23_SR2_NS2_rep")
        $ scenes_gallery_photos.add1("img24_SR2_ES1_rep")
        $ scenes_gallery_photos.add1("img25_SR2_NS3_rep")
        $ scenes_gallery_photos.add1("img26_SR2_NS4_rep")
        $ SR2_rep = False

    if Caroline_points >=4 and CR3_rep == True:
        $ scenes_gallery_photos.add1("img27_CR3_week_rep")
        $ scenes_gallery_photos.add1("img28_CR3_week2_rep")
        $ scenes_gallery_photos.add1("img29_CR3_AS8_rep")
        $ scenes_gallery_photos.add1("img30_CR3_AS9_rep")
        $ scenes_gallery_photos.add1("img31_CR3_NS2_rep")
        $ scenes_gallery_photos.add1("img32_CR3_NS3_rep")
        $ scenes_gallery_photos.add1("img33_CR3_NS5_rep")
        $ CR3_rep = False

    if Li_points >=2 and LiR1_rep == True:
        $ scenes_gallery_photos.add1("img34_LiR1_NS1_rep")
        $ scenes_gallery_photos.add1("img35_LiR1_NS2_rep")
        $ scenes_gallery_photos.add1("img36_LiR1_MS6_rep")
        $ scenes_gallery_photos.add1("img37_LiR1_NS4_rep")
        $ scenes_gallery_photos.add1("img38_LiR1_MS9_rep")
        $ scenes_gallery_photos.add1("img39_LiR1_NS5_rep")
        $ LiR1_rep = False
    if ml_points >=4 and MLR3_rep == True:
        $ scenes_gallery_photos.add1("img40_MLR3_B_event_rep")
        $ scenes_gallery_photos.add1("img41_MLR3_b_house_shower_rep")
        $ scenes_gallery_photos.add1("img42_MLR3_AS3_rep")
        $ scenes_gallery_photos.add1("img43_MLR3_NS1_rep")
        $ scenes_gallery_photos.add1("img44_MLR3_NS2_rep")
        $ MLR3_rep = False
    scene main_deskop
    call screen scenes_gallery