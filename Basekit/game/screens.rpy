init python:
    import math, random
    
    header1 = { "hyunae": Frame("hyunae-name.png", 40, 0), "mute": Frame("mute-name.png", 40, 0), "x":Frame(im.Grayscale("hyunae-name.png"), 40, 0) }
    header2 = { "hyunae": Frame("hyunae-header.png", 40, 0), "mute": Frame("mute-header.png", 40, 0), "x":Frame(im.Grayscale("hyunae-header.png"), 40, 0) }
    hover_outlines = { "hyunae": [ (2, (102, 179, 221, 32), 0, 0), (1, (102, 179, 221, 96), 0, 0) ], "mute": [ (2, (255, 0, 0, 32), 0, 0), (1, (255, 0, 0, 96), 0, 0) ], "x":[ (2, (102, 102, 102, 32), 0, 0) ] }

    header1["현애"], header2["현애"] = header1["hyunae"], header2["hyunae"]
    header1["뮤트"], header2["뮤트"] = header1["mute"], header2["mute"]
    
    def nop():
        pass
        
    def get_transition(t):
        if _preferences.transitions:
            return t
        else:
            return instant_fade

    def new_toggle_fullscreen():
        if persistent.resolution == 1:
            renpy.set_resolution(persistent.old_resolution)
        else:
            renpy.set_resolution(1)

        store.resolution = persistent.resolution

    def local_message(message):
        if persistent._language and message.id in store.translated_blocks[persistent._language]:
            translated_message = store.translated_blocks[persistent._language][message.id]

            translated_message.encrypted = message.encrypted
            translated_message.enabled = message.enabled

            return translated_message

        return message


screen keymap:
    zorder 9001
    
    key 'meta_f' action new_toggle_fullscreen
    key 'alt_K_RETURN' action new_toggle_fullscreen
    key 'alt_K_KP_ENTER' action new_toggle_fullscreen
    key 'mouseup_3' action Show("preferences", Dissolve(0.5))

screen hide_prefs:
    zorder 9002

    key 'mouseup_3' action [ Hide("preferences", Dissolve(0.5)), Hide("messages_overlay", Dissolve(0.5)) ]

screen block_everything:
    default timeout = 1.0
    zorder 9003
    modal True

    button action nop background None xalign 0.5 yalign 0.5:
        null height 1024 width 640

    key "K_RETURN" action nop

    timer timeout action Hide("block_everything")

screen rollback_keymap:
    key "mousedown_5" action RollForward()
    key "mousedown_4" action Rollback()
    key "K_PAGEUP" action Rollback()
    key "K_PAGEDOWN" action RollForward()

screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    use rollback_keymap
    
    if store.radiation and store.radiation_levels > 0.8:
        window id "window" background None:
            text what id "what" color "#000"
    else:
        # Decide if we want to use the one-window or two-window varaint.
        if not two_window:
    
            # The one window variant.        
            window at window_fade:
                id "window"
    
                has vbox:
                    style "say_vbox"
    
                if who:
                    text who id "who"
    
                text what id "what"
    
        else:            
            window bottom_padding 40 at If("{fast}" in what, [], window_fade):
                id "window"
    
                has vbox spacing 15:
                    style "say_vbox"
                    
                if who:            
                    window background header1[who.replace("*", "").replace("-", "").lower()] ypadding 0 yminimum 39 xminimum 269 xpos -48 xanchor 0 yoffset 2 left_padding 20:
                        text who size 28 bold False style style.say_label[persistent._language]:
                            id "who"
    
                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


screen bottom_menu:
    zorder 100
    default quit = True
    
    on "show" action Hide("full_bottom_menu")
    
    hbox xalign 1.0 yalign 1.0 yoffset -10 xoffset -10 focus "bottom_menu" at slower_fade_once:
        use bottom_menu_buttons(quit=quit)
        
screen full_bottom_menu:
    zorder 100
    default quit = True
    
    timer 0.5 action Hide("bottom_menu")
    
    hbox xalign 1.0 yalign 1.0 yoffset -10 xoffset -10 focus "full_bottom_menu" at slower_fade_once:
        button background If(side_conversation[current_character],ImageReference("talk_glow_" + current_character[0]), "talk.png") hover_background ("talk-" + current_character[0] + "hover.png") xminimum 74 yminimum 69 action [ Play("sound", "sfx/fxbeep5.mp3"), Jump("jump_to_dialogue") ]:
            null 
            
        use bottom_menu_buttons(quit=quit)
        
screen bottom_menu_buttons:
    button background "config.png" hover_background ("config-" + current_character[0] + "hover.png") xminimum 74 yminimum 69 action [ Play("sound", "sfx/fxbeep5.mp3"), Show("preferences", Dissolve(0.5)) ]:
        null
    
    button background "power.png" hover_background ("power-" + current_character[0] + "hover.png") xminimum 74 yminimum 69 action [ Play("sound", "sfx/fxbeep5.mp3"), If(quit, Show("quit"), Quit(False)) ]:
        null
            
screen back_text:
    default text = "Go back"
    text text ypos 73 xanchor 1.0 xpos 300 outlines hover_outlines[current_character] style style.text[persistent._language]

screen flag_text:
    text "Flag" ypos 113 xanchor 1.0 xpos 300 outlines hover_outlines[current_character]

screen unflag_text:
    text "Unflag" ypos 113 xanchor 1.0 xpos 300 outlines hover_outlines[current_character]
    
screen upload_text:    
    text "Present" ypos 113 xanchor 1.0 xpos 300 outlines hover_outlines[current_character]
    
screen home_text:
    text "Home" ypos 33 xanchor 1.0 xpos 300 outlines hover_outlines[current_character] style style.text[persistent._language]

screen up_text:
    default text = "Previous"
    text text ypos 113 xanchor 1.0 xpos 300 outlines hover_outlines[current_character] style style.text[persistent._language]

screen down_text:
    default text = "Next"
    text text ypos 153 xanchor 1.0 xpos 300 outlines hover_outlines[current_character] style style.text[persistent._language]
            
screen pronounciation_text:
    text "Pronunciation" ypos 414 xanchor 1.0 xpos 300 outlines hover_outlines[current_character] style style.text[persistent._language]

screen kim_text:
    text "Kim family tree" ypos 450 xanchor 1.0 xpos 300 outlines hover_outlines[current_character] style style.text[persistent._language]

screen smith_text:
    text "Smith family tree" ypos 478 xanchor 1.0 xpos 300 outlines hover_outlines[current_character] style style.text[persistent._language]

init python:
    def set_hover_up(val):
        persistent.hover_up = val

    def set_hover_down(val):
        persistent.hover_down = val

screen side_menu:
    #default submit = False
    default message = None
    default show_home = True
    default block = None

    default hover_up = False
    default hover_down = False

    $ prev_action = prev_text = None
    $ next_action = next_text = None

    $ back_text = "Go back"
    $ screen_type = ""
    
    if message:
        python:
            if False:
            #if _block == store.unread_block and len(store.unread_block.contents) > 1:
                block = store.unread_block
            else:
                for i in blocks:
                    if message in i.contents:
                        block = i

            if False:
            #if block == store.unread_block and len(store.scrub) == len(store.unread_block.contents):
                if last_message:
                    back_text = local_message(last_message).name
                    back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("messages"), SetVariable("_message", last_message), SetVariable("_block", None), SetVariable("new_messages", False), Jump("pan_to_message") ]
                else:
                    back_text = "Block index"
                    back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("messages"), Hide("block"), SetVariable("_block", None), SetVariable("_message", None), SetVariable("last_message", None), Jump("pan_to_logs") ]
            else:
                back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("messages"), SetVariable("last_message", None), SetVariable("_block", block), Jump("pan_to_messages") ]

                if False:
                    #if block == store.unread_block:
                    back_text = store.unread_block.name
                    back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("messages"), SetVariable("_block", block), Jump("pan_to_messages") ]
                elif _message:
                    back_text = blocks[int(_message.id.split("-")[0])-1].name
                elif last_message:
                    back_text = local_message(last_message).name

            screen_type = "messages"
            if block and message in block.contents and block.contents.index(message) > 0:
                for i in range(block.contents.index(message)-1, -1, -1):
                    if not prev_action and (block.contents[i].enabled or (not store.game_playing and get_id(block.contents[i]) in persistent.blocks)):
                        prev_action = [ Play("sound", "sfx/fxbeep5.mp3"), SetVariable("_message", block.contents[i]), renpy.curry(set_hover_up)(True), renpy.curry(set_hover_down)(False), Jump("new_message") ]
                        prev_text = local_message(block.contents[i]).name
                        

            if block and message in block.contents and block.contents.index(message) < len(block.contents):
                for i in range(block.contents.index(message)+1, len(block.contents)):
                    if not next_action and (block.contents[i].enabled or (not store.game_playing and get_id(block.contents[i]) in persistent.blocks)):
                        next_action = [ Play("sound", "sfx/fxbeep5.mp3"), SetVariable("_message", block.contents[i]), renpy.curry(set_hover_down)(True), renpy.curry(set_hover_up)(False), Jump("new_message") ]#Show("messages", message=block.contents[i]), Show("side_menu", message=block.contents[i], hover_down=True) ]
                        next_text = local_message(block.contents[i]).name

    else:
        key "mousedown_5" action nop
        key "mousedown_4" action nop

        if store.game_playing:
            timer .5 action [ try_ping, renpy.restart_interaction ]

        if show_home:
            python:
                if False:
                #if last_message and block == store.unread_block:
                    back_text = local_message(last_message).name
                    back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("block"), SetVariable("_block", None), SetVariable("new_messages", False), Jump("pan_to_message") ]
                else:
                    back_text = "Block index"
                    back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("block"), SetVariable("_block", None), SetVariable("_message", None), SetVariable("last_message", None), Jump("pan_to_logs") ]

                using_blocks = [ ]
                for i in blocks:
                    for m in i.contents:
                        if m.enabled or (not store.game_playing and get_id(m) in persistent.blocks):
                            using_blocks.append(i)
                            break

                screen_type = "block"
                if block in blocks and blocks.index(block) > 0:
                    for i in range(blocks.index(block)-1, -1, -1):
                        if not prev_action and blocks[i] in using_blocks:
                            prev_action = [ Play("sound", "sfx/fxbeep5.mp3"), Show("block", block=blocks[i]), Show("side_menu", block=blocks[i], hover_up=True) ]
                            prev_text = blocks[i].name

                if block in blocks and blocks.index(block) < len(blocks):
                    for i in range(blocks.index(block)+1, len(blocks)):
                        if not next_action and blocks[i] in using_blocks:
                            next_action = [ Play("sound", "sfx/fxbeep5.mp3"), Show("block", block=blocks[i]), Show("side_menu", block=blocks[i], hover_down=True) ]
                            next_text = blocks[i].name

        else:
            if store.game_playing:
                $ back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("logs"), SetVariable("_block", None), SetVariable("_message", None), SetVariable("last_message", None), Jump("slow_loop") ]
            else:
                $ back_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("logs"), Show("main_menu", Dissolve(0.5)) ]
    

    key "K_PAGEUP" action If(prev_action, prev_action, nop)
    key "K_PAGEDOWN" action If(next_action, next_action, nop)

    on "hide" action [ Hide("back_text", Dissolve(0.2)), Hide("home_text", Dissolve(0.2)), Hide("up_text", Dissolve(0.2)), Hide("down_text", Dissolve(0.2)), Hide("pronounciation_text", Dissolve(0.2)), Hide("kim_text", Dissolve(0.2)), Hide("smith_text", Dissolve(0.2)) ]
    on "replace" action [ If(hover_up and prev_text, Show("up_text", Dissolve(0.2), text=prev_text), Hide("up_text", Dissolve(0.2))), If(hover_down and next_text, Show("down_text", Dissolve(0.2), text=next_text), Hide("down_text", Dissolve(0.2))) ]
    
    vbox yanchor 0 ypos 26 xpos 315 xanchor 0 spacing 203:
        window at get_transition(window_fade) left_padding 10 right_padding 15 top_padding 5 bottom_padding 15 focus "side_menu":
            has vbox spacing 5 first_spacing 0
            
            if show_home:
                if store.game_playing:
                    $ home_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("messages"), Hide("block"), SetVariable("_block", None), SetVariable("_message", None), SetVariable("last_message", None), Jump("slow_loop") ]
                else:
                    $ home_action = [ Play("sound", "sfx/fxbeep4.mp3"), Hide("block"), Hide("messages"), Show("main_menu") ]

                button background "home.png" hover_background ("home-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action home_action hovered Show("home_text", Dissolve(0.2)) unhovered Hide("home_text", Dissolve(0.2)):
                    null

                key "K_HOME" action home_action
                key "K_BACKSPACE" action back_action
            else:
                button background "home.png" hover_background ("home-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action back_action hovered Show("home_text", Dissolve(0.2)) unhovered Hide("home_text", Dissolve(0.2)):
                    null

                key "K_HOME" action back_action

            if show_home:
                button background "back.png" hover_background ("back-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action back_action hovered Show("back_text", Dissolve(0.2), text=back_text) unhovered Hide("back_text", Dissolve(0.2)):
                    null

                #if not prev_text:
                #    $ renpy.hide_screen("up_text")
                #if not next_text:
                #    $ renpy.hide_screen("down_text")
                    
                button background "up.png" insensitive_background "up-disabled.png" hover_background ("up-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action prev_action hovered Show("up_text", Dissolve(0.2), text=prev_text) unhovered Hide("up_text", Dissolve(0.2)) focus "up":
                    null
                
                null height 0

                button background "down.png" insensitive_background "down-disabled.png" hover_background ("down-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action next_action hovered Show("down_text", Dissolve(0.2), text=next_text) unhovered Hide("down_text", Dissolve(0.2)) focus "down":
                    null
                
            null height 3

        if screen_type == "messages" and not message in blocks[11-1].contents:
            window at get_transition(window_fade) left_padding 10 right_padding 15 top_padding 5 bottom_padding 10 focus "side_menu" xalign 0:
                has vbox spacing 5 first_spacing 0

                button background "pronounciationicon.png" hover_background ("pronounciationicon-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action Show("messages_overlay", Dissolve(0.5), message=get_m("11-1")) hovered Show("pronounciation_text", Dissolve(0.2)) unhovered Hide("pronounciation_text", Dissolve(0.2)):
                    null

                button background "kimicon.png" hover_background ("kimicon-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action Show("messages_overlay", Dissolve(0.5), message=get_m("11-3")) hovered Show("kim_text", Dissolve(0.2)) unhovered Hide("kim_text", Dissolve(0.2)):
                    null

                if get_m("11-5").enabled or (not store.game_playing and "11-5" in persistent.blocks):
                    button background "smithicon.png" hover_background ("smithicon-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action Show("messages_overlay", Dissolve(0.5), message=get_m("11-5")) hovered Show("smith_text", Dissolve(0.2)) unhovered Hide("smith_text", Dissolve(0.2)):
                        null
                elif get_m("11-4").enabled or (not store.game_playing and "11-4" in persistent.blocks):
                    button background "smithicon.png" hover_background ("smithicon-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action Show("messages_overlay", Dissolve(0.5), message=get_m("11-4")) hovered Show("smith_text", Dissolve(0.2)) unhovered Hide("smith_text", Dissolve(0.2)):
                        null
                else:
                    null height 3

screen text_body:
    text body bold False at text_fade ypos 120 yanchor 0 xmaximum 580 xpos 400 style style.text[persistent._language]

init python:
    def scrub_message(message):
        def func():
            if message in store.unread_block.contents and message not in store.scrub:
                store.scrub.append(message)

        return func
    
    def mark_read(message, page, total_pages):
        def func():
            #scrub_message(message)()
            message.enabled = message.read = store.current_character
            if message not in store.recent_messages:
                store.recent_messages.append(message)
            store._message = message

            if page == 0:
                change_track(_block, True)
                #renpy.restart_interaction()

        return func

    def remove_read():
        for i in store.unread_block.contents:
            if i in store.scrub or i.read:
                store.unread_block.contents.remove(i)

        store.scrub = [ ]
            
screen messages:
    modal True
    default page = 0
    key "mousedown_5" action If(page < len(local_message(message).body)-1, Show("messages", message=message, page=page+1), nop)
    key "mousedown_4" action If(page > 0, Show("messages", message=message, page=page-1), nop)
    key "K_RIGHT" action If(page < len(local_message(message).body)-1, Show("messages", message=message, page=page+1), nop)
    key "K_LEFT" action If(page > 0, Show("messages", message=message, page=page-1), nop)

    if store.game_playing:
        on "show" action mark_read(message, page, len(local_message(message).body)-1)
        on "replace" action mark_read(message, page, len(local_message(message).body)-1)
        timer .5 action Show("gotoai", Dissolve(0.5))

    on "hide" action [ Hide("side_menu"), Hide("gotoai") ]
    
    window at get_transition(window_fade) top_padding 0 bottom_padding 5 xpadding 25 xanchor 1.0 xpos 1009 yanchor 0 ypos 26 yminimum 500 focus "message":
        has vbox spacing 15 first_spacing -28 xminimum 580
        
        text message.id xalign 1.0
        window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -23 xanchor 0 yoffset 2 left_padding 20:
            text local_message(message).name style style.title[persistent._language]
        hbox:
            text local_message(message).creator minwidth 250 style style.text[persistent._language]
            text local_message(message).date minwidth 250 text_align 1.0 style style.text[persistent._language]
        
        null height 5 width 580
        
    python:
        try:
            local_message(message).body[page]
        except IndexError, e:
            page = 0

    use text_body(body=local_message(message).body[page])
    
    if page > 0:
        button background None action Show("messages", message=message, page=page-1) xmaximum 150 yanchor 0.5 ypos 500 xanchor 0.5 xpos 500 focus "previous":
            text "Previous page" outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] minwidth 150 text_align 0 style style.log_pages[persistent._language]  
    if message:
        if (len(local_message(message).body)) > 1:
            text ("Page " + str(page+1) + "/" + str(len(local_message(message).body))) text_align 0.5 minwidth 150 yanchor 0.5 ypos 500 xanchor 0.5 xpos 680 style style.log_pages[persistent._language]  
        if page < len(local_message(message).body)-1:
            button background None action Show("messages", message=message, page=page+1) xmaximum 150 yanchor 0.5 ypos 500 xanchor 0.5 xpos 850 focus "next":
                text "Next page" outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] minwidth 150 text_align 1.0 style style.log_pages[persistent._language]       

    if page == len(local_message(message).body)-1 and store.game_playing:
        timer .5 action [ try_ping, renpy.restart_interaction ]

screen messages_overlay:
    modal True
    zorder 102
    default page = 0
    key "mousedown_5" action If(page < len(message.body)-1, Show("messages_overlay", message=message, page=page+1), nop)
    key "mousedown_4" action If(page > 0, Show("messages_overlay", message=message, page=page-1), nop)
    key "K_RIGHT" action If(page < len(message.body)-1, Show("messages_overlay", message=message, page=page+1), nop)
    key "K_LEFT" action If(page > 0, Show("messages_overlay", message=message, page=page-1), nop)
    key "K_ESCAPE" action Hide("messages_overlay", Dissolve(0.5))
    key "K_BACKSPACE" action Hide("messages_overlay", Dissolve(0.5))

    on "show" action Show("hide_prefs")
    on "hide" action Hide("hide_prefs")

    if persistent.animated_backgrounds:
        add ImageReference("bg white") at bg_fast
    else:
        add ImageReference("bg white static") at bg_fast

    window at get_transition(window_fade) top_padding 0 bottom_padding 5 xpadding 25 xanchor 1.0 xpos 1009 yanchor 0 ypos 26 yminimum 500 focus "message":
        has vbox spacing 15 first_spacing -28 xminimum 580
        
        text message.id xalign 1.0
        window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -23 xanchor 0 yoffset 2 left_padding 20:
            text local_message(message).name style style.title[persistent._language]
        hbox:
            text local_message(message).creator minwidth 250 style style.text[persistent._language]
            text local_message(message).date minwidth 250 text_align 1.0 style style.text[persistent._language]
        
        null height 5 width 580
        
    use text_body(body=local_message(message).body[page])
    
    if page > 0:
        button background None action Show("messages_overlay", message=message, page=page-1) xmaximum 150 yanchor 0.5 ypos 500 xanchor 0.5 xpos 500 focus "previous":
            text "Previous page" size 18 outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] minwidth 150 text_align 0
    if (len(local_message(message).body)) > 1:
        text ("Page " + str(page+1) + "/" + str(len(local_message(message).body))) size 18 text_align 0.5 minwidth 150 yanchor 0.5 ypos 500 xanchor 0.5 xpos 680
    if page < len(local_message(message).body)-1:
        button background None action Show("messages_overlay", message=message, page=page+1) xmaximum 150 yanchor 0.5 ypos 500 xanchor 0.5 xpos 850 focus "next":
            text "Next page" size 18 outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] minwidth 150 text_align 1.0         
    
    window background None yalign 0.95 xalign 1.0 xoffset -15 xpadding 0 xmargin 0 ypadding 0 ymargin 0:
        use preferences_back

screen gotoai:
    $ use_name = current_character + str(persistent._language)
    if current_character == "hyunae":
        $ use_name += store.outfit

    $ show_action = [ Play("sound", "sfx/fxbeep2.mp3"), Hide("gotoai"), Show("bottom_menu"), Show("side_menu", message=True), Jump("present") ]
    key "K_SPACE" action show_action
    
    $ background = "goto" + use_name  + ".png"
    $ hover_background = "goto" + use_name + "-hover.png"
    if _message in store.messages_shown[current_character] and not message_exception():
        $ background = im.MatrixColor(background, im.matrix.desaturate())
        $ hover_background = im.MatrixColor(hover_background, im.matrix.desaturate())

    button background background hover_background hover_background xminimum 261 yminimum 223 action show_action yalign 0.5 xpos 30 focus "goto" focus_mask background:
        null

screen main_screen:
    #modal True
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    
    $ store.game_playing = True
    $ seen_convo = max(int((not conversation[current_character] in conversations_seen or bool(side_conversation[current_character])) or not repeated_myself), 0.5)
    
    vbox at get_transition(window_fade) xpos 0.4 xanchor 0 yanchor 0 ypos 70 spacing 30 focus "main_screen":
        window ypadding 30 xalign 0 right_padding 90:
            has vbox spacing 15
            
            button background (im.Alpha("comment32.png", seen_convo)) hover_background ("comment32-" + current_character[0] + "hover.png") left_padding 52 action [ Play("sound", "sfx/fxbeep2.mp3"), Hide("main_screen"), Jump("dialogue") ]:
                text ("Speak with *" + CHARACTERS[current_character]) outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines  hover_outlines[current_character] color (61, 61, 61, 196*seen_convo) style style.main_screen[persistent._language]
            button background "linedpaper32.png" hover_background ("linedpaper32-" + current_character[0] + "hover.png") left_padding 52 action [ Play("sound", "sfx/fxbeep5.mp3"), Hide("main_screen"), If(store.override_conversation, Jump("override_conversation"), Jump("pan_to_logs")) ]:
                text "Access log documents" outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines  hover_outlines[current_character] style style.main_screen[persistent._language]
            button background "monitor32.png" hover_background ("monitor32-" + current_character[0] + "hover.png") left_padding 52 action [ Play("sound", "sfx/fxbeep4.mp3"), terminal_music, Hide("main_screen"), Jump("pan_to_terminal") ]:
                text "Use override terminal" outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines  hover_outlines[current_character] style style.main_screen[persistent._language]
        
        if not store.override_conversation:
            hbox:
                window top_padding 0 bottom_padding 30 left_padding 10 right_padding 25 xminimum 520 size_group "main":
                    has vbox spacing 0 first_spacing -30
                    
                    window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -8 xanchor 0 yoffset 2 left_padding 20:
                        if show_recent:
                            text "Recent messages" style style.title[persistent._language]
                        else:
                            text "Unread messages" style style.title[persistent._language]
                    
                    #    button action SetVariable("show_recent", False) xalign 1.0 xpadding 0 xoffset 10 background None:
                    #        text "Show unread" outlines [ (2, (0,0,0,0), 0, 0)] hover_outlines hover_outlines[current_character] bold False text_align 1.0
                    #else:
                    #    button action SetVariable("show_recent", True) xalign 1.0 xpadding 0 xoffset 10 background None:
                    #        text "Show recent" outlines [ (2, (0,0,0,0), 0, 0)] hover_outlines hover_outlines[current_character] bold False text_align 1.0

                    null height 35
                    
                    if show_recent:
                        if get_recent_messages():    
                            for i in reversed(recent_messages):
                                button action [ Play("sound", "sfx/fxbeep5.mp3"), Hide("main_screen"), SetVariable("_message", i), Jump("pan_to_message") ] background None:
                                    use message_button(message=i, short=True)
                        else:
                            text "No messages have been read." text_align 0.5 minwidth 465 style style.text[persistent._language]
                    else:
                        $ count = 0
                        for block in blocks:
                            for i in block.contents:
                                if count < 3 and i.enabled and not i.read:
                                    button action [ Play("sound", "sfx/fxbeep5.mp3"), Hide("main_screen"), SetVariable("_message", i), Jump("pan_to_message") ] background None:
                                        use message_button(message=i, short=True)
                                    $ count += 1
                        if count == 0:
                            text "No messages are unread." text_align 0.5 minwidth 465 style style.text[persistent._language]
        
    if not store.override_conversation:
        vbox xanchor 1.0 xpos 1000 ypos 287 spacing -20:
            button foreground im.Alpha("unread.png", 0.7, xpos=28, ypos=15) action SetVariable("show_recent", False) style style.button["normal"] size_group "toggle_unread":
                null height 29
            
            button foreground im.Alpha("recent.png", 0.7, xpos=28, ypos=22) action SetVariable("show_recent", True) style style.button["normal"] size_group "toggle_unread":
                null height 29

            
screen message_button:
    default short = False
    
    hbox spacing 2:
        null width 1 height 42
        vbox spacing -16 yalign 0.5:
            if not message.read and store.game_playing:
                text "NEW" size 16 xalign 1.0
            else:
                text " " size 16
            text local_message(message).name minwidth 275 outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] yalign 0.5 style style.message_button[persistent._language]
        text local_message(message).creator yalign 0.5 minwidth 170 style style.message_button[persistent._language]
        if not short:
            vbox xminimum 126:
                text local_message(message).date yalign 0.5 minwidth 126 text_align 1.0 style style.message_button_small[persistent._language]
                text message.id yalign 0.5 minwidth 126 text_align 1.0 style style.message_button_small[persistent._language]
            
screen null_button:
    hbox spacing 5:
        null width 6 height 50
        text "————————————————————" minwidth 275 outlines [ (2, (0,0,0,0), 0, 0) ] size 20 yalign 0.5
        text "—————————————" bold False yalign 0.5 minwidth 170 size 20
        vbox xminimum 121:
            text "—————————" size 20 yalign 0.5 minwidth 115 text_align 1.0
            text "—————————" size 20 yalign 0.5 minwidth 115 text_align 1.0



screen logs:
    modal True

    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    
    on "show" action SetVariable("_message", None)
    on "hide" action Hide("side_menu")

    python:
        using_blocks = [ ]
        for block in blocks:
            for message in block.contents:
                if message.enabled or (not store.game_playing and get_id(message) in persistent.blocks):
                    using_blocks.append(block)
                    break
        #if store.game_playing and store.unread_block.contents:
        #    using_blocks.append(store.unread_block)
    
    vbox at get_transition(window_fade) xanchor 0 xpos 380 yanchor 0 ypos 26 spacing 30:
        #window bottom_padding 30 top_padding 0 xpadding 25 xminimum 500:
        #    has vbox spacing 15
        #    
        #    window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -23 xanchor 0 yoffset 2 left_padding 20:
        #        text "Status" size 28 font "fonts/Delicious-Heavy.otf" bold False color (255,255,255,220)
                
        window bottom_padding 30 top_padding 0 xpadding 25 xminimum 500 size_group "window":
            has vbox spacing 15
            
            window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -23 xanchor 0 yoffset 2 left_padding 20:
                text "Search by ID" style style.title[persistent._language]
            
            hbox spacing 15:
                add "search32.png"
                input italic True color (128, 128, 128, 220)
                #$ store.input = ui.input(italic=True, color=(128, 128, 128, 220))
                
            text "Type the document ID and press enter to search." size 20 style style.plain[persistent._language]  
            
    
        window bottom_padding 30 top_padding 0 xpadding 25 xminimum 500 size_group "window":
            has vbox spacing 15
            
            window background header2[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -23 xanchor 0 yoffset 2 left_padding 20:
                text "Data blocks" style style.title[persistent._language]
               
            grid 2 math.ceil(len(using_blocks)/2.0):
                for block in using_blocks:
                    hbox:
                        button action [ Play("sound", "sfx/fxbeep5.mp3"), Hide("logs"), SetVariable("_block", block), Jump("pan_to_messages") ] background None:
                            text block.name minwidth 85 outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] style style.block[persistent._language]
                            
                        python:
                            new = False
                            if block in store.blocks:
                                for message in block.contents[:9]:
                                    if not message.read and message.enabled and store.game_playing:
                                        new = True
                                    
                        if new:
                            text "NEW" size 16
                        else:
                            null
                    
                if len(using_blocks)%2 > 0:
                    null    
                
screen block:
    modal True
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    
    #on "show" action Show("side_menu", block=block)
    on "hide" action Hide("side_menu")
    
    window at get_transition(window_fade) xanchor 0 xpos 380 yanchor 0 ypos 26 bottom_padding 15 top_padding 0 left_padding 10 right_padding 20:
        has vbox spacing -1
        
        window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -8 xanchor 0 yoffset 2 left_padding 20:
            text block.name style style.title[persistent._language]
            
        null height 3
        
        for i in block.contents[:9]:
            if i.enabled or (not store.game_playing and get_id(i) in persistent.blocks):
                $ button_action = [ Play("sound", "sfx/fxbeep5.mp3"), Hide("block"), SetVariable("_message", i), Jump("pan_to_message") ]
                button action button_action background None:
                    use message_button(message=i)
            elif not block.hide:
                use null_button
                
        null height 5 width 570

screen connecting:
    modal True
    zorder 102
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop

    default message = ""
    
    timer (max(random.random()*3.0, 1.0)) action Return()

    # Better style took from Hate Plus's AI diagnose screen - iAmGhost
    
    window style style.window["hateplus"] xalign 0.5 yalign 0.5 left_padding 50 xminimum 350 at If(store.radiation, terminal_fade_radiation, window_fade):
        has vbox
        hbox xalign 0.5 at [ main_unfold_contents, flicker ]:
            add ImageReference("spinner") yalign 0.5
            text message style style.text["hateplus" + persistent._language] yalign 0.5 text_align 0.5 minwidth 300 at diagnostic_blink

screen radiation:
    zorder 100

    if radiation_levels > 0:
        window background ImageReference("radiation") xpadding 0 ypadding 0 at Transform(alpha=radiation_levels):
            null width 1024 height 640
        
init python:
    def pad_clock(a):
        if len(a.split(":")[1]) == 1:
            return a.split(":")[0] + ":0" + a.split(":")[1]
        else:
            return a

screen death_clock:
    zorder 102
    
    timer 1.0 action [ SetVariable("death_clock", death_clock-1), If(death_clock < 1, Jump("connection_error"), Show("death_clock")) ]

    text pad_clock(str(int(math.floor(death_clock/60))) + ":" + str(death_clock%60)) size 48 color "#fff" outlines [ (4, (0,0,0,255), 0, 0) ] xoffset 30 at death_clock_transform
    
screen terminal:
    zorder 101

    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    
    default buf = [ ]
    default pause = None
    
    if pause != None:
        timer pause action Return()

    modal bool(pause)
    
    vbox xalign 0.5 yalign 0.3 at If(store.radiation, terminal_fade_radiation, terminal_fade):
        window top_padding 10 bottom_padding 15:
            if not su:
                text "Override Terminal (restricted mode)" text_align 0.5 minwidth 750 style style.terminal[persistent._language] size 20
            else:
                text "Override Terminal" text_align 0.5 minwidth 750 style style.terminal[persistent._language] size 20
            
        window top_padding 10 bottom_padding 15 yminimum 434:
            has vbox xminimum 750 spacing 3
            null height 1 width 750
            for i in buf[-23:]:
                if isinstance(i, list):
                    hbox:
                        for j in i:
                            text j font "fonts/WHITRABT.TTF" size 16 bold False
                else:
                    text i font "fonts/WHITRABT.TTF" size 16 bold False
            if pause == None:
                hbox:
                    input id "input" font "fonts/WHITRABT.TTF" size 16 bold False color (0,0,0,0) prefix "{color=#3D3D3DC4}>" suffix "{/color}" length 75
                    text "_" font "fonts/WHITRABT.TTF" size 16 bold False at blink

screen choice:
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
            

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen say_input:

    modal True
    use say(who=who, what=what)

    window xminimum 450 xmaximum 450 yminimum 95 yalign 0.7 ypadding 30:
        has vbox

        #text prompt
        input italic True color (128, 128, 128, 220)

screen say_input_kr:
    modal True
    use say(who=who, what=what)

    window xminimum 450 xmaximum 450 yminimum 95 yalign 0.7 ypadding 30:
        has vbox
        add HangulInput(font="0@fonts/NanumGothic.ttc", color="808080DC")

        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

init python:
    def buyurl():
        import webbrowser
        webbrowser.open_new('http://ahatestory.com')

screen main_menu:
    zorder 1
    modal True
    
    #$ store.game_playing = False

    on "show" action Hide("stop_preferences")
    
    add "logo2.png" xalign 0.5 yalign 0.3 at slower_fade

    if renpy.list_saved_games():
        $ restore_action = [ Play("sound", "sfx/fxbeep5.mp3"), Show("preferences", Dissolve(0.5)) ]
    else:
        $ restore_action = None
    
    hbox xalign 0.5 yalign 0.8 yoffset -20 at slow_fade:
        button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 action [ Play("sound", "sfx/fxbeep1.mp3"), Start() ] xmargin 10:
            text "New" xalign 0.5 xoffset 10 yalign 0.5 style style.menu_button[persistent._language]
            
        button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 insensitive_background "mainmenubutton-idle.png" action restore_action xmargin 10:
            text "Restore" xalign 0.5 xoffset 10 yalign 0.5 style style.menu_button[persistent._language]
            
        if not renpy.demo_mode:
            button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 insensitive_background "mainmenubutton-idle.png" xmargin 10 action If(persistent.blocks and (persistent.ending1 or persistent.ending2 or persistent.ending3 or persistent.ending4 or persistent.ending5), [ Play("sound", "sfx/fxbeep2.mp3"), Show("bonus", Dissolve(0.5)), Hide("main_menu") ], None):
                vbox xalign 0.5 xoffset 10 yalign 0.5:
                    text "Bonus content" size 32 minwidth 200 text_align 0.5 style style.menu_button[persistent._language]
                    hbox xalign 0.5:
                        text persistent_complete_rate() size 18 bold False style style.text[persistent._language]
                        text " log completion" size 18 bold False style style.text[persistent._language]
        else:
            button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 insensitive_background "mainmenubutton-idle.png" action buyurl xmargin 10:
                vbox xalign 0.5 xoffset 10 yalign 0.5:
                    text "Buy full version" size 32 minwidth 200 text_align 0.5 xalign 0.5 style style.menu_button[persistent._language]
                    text "at ahatestory.com" size 18 bold False minwidth 200 text_align 0.5 style style.menu_button[persistent._language]
        
    if renpy.demo_mode:
        window background None xalign 0.5 yalign 1.0 yoffset -20 at slow_fade:
            text "TRIAL VERSION" size 40 style style.text[persistent._language]

    use bottom_menu

screen skip:
    zorder 100

    button style style.button["normal"] action [ SetVariable("skip", True), Return() ] xalign 1.0 yalign 1.0 at fast_fade:
        text "Skip intro" style style.skip[persistent._language]

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    zorder 102
    modal True

    key "K_ESCAPE" action Hide("preferences", Dissolve(0.5))
    key "mousedown_5" action nop
    key "mousedown_4" action nop
    key "K_PAGEUP" action nop
    key "K_PAGEDOWN" action nop
    
    on "show" action [ Show("file_picker"), Show("hide_prefs") ]
    on "hide" action [ Hide("file_picker"), Hide("hide_prefs") ]
    $ persistent.animated_backgrounds = _preferences.transitions
    
    $ renpy.set_resolution(store.resolution)
    $ resolution = store.resolution
    
    if persistent.animated_backgrounds:
        add ImageReference("bg white") at bg_fast
    else:
        add ImageReference("bg white static") at bg_fast

    window top_padding 0 bottom_padding 20 xpadding 15 xalign 0.05 yalign 0.5:
        vbox:
            window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -13 xanchor 0 yoffset 2 left_padding 20:
                text "Preferences" style style.title[persistent._language]
                
            null height 10
        
            window xalign 0 background None left_padding 20 xmaximum 420 right_padding 0 ypadding 0:
                has vbox
                text "Music volume" style style.preferences[persistent._language]
                bar value Preference("music volume") left_bar "fullbar.png" right_bar "emptybar.png" hover_left_bar "fullbar-hover.png" hover_right_bar "emptybar-hover.png" thumb None thumb_shadow None right_gutter 0 bar_resizing False

            null height 10

            window xalign 0 background None left_padding 20 xmaximum 420 right_padding 0 ypadding 0:
                has vbox
                text "Effects volume" style style.preferences[persistent._language]
                bar value Preference("sound volume") left_bar "fullbar.png" right_bar "emptybar.png" hover_left_bar "fullbar-hover.png" hover_right_bar "emptybar-hover.png" thumb None thumb_shadow None right_gutter 0 bar_resizing False
              
            null height 14
            hbox:      
                button action Preference("skip", "seen") style style.button["normal"] size_group "toggle2":
                    text "Only skip seen" xalign 0.5 style style.preferences_button[persistent._language] minwidth 140 text_align 0.5
    
                button action Preference("skip", "all") style style.button["normal"] size_group "toggle2":
                    text "Skip all" style style.preferences_button[persistent._language] xalign 0.5
                    
            #hbox:
            #    button action Preference("after choices", "stop") style style.button["normal"] size_group "toggle":
            #        text "Stop at choices" size 20 xalign 0.5
            #    
            #    button action Preference("after choices", "skip") style style.button["normal"] size_group "toggle":
            #        text "Skip after choices" size 20 xalign 0.5
                    
            window size_group "prefs" xalign 0 background None left_padding 20 xmaximum 420 right_padding 0 ypadding 0:
                has vbox
                text "Text speed" style style.preferences[persistent._language]
                bar value Preference("text speed") left_bar "fullbar.png" right_bar "emptybar.png" hover_left_bar "fullbar-hover.png" hover_right_bar "emptybar-hover.png" thumb None thumb_shadow None right_gutter 0 bar_resizing False
            
            null height 10
            
            hbox:      
                button action SetVariable("resolution", 2) style style.button["normal"] xpadding 30 yminimum 100 size_group "three":
                    text "{size=-2}Fullscreen\n(1024*640){/size}" style style.preferences_button[persistent._language] xalign 0.5 text_align 0.5
                    
                button action SetVariable("resolution", 0) style style.button["normal"] xpadding 30 yminimum 100 size_group "three":
                    text "{size=-2}Fullscreen\n(1024*600){/size}" style style.preferences_button[persistent._language] xalign 0.5 text_align 0.5
    
                button action SetVariable("resolution", 1) style style.button["normal"] xpadding 30 yminimum 100 size_group "three":
                    text "Windowed" style style.preferences_button[persistent._language] xalign 0.5 text_align 0.5 yalign 0.5
                    
            hbox:      
                button action Preference("transitions", "all") style style.button["normal"] xpadding 35 size_group "toggle2":
                    text "Full animation" style style.preferences_button[persistent._language] xalign 0.5
    
                button action Preference("transitions", "none") style style.button["normal"] xpadding 35 size_group "toggle2":
                    text "Minimal animation" style style.preferences_button[persistent._language] xalign 0.5

            hbox:      
                button action NewLanguage("") style style.button["normal"] xpadding 35 size_group "toggle2" ymargin -9:
                    text "English" style style.preferences_button xalign 0.5
    
                button action NewLanguage("korean") style style.button["normal"] xpadding 35 size_group "toggle2" ymargin -9:
                    text "한글" style style.preferences_button["korean"] xalign 0.5

                button action NewLanguage("japanese") style style.button["normal"] xpadding 35 size_group "toggle2" ymargin -9:
                    text "日本語" style style.preferences_button["japanese"] xalign 0.5

            #button action Show("controls") style style.button["normal"] ymargin -9:
            #    text "Show controls" style style.preferences_button[persistent._language] xalign 0.5 text_align 0.5 minwidth 360
        
init -1 python:
    #thumbnail_offset = { "hyunae":(50,20,85,57), "mute":(80,48,85,57) }
    
    def get_image(name):
        return name.split(",")[0] + " mini"
    #    character_name = name.split(",")[0]
    #    return LiveCrop(thumbnail_offset[character_name.split(" ")[0]], Transform(ImageReference(character_name), zoom=0.3))
        
    def strip_name(name):
        unlocked = "unlocked"
        if config.translator: unlocked = config.translator.translate(unlocked)

        if "," in name:
            return "\n" + name.split(",")[1].replace("unlocked", unlocked)
            
        return ""
        
screen file_picker:
    zorder 103
    
    vbox xalign 0.95 yalign 0.5 spacing 4:
        window background Frame("blackwindow.png", 20, 20) top_padding 6 bottom_padding 15 left_padding 5 right_padding 13 xmaximum 492 xminimum 492:

            text "{b}Sponsor:{/b}{space=63}Saeju Colony Historical Society\n{b}Objective card:{/b} {color=#69f}Download any log files you can, especially any that can explain what happened to the ship. If possible, speak to the security AI *Mute for assistance.{/color}" color "#fff" justify True xalign 0.5 style style.objective[persistent._language]
        
        window top_padding 0 bottom_padding 18 left_padding 15 right_padding 20 xminimum 492:
            has vbox first_spacing -12 spacing 0
            
            window background header2[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -13 xanchor 0 yoffset 2 left_padding 20:
                text "Save files" style style.title[persistent._language]
                
            null height 35
            
            for i in range(1, 5):
                hbox:
                    button style style.button["normal-noselected"] ypadding 15 left_padding 30 right_padding 20 size_group "save" xminimum 330 top_margin -15:
                        action FileSave(i)
                        has hbox spacing 20
                        if FileSaveName(i):
                            add get_image(FileSaveName(i)) ypos -5
                        else:
                            null width 65 height 57
                            
                        # Format the description, and add it as text.
                        $ description = "%s%s" % (
                            FileTime(i, empty=_("Empty Slot.")),
                            strip_name(FileSaveName(i)))
            
                        text description style style.text[persistent._language] bold False yalign 0.5 yoffset -6
            
                        key "save_delete" action FileDelete(i)
                        
                    button style style.button["load" + str(persistent._language)] xminimum 100 action FileLoad(i) yalign 0.5 top_margin -15:
                        text "Load" style style.load[persistent._language]
                        
            hbox:
                button action FilePage("auto") background None:
                    text _("Auto") outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] selected_outlines [ (2, (0,0,0,0), 0, 0) ] style style.pages[persistent._language]
    
                for i in range(1, 5):
                    button action FilePage(i) background None:
                        text ("Page " + str(i)) outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] selected_outlines [ (2, (0,0,0,0), 0, 0) ] style style.pages[persistent._language]
                        
                    
        use preferences_back

screen controls:
    zorder 104

    if persistent.animated_backgrounds:
        add ImageReference("bg white") at bg_fast
    else:
        add ImageReference("bg white static") at bg_fast

    window top_padding 0 bottom_padding 20 xpadding 15 xalign 0.05 yalign 0.5:
        vbox:
            window background header1[current_character] ypadding 0 yminimum 39 xminimum 269 xpos -13 xanchor 0 yoffset 2 left_padding 20:
                text "Controls" size 28 font "fonts/Delicious-Heavy.otf" bold False color (255,255,255,220)
                
            null height 10

            hbox:
                text "Advance" minwidth 240
                vbox:
                    text "Left click" bold False minwidth 200
                    text "Enter" bold False minwidth 180
                    text "Space" bold False minwidth 180

            hbox:
                text "Rollback" minwidth 240
                vbox:
                    text "Mouse wheel" bold False minwidth 180
                    text "Page up/Page down" bold False minwidth 180

            hbox:
                text "Next/Previous page" minwidth 240
                vbox:
                    text "Mouse wheel" bold False minwidth 180
                    text "Left/Right" bold False minwidth 180

            hbox:
                text "Next/Previous block" minwidth 240
                vbox:
                    text "Page up/Page down" bold False minwidth 180

            hbox:
                text "Next/Previous message" minwidth 240
                vbox:
                    text "Page up/Page down" bold False minwidth 180

            hbox:
                text "Back" minwidth 240
                vbox:
                    text "Backspace" bold False minwidth 180

            hbox:
                text "Screenshot" minwidth 240
                vbox:
                    text "Alt-S" bold False minwidth 180
                    text "Cmd-S" bold False minwidth 180

            hbox:
                text "Preferences" minwidth 240
                vbox:
                    text "Right click" bold False minwidth 180

    window background None yalign 0.95 xalign 0.95 xoffset 16 xpadding 0 xmargin 0 ypadding 0 ymargin 0:  
        window top_padding 8 bottom_padding 15 xpadding 40 xalign 1.0:
            button background "back.png" hover_background ("back-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("controls", Dissolve(0.5)) ] left_padding 32:
                text "Back" outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character]
        
screen preferences_back:
    default action = [ ]
             
    window top_padding 8 bottom_padding 15 xpadding 40 xalign 1.0:
        button background "back.png" hover_background ("back-" + current_character[0] + "hover.png") xminimum 32 yminimum 32 action ([ Play("sound", "sfx/fxbeep4.mp3"), Hide("preferences", Dissolve(0.5)), Hide("preferences_back", Dissolve(0.5)), Hide("file_picker", Dissolve(0.5)), Hide("bonus", Dissolve(0.5)), Hide("messages_overlay", Dissolve(0.5)) ] + action) left_padding 32:
            text "Back" outlines [ (2, (0,0,0,0), 0, 0) ] hover_outlines hover_outlines[current_character] style style.text[persistent._language]

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0
    
screen quit:
    modal True
    zorder 105
    
    key "K_ESCAPE" action Hide("quit")
    #if not store.game_playing:
    #        $ Quit(False)()

    if persistent.animated_backgrounds:
        add ImageReference("bg white") at bg_fast
    else:
        add ImageReference("bg white static") at bg_fast

    window at fast_fade:
        ypos .1
        yanchor 0
        top_padding 40 bottom_padding 10
        
        has vbox:
            xalign .5
            yalign .5
            spacing 0
            
        text "Are you sure you want to quit?":
            xalign 0.5 style style.text[persistent._language]
            
        null height 20

        hbox:
            xalign 0.5
            spacing 10
                
            button action [ Play("sound", "sfx/fxbeep2.mp3"), Hide("main_screen"), MainMenu(False) ] style style.button["normal"] size_group "quit_button" ymargin -5:
                text "Main Menu" xalign 0.5 style style.text[persistent._language]
                
            button action Quit(False) style style.button["normal"] size_group "quit_button" ymargin -5:
                text "Quit" xalign 0.5 style style.text[persistent._language]
                
        button action [ Play("sound", "sfx/fxbeep4.mp3"), Hide("quit") ] style style.button["normal"] size_group "quit_button" xalign 0.5:
                text "Cancel" xalign 0.5 style style.text[persistent._language]


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

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
                text  _("Yes") style style.text[persistent._language]
            button action no_action background Frame("mainmenubutton.png", 30, 30) hover_background Frame("mainmenubutton-hover.png", 30, 30) xpadding 80 bottom_padding 30 top_padding 20:
                text _("No") style style.text[persistent._language]


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5

screen demo_ended:
    
    zorder 102
    modal True

    if not renpy.demo_mode:
        timer .5 action [ Hide("demo_ended"), Jump("loop") ]
    
    if persistent.animated_backgrounds:
        add ImageReference("bg white") at bg_fast
    else:
        add ImageReference("bg white static") at bg_fast

    window top_padding 30 bottom_padding 40 xpadding 50 xalign 0.5 yalign 0.5:
        has vbox spacing 30

        text "The free trial has now ended. But if you install the full version of Analogue: A Hate Story, you can continue right from your last save!" bold False size 22 justify True style style.text[persistent._language]

        hbox xalign 0.5:
            button background "mainmenubutton.png" hover_background "mainmenubutton-hover.png" xminimum 300 yminimum 100 insensitive_background "mainmenubutton-idle.png" action buyurl:
                vbox xalign 0.5 xoffset 10 yalign 0.5:
                    text "Buy full version" size 32 minwidth 200 text_align 0.5 style style.menu_button[persistent._language]
                    text "at ahatestory.com" size 18 bold False minwidth 200 text_align 0.5 style style.menu_button[persistent._language]

            button background Frame("mainmenubutton.png", 30, 30) hover_background Frame("mainmenubutton-hover.png", 30, 30) left_padding 30 right_padding 45 bottom_padding 30 top_padding 20 yminimum 110 insensitive_background "mainmenubutton-idle.png" action [ Play("sound", "sfx/fxbeep5.mp3"), Show("preferences", Dissolve(0.5)) ] xmargin 10:
                text "Save" size 28 xalign 0.5 xoffset 10 yalign 0.5 style style.menu_button[persistent._language]


    use bottom_menu
        
