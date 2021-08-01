label lain_cheat_money:
    $ inventory.money = 9999
    play sound 'sfx/correct.wav'
    "Success - $9,999 acquired!"
    return

label lain_cheat_secretcards:
    $ persistent.mod_unlock_secret_gallery = True
    play sound 'sfx/correct.wav'
    "Success - All secret cards unlocked!"
    return
label lain_cheat_scenegallery:
    $ persistent.mod_unlock_scene_gallery = True
    play sound 'sfx/correct.wav'
    "Success - All scene gallery scenes unlocked!"
    return