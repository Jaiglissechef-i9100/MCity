image CR2_MS1_p1 = "/images/home/caroline_room/morning/scenes/CR2_MS1/1.jpg"
image CR2_MS1_p2 = "/images/home/caroline_room/morning/scenes/CR2_MS1/2.jpg"
image CR2_MS1_p3 = "/images/home/caroline_room/morning/scenes/CR2_MS1/3.jpg"
image CR2_MS1_p4a = "/images/home/caroline_room/morning/scenes/CR2_MS1/4a.jpg"
image CR2_MS1_p4b = "/images/home/caroline_room/morning/scenes/CR2_MS1/4b.jpg"
image CR2_MS1_p4c = "/images/home/caroline_room/morning/scenes/CR2_MS1/4c.jpg"
image CR2_MS1_p5a = "/images/home/caroline_room/morning/scenes/CR2_MS1/5a.jpg"
image CR2_MS1_p5b = "/images/home/caroline_room/morning/scenes/CR2_MS1/5b.jpg"
image CR2_MS1_p5c = "/images/home/caroline_room/morning/scenes/CR2_MS1/5c.jpg"
image CR2_MS1_p5d = "/images/home/caroline_room/morning/scenes/CR2_MS1/5d.jpg"


label CR2_MS1_label:
    if can_CR2_MS1 == False:
        hide screen map_button
        show screen caroline_room_morning
        $ clickable = False
        MC "I've already talked to her."
        $ clickable = True
        hide screen caroline_room_morning
        jump caroline_room_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CR2_MS1_p1 with dissolve
        $ can_hide_windows = True
        MC "(There’s Caroline, with her nose buried in a book, like always!)"
        MC "(She always WAS the brainy one!)"
        MC "Hey, Caroline! What’s up?"

        scene CR2_MS1_p2

        Caroline "Oh! Hi, [player_name]. I didn’t hear you come in, there."
        Caroline "Not a lot - Just taking a break from work. Now that I’m actually making profits, I should REALLY think about reporting my earnings to the government."
        MC "Ugh, sounds boring!"
        Caroline "It REALLY is! Which is why I’m taking a well-deserved rest."

        scene CR2_MS1_p3

        MC "What’s the book?"
        Caroline "It’s a romance novel. A girl comes to work in a factory in Detroit, but soon finds herself seduced by the muscular supervisor."
        MC "It sounds like a real piece of literature..."


        scene CR2_MS1_p4a

        Caroline "I can hear the sarcasm in your voice. It’s typical mass-produced trash, but it keeps me entertained."
        MC "Is there much sex it in?"
        scene CR2_MS1_p4b

        Caroline "Hehe... Trust you to ask a question like that."
        MC "Hey- I’m serious!"
        Caroline "Of course there is - It’s a romance novel."

        scene CR2_MS1_p4c

        Caroline "It even has the “Not for Children” warning on the back."
        Caroline "I mean, I’m on chapter eight, and I’ve already seen the main character get screwed five times."
        Caroline "And TWO of those times, involved it going in her ass!"
        MC "I never imagined, chick literature was this filthy!"

        scene CR2_MS1_p4b

        Caroline "You should pick up a couple of chick books some time. You might enjoy the cheap smut."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
        menu:
            "Grab Caroline’s ass.":
                scene CR2_MS1_p5a

                MC "(I think I’ll grope her ass now. We did make that deal and Caroline owes me BIG time for all the help I gave getting her company up and running!)"
                MC "(I’m sure she won’t mind a quick squeeze. What’s the worst that could happen?)"
                MC "(Plus, she’s sitting there in her panties. She’s probably expecting it to happen… right?)"

                scene CR2_MS1_p5b

                MC "(Soft and warm! Exactly like I imagined it would be!)"
                Caroline "H-Hey! What are you doing?"
                MC "Remember the deal?"

                scene CR2_MS1_p5c
                if renpy.loadable("patch.rpy"):
                    Caroline "Yeah, but what if Mom walks in right now."
                    Caroline "Or, heaven forbid, Sara! What would she think if she saw her brother GROPING her sister’s ass?"
                else:
                    Caroline "Yeah, but what if Linda walks in right now."
                    Caroline "Or, heaven forbid, Sara! What would she think if she saw you GROPING my ass?"
                MC "But-"

                scene CR2_MS1_p5d

                Caroline "We can fool around in my work, but anything at home is far too risky."
                if renpy.loadable("patch.rpy"):
                    Caroline "I’m not welching on our deal - we’ve got a good thing going. Let’s not risk blowing it, by Mom or Dad finding out. Okay?"
                else:
                    Caroline "I’m not welching on our deal - we’ve got a good thing going. Let’s not risk blowing it, by Linda or Bob finding out. Okay?"
                MC "Yeah, I guess you’re right, Caroline."
                Caroline "Good. Let’s just pretend this never happened, okay?"
                MC "I understand."
                $ can_CR2_MS1 = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump caroline_room_morning1
            "Don’t risk grabbing Caroline’s ass.":

                scene CR2_MS1_p5a

                MC "(It isn’t worth the risk, grabbing her ass right now.)"
                if renpy.loadable("patch.rpy"):
                    MC "(It might piss her off - plus Mom or Dad or Sara could walk in!)"
                    MC "(ANY of them would freak out if they saw me groping Caroline’s bum. We should probably keep our schmoozing to her workplace, where we have some privacy.)"
                else:
                    MC "(It might piss her off - Plus, Linda or Bob or even Sara could just walk in!)"
                    MC "(ANY of them would freak out if they saw me groping Caroline’s bum. We should probably keep our schmoozing to her workplace, where we have some privacy.)"
                $ can_CR2_MS1 = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump caroline_room_morning1