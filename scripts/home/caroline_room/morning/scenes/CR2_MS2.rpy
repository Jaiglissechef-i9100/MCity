image CR2_MS2_p1 = "/images/home/caroline_room/morning/scenes/CR2_MS2/1.jpg"
image CR2_MS2_p2 = "/images/home/caroline_room/morning/scenes/CR2_MS2/2.jpg"
image CR2_MS2_p3 = "/images/home/caroline_room/morning/scenes/CR2_MS2/3.jpg"
image CR2_MS2_p4 = "/images/home/caroline_room/morning/scenes/CR2_MS2/4.jpg"
image CR2_MS2_p5 = "/images/home/caroline_room/morning/scenes/CR2_MS2/5.jpg"

label CR2_MS2_label:
    if can_CR2_MS2 == False:
        show screen caroline_room_morning
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR2_MS2_p1 with dissolve
    $ can_hide_windows = True
    Caroline "No, you don’t understand - I NEED the money to pay the rent!"
    Caroline "..."
    Caroline "I can’t wait two months for an approval. I need this right now!"
    MC "(Shit… Sounds like things aren’t going well for Caroline, with the bank.)"

    scene CR2_MS2_p2

    Caroline "How can you call it a crisis loan, if it takes two months to get approved?!"
    Caroline "..."
    Caroline "Ugh, fine… I don’t know how I’m going to keep my business afloat in the meantime though."
    Caroline "…"
    MC "(She looks properly depressed right now. I should probably intervene.)"
    Caroline "Okay… Thanks for your time… Will you call me if anything changes?"
    Caroline "Thanks..."

    scene CR2_MS2_p3

    MC "Hey Caroline, I couldn’t help overhearing the end of your conversation there.."
    Caroline "This isn’t something you need to concern yourself with."
    MC "I just want you to know that I’m here to help, if you need me."

    scene CR2_MS2_p4

    Caroline "My rent is due, I have no cash on hand, and it’ll be months before the bank can approve a crisis loan! How can you possibly help?"
    MC "I could give you a loan myself - or even GIVE you some money, to help you get back on your feet."
    Caroline "I… uh…"

    scene CR2_MS2_p5

    Caroline "No. I can’t. I’m an adult now. I have to start standing on my own two feet, and fighting my own battles for a change."
    MC "But, Carol-"
    Caroline "No buts about it. I have to sort this out on my own."

    scene CR2_MS2_p3

    Caroline "Thanks for your concern though. It means a lot to me."
    $ can_CR2_MS2 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
