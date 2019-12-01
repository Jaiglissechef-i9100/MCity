image MLR3_b_house_bag_p1 = "images/Beach/MLR3_beach_event/House/Leave bag/1.jpg"
image MLR3_b_house_bag_p2 = "images/Beach/MLR3_beach_event/House/Leave bag/2.jpg"

image MLR3_beach_house_p7 = "images/Beach/MLR3_beach_event/House/7.jpg"
image MLR3_beach_house_p8 = "images/Beach/MLR3_beach_event/House/8.jpg"
image MLR3_beach_house_p9 = "images/Beach/MLR3_beach_event/House/9.jpg"
image MLR3_beach_house_p10 = "images/Beach/MLR3_beach_event/House/10.jpg"
image MLR3_beach_house_p11 = "images/Beach/MLR3_beach_event/House/11.jpg"
image MLR3_beach_house_p12 = "images/Beach/MLR3_beach_event/House/12.jpg"
image MLR3_beach_house_p13 = "images/Beach/MLR3_beach_event/House/13.jpg"
image MLR3_beach_house_p14 = "images/Beach/MLR3_beach_event/House/14.jpg"
image MLR3_beach_house_p15 = "images/Beach/MLR3_beach_event/House/15.jpg"
image MLR3_beach_house_p16 = "images/Beach/MLR3_beach_event/House/16.jpg"
image MLR3_beach_house_p17 = "images/Beach/MLR3_beach_event/House/17.jpg"
image MLR3_beach_house_p18 = "images/Beach/MLR3_beach_event/House/18.jpg"
image MLR3_beach_house_p19 = "images/Beach/MLR3_beach_event/House/19.jpg"
image MLR3_beach_house_p20 = "images/Beach/MLR3_beach_event/House/20.jpg"
image MLR3_beach_house_p21 = "images/Beach/MLR3_beach_event/House/21.jpg"
image MLR3_beach_house_p22 = "images/Beach/MLR3_beach_event/House/22.jpg"
image MLR3_beach_house_p23 = "images/Beach/MLR3_beach_event/House/23.jpg"
image MLR3_beach_house_p24 = "images/Beach/MLR3_beach_event/House/24.jpg"
image MLR3_beach_house_p25 = "images/Beach/MLR3_beach_event/House/25.jpg"
image MLR3_beach_house_p26 = "images/Beach/MLR3_beach_event/House/26.jpg"
image MLR3_beach_house_p27 = "images/Beach/MLR3_beach_event/House/27.jpg"
image MLR3_beach_house_p28 = "images/Beach/MLR3_beach_event/House/28.jpg"
image MLR3_beach_house_p29 = "images/Beach/MLR3_beach_event/House/29.jpg"
image MLR3_beach_house_p30 = "images/Beach/MLR3_beach_event/House/30.jpg"
image MLR3_beach_house_p31 = "images/Beach/MLR3_beach_event/House/31.jpg"
image MLR3_beach_house_p32 = "images/Beach/MLR3_beach_event/House/32.jpg"
image MLR3_beach_house_p33 = "images/Beach/MLR3_beach_event/House/33.jpg"
image MLR3_beach_house_p34 = "images/Beach/MLR3_beach_event/House/34.jpg"
image MLR3_beach_house_p35 = "images/Beach/MLR3_beach_event/House/35.jpg"
image MLR3_beach_house_p36 = "images/Beach/MLR3_beach_event/House/36.jpg"
image MLR3_beach_house_p37 = "images/Beach/MLR3_beach_event/House/37.jpg"
image MLR3_beach_house_p38 = "images/Beach/MLR3_beach_event/House/38.jpg"
image MLR3_beach_house_p39 = "images/Beach/MLR3_beach_event/House/39.jpg"
image MLR3_beach_house_p40 = "images/Beach/MLR3_beach_event/House/40.jpg"
image MLR3_beach_house_p41a = "images/Beach/MLR3_beach_event/House/41a.jpg"
image MLR3_beach_house_p42a = "images/Beach/MLR3_beach_event/House/42a.jpg"
image MLR3_beach_house_p42b = "images/Beach/MLR3_beach_event/House/42b.jpg"
image MLR3_beach_house_p42c = "images/Beach/MLR3_beach_event/House/42c.jpg"
image MLR3_beach_house_p42d = "images/Beach/MLR3_beach_event/House/42d.jpg"
image MLR3_beach_house_p43 = "images/Beach/MLR3_beach_event/House/43.jpg"
label MLR3_b_house_bag:
    scene b_house_bedroom_N_map

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True

    scene MLR3_b_house_bag_p1 with dissolve

    MC "(Okay, this looks like the bedroom. I guess I’ll just leave the bag sitting in here somewhere.)"
    MC "(Hmm, over by that chair looks good.)"

    scene MLR3_b_house_bag_p2

    MC "(There we go. That’ll sit nicely there.)"

    MC "Okay, that’s me done, [Mom_name]!"
    Mom "Great! C’mon back into the lounge, Sweetie!"
    $ can_hide_windows = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump b_house_bedroom_M1

label MLR3_b_house_bag2:
    scene b_house_bedroom_N_map
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene MLR3_beach_house_p7 with dissolve

    MC "Where are you, [Mom_name]?"
    Mom "Here, in the lounge!"
    MC "Yeah, I know that - but which room is the lounge?!"

    scene MLR3_beach_house_p8

    MC "Oh… I guess this must be it."
    MC "(That’s quite a nice selection of wine! I wonder if the landlord left this for us.)"
    Mom "I’ll just be a minute. Come on in and take a seat."

    scene MLR3_beach_house_p9

    MC "Sure, no problem."
    MC "(Fresh fruit too? This couldn’t have been left by the landlord.)"
    MC "([Mom_name] must have prepared it when I was putting the luggage away in her room.)"

    scene MLR3_beach_house_p10

    Mom "Well? What do you think?"
    MC "Did you make all this?"
    Mom "Hehe… I snuck the wine with me in the car and prepared the fruit while you were in the bedroom."

    scene MLR3_beach_house_p11

    Mom "The night is still young, so I wanted you and me to enjoy it together… with a proper romantic date."
    Mom "We’ll sit back, cuddle, nibble on some fresh fruit, and maybe get a little tipsy."
    MC "That sounds great, [Mom_name]! Thanks for planning this."
    Mom "Help yourself to a glass, and join me."

    scene MLR3_beach_house_p12

    Mom "So, what do you think of the wine? I’ve never noticed you drinking much before."
    MC "It’s alright, I guess. I’m not very used to it."
    Mom "Yeah, it can take a couple of years to develop an appreciation for a good wine. If you want some pointers, try to use all your senses when drinking it."

    scene MLR3_beach_house_p13

    Mom "Focus on the smell and the visuals - as well as the taste."
    MC "*Sniff*"
    MC "I think I see what you mean."
    Mom "Don’t worry if you don’t get it yet - it’s a skill that comes with age."

    scene MLR3_beach_house_p14

    Mom "Speaking of skills: have you ever thought about what job you’d like to do after you graduate?"
    MC "Hmm… I haven’t actually."
    Mom "You should probably put some thought into that. It’ll come around much quicker than you think."

    scene MLR3_beach_house_p15

    Mom "It’s hard to describe, but time is a lot like a car sitting at the top of a hill with the handbrake left off."
    MC "What do you mean?"
    Mom "One day, that car will start to move. It’ll begin rolling its way down the hill. At the start, it’ll be slow and steady. Yet, with each passing minute it’ll become faster and faster."
    MC "I’m not following you, [Mom_name]."
    Mom "A person’s perception of time grows faster as they grow older. Each year goes quicker than the last."

    scene MLR3_beach_house_p16

    MC "(I’m sure [Mom_name] is building up to quite a heavy point here. I’m not entirely sure what it is yet though.)"
    MC "*Sip*"
    MC "(Hmm, it’s not that bad actually.)"

    scene MLR3_beach_house_p17

    Mom "Listen… What I’m trying to say is… Well, I’m trying to say a couple of things actually."
    Mom "Firstly: make plans for yourself, and do them before its too late."
    Mom "Secondly… I… I wish I hadn’t waited so long to tell you how I felt about you. Every memory that we had before our relationship started, feels like a wasted day. A day we could have spent together."

    scene MLR3_beach_house_p18

    Mom "I’m sorry, I know this is heavy. I just wanted to get it out of the way, at the start of the night."
    Mom "I envy you, [player_name]. I envy how young you are. I envy how each minute you spend with me, feels longer than the minutes I spend with you."
    MC "[Mom_name]…"

    scene MLR3_beach_house_p19

    Mom "I thought I’d be content, once I had you. I thought you were everything I wanted."
    Mom "But… I don’t know. I guess I’m just scared of losing you to someone younger. Someone your age."
    MC "[Mom_name], you’re not gonna lose me. I love you."

    scene MLR3_beach_house_p20

    Mom "I know… I love you too, [player_name]."
    MC "Are you sure you’re okay, [Mom_name]? You seem a little more… dour than usual."
    Mom "It’s just, I’m not really able to talk about any of this stuff when I’m in the house. I can’t risk myself getting too emotional."

    scene MLR3_beach_house_p21

    Mom "*Sip*"
    MC "(I guess she wanted to go on this holiday with me for more than just sex. It seems she genuinely wants to have a deep and meaningful conversation.)"
    MC "[Mom_name], c’mon and sit on my lap."

    scene MLR3_beach_house_p22

    Mom "No! I’m too heavy!"
    MC "Nonsense, you’re not at all! See? I lifted you up here, didn’t I?"
    Mom " Well… as long as I’m not hurting you."

    scene MLR3_beach_house_p23

    Mom " I really love you, [player_name]."
    Mom "I’m sorry for being so heavy, at the start of the night. I just… had to get all this crap out of my system."
    MC "It’s okay, I understand, [Mom_name]."

    scene MLR3_beach_house_p24

    MC "Everyone has crap that they need to clear, now and then. Just let it out - I’ll be here to listen."
    Mom "Are you sure? I don’t want you getting fed up with me."
    MC "I’m not gonna get fed up with you. Now, what’s on your mind?"

    scene MLR3_beach_house_p25
    if persistent.incest_patch == True:
        Mom "Well, apart from your father, I’m worried about our age difference. I’ll be at the peak of my career when you’re starting yours."
    else:
        Mom "Well, apart from Bob, I’m worried about our age difference. I’ll be at the peak of my career when you’re starting yours."
    MC "That’s not a problem at all, [Mom_name]! That’s a good thing?"
    Mom "How?"

    scene MLR3_beach_house_p26

    MC "Think about it - you’ll be at the top of your career. So, when I need advice on how to manage staff, or how to balance my accounts, who am I gonna turn to?"
    MC "I’m get advice from the woman I love - who also happens to be an expert in those areas."
    MC "And when you are introducing new technology to your workplace, you can always rely on me. I’m part of the younger generation. I can keep you up to speed with what’s going on."

    scene MLR3_beach_house_p27

    Mom "Ah, I see."
    MC "These aren’t bad things, [Mom_name]. We just have to make the most of the hand we’ve been dealt."
    MC "We can turn this unusual situation of ours, into an asset."

    scene MLR3_beach_house_p28

    Mom "God, I love a man with a brain. You look so sexy when you’re concentrating like that."
    Mom "Thanks for reassuring me. I know I’m being silly."
    MC "It’s okay, [Mom_name]. That’s what people do in a relationship, right? They support each other."

    scene MLR3_beach_house_p29

    Mom "How the heck did I get so lucky?"
    Mom "You’re like a knight in shining armour, who’s arrived to brighten up my life."
    Mom "I really love-"

    scene MLR3_beach_house_p30

    "*BZZT"
    "*BZZT*"
    Mom "Who the-?"

    scene MLR3_beach_house_p31

    if persistent.incest_patch == True:
        Mom "Oh shit. It’s your father."
    else:
        Mom "Oh shit. It’s Bob."
    MC "Fuck. Are you going to answer it?"
    "*BZZT BZZT*"

    scene MLR3_beach_house_p32

    Mom "*Sigh* I guess I better. The old man will start texting every five minutes, if I don’t."
    "*BZZT BZZT*"
    Mom "He’s such a clingy piece of-"

    scene MLR3_beach_house_p33

    Mom "Hello, Bob. What’s up?"
    MC "(I wonder what he’s calling for. Maybe just to catch up?)"
    Mom "Uh huh."

    scene MLR3_beach_house_p34

    Mom "Yes, Bob. In the freezer."
    MC "([Dad_name] must just be home from work and wondering where dinner is.)"
    Mom "Everyone knows how to work an oven, Bob. Get Sara to show you, she knows how now."

    scene MLR3_beach_house_p35

    Mom "No, Bob! Don’t just order a pizza! This is WHY you are putting on so much weight!"
    Mom "And just because I’m not there doesn’t give you an excuse to smoke your damn cigars in the bedroom. They stink my bedsheets out."
    MC "(Yikes!)"

    scene MLR3_beach_house_p36

    Mom "Ugh! Goodnight, Bob."
    Mom "I said, goodnight."
    Mom "No, I am NOT going to say those words back to you. Now, GOODNIGHT, BOB."
    "*Click*"

    scene MLR3_beach_house_p37

    Mom "*Sigh* I’m sorry about that, [player_name]. I completely forgot about him."
    Mom "The blithering imbecile can’t even prepare a frozen dinner for himself. He doesn’t know how to operate an oven. Can you believe that?! A man not knowing how to work an oven - in the 21st Century!"
    MC "Easy, [Mom_name]. Don’t let him get to you. Just take some deep breaths and-"

    scene MLR3_beach_house_p38

    "*Deedle le Deedle le Deedle*"
    Mom "Please tell me that isn’t your phone?"
    MC "*Groan* It is."

    scene MLR3_beach_house_p39

    Mom "You don’t have to answer it. Just hang up and let it go to voicemail."
    MC "I’ll just check who it is, first."
    MC "It might be Sara or Caroline needing help with something."

    scene MLR3_beach_house_p40
    if persistent.incest_patch == True:
        Mom "OR it could just be your dad."
    else:

        Mom "OR it could just be Bob."
    MC "Umm…"

    menu:
        "Answer the phone.":
            scene MLR3_beach_house_p42a

            MC "Uh, hello?"
            Bob "Hello there, champ! What’s up?"
            MC "Uh, nothing much, [Dad_name]. I’m a little busy right now though."

            scene MLR3_beach_house_p42b

            Mom "(Whispered) Hang up."
            Bob "Listen, I need your help here. I’ve just gotten one of those frozen dinners out of the freezer. I can’t figure out how to work this ruddy oven though!"
            Bob "Am I supposed to use celsius or fahrenheit?"
            MC "I, um…"

            scene MLR3_beach_house_p42c

            Bob "Hello? You still there?"
            MC "Y-Yeah, I’m just… Have you tried just putting it in and hoping for the best?"
            Mom "(Whispered) Hang. Up. Now."

            scene MLR3_beach_house_p42d

            Bob "Hello? Hello?"
            Bob "Are you there, champ?"
            Bob "There must be bad signal where you are, I’ll try calling you tomorrow! Sara! Sara! C’mon down and help me fix the oven!"
            jump MLR3_b_house_bag3
        "Let it go to voicemail.":
            scene MLR3_beach_house_p41a

            MC "I’ll just let it go to voicemail."
            MC "If he really needs help, he can speak to Caroline or Sara. They’re both at home."
            Mom "Thanks, Sweetie."
            jump MLR3_b_house_bag3

label MLR3_b_house_bag3:
    scene MLR3_beach_house_p43

    Mom "Now, I have a little surprise for you. Go and make yourself comfortable in the bedroom and wait for me there."
    MC "Okay, how long will you be?"
    Mom "Ten-ish minutes."
    $ can_hide_windows = False
    $ MLR3_b_house_bag = 3
    $ MLR3_b_house_wait = 1
    $ can_b_living_room = False

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump b_house_living_M1
