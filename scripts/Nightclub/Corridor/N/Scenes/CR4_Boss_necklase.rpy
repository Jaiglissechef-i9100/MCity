image CR4_Boss_necklace_p1 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/1.jpg"
image CR4_Boss_necklace_p2 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/2.jpg"
image CR4_Boss_necklace_p3 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/3.jpg"
image CR4_Boss_necklace_p4 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/4.jpg"
image CR4_Boss_necklace_p5 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/5.jpg"
image CR4_Boss_necklace_p6 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/6.jpg"
image CR4_Boss_necklace_p7 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/7.jpg"
image CR4_Boss_necklace_p8 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/8.jpg"
image CR4_Boss_necklace_p9 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/9.jpg"
image CR4_Boss_necklace_p10 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/10.jpg"
image CR4_Boss_necklace_p11 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/11.jpg"

image CR4_Boss_necklace_p13 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/13.jpg"
image CR4_Boss_necklace_p14 = "images/Nightclub/Corridor/N/Scenes/Security2/Next_Day/14.jpg"

default Ch_last_scene = False
label CR4_Boss_necklace:
    if NC_Boss != 2:
        jump boss_office_N
    if NC_Boss == 1:
        jump boss_office_N
    if NC_Boss == 2:
        $ can_hide_windows = True
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Danger Storm.mp3', channel="music2", loop=True, fadein = 2)

        scene CR4_Boss_necklace_p1 with dissolve
        MC "Hi sir, you told me to come back today."
        MC "Have you had a chance to look through the security footage yet?"

        scene CR4_Boss_necklace_p2
        Headmaster "Yes, hello again."
        Headmaster "Please, step over to my desk. I have indeed reviewed the cameras."
        MC "And? Did you see him?"

        scene CR4_Boss_necklace_p3
        Headmaster "I did. Can you tell me something?"
        MC "Yeah?"
        Headmaster "Was he drunk? Or is this Charles fellow always such a cunt?"

        scene CR4_Boss_necklace_p4
        MC "I think he’s just a cunt, sir."
        MC "The girl that he stole it from, her name was Caroline. "
        Headmaster "Mmm hmm."

        scene CR4_Boss_necklace_p5
        MC "They used to date. From what I understand he would beat her fairly regularly."
        Headmaster "Absolute scum."
        Headmaster "Forget about Charles. I’ll take care of that rabid dog."

        scene CR4_Boss_necklace_p6
        MC "Thank you, sir."
        Headmaster "And I have something for you as well..."
        Headmaster "Where did I put it? Aha! There it is."

        scene CR4_Boss_necklace_p7
        MC "Is that it?!"
        Headmaster "I added the box myself. I figured, returning such a priceless necklace deserves a fitting wrapping."
        MC "That’s very kind of you, sir. How much do I owe you?"

        scene CR4_Boss_necklace_p8
        Headmaster "You owe me nothing."
        Headmaster "But someday in the future, a young man will come to you. He will need your help with something. It might be next week. It might be in ten years."
        Headmaster "When that day comes, you’ll pass it on."

        scene CR4_Boss_necklace_p9
        MC "I can’t thank you enough. Caroline is going to be so happy with this."
        Headmaster "Well, I shan’t keep you any longer. Take it to her. I can tell you really care about this girl. Go and make her week!"

        scene CR4_Boss_necklace_p10
        MC "I will, sir."
        MC "(I can’t believe I actually did it! I can’t tell Caroline any of the details about how this happened… She’d kill me if she knew I risked my life with an organised crime gang…)"

        scene CR4_Boss_necklace_p11
        Headmaster "I hope to see you at school this week. I don’t want you flunking your education because you’re sleuthing around nightclubs."
        MC "I’ll be at school, don’t worry, sir! And I won’t breathe a word about who you really are."
        Headmaster "Good kid."

        scene CR4_Boss_necklace_p10
        MC "Oh wait - one more thing!"
        Headmaster "Hmm?"
        MC "Can I grab the key to Cindy’s room?"
        Headmaster "Why on Earth would you want that?"
        MC "I wouldn’t have gotten this necklace back without her help. I just wanted to talk to her."

        scene CR4_Boss_necklace_p13
        Headmaster "I have a few spare keys for that room. You can hold onto this one."
        MC "Thank you, I appreciate that."

        scene CR4_Boss_necklace_p14
        Headmaster "She’s in there until she clears her debt. I don’t expect her to be too happy about that."
        Headmaster "Just be careful. She doesn’t bite, but she can scratch."
        MC "I’ll keep that in mind, sir. "
        $ CR4_ES1_q5 = 3
        $ NC_Boss = 3
        $ CR4_Cindy_S1 = 5
        $ CR4_AS4 = True
        $ Ch_last_scene = True
        $ inventory.add(sexroom_key)
        $ inventory.add(C_necklace)
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Disco_Medusae.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False

        jump nc_corridor_N

label CR4_Boss_next_day:
    hide screen map_button
    show screen boss_office_N_scr
    $ clickable = False
    MC "I should come back tomorrow."
    $ clickable = True
    hide screen boss_office_N_scr
    jump boss_office_N