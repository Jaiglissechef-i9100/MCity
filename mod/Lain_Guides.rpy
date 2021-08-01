screen mod_linda_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_linda_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_linda_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if not salon_ml_first_visit:
            text "Linda Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Living room" pos (533, 105) xanchor 1.0

        elif d_ml_and_f_bedroom_mornig_scene_visit == 1:
            text "Linda Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- Talk to Bob and ask him for money" pos (34, 142)

        elif ml_ml_and_f_bedroom_night_visit_scene_v1 == 1:
            text "Linda Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0

        elif ml_salon_morning_visit == 1:
            text "Linda Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Living room" pos (533, 105) xanchor 1.0

        elif d_ml_and_f_bedroom_mornig_scene_visit == 2:
            text "Linda Walkthrough - Step 5" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- Ask Bob for money" pos (34, 142)

        elif ml_bedroom_book_scene and ml_points == 1:
            text "Linda Walkthrough - Step 6" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- Click the book on the right bedside table" pos (34, 142)

        elif ml_salon_morning_visit == 2:
            text "Linda Walkthrough - Step 7" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Living room" pos (533, 105) xanchor 1.0
            text "- \"Yes\"" pos (34, 142)
            text "- Go to the kitchen and wash the dishes" pos (34, 172)

        elif d_ml_and_f_bedroom_mornig_scene_visit == 3:
            text "Linda Walkthrough - Step 8" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- Ask Bob for money" pos (34, 142)

        elif not b4_spy_camera_buy:
            text "Linda Walkthrough - Step 9" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Kitchen bathroom" pos (533, 105) xanchor 1.0
            text "- Buy the spy camera ($55)" pos (34, 142)
            text "- Optional: Use the spy cam on the bathroom door" pos (34, 172) size 21
            text "- (This step will disappear after buying the cam. Remember\n   to use the cam if you want to see the scene)" pos (34, 202) size 18

        elif ml_salon_morning_visit == 3:
            text "Linda Walkthrough - Step 10" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Living room" pos (533, 105) xanchor 1.0

        elif ml_salon_morning_visit == 4:
            text "Linda Walkthrough - Step 11" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Kitchen" pos (533, 105) xanchor 1.0
            if not ml_can_salon_morning_scene:
                text "- Talk to Linda in the kitchen tomorrow morning" pos (34, 142)

        elif not ml_work_unloacked:
            text "Linda Walkthrough - Step 12" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            if not ml_can_bedroom_morning_scene5:
                text "- Talk to Linda in her room tomorrow morning" pos (34, 142)

        elif ml_work_day_scene1:
            text "Linda Walkthrough - Step 13" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Linda's office" pos (533, 105) xanchor 1.0
            if not can_ml_work_day_scene1:
                text "- Go to Linda's office tomorrow afternoon" pos (34, 142)

        elif ml_bedroom_morning_scene6:
            text "Linda Walkthrough - Step 14" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0

        elif not ml_mc_room_night_scene3:
            text "Linda Walkthrough - Step 15" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Linda's office" pos (533, 105) xanchor 1.0
            if not can_ml_work_day_scene2:
                text "- Go to Linda's office tomorrow afternoon" pos (34, 142)

        elif ml_points == 1:
            text "Linda Walkthrough - Step 16" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif MLR2_MS1_kiss_count == 1:
            text "Linda Walkthrough - Step 17" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- Do all the dialogue options" pos (34, 142)

        elif MLR2_ES1:
            text "Linda Walkthrough - Step 18" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Kitchen" pos (533, 105) xanchor 1.0

        elif MLR2_MS1_NS1 == False:
            text "Linda Walkthrough - Step 19" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            if not MLR2_Sleep:
                text "- Go to Linda's room tomorrow night" pos (34, 142)

        elif MLR2_MS1_NS1 == True:
            text "Linda Walkthrough - Step 20" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- \"Talk about Bob\"" pos (34, 142)

        elif ml_workR2_AS1:
            text "Linda Walkthrough - Step 21" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Linda's office" pos (533, 105) xanchor 1.0

        elif not can_ml_workR2_AS2:
            text "Linda Walkthrough - Step 22" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0

        elif MLR2_NS2:
            text "Linda Walkthrough - Step 23" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            if not MLR2_Sleep:
                text "- Go to Linda's room tomorrow night" pos (34, 142)

        elif MLR2_MS1_talk_count == 3:
            text "Linda Walkthrough - Step 24" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0

        elif not can1_MLR2_ES1:
            text "Linda Walkthrough - Step 25" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Linda's office" pos (533, 105) xanchor 1.0

        elif not Bob_v2_scenes:
            if not MLR2_ES3:
                text "Linda Walkthrough - Step 26" pos (27, 70) font "mod/OSB.ttf"
                text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
                text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
                text "- \"Talk about Bob\"" pos (34, 142)
            else:
                text "- The food choice doesn't matter, but she likes the bottom left dish" pos (34, 146) size 16
                text "- If you choose \"Try to stop her\" you will get a blowjob instead of footjob" pos (34, 172)

        elif Zv2_MS2_q4:
            text "Linda Walkthrough - Step 27" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Bob's office" pos (533, 105) xanchor 1.0
            text "- Talk to the receptionist then ask Bob for his keycard" pos (34, 142) size 20
            text "- \"Peek up her skirt\"" pos (34, 172)
            text "- Go back to Zuri and ask for her card" pos (34, 202)

        elif MLR2_MS1_BCalendar == False:
            text "Linda Walkthrough - Step 28" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Bob's workplace" pos (533, 105) xanchor 1.0
            if not Zv2_MS2_q5:
                text "- Talk to Zuri at Bob's office tomorrow morning" pos (34, 142)
            else:
                text "- Talk to Zuri and ask about Bob's business trip" pos (34, 142)

        elif not MLR2_weekend_event:
            text "Linda Walkthrough - Step 29" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- \"Talk about the trip\"" pos (34, 142)

        elif not red_wine_buy:
            text "Linda Walkthrough - Step 30" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Shop" pos (533, 105) xanchor 1.0
            text "- Buy the red wine ($95)" pos (34, 142)

        elif ml_points < 3:
            text "Linda Walkthrough - Step 31" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Weekend" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            text "- \"Mom weekend event\"" pos (34, 142)

        elif MLR3_MS1_can == True:
            text "Linda Walkthrough - Step 32" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0

        elif MLR3_ES1 and not MLR3_ES1_end:
            text "Linda Walkthrough - Step 33" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Kitchen" pos (533, 105) xanchor 1.0

        elif MLR3_Linda_MS1_day == 1 or MLR3_Linda_MS1_day == 2:
            text "Linda Walkthrough - Step 34" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- Talk to Linda and Bob" pos (34, 142)

        elif MLR3_MS2_can:
            text "Linda Walkthrough - Step 35" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0

        elif MLR3_MS3 == 2 or MLR3_MS3 == True:
            text "Linda Walkthrough - Step 36" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            if MLR3_MS3 == 2:
                text "- Talk to Linda in her room tomorrow morning" pos (34, 142)

        elif MLR3_AS2_event_can or MLR3_AS2_event != 3:
            text "Linda Walkthrough - Step 37" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Linda's office" pos (533, 105) xanchor 1.0
            if MLR3_AS2_event_can:
                text "- Go to Linda's office tomorrow afternoon" pos (34, 142)

        elif judy_q3:
            text "Linda Walkthrough - Step 38" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 19
            text "{font=mod/OSB.ttf}Location: {/font}Therapist's room" pos (533, 107) xanchor 1.0 size 19

        elif headmaster_S2:
            text "Linda Walkthrough - Step 39" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 109) size 18
            text "{font=mod/OSB.ttf}Location: {/font}Headmaster's room" pos (533, 109) xanchor 1.0 size 18
            if headmaster_door_locked:
                text "- Go to the school headmaster's office tomorrow" pos (34, 142)
                text "- Choose: \"Stand in front of the door\" at the end\nfor a scene" pos (34, 172)
            else:
                text "- Choose: \"Stand in front of the door\" at the end\nfor a scene" pos (34, 142)

        elif MLR3_Bob_AS1_q7:
            text "Linda Walkthrough - Step 40" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- \"Talk about the trip\"" pos (34, 142)

        elif MLR3_beach_event:
            if MLR3_beach_done == 0:
                text "Linda Walkthrough - Step 41" pos (27, 70) font "mod/OSB.ttf"
                text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
                text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
                text "- Go to sleep to trigger the event" pos (34, 142)
            else:
                text "Linda Walkthrough - Beach event" pos (27, 70) font "mod/OSB.ttf"

        elif MLR2_R3_MS1_q1:
            text "Linda Walkthrough - Step 42" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0
            text "- \"Are you missing our holiday?\"" pos (34, 142)

        elif MLR3_AS3 == 3:
            text "Linda Walkthrough - Step 43" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif MLR3_NS1 == 3:
            text "Linda Walkthrough - Step 44" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Parent's room" pos (533, 105) xanchor 1.0

        elif MLR3_NS1 == 4 or MLR3_NS1 == 5 or MLR3_NS2:
            text "Linda Walkthrough - Step 45" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            text "- Go to sleep to trigger the event" pos (34, 142)

        elif ml_points >= 4:
            text "Linda's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Linda's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

default mod_caroline_step_23_complete = False
default mod_caroline_step_24_complete = False
default mod_caroline_step_28_complete = False
default mod_caroline_step_30_complete = False
default mod_caroline_step_33_complete = False

screen mod_caroline_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_caroline_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_caroline_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if caroline_morning_scenes_visit == 1:
            text "Caroline Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            text "- Choose any dialogue option" pos (34, 142)

        elif caroline_morning_scenes_visit == 2:
            text "Caroline Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            if not caroline_can_room_morning_scenes:
                text "- Talk to Caroline tomorrow morning" pos (34, 142)

        elif caroline_morning_scenes_visit == 3:
            text "Caroline Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            if not caroline_can_room_morning_scenes:
                text "- Talk to Caroline tomorrow morning" pos (34, 142)

        elif caroline_cloth_shop_have_camera == 1:
            text "Caroline Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif cloth_shop_window_unlock == False:
            text "Caroline Walkthrough - Step 5" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Go to the left room and unlock the window" pos (34, 142)

        elif caroline_cloth_shop_have_camera == 2 and not camera1 in inventory.items:
            text "Caroline Walkthrough - Step 6" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Shop" pos (533, 105) xanchor 1.0
            text "- Buy the camera ($80)" pos (34, 142)

        elif caroline_cloth_shop_have_camera == 2 and camera1 in inventory.items:
            text "Caroline Walkthrough - Step 7" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif cloth_shop_window_unlock == True:
            text "Caroline Walkthrough - Step 8" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif not caroline_door_open:
            text "Caroline Walkthrough - Step 9" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            text "- Select Caroline's key in your inventory click her\ndoor" pos (34, 142)

        elif caroline_room_morning_scene4 == True:
            text "Caroline Walkthrough - Step 10" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif cosplay_unlock_switch < 2:
            text "Caroline Walkthrough - Step 11" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Do a photoshoot with Caroline" pos (34, 142)

        elif caroline_salon_evening_scene1:
            text "Caroline Walkthrough - Step 12" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Do a photoshoot with Caroline's 5th outfit" pos (34, 142)

        elif caroline_mc_room_evening_scene2:
            text "Caroline Walkthrough - Step 13" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif caroline_mc_room_evening_scene3:
            text "Caroline Walkthrough - Step 14" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            if not caroline_mc_room_can_evening_scene3:
                text "- Talk to Caroline tomorrow evening" pos (34, 142)

        elif cosplay_unlock_switch < 4:
            text "Caroline Walkthrough - Step 15" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Do a photoshoot with Caroline" pos (34, 142)

        elif caroline_closth_shop_afternoon_scene3:
            text "Caroline Walkthrough - Step 16" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Do a photoshoot with Caroline's 6th outfit" pos (34, 142)

        elif caroline_room_evening_scene4 == True:
            text "Caroline Walkthrough - Step 17" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif caroline_mc_room_moenig_scene5:
            text "Caroline Walkthrough - Step 18" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif can_CR2_MS1:
            text "Caroline Walkthrough - Step 19" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            text "- Choose either option" pos (34, 142)

        elif CR2_before_robber:
            text "Caroline Walkthrough - Step 20" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Do the photoshoots for all four outfits" pos (34, 142)

        elif CR2_AS3:
            text "Caroline Walkthrough - Step 21" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR2_AS3a:
            text "Caroline Walkthrough - Step 22" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Clean up all the items then talk to Caroline" pos (34, 142)

        elif not mod_caroline_step_23_complete and can_CR2_NS3:
            text "Caroline Walkthrough - Step 23" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

            textbutton "Fuck this fucking game's awful programming. If you've\nread her text message at night and went to her room,\nclick here to advance to the next walkthrough step." pos (25, 140) text_style "modguide_text" text_size 19 text_hover_color "#66c1e0" action SetVariable("mod_caroline_step_23_complete", True)

        elif not mod_caroline_step_24_complete and Caroline_points == 2:
            text "Caroline Walkthrough - Step 24" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            textbutton "Fuck this fucking game's awful programming.\nIf you've talked to her in the morning, click\nhere to advance to the next walkthrough step." pos (25, 135) text_style "modguide_text" text_hover_color "#66c1e0" action SetVariable("mod_caroline_step_24_complete", True)

        elif CR2_AS4:
            text "Caroline Walkthrough - Step 25" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Pick up the bottle on the floor" pos (34, 142)

        elif CR2_AS5:
            text "Caroline Walkthrough - Step 26" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Go through the left door and talk to her" pos (34, 142)

        elif not can1_CR2_MS2:
            text "Caroline Walkthrough - Step 27" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Living room" pos (533, 105) xanchor 1.0
            text "- Talk to Caroline about Violet" pos (34, 142)

        elif not mod_caroline_step_28_complete and Caroline_points == 2:
            text "Caroline Walkthrough - Step 28" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- Talk to Caroline only when you have $200" pos (34, 142)
            text "- \"Of course! I have two hundred here.\"" pos (34, 172)
            textbutton "Click {b}here{/b} to advance to the next walkthrough step." pos (25, 202) text_style "modguide_text" text_size 20 text_hover_color "#66c1e0" action SetVariable("mod_caroline_step_28_complete", True)

        elif violetV2_scene:
            text "Caroline Walkthrough - Step 29" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Dark Alley" pos (533, 105) xanchor 1.0
            text "- Go to the dark alley at the bottom right of the\nmap" pos (34, 142)

        elif not mod_caroline_step_30_complete and Caroline_points == 2:
            text "Caroline Walkthrough - Step 30" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- Talk to Caroline only when you have $150" pos (34, 142)
            text "- \"Yeah, I have $150 here.\"" pos (34, 172)
            textbutton "Click {b}here{/b} to advance to the next walkthrough step." pos (25, 202) text_style "modguide_text" text_size 20 text_hover_color "#66c1e0" action SetVariable("mod_caroline_step_30_complete", True)

        elif Caroline_points == 2:
            text "Caroline Walkthrough - Step 31" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Outside your house" pos (533, 105) xanchor 1.0
            text "- Choose any dialogue options" pos (34, 142)

        elif CR3_MS0:
            text "Caroline Walkthrough - Step 32" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif not mod_caroline_step_33_complete and Caroline_points == 3:
            text "Caroline Walkthrough - Step 33" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Outside your house" pos (533, 105) xanchor 1.0
            if not CR3_MS2_can3:
                text "- Talk to Caroline tomorrow morning" pos (34, 142)
            textbutton "Click {b}here{/b} to advance to the next walkthrough step." pos (25, 202) text_style "modguide_text" text_size 20 text_hover_color "#66c1e0" action SetVariable("mod_caroline_step_33_complete", True)

        elif CR3_MS1_q3:
            text "Caroline Walkthrough - Step 34" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            if not CR3_MS1:
                text "- Talk to Caroline tomorrow morning" pos (34, 142)

        elif CR3_AS1_can == True:
            text "Caroline Walkthrough - Step 35" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR2_VS:
            text "Caroline Walkthrough - Step 36" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Dark Alley" pos (533, 105) xanchor 1.0
            text "- Talk to Violet in the dark alley at the bottom\nright of the map" pos (34, 142)

        elif CR3_ES1_can and Caroline_points == 3:
            text "Caroline Walkthrough - Step 37" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Kitchen" pos (533, 105) xanchor 1.0

        elif CR3_NS1_can and CR3_NS1:
            text "Caroline Walkthrough - Step 38" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif CR3_AS5_can < 2:
            text "Caroline Walkthrough - Step 39" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- Do the photoshoots for two outfits" pos (34, 142)

        elif CR3_AS5_can == 2:
            text "Caroline Walkthrough - Step 40" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif not CR3_weekend_event:
            text "Caroline Walkthrough - Step 41" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            if CR3_AS5_can < 6:
                text "- Wait for a 3 days to pass before visiting the\nshop" pos (34, 142)

        elif CR3_WE == 0:
            text "Caroline Walkthrough - Step 42" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Weekend" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            text "- Weekend event -> Meet up with Caroline ($200)" pos (34, 142)

        elif CR3_WE >= 1 and CR3_WE <= 4:
            text "Caroline Walkthrough - Step 42" pos (27, 70) font "mod/OSB.ttf"

        elif CR3_WE == 5 and CR3_weekend_event != 3:
            text "Caroline Walkthrough - Step 42" pos (27, 70) font "mod/OSB.ttf"
            text "- Choose: \"Maybe I could play with her body\"" pos (34, 142)

        elif CR3_AS7_can and CR3_AS7:
            text "Caroline Walkthrough - Step 43" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR3_ES2_can and Caroline_points == 3:
            text "Caroline Walkthrough - Step 44" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif CR3_NS2_can:
            text "Caroline Walkthrough - Step 45" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif CR3_AS7a_can1:
            text "Caroline Walkthrough - Step 46" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0
            text "- Click her bed" pos (34, 142)

        elif outfit_start == 2:
            text "Caroline Walkthrough - Step 47" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR3_NS3_can:
            text "Caroline Walkthrough - Step 48" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif CR3_MS3_can and Caroline_points == 3:
            text "Caroline Walkthrough - Step 49" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif outfit_start == 3:
            text "Caroline Walkthrough - Step 50" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR3_AS10_can:
            text "Caroline Walkthrough - Step 51" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR3_NS5 and Caroline_points == 3:
            text "Caroline Walkthrough - Step 52" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            text "- Go to sleep to trigger the event" pos (34, 142)

        elif not CR4_MS1_talked:
            text "Caroline Walkthrough - Step 53" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif CR4_AS1 == True:
            text "Caroline Walkthrough - Step 54" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR4_NS1 != False:
            text "Caroline Walkthrough - Step 55" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            text "- \"Meet up with Caroline\"" pos (34, 142)

        elif CR4_AS2 == 1:
            text "Caroline Walkthrough - Step 56" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR4_AS2 == 3:
            text "Caroline Walkthrough - Step 57" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif CR4_NS3 == 1:
            text "Caroline Walkthrough - Step 58" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Caroline's room" pos (533, 105) xanchor 1.0

        elif CR4_AS3 < 6:
            text "Caroline Walkthrough - Step 59" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0
            text "- \"Help Caroline in the shop for three days\"" pos (34, 142)

        elif CR4_AS3 == 6:
            text "Caroline Walkthrough - Step 60" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif crowbar not in inventory.items:
            text "Caroline Walkthrough - Step 61" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your garage" pos (533, 105) xanchor 1.0
            text "- Take the crowbar on the wall" pos (34, 142)

        elif not CR4_guard:
            text "Caroline Walkthrough - Step 62" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Charles's home" pos (533, 105) xanchor 1.0
            text "- Select the crowbar in your inventory and click\nthe window to the right of Charles's door" pos (34, 142)

        elif not CR4_Cindy_S1 or CR4_Cindy_S1 == 1:
            text "Caroline Walkthrough - Step 63" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Nightclub" pos (533, 105) xanchor 1.0

        elif CR4_Cindy_S1 == 2:
            text "Caroline Walkthrough - Step 64" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Nightclub warehouse" pos (533, 105) xanchor 1.0

        elif CR4_Cindy_S1 == 3:
            text "Caroline Walkthrough - Step 65" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Nightclub" pos (533, 105) xanchor 1.0

        elif CR4_guard == 3:
            text "Caroline Walkthrough - Step 66" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Nightclub" pos (533, 105) xanchor 1.0
            text "- Talk to the security guards" pos (34, 142)

        elif NC_Boss == 1 or NC_Boss == 2:
            text "Caroline Walkthrough - Step 67" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Nightclub" pos (533, 105) xanchor 1.0
            if NC_Boss == 1:
                text "- Talk to the Headmaster again tomorrow night" pos (34, 142)

        elif CR4_AS4:
            text "Caroline Walkthrough - Step 68" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Clothes shop" pos (533, 105) xanchor 1.0

        elif CR4_week_event:
            text "Caroline Walkthrough - Step 69" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Weekend" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            text "- Weekend event -> Caroline weekend event" pos (34, 142)

        elif Caroline_points >= 5:
            text "Caroline's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Caroline's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

default mod_sara_step_31_complete = False

screen mod_sara_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_sara_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_sara_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if sis_nerdy_scene1_v1 == 1:
            text "Sara Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif sis_nerdy_school_scene1_v1_talk == 1:
            text "Sara Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School entrance" pos (533, 105) xanchor 1.0

        elif sis_nerdy_night_sleeping1_v1 == 1:
            text "Sara Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif sis_nerdy_scene1_v1 == 2:
            text "Sara Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif drawer_sis_nerdy < 3:
            text "Sara Walkthrough - Step 5" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0
            if not can_sara_scene3_v1:
                text "- Enter Sara's room tomorrow morning" pos (34, 142)
                text "- Click the drawer under the tv" pos (34, 172)
            else:
                text "- Click the drawer under the tv" pos (34, 142)

        elif not can_gamepad_sara:
            text "Sara Walkthrough - Step 6" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif can_sis_nerdy_gamepad_change == 0:
            text "Sara Walkthrough - Step 7" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif not b3_controller_buy:
            text "Sara Walkthrough - Step 8" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Shop" pos (533, 105) xanchor 1.0
            text "- Buy the cheap controller ($5)" pos (34, 142)

        elif can_sis_nerdy_gamepad_change == 1:
            text "Sara Walkthrough - Step 9" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}{size=18}Morning/Noon/Night{/size}" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0
            text "- Open your inventory and click the controller" pos (34, 142)
            text "- Click her controller under her tv" pos (34, 172)

        elif sis_nerdy_evening_scene2a_v1 == 1:
            text "Sara Walkthrough - Step 10" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0
            text "- \"Sneak a peek\"" pos (34, 142)

        elif not b4_spy_camera_buy:
            text "Sara Walkthrough - Step 11" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Kitchen bathroom" pos (533, 105) xanchor 1.0
            text "- Buy the spy camera ($55)" pos (34, 142)
            text "- Optional: Use the spy cam on the bathroom door" pos (34, 172) size 21
            text "- (This step will disappear after buying the cam. Remember\n   to use the cam if you want to see the scene)" pos (34, 202) size 18

        elif sis_nerdy_school_scene2_v1 == 1:
            text "Sara Walkthrough - Step 12" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School entrance" pos (533, 105) xanchor 1.0

        elif mc_sara_night_scene1_v1 == 1:
            text "Sara Walkthrough - Step 13" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0

        elif Sara_points == 1:
            text "Sara Walkthrough - Step 14" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School entrance" pos (533, 105) xanchor 1.0

        elif not SR2_weekend_swimming_pool:
            text "Sara Walkthrough - Step 15" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0

        elif SR2_MS1:
            text "Sara Walkthrough - Step 16" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif SR2_AS1:
            text "Sara Walkthrough - Step 17" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0
            if not can_SR2_MS2:
                text "- Optional: Use the spy cam on the bathroom\n   door in the morning" pos (34, 142)
                text "- Talk to Sara tomorrow morning" pos (34, 202)

        elif can_SR2_AS2:
            text "Sara Walkthrough - Step 18" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0

        elif SR2_NS1:
            text "Sara Walkthrough - Step 19" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif can_SR2_AS3 and not SR2_vibrator in inventory.items:
            text "Sara Walkthrough - Step 20" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sex shop" pos (533, 105) xanchor 1.0

        elif can_SR2_AS3:
            text "Sara Walkthrough - Step 21" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0

        elif SR2_AS3:
            text "Sara Walkthrough - Step 22" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif not b5_web_cam_software_buy:
            text "Sara Walkthrough - Step 23" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Shop" pos (533, 105) xanchor 1.0
            text "- Buy the webcam software ($20)" pos (34, 142)

        elif can_SR2_AS4:
            text "Sara Walkthrough - Step 24" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0

        elif SR2_AS4:
            text "Sara Walkthrough - Step 25" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            if not live_camera_instaled:
                text "- Use your PC -> CD -> Install WebCam" pos (34, 142)
            else:
                text "- Use your computer and click Live Camera" pos (34, 142)

        elif can_SR2_AS5:
            text "Sara Walkthrough - Step 26" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0

        elif SR2_NS3:
            text "Sara Walkthrough - Step 27" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your driveway" pos (533, 105) xanchor 1.0

        elif not lube_buy:
            text "Sara Walkthrough - Step 28" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sex shop" pos (533, 105) xanchor 1.0
            text "- Buy the lube ($50)" pos (34, 142)

        elif can_SR2_AS6:
            text "Sara Walkthrough - Step 29" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0

        elif Sara_points == 2:
            text "Sara Walkthrough - Step 30" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif not mod_sara_step_31_complete:
            text "Sara Walkthrough - Step 31" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            if can_sms8_sara == 1:
                text "- Wait 2 days" pos (34, 142)
            elif can_sms8_sara == 2:
                text "- Wait 1 day" pos (34, 142)
            else:
                text "- Read Sara's text messages on your phone" pos (34, 142)
                textbutton "Click {b}here{/b} to advance to the next walkthrough step." pos (25, 202) text_style "modguide_text" text_size 20 text_hover_color "#66c1e0" action SetVariable("mod_sara_step_31_complete", True)

        elif not SR3_ES1_talked:
            text "Sara Walkthrough - Step 32" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0
            text "- Romance route: \"Of course, Sara!\"" pos (34, 142)
            text "- Non-romantic route: \"I'm already in a relationship...\"" pos (34, 174) size 20

        elif SR3_weekend_event and not (SR3_we_bath or SR3_we_SC_wait or SR3_we_SC_bus or SR3_we_IC_shop_salesman or SR3_we_IC_shop_table or SR3_home_end):
            text "Sara Walkthrough - Step 33" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Weekend" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            text "- Start Sara's weekend event" pos (34, 142)

        elif SR3_we_bath:
            text "Sara Walkthrough - Step 34" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Kitchen bathroom" pos (533, 105) xanchor 1.0

        elif SR3_we_SC_wait or SR3_we_SC_bus or SR3_we_IC_shop_salesman or SR3_we_IC_shop_table:
            text "Sara Walkthrough - Step 35" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Mall" pos (533, 105) xanchor 1.0
            if SR3_we_SC_bus:
                text "- Stairs -> Ice cream van" pos (34, 142)
            elif SR3_we_IC_shop_table:
                text "- Choose any dialogue options" pos (34, 142)

        elif SR3_home_end and SR3_home_end_bath == 0:
            text "Sara Walkthrough - Step 36" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif SR3_home_end_bath > 0:
            text "Sara Walkthrough - Step 37" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            if SR3_home_end_bath == 1:
                text "{font=mod/OSB.ttf}Location: {/font}Kitchen bathroom" pos (533, 105) xanchor 1.0
            elif SR3_home_end_bath == 2:
                text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0

        elif SR3_MS1:
            text "Sara Walkthrough - Step 38" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's room" pos (533, 105) xanchor 1.0


        elif SR3_v71_end:
            text "Sara's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Sara's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_celia_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_celia_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_celia_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if talking_celia_school_morning_scene1v1 == 1:
            text "Celia Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0

        elif celia_key not in inventory.items and celia_key_take:
            text "Celia Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0
            text "- Take the teacher's break room key from Celia's\ndesk" pos (34, 142)

        elif can_take_celianote:
            text "Celia Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Teachers' break room" pos (533, 105) xanchor 1.0
            text "- Select the key in your inventory and click on\nthe break room door" pos (34, 142)
            text "- Take the note from Celia's locker" pos (34, 202)

        elif can_celia_laptopv1:
            text "Celia Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Teachers' office" pos (533, 105) xanchor 1.0
            text "- Type the password {b}Ossa36{/b} into the computer" pos (34, 142)

        elif Judy_scene1_v1 == 1:
            text "Celia Walkthrough - Step 5" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Therapist's room" pos (533, 107) xanchor 1.0 size 21
            text "- \"Talk about Celia selling grades\"" pos (34, 142)

        elif can_envelope_from_Judy_v1 == 1:
            text "Celia Walkthrough - Step 6" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Therapist's room" pos (533, 105) xanchor 1.0
            text "- Take the envelope from the cupboard near the\ndoor" pos (34, 142)

        elif can_empty_envelope_school_lockerv1 == 1:
            text "Celia Walkthrough - Step 7" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your school locker" pos (533, 105) xanchor 1.0
            text "- Select the envelope in your inventory and click\nthe pens in your locker" pos (34, 142)

        elif envolpe_event:
            text "Celia Walkthrough - Step 8" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Teachers' break room" pos (533, 105) xanchor 1.0
            text "- Select the envelope in your inventory and put\nit inside Celia's locker" pos (34, 142)

        elif not b5_web_cam_software_buy:
            text "Celia Walkthrough - Step 9" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Shop" pos (533, 105) xanchor 1.0
            text "- Buy the webcam software ($20)" pos (34, 142)

        elif celia_webcam_introdution_v1 == 1:
            text "Celia Walkthrough - Step 10" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            if not live_camera_instaled:
                text "- Use your PC -> CD -> Install WebCam" pos (34, 142)
            else:
                text "- Use your computer and click Live Camera" pos (34, 142)

        elif not dildo_buy or not vibrator_buy or not sexy_cloth_buy:
            text "Celia Walkthrough - Step 11" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sex shop" pos (533, 105) xanchor 1.0
            text "- Buy the dildo ($25)" pos (34, 142)
            text "- Buy the vibrator ($40)" pos (34, 172)
            text "- Buy the sexy clothes ($70)" pos (34, 202)

        elif (webcam_dildo_scenes_unloacked_V1 == 0 or webcam_vibrator_scenes_unloacked_V1 == 0 or webcam_sexy_cloth_scenes_unloacked_V1 == 0) and Celia_points == 1:
            text "Celia Walkthrough - Step 12" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Any" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Teachers' break room" pos (533, 105) xanchor 1.0
            text "- Put the three sex shop items into Celia's locker" pos (34, 142)

        elif webcam_dildo_scenes_unloacked2_V1 == 0 and Celia_points == 1:
            text "Celia Walkthrough - Step 13" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- Talk to Celia on your PC" pos (34, 142)
            text "- \"Did you get my present?\"" pos (34, 172)

        elif unlock_celia_toilet_cabin_day_scene3_v1 == 3 and can_unlock_celia_toilet_cabin_day_scene3_v1 == 1:
            text "Celia Walkthrough - Step 14" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- Keep doing Celia's webcam scenes until you've\ndone them all" pos (34, 142)

        elif unlock_celia_toilet_cabin_day_scene3_v1 == 1 and can_unlock_celia_toilet_cabin_day_scene3_v1 == 1:
            text "Celia Walkthrough - Step 15" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School bathroom" pos (533, 105) xanchor 1.0

        elif unlock_celia_toilet_cabin_day_scene4_v1 == 0:
            text "Celia Walkthrough - Step 16" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- \"Orders\"" pos (34, 142)

        elif unlock_celia_toilet_cabin_day_scene4_v1 == 1 and Celia_points == 1:
            text "Celia Walkthrough - Step 17" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School bathroom" pos (533, 105) xanchor 1.0

        elif celia_school_morning_scene1bv1 == 1 and Celia_points == 1:
            text "Celia Walkthrough - Step 18" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Teachers' office" pos (533, 105) xanchor 1.0

        elif CeR2_AS1 == 1 and Celia_points == 2:
            text "Celia Walkthrough - Step 19" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- \"Orders -> Blowjob using gloryhole\"" pos (34, 142)

        elif CeR2_NS1 == 1 and Celia_points == 2:
            text "Celia Walkthrough - Step 20" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Celia's apartment" pos (533, 105) xanchor 1.0

        elif CeR2_MS1_day == 1 and Celia_points == 2:
            text "Celia Walkthrough - Step 21" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School entrance" pos (533, 105) xanchor 1.0
            text "- Talk to Celia at the school entrance" pos (34, 142)

        elif CeR2_moni == 1 and Celia_points == 2:
            text "Celia Walkthrough - Step 22" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School security room" pos (533, 105) xanchor 1.0

        elif CeR2_AS1 == 2:
            text "Celia Walkthrough - Step 23" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School bathroom" pos (533, 105) xanchor 1.0
            text "- Click on the glory hole" pos (34, 142)

        elif CeR2_NS1 == 2 or CeR2_NS1 == 3:
            text "Celia Walkthrough - Step 24" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Celia's apartment" pos (533, 105) xanchor 1.0
            if CeR2_NS1 == 2:
                text "- Go to Celia's apartment tomorrow night" pos (34, 142)

        elif CeR2_moni == 3:
            text "Celia Walkthrough - Step 25" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School security room" pos (533, 105) xanchor 1.0

        elif CeR2_moni == 4:
            text "Celia Walkthrough - Step 26" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School entrance" pos (533, 105) xanchor 1.0
            text "- Talk to Celia at the school entrance" pos (34, 142)

        elif CeR2_moni == 5:
            text "Celia Walkthrough - Step 27" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School security room" pos (533, 105) xanchor 1.0

        elif CeR2_moni == 6:
            text "Celia Walkthrough - Step 28" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School entrance" pos (533, 105) xanchor 1.0
            text "- Talk to Celia at the school entrance" pos (34, 142)

        elif CeR2_moni == 7 or CeR2_MS2 == 2:
            text "Celia Walkthrough - Step 29" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Teachers' office" pos (533, 105) xanchor 1.0
            if CeR2_moni == 7:
                text "- Go to the teachers' office tomorrow morning" pos (34, 142)

        elif CeR2_AS2 == 1:
            text "Celia Walkthrough - Step 30" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- \"Orders -> Pussy using gloryhole\"" pos (34, 142)

        elif CeR2_AS2 == 2:
            text "Celia Walkthrough - Step 31" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School bathroom" pos (533, 105) xanchor 1.0

        elif CeR2_NS2 != False:
            text "Celia Walkthrough - Step 32" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Celia's apartment" pos (533, 105) xanchor 1.0

        elif CeR2_ES2:
            text "Celia Walkthrough - Step 33" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0

        elif CeR2_MS3 == 1:
            text "Celia Walkthrough - Step 34" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Teachers' office" pos (533, 105) xanchor 1.0

        elif CeR2_MS3 == 2:
            text "Celia Walkthrough - Step 35" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School bathroom" pos (533, 105) xanchor 1.0

        elif CeR2_J_q == True:
            text "Linda Walkthrough - Step 36" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 19
            text "{font=mod/OSB.ttf}Location: {/font}Therapist's room" pos (533, 107) xanchor 1.0 size 19

        elif CeR2_NS3:
            text "Celia Walkthrough - Step 37" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Celia's apartment" pos (533, 105) xanchor 1.0

        elif CeR2_J_q == 3:
            text "Linda Walkthrough - Step 38" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 19
            text "{font=mod/OSB.ttf}Location: {/font}Therapist's room" pos (533, 107) xanchor 1.0 size 19

        elif CeR2_dildo_buy == 1 or CeR2_dildo_buy == 2:
            text "Celia Walkthrough - Step 39" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sex shop" pos (533, 105) xanchor 1.0

        elif CeR2_LS >= 1 and CeR2_LS <= 4:
            text "Celia Walkthrough - Step 40" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Weekend" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your bed" pos (533, 105) xanchor 1.0
            if CeR2_LS >= 1 and CeR2_LS <= 3:
                text "- Celia will text you after 2 days have passed" pos (34, 142)
                text "- After Celia texts you, do her weekend event" pos (34, 172)



        elif Celia_points >= 3:
            text "Celia's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Celia's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_lizaYazmin_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_lizaYazmin_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_lizaYazmin_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if ml_salon_morning_visit < 5:
            text "Liza & Yazmin Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "- Complete Step #11 of Linda's story" pos (34, 142)

        elif LiR1_MAS1:
            text "Liza & Yazmin Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 107) xanchor 1.0 size 21
            if aunt_house_unlocked:
                text "- Go to Liza's house and visit her pool" pos (34, 142)
            else:
                text "- Go to Liza's pool tomorrow" pos (34, 142)

        elif LiR1_MAS1a:
            text "Liza & Yazmin Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 107) xanchor 1.0 size 21

        elif LiR1_poll_minigame:
            text "Liza & Yazmin Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's pool" pos (533, 105) xanchor 1.0
            if not Li_clean_stuff in inventory.items:
                text "- Take the mop and broom from Liza's garage" pos (34, 142)
            else:
                text "- Click the mop and clean the pool for 3 days" pos (34, 142)

        elif LiR1_poll_event_end:
            text "Liza & Yazmin Walkthrough - Step 5" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 107) xanchor 1.0 size 21
            text "- Talk to Liza -> \"I finished cleaning the pool.\"" pos (34, 142)

        elif LiR1_MAS6_can1:
            text "Liza & Yazmin Walkthrough - Step 6" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's pool" pos (533, 105) xanchor 1.0
            if not LiR1_MAS6:
                text "- Talk to Liza at her pool tomorrow" pos (34, 142)

        elif (Li_MAS3_menu_visit < 2 or Li_MAS2_menu_visit < 2) or LiR1_MAS4 == False:
            text "Liza & Yazmin Walkthrough - Step 7" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 107) xanchor 1.0 size 21
            text "- Do all of Liza's and Yazmin's conversation\noptions then go to sleep" pos (34, 142)

        elif LiR1_MAS4 == True:
            text "Liza & Yazmin Walkthrough - Step 8" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 107) xanchor 1.0 size 21

        elif LiR1_NS1:
            text "Liza & Yazmin Walkthrough - Step 9" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 105) xanchor 1.0

        elif (LiR1_MAS5_can1 and LiR1_MAS5 == False) or LiR1_MAS5:
            text "Liza & Yazmin Walkthrough - Step 10" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's kitchen" pos (533, 105) xanchor 1.0

        elif LiR1_NS2_can1 and LiR1_NS2_can2:
            text "Liza & Yazmin Walkthrough - Step 11" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 105) xanchor 1.0

        elif MAS7_fridge == False:
            text "Liza & Yazmin Walkthrough - Step 12" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's pool" pos (533, 105) xanchor 1.0

        elif not Li_key1 in inventory.items:
            text "Liza & Yazmin Walkthrough - Step 13" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 107) xanchor 1.0 size 21
            text "- Go inside Yazmin's home office and take the\nkey on the left by the plant" pos (34, 142)

        elif MAS7_fridge == True:
            text "Liza & Yazmin Walkthrough - Step 14" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's kitchen" pos (533, 105) xanchor 1.0
            text "- Open the fridge and take the beer on the right" pos (34, 142)

        elif LiR1_MAS7:
            text "Liza & Yazmin Walkthrough - Step 15" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's pool" pos (533, 105) xanchor 1.0

        elif LiR1_NS4:
            text "Liza & Yazmin Walkthrough - Step 16" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 105) xanchor 1.0
            text "- Climb up the house" pos (34, 142)

        elif not LiR1_MAS8_talked:
            text "Liza & Yazmin Walkthrough - Step 17" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's pool" pos (533, 105) xanchor 1.0

        elif LiR1_MAS9:
            text "Liza & Yazmin Walkthrough - Step 18" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's bathroom" pos (533, 105) xanchor 1.0

        elif LiR1_NS5:
            text "Liza & Yazmin Walkthrough - Step 19" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Liza's house" pos (533, 105) xanchor 1.0

        elif Li_points >= 2:
            text "Liza & Yazmin Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Liza & Yazmin Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_zuriSuri_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_zuriSuri_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_zuriSuri_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if not Z_home_unlocked:
            text "Zuri & Suri Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "- Complete Step #28 of Linda's story" pos (34, 142)

        elif Zv2_ES1:
            text "Zuri & Suri Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Zuri's house" pos (533, 105) xanchor 1.0

        elif Zv2_MS2_companyname == 0 and type(Zv2_MS2_companyname) is type(0):
            text "Zuri & Suri Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Bob's workplace" pos (533, 107) xanchor 1.0 size 21
            text "- Talk to Zuri -> \"Talk about Zuri's proposition\"" pos (34, 142)
            text "- \"Yes, I'll help\"" pos (34, 172)

        elif not Bob_work_minigame:
            text "Zuri & Suri Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Bob's office" pos (533, 105) xanchor 1.0
            text "- \"Do you have any work for me?\"" pos (34, 142)

        elif Zv2_MS2_companyname_found == 0:
            text "Zuri & Suri Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Bob's office" pos (533, 105) xanchor 1.0
            text "- Sit in Bob's chair then read Bob's reports" pos (34, 142)

        elif Zv2_MS2_companyname == 1:
            text "Zuri & Suri Walkthrough - Step 5" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Bob's workplace" pos (533, 107) xanchor 1.0 size 21
            text "- Talk to Zuri -> \"Talk about company name\" -> \"Yes\"" pos (34, 144) size 20
            text "- Decide if you want to do the Truth or Lie route" pos (34, 172)

        elif Zv2_ES2:
            text "Zuri & Suri Walkthrough - Step 6" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Zuri's house" pos (533, 105) xanchor 1.0

        elif Zv2_MS2_companyname_found == 1 or bob_safenote in inventory.items:
            text "Zuri & Suri Walkthrough - Step 7" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Bob's office" pos (533, 105) xanchor 1.0
            text "1. Take the note inside the left sofa table" pos (34, 142)
            text "2. Take the items in Bob's safe under his desk" pos (34, 172)
            text "3. Select the note in your inventory and put it back in the\nleft sofa table" pos (34, 205) size 18

        elif Zv2_MS2_companyname == 2:
            text "Zuri & Suri Walkthrough - Step 8" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Bob's workplace" pos (533, 107) xanchor 1.0 size 21
            text "- Talk to Zuri -> \"Talk about company name\"" pos (34, 142)
            text "- If doing Truth route, always tell the truth" pos (34, 172)
            text "- If doing Lie route, always lie" pos (34, 202)

        elif Zv2_ES3:
            text "Zuri & Suri Walkthrough - Step 9" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Zuri's house" pos (533, 105) xanchor 1.0

        elif Zv2_MS2_companyname == 3:
            text "Zuri & Suri Walkthrough - Step 10" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Bob's workplace" pos (533, 107) xanchor 1.0 size 21
            text "- Talk to Zuri -> \"Talk about company name\"" pos (34, 142)

        elif Zv2_MS2_companyname_found == 2:
            text "Zuri & Suri Walkthrough - Step 11" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Bob's office" pos (533, 105) xanchor 1.0
            text "- \"Ask about company name\"" pos (34, 142)

        elif Zv2_MS2_companyname == 4:
            text "Zuri & Suri Walkthrough - Step 12" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Noon" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}Bob's workplace" pos (533, 107) xanchor 1.0 size 21
            text "- Talk to Zuri -> \"Talk about company name\"" pos (34, 142)

        elif Zv2_ES3a:
            text "Zuri & Suri Walkthrough - Step 13" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Zuri's house" pos (533, 105) xanchor 1.0

        elif Zv2_ES4_counter < 3:
            text "Zuri & Suri Walkthrough - Step 14" pos (27, 70) font "mod/OSB.ttf"
            text "- Let 3 days pass" pos (34, 142)
            text "- Days passed: [Zv2_ES4_counter]" pos (34, 172)

        elif Z_points < 2:
            text "Zuri & Suri Walkthrough - Step 15" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Zuri's house" pos (533, 105) xanchor 1.0

        elif Z_points >= 2:
            text "Zuri & Suri Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Zuri & Suri Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_sidraIsla_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_sidraIsla_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_sidraIsla_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if not b1_binoculars_buy:
            text "Neighbors Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning/Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Shop" pos (533, 105) xanchor 1.0
            text "- Buy the binoculars ($100)" pos (34, 142)

        elif Neighboor_spy_mc_room:
            text "Neighbors Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your room" pos (533, 105) xanchor 1.0
            text "- Select the binoculars in your inventory and\nclick your window" pos (34, 142)

        elif Ne_MS1 == 1:
            text "Neighbors Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Neighbor's home" pos (533, 105) xanchor 1.0

        elif Ne_MS1 == 2 or Ne_MS1 == 3:
            text "Neighbors Walkthrough - Step 4" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Neighbor's home" pos (533, 105) xanchor 1.0
            if Ne_MS1 == 2:
                text "- Talk to her again tomorrow morning" pos (34, 142)

        elif Ne_MS2 == 2:
            text "Neighbors Walkthrough - Step 5" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}School changing room" pos (533, 107) xanchor 1.0 size 21
            text "- Click the right parking lot outside of the school\nto travel to the school gym" pos (34, 142)

        elif Ne_MS1 == 5 or Ne_MS1 == 6:
            text "??? & Isla Walkthrough - Step 6" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Neighbor's home" pos (533, 105) xanchor 1.0
            if Ne_MS1 == 5:
                text "- Visit their house tomorrow morning" pos (34, 142)

        elif Ne_ES1:
            text "Sidra & Isla Walkthrough - Step 7" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Neighbor's home" pos (533, 105) xanchor 1.0
            text "- Climb the neighbor's fence" pos (34, 142)

        elif Ne_MS2 == 4:
            text "Sidra & Isla Walkthrough - Step 8" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}School changing room" pos (533, 107) xanchor 1.0 size 21
            text "- Optional: You can jump their fence at night to\ndo night scenes" pos (34, 142)

        elif Ne_ES2:
            text "Sidra & Isla Walkthrough - Step 9" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Evening" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Neighbor's home" pos (533, 105) xanchor 1.0

        elif Ne_MS2 == 5:
            text "Sidra & Isla Walkthrough - Step 10" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 107) size 21
            text "{font=mod/OSB.ttf}Location: {/font}School changing room" pos (533, 107) xanchor 1.0 size 21

        elif Ne_MS3:
            text "Sidra & Isla Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Sidra & Isla Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_cindy_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_cindy_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_cindy_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if not renpy.seen_label("headmaster_S2"):
            text "Cindy Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "- Complete Step #39 of Linda's story" pos (34, 142)

        elif CR4_Cindy_S1 == False or CR4_Cindy_S1 < 5:
            text "Cindy Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "- Complete Step #67 of Caroline's story" pos (34, 142)

        elif CR4_Cindy_S1 == 5:
            text "Cindy Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Night" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Nightclub sex room" pos (533, 105) xanchor 1.0
            text "- \"It's a deal!\" (requires $1,000)" pos (34, 142)

        elif CR4_Cindy_S1 >= 6:
            text "Cindy's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Cindy's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_delilah_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_delilah_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_delilah_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if not delilah_work_inprogress:
            text "Delilah Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}School pool" pos (533, 105) xanchor 1.0

        elif delilah_work_inprogress:
            text "Delilah's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Delilah's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_judy_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_judy_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_judy_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if MLR2_MS1_talk_count < 4:
            text "Judy Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "- Complete Step #24 of Linda's story" pos (34, 142)

        elif judy_q2:
            text "Judy Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Therapist's room" pos (533, 105) xanchor 1.0

        elif J_home_unlocked:
            text "Judy's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Judy's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_lily_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_lily_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_lily_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if lily_school_day_scene1_v1 == 1:
            text "Lily Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0

        elif Sara_points == 1:
            text "Lily Walkthrough - Step 2" pos (27, 70) font "mod/OSB.ttf"
            text "- Complete Step #14 of Sara's story" pos (34, 142)

        elif lily_school_day_scene2_v1 == 1:
            text "Lily Walkthrough - Step 3" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Afternoon" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Sara's classroom" pos (533, 105) xanchor 1.0
            text "- \"Bend down and pick up the pen\"" pos (34, 142)

        elif lily_work_in_progress_v1 == 1:
            text "Lily's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Lily's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_macy_story():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_macy_story"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 256)
            align (0.5, 0.5)
        add "mod/images/modguide.png"
        textbutton "X" action Hide("mod_macy_story") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if not macy_work_inprogress:
            text "Macy Walkthrough - Step 1" pos (27, 70) font "mod/OSB.ttf"
            text "{font=mod/OSB.ttf}Time: {/font}Morning" pos (27, 105)
            text "{font=mod/OSB.ttf}Location: {/font}Your classroom" pos (533, 105) xanchor 1.0

        elif macy_work_inprogress:
            text "Macy's Story - Max level reached!" pos (27, 70) font "mod/OSB.ttf"

        else:
            text "Macy's Walkthrough - Unknown step!" pos (27, 70) font "mod/OSB.ttf"

screen mod_linda_nightscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_linda_nightscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_linda_nightscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Linda - Night Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)
        text "{font=mod/OSB.ttf}Watched:{/font}" ypos 105 xalign 0.5
        text "{font=mod/OSB.ttf}Unlocked:{/font}" pos (533, 105) xanchor 1.0

        text "{font=mod/OSB.ttf}Your room:{/font}" pos (27, 142)
        text "Mouth" pos (27, 172)
        if ML_NS_mouth.played:
            text "Yes" ypos 172 xalign 0.5
        else:
            text "No" ypos 172 xalign 0.5
        if ML_NS_mouth in nsb_box.ml_nsb_s:
            text "Yes" pos (533, 172) xanchor 1.0
        else:
            text "No" pos (533, 172) xanchor 1.0

        text "Tits" pos (27, 202)
        if ML_NS_tits.played:
            text "Yes" ypos 202 xalign 0.5
        else:
            text "No" ypos 202 xalign 0.5
        if ml_points >= 2:
            text "Yes" pos (533, 202) xanchor 1.0
        else:
            text "No" pos (533, 202) xanchor 1.0

        text "Feet" pos (27, 232)
        if ML_NS_feet.played:
            text "Yes" ypos 232 xalign 0.5
        else:
            text "No" ypos 232 xalign 0.5
        if ML_NS_mouth in nsb_box.ml_nsb_s:
            text "Yes" pos (533, 232) xanchor 1.0
        else:
            text "No" pos (533, 232) xanchor 1.0

        text "{font=mod/OSB.ttf}Her room:{/font}" pos (27, 292)
        text "Handjob" pos (27, 322)
        if ML_NS_sleep_hand.played:
            text "Yes" ypos 322 xalign 0.5
        else:
            text "No" ypos 322 xalign 0.5
        if ml_points >= 3:
            text "Yes" pos (533, 322) xanchor 1.0
        else:
            text "No" pos (533, 322) xanchor 1.0

        text "Footjob" pos (27, 352)
        if ML_NS_sleep_foot_job.played:
            text "Yes" ypos 352 xalign 0.5
        else:
            text "No" ypos 352 xalign 0.5
        if ml_points >= 3:
            text "Yes" pos (533, 352) xanchor 1.0
        else:
            text "No" pos (533, 352) xanchor 1.0

        text "Her choice" pos (27, 382)
        if ML_NS_sleep_her.played:
            text "Yes" ypos 382 xalign 0.5
        else:
            text "No" ypos 382 xalign 0.5
        if ml_points >= 3:
            text "Yes" pos (533, 382) xanchor 1.0
        else:
            text "No" pos (533, 382) xanchor 1.0

screen mod_caroline_nightscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_caroline_nightscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_caroline_nightscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Caroline - Night Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)
        text "{font=mod/OSB.ttf}Watched:{/font}" ypos 105 xalign 0.5
        text "{font=mod/OSB.ttf}Unlocked:{/font}" pos (533, 105) xanchor 1.0

        text "Mouth" pos (27, 142)
        if C_NS_cock.played:
            text "Yes" ypos 142 xalign 0.5
        else:
            text "No" ypos 142 xalign 0.5
        if C_NS_cock in nsb_box.c_nsb_s:
            text "Yes" pos (533, 142) xanchor 1.0
        else:
            text "No" pos (533, 142) xanchor 1.0

        text "Tits" pos (27, 172)
        if C_NS_tits.played:
            text "Yes" ypos 172 xalign 0.5
        else:
            text "No" ypos 172 xalign 0.5
        if C_NS_cock in nsb_box.c_nsb_s:
            text "Yes" pos (533, 172) xanchor 1.0
        else:
            text "No" pos (533, 172) xanchor 1.0

        text "Ass" pos (27, 202)
        if C_NS_ass.played:
            text "Yes" ypos 202 xalign 0.5
        else:
            text "No" ypos 202 xalign 0.5
        if C_NS_cock in nsb_box.c_nsb_s:
            text "Yes" pos (533, 202) xanchor 1.0
        else:
            text "No" pos (533, 202) xanchor 1.0

        text "Feet" pos (27, 232)
        if C_NS_feet.played:
            text "Yes" ypos 232 xalign 0.5
        else:
            text "No" ypos 232 xalign 0.5
        if C_NS_cock in nsb_box.c_nsb_s:
            text "Yes" pos (533, 232) xanchor 1.0
        else:
            text "No" pos (533, 232) xanchor 1.0


        text "Handjob" pos (27, 262)
        if C_NS_wake_hand.played:
            text "Yes" ypos 262 xalign 0.5
        else:
            text "No" ypos 262 xalign 0.5
        if Caroline_points >= 2:
            text "Yes" pos (533, 262) xanchor 1.0
        else:
            text "No" pos (533, 262) xanchor 1.0

        text "Feet" pos (27, 292)
        if C_NS_wake_feet.played:
            text "Yes" ypos 292 xalign 0.5
        else:
            text "No" ypos 292 xalign 0.5
        if Caroline_points >= 2:
            text "Yes" pos (533, 292) xanchor 1.0
        else:
            text "No" pos (533, 292) xanchor 1.0

        text "Kissing" pos (27, 322)
        if C_NS_wake_kissing.played:
            text "Yes" ypos 322 xalign 0.5
        else:
            text "No" ypos 322 xalign 0.5
        if CR3_weekend_event == 3:
            text "Yes" pos (533, 322) xanchor 1.0
        else:
            text "No" pos (533, 322) xanchor 1.0

        text "Titjob" pos (27, 352)
        if C_NS_wake_titsjob.played:
            text "Yes" ypos 352 xalign 0.5
        else:
            text "No" ypos 352 xalign 0.5
        if CR3_weekend_event == 3:
            text "Yes" pos (533, 352) xanchor 1.0
        else:
            text "No" pos (533, 352) xanchor 1.0

        text "Buttjob" pos (27, 382)
        if C_NS_wake_butt.played:
            text "Yes" ypos 382 xalign 0.5
        else:
            text "No" ypos 382 xalign 0.5
        if CR3_weekend_event == 3:
            text "Yes" pos (533, 382) xanchor 1.0
        else:
            text "No" pos (533, 382) xanchor 1.0

        text "Licking" pos (27, 412)
        if C_NS_wake_licking.played:
            text "Yes" ypos 412 xalign 0.5
        else:
            text "No" ypos 412 xalign 0.5
        if (C_NS_wake_hand in nsb_box.c_nsb_wake) or can_add_C_NS_wake_licking_loc:
            text "Yes" pos (533, 412) xanchor 1.0
        else:
            text "No" pos (533, 412) xanchor 1.0

screen mod_sara_nightscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_sara_nightscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_sara_nightscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Sara - Night Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)
        text "{font=mod/OSB.ttf}Watched:{/font}" ypos 105 xalign 0.5
        text "{font=mod/OSB.ttf}Unlocked:{/font}" pos (533, 105) xanchor 1.0

        text "Mouth" pos (27, 142)
        if S_NS_mouth.played:
            text "Yes" ypos 142 xalign 0.5
        else:
            text "No" ypos 142 xalign 0.5
        text "Yes" pos (533, 142) xanchor 1.0

        text "Hand" pos (27, 202)
        if S_NS_hand.played:
            text "Yes" ypos 202 xalign 0.5
        else:
            text "No" ypos 202 xalign 0.5
        text "Yes" pos (533, 202) xanchor 1.0

        text "Pussy" pos (27, 262)
        if S_NS_pussy.played:
            text "Yes" ypos 262 xalign 0.5
        else:
            text "No" ypos 262 xalign 0.5
        text "Yes" pos (533, 262) xanchor 1.0

        text "Thighs" pos (27, 322)
        if S_NS_thigh.played:
            text "Yes" ypos 322 xalign 0.5
        else:
            text "No" ypos 322 xalign 0.5
        text "Yes" pos (533, 322) xanchor 1.0

        text "Thighjob" pos (27, 382)
        if S_NS_wake_thigh.played:
            text "Yes" ypos 382 xalign 0.5
        else:
            text "No" ypos 382 xalign 0.5
        if Sara_points >= 2:
            text "Yes" pos (533, 382) xanchor 1.0
        else:
            text "No" pos (533, 382) xanchor 1.0

screen mod_celia_nightscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_celia_nightscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_celia_nightscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Celia - Night Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)
        text "{font=mod/OSB.ttf}Watched:{/font}" ypos 105 xalign 0.5
        text "{font=mod/OSB.ttf}Unlocked:{/font}" pos (533, 105) xanchor 1.0

        text "Mouth" pos (27, 142)
        if Ce_NS_cock.played:
            text "Yes" ypos 142 xalign 0.5
        else:
            text "No" ypos 142 xalign 0.5
        if Ce_home_key in inventory.items:
            text "Yes" pos (533, 142) xanchor 1.0
        else:
            text "No" pos (533, 142) xanchor 1.0

        text "Kissing" pos (27, 202)
        if Ce_NS_kissing.played:
            text "Yes" ypos 202 xalign 0.5
        else:
            text "No" ypos 202 xalign 0.5
        if Ce_home_key in inventory.items:
            text "Yes" pos (533, 202) xanchor 1.0
        else:
            text "No" pos (533, 202) xanchor 1.0

        text "Tits" pos (27, 262)
        if Ce_NS_tits.played:
            text "Yes" ypos 262 xalign 0.5
        else:
            text "No" ypos 262 xalign 0.5
        if Ce_home_key in inventory.items:
            text "Yes" pos (533, 262) xanchor 1.0
        else:
            text "No" pos (533, 262) xanchor 1.0

        text "Pussy" pos (27, 322)
        if Ce_NS_pussy.played:
            text "Yes" ypos 322 xalign 0.5
        else:
            text "No" ypos 322 xalign 0.5
        if Ce_home_key in inventory.items:
            text "Yes" pos (533, 322) xanchor 1.0
        else:
            text "No" pos (533, 322) xanchor 1.0

        text "Footjob" pos (27, 382)
        if Ce_NS_feet.played:
            text "Yes" ypos 382 xalign 0.5
        else:
            text "No" ypos 382 xalign 0.5
        if Ce_home_key in inventory.items:
            text "Yes" pos (533, 382) xanchor 1.0
        else:
            text "No" pos (533, 382) xanchor 1.0

screen mod_lizaYazmin_nightscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_lizaYazmin_nightscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_lizaYazmin_nightscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Liza & Yazmin - Night Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)
        text "{font=mod/OSB.ttf}Watched:{/font}" ypos 105 xalign 0.5
        text "{font=mod/OSB.ttf}Unlocked:{/font}" pos (533, 105) xanchor 1.0

        text "Liza:" pos (27, 142) font "mod/OSB.ttf"
        text "Mouth" pos (27, 172)
        if Li_NS_mouth.played:
            text "Yes" ypos 172 xalign 0.5
        else:
            text "No" ypos 172 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 172) xanchor 1.0
        else:
            text "No" pos (533, 172) xanchor 1.0

        text "Pussy" pos (27, 202)
        if Li_NS_pussy.played:
            text "Yes" ypos 202 xalign 0.5
        else:
            text "No" ypos 202 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 202) xanchor 1.0
        else:
            text "No" pos (533, 202) xanchor 1.0

        text "Feet" pos (27, 232)
        if Li_NS_feet.played:
            text "Yes" ypos 232 xalign 0.5
        else:
            text "No" ypos 232 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 232) xanchor 1.0
        else:
            text "No" pos (533, 232) xanchor 1.0

        text "Yazmin:" pos (27, 262) font "mod/OSB.ttf"
        text "Mouth" pos (27, 292)
        if Yaz_NS_mouth.played:
            text "Yes" ypos 292 xalign 0.5
        else:
            text "No" ypos 292 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 292) xanchor 1.0
        else:
            text "No" pos (533, 292) xanchor 1.0

        text "Ass" pos (27, 322)
        if Yaz_NS_ass.played:
            text "Yes" ypos 322 xalign 0.5
        else:
            text "No" ypos 322 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 322) xanchor 1.0
        else:
            text "No" pos (533, 322) xanchor 1.0

        text "Feet" pos (27, 352)
        if Yaz_NS_feet.played:
            text "Yes" ypos 352 xalign 0.5
        else:
            text "No" ypos 352 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 352) xanchor 1.0
        else:
            text "No" pos (533, 352) xanchor 1.0


        text "Tits" pos (27, 382)
        if Yaz_NS_Turn_tits.played:
            text "Yes" ypos 382 xalign 0.5
        else:
            text "No" ypos 382 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 382) xanchor 1.0
        else:
            text "No" pos (533, 382) xanchor 1.0

        text "Bush" pos (27, 412)
        if Yaz_NS_Turn_bush.played:
            text "Yes" ypos 412 xalign 0.5
        else:
            text "No" ypos 412 xalign 0.5
        if Li_key1 in inventory.items:
            text "Yes" pos (533, 412) xanchor 1.0
        else:
            text "No" pos (533, 412) xanchor 1.0

screen mod_sidraIsla_nightscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_sidraIsla_nightscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_sidraIsla_nightscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        if Ne_fence:
            text "Sidra & Isla - Night Scenes" pos (27, 70) font "mod/OSB.ttf"
        else:
            text "Neighbors - Night Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)
        text "{font=mod/OSB.ttf}Watched:{/font}" ypos 105 xalign 0.5
        text "{font=mod/OSB.ttf}Unlocked:{/font}" pos (533, 105) xanchor 1.0

        if Ne_fence:
            text "Sidra:" pos (27, 142) font "mod/OSB.ttf"
        else:
            text "???:" pos (27, 142) font "mod/OSB.ttf"
        text "Tits" pos (27, 172)
        if Sidra_NS_tits.played:
            text "Yes" ypos 172 xalign 0.5
        else:
            text "No" ypos 172 xalign 0.5
        if Ne_fence:
            text "Yes" pos (533, 172) xanchor 1.0
        else:
            text "No" pos (533, 172) xanchor 1.0

        if Ne_fence:
            text "Isla:" pos (27, 232) font "mod/OSB.ttf"
        else:
            text "???:" pos (27, 232) font "mod/OSB.ttf"
        text "Kissing" pos (27, 262)
        if Isla_NS_kissing.played:
            text "Yes" ypos 262 xalign 0.5
        else:
            text "No" ypos 262 xalign 0.5
        if Ne_fence:
            text "Yes" pos (533, 262) xanchor 1.0
        else:
            text "No" pos (533, 262) xanchor 1.0

        text "Tits" pos (27, 292)
        if Isla_NS_tits.played:
            text "Yes" ypos 292 xalign 0.5
        else:
            text "No" ypos 292 xalign 0.5
        if Ne_fence:
            text "Yes" pos (533, 292) xanchor 1.0
        else:
            text "No" pos (533, 292) xanchor 1.0

        text "Pussy" pos (27, 322)
        if Isla_NS_pussy.played:
            text "Yes" ypos 322 xalign 0.5
        else:
            text "No" ypos 322 xalign 0.5
        if Ne_fence:
            text "Yes" pos (533, 322) xanchor 1.0
        else:
            text "No" pos (533, 322) xanchor 1.0

screen mod_bathdreamscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_bathdreamscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_bathdreamscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Bath Dream Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)
        text "{font=mod/OSB.ttf}Watched:{/font}" ypos 105 xalign 0.5

        text "Linda" pos (27, 142)
        if renpy.seen_image("bath_event_pLinda"):
            text "Yes" ypos 142 xalign 0.5
        else:
            text "No" ypos 142 xalign 0.5

        text "Sara" pos (27, 172)
        if renpy.seen_image("bath_event_pSara"):
            text "Yes" ypos 172 xalign 0.5
        else:
            text "No" ypos 172 xalign 0.5

        text "Caroline" pos (27, 202)
        if renpy.seen_image("bath_event_pCaroline"):
            text "Yes" ypos 202 xalign 0.5
        else:
            text "No" ypos 202 xalign 0.5

        text "Judy" pos (27, 232)
        if renpy.seen_image("bath_event_pJudy"):
            text "Yes" ypos 232 xalign 0.5
        else:
            text "No" ypos 232 xalign 0.5

        text "Celia" pos (27, 262)
        if renpy.seen_image("bath_event_pCelia"):
            text "Yes" ypos 262 xalign 0.5
        else:
            text "No" ypos 262 xalign 0.5

        text "Liza" pos (27, 292)
        if renpy.seen_image("bath_event_pAu"):
            text "Yes" ypos 292 xalign 0.5
        else:
            text "No" ypos 292 xalign 0.5

        text "Violet" pos (27, 322)
        if renpy.seen_image("bath_event_pViolet"):
            text "Yes" ypos 322 xalign 0.5
        else:
            text "No" ypos 322 xalign 0.5

        text "Lily" pos (27, 352)
        if renpy.seen_image("bath_event_pLily"):
            text "Yes" ypos 352 xalign 0.5
        else:
            text "No" ypos 352 xalign 0.5

        text "Zuri & Suri" pos (27, 382)
        if renpy.seen_image("bath_event_pZuri"):
            text "Yes" ypos 382 xalign 0.5
        else:
            text "No" ypos 382 xalign 0.5

screen mod_replayspycamscenes():
    tag guide
    zorder 998
    style_prefix "modguide"
    drag:
        drag_name "mod_replayspycamscenes"
        align (1.0, 1.0)
        drag_handle (0, 0, 1.0, 68)

        has fixed:
            xysize (560, 466)
            align (0.5, 0.5)
        add "mod/images/modguide_sleep.png"
        textbutton "X" action Hide("mod_replayspycamscenes") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6

        text "Scene Replay - Spy Cam Scenes" pos (27, 70) font "mod/OSB.ttf"
        text "{font=mod/OSB.ttf}Scene:{/font}" pos (27, 105)

        text "Linda - #1" pos (27, 142)
        textbutton "Replay scene" pos (533, 142) xanchor 1.0 text_style "modguide_text" text_hover_color "#66c1e0" action Replay("modreplay_bath_Linda1", locked=False)

        text "Linda - #2" pos (27, 172)
        textbutton "Replay scene" pos (533, 172) xanchor 1.0 text_style "modguide_text" text_hover_color "#66c1e0" action Replay("modreplay_bath_Linda2", locked=False)

        text "Sara - #1" pos (27, 232)
        textbutton "Replay scene" pos (533, 232) xanchor 1.0 text_style "modguide_text" text_hover_color "#66c1e0" action Replay("modreplay_bath_Sara1", locked=False)

        text "Sara - #2" pos (27, 262)
        textbutton "Replay scene" pos (533, 262) xanchor 1.0 text_style "modguide_text" text_hover_color "#66c1e0" action Replay("modreplay_bath_Sara2", locked=False)

        text "Sara - #3" pos (27, 292)
        textbutton "Replay scene" pos (533, 292) xanchor 1.0 text_style "modguide_text" text_hover_color "#66c1e0" action Replay("modreplay_bath_Sara3", locked=False)

        text "Sara - #4" pos (27, 322)
        textbutton "Replay scene" pos (533, 322) xanchor 1.0 text_style "modguide_text" text_hover_color "#66c1e0" action Replay("modreplay_bath_Sara4", locked=False)

        text "Sara - #5" pos (27, 352)
        textbutton "Replay scene" pos (533, 352) xanchor 1.0 text_style "modguide_text" text_hover_color "#66c1e0" action Replay("modreplay_bath_Sara5", locked=False)

