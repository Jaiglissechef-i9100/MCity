image MLR3_beach_cliff_p1 = "images/Beach/MLR3_beach_event/Cliff/1.jpg"
image MLR3_beach_cliff_p2 = "images/Beach/MLR3_beach_event/Cliff/2.jpg"
image MLR3_beach_cliff_p3 = "images/Beach/MLR3_beach_event/Cliff/3.jpg"
image MLR3_beach_cliff_p4 = "images/Beach/MLR3_beach_event/Cliff/4.jpg"
image MLR3_beach_cliff_p5 = "images/Beach/MLR3_beach_event/Cliff/5.jpg"
image MLR3_beach_cliff_p6 = "images/Beach/MLR3_beach_event/Cliff/6.jpg"
image MLR3_beach_cliff_p7 = "images/Beach/MLR3_beach_event/Cliff/7.jpg"
image MLR3_beach_cliff_p8 = "images/Beach/MLR3_beach_event/Cliff/8.jpg"
image MLR3_beach_cliff_p9 = "images/Beach/MLR3_beach_event/Cliff/9.jpg"
image MLR3_beach_cliff_p10 = "images/Beach/MLR3_beach_event/Cliff/10.jpg"
image MLR3_beach_cliff_p11 = "images/Beach/MLR3_beach_event/Cliff/11.jpg"
image MLR3_beach_cliff_p12 = "images/Beach/MLR3_beach_event/Cliff/12.jpg"
image MLR3_beach_cliff_p13 = "images/Beach/MLR3_beach_event/Cliff/13.jpg"
image MLR3_beach_cliff_p14 = "images/Beach/MLR3_beach_event/Cliff/14.jpg"
image MLR3_beach_cliff_p15 = "images/Beach/MLR3_beach_event/Cliff/15.jpg"
image MLR3_beach_cliff_p16 = "images/Beach/MLR3_beach_event/Cliff/16.jpg"
image MLR3_beach_cliff_p17 = "images/Beach/MLR3_beach_event/Cliff/17.jpg"
image MLR3_beach_cliff_p18 = "images/Beach/MLR3_beach_event/Cliff/18.jpg"
image MLR3_beach_cliff_p19 = "images/Beach/MLR3_beach_event/Cliff/19.jpg"
image MLR3_beach_cliff_p20 = "images/Beach/MLR3_beach_event/Cliff/20.jpg"
image MLR3_beach_cliff_p21 = "images/Beach/MLR3_beach_event/Cliff/21.jpg"
image MLR3_beach_cliff_p22 = "images/Beach/MLR3_beach_event/Cliff/22.jpg"
image MLR3_beach_cliff_p23 = "images/Beach/MLR3_beach_event/Cliff/23.jpg"
image MLR3_beach_cliff_p24 = "images/Beach/MLR3_beach_event/Cliff/24.jpg"

label MLR3_beach_cliff:
    scene beach_up2_M_map
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)

    $ can_hide_windows = True

    scene MLR3_beach_cliff_p1 with dissolve

    Mom "Have you ever been cliff jumping before?"
    MC "Cliff jumping?!"
    MC "Please tell me that isn’t what it sounds like."

    scene MLR3_beach_cliff_p2

    Mom "What else could it possibly be? You jump off a cliff into the ocean! It’s amazing!"
    MC "Err… it it not really dangerous?"
    MC "I mean, there’s gotta be rocks and stuff in the water?"

    scene MLR3_beach_cliff_p3

    Mom "Some places can be dangerous, but these cliffs are very safe. The water’s deep and there’s no rocks to worry about."
    MC "Hmm, as long as you’re sure. Sorry, I’m not great with heights."

    scene MLR3_beach_cliff_p4

    Mom "C’mon, take my hand and we’ll go up there together."
    MC "Okay, sure."

    scene MLR3_beach_cliff_p5

    MC "(I guess I’m just gonna have to trust her. She’s done this before.)"
    Mom "This way!"

    scene MLR3_beach_cliff_p6

    Mom "Wow! Just look at the view… it takes my breath away every time I come up here."
    MC "Do you come here often?"
    Mom "Every chance I get. I like to get away here, by myself, some days."

    scene MLR3_beach_cliff_p7

    MC "(Yikes… that’s quite the drop.)"
    MC "H-How high is this cliff, [Mom_name]?"
    Mom "Sixty, maybe seventy feet?"

    scene MLR3_beach_cliff_p8

    MC "(Damn, I’ve got butterflies in my stomach now…)"
    Mom "The trick is to not spend too long looking down. You’ll only freak yourself out."
    MC "Y-Yeah…"

    scene MLR3_beach_cliff_p9

    Mom "You don’t really want to do this, do you?"
    MC "Honestly? Given how high it is, not really…"
    Mom "That’s okay. The first time is always the scariest. Once you get over your initial fears, it becomes much easier."

    scene MLR3_beach_cliff_p10

    Mom "Think about how scary it was, the first time you ever had to ride a bike, or do an exam."
    Mom "What we fear the most is the unknown, and you don’t know how it’s going to feel, jumping off a cliff."
    Mom "Once you’ve done it, you’ll feel much more confident about it."

    scene MLR3_beach_cliff_p11

    Mom "I’ll go first, to prove everything is safe. You can come, after me, if you want to."
    MC "O-Okay…"
    MC "(Now I do not have, really any other choice, but to follow her.)"

    scene MLR3_beach_cliff_p12

    Mom "Ahhha-ha-ha!"
    MC "Ahhh!"

    scene MLR3_beach_cliff_p13

    Mom "Haha! Woohoo!"
    MC "SHIIIITTT! AHHHHH!!!!"
    MC "(THIS WAS A TERRIBLE IDEA!)"

    scene MLR3_beach_cliff_p14

    Mom "Woooo!!!"
    MC "AHHHH!!!"
    "*SPLASH*"

    scene MLR3_beach_cliff_p15
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)


    Mom "Well? How was your first time cliff-diving? Ready for round two?"
    MC "N-No! It was horrifying!"
    Mom "Oh, you’ll get used to it!"

    scene MLR3_beach_cliff_p16

    Mom "I’ve never heard ANYONE scream that loud before - I didn’t know you had acrophobia."
    MC "I don’t - it’s just… no sane person should go jumping off cliffs! Haha!"

    scene MLR3_beach_cliff_p17

    Mom "Thank you for coming out with me today. I’d been looking forward to this for a long, long time."
    MC "You don’t need to thank me, [Mom_name]. I’ve wanted to come out with you."

    scene MLR3_beach_cliff_p18

    Mom "You really have made so many of my dreams come true. I’m such a lucky woman."
    MC "You’ve made a few of my dreams come true too. I’ll admit, I never knew I had such fantasies, before you started making your advances on me."
    MC "I’m glad you did though."

    scene MLR3_beach_cliff_p19

    Mom "Can you hold me for a while here?"
    MC "Sure, [Mom_name]."
    MC "(The water is so warm, with the sun beating down on it.)"

    scene MLR3_beach_cliff_p20

    Mom "God, you’re handsome. I love your eyes."
    MC "Your eyes are beautiful too, [Mom_name]. Their blue puts the ocean to shame."
    Mom "Mmm, that was rather poetic."

    scene MLR3_beach_cliff_p21

    MC "Heh, thank you."
    Mom "Even the weather turned out to be perfect. I couldn’t have asked for this to be any better."

    scene MLR3_beach_cliff_p22

    MC "Mmm…"
    Mom "Mmm…"
    Mom "(I wonder if any of those people on the beach can see us. What are they thinking right now?)"

    scene MLR3_beach_cliff_p23

    if renpy.loadable("patch.rpy"):
        Mom "(Could they see the resemblance between [player_name] and I?)"
        Mom "(Could any of them work out that I’m actually his mother? Or would they just think I’m a cougar dating a teenager?)"
    else:
        Mom "(Could they see the age difference between [player_name] and I?)"
        Mom "(Would any of them think that I could actually be his mother? Or would they just think I’m a cougar dating a teenager?)"

    Mom "(Then again, it would be pretty hot if they suspected me of being his mom.) "
    MC "What’s on your mind, [Mom_name]?"

    scene MLR3_beach_cliff_p24

    Mom "Hmm? Oh, nothing at all. Just enjoying being here with you."
    MC "Okay, shall we swim back to shore now?"
    Mom "Yeah, let’s get back before the sun sets."

    $ MLR3_beach_cliff = False
    $ MLR3_beach_done += 1
    $ can_hide_windows = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump beach2_M1