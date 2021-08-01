image SR3_we_SC_bus_p10 = "images/v71/2_WE/3_Shopping Centre/10.jpg"
image SR3_we_SC_bus_p11 = "images/v71/2_WE/3_Shopping Centre/11.jpg"
image SR3_we_SC_bus_p12 = "images/v71/2_WE/3_Shopping Centre/12.jpg"
image SR3_we_SC_bus_p13 = "images/v71/2_WE/3_Shopping Centre/13.jpg"
image SR3_we_SC_bus_p14 = "images/v71/2_WE/3_Shopping Centre/14.jpg"
image SR3_we_SC_bus_p15 = "images/v71/2_WE/3_Shopping Centre/15.jpg"
image SR3_we_SC_bus_p16 = "images/v71/2_WE/3_Shopping Centre/16.jpg"
image SR3_we_SC_bus_p17 = "images/v71/2_WE/3_Shopping Centre/17.jpg"
image SR3_we_SC_bus_p18 = "images/v71/2_WE/3_Shopping Centre/18.jpg"
image SR3_we_SC_bus_p19 = "images/v71/2_WE/3_Shopping Centre/19.jpg"
image SR3_we_SC_bus_p20 = "images/v71/2_WE/3_Shopping Centre/20.jpg"
image SR3_we_SC_bus_p21 = "images/v71/2_WE/3_Shopping Centre/21.jpg"
image SR3_we_SC_bus_p22 = "images/v71/2_WE/3_Shopping Centre/22.jpg"
image SR3_we_SC_bus_p23 = "images/v71/2_WE/3_Shopping Centre/23.jpg"
image SR3_we_SC_bus_p24 = "images/v71/2_WE/3_Shopping Centre/24.jpg"
image SR3_we_SC_bus_p25 = "images/v71/2_WE/3_Shopping Centre/25.jpg"

label SR3_we_SC_bus_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene SR3_we_SC_bus_p10
    MC "Well, this is the place. Do you know what you want?"
    Sara "Hmm… Caroline always used to buy orange sorbet every time we went out. And I’d always pick the mint."
    MC "Okay, mint it is then."
    scene SR3_we_SC_bus_p11
    Sara "Two seconds, I just want to check the menu."
    MC "Do you know if the strawberry is good?"
    Sara "Dunno, never tried it. Their other flavours are all amazing though, so I don’t think you can go wrong."
    scene SR3_we_SC_bus_p12
    MC "I haven’t seen you this excited in years. Haha!"
    Sara "I know, I’m getting major nostalgia right now. I haven’t had one of these since I was a kid."
    scene SR3_we_SC_bus_p13
    Salesman "Hello there, what can I get for you?"
    MC "Uhh… I’ll take one strawberry, and Sara will take…"
    Sara "Can I get a double, [player_name]?"
    MC "Sure."
    Sara "In that case I’ll take one scoop or orange and one scoop of mint."

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)

    scene SR3_we_SC_bus_p14
    Salesman "Ah… right. I'm afraid that we've run out of the mint."
    Salesman "I do have a wide selection of other flavours though. Perhaps you’d like to try coffee or raspberry?"
    Sara "Aww…"
    scene SR3_we_SC_bus_p15
    Salesman "I really am sorry, madam. It’s been extremely busy ever since we opened today."
    Salesman "There’s a freezer to the left of my van, if you take a look in that there *might* be some mint ice lollies left if you fancy one of those instead?"
    Sara "Better than nothing, I guess."
    scene SR3_we_SC_bus_p16
    MC "I can’t believe you’ve sold out already."
    Salesman "Honestly, we got far bigger crowds than anyone was expecting. Do you still want me to make you a strawberry cone?"
    MC "Hold off one minute."
    scene SR3_we_SC_bus_p17
    MC "Any luck, Sara?"
    Sara "Umm… Vanilla, vanilla, more vanilla… lemon, vanilla again…"
    scene SR3_we_SC_bus_p18
    Salesman "I am terribly sorry, madam. It appears that our selection of ice lollies is also running low as well."
    Sara "Aww… This sucks…"
    MC "(Wow! Sara’s ass looks so fucking hot in that mini dress.)"
    scene SR3_we_SC_bus_p19
    MC "(Those panties she’s wearing are a size too small! I can see the edges of her vulva spilling out the sides! If I got her to lean over a bit more, I could get a better view.)"
    MC "Hey Sara, try deeper in the freezer. Search way down at the bottom."
    Salesman "Mmm, yes! That’s a good idea. And take your time… no rush at all."
    scene SR3_we_SC_bus_p20
    MC "Oh yeah…"
    MC "(Her asshole’s barely covered at all right now! If her panties slip, even a little bit, I should be able to see her tight little asshole.)"
    Salesman "(This is the best shift ever!)"
    scene SR3_we_SC_bus_p21
    Sara "I can’t find any, [player_name]..."
    Sara "Ugh… Nope, this freezer is like a Catholic schoolgirl’s browser history, nothing but vanilla."
    scene SR3_we_SC_bus_p22
    MC "(God, that ass is to die for. I still can’t believe that I got to fuck that.)"
    MC "(AND I was the first one too! If there was no one else here, I’d tug those panties down to her ankles and ram my dick into her little virgin pussy while she was bent over the freezer.)"
    scene SR3_we_SC_bus_p23
    MC "(She’d be screaming in ecstasy as my thick cock made her cum again and again.)"
    MC "(And then I’d finish by filling up her teenage pussy with a thick creamy load.)"
    scene SR3_we_SC_bus_p24
    Sara "Hello? [player_name]?"
    Sara "[player_name]!"
    MC "Huh? W-What?"
    Sara "I was talking to you - you’d spaced out on me. I was saying that there’s no mint left."
    scene SR3_we_SC_bus_p25
    Salesman "Y’know, if you guys are okay sitting in for your ice cream, our parlour is still open. They probably have a tonne of different flavours still in stock."
    MC "Should we check out the parlour then, Sara?"
    scene SR3_we_SC_bus_p12
    Sara "I would have preferred to walk around and explore the new mall, but that’s okay. Thanks for your help!"
    Salesman "My pleasure, thanks for the view."
    Sara "The view?"
    Salesman "I… uh… I mean, thank you for viewing my store!"
    Sara "Oh… No problem!"
    MC "C’mon Sara, let’s go and see what the parlour is like."

    $ SR3_we_SC_bus = False
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Life of Riley.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR3_we_IC_shop_salesman = True
    scene black
    $ renpy.pause(3, hard= True)
    jump SR3_we_IC_shop