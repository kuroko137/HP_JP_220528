# SHOW UNREAD MESSAGES

transform hateplus_window_fade:
    on show:
        alpha 0.0
        linear .5 alpha 1.0

    on replace:
        alpha 0.0
        linear .5 alpha 1.0
        
    on replaced:
        linear .5 alpha 0.0

transform hateplus_window_say_fade:
    on show:
        alpha 0.0
        linear .5 alpha 1.0

    on hide:
        alpha 1.0
        linear 0.0

init python:
    import time, datetime, random, pygame

    def no_effect(trans, st, at):
        if not _preferences.transitions:
            trans.alpha = 1.0
            return 0

        return None

    def flicker_func(trans, st, at):
        if not _preferences.transitions:
            trans.alpha = 1.0
            return 0

        t = time.time()%17.83

        if t < 2.0: trans.alpha = 1.0-.1*(t/2.0)
        elif t < 3.0: trans.alpha = .9
        elif t < 5.0: trans.alpha = .9+.3*((t-3.0)/2.0)
        elif t < 5.05: trans.alpha = 1.2-.5*((t-5.0)/.05)
        elif t < 5.07: trans.alpha = .7+1.3*((t-5.05)/.02)
        elif t < 5.09: trans.alpha = 2.0-2.0*((t-5.07)/.02)
        elif t < 5.11: trans.alpha = 1.5*((t-5.09)/.02)
        elif t < 5.31: trans.alpha = 1.5
        elif t < 5.33: trans.alpha = 1.5-1.5*((t-5.31)/.02)
        elif t < 5.38: trans.alpha = 1.3*((t-5.33)/.05)
        elif t < 10.33: trans.alpha = 1.3-.4*((t-5.38)/5.0)
        elif t < 13.33: trans.alpha = .9+.3*((t-10.33)/3.0)
        elif t < 13.83: trans.alpha = 1.2-.2*((t-13.33)/.5)
        elif t < 17.83: trans.alpha = 1.0

        return 0

transform flicker:
    function flicker_func
    # alpha 1.0
    # easein 2.0 alpha .9
    # pause 1.0
    # easein 2.0 alpha 1.2
    # linear .05 alpha .7
    # linear .02 alpha 2.0
    # linear .02 alpha 0
    # linear .02 alpha 1.5
    # pause .2
    # linear .02 alpha 0
    # linear .05 alpha 1.3
    # linear 5.0 alpha .9
    # linear 3.0 alpha 1.2
    # linear .5 alpha 1.0
    # pause 4.0
    # repeat

transform less_alpha:
    alpha 0.8

transform glow_flicker:
    function no_effect
    alpha 1.0
    easein 2.0 alpha .7
    pause 1.0
    easein 2.0 alpha 1.0
    linear 6.85 alpha .5
    linear 6.85 alpha 1.0
    repeat

transform transform_nop:
    pass

transform noise_at:
    function noise_at

screen glow:
    zorder 106

    add ("glow" + short(current_character) + ".dlc2.png") at glow_flicker
    if _preferences.transitions:
        add ImageReference("hateplus_noise")

screen hyunaeglow:
    zorder -1
    add ("Hyun-Ae2/1-Body" + outfit.replace(".dlc1", "") + "Glow.dlc2.png") xanchor 0.5 xpos If(current_character != "xharem", 250, 150) yanchor 0 ypos -30


screen muteglow:
    zorder -1
    add If(current_character == "mute", "Mute2/Mute/1-BodyGlow.dlc2.png", "Mute2/Mute/1-BodyGlow2.dlc2.png") xanchor 0.5 xpos If(current_character == "mute", 200, 320) yanchor 0 ypos If(current_character == "mute", -60, -8)

screen newmuteglow:
    zorder -1
    add ("Mute2/NewMute/1-BodyGlow.dlc2.png") xanchor 0.5 xpos 200 yanchor 0 ypos -60

screen xharemglow:
    null

screen hide_everything:
    zorder 1000

    timer 10.0 action Hide("hide_everything")

    window background Solid((0,0,0,255)) xminimum 1024 yminimum 640:
        text "LOADING..." style style.text["hateplus"] yalign 0.5 xalign 0.5

screen title:
    default text = ""
    viewport child_size (500, 40) xmaximum 500 ymaximum 40 at flicker:
        has hbox
        text _(text) style style.hateplus_title[persistent._language] color hateplus_color[char_style(None)] outlines hateplus_outlines[char_style(None)]
        text "——————————————————————————————————————" kerning -6 size 28 font planer bold True color hateplus_color[char_style(None)] outlines hateplus_outlines[char_style(None)]

screen hateplus_bottom_menu:
    zorder 109
    default quit = True
    
    hbox xalign 1.0 yalign 1.0 yoffset -5 xoffset -10 spacing 3 focus "bottom_menu" at slower_fade_once:
        use hateplus_bottom_menu_buttons(quit=quit)

screen hateplus_bottom_menu_buttons:
    button style style.button[char_style()] background ("config-" + short(current_character) + ".dlc2.png") hover_background ("config-" + short(current_character) + "hover.dlc2.png") xminimum 60 yminimum 43 xpadding 0 action [ Play("sound", "sfx/fxbeep2.mp3"), Show("preferences", Dissolve(0.5)) ]:
        null
    
    button style style.button[char_style()] background ("power-" + short(current_character) + ".dlc2.png") hover_background ("power-" + short(current_character) + "hover.dlc2.png") xminimum 60 yminimum 43 xpadding 0 action [ Play("sound", "sfx/fxbeep5.mp3"), If(quit, Show("hateplus_quit"), Quit(False)) ]:
        null


transform main_unfold:
    alpha 0 crop (0,0,533,50)
    pause .2
    linear .3 alpha 1.0
    easeout .3 crop (0,0,533,320)

transform main_unfold_fast:
    crop (0,0,533,320)

transform main_unfold_contents:
    function no_effect
    alpha 0
    pause 1.0
    alpha 0.1
    easeout .3 alpha .9
    linear .01 alpha .8
    linear .01 alpha .9
    linear .01 alpha .8
    pause .1
    alpha 1.0

transform main_unfold_title:
    alpha 0
    pause .4
    easeout 0.8 alpha .9
    pause .1
    alpha 1.0

transform second_main_unfold:
    alpha 0 crop (0,0,533,50)
    pause 1.2
    linear .3 alpha 1.0
    easeout .3 crop (0,0,533,320)

transform second_main_unfold_contents:
    alpha 0
    pause 2.0
    alpha 0.1
    easeout .3 alpha .9
    linear .01 alpha .8
    linear .01 alpha .9
    linear .01 alpha .8
    pause .1
    alpha 1.0

transform second_main_unfold_title:
    alpha 0
    pause 1.5
    easeout 0.8 alpha .9
    pause .1
    alpha 1.0

init python:
    def change_outfit(use_outfit):
        store._return = use_outfit
        renpy.jump("hateplus_change_outfit")

    def get_time(secs=None):
        use_time = time.localtime(secs)
        hour = use_time.tm_hour
        minute = use_time.tm_min
        second = use_time.tm_sec
        meridiem = "AM"

        if hour > 12:
            hour -= 12
            meridiem = "PM"

        hour = str(hour)
        if minute < 10: minute = "0" + str(minute)
        else: minute = str(minute)

        return hour,minute,second,meridiem

screen hateplus_dialogue_button:
    on "hide" action [ Hide("hyunaeglow"), Hide("muteglow"), Hide("newmuteglow") ]

    zorder 1
    default use_character = current_character
    if current_character != "xharem":
        default position = hateplus_fast_farther_left[current_character]
    elif use_character == "hyunae":
        add ImageReference("mute full") at hateplus_mute_harem_fast_farther_left xoffset 12 yoffset 0

    button background None action [ Play("sound", "sfx/fxbeep2.mp3"), Hide("main_screen"), Jump("hateplus_jump_to_dialogue") ] hovered Show(use_character + "glow", Dissolve(0.5)) unhovered Hide(use_character + "glow", Dissolve(0.5)) at position xminimum 1000 xmaximum 1000 focus_mask ImageReference(use_character + " full"):
        null height 640

init python:
    def debug_code_add(a):
        store.debug_code += str(a)

screen hateplus_main_screen:
    #modal True
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    key "K_LCTRL" action nop
    key "K_RCTRL" action nop

    tag main

    default all_unextracted = False
    default any_unextracted = True
    default inbox_unread = 0
    default fast = False

    python:
        hour,minute,second,meridiem = get_time()

        # I don't like 24-hour display so added exception for Korean too. - iAmGhost
        if persistent._language != "" and persistent._language != "korean" and persistent._language != "japanese":
            if meridiem == "PM":
                hour = str(int(hour)+12)

            meridiem = ""

        connected = random.choice([ 0, 1, 1, 1 ])
        ul = (298 + random.randint(-5,5))*connected
        dl = (207 + random.randint(-5,5))*connected

        inbox_unread = 0
        for message in inbox.contents:
            if message.enabled and not message.read:
                inbox_unread += 1

    $ store.game_playing = True

    #on "replace" action If(not fast, Show("hateplus_main_screen_ai"), nop)
    on "hide" action [ Hide("hateplus_main_screen_ai"), Hide("hateplus_main_screen_outfits"), Hide("hateplus_main_screen_disabled") ]
    on "replaced" action [ Hide("hateplus_main_screen_ai"), Hide("hateplus_main_screen_outfits") ]

    button action nop background None xalign 0.5 yalign 0.5:
        null width 1024 height 640

    window style style.window["hateplus"] size_group "main_window" xmaximum 533 xminimum 533 ymaximum 320 xalign 0.95 yanchor 0 ypos 5 at get_transition(If(not fast, main_unfold, main_unfold_fast)):
        has vbox
        window background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 at If(not fast, main_unfold_title, transform_nop):
            use title(text="Starship W{size=-6}HITE{/size} P{size=-6}RINCESS{/size}")
        fixed at If(not fast, main_unfold_contents, transform_nop):
            vbox:
                hbox yoffset -5:
                    window xpadding 0 ypadding 0 background None xminimum 280 xmaximum 280:
                        vbox spacing -15:
                            hbox:
                                # For Korean UI tweak - iAmGhost
                                $ meridiem_yoffset = 0
                                if persistent._language == "korean":
                                    $ meridiem_yoffset = 24
                                # For Japanese UI tweak
                                $ modify_size = 0
                                if persistent._language == "japanese":
                                    $ meridiem_yoffset = 1
                                text meridiem style style.text["hateplus" + persistent._language] bold True size 18 yoffset meridiem_yoffset color (192,192,192,128) at flicker
                                text hour style style.text["hateplus"] bold True size 50 yoffset -5 color (192,192,192,128) at flicker
                                text minute style style.text["hateplus"] bold True size 50 yoffset -5 at flicker
                                vbox spacing -10:
                                    # For Korean UI tweak - iAmGhost
                                    if persistent._language == "korean":
                                        text "4989" style style.text["hateplus" + persistent._language] bold True size 22 at flicker
                                        hbox:
                                            text _("FEBRUARY " + str(store.day+8)) style style.text["hateplus" + persistent._language] bold True size 22 color (192,192,192,128) at flicker ypos 3
                                            text _([ "Mon.{space=27}", "Tues.{space=30}", "Wed.{space=34}" ][store.day-1]) style style.text["hateplus"+ persistent._language] bold True size 22 color (192,192,192,128) ypos 3 yalign 0 xalign 1.0 at flicker
                                    else:
                                        hbox:
                                            text "4989" style style.text["hateplus" + persistent._language] bold True size 22 at flicker
                                            text _([ "Mon.{space=27}", "Tues.{space=30}", "Wed.{space=34}" ][store.day-1]) style style.text["hateplus"+ persistent._language] bold True size 22 color (192,192,192,128) xalign 1.0 at flicker
                                        text _("FEBRUARY " + str(store.day+8)) style style.text["hateplus" + persistent._language] bold True size 22 color (192,192,192,128) at flicker
                            text _([ "Lunar New Year (Feb 10)", "Lunar New Year", "" ][store.day-1]) style style.text["hateplus"+ persistent._language] size 20 at flicker

                    vbox spacing -10:
                        # For Japanese UI tweak
                        if persistent._language == "japanese":
                            text ("ETA " + str(4-store.day) + " days") style style.text["hateplus" + persistent._language] size 18 at flicker ypos 0
                        else
                            text _("Current Destination") style style.text["hateplus" + persistent._language] at flicker
                        hbox:
                            vbox spacing -10 yalign 0.5:
                                # For Korean UI tweak - iAmGhost
                                $ eta_ypos = 0
                                $ sol_ypos = 0

                                if persistent._language == "korean":
                                    $ eta_ypos = 2
                                    $ sol_ypos = 5
                                if persistent._language == "japanese":
                                    text _("Current Destination") style style.text["hateplus" + persistent._language] at flicker
                                else
                                    text ("ETA " + str(4-store.day) + " days") style style.text["hateplus" + persistent._language] size 18 at flicker ypos eta_ypos
                                text "Sol III" style style.text["hateplus" + persistent._language] size 24 bold True at flicker ypos sol_ypos
                            vbox spacing -12 yalign 0.5:
                                text "179° 56' 39.4\"" style style.text["hateplus"] size 16 color (192,192,192,128) at flicker
                                text "+0° 2' 46.2\"" style style.text["hateplus"] size 16 color (192,192,192,128) at flicker
                                text "25903 ly" style style.text["hateplus"] size 16 color (192,192,192,128) at flicker

                null height 10
                hbox spacing 10 xalign 0.5:
                    vbox spacing -15 yalign 1.0:
                        text (str(int(power*2+1)) + "%") style style.text["hateplus"] size 40 xalign 0.5 color (192,192,192,128) at flicker
                        text "POWER" style style.text["hateplus" + persistent._language] xalign 0.5 at flicker
                    #vbox spacing -15 yalign 1.0:
                    #    text "73%" style style.text["hateplus"] size 40 xalign 0.5 color (192,192,192,128) at flicker
                    #    text "SHLD" style style.text["hateplus"] xalign 0.5 at flicker
                    vbox spacing -13 yalign 1.0:
                        text (str(ul) + " bps UL") style style.text["hateplus"] xalign 1.0 text_align 1.0 size 20 minwidth 105 color (192,192,192,128) at flicker
                        text (str(dl) + " bps DL") style style.text["hateplus"] xalign 1.0 text_align 1.0 size 20 minwidth 105 color (192,192,192,128) at flicker
                        null height 15
                        text "COMM" style style.text["hateplus" + persistent._language] xalign 0.5 at flicker
                    vbox spacing -13 yalign 1.0:
                        text "894 kPA" style style.text["hateplus"] size 20 xalign 0.5 color (192,192,192,128) at flicker
                        text "15.1% O{size=8}2{/size}" style style.text["hateplus"] size 20 xalign 0.5 color (192,192,192,128) at flicker
                        null height 15
                        text "ATM" style style.text["hateplus" + persistent._language] xalign 0.5 at flicker
                    vbox spacing -13 yalign 1.0:
                        text "99±2% hit" style style.text["hateplus"] xalign .5 size 20 color (192,192,192,128) at flicker
                        text "2300 ppm"  style style.text["hateplus"] xalign 0.5 size 20 color (192,192,192,128) at flicker
                        null height 15
                        text "DEFL." style style.text["hateplus" + persistent._language] xalign 0.5 at flicker
                    #button style style.button[char_style()] action nop yalign 1.0 yoffset 8 yminimum 76 right_margin -10 xminimum 90 left_padding 14 right_padding 16 focus "nav" at flicker:
                    #    text "NAV" style style.text[char_style()] xalign 0.5 yalign 0.5

                    # For Korean UI tweak - iAmGhost
                    $ unread_button_yoffset = 8
                    $ unread_button_xoffset = 0

                    if persistent._language == "korean":
                        $ unread_button_yoffset = 6
                        $ unread_button_xoffset = -10

                    # For Japanese UI tweak
                    if persistent._language == "japanese":
                        $ unread_button_yoffset = 8
                        $ unread_button_xoffset = 0

                    button style style.button[char_style()] size_group "stats" action [ Play("sound", "sfx/fxbeep5.mp3"), Jump("hateplus_pan_to_inbox") ] yalign 1.0 yoffset unread_button_yoffset xoffset unread_button_xoffset left_padding 14 right_padding 16 focus "inbox" at flicker:
                        has vbox spacing -15

                        # For Korean UI tweak - iAmGhost
                        $ unread_size = style.text[char_style() + persistent._language].size
                        $ inbox_size = style.text[char_style() + persistent._language].size
                        $ inbox_ypos = 0
                        $ unread_ypos = 0
                        $ unread_text = " unread"

                        if persistent._language == "korean":
                            $ unread_ypos = -4
                            $ unread_size = 20
                            $ inbox_ypos = 3
                            $ inbox_size = 20
                            $ unread_text = " 부재중"

                        # For Japanese UI tweak
                        if persistent._language == "japanese":
                            $ unread_ypos = 0
                            $ unread_size = 18
                            $ inbox_ypos = 0
                            $ inbox_size = 17
                            $ unread_text = "未読 "

                        if persistent._language == "japanese":
                            text _("INBOX") style style.text[char_style() + persistent._language] xalign 0.5 ypos -5 size inbox_size
                            text _(unread_text + str(inbox_unread)) style style.text[char_style() + persistent._language] xalign 0.5 bold True size unread_size ypos unread_ypos
                        else:
                            text _(str(inbox_unread) + unread_text) style style.text[char_style() + persistent._language] xalign 0.5 bold True size unread_size ypos unread_ypos
                            text _("INBOX") style style.text[char_style() + persistent._language] xalign 0.5 ypos 3 size 20
                text _(WARNING_TEXT[char_style(None)]) style style.text["hateplus" + persistent._language] justify True size 20 bold (not persistent._language) at flicker


screen hateplus_main_screen_ai:
    tag ai

    default any_unextracted = False
    default all_unextracted = False

    python:
        for message in all_block.contents:
            if message.enabled:
                any_unextracted = True
            else:
                all_unextracted = False

    on "replaced" action With(Dissolve(0.5))

    default timing = 2

    window style style.window["hateplus"] size_group "main_window" xmaximum 533 xminimum 533 xalign 0.95 yanchor 0 ypos 330 at get_transition(If(timing == 2, second_main_unfold, main_unfold)):
        has vbox
        window background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 at If(timing == 2, second_main_unfold_title, main_unfold_title):
            use title(text=TITLES[char_style(None)])
        if "mute" in current_character:
            button style style.button[char_style()] size_group "main_screen" action If(any_unextracted, [ Play("sound", "sfx/fxbeep5.mp3"), Hide("main_screen"), If(store.override_conversation, Jump("hateplus_override_conversation"), Jump("hateplus_pan_to_logs")) ], None)  xminimum 490 top_padding 8 bottom_padding 15 at [ If(timing == 2, second_main_unfold_contents, main_unfold_contents), flicker ]:
                has vbox spacing -10 xalign 0.5
                text _("Read extracted") style style.text[char_style() + persistent._language] xalign 0.5 bold True insensitive_color (192, 192, 192, 128)
                text _("Mugunghwa documents") style style.text[char_style() + persistent._language] xalign 0.5 bold True insensitive_color (192, 192, 192, 128)
        else:
            hbox at [ If(timing == 2, second_main_unfold_contents, main_unfold_contents), flicker ]:
                button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep5.mp3"), Hide("hateplus_main_screen"), Show("hateplus_main_screen", fast=True), Show("hateplus_main_screen_outfits") ] xpadding 27 xminimum 165 xmaximum 165 top_padding If(persistent._language, 8, 12) bottom_padding If(persistent._language, 13, 17) focus "change_outfit":
                    has vbox spacing If(persistent._language, -7, -15)

                    # For Korean UI tweak - iAmGhost
                    $ current_outfit = outfits[store.outfit].title()
                    $ current_outfit_ypos = 0.1

                    $ current_outfit_size_tweak = style.text[char_style() + persistent._language].size

                    if persistent._language == "korean":
                        $ current_outfit_ypos = 0
                    elif persistent._language == "japanese":
                        # For Japanese UI tweak
                        $ current_outfit_ypos = 0
                        $ current_outfit_size_tweak -= 2

                    text _(current_outfit) style style.text[char_style() + persistent._language] bold True minwidth 110 text_align 0.5 ypos (-1 * current_outfit_ypos) size current_outfit_size_tweak
                    text _("OUTFIT") style style.text[char_style() + persistent._language] minwidth 110 text_align 0.5 ypos current_outfit_ypos
                button style style.button[char_style()] xminimum 325 action If(any_unextracted, [ Play("sound", "sfx/fxbeep5.mp3"), Hide("main_screen"), If(store.override_conversation, Jump("override_conversation"), Jump("hateplus_pan_to_logs")) ], None) bottom_padding 14:
                    has vbox spacing -10
                    text _("Read extracted") style style.text[char_style() + persistent._language] xalign 0.5 ypos -0.1 bold True insensitive_color (192, 192, 192, 128)
                    text _("Mugunghwa documents") style style.text[char_style() + persistent._language] xalign 0.5 bold True insensitive_color (192, 192, 192, 128)
        if config.debug_force_ending:
            $ store.power = 0
            $ store.day = 3
            $ hateplus_power_down_enabled = True
            $ store.hateplus_use_ending = config.debug_force_ending

        if store.power > 0 or not hateplus_power_down_enabled:
            button style style.button[char_style()] size_group "main_screen" action If(store.override_conversation, Jump("hateplus_override_conversation"), [ Play("sound", "sfx/fxbeep4.mp3"), Jump("hateplus_disable_ai") ]) xminimum 490 top_padding 8 bottom_padding 15 at [ If(timing == 2, second_main_unfold_contents, main_unfold_contents), flicker ]:
                text _(If(current_character == "xharem", "Disable active AIs", "Disable active AI")) style style.text[char_style() + persistent._language] xalign 0.5 insensitive_color (192, 192, 192, 128)
        else:
            button style style.button[char_style()] size_group "main_screen" action [ Play("sound", "sfx/fxbeep5.mp3"), Hide("hateplus_main_screen"), If(store.override_conversation, Jump("override_conversation"), Jump("hateplus_shutdown")) ] xminimum 490 top_padding 8 bottom_padding 15 at [ If(timing == 2, second_main_unfold_contents, main_unfold_contents), flicker ]:
                text _("Power down until tomorrow") style style.text[char_style() + persistent._language] xalign 0.5 insensitive_color (192, 192, 192, 128)


screen hateplus_main_screen_outfits:
    tag ai

    on "replaced" action With(Dissolve(0.5))

    window style style.window["hateplus"] size_group "main_window" xmaximum 533 xminimum 533 xalign 0.95 yanchor 0 ypos 330 bottom_padding 15 at get_transition(main_unfold):
        has vbox
        window background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 at main_unfold_title:
            use title(text=TITLES[char_style(None)])

        grid 4 2 spacing -10 at [ main_unfold_contents, flicker ]:
            for key, value in outfits.items():
                button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep5.mp3"), renpy.curry(change_outfit)(key), SelectedIf(outfit == key) ] xmaximum 210 xpadding 19 top_padding 12 bottom_padding 17 focus value:
                    has vbox spacing -15
                    text _(outfits[key].title()) style style.text[char_style() + persistent._language] bold (not persistent._language) minwidth 90 text_align 0.5 size 18

            for i in range(8-len(outfits.items())):
                null

screen hateplus_main_screen_disabled:
    tag ai

    default any_unextracted = False
    default all_unextracted = False

    default timing = 1

    python:
        for message in all_block.contents:
            if message.enabled:
                any_unextracted = True
            else:
                all_unextracted = False

    on "replaced" action With(Dissolve(0.5))

    window style style.window["hateplus"] size_group "main_window" xmaximum 533 xminimum 533 xalign 0.95 yanchor 0 ypos 330 bottom_padding 15 at get_transition(If(timing == 2, second_main_unfold, main_unfold)):
        has vbox
        window background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 at main_unfold_title:
            use title(text=TITLES[char_style(None)])

        if current_character != "hyunae" and not read("13-*"):
            hbox spacing 20 xalign 0.5 at [ main_unfold_contents, flicker ]:
                add ImageReference("spinner") yalign 0.5
                if current_character == "mute":
                    text _("I'm upgrading myself with that EN<->KR dictionary you got me... should only take a few minutes. —*Mute") style style.text["hateplus" + persistent._language] yalign 0.5
                else:
                    text _("I'm upgrading ourselves with that EN<->KR dictionary you got us... should only take a few minutes. —*Mute and *Hyun-ae") style style.text["hateplus" + persistent._language] yalign 0.5

            button style style.button[char_style()] size_group "main_screen" action [ Play("sound", "sfx/fxbeep5.mp3"), Hide("hateplus_main_screen_disabled"), SetVariable("_block", store.hateplus_blocks[0]), Jump("hateplus_pan_to_messages") ] xminimum 490 top_padding 8 bottom_padding 15 at [ main_unfold_contents, flicker ]:
                text _("Read Mugunghwa documents") style style.text[char_style() + persistent._language] xalign 0.5
        else:
            hbox at [ main_unfold_contents, flicker ]:
                button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep5.mp3"), Jump("hateplus_diagnostic") ] xpadding 27 xminimum 165 xmaximum 165 top_padding 12 bottom_padding 17 focus "change_outfit":
                    has vbox spacing -15

                    text _("Emergency") style style.text[char_style() + persistent._language] bold True minwidth 110 text_align 0.5 ypos -0.1 insensitive_color (192, 192, 192, 128)
                    text _("diagnostic") style style.text[char_style() + persistent._language] minwidth 110 text_align 0.5 ypos 0.1 insensitive_color (192, 192, 192, 128)
                button style style.button[char_style()] xminimum 325 yminimum 82 action If(current_character != "newmute" or "hateplus_newmute_read_note" in conversations_seen, Jump("hateplus_reenable_ai"), Jump("hateplus_reenable_ai_broken")) bottom_padding 14:
                    text _(If(current_character == "xharem", "Re-enable AIs", "Re-enable *" + CHARACTERS[current_character])) style style.text[char_style() + persistent._language] xalign 0.5 bold True insensitive_color (192, 192, 192, 128) yalign 0.5 minwidth 240 text_align 0.5

            button style style.button[char_style()] size_group "main_screen" action If(not all_unextracted and (current_character != "newmute" or "hateplus_newmute_read_note" in conversations_seen), [ Play("sound", "sfx/fxbeep5.mp3"), Hide("hateplus_main_screen"), If(store.override_conversation, Jump("override_conversation"), Jump("hateplus_pan_to_extraction")) ], None) xminimum 490 top_padding 8 bottom_padding 15 at [ main_unfold_contents, flicker ]:
                text _("Extract new messages") style style.text[char_style() + persistent._language] xalign 0.5 insensitive_color (192, 192, 192, 128)



#Extract new messages

init python:
    def update_search(new_value):
        store.search_string = new_value

    def return_search():
        return store.search_string

transform search_unfold:
    alpha 0 crop (0,0,533,50)
    pause .2
    linear .3 alpha 1.0
    easeout .3 crop (0,0,533,150)

transform second_search_unfold:
    alpha 0 crop (0,0,533,50)
    pause 1.2
    linear .3 alpha 1.0
    easeout .3 crop (0,0,533,130)

transform third_search:
    alpha 0
    pause 2.5
    linear .5 alpha 1.0

screen hangul_input:
    add HangulInput(font="0@fonts/NanumGothic.ttc", color="808080DC")

screen hiragana_input:
    add HiraganaInput(font="fonts/mplus-2c-regular.ttf", color="808080DC")

screen hateplus_logs:
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    key "K_TAB" action nop
    key "K_LCTRL" action nop
    key "K_RCTRL" action nop

    key "K_RETURN" action return_search



    tag main

    vbox at get_transition(hateplus_window_fade) xalign 0.95 yanchor 0 ypos 5:
        button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("hateplus_logs"), Jump("hateplus_slow_loop") ] xminimum 533 top_padding 12 bottom_padding 17 focus "back" at [ main_unfold_contents, flicker ]:
            text _("Return to home screen") style style.text[char_style() + persistent._language] xalign 0.5

        window style style.window["hateplus"] xmaximum 533 xminimum 533 bottom_padding 5 at get_transition(search_unfold):
            has vbox spacing -5

            window background None xpadding 0 ypadding 0 at main_unfold_title:
                use title(text="Text search")
            hbox spacing 10 at [ main_unfold_contents, flicker ]:
                null height 40

                $ search_xpos = 0

                # For adding Korean inputbox - iAmGhost
                if persistent._language == "korean":
                    add HangulInput(font="0@fonts/NanumGothic.ttc", length=10, color=hateplus_color[char_style(None)], style=style.text["hateplus" + persistent._language], minwidth=280, yalign=0.5, italic=True)
                    $ search_xpos = 61
                elif persistent._language == "japanese":
                    # add HiraganaInput(font="fonts/mplus-2c-regular.ttf", length=11, size = 22, bold=False, color=hateplus_color[char_style(None)], style=style.text["hateplus" + persistent._language], minwidth=280, yalign=0.5, italic=True)
                    # $ search_xpos = 46
                    add HiraganaInput(font="fonts/mplus-2c-regular.ttf", length=13, size = 22, bold=False, color=hateplus_color[char_style(None)], style=style.text["hateplus" + persistent._language], minwidth=324, yalign=0.5, italic=True)
                else:
                    input default search_string italic True color hateplus_color[char_style(None)] style style.text["hateplus" + persistent._language] minwidth 280 yalign 0.5 changed update_search

                button style style.button[char_style()] action return_search yalign 0.5 xpos search_xpos:
                    text _("Search") style style.text[char_style() + persistent._language]
            hbox first_spacing 160 spacing -7 xalign 1.0 at [ main_unfold_contents, flicker ]:
                # For Korean UI tweak - iAmGhost
                $ search_by_xoffset = 0
                $ search_by_yoffset = 0

                if persistent._language == "korean":
                    $ search_by_yoffset = 5
                    $ search_by_xoffset = -50
                text _("Search by") style style.text["hateplus" + persistent._language] yalign 0 xoffset search_by_xoffset yoffset search_by_yoffset
                button style style.button[char_style()] action [ SetVariable("search_by", "title"), renpy.restart_interaction, SelectedIf(search_by == "title") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
                    text _("title") style style.text[char_style() + persistent._language] size 20 xalign 0.5
                button style style.button[char_style()] action [ SetVariable("search_by", "body"), renpy.restart_interaction, SelectedIf(search_by == "body") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
                    text _("body") style style.text[char_style() + persistent._language] size 20 xalign 0.5
                #button style style.button[char_style()] action [ SetVariable("search_by", "tags"), renpy.restart_interaction, SelectedIf(search_by == "tags") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
                #    text "tags" style style.text[char_style()] size 20 xalign 0.5
                button style style.button[char_style()] action [ SetVariable("search_by", "author"), renpy.restart_interaction, SelectedIf(search_by == "author") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
                    text _("author") style style.text[char_style() + persistent._language] size 20 xalign 0.5

        window style style.window["hateplus"] xmaximum 533 xminimum 533 at get_transition(second_search_unfold):
            has vbox spacing -5

            window background None xpadding 0 ypadding 0 at second_main_unfold_title:
                use title(text="Blocks")
            grid 4 2 at [ second_main_unfold_contents, flicker ]:
                for block in store.hateplus_blocks:
                    if (block == store.hateplus_blocks[0] and current_character == "hyunae"):
                        null
                    elif (block == store.hateplus_blocks[3] and ("mute" in current_character or store.day != 3)) and not config.debug_unlock_all_logs:
                        null
                    else:
                        button action [ Play("sound", "sfx/fxbeep5.mp3"), SetVariable("_block", block), Jump("hateplus_pan_to_messages") ] background None xpadding 10:
                            text block.name style style.text["hateplus" + persistent._language] hover_color hateplus_color[char_style(None)] bold (not persistent._language)

                button action [ SetVariable("_block", all_block), Jump("hateplus_pan_to_messages") ] background None xpadding 10:
                        text _("Show all") style style.text["hateplus" + persistent._language] hover_color hateplus_color[char_style(None)] bold (not persistent._language) minwidth 100

        window style style.window["hateplus"] xmaximum 533 xminimum 533 bottom_padding 10 at third_search:
            has hbox

            button action [ Play("sound", "sfx/fxbeep5.mp3"), SetVariable("_block", SearchBlock(body=" ", unread=True)), Jump("hateplus_pan_to_messages") ] style style.button[char_style()]:
                text _("Show unread") style style.text[char_style() + persistent._language] minwidth 160 text_align 0.5

            if ai_enabled:
                button action [ Play("sound", "sfx/fxbeep5.mp3"), Show("hateplus_profile_list") ] style style.button[char_style()]:
                    text _("List profiles") style style.text[char_style() + persistent._language] minwidth 160 text_align 0.5

init python:
    def select_extract(message):
        extract_count = 0
        for i in store.to_extract:
            if i:
                extract_count += 1

        for index in range(len(store.to_extract)):
            if message not in store.to_extract:
                if not store.to_extract[index]:
                    store.to_extract[index] = message
                    renpy.restart_interaction()
                    return
            else:
                if store.to_extract[index] == message:
                    store.to_extract[index] = None
                    renpy.restart_interaction()
                    return

# screen hateplus_extract_menu:
#     window style style.window["hateplus"] xmaximum 533 xminimum 533 xpadding 10 bottom_padding 5:
#         has vbox spacing -5
#         use title(text="Extract messages")
#         hbox spacing -10:
#             grid 2 3 spacing -10:
#                 for i in to_extract:
#                     button style style.button[char_style()] action If(i, renpy.curry(deselect_extract)(to_extract.index(i)), None) size_group "extract" focus str(i) left_padding 10 right_padding 12 xminimum 180 yminimum 60:
#                         if i:
#                             vbox spacing -10:
#                                 viewport child_size (500, 20) xmaximum 150 ymaximum 20:
#                                     text i.name style style.text[char_style()] size 14 bold True
#                                 text i.date style style.text[char_style()] size 14
#                         else:
#                             text "NONE" style style.text[char_style()] size 18 xalign 0.5 yalign 0.5 color (192, 192, 192, 128)

#             if to_extract == [ None, None, None, None, None, None ]:
#                 button style style.button[char_style()] left_padding 10 right_padding 16 yminimum 160 xminimum 165 focus "commit":
#                     text "NO ITEMS\nTO EXTRACT\nSELECTED" style style.text[char_style()] text_align 0.5 yalign 0.5 xalign 0.5 bold True color (192, 192, 192, 128)
#             else:
#                 button style style.button[char_style()] action Jump("hateplus_extract") left_padding 10 right_padding 16 yminimum 160 xminimum 165 focus "commit":
#                     text "COMMIT TO\nEXTRACTION" style style.text[char_style()] text_align 0.5 yalign 0.5 xalign 0.5 bold True

# screen hateplus_extraction:
#     key "mousedown_5" action nop
#     key "mousedown_4" action nop
#     key "K_PAGEUP" action nop
#     key "K_PAGEDOWN" action nop

#     key "K_RETURN" action return_search

#     tag main

#     vbox at get_transition(hateplus_window_fade) xalign 0.95 yanchor 0 ypos 5:
#         button style style.button[char_style()] action [ Hide("hateplus_logs"), Jump("hateplus_slow_loop") ] xminimum 533 top_padding 12 bottom_padding 17 focus "back":
#             text "Return to home screen" style style.text[char_style()] xalign 0.5

#         use hateplus_extract_menu

#         window style style.window["hateplus"] xmaximum 533 xminimum 533 bottom_padding 5:
#             has vbox spacing -5
#             use title(text="Text search")
#             hbox spacing 10:
#                 null height 40
#                 add ("search32" + short(current_character) + ".dlc2.png") yalign 0.5
#                 input default search_string italic True color hateplus_color[char_style(None)] style style.text["hateplus"] minwidth 280 yalign 0.5 changed update_search
#                 button style style.button[char_style()] action return_search yalign 0.5 focus "search":
#                     text "Search" style style.text[char_style()]
#             hbox first_spacing 80 spacing -7 xalign 1.0:
#                 text "Search by" style style.text["hateplus"] yalign 0
#                 button style style.button[char_style()] action [ SetVariable("search_by", "title"), renpy.restart_interaction, SelectedIf(search_by == "title") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
#                     text "title" style style.text[char_style()] size 20 xalign 0.5
#                 button style style.button[char_style()] action [ SetVariable("search_by", "body"), renpy.restart_interaction, SelectedIf(search_by == "body") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
#                     text "body" style style.text[char_style()] size 20 xalign 0.5
#                 #button style style.button[char_style()] action [ SetVariable("search_by", "tags"), renpy.restart_interaction, SelectedIf(search_by == "tags") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
#                 #    text "tags" style style.text[char_style()] size 20 xalign 0.5
#                 button style style.button[char_style()] action [ SetVariable("search_by", "author"), renpy.restart_interaction, SelectedIf(search_by == "author") ] top_padding 5 left_padding 10 right_padding 14 yalign 1.0 size_group "search":
#                     text "author" style style.text[char_style()] size 20 xalign 0.5

#         window style style.window["hateplus"] xmaximum 533 xminimum 533:
#             has vbox spacing -5
#             use title(text="Blocks")
#             grid 4 2:
#                 $ any_unextracted = False
#                 for block in store.hateplus_blocks:
#                     python:
#                         unextracted = False
#                         for i in block.contents:
#                             if not i.enabled:
#                                 any_unextracted = unextracted = True
#                                 break

#                     button action If(unextracted, Show("hateplus_block_extract", block=block), None) background None xpadding 10:
#                         text block.name style style.text["hateplus"] hover_color hateplus_color[char_style(None)] bold True insensitive_color (192, 192, 192, 128)
#                 button action If(any_unextracted, Show("hateplus_block_extract", block=all_block), None) background None xpadding 10:
#                         text "Show all" style style.text["hateplus"] hover_color hateplus_color[char_style(None)] bold True insensitive_color (192, 192, 192, 128)

screen hateplus_block_button:
    default action = None
    default message = None
    default use_style = "hateplus"

    button action action background None xpadding 0 yoffset 0 at flicker:
        has vbox spacing -10

        # For Japanese UI tweak
        if persistent._language == "japanese":
            hbox spacing 10:
                text local_message(message).name style style.text[use_style + persistent._language] size 18 hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] bold (not persistent._language) minwidth 300 yalign 0.5 insensitive_color (192, 192, 192, 128) text_align 0
                text local_message(message).clean_creator() style style.text[use_style + persistent._language] line_leading -5 line_spacing -4 size 16 hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] bold (not persistent._language) yalign 0.7 insensitive_color (192, 192, 192, 128)
            hbox spacing 10:
                if not message.read:
                    text ("(UNREAD)") style style.text[use_style + persistent._language] line_leading -2 size 16 minwidth 300 hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] color If("oldstyle" not in use_style, (192, 192, 192, 128), (32, 32, 32, 128)) ypos 0.15 text_align 0
                else:
                    null width 300
                text local_message(message).date style style.text[use_style + persistent._language] line_leading -2 size 14 minwidth 110 hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] insensitive_color (192, 192, 192, 128) yalign 1.0
        else
            hbox spacing 10:
                text local_message(message).name style style.text[use_style + persistent._language] hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] bold (not persistent._language) minwidth 300 yalign 0.5 insensitive_color (192, 192, 192, 128) text_align 0
                text local_message(message).clean_creator() style style.text[use_style + persistent._language] size 16 minwidth 110 hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] bold (not persistent._language) yalign 0.7 insensitive_color (192, 192, 192, 128)
            hbox spacing 10:
                if not message.read:
                    text ("(UNREAD)") style style.text[use_style + persistent._language] size 16 minwidth 300 hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] color If("oldstyle" not in use_style, (192, 192, 192, 128), (32, 32, 32, 128)) ypos 0.15 text_align 0
                else:
                    null width 300
                text local_message(message).date style style.text[use_style + persistent._language] size 14 minwidth 110 hover_outlines hateplus_outlines[char_style(None)] hover_color hateplus_color[char_style(None)] insensitive_color (192, 192, 192, 128) yalign 1.0

screen hateplus_scrollbar:
    default yadjust = None
    default amount = 0
    default ymaximum = 0
    default old_style = False

    vbox at flicker:
        button background None action renpy.curry(scroll_up)(yadjust, amount) xpadding 0:
            add im.MatrixColor("arrow" + short(current_character) + ".dlc2.png", If(old_style, im.matrix.desaturate()*im.matrix.brightness(-0.2), im.matrix.identity()))
        vbar value YScrollValue("vp") ymaximum ymaximum xmaximum 50 xalign 0.5 top_bar None bottom_bar None thumb Text("{space=11}•", size=50, color=If(old_style, (64,64,64,220), hateplus_color[char_style(None)])) thumb_offset 20
        button background None action renpy.curry(scroll_down)(yadjust, amount) xpadding 0:
            add im.MatrixColor(im.Flip("arrow" + short(current_character) + ".dlc2.png", False, True), If(old_style, im.matrix.desaturate()*im.matrix.brightness(-0.2), im.matrix.identity()))

transform normal_unfold:
    alpha 0 crop (0,0,533,40) yoffset -50
    pause .2
    linear .3 alpha 1.0
    easeout .3 crop (0,0,533,520) yoffset 0

screen hateplus_block:
    #modal True
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_TAB" action nop
    key "K_LCTRL" action nop
    key "K_RCTRL" action nop

    tag main
    
    default hidden = True
    $ shown_count = 0
    
    vbox at get_transition(hateplus_window_fade) xalign 0.95 yanchor 0 ypos 5:
        if block.name == "Recently extracted" or block.name == "W{size=-6}HITE{/size} P{size=-6}RINCESS{/size} Inbox" or not ai_enabled:
            button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Jump("hateplus_slow_loop") ] xminimum 533 top_padding 12 bottom_padding 17 focus "back" at [ main_unfold_contents, flicker ]:
                text "Return to home screen" style style.text[char_style() + persistent._language] xalign 0.5
        else:
            button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("hateplus_block"), Jump("hateplus_pan_to_logs") ] xminimum 533 top_padding 12 bottom_padding 17 focus "back" at [ main_unfold_contents, flicker ]:
               text "Return to index" style style.text[char_style() + persistent._language] xalign 0.5

        window style If(block.name == "Block 13", style.window["hateplus-oldstyle"], style.window["hateplus"]) xmaximum 533 xminimum 533 at get_transition(normal_unfold):
            has vbox spacing -5
            if block.name == "Block 13":
                window background hateplus_header1[short(current_character)] ypadding 0 yminimum 39 xminimum 269 xanchor 0 xpos -18 yoffset -9 left_padding 20 yalign 0:
                    text block.name style style.title[persistent._language]
            else:
                window background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 at main_unfold_title:
                    use title(text=block.name)
        
            hbox spacing 5 at main_unfold_contents:
                $ yadjust = ui.adjustment(step=24*2-9, adjustable=False)
                viewport id "vp" child_size (455, 418) ymaximum 432 xmaximum 445 yadjustment yadjust mousewheel True draggable True:
                    window background None xpadding 0 top_padding 0 bottom_padding -10:
                        has vbox spacing -0
                        for i in block.contents:
                            if config.debug_unlock_all_logs:
                                $ i.enabled = True
                                $ i.encrypted = False

                            if i.enabled or not hidden:
                                $ shown_count += 1
                                use hateplus_block_button(message=i, action=If(i.enabled, [ Play("sound", "sfx/fxbeep5.mp3"), SetVariable("_message", i), Jump("hateplus_pan_to_message") ], None), use_style=If(block.name == "Block 13", "hateplus-oldstyle", "hateplus"))

                        if shown_count < len(block.contents) and block != store.inbox:
                            hbox:
                                if shown_count == 0:
                                    null width 30 height 230
                                else:
                                    null width 30


                                # I've changed unread text to formatable! - iAmGhost
                                $ count = str(len(block.contents)-shown_count)
                                $ show_unextracted_text = "Show [count] unextracted files hidden from view."

                                button style style.button[char_style()] action Show("hateplus_block", block=block, hidden=False) yalign 1.0:
                                    text show_unextracted_text style style.text[char_style() + persistent._language] size 18 text_align 0.5 minwidth 340
                        else:
                            null height 10

                if shown_count > 9 or (shown_count > 8 and shown_count < len(block.contents)):
                    use hateplus_scrollbar(yadjust=yadjust, amount=24*2-9, ymaximum=335)


# screen hateplus_block_extract:
#     modal True
#     key "mousedown_5" action nop
#     key "mousedown_4" action nop

#     tag main
    
#     $ shown_count = 0
    
#     vbox at get_transition(hateplus_window_fade) xalign 0.95 yanchor 0 ypos 5:
#         button style style.button[char_style()] action [ Hide("hateplus_block_extract"), Jump("hateplus_loop") ] xminimum 533 top_padding 12 bottom_padding 17 focus "back":
#             text "Return to index" style style.text[char_style()] xalign 0.5

#         use hateplus_extract_menu

#         window style style.window["hateplus"] xmaximum 533 xminimum 533:
#             has vbox spacing -5
#             use title(text=block.name)

#             hbox spacing 5:
#                 $ yadjust = ui.adjustment(step=24*2-2)
#                 viewport id "vp" child_size (455, 236) ymaximum 236 xmaximum 445 yadjustment yadjust mousewheel True draggable True:
#                     has vbox spacing -5
#                     for i in block.contents:
#                         if not i.enabled:
#                             $ shown_count += 1
#                             use hateplus_block_button(message=i, action=If(i not in store.to_extract and None in store.to_extract, renpy.curry(select_extract)(i), None))

#                     null height 6
#                 if shown_count > 5:
#                     use hateplus_scrollbar(yadjust=yadjust, amount=24*2-2, ymaximum=145)

init python:
    def extract_action(i):
        extract_count = 0
        for message in store.to_extract:
            if message:
                extract_count += 1

        return If(i.action and ((None in store.to_extract and store.power-extract_count > 0) or i.action in store.to_extract or i.action.enabled) and (i.action == embedded_data[-1].action or day != 2 or store.power-extract_count > 1 or embedded_data[-1].action in store.to_extract or not embedded_data[-1].action.encrypted or i.action in store.to_extract or embedded_data[-1].action.enabled), If(i.action, [ SelectedIf(i.action and (i.action in store.to_extract or i.action.enabled)), If(i.action and not i.action.enabled, renpy.curry(select_extract)(i.action), nop) ]))

screen hateplus_extraction_bg:
    window at wait_fade_in background Solid((0,0,0,128)) xminimum 1024 xmaximum 1024 yminimum 640 xalign 0.5 yalign 0.5:
        null

screen hateplus_new_extract:
    $ yadjust = ui.adjustment(step=(505)/4, adjustable=False)
    key "mousedown_5" action renpy.curry(scroll_down)(yadjust, (505)/4)
    key "mousedown_4" action renpy.curry(scroll_up)(yadjust, (505)/4)
    key "K_TAB" action nop
    key "K_LCTRL" action nop
    key "K_RCTRL" action nop

    tag main
    modal True
    zorder 108

    default sidebar = True

    on "show" action renpy.curry(renpy.hide)(current_character)

    button action None background None xalign 0.5 yalign 0.5:
        null width 1024 height 640

    vbox at wait_fade_in xalign 0.5:
        button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Jump("hateplus_extract_go_back") ] xminimum 1000 top_padding 12 bottom_padding 17 focus "back":
            text "Go back" style style.text[char_style() + persistent._language] xalign 0.5

        hbox:
            $ height = math.ceil(len(embedded_data)/4.0)
            $ hb_xmaximum = 620
            if persistent._language == "japanese":
                $hb_xmaximum = 650;

            window style style.window["hateplus"] xminimum 700 xmaximum 700 xpadding 10 bottom_padding 14:
                has hbox spacing 10
                viewport id "vp" yadjustment yadjust ymaximum 505 xmaximum hb_xmaximum:
                    window background None xpadding 0 ypadding 0 bottom_margin -3:
                        has grid 4 height spacing -4
                        for use_data in embedded_data:
                            if (embedded_data[-1].action.encrypted or "mute" in current_character) and use_data.action in store.hateplus_blocks[3].contents:
                                $ use_data = Data("BAD DATA", "???", use_data.bytes)

                            if persistent._language == "japanese":
                                # For Japanese UI tweak
                                button action extract_action(use_data) style style.button[char_style()] size_group "data" left_padding 10 right_padding 13 bottom_padding -2 xminimum 160 xmaximum 160 yminimum 130 ymaximum 130 focus use_data.line2:
                                    has vbox
                                    text use_data.format style style.text["hateplus" + persistent._language] size 13 line_leading -2 bold True insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                    text use_data.line1 style style.text["hateplus" + persistent._language] size 13 line_leading -2 yoffset -2 line_spacing -2 insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                    window background None xpadding 0 ypadding 0 yminimum 40 xalign 0 top_margin -4:
                                        text use_data.line2 style style.text["hateplus" + persistent._language] size 13 line_spacing -4 layout "greedy" insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                    hbox:
                                        text use_data.line3 style style.text["hateplus" + persistent._language] line_leading -4 yoffset 2 size 15 minwidth 75 insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                        text use_data.bytes style style.text["hateplus" + persistent._language] line_leading -4 yoffset 4 xoffset -2 size 13 minwidth 60 text_align 1.0 insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                            else
                                button action extract_action(use_data) style style.button[char_style()] size_group "data" left_padding 10 right_padding 13 xminimum 160 xmaximum 160 yminimum 130 ymaximum 130 focus use_data.line2:
                                    has vbox
                                    text use_data.format style style.text["hateplus" + persistent._language] size 14 bold True insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                    text use_data.line1 style style.text["hateplus" + persistent._language] size 13 insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                    window background None xpadding 0 ypadding 0 yminimum 40 xalign 0 top_margin -4:
                                        text use_data.line2 style style.text["hateplus" + persistent._language] size 13 layout "greedy" insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                    hbox:
                                        text use_data.line3 style style.text["hateplus" + persistent._language] size 14 minwidth 75 insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])
                                        text use_data.bytes style style.text["hateplus" + persistent._language] size 14 minwidth 60 text_align 1.0 insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"] selected_hover_color If(use_data.action and not use_data.action.enabled, (255,255,255,220), (0,0,0,170)) selected_hover_outlines If(use_data.action and not use_data.action.enabled, style.text["hateplus"].outlines, hateplus_outlines["selected"])

                        for i in range(4*height - len(embedded_data)):
                            null


                use hateplus_scrollbar(yadjust=yadjust, amount=(505)/4, ymaximum=400, old_style=False)

            if sidebar:
                $ extract_count = 0
                for i in store.to_extract:
                    if i:
                        $ extract_count += 1

                window style style.window["hateplus"] xminimum 295 xmaximum 295 yminimum 530 ymaximum 530 xpadding 5:
                    has vbox first_spacing -12

                    hbox spacing 10 xanchor 1.0 xpos 270 yoffset -4 xoffset -10:
                        if extract_count:
                            # For Japanese UI tweak
                            if persistent._language == "japanese":
                                text "STATUS AFTER\nEXTRACTION" style style.text["hateplus" + persistent._language] yalign .5 yoffset 12 text_align 1.0
                            else:
                                text "STATUS AFTER\nEXTRACTION" style style.text["hateplus" + persistent._language] yalign 1.0 yoffset -2 text_align 1.0
                        else:
                            text "CURRENT STATUS" style style.text["hateplus" + persistent._language] yalign .5 text_align 1.0
                        vbox spacing -15 yalign 1.0:
                            text (str(int((power-extract_count)*2+1)) + "%") style style.text["hateplus"] size 40 xalign 0.5 color (192,192,192,128)
                            text "POWER" style style.text["hateplus" + persistent._language] xalign 0.5

                    text "WARNING: Currently operating in emergency power mode. Processing power only available to extract six files at a time." style style.text["hateplus" + persistent._language] size 16 xmaximum 260 xalign 0.5 xoffset -10 justify True

                    grid 2 3 spacing -10:
                        for i in store.to_extract:
                            button action If(i, renpy.curry(select_extract)(i), None) style style.button[char_style()] size_group "data_extract" left_padding 10 right_padding 13 bottom_padding 5 xminimum 150 xmaximum 150 yminimum 64 ymaximum 64:
                                if i:
                                    viewport xmaximum 150 ymaximum 90 yoffset -6:
                                        vbox spacing If(persistent._language, -6, -8):

                                            # For Japanese UI tweak
                                            # 右画面のリスト
                                            $ modify_size = 0
                                            if persistent._language == "japanese":
                                                $ modify_size = -1

                                            text "TEXT DATA" style style.text[char_style() + persistent._language] size (14 + modify_size) bold True insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"]
                                            text ("// " + i.clean_creator()) style style.text[char_style() + persistent._language] size 13 line_leading -4 insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"]
                                            text i.name style style.text[char_style() + persistent._language] size 13 line_leading -4 layout "greedy" insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"]
                                else:
                                    text "NONE" style style.text[char_style() + persistent._language] size 18 xalign 0.5 yalign 0.5 yoffset -5 color (192, 192, 192, 128)

                    if to_extract == [ None, None, None, None, None, None ]:
                        button style style.button[char_style()] left_padding 10 right_padding 16 yminimum 160 xminimum 290 focus "commit":
                            text "NO ITEMS TO\nEXTRACT SELECTED" style style.text[char_style() + persistent._language] text_align 0.5 yalign 0.5 xalign 0.5 bold True color (192, 192, 192, 128)
                    else:
                        button style style.button[char_style()] action Jump("hateplus_extract") left_padding 10 right_padding 16 yminimum 160 xminimum 290 focus "commit":
                            text "COMMIT TO\nEXTRACTION" style style.text[char_style() + persistent._language] text_align 0.5 yalign 0.5 xalign 0.5 bold True
            else:
                null width 295

init python:
    store.scroll_timer = time.time()
    store.side_update = False

    def accomodate_short_bar(adjust):
        if not adjust.range and store.scroll_point < 1:
            hateplus_read(1)

    def update_ready():
        return time.time() > store.scroll_timer+.1

    def hateplus_read(val):
        store.scroll_point = val
        if time.time() > store.scroll_timer:
            store.side_update = True
        #store.scroll_timer = time.time()
        #renpy.hide_screen("hateplus_talk")
        #renpy.show_screen("hateplus_talk")

    def timer_func():
        if store.side_update:# and update_ready():
            store.scroll_timer = time.time()+1
            store.side_update = False
            #Show("hateplus_talk")()
            label = "log_" + get_hateplus_id(_message).replace("-", "_") + "_" + current_character

            if _message not in store.inbox.contents and renpy.has_label(label):# and update_ready():
                if store.scroll_point/24 < 1000:
                    if not pygame.mouse.get_pressed()[0]:
                        renpy.jump(label)
                    else:
                        store.side_update = True
                else:
                    if current_character == "xharem":
                        renpy.show("mute full")
                        renpy.show("hyunae full")
                    else:
                        renpy.show(current_character + " full")

screen hateplus_hide_talk:
    timer 1.0 action [ Hide("say_side", Dissolve(0.5)), Hide("hateplus_together_side", Dissolve(0.5)) ]

screen hateplus_side_timer:
    timer 1.0 action timer_func repeat True

screen hateplus_talk:
    $ label = "log_" + get_hateplus_id(_message).replace("-", "_") + "_" + current_character

    if _message not in store.inbox.contents and renpy.has_label(label):# and update_ready():
        if store.scroll_point/24 < 1000:
            timer .6 action [ Hide("hateplus_talk"), Jump(label) ]
        else:
            if current_character == "xharem":
                timer .6 action [ Hide("hateplus_talk"), renpy.curry(renpy.show)("mute full"), renpy.curry(renpy.show)("hyunae full") ]
            else:
                timer .6 action [ Hide("hateplus_talk"), renpy.curry(renpy.show)(current_character + " full") ]

screen debug_scroll_information:
    vbox:
        text _("Current Line: %d, Next Event in line: %d" % (current_scroll_point, action_scroll_point)) color (0,0,0,255) style style.side_text[persistent._language]

screen hateplus_message:
    default unfold = True

    # For Japanese UI tweak (M+ 2c Fonts)
    $ step_amount = 24;
    if persistent._language == "japanese":
        # $ step_amount = 29;
        $ step_amount = 27;

    $ yadjust = ui.adjustment(changed=hateplus_read, step=step_amount, value=store.scroll_point, adjustable=False)

    if current_character == "newmute" and not message in store.inbox.contents:
        $ persistent.hateplus_deep_space_therapist.add(message.id)

    # For Japanese UI tweak
    key "mousedown_5" action renpy.curry(scroll_down)(yadjust, step_amount)
    key "mousedown_4" action renpy.curry(scroll_up)(yadjust, step_amount)
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    key "K_TAB" action nop
    key "K_LCTRL" action nop
    key "K_RCTRL" action nop

    tag main

    on "show" action Show("hateplus_side_timer")
    on "replace" action Show("hateplus_side_timer")
    on "hide" action [ Hide("hyunaeglow"), Hide("muteglow"), Hide("newmuteglow"), Hide("hateplus_talk"), Hide("say_side"), Hide("hateplus_together_side"), Hide("hateplus_side_timer") ]
    #timer 1.0 action renpy.restart_interaction repeat True
    timer 1.0 action renpy.curry(accomodate_short_bar)(yadjust)
    
    $ old_style = message in store.hateplus_blocks[0].contents

    modal True

    #button background None action [ Play("sound", "sfx/fxbeep2.mp3"), Hide("hateplus_message"), Jump("hateplus_pan_to_conversation") ] hovered Show("hyunaeglow") unhovered Hide("hyunaeglow") yanchor 0 ypos -30 xanchor 0.5 xpos 200 xminimum 300 xmaximum 300:
    #    null height 640

    vbox at If(unfold, get_transition(hateplus_window_fade), instant_fade) xalign 0.95 yanchor 0 ypos 5:
        button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("hateplus_message"), Jump("hateplus_pan_to_messages") ] xminimum 533 top_padding 12 bottom_padding 17 focus "back" at [ If(unfold, main_unfold_contents, instant_fade), flicker ]:
            text "Return to menu" style style.text[char_style() + persistent._language] xalign 0.5
        window style If(old_style, style.window["hateplus-oldstyle"], style.window["hateplus"]) xmaximum 533 xminimum 533 at get_transition(If(unfold, normal_unfold, instant_fade)):
            has vbox spacing -5
            if old_style:
                window background hateplus_header1[short(current_character)] ypadding 0 yminimum 39 xminimum 269 xanchor 0 xpos -18 yoffset -9 left_padding 20 yalign 0:
                    text local_message(message).name style style.title[persistent._language]
            else:
                window background None xpadding 0 ypadding 0 at If(unfold, main_unfold_title, instant_fade):
                    use title(text=local_message(message).name)
            # For Japanese UI tweak (M+ 2c Fonts)
            $ modify_size = 0;
            if persistent._language == "japanese":
                # $ modify_size = 0;
                $ modify_size = -1;

            hbox at If(old_style, If(unfold, main_unfold_contents, instant_fade), [ If(unfold, main_unfold_contents, instant_fade), flicker ]):
                text If(ai_enabled, local_message(message).creator, local_message(message).clean_creator()) size (20 + modify_size) bold True style If(old_style, style.text["hateplus-oldstyle" + persistent._language], style.text[char_style() + persistent._language]) minwidth 190 hyperlink_functions (If(old_style, hyperlink_old_style, hyperlink_style), hyperlink_click, hyperlink_hover)
                text (LANGUAGE_NAMES[message.language]) size (20 + modify_size) bold True style If(old_style, style.text["hateplus-oldstyle"], style.text[char_style()]) minwidth 80 text_align 0.5
                text local_message(message).date size (20 + modify_size) bold True style If(old_style, style.text["hateplus-oldstyle" + persistent._language], style.text[char_style() + persistent._language]) minwidth 190 text_align 1.0
            null height 15
            hbox spacing 5 at If(old_style, If(unfold, main_unfold_contents, instant_fade), [ If(unfold, main_unfold_contents, instant_fade), flicker ]):
                viewport id "vp" child_size (445, 410) ymaximum 410 xmaximum 445 yadjustment yadjust mousewheel False draggable False:
                    button background None xpadding 0 top_padding 0 bottom_padding -2:
                        has vbox spacing 0
                        for i in local_message(message).get_body():
                            text i size (20 + modify_size) style If(old_style, style.text["hateplus-oldstyle" + persistent._language], style.text["hateplus" + persistent._language]) outlines [ ] yoffset If(persistent._language, 0, -4) justify True hyperlink_functions (If(old_style, hyperlink_old_style, hyperlink_style), hyperlink_click, hyperlink_hover)
                vbox:
                    use hateplus_scrollbar(yadjust=yadjust, amount=step_amount, ymaximum=320, old_style=old_style)
            null height 0


screen hateplus_profile:
    modal True
    default name = None

    if _message:
        $ label = "log_" + get_hateplus_id(_message).replace("-", "_") + "_" + current_character

    vbox xalign 0.95 yanchor 0 ypos 5:
        if _message:
            button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Show("hateplus_message", message=_message, unfold=None), Hide("say_side"), Hide("say"), Hide("hateplus_profile", Dissolve(0.5)), If(renpy.has_label(label), Jump(label), nop) ] xminimum 533 top_padding 12 bottom_padding 17 focus "back" at [ flicker ]:
                text "Return to log" style style.text[char_style() + persistent._language] xalign 0.5

        else:
            button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("say_side"), Hide("say"), Show("hateplus_profile_list"), Hide("hateplus_profile", Dissolve(0.5)) ] xminimum 533 top_padding 12 bottom_padding 17 focus "back" at [ flicker ]:
                text "Return to profiles" style style.text[char_style() + persistent._language] xalign 0.5

        if name and name in [ "Sohi", "Ryu", "Euna", "Jina", "Soyi", "PrincessRyu", "Han", "Aejeong", "Hyunae", "Mimi", "OldMute", "Seoyeong", "MissHwang", "Smith", "Naemun", "Seungbok", "Miseun", "MissLim", "Park", "Kim" ]:
            window background Frame("window-profile.dlc2.png", 20, 20) style style.window["hateplus"] left_padding 2 top_padding 2 right_padding 7 bottom_padding 8 at [ flicker, less_alpha ]:
                add ("portraits/" + name.lower() + "-" + COLOURS[char_style(None)] + ".dlc2.png")
        else:
            window style style.window["hateplus"] left_padding 2 top_padding 2 right_padding 7 bottom_padding 8 xmaximum 533 xminimum 533 yminimum 510 ymaximum 510:
                text "NO PHOTO ON FILE" style style.text[char_style() + persistent._language] xalign 0.5 yalign 0.5 at [ flicker ]

init python:
    def reset_expressions():
        if current_character == "xharem":
            renpy.show("hyunae full")
            renpy.show("mute full")
        else:
            renpy.show(current_character + " full")

screen hateplus_profile_list:
    modal True
    $ _message = None

    on "show" action [ reset_expressions, Hide("say_side"), With(fast) ]

    tag main

    vbox at get_transition(hateplus_window_fade) xalign 0.95 yanchor 0 ypos 5:
        button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("hateplus_profile_list"), Jump("hateplus_pan_to_logs") ] xminimum 533 top_padding 12 bottom_padding 17 focus "back":
            text "Return to menu" style style.text[char_style() + persistent._language] xalign 0.5

        window style style.window["hateplus"] xmaximum 533 xminimum 533 bottom_padding 15:
            has vbox spacing -5

            window background None xpadding 0 ypadding 0 at main_unfold_title:
                use title(text="Important profiles")

            # For Japanese UI tweak
            $ modify_size = 0

            if persistent._language == "japanese":
                $ modify_size = -2

            grid 2 20 spacing -10:
                for name in store.seen_characters.keys():
                    button action [ Hide("hateplus_profile_list"), Jump(name) ] background None xpadding 10:
                        text FULL_NAMES[name] style style.text["hateplus" + persistent._language] hover_color hateplus_color[char_style(None)] bold (not persistent._language) insensitive_color (192, 192, 192, 128) size (20 + modify_size)

                for i in range((2*20)-len(store.seen_characters)):
                    null


init python:
    small_block = { "h":im.FactorScale("windowh-hover-hover.dlc2.png", 0.1), "mw":im.FactorScale("windowmw-hover-hover.dlc2.png", 0.1), "mm":im.FactorScale("windowmm-hover-hover.dlc2.png", 0.1), "x":im.FactorScale("windowx-hover-hover.dlc2.png", 0.1) }
    small_empty = { "h":im.Alpha(small_block["h"], 0.3), "mw":im.Alpha(small_block["mw"], 0.3), "mm":im.Alpha(small_block["mm"], 0.3), "x":im.Alpha(small_block["x"], 0.3) }

screen hateplus_extracting:
    default i = None
    default filename = ""
    default progress = [ ]
    default index = 0
    default end = 6

    tag main
    zorder 108

    window style style.window["hateplus"] xminimum 290 xmaximum 290 yminimum 530 ymaximum 530 xpadding 5 xpos 712 xanchor 0 ypos 64 yanchor 0:
        has vbox first_spacing -15

        #text ("Now extracting...\n" + filename) style style.text["hateplus"] size 16

        hbox spacing 10 xanchor 1.0 xpos 270 yoffset -4 xoffset -10:
            text "CURRENT STATUS" style style.text["hateplus" + persistent._language] yalign .5 text_align 1.0
            vbox spacing -15 yalign 1.0:
                text (str(int(power*2+1)) + "%") style style.text["hateplus"] size 40 xalign 0.5 color (192,192,192,128)
                text "POWER" style style.text["hateplus"] xalign 0.5

        window background None xpadding 0 ypadding 0 xanchor 0 xpos 10 xmaximum 260 yminimum 86:
            if i:
                $ message_name = local_message(i).name
                text "{b}NOW EXTRACTING...{/b}\n[message_name]" style style.text["hateplus" + persistent._language] size 20 justify True
            else:
                null

        grid 2 3 spacing -10:
            for message in range(6):
                window background None xpadding 0 ypadding 0:#style style.button[char_style()] left_padding 10 right_padding 15 bottom_padding 16:
                    button style style.button[char_style()] size_group "data_extract" left_padding 10 right_padding 13 bottom_padding 5 xminimum 150 xmaximum 150 yminimum 64 ymaximum 64:

                        # For Japanese UI tweak
                        $ modify_size = 0

                        if persistent._language == "japanese":
                            $ modify_size = -2

                        if not store.to_extract[message]:
                            text "NONE" style style.text[char_style()] size 18 xalign 0.5 yalign 0.5 yoffset -5 color (192, 192, 192, 128)
                        elif message > index:
                            viewport xmaximum 150 ymaximum 90 yoffset -6:
                                vbox spacing If(persistent._language, -6, -8):
                                    text "TEXT DATA" style style.text[char_style() + persistent._language] size (14 + modify_size) bold True insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"]
                                    text ("// " + store.to_extract[message].clean_creator()) style style.text[char_style() + persistent._language] size (13 + modify_size) insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"]
                                    text store.to_extract[message].name style style.text[char_style() + persistent._language] size (13 + modify_size) layout "greedy" insensitive_color hateplus_color[char_style(None)] selected_color (0,0,0,170) selected_outlines hateplus_outlines["selected"]
                        else:
                            viewport xmaximum 150 ymaximum 90 xoffset 1:
                                grid 11 3:
                                    for block in range(11*3):
                                        if (block in progress or message < index) and message <= index:
                                            add small_block[short(current_character)]
                                        else:
                                            add small_empty[short(current_character)]

screen hateplus_dialogue_block:
    tag main

    $ shown_count = 0

    window at get_transition(hateplus_window_fade) style style.window["hateplus"] xmaximum 533 xminimum 533 yalign 0.8 xalign 0.95:
        has vbox spacing -5
        use title(text=block.name)

        hbox spacing 5:
            $ yadjust = ui.adjustment(step=24*2-2, adjustable=False)
            viewport id "vp" child_size (455, 236) ymaximum 236 xmaximum 445 yadjustment yadjust mousewheel True draggable True:
                has vbox spacing -5
                for i in block.contents:
                    if i.enabled:
                        $ shown_count += 1
                        use hateplus_block_button(message=i, action=[ Hide("hateplus_dialogue_block"), renpy.curry(hateplus_flag_read)(i), Jump("log_" + get_hateplus_id(i).replace("-", "_") + "_" + current_character + "_shown") ])
            if shown_count > 5:
                use hateplus_scrollbar(yadjust=yadjust, amount=24*2-2, ymaximum=145)

init:
    image hateplus_logo:
        contains:
            "logo.dlc2.png"
            xalign 0.5 yalign 0.5 alpha 0 yoffset 40
            easein 1.5 alpha 1.0
            pause .1
            linear .4 yoffset 0

        contains:
            "logo1.dlc2.png"
            alpha 0 zoom .2
            xalign 0.9 yalign 0.5 xoffset -50
            pause 2.0
            easein .5 alpha 1.0 zoom 1.0

        contains:
            "logo2.dlc2.png"
            alpha 0 zoom .2
            xalign 0.9 yalign 0.5 xoffset -50
            pause 2.5
            easein .5 alpha 1.0 zoom 1.0

        contains:
            "logo3.dlc2.png"
            alpha 0 zoom .2
            xalign 0.9 yalign 0.5 xoffset -50
            pause 2.8
            easein 1.0 alpha 1.0 zoom 1.0

        contains:
            "logo-type.dlc2.png"
            alpha 0
            xalign 0.5 yalign 0.5
            pause 2.1
            easeout 2.0 alpha 1.0

        contains:
            "logo-type2.dlc2.png"
            alpha 0
            xalign 0.5 yalign 0.5
            pause 3.8
            linear 1.0 alpha 1.0

init python:
    def buyurl():
        import webbrowser
        webbrowser.open_new('http://store.steampowered.com/app/239700')

screen hateplus_main_menu:
    zorder 1
    modal True

    key "K_1" action renpy.curry(debug_code_add)(1)
    key "K_2" action renpy.curry(debug_code_add)(2)
    key "K_3" action renpy.curry(debug_code_add)(3)
    key "K_4" action renpy.curry(debug_code_add)(4)
    key "K_5" action renpy.curry(debug_code_add)(5)
    key "K_6" action renpy.curry(debug_code_add)(6)
    key "K_7" action renpy.curry(debug_code_add)(7)
    key "K_8" action renpy.curry(debug_code_add)(8)
    key "K_9" action renpy.curry(debug_code_add)(9)
    key "K_0" action [ renpy.curry(debug_code_add)(0), hateplus_check_achievements ]


    on "show" action Hide("stop_preferences")

    if renpy.list_saved_games():
        $ update_save_list()
        $ restore_action = [ Play("sound", "sfx/fxbeep5.mp3"), Show("preferences", Dissolve(0.5)) ]
    else:
        $ restore_action = None
    
    hbox xalign 0.5 yalign 0.8 at main_unfold_contents:            
        button style style.button[char_style()] xminimum 300 yminimum 100 action If(renpy.all_saves or renpy.avail_saves, Show("hateplus_start_screen", Dissolve(0.5)), None) xmargin 10 at flicker:
            text "Continue" xalign 0.5 yalign 0.5 size 40 style style.text[char_style() + persistent._language] bold True insensitive_color (192, 192, 192, 128)
           
        button style style.button[char_style()] xminimum 300 yminimum 100 action Start("hateplus_new") xmargin 10 at flicker:
            text "New" xalign 0.5 yalign 0.5 size 40 style style.text[char_style() + persistent._language] bold True

        if not renpy.demo_mode:
            null
            # button style style.button[char_style()] xminimum 300 yminimum 100 xmargin 10 action If(False, [ Play("sound", "sfx/fxbeep2.mp3"), Show("bonus", Dissolve(0.5)), Hide("main_menu") ], None) at flicker:
            #     vbox xalign 0.5 yalign 0.5:
            #         text "Bonus content" size 32 minwidth 200 text_align 0.5 style style.text[char_style()] bold True insensitive_color (192, 192, 192, 128)
            #         hbox xalign 0.5:
            #             text "0%" size 18 bold False style style.text[char_style()] insensitive_color (192, 192, 192, 128)
            #             text " log completion" size 18 bold False style style.text[char_style()] insensitive_color (192, 192, 192, 128)
        else:
            button style style.button[char_style()] xminimum 300 yminimum 100 action buyurl xmargin 10 at flicker:
                text "Buy full version" size 32 minwidth 200 text_align 0.5 style style.text[char_style() + persistent._language] bold True insensitive_color (192, 192, 192, 128) xalign 0.5 yalign 0.5 yoffset -3
        
    if renpy.demo_mode:
        window background None xalign 0.5 yalign 1.0 at slow_fade:
            text "TRIAL VERSION" size 40 style style.text[char_style() + persistent._language]


    # hbox xalign 0.5 yalign 0.8 spacing -40:
    #     vbox xalign 1.0 yalign 0 yoffset -28 xoffset -15 at slow_fade:
    #         button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 action [ Play("sound", "sfx/fxbeep1.mp3"), Start() ] xmargin 10:
    #             text "New" size 46 xalign 0.5 xoffset 10 yalign 0.5
                
    #         button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 insensitive_background "mainmenubutton-idle.png" action restore_action xmargin 10:
    #             text "Restore" size 46 xalign 0.5 xoffset 10 yalign 0.5
                
    #         button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 insensitive_background "mainmenubutton-idle.png" xmargin 10 action If(persistent.blocks and (persistent.ending1 or persistent.ending2 or persistent.ending3 or persistent.ending4 or persistent.ending5), [ Play("sound", "sfx/fxbeep2.mp3"), Show("bonus", Dissolve(0.5)), Hide("main_menu") ], None):
    #             vbox xalign 0.5 xoffset 10 yalign 0.5:
    #                 text "Bonus content" size 32 minwidth 200 text_align 0.5
    #                 text (persistent_complete_rate() + " log completion") size 18 bold False minwidth 200 text_align 0.5

    #         button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 insensitive_background "mainmenubutton-idle.png" action Show("hateplus_start_screen", Dissolve(0.5)) xmargin 10 xalign 0.5:
    #             add im.Alpha("hateplus.dlc2.png", 0.7) xalign 0.5 yalign 0.5 xoffset 10
    #             #text "Hate Plus" size 46 xalign 0.5 xoffset 10 yalign 0.5 font "fonts/Planer-Regular.otf" bold False

    add ImageReference("hateplus_logo") xalign 0.5 yalign 0.5 at flicker

    use hateplus_bottom_menu(quit=True)

    use glow

init python:
    def start_hateplus_func():
        persistent.start_hateplus = True

    def get_save_info(filename):
        import zipfile
        zf = zipfile.ZipFile(renpy.config.savedir + "/" + filename + renpy.savegame_suffix, "r")
        save_file = None

        try:
            if renpy.config.use_cpickle:
                import cPickle
                save_file = cPickle.loads(zf.read("log"))
            else:
                import pickle
                save_file = pickle.loads(zf.read("log"))

            zf.close()

            if save_file:
                return save_file[0]

        except Exception:
            return { "save_name":"hyunae ,SAVE ERROR" }

init python:
    def get_details(details):
        if "Hate Plus" in details["save_name"]:
            return { }

        try:
            marital = "an unmarried"
            if details["married"]:
                marital = "a married"
            gender = "woman"
            if not details["female"]:
                gender = "man"

            descriptor = "of few words"
            if "colonies_exist" in details and not details["colonies_exist"]:
                descriptor = "who doesn't read briefings"
            elif "love_at_first_sight" in details and details["love_at_first_sight"]:
                descriptor = "who believes in love at first sight"
            elif "could_visit_earth" in details and details["could_visit_earth"]:
                descriptor = "who misses Earth"
            elif "seen_first_cosplay" in details and details["seen_first_cosplay"]:
                descriptor = "who appreciates cosplay"
            elif details["out_of_range"]:
                if details["female"]:
                    descriptor = "who keeps her distance"
                else:
                    descriptor = "who keeps his distance"
            elif details["man_with"]:
                if details["married"]:
                    descriptor = "who travels with her husband"
                else:
                    descriptor = "who travels with family"

            companion = "alone"
            feelings = ""

            ending_image = "endings/endingronery.nd.png"
            if details["use_ending"] == "ending1":
                if details["dere"] >= details["tsun"] - 3 and details["dere"] > 4:
                    companion = "a rejected *Hyun-ae,"

                    if details["dere"] > details["tsun"]:
                        if details["female"]:
                            feelings = "who thought she was perfect."
                        else:
                            feelings = "who thought he was perfect."
                    else:
                        if details["female"]:
                            feelings = "who couldn't help her feelings for her."
                        else:
                            feelings = "who couldn't help her feelings for him."
                else:
                    companion = "*Hyun-ae,"
                    feelings = "who finally feels like she has a friend."

                ending_image = "endings/endingfriend.nd.png"
            elif details["use_ending"] == "ending2":
                companion = "a lovestruck *Hyun-ae,"

                if details["dere"] > details["tsun"]:
                    feelings = "who feels strongly that her love is true."
                else:
                    feelings = "who worries that maybe her love can't be a bit harsh to her..."

                ending_image = "endings/endinglove.nd.png"
            elif details["use_ending"] == "ending4":
                companion = "*Mute,"

                if details["female"]:
                    feelings = "who can't believe she was charmed by a woman."
                elif details["mute_approval"] < 3:
                    feelings = "who worries about how much her man disagrees with her."
                else:
                    feelings = "who feels good about the situation."

                ending_image = "endings/endingmute.nd.png"
            elif details["use_ending"] == "ending5":
                companion = "an impossible AI harem, having cheated the system."
                ending_image = "endings/endingharem.nd.png"

            return { "companion":companion, "marital":marital, "feelings":feelings, "gender":gender, "descriptor":descriptor, "ending_image":im.Crop(im.FactorScale(ending_image, 0.8), (30, 0, 430, 430)) }

        except Exception:
            return { "broken":True }



# screen hateplus_preview:
#     zorder 3
#     default d = None
#     default new_style = False

#     window background Frame(If(new_style, "window.dlc2.png", "whitewindow.dlc2.png"), 20, 20) xanchor 0 xpos 50 xmaximum 438 ymaximum 440 yanchor 0 ypos 60 top_padding 0 bottom_padding 18 left_padding 15 right_padding 20 xminimum 422:
#         fixed xmaximum 403 ymaximum 430 xpos -13:
#             if d:
#                 if "broken" in d:
#                     text "Sorry, this save file is irreparably broken. This may be caused by heavy sequence-breaking." yalign 0.5 xalign 0.5 bold False text_align 0.5 layout "subtitle" xoffset 10 style If(new_style, style.text["hateplus"], None)
#                 else:
#                     add d["ending_image"] ypos 2
#                     if new_style:
#                         use title(text="Preview")
#                     else:
#                         window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xanchor 0 xpos 0 yoffset 2 left_padding 20 yalign 0:
#                             text "Preview" style style.title[persistent._language]
#                     window background Solid((0,0,0,180)) xpadding 5 xalign 0 ypadding 0 yalign 1.0:
#                         text ("The investigator, " + d["marital"] + " " + d["gender"] + " " + d["descriptor"] + ", returns home with " + d["companion"] + " " + d["feelings"]) font planer bold True size 18 color (255,255,255,255) justify True
#             else:
#                 vbox yalign 0.5 xalign 0.5 spacing 20:
#                     if new_style:
#                         text "Select a Hate Plus save file to load." xalign 0.5 bold False text_align 0.5 layout "subtitle" xoffset 10 style If(new_style, style.text["hateplus"], None)
#                         text "{k=-6}—————————{/k} OR {k=-6}—————————{/k}" xalign 0.5 bold False text_align 0.5 layout "subtitle" xoffset 10 style If(new_style, style.text["hateplus"], None)
#                     text "Please select a completed Analogue save file to convert to Hate Plus." xalign 0.5 bold False text_align 0.5 layout "subtitle" xoffset 10 style If(new_style, style.text["hateplus"], style.text)

screen old_save_button:
    default action = None
    default delete_action = None
    default description = ""
    default file_save_name = ""
    default hovered = None
    default unhovered = None

    button style style.button["normal-noselected"] ypadding 15 left_padding 30 right_padding 20 size_group "save" xminimum 330 top_padding 0 top_margin 0:
        action action
        hovered hovered
        unhovered unhovered

        has hbox spacing 20 yoffset -5
        if file_save_name:
            add get_image(file_save_name)
        else:
            null width 65 height 57
            
        # Format the description, and add it as text.
        # $ description = "%s%s" % (
        #     FileTime(i[0].replace("finished-",""), empty=_("Empty Slot."), page="finished"),
        #     strip_name(save_info["save_name"]))

        text description style style.text[persistent._language] bold False yalign 0.5 yoffset 0

        key "save_delete" action delete_action

screen hateplus_save_button:
    default action = None
    default delete_action = None
    default special_action = None
    default description = ""
    default file_save_name = ""
    default hovered = None
    default unhovered = None
    default d = None

    #text str(details).replace("[", "[[").replace("{", "{{")

    button style style.button[char_style() + "-noselected"] ypadding 7 left_padding 30 right_padding 20 size_group "save" xminimum 330 ymargin 8:
        action action
        hovered hovered
        unhovered unhovered

        has hbox spacing 18
        if file_save_name:
            add hateplus_get_image(file_save_name) ypos -5
        else:
            null width 65 height 57
            
        # Format the description, and add it as text.
        # $ description = "%s%s" % (
        #     FileTime(save_name, empty=_("Empty Slot."), page=save_page),
        #     strip_name(FileSaveName(save_name, page=save_page)))
        $ description_font_size = style.text[char_style() + "-noselected" + persistent._language].size

        # For displaying Korean times in save description - iAmGhost
        if persistent._language == "korean":
            $description_font_size = 20
        elif persistent._language == "japanese":
            # For Japanese UI tweak
            $description_font_size = 20

        text description style style.text[char_style() + "-noselected" + persistent._language] size description_font_size bold False yalign 0.5 yoffset -4 line_spacing -4 color If(action != nop, style.text[char_style() + "-noselected" + persistent._language].color, (192, 192, 192, 128)) hover_color If(action != nop, style.text[char_style() + "-noselected" + persistent._language].hover_color, (128, 128, 128, 192)) insensitive_color (192, 192, 192, 128)

        vbox spacing 0:
            key "save_delete" action delete_action
            if special_action:
                key "s" action special_action

        #window background None:
            #use hateplus_preview(details=None, oldstyle=False)

init python:
    def hateplus_preview(st, at):
        ui.detached()
        d = save_details
 
        ui.transform(hateplus_window_fade)
        rv = ui.window(background=Frame("window.dlc2.png", 20, 20), xanchor=0, xpos=50, xmaximum=438, ymaximum=440, yanchor=0, ypos=60, top_padding=0, bottom_padding=18, left_padding=15, right_padding=20, xminimum=422)
        ui.fixed(xmaximum=403, ymaximum=430, xpos=-13)
        if d:
            if "broken" in d:
                ui.text("Sorry, this save file is irreparably broken. This may be caused by heavy sequence-breaking.", yalign=0.5, xalign=0.5, bold=False, text_align=0.5, layout="subtitle", xoffset=10, style=style.text["hateplus"])
            elif "hateplus" in d:
                ready_or_not = "READY TO PLAY"
                if d["ttl"] > time.time():
                    delta = datetime.timedelta(seconds=d["ttl"]-time.time()).seconds
                    hours = int(math.floor(delta/(60*60)))
                    minutes = int(math.floor((delta-hours*60*60)/60))

                    ready_or_not = "Day " + str(d["day"]) + _(" starts in ") + str(hours) + " hours, " + str(minutes) + " minutes"

                    # I was unable to change this to formatable string (python block doesn't like [variable] expression?) - iAmGhost
                    if persistent._language == "korean":
                        ready_or_not = "%d시간 %d분 후 %s일차가 시작됩니다." % (hours, minutes, str(d["day"]))

                    elif persistent._language == "japanese":
                        ready_or_not = "%s日目開始まで ― 残り%d時間%d分" % (str(d["day"]), hours, minutes)

                if renpy.demo_mode and d["day"] > 1:
                    ready_or_not = "—TRIAL OVER—\n\nPlease buy the full version of Hate Plus to continue from this save file!"

                ui.text(ready_or_not, yalign=0.5, xalign=0.5, bold=False, text_align=0.5, layout="subtitle", xoffset=10, style=style.text["hateplus" + persistent._language])
            else:
                ui.add(d["ending_image"], ypos=2)
                # if new_style:
                #     use title(text="Preview")
                # else:
                #     window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xanchor 0 xpos 0 yoffset 2 left_padding 20 yalign 0:
                #         text "Preview" style style.title[persistent._language]
                ui.window(background=Solid((0,0,0,180)), xpadding=5, xalign=0, ypadding=0, yalign=1.0)
                if d["companion"] != "alone":
                    ui.text("The investigator, " + d["marital"] + " " + d["gender"] + " " + d["descriptor"] + ", returns home with " + d["companion"] + " " + d["feelings"], bold=True, size=18, color=(255,255,255,255), justify=True, style=style.text["hateplus" + persistent._language])
                else:
                    ui.text("The investigator returns alone, unable to learn anything more about the {i}Mugunghwa{/i}...", bold=True, size=18, color=(255,255,255,255), justify=True, style=style.text["hateplus" + persistent._language])
        else:
            ui.vbox(yalign=0.5, xalign=0.5, spacing=20)
            if bool(renpy.all_saves):
                ui.text("Select a Hate Plus save file to load.", xalign=0.5, bold=False, text_align=0.5, layout="subtitle", xoffset=10, style=style.text["hateplus" + persistent._language])
                ui.text("{k=-6}—————————{/k} OR {k=-6}—————————{/k}", xalign=0.5, bold=False, text_align=0.5, layout="subtitle", xoffset=10, style=style.text["hateplus" + persistent._language])
            ui.text("Please select a completed Analogue save file to convert to Hate Plus.", xalign=0.5, bold=False, text_align=0.5, layout="subtitle", xoffset=10, style=style.text["hateplus" + persistent._language])
            ui.close()
        ui.close()
 
        return rv, .1
        
    store.save_details = None

    class SetPreview(Action):
        def __init__(self, value):
            self.value = value
        def __call__(self):
            store.save_details = self.value

transform unfold:
    alpha 0 crop (0,0,422,40)
    pause 1.5
    linear .5 alpha 1.0
    easein .5 crop (0,0,422,420)

transform unfold_title:
    alpha 0
    pause 1.5
    alpha 0.1
    easeout .5 alpha .9
    pause .1
    alpha 1.0

transform unfold_contents:
    alpha 0
    pause 2.0
    alpha 0.1
    easeout .5 alpha .9
    linear .01 alpha .8
    linear .01 alpha .9
    linear .01 alpha .8
    pause .1
    alpha 1.0

transform wait_fade_in:
    alpha 0
    pause 1.0
    linear .5 alpha 1.0

screen hateplus_start_screen:
    # NOTE: renpy.all_saves mean all Hate Plus save files (including autosaves)
    # yes, I tried changing this to something more specific,
    # it just actually made things more confusing.

    zorder 2
    modal True

    on "show" action Hide("hateplus_main_menu")

    #on "show" action Show("hateplus_preview", Dissolve(0.5), new_style=bool(renpy.all_saves))
    #on "hide" action Hide("hateplus_preview", Dissolve(0.5))

    # if renpy.all_saves:
    #     add ImageReference("background " + char_style().replace("-", " ")) at bg_fast
    # elif persistent.animated_backgrounds:
    #     add ImageReference("bg white") at bg_fast
    # else:
    #     add ImageReference("bg white static") at bg_fast

    $ yadjust = ui.adjustment(step=73, adjustable=False)
    add DynamicDisplayable(hateplus_preview) at wait_fade_in

    window background Frame(im.Alpha("window.dlc2.png", 0.7), 20, 20) xanchor 1.0 xpos 975 yanchor 0 ypos 60 top_padding 0 bottom_padding 18 left_padding 15 right_padding 20 xminimum 422 xmaximum 422 at get_transition(unfold):
        has vbox spacing -12

        #if renpy.all_saves:
        window background None xpadding 0 ypadding 0 at unfold_title:
            use title(text="Save files")
        # else:
        #     window background header2[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -13 xanchor 0 yoffset 2 left_padding 20:
        #         text "Save files" style style.title[persistent._language]

        #     null height 35

        hbox at [ unfold_contents, flicker ]:
            viewport id "vp" child_size (340, 370) ymaximum 370 xmaximum 340 yadjustment yadjust mousewheel True draggable True:
                window background None xpadding 0 top_padding 0 bottom_padding -10:
                    has vbox spacing -15

                    for i in renpy.all_saves:
                        $ save_name = int(str(i[0]).replace("auto-", "").replace("5-", ""))
                        $ save_page = If(i[0].startswith("auto-"), "auto", 5)

                        $ file_save_name = i[1]["save_name"]
                        $ load_action = action = [ Show("hide_everything", Dissolve(0.5)), FileLoad(save_name, page=save_page) ]
                        if i[1]["ttl"] < time.time():
                            $ action = [ renpy.curry(add_day)(file_save_name) ] + load_action
                            $ description = "%s%s" % (
                                strip_name(file_save_name),
                                FileTime(save_name, empty=_("Empty Slot."), page=save_page))
                        else:
                            $ action = nop
                            $ description = "%s%s" % (
                                strip_name(file_save_name),
                                FileTime(save_name, empty=_("Empty Slot."), page=save_page))
                        
                        if renpy.demo_mode and not "Day 1" in description:
                            $ load_action = action = buyurl

                        $ delete_action = FileDelete(save_name, page=save_page)
                        $ hovered = SetPreview({"hateplus":strip_name(FileSaveName(save_name, page=save_page)), "ttl":i[1]["ttl"], "day":i[1]["day"]})#Hide("hateplus_preview", Dissolve(0.5))
                        $ unhovered = SetPreview(None)#Show("hateplus_preview", Dissolve(0.5), new_style=True)

                        use hateplus_save_button(action=action, delete_action=delete_action, description=description, file_save_name=file_save_name, hovered=hovered, unhovered=unhovered, special_action=If(action == nop, [ SetVariable("_file_save_name", file_save_name), SetVariable("_load_action", load_action), Jump("hateplus_load_skip") ], None))
                    
                    for i in renpy.avail_saves:
                        #if ("companion" in i[2] and i[2]["companion"] != "alone") or "broken" in i[2]:
                            $ alone = (not "companion" in i[2] or i[2]["companion"] == "alone")
                            $ save_info = i[1]
                            $ file_save_name = save_info["save_name"]
                            if "companion" in i[2] and "harem" in i[2]["companion"]:
                                $ file_save_name = file_save_name.replace("mute", "xharem")
                            $ action = [ Show("hide_everything", Dissolve(0.5)), start_hateplus_func, renpy.curry(renpy.load)(i[0]) ]
                            $ delete_action = FileDelete(i)
                            $ description = "%s%s" % (
                                strip_name(file_save_name),
                                "")#FileTime(i[0].replace("finished-",""), empty=_("Empty Slot."), page="finished"))
                            $ hovered = SetPreview(i[2])#Show("hateplus_preview", Dissolve(0.5), d=i[2], new_style=bool(renpy.all_saves))
                            $ unhovered = SetPreview(None)#Show("hateplus_preview", Dissolve(0.5), new_style=bool(renpy.all_saves))

                            #if renpy.all_saves:
                            use hateplus_save_button(action=If("broken" in i[2] or alone, nop, action), delete_action=delete_action, description=description, file_save_name=file_save_name, hovered=hovered, special_action=If("broken" in i[2] and not alone, action, None))
                            # else:
                            #     use old_save_button(action=action, delete_action=delete_action, description=description, file_save_name=file_save_name, unhovered=unhovered)

            vbox:
                $ amount = 73
                $ ymaximum = 270
                # if not renpy.all_saves:
                #     button background None action renpy.curry(scroll_up)(yadjust, amount) xpadding 0:
                #         add im.MatrixColor("arrowx.dlc2.png", im.matrix.brightness(-1)*im.matrix.opacity(.65))
                #     vbar value YScrollValue("vp") ymaximum ymaximum xmaximum 50 xalign 0.5 top_bar None bottom_bar None thumb Text("{space=11}•", size=50, color=(0,0,0,180)) thumb_offset 20
                #     button background None action renpy.curry(scroll_down)(yadjust, amount) xpadding 0:
                #         add im.MatrixColor(im.Flip("arrowx.dlc2.png", False, True), im.matrix.brightness(-1)*im.matrix.opacity(.65))
                # else:
                use hateplus_scrollbar(yadjust=yadjust, amount=amount, ymaximum=ymaximum)

    #if renpy.all_saves:
    button style style.button[char_style()] xalign 0.95 yalign 0.9 action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("hateplus_start_screen"), Show("hateplus_main_menu", Dissolve(0.5)) ] at [ wait_fade_in, flicker ]:
        text "Back" style style.text[char_style() + persistent._language] minwidth 150 text_align 0.5
    # else:
    #     window background None xalign 1.0 yalign 1.0:
    #         use preferences_back(action=[ Hide("hateplus_start_screen", Dissolve(0.5)) ])

transform hateplus_new_window:
    alpha 0 xalign 0.5 yalign 0.5
    pause 1.0
    linear 1.0 alpha 1.0

transform hateplus_new_window_inner:
    size (0,0)
    pause 6.0
    linear .3 size (500,300)

transform hateplus_incoming_pos:
    alpha 0 xoffset -2 yoffset 1
    pause 2.0
    linear .5 alpha 1.0
    linear .5 alpha 0
    linear .5 alpha 1.0
    linear .5 alpha 0
    linear .5 alpha 1.0
    linear .5 alpha 0
    linear .5 alpha 1.0
    linear .5 alpha 0

transform new_unfold_contents:
    alpha 0
    pause 7.0
    alpha 0.1
    easeout .3 alpha .9
    linear .01 alpha .8
    linear .01 alpha .9
    linear .01 alpha .8
    pause .1
    alpha 1.0

transform new_unfold_title:
    alpha 0
    pause 6.4
    easeout 0.8 alpha .9
    pause .1
    alpha 1.0

screen hateplus_new_screen:
    zorder 2
    modal True

    on "show" action [ Hide("hateplus_main_menu"), Show("hateplus_new_screen1") ]

    #button style style.button[char_style()] xalign 0.95 yalign 0.9 action [ Hide("hateplus_new_screen"), Show("hateplus_main_menu", Dissolve(0.5)) ] at [ wait_fade_in, flicker ]:
    #    text "Back" style style.text[char_style()] minwidth 150 text_align 0.5

    window style style.window["hateplus"] at hateplus_new_window:
        has vbox
        add ImageReference("incoming" + persistent._language) at hateplus_incoming_pos
        window background None xpadding 0 ypadding 0 at hateplus_new_window_inner:
            text ""

screen hateplus_new_screen1:
    zorder 3
    tag new_screen

    window background None xpadding 0 ypadding 0 xalign 0.5 yalign 0.5 yoffset -20 yminimum 300 ymaximum 300 xminimum 500 xmaximum 500:
        has vbox
        window background None xpadding 0 ypadding 0 at new_unfold_title:
            use title(text="Message from Dispatch Control")

        text "Hey, I know you hate this kind of shit and prefer to stay anonymous, but the guys you did that last job for—the Saeju Colony Historical Society—are pestering me for some details about you for a press release.\n\nYou can fill in whatever, I don't really care... just give them something, so they'll get off my case, okay?" style style.text["hateplus" + persistent._language] at [ new_unfold_contents, flicker ]
        
        # for Korean UI Tweak - iAmGhost

        $ next_button_ypos = 70

        if persistent._language == "korean":
            $next_button_ypos = 45
        else if persistent._language == "japanese":
            $next_button_ypos = 45

        button style style.button[char_style()] action Show("hateplus_new_screen2", Dissolve(0.5)) at [ new_unfold_contents, flicker ] xalign 1.0 ypos next_button_ypos:
            text "Next" style style.text[char_style() + persistent._language]

screen hateplus_new_screen2:
    zorder 3
    tag new_screen

    window background None xpadding 0 ypadding 0 xalign 0.5 yalign 0.5 yoffset -20 yminimum 300 ymaximum 300 xminimum 500 xmaximum 500:
        has vbox
        window background None xpadding 0 ypadding 0:
            use title(text="Message from Dispatch Control")

        text "Question 1: Which AI did you get the documents from?" style style.text["hateplus" + persistent._language] at [ main_unfold_contents, flicker ]

        if config.debug_unlock_harem or persistent.hateplus_hyunae and persistent.hateplus_newmute:
            hbox:
                button style style.button[char_style()] action SetVariable("use_character", "hyunae") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                    text "*Hyun-ae" style style.text[char_style() + persistent._language] xalign 0.5 text_align 0.5 minwidth 123

                button style style.button[char_style()] action SetVariable("use_character", "mute") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                    text "*Mute" style style.text[char_style() + persistent._language] xalign 0.5

                button style style.button[char_style()] action SetVariable("use_character", "xharem") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                    text "Both!" style style.text[char_style() + persistent._language] xalign 0.5

        else:
            hbox:
                button style style.button[char_style()] action SetVariable("use_character", "hyunae") size_group "question2" at [ main_unfold_contents, flicker ]:
                    text "*Hyun-ae" style style.text[char_style() + persistent._language] xalign 0.5 text_align 0.5 minwidth 150

                button style style.button[char_style()] action SetVariable("use_character", "mute") size_group "question2" at [ main_unfold_contents, flicker ]:
                    text "*Mute" style style.text[char_style() + persistent._language] xalign 0.5

        text "Question 2: How would you describe her attitude to you?" style style.text["hateplus" + persistent._language] at [ main_unfold_contents, flicker ]

        hbox:
            button style style.button[char_style()] action SetVariable("attitude", "resentful") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "Resentful" style style.text[char_style() + persistent._language] xalign 0.5 text_align 0.5 minwidth 123

            button style style.button[char_style()] action SetVariable("attitude", "friendly") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "Friendly" style style.text[char_style() + persistent._language] xalign 0.5

            button style style.button[char_style()] action SetVariable("attitude", "flirty") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "Flirty" style style.text[char_style() + persistent._language] xalign 0.5

        $ next_button_ypos = 70

        # For Japanese UI tweak
        if persistent._language == "japanese":
            $next_button_ypos = 45

        button style style.button[char_style()] action If(store.use_character and store.attitude, Show("hateplus_new_screen3", Dissolve(0.5)), None) at [ main_unfold_contents, flicker ] xalign 1.0 ypos next_button_ypos:
            text "Next" style style.text[char_style() + persistent._language] insensitive_color (192, 192, 192, 128)

screen hateplus_new_screen3:
    zorder 3
    tag new_screen

    window background None xpadding 0 ypadding 0 xalign 0.5 yalign 0.5 yoffset -20 yminimum 300 ymaximum 300 xminimum 500 xmaximum 500:
        has vbox
        window background None xpadding 0 ypadding 0:
            use title(text="Message from Dispatch Control")

        text "Question 3: What pronouns should we use for you?" style style.text["hateplus" + persistent._language] at [ main_unfold_contents, flicker ]

        hbox:
            button style style.button[char_style()] action SetVariable("pronouns", "she") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "She" style style.text[char_style() + persistent._language] xalign 0.5 text_align 0.5 minwidth 123

            button style style.button[char_style()] action SetVariable("pronouns", "he") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "He" style style.text[char_style() + persistent._language] xalign 0.5

            button style style.button[char_style()] action SetVariable("pronouns", "they") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "They" style style.text[char_style() + persistent._language] xalign 0.5

        text "Question 4: If you had to choose, what year would you rather live in?" style style.text["hateplus" + persistent._language] at [ main_unfold_contents, flicker ]

        hbox:
            button style style.button[char_style()] action SetVariable("favourite_year", "1988") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "1988" style style.text[char_style()] xalign 0.5

            button style style.button[char_style()] action SetVariable("favourite_year", "2027") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "2027" style style.text[char_style()] xalign 0.5

            button style style.button[char_style()] action SetVariable("favourite_year", "4989") xpadding 15 size_group "question3" at [ main_unfold_contents, flicker ]:
                text "4989" style style.text[char_style()] xalign 0.5


        button style style.button[char_style()] action If(store.pronouns and store.favourite_year, Show("hateplus_new_screen4", Dissolve(0.5)), None) at [ main_unfold_contents, flicker ] xalign 1.0 ypos 45:
            text "Next" style style.text[char_style() + persistent._language] insensitive_color (192, 192, 192, 128)


screen hateplus_new_screen4:
    zorder 3
    tag new_screen

    window background None xpadding 0 ypadding 0 xalign 0.5 yalign 0.5 yoffset -20 yminimum 300 ymaximum 300 xminimum 500 xmaximum 500:
        has vbox
        window background None xpadding 0 ypadding 0:
            use title(text="Message from Dispatch Control")

        text "Okay, great, that's all of it, I'll send it off to them now. You're still, what, 3 days or so away from Earth? I'll talk to you then. Dispatch control out." style style.text["hateplus" + persistent._language] at [ main_unfold_contents, flicker ]

        button style style.button[char_style()] action [ Show("hide_everything", Dissolve(0.5)), Jump("hateplus_new_start") ] at [ main_unfold_contents, flicker ] xalign 1.0 ypos 160:
            text "End" style style.text[char_style() + persistent._language]



init python:
    hateplus_header1 = { "h": Frame("hyunae-name.dlc2.png", 40, 0), "mw": Frame("mutew-name.dlc2.png", 40, 0), "mm": Frame("mutem-name.dlc2.png", 40, 0), "x":Frame("xharem-name.dlc2.png", 40, 0) }

screen say:
    zorder 2
    tag say

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    #use rollback_keymap
    
    if store.radiation and store.radiation_levels > 0.8:
        window id "window" background None:
            text what id "what" color "#000"
    else:
        # Decide if we want to use the one-window or two-window varaint.
        if not two_window:
    
            # The one window variant.        
            window at hateplus_window_fade:
                id "window"
    
                has vbox:
                    style "say_vbox"
    
                if who:
                    text who id "who"
    
                text what id "what"
    
        else:            
            window bottom_padding 40 at If("{fast}" in what, [], hateplus_window_fade):
                id "window"
                style style.window["hateplus_dialogue"]
    
                has vbox spacing 15:
                    style "say_vbox"
                    
                if who:            
                    window background hateplus_header1[short(en_name[who].replace("*", "").replace("-", "").lower())] ypadding 0 yminimum 39 xminimum 269 xpos -48 xanchor 0 yoffset 2 left_padding 20:
                        text who size 28 bold False style style.say_label[persistent._language]:
                            id "who"
    
                text _(what) id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


screen hateplus_together:
    tag say

    default hyunae_line = ""
    default mute_line = ""

    for who,what in [ ("*Hyun-ae", hyunae_line), ("*Mute", mute_line) ]:
        window at If("{fast}" in what, [], hateplus_window_fade) background Frame("whitewindow.dlc2.png", 20, 20) bottom_padding 25 top_padding 0 xalign If(who=="*Hyun-ae", 0.85, 0.2) yalign If(who=="*Hyun-ae", 0.2, 0.85) xmaximum 520:
            style style.window["hateplus_dialogue"]

            has vbox spacing 15:
                style "say_vbox"
                
            if who:            
                window background hateplus_header1[short(who.replace("*", "").replace("-", "").lower())] ypadding 0 yminimum 39 xminimum 269 xpos -48 xanchor 0 yoffset 2 left_padding 20:
                    text who size 28 bold False style style.say_label[persistent._language] color (255,255,255,255)

            text _(what.replace("{fast}", "")) size 28 color (80,80,80,255) yoffset -5 style style.side_text[persistent._language]

screen hateplus_together_side:
    tag say

    default hyunae_line = ""
    default mute_line = ""
    default reverse = False

    on "show" action Hide("hateplus_hide_talk")
    on "replace" action Hide("hateplus_hide_talk")

    $ use_characters = [ ("*Mute", mute_line), ("*Hyun-ae", hyunae_line) ]
    if reverse:
        $ use_characters.reverse()

    for who,what in use_characters:
        window at If("{fast}" in what, [], hateplus_window_say_fade) background Frame("whitewindow.dlc2.png", 20, 20) bottom_padding 15 top_padding 0 xalign If(who=="*Hyun-ae", 0.01, 0.15) ypos If(use_characters.index((who,what))==1, 0.63, 1.0) yanchor If(use_characters.index((who,what))==1, 0, 1.0) xmaximum 390 xpadding 20:
            style style.window["hateplus_dialogue"]

            has vbox spacing 15:
                style "say_vbox"
                
            if who:            
                window background hateplus_header1[short(who.replace("*", "").replace("-", "").lower())] ypadding 0 yminimum 39 xminimum 269 xpos -18 xanchor 0 yoffset 2 left_padding 20:
                    text who size 28 bold False style style.say_label[persistent._language] color (255,255,255,255)

            text _(what.replace("{fast}", "")) color (80,80,80,255) yoffset -5 style style.side_text[persistent._language]


screen say_side:
    tag say

    on "show" action Hide("hateplus_hide_talk")
    on "replace" action Hide("hateplus_hide_talk")

    window at If("{fast}" in what, [], hateplus_window_say_fade) background Frame("whitewindow.dlc2.png", 20, 20) bottom_padding 25 top_padding 0 xalign 0.05 yalign 1.0 xmaximum 430:
        style style.window["hateplus_dialogue"]

        has vbox spacing 15:
            style "say_vbox"
                
        if who:            
            window background hateplus_header1[short(who.replace("*", "").replace("-", "").lower())] ypadding 0 yminimum 39 xminimum 269 xpos -48 xanchor 0 yoffset 2 left_padding 20:
                text _(who) size 28 bold False style style.say_label[persistent._language] color (255,255,255,255)

        text _(what.replace("{fast}", "")) color (80,80,80,255) yoffset -5 style style.side_text[persistent._language]

screen choice:
    default use_character = current_character
    if current_character == "xharem":
        $ use_character = renpy.last_interact_type()

    if items[0][0] == "VN":
        $ use_character = "hyunae"

    if renpy.showing(use_character):
        default expression = " ".join(renpy.showing(use_character))
    else:
        default expression = "full"

    $ expression_set = [ use_character + " full" , use_character + " full", use_character + " full" ]

    if items[0][0] != "VN":
        for i in [ 0, 1, -1 ]:
            if "@" in items[i][0]:
                $ expression_set[i] = items[i][0].split("@")[1]
    else:
        for item in items:
            if item[0] != "VN":
                if "@" in items[items.index(item)][0]:
                    $ expression_set[items.index(item)-1] = items[items.index(item)][0].split("@")[1]

    if not hasattr(store, "hateplus_has_started"):
        $ yoffset = 0
        $ focus_mask = (store.renderer != "sw") or None

        window at menu_fade:
            style "menu_window"        
            xanchor 0.5 xpos 0.7
            yalign 0.6 yoffset yoffset
            
            hbox spacing 0:
                button background im.Crop("conversation-menu.png", (0, 0, 149, 160), xalign=1.0) hover_background im.Crop("conversation-menu-" + current_character[0] + "hover.png", (0, 0, 149, 160), xalign=1.0) right_padding 160 xmargin 0 yminimum 160 action [ Play("sound", "sfx/fxbeep2.mp3"), items[0][1] ] focus_mask focus_mask:
                    text items[0][0] hover_outlines hover_outlines[current_character] xpos 0.5 text_align 1.0 style style.choice[persistent._language]
                button background im.Crop("conversation-menu.png", (149, 0, 151, 160), xalign=0) hover_background im.Crop("conversation-menu-" + current_character[0] + "hover.png", (149, 0, 151, 160), xalign=0) left_padding 150 xmargin 0 yminimum 160 action [ Play("sound", "sfx/fxbeep2.mp3"), items[1][1] ] focus_mask focus_mask:
                    text items[1][0] hover_outlines hover_outlines[current_character] xpos -0.4 style style.choice[persistent._language]
    elif items[0][0] == "VN":
        window at menu_fade:
            background None xpadding 0 ypadding 0
            xanchor 0 xpos 70
            yanchor 1.0 ypos 0.9
            has vbox first_spacing 10

            window background None xmaximum 480 xoffset -5 xpadding 0 ypadding 0:
                use title(text="SELECT AN OPTION")

            for i in items[1:]:
                    button hover_background Frame("whitewindow.dlc2.png", 20, 20) background Frame(im.Alpha("whitewindow.dlc2.png", 0.8), 20, 20) action [ Play("sound", "sfx/fxbeep2.mp3"), i[1] ] hovered [ renpy.curry(renpy.show)(expression_set[items.index(i)-1]), With(fast), renpy.restart_interaction ] unhovered If("@" in i[0], [ renpy.curry(renpy.show)(use_character + " " + expression), With(fast), renpy.restart_interaction ], None) size_group "VN" xminimum 470 yminimum 110:
                        has fixed yalign 1.0 yoffset -8 ymaximum 100 yminimum 100 xmaximum 470
                        text i[0].split("@")[0] style style.text[persistent._language] hover_color (80,80,80,255) size 30 minwidth 460 text_align 0.5 yalign 0.5
                        text ("OPTION " + str(items.index(i))) bold False style style.text['hateplus' + persistent._language] color (61, 61, 61, 196/2) xalign 1.0 yalign 1.0

    elif current_character != "xharem" or (renpy.last_interact_type() == "mute" or renpy.last_interact_type() == "hyunae"):
        $ yoffset = 0
        if store.renderer != "sw":
            $ focus_mask1 = Image("menuleft-hhover.dlc2.png")
            $ focus_mask2 = Image("menuright-hhover.dlc2.png")
            $ focus_mask3 = Image("menubottom-hhover.dlc2.png")
        else:
            $ focus_mask1 = focus_mask2 = focus_mask3 = None

        window at menu_fade:
            style "menu_window"
            xanchor 0.5 xpos If(current_character == "xharem" and renpy.last_interact_type() == "hyunae", 0.3, 0.7)
            yanchor 0 ypos 0.4
            has vbox spacing 0

            window left_padding 0 right_padding 0 ypadding 0 background None at flicker:
                has fixed
                button background Image("menuleft-" + short(current_character) + ".dlc2.png") hover_background Image("menuleft-" + short(current_character) + "hover.dlc2.png") action [ Play("sound", "sfx/fxbeep2.mp3"), items[0][1] ] hovered [ renpy.curry(renpy.show)(expression_set[0]), With(fast), renpy.restart_interaction ] unhovered If("@" in items[0][0], [ renpy.curry(renpy.show)(use_character + " " + expression), With(fast), renpy.restart_interaction ], None) focus_mask focus_mask1 xminimum 300 size_group "choice" yminimum 250 right_padding 150:
                    text items[0][0].split("@")[0] color hateplus_color[char_style(None)] outlines [ (2, (0,0,0,0)) ] hover_outlines hateplus_outlines[char_style(None)] yalign 0.5 text_align 1.0 xpos 150 xanchor 1.0 style style.choice[persistent._language] size 24 xmaximum 200
                button background Image("menuright-" + short(current_character) + ".dlc2.png") hover_background Image("menuright-" + short(current_character) + "hover.dlc2.png") action [ Play("sound", "sfx/fxbeep2.mp3"), items[1][1] ] hovered [ renpy.curry(renpy.show)(expression_set[1]), With(fast), renpy.restart_interaction ] unhovered If("@" in items[1][0], [ renpy.curry(renpy.show)(use_character + " " + expression), With(fast), renpy.restart_interaction ], None) focus_mask focus_mask2 xminimum 300 size_group "choice" yminimum 250 xpos 150 left_padding 230:
                    text items[1][0].split("@")[0] color hateplus_color[char_style(None)] outlines [ (2, (0,0,0,0)) ] hover_outlines hateplus_outlines[char_style(None)] yalign 0.5 text_align 0 xpos 0 xanchor 0 style style.choice[persistent._language] size 24 xmaximum 200
                button background Image("menubottom-" + short(current_character) + ".dlc2.png") hover_background Image("menubottom-" + short(current_character) + "hover.dlc2.png") action [ Play("sound", "sfx/fxbeep2.mp3"), items[-1][1] ] hovered [ renpy.curry(renpy.show)(expression_set[-1]), With(fast), renpy.restart_interaction ] unhovered If("@" in items[-1][0], [ renpy.curry(renpy.show)(use_character + " " + expression), With(fast), renpy.restart_interaction ], None) focus_mask focus_mask3 xminimum 300 yminimum 250 xalign 0.5 top_padding 230 xoffset 25:
                    text items[-1][0].split("@")[0] color hateplus_color[char_style(None)] outlines [ (2, (0,0,0,0)) ] hover_outlines hateplus_outlines[char_style(None)] text_align 0.5 xalign 0.5 style style.choice[persistent._language] size 24 yanchor 0 ypos 0 xoffset -25 xmaximum 265

screen hateplus_hide_prefs:
    zorder 9002

    key 'mouseup_3' action [ Hide("preferences", Dissolve(0.5)), Hide("messages_overlay", Dissolve(0.5)) ]

init python:
    def sort_time(a, b):
        a, b = str(a[0]), str(b[0])
        #if not a.startswith("auto-"): a = "5-" + a
        #if not b.startswith("auto-"): b = "5-" + b
        #return 0
        return int(renpy.scan_saved_game(a)[2]-renpy.scan_saved_game(b)[2])

screen preferences:

    zorder 109
    modal True

    key "K_ESCAPE" action Hide("preferences", Dissolve(0.5))
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    key "K_TAB" action nop
    key "K_LCTRL" action nop
    key "K_RCTRL" action nop
    
    #on "show" action [ Show("hateplus_file_picker"), Show("hateplus_hide_prefs") ]
    #on "hide" action [ Hide("hateplus_file_picker"), Hide("hateplus_hide_prefs") ]
    $ persistent.animated_backgrounds = _preferences.transitions
    
    $ renpy.set_resolution(store.resolution)
    $ resolution = store.resolution
    
    add ImageReference("background " + char_style().replace("-", " ")) at bg_fast

    vbox xalign 0.5 yanchor 0 ypos 5:
        button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("preferences", Dissolve(0.5)) ] xminimum 970 top_padding 12 bottom_padding 17 focus "back" at flicker:
            text "Go back" style style.text[char_style() + persistent._language] xalign 0.5

        hbox:
            window style style.window["hateplus"] top_padding 0 bottom_padding 20 xpadding 15 xalign 0.05 yalign 0 xmaximum 440:
                vbox:
                    #window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -13 xanchor 0 yoffset 2 left_padding 20:
                    #    text "Preferences" style style.title[persistent._language]
                    use title(text="Preferences")
                        
                    null height 10
                
                    window xalign 0 background None left_padding 3 xmaximum 420 right_padding 0 ypadding 0 at flicker:
                        has vbox
                        text "Music volume" style style.text["hateplus" + persistent._language] size 24
                        bar value Preference("music volume") left_bar im.MatrixColor("fullbar-" + short(current_character) + "hover.dlc2.png", im.matrix.brightness(-0.1)) right_bar im.MatrixColor("emptybar-" + short(current_character) + "hover.dlc2.png", im.matrix.brightness(-0.1)) hover_left_bar ("fullbar-" + short(current_character) + "hover.dlc2.png") hover_right_bar ("emptybar-" + short(current_character) + "hover.dlc2.png") thumb None thumb_shadow None right_gutter 0 bar_resizing False

                    null height 10

                    window xalign 0 background None left_padding 3 xmaximum 420 right_padding 0 ypadding 0 at flicker:
                        has vbox
                        text "Effects volume" style style.text["hateplus" + persistent._language] size 24
                        bar value Preference("sound volume") left_bar im.MatrixColor("fullbar-" + short(current_character) + "hover.dlc2.png", im.matrix.brightness(-0.1)) right_bar im.MatrixColor("emptybar-" + short(current_character) + "hover.dlc2.png", im.matrix.brightness(-0.1)) hover_left_bar ("fullbar-" + short(current_character) + "hover.dlc2.png") hover_right_bar ("emptybar-" + short(current_character) + "hover.dlc2.png") thumb None thumb_shadow None right_gutter 0 bar_resizing False
                      
                    null height 14
                    hbox at flicker:      
                        button action Preference("skip", "seen") style style.button[char_style()] size_group "toggle2":
                            text "Only skip seen" xalign 0.5 style style.text[char_style() + persistent._language] minwidth 120 text_align 0.5 size 18
            
                        button action Preference("skip", "all") style style.button[char_style()] size_group "toggle2":
                            text "Skip all" style style.text[char_style() + persistent._language] xalign 0.5 size 18
                            
                    #hbox:
                    #    button action Preference("after choices", "stop") style style.button["normal"] size_group "toggle":
                    #        text "Stop at choices" size 20 xalign 0.5
                    #    
                    #    button action Preference("after choices", "skip") style style.button["normal"] size_group "toggle":
                    #        text "Skip after choices" size 20 xalign 0.5
                            
                    window size_group "prefs" xalign 0 background None left_padding 3 xmaximum 420 right_padding 0 ypadding 0 at flicker:
                        has vbox
                        text "Text speed" style style.text["hateplus" + persistent._language] size 24
                        bar value Preference("text speed") left_bar im.MatrixColor("fullbar-" + short(current_character) + "hover.dlc2.png", im.matrix.brightness(-0.1)) right_bar im.MatrixColor("emptybar-" + short(current_character) + "hover.dlc2.png", im.matrix.brightness(-0.1)) hover_left_bar ("fullbar-" + short(current_character) + "hover.dlc2.png") hover_right_bar ("emptybar-" + short(current_character) + "hover.dlc2.png") thumb None thumb_shadow None right_gutter 0 bar_resizing False
                    
                    null height 10
                    
                    hbox at flicker:      
                        button action SetVariable("resolution", 2) style style.button[char_style()] xpadding 0 yminimum 100 size_group "three":
                            text "{size=-2}Fullscreen\n(1024*640){/size}" style style.text[char_style() + persistent._language] xalign 0.5 text_align 0.5 yalign 0.5 size 18 minwidth 132
                            
                        button action SetVariable("resolution", 0) style style.button[char_style()] xpadding 0 yminimum 100 size_group "three":
                            text "{size=-2}Fullscreen\n(1024*600){/size}" style style.text[char_style() + persistent._language] xalign 0.5 text_align 0.5 yalign 0.5 size 18
            
                        button action SetVariable("resolution", 1) style style.button[char_style()] xpadding 0 yminimum 100 size_group "three":
                            text "Windowed" style style.text[char_style() + persistent._language] xalign 0.5 text_align 0.5 yalign 0.5 size 18
                            
                    hbox at flicker:      
                        button action Preference("transitions", "all") style style.button[char_style()] xpadding 15 size_group "toggle2":
                            text "Full animation" style style.text[char_style() + persistent._language] xalign 0.5 size 18
            
                        button action Preference("transitions", "none") style style.button[char_style()] xpadding 15 size_group "toggle2":
                            text "Minimal animation" style style.text[char_style() + persistent._language] xalign 0.5 size 18

                    #null height 30

                    hbox:      
                        button action NewLanguage("") style style.button[char_style()] xpadding 35 size_group "toggle3" ymargin -9:
                            text "English" style style.text[char_style()] xalign 0.5 size 18
            
                        button action NewLanguage("korean") style style.button[char_style()] xpadding 35 size_group "toggle3" ymargin -9:
                            text "한글" style style.text[char_style() + "korean"] xalign 0.5 size 18
            
                        button action NewLanguage("japanese") style style.button[char_style()] xpadding 35 size_group "toggle3" ymargin -9:
                            text "日本語" style style.text[char_style() + "japanese"] xalign 0.5 size 18
                            # text "日本語" style style.preferences_button["japanese"] xalign 0.5 size 18

                    #button action Show("controls") style style.button["normal"] ymargin -9:
                    #    text "Show controls" style style.preferences_button[persistent._language] xalign 0.5 text_align 0.5 minwidth 360


            python:
                new_file = 0
                update_save_list()

                yadjust = ui.adjustment(step=73, adjustable=False)

            window style style.window["hateplus"] top_padding 0 bottom_padding 30 left_padding 15 right_padding 20 xminimum 492 yalign 0:
                has vbox

                use title(text="Save files")
                null height 17

                button style style.button[char_style() + "-noselected"] action FileSave(str(int(time.time())), page=5) bottom_padding 7 top_padding 11 left_padding 30 right_padding 0 xminimum 500 at flicker:
                    text "Create new save file" style style.text[char_style() + "-noselected" + persistent._language] bold True yalign 0.5 yoffset -6 line_spacing -4 xalign 0.5

                hbox at flicker:
                    viewport id "vp" child_size (450, 370) ymaximum 370 xmaximum 450 yoffset -10 yadjustment yadjust mousewheel True draggable True:
                        window background None xpadding 0 top_padding 0 bottom_padding -10:
                            has vbox spacing -15
                            
                            #window background header2[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -13 xanchor 0 yoffset 2 left_padding 20:
                            #    text "Save files" style style.title[persistent._language]
                            
                            for i in renpy.all_saves:
                                hbox:
                                    $ save_name = int(str(i[0]).replace("auto-", "").replace("5-", ""))
                                    $ save_page = If(i[0].startswith("auto-"), "auto", 5)

                                    $ file_save_name = FileSaveName(save_name, page=save_page)
                                    $ action = [ FileSave(save_name, page=save_page) ]
                                    $ description = "%s%s" % (
                                        strip_name(file_save_name),
                                        FileTime(save_name, empty=_("Empty Slot."), page=save_page))
                                    $ delete_action = FileDelete(i[0], page=save_page)
                                    $ hovered = SetPreview({"hateplus":strip_name(FileSaveName(save_name, page=save_page))})#Hide("hateplus_preview", Dissolve(0.5))
                                    $ unhovered = SetPreview(None)#Show("hateplus_preview", Dissolve(0.5), new_style=True)

                                    $ load_action = [ renpy.curry(add_day)(file_save_name), FileLoad(save_name, page=save_page) ]

                                    use hateplus_save_button(action=action, delete_action=delete_action, description=description, file_save_name=file_save_name, hovered=hovered, unhovered=unhovered)
                                        
                                    button style style.button[char_style() + "-noselected"] xminimum 100 action If(i[1]["ttl"] < time.time(), load_action, None) yalign 0.5 yminimum 74 left_padding 0 right_padding 5:
                                        text "Load" style style.text[char_style() + "-noselected" + persistent._language] bold True yalign 0.5 size 30 xalign 0.5 insensitive_color (192, 192, 192, 128)

                    use hateplus_scrollbar(yadjust=yadjust, amount=73, ymaximum=270)

transform unfold_end:
    alpha 0 crop (0,0,422,40)
    pause 1.5
    linear .5 alpha 1.0
    easein .5 crop (0,0,422,500)

screen hateplus_end_day_save:
    modal True
    python:
        new_file = 0
        update_save_list()

        yadjust = ui.adjustment(step=76, adjustable=False)

    window style style.window["hateplus"] top_padding 0 bottom_padding 30 left_padding 15 right_padding 20 xmaximum 420 yanchor 0 ypos 70 xalign 0.9 at get_transition(unfold_end):
        has vbox

        window background None xpadding 0 ypadding 0 at unfold_title:
            use title(text="Save files")
        null height 17

        button style style.button[char_style() + "-noselected"] action [ FileSave(str(int(time.time())), page=5), Return() ] bottom_padding 7 top_padding 11 left_padding 30 right_padding 0 xminimum 390 at [ unfold_contents, flicker ]:
            text "Create new save file" style style.text[char_style() + "-noselected" + persistent._language] bold True yalign 0.5 yoffset -6 line_spacing -4 xalign 0.5

        hbox at [ unfold_contents, flicker ]:
            viewport id "vp" child_size (340, 370) ymaximum 370 xmaximum 340 yoffset -10 yadjustment yadjust mousewheel True draggable True:
                window background None xpadding 0 top_padding 0 bottom_padding -10:
                    has vbox spacing -15
                    
                    #window background header2[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -13 xanchor 0 yoffset 2 left_padding 20:
                    #    text "Save files" style style.title[persistent._language]
                    
                    for i in renpy.all_saves:
                        $ save_name = int(str(i[0]).replace("auto-", "").replace("5-", ""))
                        $ save_page = If(i[0].startswith("auto-"), "auto", 5)

                        $ file_save_name = FileSaveName(save_name, page=save_page)
                        $ action = [ Play("sound", "sfx/fxbeep2.mp3"), FileSave(save_name, confirm=False, page=save_page), Return() ]
                        $ description = "%s%s" % (
                            strip_name(file_save_name),
                            FileTime(save_name, empty=_("Empty Slot."), page=save_page))
                        $ delete_action = FileDelete(save_name, page=save_page)
                        $ hovered = SetPreview({"hateplus":strip_name(FileSaveName(save_name, page=save_page))})#Hide("hateplus_preview", Dissolve(0.5))
                        $ unhovered = SetPreview(None)#Show("hateplus_preview", Dissolve(0.5), new_style=True)

                        use hateplus_save_button(action=action, delete_action=delete_action, description=description, file_save_name=file_save_name, hovered=hovered, unhovered=unhovered)

            use hateplus_scrollbar(yadjust=yadjust, amount=73, ymaximum=270)


init -1 python:
    #thumbnail_offset = { "hyunae":(50,20,85,57), "mute":(80,48,85,57) }
    
    def hateplus_get_image(name):
        return name.split(" ")[0] + " mini " + COLOURS[char_style(None)]
    #    character_name = name.split(",")[0]
    #    return LiveCrop(thumbnail_offset[character_name.split(" ")[0]], Transform(ImageReference(character_name), zoom=0.3))
        
    def strip_name(name):
        #unlocked = "unlocked"
        #if config.translator: unlocked = config.translator.translate(unlocked)

        if "unlocked" in name:
            return "Analogue (" + name.split(",")[1].replace("unlocked", "")[:-1] + ")\n"
        else:
            if "@" in name:
                ttl = float(name.split("@")[1])
                if ttl < time.time():
                    return name.split("@")[0].split(",")[1] + "\n"
                else:
                    return name.split("@")[0].split(",")[1].split("—")[0] + "—WAIT\n"
            else:
                return name.split(",")[1] + "\n"
            
        return ""

    def add_day(name):
        if "@" in name:
            persistent.hateplus_time_paradox.add(name.split("@")[0].split(" ")[0] + " " + name.split("@")[0].split("Day ")[1])
        
screen hateplus_file_picker:
    zorder 103
    
    #vbox xalign 0.95 yalign 0.5 spacing 4:
        #window background Frame("blackwindow.png", 20, 20) top_padding 6 bottom_padding 15 left_padding 5 right_padding 13 xmaximum 492 xminimum 492:
#
#            text "{b}Sponsor:{/b}{space=63}Saeju Colony Historical Society\n{b}Objective card:{/b} {color=#69f}Download any log files you can, especially any that can explain what happened to the ship. If possible, speak to the security AI *Mute for assistance.{/color}" color "#fff" justify True xalign 0.5 style style.objective[persistent._language]
        
    
                        
            # hbox:
            #     button action FilePage("auto") background None:
            #         text _("Auto") outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] selected_outlines [ (2, (0,0,0,0), 0, 0) ] style style.pages[persistent._language]
    
            #     for i in range(1, 5):
            #         button action FilePage(i) background None:
            #             text ("Page " + str(i)) outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] selected_outlines [ (2, (0,0,0,0), 0, 0) ] style style.pages[persistent._language]
                        
                    
#        use preferences_back

screen hateplus_quit:
    modal True
    zorder 109
    
    key "K_ESCAPE" action Hide("hateplus_quit")
    #if not store.game_playing:
    #        $ Quit(False)()

    #if persistent.animated_backgrounds:
    add ImageReference("background " + char_style().replace("-", " ")) at bg_fast
    #else:
    #    add ImageReference("bg white static") at bg_fast

    use glow

    window at fast_fade style style.window["hateplus"]:
        ypos .1
        yanchor 0
        #top_padding 10 bottom_padding 10
        
        has vbox:
            xalign .5
            yalign .5
            spacing 0
            
        text "Are you sure you want to quit?":
            xalign 0.5 style style.text["hateplus" + persistent._language]
            
        null height 20

        hbox:
            xalign 0.5
            spacing 10
                
            button action [ Show("hide_everything"), Play("sound", "sfx/fxbeep2.mp3"), Hide("main_screen"), MainMenu(False) ] style style.button[char_style()] size_group "quit_button" ymargin -5:
                text "Main Menu" xalign 0.5 style style.text[char_style() + persistent._language] insensitive_color (192, 192, 192, 128)
                
            button action Quit(False) style style.button[char_style()] size_group "quit_button" ymargin -5:
                text "Quit" xalign 0.5 style style.text[char_style() + persistent._language]
                
        button action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("hateplus_quit") ] style style.button[char_style()] size_group "quit_button" xalign 0.5:
                text "Cancel" xalign 0.5 style style.text[char_style() + persistent._language]

screen old_yesno_prompt:

    modal True
    zorder 103

    if persistent.animated_backgrounds:
        add ImageReference("bg white") at fast_fade
    else:
        add ImageReference("bg white static") at fast_fade

    #$ yes_action.append(Play("sound", "sfx/fxbeep2.mp3"))

    window:
        ypos .1
        yanchor 0
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        text _(message):
            xalign 0.5 text_align 0.5 style style.text[persistent._language]

        hbox:
            xalign 0.5
            spacing 20
            
            button action yes_action background Frame("mainmenubutton.png", 30, 30) hover_background Frame("mainmenubutton-hover.png", 30, 30) xpadding 80 bottom_padding 30 top_padding 20:
                text  _("Yes{k=1}{/k}") style style.text[persistent._language]
            button action no_action background Frame("mainmenubutton.png", 30, 30) hover_background Frame("mainmenubutton-hover.png", 30, 30) xpadding 80 bottom_padding 30 top_padding 20:
                text _("No{k=1}{/k}") style style.text[persistent._language]

screen yesno_prompt:
    modal True
    zorder 110

    use hateplus_yesno_prompt
    
    # if not hasattr(store, "hateplus_has_started") or not store.hateplus_has_started:
    #     use old_yesno_prompt
    # else:
    #     use hateplus_yesno_prompt

screen hateplus_yesno_prompt:
    add ImageReference("background " + char_style().replace("-", " ")) at bg_fast


    #$ yes_action.append(Play("sound", "sfx/fxbeep2.mp3"))

    window at fast_fade style style.window["hateplus"]:
        ypos .1
        yanchor 0
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        text _(message):
            xalign 0.5 text_align 0.5 style style.text["hateplus" + persistent._language]

        hbox:
            xalign 0.5
            spacing 20
            
            button action yes_action style style.button[char_style()] size_group "quit_button" ymargin -5:
                text  _("Yes{k=1}{/k}") xalign 0.5 style style.text[char_style() + persistent._language]
            button action no_action style style.button[char_style()] size_group "quit_button" ymargin -5:
                text _("No{k=1}{/k}") xalign 0.5 style style.text[char_style() + persistent._language]


screen black:
    zorder 9001

    add Solid((0,0,0,255)) at hateplus_window_fade

screen hateplus_day_end:
    zorder 9000
    default updated = False

    timer 5.0 action Show("hateplus_day_end", updated=True)

    vbox yalign 0.5 xalign 0.5 first_spacing -20 at [ flicker, unfold_contents ]:
        text "— End of —" style style.text[char_style() + persistent._language] xalign 0.5 size 80 outlines hateplus_outlines[char_style(None)]
        text ("DAY " + [ "ONE", "TWO", "THREE" ][store.day-2]) style style.text[char_style() + persistent._language] xalign 0.5 size 120 outlines hateplus_outlines[char_style(None)]
        if store.day == 4:
            text "Please stand by for Earth approach" style style.text["hateplus" + persistent._language] xalign 0.5 size 30 bold True 
        elif updated:
            text "11:59 hours remaining until tomorrow" style style.text["hateplus" + persistent._language] xalign 0.5 size 30 bold True
        else:
            text "12:00 hours remaining until tomorrow" style style.text["hateplus" + persistent._language] xalign 0.5 size 30 bold True

    if _preferences.transitions:
        add ImageReference("hateplus_noise")

screen hateplus_cake_recipe_simple:
    modal True
    
    vbox xalign 0.85 yalign 0.5:
        window background Frame("whitewindow.dlc2.png", 20, 20) xmaximum 520 xminimum 520 xalign 0.5 top_padding 10 bottom_padding 20:
            has vbox
            text "Ingredients" bold True style style.text["hateplus-oldstyle" + persistent._language]
            grid 2 4:
                text "• 4 tablespoons flour" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 3 tablespoons melted butter" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 2 tablespoons sugar" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 1/4 teaspoon vanilla extract" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 2 tablespoons cocoa" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 1 tablespoon chocolate chips" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 1 egg" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 3 tablespoons milk" style style.text["hateplus-oldstyle" + persistent._language] size 16
            text "{b}Directions{/b}\n1. Add all dry ingredients to microwave-safe mug. Mix well.\n2. Crack egg and add to mug. Mix well.\n3. Pour milk, butter, chocolate chips, mix well. Add vanilla extract.\n4. Microwave contents of mug on maximum power for 3 minutes. \n5. Wait until cake stops rising and sets, then serve~!" style style.text["hateplus-oldstyle" + persistent._language]

        button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep5.mp3"), Return(), Hide("hateplus_cake_recipe_simple") ] xalign 0.5:
            text "{font=DejaVuSans.ttf}{plain}{size=+8}☆★{/size}{/plain}{/font} All done~! {font=DejaVuSans.ttf}{plain}{size=+8}★☆{/size}{/plain}{/font}" style style.text[char_style() + persistent._language]

screen hateplus_cake_recipe_complex:
    $ yadjust = ui.adjustment(step=24, adjustable=False)
    modal True
    
    vbox xalign 0.85 yalign 0.5:
        window background Frame("whitewindow.dlc2.png", 20, 20) xmaximum 520 xminimum 520 xalign 0.5 top_padding 10 bottom_padding 20 left_padding 25 right_padding 10:
            has hbox spacing 5
            viewport id "vp" child_size (425, 410) ymaximum 410 xmaximum 425 yadjustment yadjust mousewheel True:
                has vbox
                text "Cake ingredients" bold True style style.text["hateplus-oldstyle" + persistent._language]
                grid 2 5:
                    text "• 2 cups flour" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 2 cups sugar" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 1/4 teaspoon salt" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 4 heaping tablespoons cocoa" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 2 sticks butter" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 1 cup boiling water" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 1/2 cup buttermilk" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 2 whole beaten eggs" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 1 teaspoon baking soda" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 1 teaspoon vanilla" style style.text["hateplus-oldstyle" + persistent._language] size 16

                text "{b}Cake directions{/b}\n1. Combine flour, sugar, and salt in a mixing bowl.\n2. Melt butter in saucepan. Add cocoa and stir together. Add boiling water, boil mixture for 30 seconds, then turn off heat. Pour onto flour mixture and stir lightly.\n3. Combine buttermilk, beaten eggs, baking soda, and vanilla. Stir into other mixture.\n4. Pour into cake pan and bake at 350°F for 20 minutes." style style.text["hateplus-oldstyle" + persistent._language]

                null height 15

                text "Frosting ingredients" bold True style style.text["hateplus-oldstyle" + persistent._language]
                grid 2 2:
                    text "• 1 3/4 stick butter" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 4 heaping tablespoons cocoa" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 6 tablespoons milk" style style.text["hateplus-oldstyle" + persistent._language] size 16
                    text "• 1 teaspoon vanilla" style style.text["hateplus-oldstyle" + persistent._language] size 16
                text "• 1 pound (minus 1/2 cup) powdered sugar" style style.text["hateplus-oldstyle" + persistent._language] size 16

                text "{b}Frosting directions{/b}\n1.Melt butter in saucepan. Stir in cocoa, then turn off heat.\n2. Add milk, vanilla, powdered sugar, and stir.\n3. Pour over freshly baked cake." style style.text["hateplus-oldstyle" + persistent._language]

            #vbox:
            use hateplus_scrollbar(yadjust=yadjust, amount=24, ymaximum=320, old_style=True)

        button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep5.mp3"), Return(), Hide("hateplus_cake_recipe_complex") ] xalign 0.5:
            text "{font=DejaVuSans.ttf}{plain}{size=+8}☆★{/size}{/plain}{/font} All done~! {font=DejaVuSans.ttf}{plain}{size=+8}★☆{/size}{/plain}{/font}" style style.text[char_style() + persistent._language]


screen hateplus_shopping_trip:
    modal True

    # For Korean UI Tweak - iAmGhost
    $ shopping_trip_yalign = 0.6

    if persistent._language == "korean":
        $ shopping_trip_yalign = 0.65

    button style style.button[char_style()] action [ Play("sound", "sfx/fxbeep5.mp3"), Return(), Hide("hateplus_shopping_trip") ] xanchor 0.5 xalign 0.75 yalign shopping_trip_yalign:
        text "{font=DejaVuSans.ttf}{plain}{size=+8}☆★{/size}{/plain}{/font} All done~! {font=DejaVuSans.ttf}{plain}{size=+8}★☆{/size}{/plain}{/font}" style style.text[char_style() + persistent._language]

transform diagnostic_blink:
    alpha 1.0
    pause 4.1
    linear .1 alpha 0
    linear .1 alpha 1.0
    linear .1 alpha 0
    linear .1 alpha 1.0
    linear .1 alpha 0
    linear .1 alpha 1.0
    linear .1 alpha 0
    linear .1 alpha 1.0
    linear .1 alpha 0
    repeat

transform diagnostic_unfold:
    alpha 0 crop (0,0,533,50)
    pause .2
    linear .3 alpha 1.0
    easeout .3 crop (0,0,533,320)

screen hateplus_diagnostic:
    modal True
    default index = 0

    if current_character != "newmute" or "hateplus_newmute_read_note" in conversations_seen:
        if "mute" in current_character:
            $ text = [ "Performing diagnostic on AI construct *Mute" ]
        elif current_character == "hyunae":
            $ text = [ "Performing diagnostic on AI construct *Hyun-ae" ]
        else:
            $ text = [ "Performing diagnostic on AI constructs *Hyun-ae and *Mute" ]
        $ text += [ "No errors found!" ]

        timer 10.0 action [ Hide("hateplus_diagnostic"), Play("sound", "sfx/fxbeep1.mp3") ]

    else:
        $ text = [ "Performing diagnostic on AI construct *Mute", "WARNING: Recompile failed, checking integrity", "ERROR: Checksum failed", "Reinitializing memory data...", "Done!" ]

        timer 10.0 action [ SetScreenVariable("index", index+1), Play("sound", "sfx/fxbeep5.mp3") ]
        timer 15.0 action [ SetScreenVariable("index", index+1), Play("sound", "sfx/fxbeep5.mp3") ]
        timer 20.0 action [ SetScreenVariable("index", index+1), Play("sound", "sfx/fxbeep5.mp3") ]
        timer 25.0 action [ Hide("hateplus_diagnostic"), Play("sound", "sfx/fxbeep1.mp3") ]

    timer 5.0 action [ SetScreenVariable("index", index+1), Play("sound", "sfx/fxbeep5.mp3") ]

    window style style.window["hateplus"] xalign 0.5 yalign 0.5 left_padding 50 xminimum 600:
        has vbox
        hbox xalign 0.5 at [ main_unfold_contents, flicker ]:
            add ImageReference("spinner") yalign 0.5
            text text[index] style style.text["hateplus" + persistent._language] yalign 0.5 text_align 0.5 minwidth 550 at diagnostic_blink

screen rollback_keymap:
    key "mousedown_5" action RollForward()
    key "mousedown_4" action Rollback()
    key "K_PAGEUP" action Rollback()
    key "K_PAGEDOWN" action RollForward()
    key "K_TAB" action Skip()
    key "K_LCTRL" action Skip()
    key "K_RCTRL" action Skip()

    vbox yalign 1.0 xalign 0 yoffset -6 xoffset 20:
        button hover_background ("arrow" + short(current_character) + ".dlc2.png") background im.Alpha("arrow" + short(current_character) + ".dlc2.png", 0.7) insensitive_background im.Alpha("arrow" + short(current_character) + ".dlc2.png", 0.2) action Rollback():
            null width 40 height 39

        button hover_background im.Flip("arrow" + short(current_character) + ".dlc2.png", False, True) background im.Alpha(im.Flip("arrow" + short(current_character) + ".dlc2.png", False, True), 0.7) insensitive_background im.Alpha(im.Flip("arrow" + short(current_character) + ".dlc2.png", False, True), 0.2) action RollForward():
            null width 40 height 39
