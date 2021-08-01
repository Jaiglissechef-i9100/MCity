
define config.enter_replay_transition = Fade(0.3, 0.3, 0.3)
define config.exit_replay_transition = Fade(0.3, 0.3, 0.3)

label setup_gallery:
    if _in_replay:
        $ player_name = "You"
        $ Sara_name = "Sara"
    return

label modreplay_bath_Linda1:
    call setup_gallery
    play music "/sfx/Sneaky Snitch.mp3" loop fadein 2.0
    scene ml_evening_bathroom_scene_v1_p1
    if renpy.loadable("patch.rpy"):
        MC "(Just in time! It looks like Mom’s about to take a bath!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Just in time! It looks like Linda’s about to take a bath!)"
    MC "(Damn… She’s got the best pair of thighs I’ve ever seen on a woman.)"
    MC "(No girl in my school even comes close to that!)"
    scene ml_evening_bathroom_scene_v1_p2
    if renpy.loadable("patch.rpy"):
        MC "(I can’t help but feel this is wrong… She’s my mother and I shouldn’t be thinking these things about her.)"
    if not renpy.loadable("patch.rpy"):
        MC "(I can’t help but feel this is wrong… She’s my friend and I shouldn’t be thinking these things about her.)"
    MC "(On the other hand, just look at that ass. It’s fucking perfect!)"
    MC "(I can almost see her vulva, with that tight g-string she’s wearing!)"
    $ renpy.end_replay()


label modreplay_bath_Linda2:
    call setup_gallery
    play music "/sfx/Sneaky Snitch.mp3" loop fadein 2.0
    scene black
    if renpy.loadable("patch.rpy"):
        MC "(I’m a little late tonight - I hope I haven’t missed Mom getting washed!)"
    if not renpy.loadable("patch.rpy"):
        MC "(I’m a little late tonight - I hope I haven’t missed Linda getting washed!)"
    scene ml_evening_bathroom_scene2_v1_p1 with dissolve
    MC "(Phew! Just in time!)"
    MC "(And she’s naked too! Awesome!)"
    MC "(I wonder how often she works out, to get a body THAT fit.)"
    scene ml_evening_bathroom_scene2_v1_p2
    if renpy.loadable("patch.rpy"):
        MC "(I’d give my right arm, for the girls at my school to have tits like Mom does! Those puppies are amazing!)"
    if not renpy.loadable("patch.rpy"):
        MC "(I’d give my right arm, for the girls at my school to have tits like Linda does! Those puppies are amazing!)"
    MC "(I’d be so distracted in class that I’d never learn anything though. Haha!)"
    MC "(Right, I better head on out of here before I get caught…)"
    $ renpy.end_replay()




label modreplay_bath_Sara1:
    call setup_gallery
    play music "/sfx/Aces High.mp3" loop fadein 2.0
    scene scene4_v1p1
    MC "(Looks like I made it just in time.)"
    MC "(Hey, those are the panties I almost stole from her!)"
    MC "(She’s got a matching bra too - it must be a set she likes.)"
    MC "(Maybe tomorrow there will be a better view!)"
    $ renpy.end_replay()


label modreplay_bath_Sara2:
    call setup_gallery
    play music "/sfx/Aces High.mp3" loop fadein 2.0
    scene scene4_v1p2
    MC "(Mmm, even better this time! I get a front row seat to her naked ass!)"
    MC "(Damn, she has such sexy thighs too.)"
    MC "(I’d love to spread those cheeks and fuck her silly.)"
    MC "(Let’s watch her again some other time.)"
    $ renpy.end_replay()


label modreplay_bath_Sara3:
    call setup_gallery
    play music "/sfx/Aces High.mp3" loop fadein 2.0
    scene scene4_v1p3
    MC "(Perfect timing! It looks like she’s just about to take a shower!)"
    MC "(I can almost see her pussy from this angle!)"
    if renpy.loadable("patch.rpy"):
        MC "(Please, if there’s a God up there, I’m begging you! Let my sister bend over right now!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Please, if there’s a God up there, I’m begging you! Let my friend bend over right now!)"
    scene scene4_v1p3a
    Sara "(Huh, looks like I missed a hair when I was shaving my legs.)"
    MC "(There is a God!)"
    MC "(Damn, she looks so tight! I would love to bury my cock in her cunt.)"
    MC "(It would feel fucking amazing!)"
    $ renpy.end_replay()


label modreplay_bath_Sara4:
    call setup_gallery
    play music "/sfx/RetroFuture_Clean.mp3" loop fadein 2.0
    scene scene4_v1p4
    Sara "Ah! Ah… Ahh… Mmm… Ooh…"
    MC "(Just in time! Looks like she is masturbating!)"
    MC "(I wonder what she’s looking at on her phone. Could it be that picture of my cock?)"

    Sara "Ohh… Yes, brother! Yes…!"
    if renpy.loadable("patch.rpy"):
        MC "(She’ll need to be quieter than that, if she doesn’t want Mom to hear her!)"
    if not renpy.loadable("patch.rpy"):
        MC "(She’ll need to be quieter than that, if she doesn’t want Linda to hear her!)"
    $ renpy.end_replay()


label modreplay_bath_Sara5:
    call setup_gallery
    play music "/sfx/March of the Spoons.mp3" loop fadein 2.0
    scene SR2_bath_p1 with dissolve
    MC "Huh? What is she doing?"
    MC "She was supposed to take a shower."
    scene SR2_bath_p2
    MC "Is she sleepy again? Those games are gonna kill her one day."
    scene SR2_bath_p3
    MC "Seriously!? Is she planning on taking a nap in the bathroom?"
    MC "..."
    if renpy.loadable("patch.rpy"):
        MC "I hope Mom doesn't notice her."
    else:
        MC "I hope Linda doesn't notice her."
    $ renpy.end_replay()