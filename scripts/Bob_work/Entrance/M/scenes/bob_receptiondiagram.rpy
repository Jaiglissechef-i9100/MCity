image Protif0 = "/images/Bob_work/entrance/M/Protif0.jpg"
image Protif1 = "/images/Bob_work/entrance/M/Protif1.jpg"
image Protif2 = "/images/Bob_work/entrance/M/Protif2.jpg"
default company_profit = 0

label bob_receptiondiagram:
    $ can_hide_windows = True
    hide screen map_button
    if company_profit == 0:
        scene Protif0
        if renpy.loadable("patch.rpy"):
            MC "(Eh… Profits aren’t looking too bad for Dad.)"
        else:
            MC "(Eh… Profits aren’t looking too bad for Bob.)"
        MC "(They’ve taken a hit in recent months - but at least it looks like things are finally stabilising.)"
        MC "(That must have been why he was so busy.)"

    if company_profit ==1:
        scene Protif1
        if renpy.loadable("patch.rpy"):
            MC "(Uh oh… Looks like me giving out sensitive company information to Zuri has led to Dad’s profit margins falling!)"
        else:
            MC "(Uh oh… Looks like me giving out sensitive company information to Zuri has led to Bob’s profit margins falling!)"


    if company_profit == 2:
        scene Protif2
        if renpy.loadable("patch.rpy"):
            MC "(Huh? Lying to Zuri has ensured that Dad’s company returns to a profitable position. That’s good to see!)"
            MC "(The projections are looking even stronger than before the crash. Dad’ll be pleased with this!)"
        else:
            MC "(Huh, lying to Zuri has ensured that Bob’s company returns to a profitable position. That’s good to see!)"
            MC "(The projections are looking even stronger than before the crash. Bob’ll be pleased with this!)"
    $ can_hide_windows = False
    jump bob_entrance_M1