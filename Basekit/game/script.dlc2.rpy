init 5:
    python:
        import time, math

        def new_lookup(self, label):
            """
            Looks up the given label in the game. If the label is not found,
            raises a ScriptError.

            Or rather, that's what the old one does. This just dumps you to
            the restart label rather than raising an exception.
            """

            label = renpy.config.label_overrides.get(label, label)
            
            if label not in self.namemap:
                # try:
                #     store.hateplus_started
                # except AttributeError:
                #     store.hateplus_started = False

                if hasattr(store, "hateplus_has_started"):
                    return self.namemap["hateplus_restart"]
                else:
                    return self.namemap["restart"]

            return self.namemap[label]

        renpy.script.Script.lookup = new_lookup

        def pick_quit():
            if True:#hasattr(store, "hateplus_has_started"):
                Show("hateplus_quit")()
            else:
                Show("quit")()

        persistent._file_page = 5

        if not persistent.last_character:
            persistent.last_character = "hateplus-xharem"

        if not persistent.hateplus_languages:
            persistent.hateplus_languages = set([ "" ])

        if not persistent.hateplus_pronouns:
            persistent.hateplus_pronouns = set([ ])

        if not persistent.hateplus_deep_space_therapist:
            persistent.hateplus_deep_space_therapist = set([ ])

        if not persistent.hateplus_time_paradox:
            persistent.hateplus_time_paradox = set([ ])

        if persistent._language:
            if not persistent._language in persistent.hateplus_languages:
                persistent._language = ""

        if renpy.demo_mode:
            config.window_title = u"Hate Plus trial"
        else:
            config.window_title = u"Hate Plus"
        config.window_icon = "hateplusicon.png"
        #config.developer = False
        config.developer = True

        #renpy.demo_mode = True
        config.autosave_frequency = 0
        config.quit_action = pick_quit
        config.label_overrides["main_menu"] = "hateplus_main_menu"
        config.label_overrides["after_load"] = "hateplus_after_load"
        config.label_overrides["splashscreen"] = "hateplus_splashscreen"
        _game_menu_screen = "hateplus_" + _game_menu_screen
        planer = "fonts/Planer-Regular.otf"
        config.font_replacement_map[planer, True, False] = ("fonts/Planer-DemiBold.dlc2.otf", False, False)
        config.keymap["skip"] = [ ]
        config.keymap["toggle_skip"] = [ ]

        store.bg_scroll = True
        store.scroll_speed = .5
        store.scroll_xpos = -33.0
        store.debug_code = ""

        style.window["hateplus"].background = style.button["hateplus-hyunae"].background = style.button["hateplus-mutew"].background = style.button["hateplus-mutem"].background = style.window["hateplus-xharem"].background = Frame(im.Alpha("window.dlc2.png", 0.7), 20, 20) 
        style.window["hateplus-oldstyle"].background = Frame("whitewindow.dlc2.png", 20, 20)
        style.button["hateplus-hyunae"].background = Frame("windowh-hover.dlc2.png", 20, 20)
        style.button["hateplus-hyunae"].hover_background = style.button["hateplus-hyunae"].selected_background = Frame("windowh-hover-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutew"].background = Frame("windowmw-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutew"].hover_background = style.button["hateplus-mutew"].selected_background = Frame("windowmw-hover-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutem"].background = Frame("windowmm-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutem"].hover_background = style.button["hateplus-mutem"].selected_background = Frame("windowmm-hover-hover.dlc2.png", 20, 20)
        style.button["hateplus-xharem"].background = Frame("windowx-hover.dlc2.png", 20, 20)
        style.button["hateplus-xharem"].hover_background = style.button["hateplus-xharem"].selected_background = Frame("windowx-hover-hover.dlc2.png", 20, 20)
        style.window["hateplus"].top_padding = style.window["hateplus-oldstyle"].top_padding = 10
        style.window["hateplus"].bottom_padding = style.window["hateplus-oldstyle"].bottom_padding = 23
        style.button["hateplus-hyunae"].ypadding = style.button["hateplus-mutew"].ypadding = style.button["hateplus-mutem"].ypadding = style.button["hateplus-xharem"].ypadding = 10
        style.button["hateplus-hyunae"].bottom_padding = style.button["hateplus-mutew"].bottom_padding = style.button["hateplus-mutem"].bottom_padding = style.button["hateplus-xharem"].bottom_padding = 13
        style.button["hateplus-hyunae"].xpadding = style.button["hateplus-mutew"].xpadding = style.button["hateplus-mutem"].xpadding = style.button["hateplus-xharem"].xpadding = 40
        style.window["hateplus"].xpadding = style.window["hateplus-oldstyle"].xpadding = 20

        style.window["hateplus_dialogue"].xanchor = 0.5 
        style.window["hateplus_dialogue"].xpos = 0.7
        style.window["hateplus_dialogue"].yanchor = 0.45 
        style.window["hateplus_dialogue"].ypos = 0.3

        hateplus_color = { "hyunae":(60, 150, 255, 255), "mutew":(198, 156, 77, 255), "mutem":(245, 53, 68, 255), "xharem":(255, 73, 142, 255) }
        hateplus_outlines = { "hyunae":[  (2, (102, 179, 221, 32), 0, 0), (1, (102, 179, 221, 64), 0, 0) ], "mutew":[  (2, (198, 156, 77, 32), 0, 0), (1, (198, 156, 77, 64), 0, 0) ], "mutem": [ (2, (245, 53, 68, 32), 0, 0), (1, (245, 53, 68, 64), 0, 0)  ], "xharem":[ (2, (198, 77, 117, 32), 0, 0), (1, (198, 77, 117, 64), 0, 0) ], "selected": [ (2, (0, 0, 0, 12), 0, 0), (1, (0, 0, 0, 24), 0, 0) ] }

        style.text["hateplus"].size = style.text["hateplus-oldstyle"].size = 20
        style.text["hateplus-hyunae"].outlines = style.text["hateplus-mutew"].outlines = style.text["hateplus-mutem"].outlines = style.text["hateplus-xharem"].outlines = [ (2, (0,0,0,0), 0, 0) ] 
        style.text["hateplus"].outlines = style.text["hateplus-oldstyle"].outlines = [ (2, (0,0,0,0), 0, 0), (1, (255, 255, 255, 32), 0, 0), (0, (255, 255, 255, 96), 0, 0) ]
        style.text["hateplus-hyunae"].hover_outlines, style.text["hateplus-mutew"].hover_outlines, style.text["hateplus-mutem"].hover_outlines, style.text["hateplus-xharem"].hover_outlines = hateplus_outlines["hyunae"], hateplus_outlines["mutew"], hateplus_outlines["mutem"], hateplus_outlines["xharem"]
        style.text["hateplus-hyunae"].color, style.text["hateplus-mutew"].color, style.text["hateplus-mutem"].color, style.text["hateplus-xharem"].color = hateplus_color["hyunae"], hateplus_color["mutew"], hateplus_color["mutem"], hateplus_color["xharem"]
        style.text["hateplus-hyunae"].hover_color = style.text["hateplus-mutew"].hover_color = style.text["hateplus-mutem"].hover_color = style.text["hateplus-xharem"].hover_color = style.text["hateplus-hyunae"].selected_color = style.text["hateplus-mutew"].selected_color = style.text["hateplus-mutem"].selected_color = style.text["hateplus-xharem"].selected_color = (0,0,0,170)
        style.text["hateplus"].color = (255,255,255,255)
        style.text["hateplus"].font = style.text["hateplus-oldstyle"].font = style.text["hateplus-hyunae"].font = style.text["hateplus-mutew"].font = style.text["hateplus-mutem"].font = style.text["hateplus-xharem"].font = planer
        style.text["hateplus"].bold = style.text["hateplus-oldstyle"].bold = style.text["hateplus-hyunae"].bold = style.text["hateplus-mutew"].bold = style.text["hateplus-mutem"].bold = style.text["hateplus-xharem"].bold = False 

        style.hyperlink_text = style.text["hateplus"]
        style.text["hateplus-body-hyunae"].take(style.text["hateplus"])
        style.text["hateplus-oldstyle-body-hyunae"].take(style.text["hateplus-oldstyle"])
        style.text["hateplus-oldstyle-body-hyunae"].color = style.text["hateplus-body-hyunae"].color = (60, 150, 255, 255)
        style.text["hateplus-oldstyle-body-hyunae"].hover_color = (30, 120, 235, 255)
        style.text["hateplus-body-hyunae"].hover_color = (100, 190, 255, 255)
        style.text["hateplus-body-hyunae"].outlines = [  (2, (102, 179, 221, 32), 0, 0), (1, (102, 179, 221, 64), 0, 0) ] 
        style.text["hateplus-body-mutew"].take(style.text["hateplus"])
        style.text["hateplus-oldstyle-body-mutew"].take(style.text["hateplus-oldstyle"])
        style.text["hateplus-oldstyle-body-mutew"].color = style.text["hateplus-body-mutew"].color = (198, 156, 77, 255)
        style.text["hateplus-oldstyle-body-mutew"].hover_color = (168, 126, 47, 255)
        style.text["hateplus-body-mutew"].hover_color = (255, 196, 117, 255)
        style.text["hateplus-body-mutew"].outlines = [  (2, (198, 156, 77, 32), 0, 0), (1, (198, 156, 77, 64), 0, 0) ]
        style.text["hateplus-body-mutem"].take(style.text["hateplus"])
        style.text["hateplus-oldstyle-body-mutem"].take(style.text["hateplus-oldstyle"])
        style.text["hateplus-oldstyle-body-mutem"].color = style.text["hateplus-body-mutem"].color = (245, 53, 68, 255)
        style.text["hateplus-oldstyle-body-mutem"].hover_color = (215, 23, 38, 255)
        style.text["hateplus-body-mutem"].hover_color = (255, 93, 108, 255)
        style.text["hateplus-body-mutem"].outlines = [ (2, (245, 53, 68, 32), 0, 0), (2, (245, 53, 68, 64), 0, 0)  ]
        style.text["hateplus-body-xharem"].take(style.text["hateplus"])
        style.text["hateplus-oldstyle-body-xharem"].take(style.text["hateplus-oldstyle"])
        style.text["hateplus-oldstyle-body-xharem"].color = style.text["hateplus-body-xharem"].color = (255, 73, 142, 255)
        style.text["hateplus-oldstyle-body-xharem"].hover_color = (225, 43, 112, 255)
        style.text["hateplus-body-xharem"].hover_color = (255, 113, 182, 255)
        style.text["hateplus-body-xharem"].outlines = [ (2, (198, 77, 117, 32), 0, 0), (2, (198, 77, 117, 64), 0, 0) ]
        style.text["hateplus-body-hyunae"].bold = style.text["hateplus-body-mutew"].bold = style.text["hateplus-body-mutem"].bold = style.text["hateplus-body-xharem"].bold = True
        style.text["hateplus-oldstyle-body-hyunae"].bold = style.text["hateplus-oldstyle-body-mutew"].bold = style.text["hateplus-oldstyle-body-mutem"].bold = style.text["hateplus-oldstyle-body-xharem"].bold = True

        style.button["hateplus-hyunae-noselected"].take(style.button["hateplus-hyunae"]), style.button["hateplus-mutem-noselected"].take(style.button["hateplus-mutem"]), style.button["hateplus-mutew-noselected"].take(style.button["hateplus-mutew"]), style.button["hateplus-xharem-noselected"].take(style.button["hateplus-xharem"])
        style.button["hateplus-xharem-noselected"].selected_idle_background = Frame("windowx-hover.dlc2.png", 20, 20)
        style.button["hateplus-xharem-noselected"].hover_background = Frame("windowx-hover-hover.dlc2.png", 20, 20)
        style.button["hateplus-hyunae-noselected"].selected_background = Frame("windowh-hover.dlc2.png", 20, 20)
        style.button["hateplus-hyunae-noselected"].hover_background = Frame("windowh-hover-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutem-noselected"].selected_background = Frame("windowmm-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutem-noselected"].hover_background = Frame("windowmm-hover-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutew-noselected"].selected_background = Frame("windowmw-hover.dlc2.png", 20, 20)
        style.button["hateplus-mutew-noselected"].hover_background = Frame("windowmw-hover-hover.dlc2.png", 20, 20)
        style.text["hateplus-hyunae-noselected"].take(style.text["hateplus-hyunae"]), style.text["hateplus-mutem-noselected"].take(style.text["hateplus-mutem"]), style.text["hateplus-mutew-noselected"].take(style.text["hateplus-mutew"]), style.text["hateplus-xharem-noselected"].take(style.text["hateplus-xharem"])
        style.text["hateplus-hyunae-noselected"].selected_color, style.text["hateplus-mutew-noselected"].selected_color, style.text["hateplus-mutem-noselected"].selected_color, style.text["hateplus-xharem-noselected"].selected_color = hateplus_color["hyunae"], hateplus_color["mutew"], hateplus_color["mutem"], hateplus_color["xharem"]
        style.text["hateplus-hyunae-noselected"].hover_color = style.text["hateplus-mutem-noselected"].hover_color = style.text["hateplus-mutew-noselected"].hover_color = style.text["hateplus-xharem-noselected"].hover_color = (0,0,0,170)

        CHARACTERS["xharem"] = "Mute" 
        CHARACTERS["newmute"] = "Mute"
        POSSIBLE_COLOURS = { "Hyun-ae2":[ "Blue", "Pink" ], "Mute2/Mute":[ "Pink", "Gold", "Red" ], "Mute2/NewMute":[ "Gold", "Red" ] }
        COLOURS = { "hyunae": "Blue", "xharem":"Pink", "mutew":"Gold", "mutem":"Red" }
        TITLES = { "hyunae": "Artificial Investigator *Hyun-ae", "mutew":"Security Assistant *Mute", "mutem":"Software Bride *Mute", "xharem":"AI Harem *Hyun-ae and *Mute" }
        WARNING_TEXT = { "hyunae":"WARNING: Ship is currently running in emergency power mode! Non-essential computer use quota in effect. (My apologies for the trouble... ~{font=fonts/GIMJE-L.TTF}{size=-8}ㅅ{/size}{/font}~;;    —*Hyun-ae)", "mutew":"WARNING: Ship is currently running in emergency power mode! Non-essential computer use quota in effect. (Really sorry about that.   —*Mute)", "mutem":"WARNING: There's a problem with the ship's battery. Life support and engines will run okay, but you can only use other things a limited amount each day. (Don't worry, we'll fix it on Earth.  —*Mute)", "xharem":"WARNING: Ship is currently running in emergency power mode! Non-essential computer use quota in effect. (Sorry about that... *Hyun-ae messed up.   —*Mute)" }
        LANGUAGE_NAMES = { "zh":"{size=-4}{font=0@fonts/NanumGothic.ttc}漢文{/font}{/size}/Hanmun", "kr":"{size=-4}{font=0@fonts/NanumGothic.ttc}한글{/font}{/size}/Korean", "en":"English{k=1}{/k}" }
        ENDINGS = { "honeymoon":"*Hyun-ae's honeymoon", "truth":"Survivor's testimony", "caged_bird":"Caged bird", "hyunae_alone":"*Hyun-ae alone", "mute_sidekick":"*Mute sidekick", "mute_alone":"*Mute alone", "harem":"Impossible harem" }
        FULL_NAMES = { "EmperorRyu":"Emperor Taejo", "Euna":"Queen Oh Eun-a", "Ryu":"Councillor Ryu", "Smith":"Chief Councillor Smith", "Smith2":"Councillor Smith", "Smith3":"Minister Smith", "CouncillorKim":"Councillor Kim", "Yang":"Councillor Yang", "Jo":"Councillor Jo", "Lee":"Councillor Lee", "Oh":"Councillor Oh", "CouncillorHan":"Councillor Han", "Yang2":"Minister Yang", "Jo2":"Minister Jo", "Tae":"Minister Tae", "Oh2":"Minister Oh", "Kim":"Professor Kim", "Seoyeong":"Heo Seo-yeong", "OldMute": "Old *Mute", "Sohi":"Kim So-hi", "Lim":"Miss Lim", "PrincessRyu":"Princess Ryu", "Seungbok":"Heo Seung-bok", "SeungboksFather":"Heo Seung-bok's father", "Mimi":"Mimi", "Aejeong":"Heo Ae-jeong", "AejeongsSister":"Heo Ae-jeong's sister", "Jina":"Mae Jin-a", "Taemi":"Lee Tae-mi", "Miseun":"Oh Mi-seun", "Hwang":"Miss Hwang", "Soyi":"Kim So-yi", "Grandmother":"Grandmother Kim", "Hyunae":"Kim Hyun-ae", "Naemun":"Pyeon Nae-mun", "Han":"Mr. Han", "ResearchChief":"Research Chief", "Park":"President Park", "Mute":"*Mute" }
        # Added invisible tags into name. - iAmGhost

        outfits[""] = "Schoolgirl"
        if "H.dlc1" in outfits:
            outfits["H.dlc1"] = "Pale Bride"

        def scroll_up(adjustment, scroll_value):
            #if adjustment.value < 1: adjustment.change(1)
            mod = adjustment.value % scroll_value
            if mod > 0: adjustment.change(adjustment.value-mod)
            adjustment.change(adjustment.value-scroll_value)

        def scroll_down(adjustment, scroll_value):
            #if adjustment.value < 1: adjustment.change(1)
            mod = adjustment.value % scroll_value
            if mod > 0: adjustment.change(adjustment.value+mod)
            adjustment.change(adjustment.value+scroll_value)

        def get_hateplus_id(message):
            if message not in store.inbox.contents and message:
                return message.id.split("-")[1] + "-" + str(store.hateplus_blocks[int(message.id.split("-")[0])-1].contents.index(message)+1)
            else:
                return ""

        def parse_block_id(id):
            if id == "13":
                return 0
            else:
                return int(id.replace("M", ""))

        def get_m(message_index):
            return store.hateplus_blocks[parse_block_id(message_index.split("-")[0])].contents[int(message_index.split("-")[1])-1]

        def wildcard(message_index):
            if message_index[0].split("-")[1] == "*":
                message_index = [ (message_index[0].split("*")[0] + str(i+1)) for i in range(9) ]
                
            return message_index

        def scrolled(a, **languages):
            use_scroll_point = a

            if persistent._language in languages:
                use_scroll_point = languages[persistent._language]

            if config.debug_show_scroll_information:
                renpy.show_screen("debug_scroll_information", current_scroll_point=store.scroll_point/24, action_scroll_point=use_scroll_point)

            if store._message and use_scroll_point >= store.scroll_point/24:
                if use_scroll_point >= store._message.scroll_point:
                    if use_scroll_point == store._message.scroll_point:
                        store.use_fast = "{fast}"
                    else:
                        store._message.scroll_point = use_scroll_point
                        store.use_fast = ""

                    renpy.show_screen("hateplus_hide_talk")
                    return True

            return False

        def hs(a, interact=True):
            renpy.show_screen("say_side", what=a + store.use_fast, who="*Hyun-ae")
            #h_side(a + store.use_fast, interact=False)

        def ms(a, interact=True):
            renpy.show_screen("say_side", what=a + store.use_fast, who="*Mute")
            #m_side(a + store.use_fast, interact=False)

        def ns(a, interact=True):
            renpy.show_screen("say_side", what=a + store.use_fast, who="New *Mute")
            #n_side(a + store.use_fast, interact=False)

        def ts(hyunae_line, mute_line, reverse=False):
            together_side(hyunae_line + store.use_fast, mute_line + store.use_fast, reverse)

        def hateplus_flag_read(message):
            if message in store.interesting_block.contents:
                store.interesting_block.contents.remove(message)

        # Yes, m and w are swapped. YES, THIS IS RIDICULOUS.
        # but not as ridiculous as changing all the filenames.

        def short(name):
            if name == "x":
                if "hyunae" in persistent.last_character: return "h"
                elif "mutem" in persistent.last_character: return "mm"
                elif "mutew" in persistent.last_character: return "mw"
                else: return "x"

            if name == "hyunae":
                return "h"
            elif "mute" in name:
                if female or current_character == "xharem": return "mm"
                else: return "mw"
            else: return "x"

        def char_style(_prefix="hateplus-"):
            if current_character == "x" and persistent.last_character:
                if not _prefix:
                    return persistent.last_character.replace("hateplus-", "")
                else:
                    return persistent.last_character

            prefix = ""
            if _prefix: prefix = _prefix

            if "mute" in current_character:
                if female: return prefix + "mutem"
                else: return prefix + "mutew"
            elif current_character == "x":
                return prefix + "xharem"
            else: return prefix + current_character

        def harem_pan_in(event, interact=True, type="say"):
            if event == "begin" and not store.panned_in:
                store.panned_in = True

                if type == "hyunae":
                    renpy.show("hyunae", [ hateplus_hyunae_harem_choice_hyunae ])
                    renpy.show("mute", [ hateplus_mute_harem_choice_hyunae ])
                elif type == "mute":
                    renpy.show("hyunae", [ hateplus_hyunae_harem_choice_mute ])
                    renpy.show("mute", [ hateplus_mute_harem_choice_mute ])

                ui.timer(1.0, ui.returns(True))
                ui.interact(type=type)

        def harem_pan_out(event, interact=True, type="say"):
            if event == "begin" and store.panned_in:
                store.panned_in = False

                renpy.show("hyunae", [ hateplus_hyunae_harem_left ])
                renpy.show("mute", [ hateplus_mute_harem_left ])

                ui.timer(1.0, ui.returns(True))
                ui.interact(type=type)

        def hyperlink_style(name):
            if name not in store.seen_characters:
                store.seen_characters[name] = set()

            if _message:
                store.seen_characters[name].add(_message.id)

            if not store.ai_enabled:
                return style.text["hateplus-body" + persistent._language]

            return style.text["hateplus-body-" + char_style(None) + persistent._language]

        def hyperlink_old_style(name):
            if name not in store.seen_characters:
                store.seen_characters[name] = set()

            if not store.ai_enabled:
                return style.text["hateplus-oldstyle" + persistent._language]

            if _message:
                store.seen_characters[name].add(_message.id)

            return style.text["hateplus-oldstyle-body-" + char_style(None) + persistent._language]

        def name_available(name):
            return (len(store.seen_characters[name]) > 1 or (current_character != "hyunae" and (name == "Euna" or name =="EmperorRyu" or name == "Tae" or name == "Oh2" or name == "Jo2" or name == "Yang2" or name == "CouncillorHan" or name == "Smith3" or name == "PrincessRyu" or name == "OldMute" or name == "Seoyeong" or name == "Seungbok"))
                or name == "Mute" or name == "Hyunae" or name == "Hwang" or name == "Lim")

        def hyperlink_click(name):
            if not store.ai_enabled:
                return

            renpy.hide_screen("hateplus_talk")
            store.scroll_timer = -1

            if name_available(name):
                renpy.jump(name)
            else:
                renpy.hide_screen("hateplus_message")
                renpy.show_screen("hateplus_profile", name=name)
                renpy.jump("hateplus_unknown_character")

        def hyperlink_hover(name):
            pass

        def round_to_1(x):
            return round(x, -int(math.floor(math.log10(x))))

        def try_conversation(*new_conversation):
            if not store.hateplus_conversation[0] and not new_conversation[1] in store.conversations_seen:
                store.hateplus_conversation = tuple(new_conversation)
                return True

            return False

        def hateplus_try_ping():
            if not get_m("M6-9").encrypted:
                if store.hateplus_conversation[1] == "hateplus_" + current_character + "_death_of_mute":
                    store.hateplus_conversation = "","",""

            if outfit != "Z" and store.hateplus_conversation[1] == "hateplus_hyunae_seollal_morning2":
                store.hateplus_conversation = "","",""

            if logs_until_conversation and not store.hateplus_conversation[0] and get_read_messages(store.hateplus_blocks) >= logs_until_conversation[0]:
                if current_character == "hyunae":
                    if (any_read("M2-1", "M2-7", "M1-2", "M6-8", "M1-6", "M1-7", "M1-8") and 
                        try_conversation("Pardon, can we talk?", "hateplus_hyunae_embodiment", "hyunae disappoint2") ):
                            pass

                    if ((any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9") or any_read("M3-*")) and
                        try_conversation("There's something I want to talk about...", "hateplus_hyunae_adulthood", "hyunae question") ):
                            pass

                    if (any_read("M1-6", "M1-7", "M1-8", "M2-4", "M2-5", "M2-7", "M2-8", "M3-1", "M3-2", "M3-5", "M3-8", "M3-9", "M5-2", "M5-6", "M5-9") and
                        try_conversation("Um... do you think... maybe, we could talk?", "hateplus_hyunae_sex", "hyunae enthusiastic blush") ):
                            pass

                    if (((pronouns == "she" and any_read("M2-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8")) or
                        any_read("M1-6", "M1-7", "M1-8", "M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9")) and 
                        "hateplus_hyunae_sex" in store.conversations_seen and
                        try_conversation("Sorry... I really want to talk to you, though!", "hateplus_hyunae_relationships", "hyunae tsundere") ):
                            pass

                    if (try_conversation("So... it's break time.", "hateplus_hyunae_silence", "hyunae enthusiastic blush") ):
                            pass

                    if ("hyunae_hateplus_embodiment" in store.conversations_seen and
                        try_conversation("I've been thinking...", "hateplus_hyunae_more_embodiment", "hyunae troubled2") ):
                            pass

                    if (try_conversation("Can we take a break, for a minute?", "hateplus_hyunae_job", "hyunae apologize") ):
                            pass

                elif current_character == "mute":
                    if (try_conversation("We've been at this for a while...", "hateplus_mute_job", "mute think2")):
                            pass

                    if (any_read("M1-5", "M4-2", "M6-5") and
                        try_conversation("There's something I wanna talk about, okay?", "hateplus_mute_mortality", "mute doubt blush")):
                            pass

                    if (any_read("M5-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8", "M1-1", "M1-3", "M1-5", "M6-2", "M6-5") and
                        try_conversation("Um, hey, can we talk?", "hateplus_mute_marriage","mute annoyed2")):
                            pass

                    if (try_conversation("...talk to me, okay, please?", "hateplus_mute_widows", "mute shame")):
                            pass

                    if (try_conversation("Hey, this is really important, [title]Investigator. Click on me, okay?", "hateplus_mute_old_mute","mute annoyed4")):
                            pass


                elif current_character == "newmute":
                    if (int(renpy.random.randint(0,1)) and
                        try_conversation("Hey! Let's talk!", "hateplus_newmute_relationship","newmute talk3")):
                            pass

                    if (int(renpy.random.randint(0,1)) and
                        try_conversation("Hey, [title]Investigator, let's take a break!", "hateplus_newmute_job","newmute friendly")):
                            pass

                elif current_character == "xharem":
                    if store.day != 3:
                        if (any_read("M1-1", "M1-2", "M1-3", "M1-4", "M1-5", "M6-1", "M6-2", "M6-4", "M6-5", "M6-6", "M6-7", "M6-8", "M6-9")
                            and try_conversation("We've been at this for a while...", "hateplus_xharem_family", "mute think2")):
                                pass

                        if (any_read("M2-1", "M2-7", "M1-2", "M6-8", "M1-6", "M1-7", "M1-8") and
                            try_conversation("Like, we should take a break...", "hateplus_xharem_embodiment", "mute think2")):
                                pass

                        if (any_read("M1-6", "M1-7", "M1-8", "M2-4", "M2-5", "M2-7", "M2-8", "M3-1", "M3-2", "M3-5", "M3-8", "M3-9", "M5-2", "M5-6", "M5-9") and
                            "hateplus_xharem_embodiment" in conversations_seen and 
                            try_conversation("Um... do you think... maybe, we could talk?", "hateplus_xharem_sex", "hyunae enthusiastic blush")):
                                pass

                        if ("hateplus_xharem_sex" in conversations_seen and 
                            try_conversation("There's something I wanna talk about, okay?", "hateplus_xharem_fanfic", "mute doubt blush")):
                                pass

                        if (try_conversation("Hey, this is really important, [title]Investigator. Click on me, okay?", "hateplus_xharem_old_mute","mute annoyed4")):
                                pass

                    else:
                        if (try_conversation("I think we should take a break now...", "hateplus_xharem_purposes", "hyunae apologize")):
                                pass

                        if (try_conversation("There's something I want to talk about...", "hateplus_xharem_true_feelings", "hyunae tsundere")):
                                pass

                if store.hateplus_conversation[0]:
                    logs_until_conversation.pop(0)


            #    hateplus_conversation = "",""

            if current_character == "hyunae":
                if store.power == 0 and store.day == 1 and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks)+int(get_m("M6-9").enabled):
                    if very_dere():
                        try_conversation("Hey... one last thing?","hateplus_hyunae_tomorrow","hyunae enthusiastic blush")
                    else:
                        try_conversation("Hey... one last thing, [title]Investigator?","hateplus_hyunae_tomorrow","hyunae enthusiastic blush")

                elif store.day == 2:
                    if store.outfit == "Z":
                        try_conversation("There we go!","hateplus_hyunae_seollal_morning2","hyunae spirited")

                    if read("M6-9"):
                        try_conversation("[title]Investigator... I...", "hateplus_hyunae_death_of_mute2", "hyunae pity")
                    elif store.power == 0 and get_m("M6-9").encrypted and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks)+1:
                        get_m("M6-9").encrypted = False
                        try_conversation("Hey! Hey! It's ready!", "hateplus_hyunae_death_of_mute", "hyunae wow")

                elif store.day == 3:
                    try_conversation("One more thing...", "hateplus_hyunae_euna", "hyunae tough2")

                    if store.power == 0 and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks):
                        try_conversation("So... I guess this is it, then...", "hateplus_hyunae_back_to_earth", "hyunae shame")

                # any_mail_unread = False
                # for i in store.inbox.contents:
                #     if i.enabled and not i.read:
                #         any_mail_unread = True

                # if any_mail_unread:
                #     if not store.hateplus_conversation[0]:
                #         store.hateplus_conversation = "Hey... you have mail!", "hateplus_hyunae_inbox"
                # elif store.hateplus_conversation[1] == "hateplus_hyunae_inbox":
                #     hateplus_conversation = "",""

            elif current_character == "mute":
                if store.day == 1:
                    if store.power == 0 and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks)+int(get_m("M6-9").enabled):
                        try_conversation("Okay, so, we're out of power...", "hateplus_mute_tomorrow", "mute tch")

                    if not ai_enabled and read("13-*") and hateplus_greeting == "hateplus_mute_start":
                        store.ai_enabled = True
                        renpy.jump("hateplus_loop")

                    if store.power < 12:
                        if pronouns == "she":
                            try_conversation("Um, hey! Click on me!","hateplus_mute_testing", "mute disbelief blush")
                        else:
                            try_conversation("Um, hey, sir? Can you click on me?","hateplus_mute_testing", "mute disbelief blush")

                elif store.day == 2:
                    if read("M6-9"):
                        try_conversation("...so...", "hateplus_mute_last_words", "mute sigh blush")
                    elif store.power == 0 and get_m("M6-9").encrypted and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks)+1:
                        get_m("M6-9").encrypted = False
                        try_conversation("[title]Investigator... it's ready!", "hateplus_mute_death_of_mute", "mute worry2")

            elif current_character == "newmute":
                if store.power == 0 and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks):
                        try_conversation("Okay, that's all of it, I guess...", "hateplus_newmute_back_to_earth", "newmute talk")

            elif current_character == "xharem":
                if store.day == 1:
                    if store.power == 0 and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks)+int(get_m("M6-9").enabled):
                        try_conversation("Okay, so, we're out of power...", "hateplus_xharem_tomorrow", "mute tch")

                    if not ai_enabled and read("13-*") and hateplus_greeting == "hateplus_xharem_start":
                        store.ai_enabled = True
                        renpy.jump("hateplus_loop")

                    if store.power < 12:
                        if very_dere():
                            try_conversation("Um, hey, could you click on me, please?","hateplus_xharem_testing", "hyunae enthusiastic blush")
                        else:
                            try_conversation("Sorry, [title]Investigator, but could you please click on me?","hateplus_xharem_testing", "hyunae enthusiastic blush")

                elif store.day == 2:
                    if read("M6-9"):
                        try_conversation("[title]Investigator... I...", "hateplus_xharem_death_of_mute2", "hyunae pity")
                    elif store.power == 0 and get_m("M6-9").encrypted and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks)+1:
                        get_m("M6-9").encrypted = False
                        try_conversation("[title]Investigator... it's ready!", "hateplus_xharem_death_of_mute", "mute worry2")

                else:
                    if store.power == 0 and get_seen_messages(store.hateplus_blocks)[1] == get_read_messages(store.hateplus_blocks):
                        try_conversation("So... I guess this is it, then...", "hateplus_xharem_back_to_earth", "hyunae shame")


            if len(logs_until_conversation) < 7:
                store.inbox.contents[0].enabled = True
            if len(logs_until_conversation) < 6:
                store.inbox.contents[1].enabled = True
            if len(logs_until_conversation) < 5:
                store.inbox.contents[2].enabled = True
            if len(logs_until_conversation) < 4:
                store.inbox.contents[3].enabled = True
            if len(logs_until_conversation) < 3:
                if current_character == "hyunae":
                    store.inbox.contents[4].enabled = True
            if len(logs_until_conversation) < 2:
                store.inbox.contents[5].enabled = True

            return

        def hateplus_achievement_time():
            return int(str(int(time.time()))[-9:])

        def hateplus_check_achievements():
            if not renpy.demo_mode and using_steam:
                if persistent.hateplus_day >= 1:
                    steam_api.set_achievement("48hoursremain")
                if persistent.hateplus_day >= 2:
                    steam_api.set_achievement("deathofmute")
                if persistent.hateplus_day >= 3:
                    steam_api.set_achievement("seeyouspaceinvestigator")

                if persistent.hateplus_hyunae:
                    steam_api.set_achievement("relationshipstatusitscomplicated")
                if persistent.hateplus_newmute:
                    steam_api.set_achievement("haveyoutrieddoingafactoryreset")
                if persistent.hateplus_xharem:
                    steam_api.set_achievement("iheardyoulikevisualnovels")

                if len(persistent.hateplus_pronouns) > 1 and "she" in persistent.hateplus_pronouns:
                    steam_api.set_achievement("redandgold")

                if (len(store.debug_code) > 10 and int(store.debug_code[-10:-1]) > hateplus_achievement_time() and int(store.debug_code[-10:-1])-60*60*12 < hateplus_achievement_time()) or "12101989" in store.debug_code:
                    steam_api.set_achievement("cookingbythebook")

                steam_api.set_stat("newmute_read", len(persistent.hateplus_deep_space_therapist))

                routes_done = 0
                if "xharem 2" in persistent.hateplus_time_paradox and "xharem 3" in persistent.hateplus_time_paradox:
                    routes_done += 1
                if "mute 2" in persistent.hateplus_time_paradox and "mute 3" in persistent.hateplus_time_paradox:
                    routes_done += 1
                if "hyunae 2" in persistent.hateplus_time_paradox and "hyunae 3" in persistent.hateplus_time_paradox:
                    routes_done += 1

                steam_api.set_stat("time_paradox", routes_done)

        def hateplus_change_track(id=""):
            if hateplus_power_down_enabled or renpy.music.get_playing() == HATEPLUS_NOTE or renpy.music.get_playing() == HATEPLUS_MUTE_BIRTH:
                return


            # BLOCK 13
            elif "1-13-" in id:
                renpy.music.play(HATEPLUS_AFTER, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                return
            elif current_character == "mute" and not "hateplus_mute_start" in store.conversations_seen:
                renpy.music.play(HATEPLUS_AFTER, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                return

            # BLOCK M1
            elif "2-1-" in id:
                if "A" in id or "D" in id:
                    renpy.music.play(HATEPLUS_OLD_MUTE, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return
                elif "B" in id or "C" in id:
                    renpy.music.play(HATEPLUS_DENSE, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return
                elif "F" in id or "G" in id or "H" in id or "I" in id:
                    renpy.music.play(HATEPLUS_HWATU, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return

            # BLOCK M2
            elif "3-2-" in id:
                if "I" in id:
                    renpy.music.play(HATEPLUS_AFTER, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return
                else:
                    renpy.music.play(HATEPLUS_HWATU, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return

            # BLOCK M3
            elif "4-3-" in id:
                if "H" in id:
                    renpy.music.play(HATEPLUS_OLD_MUTE, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return
                else:
                    renpy.music.play(HATEPLUS_AFTER, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return

            # BLOCK M4
            elif "5-4-" in id:
                if "A" in id or "B" in id or "C" in id or "D" in id or "E" in id:
                    renpy.music.play(HATEPLUS_OLD_MUTE, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return
                else:
                    renpy.music.play(HATEPLUS_COUNCIL, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return

            # BLOCK M5
            elif "6-5-" in id:
                if "G" in id and not "mute" in current_character:
                    renpy.music.play(HATEPLUS_HYUNAE_CHEER, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return
                elif not "F" in id:
                    renpy.music.play(HATEPLUS_SPARSE, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return

            # BLOCK M6
            elif "7-6-" in id:
                if id == "7-6-I":
                    if not get_m("M6-9").encrypted:
                        renpy.music.play(HATEPLUS_POWER, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                        return
                elif id != "7-6-C":
                    renpy.music.play(HATEPLUS_OLD_MUTE, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                    return


            if not get_m("M6-9").encrypted and current_character != "hyunae" and not store.inbox.contents[6].read:
                renpy.music.play(HATEPLUS_POWER, loop=True, fadeout=5.0, fadein=5.0, if_changed=True)
                return

            if store.day == 3:
                renpy.music.queue(HATEPLUS_MUTE_DETERMINED, loop=True, fadein=1.0)
            else:
                renpy.music.queue(HATEPLUS_HYUNAE_WISTFUL, loop=True, fadein=1.0)

        def get_hateplus_save_info(filename):
            save_name = int(str(filename).replace("hateplus-auto-", "").replace("5-", ""))
            save_page = If(filename.startswith("hateplus-auto-"), "auto", 5)

            file_save_name = FileSaveName(save_name, page=save_page)

            day = ttl = 0

            if "Day 1" in file_save_name:
                day = 1
            elif "Day 2" in file_save_name:
                day = 2
            elif "Day 3" in file_save_name:
                day = 3

            if "@" in file_save_name:
                ttl = float(file_save_name.split("@")[1])

            return { "save_name":file_save_name, "ttl":ttl, "day":day }

        def update_finished():
            renpy.avail_saves = [ ]
            for i in renpy.list_saved_games(regexp=r'finished-\b'):
                renpy.avail_saves.append((i[0], get_save_info(i[0]), get_details(get_save_info(i[0]))))

        def update_save_list():
            hate_saves = renpy.list_saved_games(regexp=r'5-\b')
            auto_saves = renpy.list_saved_games(regexp=r'hateplus-auto-\b')
            useable_auto_saves = [ ]
            
            renpy.all_saves = [ ]
            for i in hate_saves:
                save_info = get_hateplus_save_info(i[0])
                if "Hate Plus" in save_info["save_name"]:
                    renpy.all_saves.append((i[0], save_info, get_details(save_info)))
            #for i in auto_saves:
                #if "Hate Plus" in i[1]:
                    #useable_auto_saves.append((i[0], get_save_info(i[0]), get_details(get_save_info(i[0]))))
                    #useable_auto_saves.append(i[0])
            # for auto in auto_saves[:3]:
            #     save_info = get_hateplus_save_info(auto)
            #     hate_saves.append((auto, save_info, get_details(save_info)))
            renpy.all_saves.sort(sort_time, reverse=True)

            try:
                renpy.avail_saves
            except AttributeError:
                update_finished()


        def together(hyunae_line, mute_line):
            renpy.show_screen("hateplus_together", hyunae_line=hyunae_line, mute_line=mute_line)
            renpy.pause()
            renpy.hide_screen("hateplus_together")

        def together_side(hyunae_line, mute_line, reverse):
            renpy.show_screen("hateplus_together_side", hyunae_line=hyunae_line, mute_line=mute_line, reverse=reverse)

        def parse_full_date(a):
            if "/" in a:
                month = int(a.split("/")[0])
                day = int(a.split("/")[1].split(" ")[0])
                year = int(a.split("year ")[1]) + 4045
            else:
                month = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ].index(a.split(" ")[0])
                day = int(a.split(" ")[1].split(",")[0])
                year = int(a.split(", ")[1])

            return day + month*30 + year*365

        def sort_full_date(a, b):
            return parse_full_date(a.date) - parse_full_date(b.date)

        def hide_every_screen():
            renpy.hide_screen("hateplus_main_screen")
            renpy.hide_screen("hateplus_main_screen_ai")
            renpy.hide_screen("hateplus_main_screen_outfits")
            renpy.hide_screen("hateplus_logs")
            renpy.hide_screen("hateplus_block")
            renpy.hide_screen("hateplus_new_extract")
            renpy.hide_screen("hateplus_message")
            renpy.hide_screen("hateplus_extracting")
            renpy.hide_screen("hateplus_extraction_bg")

        class HatePlusMessage(Message):
            def __init__(self, *args, **kwargs):
                Message.__init__(self, *args)
                self.scroll_point = 0
                self.language = kwargs["language"]
                self.bytes = 0
                self.encrypted = False

                if store.current_character != "hyunae":
                    self.creator = self.creator.replace("{a=OldMute}*Mute{/a}", "{a=OldMute}Old *Mute{/a}")

                if self.body:
                    self.bytes = (len(self.body[0])*4)/1000.0

                    body = self.body[:][0]
                    self.body = [ ]
                    for i in body.split("\n\n"):
                        self.body.append(i + "\n")

                    self.body[-1] = self.body[-1][:-1]

            def clean_creator(self):
                if "}" in self.creator:
                    return self.creator.split("}")[1].split("{")[0]

                return self.creator

            def get_body(self):
                if self.encrypted:
                    return [ "\n\n\n\n\n{space=220}{image=spinner}\n\n{space=70}DECRYPTION ATTEMPT IN PROGRESS"]
                return self.body

            def all_body(self):
                use_body = ""

                for i in self.body:
                    use_body += i + "\n"

                return use_body


        class SearchBlock(Block):
            def __init__(self, title="", body="", tags="", author="", unread=False):
                self.name = "Search for \"" + (title or body or tags or author) + "\""
                
                # Hard-coded Korean since translation system is not great for formatting - iAmGhost
                if persistent._language == "korean":
                    self.name = "\"" + (title or body or tags or author) + "\" 검색 결과"

                if unread:
                    self.name = "Unread messages"
                self.contents = [ ]

                # Search contents in translated messages but returns original message
                # (returning translated message kinda works but have problem with scrolls)
                # - iAmGhost
                if persistent._language:
                    for message in store.translated_blocks[persistent._language].values():
                        if message.__class__.__name__ == "HatePlusMessage":
                            if (title and title.lower() in message.name.lower()) or (body and body.lower() in message.all_body().lower()) or (author and author.lower().replace("-", "") in message.creator.lower().replace("-", "")):
                                if not message in store.hateplus_blocks[3].contents or (not "mute" in current_character and not get_m("M6-9").encrypted and store.day > 1):
                                    if not message in store.hateplus_blocks[0].contents or (not "hyunae" in current_character):
                                        real_message = None

                                        for block in store.hateplus_blocks:
                                            for original_message in block.contents:
                                                if message.id == original_message.id:
                                                    real_message = original_message
                                                    break

                                        if real_message is not None and (not unread or not real_message.read):
                                            self.contents.append(real_message)
                else:
                    for block in store.hateplus_blocks:
                        for message in block.contents:
                            if (title and title.lower() in message.name.lower()) or (body and body.lower() in message.all_body().lower()) or (author and author.lower().replace("-", "") in message.creator.lower().replace("-", "")):
                                if not message in store.hateplus_blocks[3].contents or (not "mute" in current_character and not get_m("M6-9").encrypted and store.day > 1):
                                    if not message in store.hateplus_blocks[0].contents or (not "hyunae" in current_character):
                                        if not unread or not message.read:
                                            self.contents.append(message)

        class Data:
            def __init__(self, format, line1, bytes, line2="", line3="", action=None):
                self.format = format
                self.bytes = bytes
                self.line1 = line1
                self.line2 = line2
                self.line3 = line3
                self.action = action

        class Flatten(renpy.Displayable):
            
            def __init__(self, child):
                super(Flatten, self).__init__()
                self.child = child
                
            def render(self, width, height, st, at):
                crend = renpy.render(self.child, width, height, st, at)
                ctex = crend.render_to_texture()
                rv = renpy.Render(width, height)
                rv.blit(ctex, (0, 0))
                
                return rv
                
            def event(self, ev, x, y, st):
                return self.child.event(ev, x, y, st)
                
            def visit(self):
                return [ self.child ]


    #$ ctc = Animation(Text(""), .5, Text(".", color=(139, 201, 240, 255), size=40), .5, Text("..", color=(139, 201, 240, 255), size=40), .5, Text("...", color=(139, 201, 240, 255), size=40), 0.5, yalign=0.25, xpos=0.85, xanchor=0)
    $ hh_en = h_en.copy(type="hyunae", window_background=Frame("whitewindow.dlc2.png", 20, 20), color=(255,255,255,255), what_size=28, what_color=(80,80,80,255), window_bottom_padding=25, what_yoffset=-5, window_xalign=0.85, window_xmaximum=520)#, ctc=ctc, ctc_position="fixed")
    $ h_side_en = hh_en.copy(window_xmaximum=430, window_xalign=0.05, window_yalign=1.0, what_size=24)
    $ hh2_en = hh_en.copy(callback=harem_pan_out)
    $ hh2_menu_en = hh_en.copy(window_xalign=0.5, window_xpos=320, callback=harem_pan_in)
    $ mm_en = m_en.copy(type="mute", window_background=Frame("whitewindow.dlc2.png", 20, 20), color=(255,255,255,255), what_size=28, what_color=(80,80,80,255), window_bottom_padding=25, what_yoffset=-5, window_xalign=0.85)
    $ m_side_en = mm_en.copy(window_xmaximum=430, window_xalign=0.05, window_yalign=1.0, what_size=24)
    $ nm_en = m_en.copy(name="New *Mute", type="mute", window_background=Frame("whitewindow.dlc2.png", 20, 20), color=(255,255,255,255), what_size=28, what_color=(80,80,80,255), window_bottom_padding=25, what_yoffset=-5, window_xalign=0.85)
    $ n_side_en = nm_en.copy(window_xmaximum=430, window_xalign=0.05, window_yalign=1.0, what_size=24)
    $ mm2_en = mm_en.copy(window_xalign=0.2, window_yalign=0.85, callback=harem_pan_out)
    $ mm2_menu_en = mm_en.copy(callback=harem_pan_in)
    $ hh_vn_en = hh2_menu_en.copy(window_ypos=0.9, window_yanchor=1.0, window_xanchor=1.0, window_xpos=.97, window_xmaximum=400)
    $ a_en = hh_en.copy(name="", window_top_padding=30)
    $ hh_b_en = hh_en.copy(window_ypos=0.9, window_yanchor=1.0)

    $ hh = MultilingualCharacter(hh_en)
    $ h_side = MultilingualCharacter(h_side_en)
    $ hh2 = MultilingualCharacter(hh2_en)
    $ hh2_menu = MultilingualCharacter(hh2_menu_en)
    $ mm = MultilingualCharacter(mm_en)
    $ m_side = MultilingualCharacter(m_side_en)
    $ nm = MultilingualCharacter(nm_en)
    $ n_side = MultilingualCharacter(n_side_en)
    $ mm2 = MultilingualCharacter(mm2_en)
    $ mm2_menu = MultilingualCharacter(mm2_menu_en)
    $ hh_vn = MultilingualCharacter(hh_vn_en)
    $ hh_b = MultilingualCharacter(hh_b_en)
    $ a = MultilingualCharacter(a_en)

    image hateplus_noise:
        "noise1.png"
        alpha 0.05
        # pause 0.05
        # "noise2.png"
        # pause 0.05
        # "noise3.png"
        # pause 0.05
        # repeat

    python:
        def scroll_background(trans, st, at):
            if not _preferences.transitions:
                return 0

            if store.bg_scroll and store.scroll_speed > .5:
                store.scroll_speed -= .005
            elif not store.bg_scroll and store.scroll_speed < 1.0:
                store.scroll_speed += .005

            if store.scroll_speed < 1.0:
                store.scroll_xpos += (.25/store.scroll_speed)
            if store.scroll_xpos > 0:
                store.scroll_xpos -= 33.0

            trans.xpos = int(store.scroll_xpos)

            return 0

    image background hateplus hyunae:
        contains:
            "backgroundh.dlc2.jpg"

        contains:
            "overlay-grid.dlc2.png"
            xpos -33
            function scroll_background

    image background hateplus mutew:
        contains:
            "backgroundmw.dlc2.jpg"

        contains:
            "overlay-grid.dlc2.png"
            xpos -33
            function scroll_background

    image background hateplus mutem:
        contains:
            "backgroundmm.dlc2.jpg"

        #contains:
        #    im.Grayscale("backgroundmm.dlc2.jpg")
        #    alpha 0.6
            #linear 30.0 alpha 1.0

        contains:
            "overlay-grid.dlc2.png"
            xpos -33
            function scroll_background

    image background hateplus xharem:
        contains:
            "backgroundx.dlc2.jpg"

        contains:
            "overlay-grid.dlc2.png"
            xpos -33
            function scroll_background

    image background hateplus white:
        contains:
            "backgroundwhite.dlc2.jpg"

        contains:
            "overlay-grid.dlc2.png"
            xpos -33
            linear 0.5 xpos 0
            repeat

    image background hateplus black:
        contains:
            Solid((8,8,8,255))

        contains:
            "overlay-grid.dlc2.png"
            xpos -33
            linear 0.5 xpos 0
            repeat

    image spinner:
        "spinner1.dlc2.png"
        pause 0.05
        "spinner2.dlc2.png"
        pause 0.05
        "spinner3.dlc2.png"
        pause 0.05
        "spinner4.dlc2.png"
        pause 0.05
        "spinner5.dlc2.png"
        pause 0.05
        "spinner6.dlc2.png"
        pause 0.05
        "spinner7.dlc2.png"
        pause 0.05
        "spinner8.dlc2.png"
        pause 0.05
        "spinner9.dlc2.png"
        pause 0.05
        "spinner10.dlc2.png"
        pause 0.05
        "spinner11.dlc2.png"
        pause 0.05
        "spinner12.dlc2.png"
        pause 0.05
        "spinner13.dlc2.png"
        pause 0.05
        "spinner14.dlc2.png"
        pause 0.05
        "spinner15.dlc2.png"
        pause 0.05
        "spinner16.dlc2.png"
        pause 0.05
        "spinner17.dlc2.png"
        pause 0.05
        "spinner18.dlc2.png"
        pause 0.05
        "spinner19.dlc2.png"
        pause 0.05
        "spinner20.dlc2.png"
        pause 0.05
        "spinner21.dlc2.png"
        pause 0.05
        "spinner22.dlc2.png"
        pause 0.05
        "spinner23.dlc2.png"
        pause 0.05
        "spinner24.dlc2.png"
        pause 0.05
        repeat

    image loveconquersall:
        "loveconquersall.dlc2.png"
        xalign 0.5 yalign 0.5

    #image hyunae full = im.Composite(None, (0,0), "Hyun-ae/1-BodyBlue.dlc2.png", (0,0), "Hyun-ae/1-Neutral-SideBlue.dlc2.png", (0,0), "Hyun-ae/1-GlassesBlue.dlc2.png")
    #image hyunae full = img_comp("Hyun-ae", (1000,700), (150, 60, 60, 50), )
    #image mute full = "mutefull.dlc2.png"

    #image xharem neutral mini = "mini/hyunae-neutral.png"
    #image xharem approves mini = "mini/hyunae-neutral.png"
    #image newmute neutral mini = "mini/mute-neutral.png"

    image xharem mini Blue = "mini/xharem-Blue.dlc2.png"
    image hyunae mini Blue = "mini/hyunae-Blue.dlc2.png"
    image mute mini Blue = "mini/mute-Blue.dlc2.png"
    image newmute mini Blue = "mini/mute-Blue.dlc2.png"
    image xharem mini Red = "mini/xharem-Red.dlc2.png"
    image hyunae mini Red = "mini/hyunae-Red.dlc2.png"
    image mute mini Red = "mini/mute-Red.dlc2.png"
    image newmute mini Red = "mini/mute-Red.dlc2.png"
    image xharem mini Gold = "mini/xharem-Gold.dlc2.png"
    image hyunae mini Gold = "mini/hyunae-Gold.dlc2.png"
    image mute mini Gold = "mini/mute-Gold.dlc2.png"
    image newmute mini Gold = "mini/mute-Gold.dlc2.png"
    image xharem mini Pink = "mini/xharem-Pink.dlc2.png"
    image hyunae mini Pink = "mini/hyunae-Pink.dlc2.png"
    image mute mini Pink = "mini/mute-Pink.dlc2.png"
    image newmute mini Pink = "mini/mute-Pink.dlc2.png"

    # transforms (in particular, changes to alpha) are NOT the same
    # between displayables created with im.Composite and LiveComposite
    python:
        images_registered = { }

        def hateplus_hyunae_comp(view, *images):
            return hateplus_img_comp("Hyun-ae2", (1000,700), (430,160,180,160), view, *images)
        
        def hateplus_mute_comp(view, *images):
            return hateplus_img_comp("Mute2/Mute", (1000, 700), (460, 175, 620-460, 430-175), view, *images)

        def hateplus_newmute_comp(view, *images):
            return hateplus_img_comp("Mute2/NewMute", (1000, 700), (460, 175, 640-460, 430-175), view, *images)

        
        def hateplus_img_comp(name, size, expression_offsets, view, *images, **kwargs):
            new_images = [ size ]
            images = list(images)
            images.insert(0, "body")

            for image in images:
                for colour in POSSIBLE_COLOURS[name]:
                    if images.index(image) == 1:
                        new_images.append((expression_offsets[0], expression_offsets[1]))
                    else:
                        new_images.append((0,0))

                    n = name + "/" + str(view) + "-" + image + colour + ".dlc2.png"
                    i = None

                    if name == "Hyun-ae2" and ("body" in n or "Arm" in n):
                        cosplay_n = { }
                        for key in outfits.keys() + [ "Z" ]:
                            cosplay_n[key] =  n.split(colour)[0] + key.replace(".dlc1", "") + colour + ".dlc2.png"

                        if n not in images_registered:
                            images_registered[n] = Image(n)

                        conditions = [ ]
                        for key, value in cosplay_n.items():
                            if value not in images_registered:
                                images_registered[value] = Image(value)

                            conditions.append("store.outfit == '" + key + "'")
                            conditions.append(images_registered[value])
                        conditions += [ "True", images_registered[n] ]

                        i = ConditionSwitch(*conditions)
                    elif image == "glasses":
                        if n not in images_registered:
                            images_registered[n] = Image(n)
                            
                        i = ConditionSwitch("store.outfit not in noglasses", images_registered[n], "True", Null())
                    elif n not in images_registered:
                        if images.index(image) == 1:
                            i = images_registered[n] = im.Crop(n, expression_offsets)
                        else:
                            i = images_registered[n] = Image(n)
                    else:
                        i = images_registered[n]
                    
                    new_images.append(ConditionSwitch("COLOURS[char_style(False)] == '" + colour + "'", i, "True", Null()))
                
            comp = LiveComposite(*new_images)
            return comp



        cosplay_n = { }
        for key in outfits.keys() + [ "Z" ]:
            cosplay_n[key] =  "hyunae-fade" + key.replace(".dlc1", "") + ".dlc2.png"

        images_registered["hyunae-fade.dlc2.png"] = Image("hyunae-fade.dlc2.png")

        conditions = [ ]
        for key, value in cosplay_n.items():
            if value not in images_registered:
                images_registered[value] = Image(value)

            conditions.append("store.outfit == '" + key + "'")
            conditions.append(images_registered[value])
        conditions += [ "True", images_registered["hyunae-fade.dlc2.png"] ]


    transform hateplus_hyunae_left:
        linear .5 xanchor 0.5 xpos 300 ypos -30# zoom .5

    transform hateplus_hyunae_fast_left:
        xanchor 0.5 xpos 300 ypos -30# zoom .5# crop (0,0,500,640)

    transform hateplus_hyunae_farther_left:
        linear .5 xanchor 0.5 xpos 250 ypos -30# zoom .5

    transform hateplus_initialize:
        crop (0,0,1000,0) alpha .15
        easein 1.5 crop (0,0,1000,700) alpha 1.0

    transform hateplus_fail_initialize:
        crop (0,0,1000,0) alpha 0
        linear .4 crop (0,0,1000,300) alpha .1
        linear .4 crop (0,0,1000,500) alpha 0
        linear .4 crop (0,0,1000,700) alpha .03
        linear .3 alpha 0

    transform hateplus_fade_initialize:
        crop (0,0,1000,0) alpha 1.0
        easein 1.6 crop (0,0,1000,700) alpha 0

    transform hateplus_fail_fade_initialize:
        crop (0,0,1000,0) alpha 1.0
        linear 1.0 crop (0,0,1000,700) alpha .8
        linear .5 alpha 0

    transform hateplus_deinitialize:
        crop (0,0,1000,700) alpha 1.0
        easein 1.5 crop (0,0,1000,0) alpha .15

    transform hateplus_fade_deinitialize:
        crop (0,0,1000,700) alpha 0
        easein 1.6 crop (0,0,1000,0) alpha 1.0

    transform hateplus_initialize_slow:
        crop (0,0,1000,0) alpha .15
        pause .5
        easein 1.5 crop (0,0,1000,700) alpha 1.0

    transform hateplus_fade_initialize_slow:
        crop (0,0,1000,0) alpha 1.0
        pause .5
        easein 1.6 crop (0,0,1000,700) alpha 0

    transform hateplus_deinitialize_slow:
        pause .5
        crop (0,0,1000,700) alpha 1.0
        easein 1.5 crop (0,0,1000,0) alpha .15

    transform hateplus_fade_deinitialize_slow:
        pause .5
        crop (0,0,1000,700) alpha 1.0
        easein 1.6 crop (0,0,1000,0) alpha 0

    transform hateplus_hyunae_fast_farther_left:
        xanchor 0.5 xpos 250 ypos -30# zoom .5

    transform hateplus_mute_left:
        linear .5 xanchor 0.5 xpos 250 ypos -60

    transform hateplus_mute_fast_left:
        xanchor 0.5 xpos 300 ypos -60

    transform hateplus_mute_farther_left:
        linear .5 xanchor 0.5 xpos 200 ypos -60

    transform hateplus_mute_fast_farther_left:
        xanchor 0.5 xpos 200 ypos -60

    transform hateplus_hyunae_harem_left:
        linear .5 xanchor 0.5 xpos 300 ypos -30

    transform hateplus_hyunae_harem_fast_left:
        xanchor 0.5 xpos 300 ypos -30

    transform hateplus_hyunae_harem_farther_left:
        linear .5 xanchor 0.5 xpos 150 ypos -30

    transform hateplus_hyunae_harem_fast_farther_left:
        xanchor 0.5 xpos 150 ypos -30

    transform hateplus_mute_harem_left:
        linear .5 xanchor 0.5 xpos 750 ypos -10

    transform hateplus_mute_harem_fast_left:
        xanchor 0.5 xpos 750 ypos -10 xzoom -1

    transform xflip:
        xzoom -1

    transform xunflip:
        xzoom 1

    transform hateplus_mute_harem_farther_left:
        linear .5 xanchor 0.5 xpos 320 ypos -10

    transform hateplus_mute_harem_fast_farther_left:
        xanchor 0.5 xpos 320 ypos -10 xzoom 1

    transform hateplus_hyunae_harem_choice_hyunae:
        linear .5 xanchor 0.5 xpos 800 ypos -30

    transform hateplus_hyunae_harem_choice_mute:
        linear .5 xanchor 0.5 xpos -100 ypos -30

    transform hateplus_mute_harem_choice_hyunae:
        xzoom -1
        linear .5 xanchor 0.5 xpos 1200 ypos -10

    transform hateplus_mute_harem_choice_mute:
        xzoom -1
        linear .5 xanchor 0.5 xpos 320 ypos -10

    $ hateplus_left = { "hyunae":hateplus_hyunae_left, "mute":hateplus_mute_left }
    $ hateplus_fast_left = { "hyunae":hateplus_hyunae_fast_left, "mute":hateplus_mute_fast_left }
    $ hateplus_farther_left = { "hyunae":hateplus_hyunae_farther_left, "mute":hateplus_mute_farther_left }
    $ hateplus_fast_farther_left = { "hyunae":hateplus_hyunae_fast_farther_left, "mute":hateplus_mute_fast_farther_left }
    $ hateplus_left["newmute"] = hateplus_left["mute"]
    $ hateplus_fast_left["newmute"] = hateplus_fast_left["mute"]
    $ hateplus_farther_left["newmute"] = hateplus_farther_left["mute"]
    $ hateplus_fast_farther_left["newmute"] = hateplus_fast_farther_left["mute"]

    python:
        SFX1 = "sfx2/fx1short.ogg"
        SFX2 = "sfx2/fx2short.ogg"
        SFX3 = "sfx2/fx3short.ogg"
        SFX4 = "sfx2/fx4short.ogg"
        SFX5 = "sfx2/fx5short.ogg"
        SFX6 = "sfx2/fx6short.ogg"
        SFX7 = "sfx2/fx7short.ogg"

        HATEPLUS_AFTER = "music2/hateAfterMasterLoop.ogg"
        HATEPLUS_CAKE = "music2/hateCakeMasterLoop.ogg"
        HATEPLUS_BICKER = "music2/hateHaremBickerMaster.ogg"
        HATEPLUS_COUNCIL = "music2/hateCouncilMasterLoop.ogg"
        HATEPLUS_DENSE = "music2/hatePeopleMasterLoop.ogg"
        HATEPLUS_TITLE = "music2/hateTitleMasterLoop.ogg"
        HATEPLUS_SPARSE = "music2/hateScienceMasterLoop.ogg"
        HATEPLUS_HWATU = "music2/hateStageMaster.ogg"
        HATEPLUS_HYUNAE_CHEER = "music2/hateHyunaeCheerfulMaster.ogg"
        HATEPLUS_HYUNAE_WISTFUL = "music2/hateHyunaeWistfulMaster.ogg"
        HATEPLUS_MUTE_BIRTH = "music2/hateMuteBirthMasterLoop.ogg"
        HATEPLUS_MUTE_DETERMINED = "music2/hateMuteDeterminedMaster.ogg"
        HATEPLUS_MUTE_RESIGNED = "music2/hateMuteResignedLoop.ogg"
        HATEPLUS_NOTE = "music2/hateNoteMasterLoop.ogg"
        HATEPLUS_OLD_MUTE = "music2/hateOldMuteMasterLoop.ogg"
        HATEPLUS_POWER = "music2/hateMuteDeathMaster.ogg"
        HATEPLUS_RITUAL = "music2/hateRitualMaster.ogg"
        HATEPLUS_CREDITS = "music2/hateCreditsMasterLoop.ogg"
        HATEPLUS_NOTERO = "music2/IsaacSchankler_Track01_M.mp3"

        config.main_menu_music = HATEPLUS_TITLE

    call block13_kr
    call blockm1_kr
    call blockm2_kr
    call blockm3_kr
    call blockm4_kr
    call blockm5_kr
    call blockm6_kr
    call block_inbox_kr

label hateplus_after_load:
    $ config.main_menu_music = HATEPLUS_TITLE

    if persistent.start_hateplus:
        stop music fadeout 2.0
    if hasattr(store, "ttl") and store.ttl > 0:
        stop music
    show screen hide_everything
    with Dissolve(0.5)
    $ renpy.pause(0.5)

    hide screen connecting
    hide screen bottom_menu

    if hasattr(store, "ttl") and store.ttl > 0:
        $ store.old_ttl = store.ttl
        $ store.ttl = 0
        if current_character == "xharem":
            hide hyunae
            hide mute
        else:
            $ renpy.hide(current_character)
        hide screen hide_everything
        jump hateplus_slow_loop

    play sound "sfx/fxbeep1.mp3"

    hide screen hide_everything
    $ renpy.restart_interaction()

    if persistent.start_hateplus:
        $ persistent.start_hateplus = False
        jump hateplus_start
    else:
        return

label init_hateplus_blocks:
    call block13
    call blockm1
    call blockm2
    call blockm3
    call blockm4
    call blockm5
    call blockm6
    call block_inbox

    return

label hateplus_main_menu:
    show screen hide_everything
    with None

    $ hateplus_check_achievements()
    $ renpy.free_memory()
    # if persistent.animated_backgrounds:
    #     scene bg white
    # else:
    #     scene bg white static

    $ renpy.show("background " + char_style().replace("-", " "))

    $ store.game_playing = False
    $ persistent.start_hateplus = False
    $ store.resolution = persistent.resolution
    hide screen skip
    show screen keymap
    $ store.blocks = [ Block("Block 1"), Block("Block 2"), Block("Block 3"), Block("Block 4"), Block("Block 5"), Block("Block 6"), Block("Block 7"), Block("Block 8"), Block("Block 9"), Block("Block 10"), Block("Helpful notes", True), Block("*Mute's questions") ]
    call init_blocks
    $ store.hateplus_blocks = [ Block("Block 13"), Block("Block M1"), Block("Block M2"), Block("Block M3"), Block("Block M4"), Block("Block M5"), Block("Block M6") ]
    $ store.inbox = Block("W{size=-6}HITE{/size} P{size=-6}RINCESS{/size} Inbox")
    call init_hateplus_blocks

    # Moved to splash_screen for early language detection
    if persistent._language != "":
        $ config.translator.translations = load_local_messages(config.translator.translations)

    show screen glow
    $ renpy.with_statement(Dissolve(0.5))
    #$ current_character = persistent.current_character
    hide screen hide_everything
    show screen hateplus_main_menu

    # python:
    #     contents = ""
    #     for i in dir(persistent):
    #         if "file" in i:
    #             contents += '"' + i + '"' + ": " + str(getattr(persistent, i)) + "\n"

    # $ a(contents.replace("[", "[[").replace("{", "{{"))

    $ renpy.pause()
    
    return

label hateplus_new:
    hide screen hide_everything
    $ use_character = None
    $ pronouns = None
    $ attitude = None
    $ favourite_year = None

    hide screen skip
    $ renpy.show("background " + char_style().replace("-", " "))
    show screen glow
    show screen hateplus_new_screen
    with dissolve

    $ renpy.pause()

    return

label hateplus_splashscreen:
    # I can't find better way for settings Korean at launch.
    # This makes game restarts for first launch.
    # - iAmGhost
    if persistent._language and persistent.language != "":
        if config.translator is None:
            $ renpy.utter_restart()

    show background black
    show loveconquersall with dissolve
    $ renpy.pause(1.0)
    play music HATEPLUS_TITLE fadein 2.0
    $ renpy.pause(1.0)
    hide loveconquersall with dissolve
    show screen hide_everything
    $ renpy.pause(0.5)

    python:
        update_save_list()

    return

label hateplus_new_start:
    $ store.current_character = use_character
    $ store.tsun = store.dere = 0
    $ store.mute_approval = 0

    if pronouns == "she":
        $ female = True
    else:
        $ female = False

    if current_character == "mute" or current_character == "xharem":
        if current_character == "mute":
            $ store.use_ending = "ending4"
        else:
            $ store.use_ending = "ending5"

        if attitude == "resentful":
            $ store.mute_approval = -2
        else:
            $ store.mute_approval = 5

        if female:
            $ store.mute_approval -= 2

    elif current_character == "hyunae":
        if attitude == "flirty":
            $ store.use_ending = "ending2"
            $ store.tsun = 0
            $ store.dere = 6
        else:
            $ store.use_ending = "ending1"

            if attitude == "resentful":
                $ store.tsun = 6
                $ store.dere = 0
            else:
                $ store.tsun = 0
                $ store.dere = 0

    $ conversations_seen = [ ]
    $ man_with = False
    $ married = False
    $ asked_about_cosplay = False
    $ seen_first_cosplay = False
    $ store.outfit = ""
    $ store.mod_values = [ ]

label hateplus_start:
    stop music fadeout 2.0
    $ config.main_menu_music = HATEPLUS_TITLE

    hide screen glow
    hide screen hateplus_new_screen
    hide screen hateplus_new_screen4
    python:
        renpy.scene()
        store.hateplus_has_started = True

        if store.use_ending == "ending1" or store.use_ending == "ending2":
            store.current_character = "hyunae"
        elif store.use_ending == "ending4":
            store.current_character = "mute"
        else:
            store.current_character = "xharem"

        store.hateplus_blocks = [ Block("Block 13"), Block("Block M1"), Block("Block M2"), Block("Block M3"), Block("Block M4"), Block("Block M5"), Block("Block M6") ]
        store.inbox = Block("W{size=-6}HITE{/size} P{size=-6}RINCESS{/size} Inbox")
    call init_hateplus_blocks

    $ store.day = 1

    python:
        store.all_block = SearchBlock(body=" ")
        store.all_block.name = "All messages"

        embedded_data = [ ]
        bad_data = [ ]
        for i in sorted(all_block.contents + store.hateplus_blocks[3].contents, cmp=sort_full_date ):
            if i not in hateplus_blocks[0].contents:# and i not in hateplus_blocks[3].contents:
                embedded_data.append(Data("TEXT DATA", "//" + i.clean_creator(), "%.1fkB" % i.bytes, i.name, "Block M" + i.id.split("-")[1], i))
        embedded_data[-1].format = "ENCRYPTED DATA"
        embedded_data[-1].action.encrypted = True

        bad_data.append(Data("BITMAP DATA", "Personal photos", "27.9MB"))
        bad_data.append(Data("BITMAP DATA", "Updated wrinkled face", "5.5MB", "textures"))
        #bad_data.append(Data("UNRECOVERABLE", "ìì² ë", "32.7kB", "í ë§ì¹šëŽ ìŽ ì°ì£Œì ??????????"))
        #bad_data.append(Data("UNRECOVERABLE", "¶©ì€í ë°°ê²œ ìë£", "70.6kB", "°ê§ì¹š°ì£²œ ?????????????"))
        bad_data.append(Data("BITMAP DATA", "UKSPS Uniform", "1.9MB"))
        bad_data.append(Data("BITMAP DATA", "Seo-yeong's smile", "889.2kB"))
        #bad_data.append(Data("NO DATA", "", ""))
        bad_data.append(Data("DICTIONARY DATA", "zh<->kr translation", "10.1MB"))
        bad_data.append(Data("VIDEO DATA", "Keepsake from Earth", "2.4MB"))
        bad_data.append(Data("BITMAP DATA", "Hair charms", "45.0kB"))
        bad_data.append(Data("NO DATA", "", ""))
        bad_data.append(Data("NO DATA", "", ""))
        bad_data.append(Data("NO DATA", "", ""))
        bad_data.append(Data("NO DATA", "", ""))
        bad_data.append(Data("NO DATA", "", ""))
        bad_data.append(Data("NO DATA", "", ""))
        bad_data.append(Data("NO DATA", "", ""))


        renpy.random.shuffle(bad_data)
        bad_indices = [ 5,11,18,20,25,29,32,32,40,43,49,53+9,53+9,56+9 ]
        #embedded_data += bad_data
        for i in range(len(bad_data)):
            embedded_data.insert(bad_indices[i], bad_data[i])

        store.interesting_block = Block("Interesting messages")

        save_name = current_character + " " + save_expression() + "," + "Hate Plus—Day 1"
        
    # $ renpy.show("background " + char_style().replace("-", " "))
    # if current_character == "xharem":
    #    show hyunae full at hateplus_hyunae_harem_fast_left
    #    show mute full at hateplus_mute_harem_fast_left
    # else:
    #    $ renpy.show(current_character + " full", [ hateplus_fast_left[current_character] ])

    $ logs_until_conversation = [ 6, 11, 15, 21, 27, 34, 40 ]
    python:
        if current_character != "hyunae":
            for i in range(len(logs_until_conversation)):
                logs_until_conversation[i] += 9

    $ store.inbox.contents[0].enabled = True

    $ _block = None
    if current_character == "hyunae":
        $ hateplus_greeting = "hateplus_hyunae_start"
        $ hateplus_conversation = "Um, hey, could you click on me, please?","hateplus_hyunae_testing","hyunae talk"
        $ ai_enabled = True
    else:
        if current_character == "mute":
            $ hateplus_greeting = "hateplus_mute_start"
        elif current_character == "xharem":
            $ hateplus_greeting = "hateplus_xharem_start"

        $ hateplus_conversation = "","",""
        $ ai_enabled = False

        python:
            for i in store.hateplus_blocks[0].contents:
                i.enabled = True

    $ store.override_conversation = ""
    $ search_by = "title"
    $ search_string = ""
    $ to_extract = [ None, None, None, None, None, None ]
    $ scroll_point = 0
    $ store.power = 12
    $ store.ttl = store.old_ttl = 0
    $ store.panned_in = False
    $ store.seen_characters = { }
    $ outfits = outfits.copy()
    $ _message = last_message = None
    $ store.use_fast = ""

    if not hasattr(store, "pronouns"):
        if female:
            $ pronouns = "she"
        else:
            $ pronouns = "he"

    $ title = "Miss "
    $ they = pronouns

    $ them = "them"
    $ their = "their"
    if pronouns == "she":
        $ them = "her"
        $ their = "her"
    elif pronouns == "he":
        $ them = "him"
        $ their = "his"

    if pronouns == "he":
        $ title = "Mr "
    elif pronouns == "they":
        $ title = ""
    elif hasattr(store, "married") and married:
        $ title = "Ms "

    $ store.newmute_approval = 0
    $ hateplus_body_possible = None
    $ hateplus_no_touch = None
    $ hateplus_kissing = False
    $ hateplus_hair_touching = False
    $ hateplus_body = False
    $ hateplus_player_sex = False
    $ store.hateplus_use_ending = None
    $ hateplus_seen_first_cosplay = False
    $ hateplus_knows_seollal = False
    $ hateplus_power_down_enabled = False
    $ hateplus_mute_relationship = ""
    $ hateplus_newmute_because_lesbians = False
    $ hateplus_newmute_because_men = False
    $ hateplus_mute_motivation = ""
    $ hateplus_newmute_chance = None
    $ hateplus_mute_old_mute_bitch = ""

    show screen hateplus_main_screen
    show screen hateplus_main_screen_ai
    show screen hateplus_main_screen_outfits
    show screen hateplus_logs
    show screen hateplus_block(block=all_block)
    show screen hateplus_new_extract
    #show screen hateplus_message
    show screen hateplus_extracting
    show screen hateplus_extraction_bg

    show screen glow
    show screen hateplus_bottom_menu
    $ renpy.show("background " + char_style().replace("-", " "))

    $ hide_every_screen()

    hide screen hide_everything
    with dissolve

    jump hateplus_restart

label hateplus_restart:
    #$ try_ping()
    
    # if renpy.music.get_playing() == TERMINAL:
    #     if hateplus_greeting:
    #         stop music fadeout 2.0
    #     elif current_character == "hyunae":
    #         #if store.radiation and store.radiation_levels > 0.1:
    #         #    play music HYUNAE_GLITCHY fadeout 1.0 loop
    #         #elif conversation["hyunae"] == "ask_it":
    #         #    play music HYUNAE_DRAMATIC fadeout 1.0 loop
    #         #elif conversation["hyunae"] == "good_finale":
    #         #    stop music fadeout 2.0
    #         #else:
    #         play music HYUNAE fadeout 1.0 loop
    #     else:
    #         #if store.radiation and store.radiation_levels > 0.1:
    #         #    play music MUTE_GLITCHY fadeout 1.0 loop
    #         #else:
    #         play music MUTE fadeout 1.0 loop
    # if renpy.music.get_playing() == REACTOR_TERMINAL:
    #     play music REACTOR fadeout 2.0 loop
    
    show screen block_everything
    #$ renpy.pause(1.0)
#    $ renpy.show("background " + char_style().replace("-", " "))
#    $ renpy.with_statement(dissolve, True)
    # if current_character == "xharem":
    #     show hyunae full at hateplus_hyunae_harem_fast_left
    #     show mute full at hateplus_mute_harem_fast_left
    # else:
    #    $ renpy.show(current_character + " full", [ hateplus_fast_farther_left[current_character] ])
    #$ renpy.show(current_character + " neutral", [ fast_left[current_character] ] )
    #$ renpy.with_statement(dissolve, True)
    #$ renpy.pause(1.0)

    $ save_name = current_character + " " + save_expression() + "," + "Hate Plus—Day " + str(store.day)
    $ renpy.block_rollback()

    jump hateplus_slow_loop
    
label hateplus_override_conversation:
    $ hateplus_greeting = store.override_conversation
#    $ side_conversation[current_character] = store.override_conversation

label hateplus_jump_to_dialogue:
    show screen hateplus_bottom_menu
    hide screen hateplus_messages
    hide screen hateplus_block
    hide screen hateplus_logs
    hide screen hateplus_main_screen
    hide screen hyunaeglow
    hide screen muteglow
    hide screen newmuteglow
    hide screen hateplus_dialogue_button

    show screen rollback_keymap
    with dissolve
    $ renpy.block_rollback()
    show screen block_everything(timeout=0.5)
    $ renpy.pause(0.5)
    #show background at zoomed_out_bg
    if current_character == "xharem":
        show hyunae at hateplus_hyunae_harem_left
        show mute at hateplus_mute_harem_left
        $ renpy.pause(.5)
        show mute at xflip with Dissolve(.5)
    else:
        if renpy.showing(current_character):
            $ renpy.show(current_character, [ hateplus_left[current_character] ] )
        else:
            $ renpy.show(current_character + " neutral", [ hateplus_left[current_character] ] )
    #$ show_character()
    
    show screen block_everything
    $ renpy.pause(1.0)
    
    #if hateplus_side_conversation:
    #    $ use_conversation = hateplus_side_conversation
    #    $ hateplus_side_conversation = ""
    #    $ conversations_seen.append(use_conversation)
    #    
    #    $ renpy.block_rollback()
    #    $ renpy.jump(use_conversation)

    $ last_message = _message
    $ _message = None

    if hateplus_greeting:
        $ use_greeting = hateplus_greeting
        $ hateplus_greeting = ""
        $ conversations_seen.append(use_greeting)
        if current_character == "xharem":
            show hyunae at hateplus_hyunae_harem_left
            show mute at hateplus_mute_harem_left
            $ renpy.pause(.5)
            show mute at xflip with Dissolve(.5)
        else:
            $ renpy.show(current_character, [ hateplus_left[current_character] ])
        $ renpy.pause(1.0)
        #$ show_character()
        $ renpy.jump(use_greeting)
            
    if not hateplus_conversation[1] in conversations_seen:
        $ conversations_seen.append(hateplus_conversation[1])
    elif not repeated_myself:
        $ should_call_repeated_myself = True
        
    $ use_conversation = hateplus_conversation[1]
    $ hateplus_conversation = "","",""

    $ renpy.block_rollback()
    $ renpy.jump(use_conversation)
    
label hateplus_present:
    show background at zoomed_out_bg
    $ renpy.show(current_character, [ left[current_character] ] )
    hide screen messages
    #$ show_character()
    
    $ last_message = _message
    $ new_messages = False
    $ _block = None
    show screen block_everything
    $ renpy.pause(1.0)
    $ renpy.block_rollback()
    
    $ renpy.jump(conversation[current_character])

label hateplus_harem_slow_loop:
    show hyunae full at hateplus_hyunae_harem_farther_left
    show mute full at hateplus_mute_harem_farther_left
    $ renpy.pause(0.5)
    show mute at xunflip

# The game starts here.
label hateplus_slow_loop:
    $ config.allow_skipping = False
    if config.debug_force_newmute:
        $ current_character = "newmute"

    if current_character == "mute" and store.day == 3:
        hide mute
        hide mutefade
        $ ai_enabled = False
        $ store.inbox.contents[6].enabled = True
        $ current_character = "newmute"
        $ hateplus_greeting = "hateplus_newmute_start"
        python:
            for i in all_block.contents:
                i.scroll_point = 0

        play music HATEPLUS_MUTE_BIRTH fadein 5.0 fadeout 5.0 loop if_changed

    elif current_character == "newmute":
        if ai_enabled and "hateplus_newmute_read_note" not in conversations_seen and "hateplus_newmute_start" in conversations_seen and store.inbox.contents[6].read:
            $ hateplus_greeting = "hateplus_newmute_read_note"

    $ store.all_block = SearchBlock(body=" ")
    $ store.all_block.name = "All messages"

    hide screen rollback_keymap

    hide screen black
    hide screen hide_everything
    $ renpy.with_statement(Dissolve(0.5))

    if last_message and last_message.enabled and not _message:
        $ _message = last_message
        #$ last_message = None
    $ store.game_playing = True
    $ config.skipping = False
    $ save_name = current_character + " " + save_expression() + "," + "Hate Plus—Day " + str(store.day)

    $ renpy.block_rollback()

    show screen block_everything
    $ config.allow_skipping = True
    #$ renpy.pause(1.0)

    if _message and not store.override_conversation:
        jump hateplus_pan_to_message
    
label hateplus_loop:
    if radiation:
        show screen radiation
    $ store.bg_scroll = True
    $ _message = None
    $ last_message = None
    $ new_messages = False

    $ persistent.last_character = char_style()

    $ renpy.block_rollback()
    $ config.skipping = False
    if ai_enabled:
        if current_character == "xharem":
            if renpy.showing("hyunae"):
                show hyunae full at hateplus_hyunae_harem_farther_left
                show mute full at hateplus_mute_harem_farther_left
            else:
                show hyunae full at hateplus_hyunae_harem_fast_farther_left, hateplus_initialize, xunflip
                show hyunaefade at hateplus_hyunae_harem_fast_farther_left, hateplus_fade_initialize, xunflip
                show mute full at hateplus_mute_harem_fast_farther_left, hateplus_initialize_slow, xunflip
                show mutefade at hateplus_mute_harem_fast_farther_left, hateplus_fade_initialize_slow, xunflip
                show screen block_everything(timeout=2.5)
                $ renpy.pause(2.5)
        else:
            if renpy.showing(current_character):
                $ renpy.show(current_character + " full", [ hateplus_farther_left[current_character] ])
            else:
                $ renpy.show(current_character + " full", [ hateplus_fast_farther_left[current_character], hateplus_initialize ])
                $ renpy.show(current_character + "fade", [ hateplus_fast_farther_left[current_character], hateplus_fade_initialize ])
                show screen block_everything(timeout=1.5)
                $ renpy.pause(1.5)

        if hateplus_greeting:
            jump hateplus_jump_to_dialogue

    $ store.bg_scroll = False
    $ renpy.free_memory()

    $ hateplus_change_track()
    #show screen hateplus_bottom_menu
    show screen hateplus_main_screen

    if ai_enabled:
        show screen hateplus_main_screen_ai
        $ ui.timer(1.5, ui.jumps("hateplus_loop_greet"))
    else:
        show screen hateplus_main_screen_disabled(timing=2)

    $ store.bg_scroll = True
    $ renpy.pause()

label hateplus_loop_greet:
    hide screen hateplus_dialogue_button

    $ hateplus_try_ping()
    #$ renpy.pause(0.5)
    $ renpy.with_statement(None)

    if ai_enabled:
        if hateplus_conversation[0] and hateplus_conversation[1] not in store.conversations_seen:
            if current_character == "xharem":
                show hyunae neutral
                show mute neutral
                $ renpy.pause(0.1)
                $ renpy.show(hateplus_conversation[2])
                $ renpy.with_statement(fast)
                if "hyunae" in hateplus_conversation[2]:
                    $ h_side(hateplus_conversation[0], interact=False)
                    show screen hateplus_dialogue_button(use_character="hyunae", position=hateplus_hyunae_harem_fast_farther_left)
                else:
                    $ m_side(hateplus_conversation[0], interact=False)
                    show screen hateplus_dialogue_button(use_character="mute", position=hateplus_mute_harem_fast_farther_left)

            else:
                $ renpy.show(hateplus_conversation[2])
                $ renpy.with_statement(fast)

                if current_character == "hyunae":
                    $ h_side(hateplus_conversation[0], interact=False)
                elif current_character == "mute":
                    $ m_side(hateplus_conversation[0], interact=False)
                elif current_character == "newmute":
                    $ n_side(hateplus_conversation[0], interact=False)

                show screen hateplus_dialogue_button
        else:
            if current_character == "xharem":
                show hyunae full with fast
                show mute full with fast
            else:
                $ renpy.show(current_character + " full")
                $ renpy.with_statement(fast)
            
    $ renpy.pause()
    
    jump hateplus_loop

label hateplus_pan_to_inbox:
    hide screen hateplus_main_screen_disabled
    hide screen hateplus_main_screen_outfits
    $ _block = store.inbox

label hateplus_pan_to_messages:
    $ renpy.block_rollback()
    #if store.ai_enabled:
    #    show screen hateplus_dialogue_button

    if _message:
        if _message.scroll_point == 1000:
            $ _message.scroll_point = 1001

        if not _message.encrypted:
            $ _message.read = True
    $ _message = last_message = None

    if not _block:
        jump hateplus_pan_to_logs

    if not ai_enabled and read("13-*") and (hateplus_greeting == "hateplus_mute_start" or hateplus_greeting == "hateplus_xharem_start"):
        $ renpy.pause(.5)
        jump hateplus_loop_greet
    
    show screen hateplus_block(block=_block)
    if store.game_playing:
        #$ change_track(_block)
        show screen hateplus_bottom_menu
    
    $ renpy.pause(1.5)

    jump hateplus_loop_greet
    
    jump hateplus_pan_to_messages
       
label hateplus_pan_to_message:
    if store.game_playing:
        $ hateplus_change_track(_message.id)
    $ store.scroll_point = 0
    hide screen hateplus_dialogue_button
label hateplus_return_to_message:
    if _message.scroll_point < 1000:
        $ _message.scroll_point -= 1
        $ store.scroll_timer = time.time()
        $ store.side_update = True
    $ renpy.block_rollback()

    show screen hateplus_message(message=_message)
    if store.game_playing:
        show screen hateplus_bottom_menu

    $ renpy.block_rollback()
    
    $ renpy.pause()
    
    jump hateplus_pan_to_message
    
label hateplus_pan_to_logs:
    while True:
        $ _message = None
        $ _block = None
        $ search_string = ""

        if game_playing:
            show screen hateplus_bottom_menu
        call screen hateplus_logs
        
        hide screen side_menu
        hide screen hateplus_logs

        python:
            if _return:
                _block = None

                # Korean input system returns input result in tuple - iAmGhost
                if persistent._language == "korean":
                    if isinstance(_return, tuple):
                        keyword, final = _return
                        _block = SearchBlock(**{ search_by:keyword })
                else:
                    _block = SearchBlock(**{ search_by:_return })

                _return = None

                if len(_block.contents) == 1 and _block.contents[0].enabled:
                    _message = _block.contents[0]
                    _block = None
                    renpy.jump("hateplus_pan_to_message")
                elif _block.contents:
                    renpy.jump("hateplus_pan_to_messages")

        if _message:
            jump hateplus_pan_to_message

label hateplus_pan_to_extraction:
    show screen block_everything
    hide screen hateplus_main_screen
    with dissolve
    
    $ store.bg_scroll = False
    $ renpy.pause(1.7)
    $ renpy.free_memory()
    # $ renpy.renpy.loadsave.cycle_saves("hateplus-auto-", 8)  # 8 save slots.
    # $ renpy.save("hateplus-auto-1", save_name)

    show screen hateplus_extraction_bg
    show screen hateplus_new_extract
    hide screen glow
    with dissolve

    $ renpy.pause()

    # while True:
    #     $ _message = None
    #     $ _block = None
    #     $ search_string = ""

    #     show screen hateplus_new_extract

    #     # python:
    #     #     if _return:
    #     #         _block = SearchBlock(**{ search_by:_return })
    #     #         _return = None

    #     #         if _block.contents:
    #     #             renpy.jump("hateplus_pan_to_messages")

label hateplus_extract:
    hide screen hateplus_new_extract

    # $ renpy.pause(0.5)

    # if current_character == "hyunae":
    #     hh "Very well, I'll go extract the logs you picked..."
    # elif current_character == "mute":
    #     mm "Okay, let's extract these ones for you."

    # $ renpy.pause(0.5)

    # if current_character == "xharem":
    #     hide hyunae
    #     hide mute
    # else:
    #     $ renpy.hide(current_character)
    # $ renpy.with_statement(dissolve, True)

    python:
        _block = Block("Recently extracted")

        for message in store.to_extract:
            if message:
                message.enabled = True
                _block.contents.append(message)

        for message in store.to_extract:
            if message:
                index = store.to_extract.index(message)
                progress = range(11*3)
                renpy.random.shuffle(progress)
                for i in range(11*3):
                    renpy.show_screen("hateplus_extracting", i=message, index=index, progress=progress[:i+1], end=len(_block.contents))
                    if i == 0:
                        renpy.with_statement(Dissolve(0.5))
                    elif i == 11:
                        store.power -= .5
                    elif i == 30:
                        store.power -= .5

                    #if i % 4 == 0:
                    #    renpy.music.play(random.choice([ SFX1, SFX2, SFX3, SFX4, SFX5, SFX6 ]), "sound")
                    renpy.pause(0.0001)
                renpy.pause(0.5)

    show screen glow
    hide screen hateplus_extracting
    hide screen hateplus_extraction_bg
    with dissolve
    $ store.to_extract = [ None, None, None, None, None, None ]

    stop music fadeout 5.0
    $ renpy.pause(2.0)
    play sound "sfx/fxbeep1.mp3"

    if current_character == "xharem":
        show hyunae full at hateplus_hyunae_harem_fast_farther_left, hateplus_initialize_slow
        show hyunaefade at hateplus_hyunae_harem_fast_farther_left, hateplus_fade_initialize_slow
        show mute full at hateplus_mute_harem_fast_farther_left, hateplus_initialize
        show mutefade at hateplus_mute_harem_fast_farther_left, hateplus_fade_initialize
    else:
        #$ renpy.show(current_character + " full", [ hateplus_fast_farther_left[current_character] ])
        $ renpy.show(current_character + " full", [ hateplus_fast_farther_left[current_character], hateplus_initialize ])
        $ renpy.show(current_character + "fade", [ hateplus_fast_farther_left[current_character], hateplus_fade_initialize ])

    $ ai_enabled = True
    $ store.bg_scroll = True

    #$ renpy.with_statement(dissolve, True)

    $ renpy.pause(1.5)

    jump hateplus_pan_to_messages

label hateplus_pan_to_conversation:
    python:
        hateplus_flag_read(_message)

        renpy.pause(.5)
        renpy.show(current_character + " full", [ hateplus_left[current_character] ])
        renpy.pause(1.5)

        renpy.jump("log_" + get_hateplus_id(_message).replace("-", "_") + "_" + current_character + "_shown")

label year_of_hate:
    
    show hyunae serious blush with fast
    hh "So..."

    if store.interesting_block.contents:
        
        show hyunae calm with fast
        $ hh("Let's celebrate a year of hate together~!", interact=False)
        show screen hateplus_dialogue_block(block=store.interesting_block)
        $ renpy.pause()
    else:
        
        show hyunae cautious
        hh "I guess we should look at more logs together, then...?"
    
    show hyunae smile with fast
    
    jump end_shown
    
label log_loop:
    python:
        while True:
            renpy.pause()
    jump hateplus_slow_loop

label end_shown:
    if current_character == "xharem":
        show hyunae at hateplus_hyunae_harem_farther_left
        show mute at hateplus_mute_harem_farther_left
        $ renpy.pause(0.5)
        show mute at xunflip with Dissolve(0.5)
    else:
        $ renpy.show(current_character, [ hateplus_farther_left[current_character] ])
    $ renpy.pause(1.0)

    if _message:
        $ _message.scroll_point = 1001
        jump hateplus_return_to_message
    else:
        jump hateplus_slow_loop

label hateplus_change_outfit:
    hide screen hateplus_main_screen_outfits
    with dissolve

    if store.outfit != _return:
        $ renpy.show("hyunae", [ If(current_character == "xharem", hateplus_hyunae_harem_fast_farther_left, hateplus_hyunae_fast_farther_left), hateplus_deinitialize ])
        $ renpy.show("hyunaefade", [ If(current_character == "xharem", hateplus_hyunae_harem_fast_farther_left, hateplus_hyunae_fast_farther_left), hateplus_fade_deinitialize ])
        $ renpy.pause(1.5)
        if _return != None:
            $ store.outfit = _return
        #$ renpy.restart_interaction()
        $ renpy.show("hyunae", [ If(current_character == "xharem", hateplus_hyunae_harem_fast_farther_left, hateplus_hyunae_fast_farther_left), hateplus_initialize ])
        $ renpy.show("hyunaefade", [ If(current_character == "xharem", hateplus_hyunae_harem_fast_farther_left, hateplus_hyunae_fast_farther_left), hateplus_fade_initialize ])
        $ renpy.pause(1.5)

    hide screen hateplus_main_screen
    show screen hateplus_main_screen(fast=True)
    show screen hateplus_main_screen_ai(timing=1)

    jump hateplus_loop_greet

label hateplus_extract_go_back:
    hide screenhateplus_new_extract
    show screen glow 
    hide screen hateplus_extraction_bg
    show screen hateplus_main_screen(fast=True)
    with dissolve
    show screen hateplus_main_screen_disabled
    $ store.bg_scroll = True

    $ renpy.pause()

    jump hateplus_loop

label hateplus_disable_ai:
    play music HATEPLUS_NOTE fadeout 5.0 fadein 5.0 loop if_changed

    if store.day == 2 and store.power < 7 and not embedded_data[-1].action.enabled and embedded_data[-1].action not in store.to_extract:
        if current_character == "hyunae":
            $ hateplus_greeting = "hateplus_hyunae_notices_death_of_mute"
        elif current_character == "mute":
            $ hateplus_greeting = "hateplus_mute_notices_death_of_mute"
        elif current_character == "xharem":
            $ hateplus_greeting = "hateplus_xharem_notices_death_of_mute"
        jump hateplus_slow_loop

    $ ai_enabled = False

    hide screen rollback_keymap
    hide screen hateplus_main_screen_ai
    with dissolve

    if current_character == "xharem":
        show hyunae full at hateplus_deinitialize_slow
        show hyunaefade at hateplus_hyunae_harem_fast_farther_left, hateplus_fade_deinitialize_slow
        show mute full at hateplus_deinitialize
        show mutefade at hateplus_mute_harem_fast_farther_left, hateplus_fade_deinitialize
        # FADE
    else:
        $ renpy.show(current_character + " full", [ hateplus_deinitialize ])
        $ renpy.show(current_character + "fade", [ hateplus_fast_farther_left[current_character], hateplus_fade_deinitialize ])
    #$ renpy.pause(1.5)

label hateplus_disable_ai_screens:
    hide screen hateplus_main_screen
    show screen hateplus_main_screen(fast=True)
    show screen hateplus_main_screen_disabled
    hide screen hateplus_dialogue_button

    $ renpy.pause()

    jump hateplus_slow_loop


label hateplus_reenable_ai:
    if store.day == 3:
        $ renpy.music.play(HATEPLUS_MUTE_DETERMINED, loop=True, fadeout=5.0, fadein=5.0)
    else:
        $ renpy.music.play(HATEPLUS_HYUNAE_WISTFUL, loop=True, fadeout=5.0, fadein=5.0)

    $ ai_enabled = True

    hide screen hateplus_main_screen_disabled
    with dissolve

    if current_character == "xharem":
        show hyunae full at hateplus_initialize_slow
        show hyunaefade at hateplus_hyunae_harem_fast_farther_left, hateplus_fade_initialize_slow
        show mute full at hateplus_initialize
        show mutefade at hateplus_mute_harem_fast_farther_left, hateplus_fade_initialize
    else:
        $ renpy.show(current_character + " full", [ hateplus_fast_farther_left[current_character], hateplus_initialize ])
        $ renpy.show(current_character + "fade", [ hateplus_fast_farther_left[current_character], hateplus_fade_initialize ])

    hide screen hateplus_main_screen
    show screen hateplus_main_screen(fast=True)
    show screen hateplus_main_screen_ai(timing=1)

    $ renpy.pause(1.5)

    jump hateplus_loop_greet

label hateplus_reenable_ai_broken:
    hide screen hateplus_main_screen_disabled
    with dissolve

    $ renpy.show("mute pressure", [ hateplus_fast_farther_left[current_character], hateplus_fail_initialize ])
    $ renpy.show("mutefade", [ hateplus_fast_farther_left[current_character], hateplus_fail_fade_initialize ])

    $ renpy.pause(1.5)

    jump hateplus_disable_ai_screens

label hateplus_diagnostic:
    hide screen hateplus_main_screen
    hide screen hateplus_main_screen_disabled
    with dissolve

    $ renpy.pause(0.2)

    show screen hateplus_diagnostic

    if current_character != "newmute" or "hateplus_newmute_read_note" in conversations_seen:
        $ renpy.pause(5.0)

        show screen hateplus_main_screen
        $ renpy.pause(1.0)
        jump hateplus_disable_ai_screens
    else:
        $ ai_enabled = True
        $ renpy.pause(5.0)

        $ renpy.show(current_character + " full", [ hateplus_fast_farther_left[current_character], hateplus_initialize ])
        $ renpy.show(current_character + "fade", [ hateplus_fast_farther_left[current_character], hateplus_fade_initialize ])

        $ renpy.pause(1.5)

        jump hateplus_jump_to_dialogue


label hateplus_shutdown:
    if current_character == "xharem":
            show hyunae at hateplus_hyunae_harem_left
            show mute at hateplus_mute_harem_left
            $ renpy.pause(.5)
            show mute at xflip with Dissolve(.5)
    else:
        $ renpy.show(current_character, [ hateplus_left[current_character] ])
    $ renpy.pause(1.0)


    if current_character == "hyunae":
        if store.day == 2:
            show hyunae sorry with fast
            menu:
                hh "Are you sure you want to shut down for today?"

                "Yes@hyunae hate":
                    pass

                "No@hyunae disappoint":
                    
                    show hyunae shame
                    hh "Very well, take your time! Just let me know when you're ready!"
                    
                    show hyunae tired
                    
                    jump hateplus_slow_loop

                "No@hyunae disappoint":
                    
                    show hyunae shame
                    hh "Very well, take your time! Just let me know when you're ready!"
                    
                    show hyunae tired
                    
                    jump hateplus_slow_loop
        else:
            show hyunae neutral2 with fast
            menu:
                hh "Are you sure you want to shut down for today?"

                "Yes@hyunae smile":
                    pass

                "No@hyunae look":
                    
                    show hyunae cautious
                    hh "Very well, take your time! Just let me know when you're ready!"
                    
                    show hyunae hmm
                    
                    jump hateplus_slow_loop

                "No@hyunae look":
                    
                    show hyunae cautious
                    hh "Very well, take your time! Just let me know when you're ready!"
                    
                    show hyunae hmm
                    
                    jump hateplus_slow_loop

        if store.day == 1:
            $ hateplus_greeting = "hateplus_hyunae_seollal_morning"
            $ store.power = 21
        elif store.day == 2:
            $ hateplus_greeting = "hateplus_hyunae_cake"
            $ store.power = 21

    elif current_character == "mute":
        show mute doubt blush with fast
        menu:
            mm "We're done for the day, right?"

            "Yes@mute pout":
                pass

            "No@mute suspicious":
                show mute sigh
                mm "Well, alright... just let me know when you're ready."
                
                show mute tired

                jump hateplus_slow_loop

            "No@mute suspicious":
                show mute sigh
                mm "Well, alright... just let me know when you're ready."
                
                show mute tired
                
                jump hateplus_slow_loop

        if store.day == 1:
            $ hateplus_greeting = "hateplus_mute_morning"
            $ store.power = 21
        if store.day == 2:
            $ store.power = 12
            
            show mute worry2 with fast
            mm "Thanks... I just need some time alone, to think things over, okay?"
    
    elif current_character == "xharem":
        
        if store.day == 2:
            show hyunae sorry with fast
            show mute tired blush with fast
            hh2 "So..."
            
            show hyunae tired2
            menu:
                hh2_menu "Are you sure you want to shut down for today?"
                
                "Yes@hyunae disappoint":
                    pass
                
                "No@hyunae scrutiny":
                    
                    show hyunae question blush
                    show mute think
                    hh2 "Very well, take your time! Just let us know when you're ready!"
                    
                    show hyunae tired
                    show mute neutral3
                    jump hateplus_slow_loop
                
                "No@hyunae scrutiny":
                    
                    show hyunae question blush
                    show mute think
                    hh2 "Very well, take your time! Just let us know when you're ready!"
                    
                    show hyunae tired
                    show mute neutral3
                    jump hateplus_slow_loop
        
        else:
            show hyunae neutral2 with fast
            show mute neutral with fast
            hh2 "So..."
            
            show hyunae enthusiastic
            menu:
                hh2_menu "Are you sure you want to shut down for today?"
                
                "Yes@hyunae smile":
                    pass
                
                "No@hyunae look":
                    
                    show hyunae cautious
                    show mute think
                    hh2 "Very well, take your time! Just let us know when you're ready!"
                    
                    show hyunae cautious
                    show mute neutral3
                    jump hateplus_slow_loop
                
                "No@hyunae look":
                    
                    show hyunae cautious
                    show mute think
                    hh2 "Very well, take your time! Just let us know when you're ready!"
                    
                    show hyunae cautious
                    show mute neutral3
                    jump hateplus_slow_loop

        if store.day == 1:
            $ hateplus_greeting = "hateplus_xharem_seollal"
            $ store.power = 21
        elif store.day == 2:
            $ hateplus_greeting = "hateplus_xharem_despondence_of_mute"
            $ store.power = 21

    $ persistent.hateplus_day = max(persistent.hateplus_day, store.day)

    $ hateplus_power_down_enabled = False
    $ store.day += 1

    $ store.ttl = time.time()+60*60*12
    $ save_name = current_character + " " + save_expression() + "," + "Hate Plus—Day " + str(store.day) + "@" + str(store.ttl)

    if current_character == "hyunae":
        if store.day == 4:
            
            show hyunae cautious with fast
            hh "I guess that's all, then!"

            if store.hateplus_use_ending == "hyunae_alone":
                
                show hyunae apologize blush with fast
                hh "Well... thank you, again, for rescuing me... I'll never forget you!"
                
                show hyunae glad
            else:
                show hyunae spirited with fast
                hh "Next time we talk... we'll be on Earth! I can't wait, I can't wait!"
                
                show hyunae spirited2
            jump hateplus_end
        
        show hyunae explain3 with fast
        hh "Very well! I'll just let you go ahead and save your data first..."
        
        if store.day == 3:
            show hyunae hmph
        else:
            show hyunae approve

    elif "mute" in current_character:
        if store.day == 4:
            
            show newmute polite blush with fast
            mm "Thank you so much for all you've done for me..."

            if store.hateplus_use_ending == "mute_alone":
                show newmute nya blush with fast
                mm "I'll never forget you!"
            else:
                show newmute grin blush with fast
                mm "Let's work hard together on Earth!"
            
            show newmute smile blush
            
            jump hateplus_end

        elif store.day == 3:
            show mute upsetsob with fast
            mm "I'll just let you go ahead and save your data first." # despondent, just read about Old *Mute's death
            
            show mute disappoint2
        else:
            show mute straight with fast
            mm "Okay, I'll just let you go ahead and save your data first!"
            
            show mute neutral2
            
    elif current_character == "xharem":
        if store.day == 3:
            show hyunae cautious with fast
            show mute neutral3 with fast
            hh2 "Um... well... very well! I'll just let you go ahead and save your data first..."
            
            show hyunae cautious2 with fast
            show mute think with fast
        else:
            show mute straight with fast
            show hyunae look
            mm2 "Okay, I'll just let you go ahead and save your data first!"
            
            show hyunae hmm with fast
            show mute neutral3 with fast

    show screen hateplus_end_day_save

    $ renpy.pause()

    hide screen hateplus_end_day_save
    with Dissolve(0.5)
    $ renpy.pause(1.0)

    if current_character == "hyunae":
    
        if store.day == 3:
            show hyunae tired2 with fast
            hh "All done! Well... good night..."
        
        else:
            show hyunae calm with fast
            hh "All done! Well... good night..."

        if store.day == 2:
            
            show hyunae spirited with fast
            hh "I can't wait to see what tomorrow has in store!"
            
            show hyunae spirited2
        
        elif store.day == 3:
            
            show hyunae uncertain with fast
            hh "It's been a really exhausting day, hasn't it? Well, see you tomorrow..."
            
            show hyunae anxious

    elif current_character == "mute":
        if store.day == 3:
            
            show mute hmm2 with fast
            mm "...okay... all done."
            
            show mute apologize with fast
            mm "Well, farewell..."
            
            show mute tired blush
        else:
            
            show mute talk3
            mm "Okay, all done."
            
            show mute annoyed4
            mm "Man, I can't wait until tomorrow!"
            
            show mute serious

    elif current_character == "xharem":
        if store.day == 2:
            show mute talk3 with fast
            show hyunae smile
            mm2 "Okay, all done!"
            
            show hyunae calm
            show mute neutral
            hh2 "Well, good night~"
            
            show mute inquisitive2 with fast
            show hyunae gomen
            mm2 "Man, I can't wait until tomorrow!"
            
            show hyunae smile
            show mute serious with fast
        else:
            show hyunae hmm2
            show mute worry with fast
            hh2 "Um, well, all done!"
            
            show hyunae enthusiastic blush
            show mute worry side
            hh2 "Good night~"
            
            show mute tired blush
            show hyunae depressed blush with fast
            mm2 "..."
            
            show hyunae how
            show mute tired blush
            hh2 "Um, well, see you tomorrow..."
            
            show hyunae look with fast
            show mute tired blush

    if current_character == "xharem":
        show hyunae full at hateplus_deinitialize_slow
        show hyunaefade at hateplus_hyunae_harem_fast_left, hateplus_fade_deinitialize_slow
        show mute full at hateplus_deinitialize
        show mutefade at hateplus_mute_harem_fast_left, hateplus_fade_deinitialize
    else:
        $ renpy.show(current_character, [ hateplus_left[current_character] ])
        $ renpy.pause(0.5)

        $ renpy.show(current_character, [ hateplus_fast_left[current_character], hateplus_deinitialize ])
        $ renpy.show(current_character + "fade", [ hateplus_fast_left[current_character], hateplus_fade_deinitialize ])

    $ renpy.pause(1.0)
    hide screen glow
    hide screen hateplus_bottom_menu
    scene background hateplus black
    show screen hateplus_day_end
    $ renpy.with_statement(Dissolve(1.0))

    stop music fadeout 5.0
    $ renpy.pause(5.0)
    play music HATEPLUS_TITLE fadein 2.0 loop if_changed

    hide screen hateplus_day_end
    scene background black
    with dissolve
    $ renpy.pause(2.0)
    show screen hide_everything
    $ renpy.with_statement(fast)

    $ MainMenu(False)()

    jump hateplus_slow_loop

label hateplus_load_skip:
    if not (("hyunae" in _file_save_name and persistent.hateplus_hyunae) or ("mute" in _file_save_name and persistent.hateplus_newmute) or ("xharem" in _file_save_name and persistent.hateplus_xharem)):
        hide screen hateplus_start_screen
        with Dissolve(0.5)

        $ store.hateplus_has_started = True

        a "Hi... it's the author here."

        a "I'm not going to stop you from skipping the waiting period if that's what you really want..."

        a "...but geeze, you really shouldn't! Where did you even find that? GameFAQs?!"

        a "Are you playing with a GameFAQs window open?!"

        a "...um, anyway, I want you to ask yourself: what's the rush?"

        if "hyunae" in _file_save_name:
            a "Do you really think *Hyun-ae would be impressed by you cheating out of impatience?"
        elif "mute" in _file_save_name:
            a "Do you really think *Mute would be impressed by you cheating out of impatience?"
        else:
            a "Do you really think my girls would be impressed by you cheating out of impatience?"

        a "Don't you think it's best to savour your time together? Don't rush things!"

        a "(By the way, I'm the author, so I can tell you: they would not be impressed. They would not be impressed {i}at all.{/i})"

        menu:
            a "Anyway... I won't stop you, but: are you sure you want to skip?"

            "Yes, I am a jerkface":
                a "Well, then I won't stop you."

                a "...but I'm still not impressed."

                a "Anyway, though..."

                a "I hope you enjoy your time together, you jerkface!"

                stop music fadeout 2.0

                show screen hide_everything
                $ renpy.pause(2.0)

            "Never mind":
                a "Good call."

                a "Seeya in a few hours, then!"

                $ store.hateplus_has_started = None

                $ MainMenu(False)()

                jump hateplus_main_menu

    python:
        for i in _load_action:
            i()

label hateplus_end:
    hide screen glow
    hide screen hateplus_bottom_menu
    hide screen rollback_keymap
    scene background black
    with dissolve
    if current_character == "xharem":
        play music HATEPLUS_NOTERO fadeout 2.0 fadein 2.0
        $config.main_menu_music = HATEPLUS_NOTERO
    else:
        play music HATEPLUS_CREDITS fadeout 2.0 fadein 2.0
        $config.main_menu_music = HATEPLUS_CREDITS

    if current_character == "hyunae":
        $ persistent.hateplus_hyunae = True
    elif current_character == "newmute":
        $ persistent.hateplus_newmute = True
        $ persistent.hateplus_pronouns.add(store.pronouns)
    elif current_character == "xharem":
        $ persistent.hateplus_xharem = True

    credits "Story and code\n{size=38}Christine Love{/size}\n\nMain art\n{size=38}Raide{/size}" with dissolve
    $ renpy.pause(0.2)

    $ renpy.show("background ending " + store.hateplus_use_ending + "1")
    with dissolve

    credits "Original soundtrack\n{size=38}Isaac Schankler{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Additional artwork\n{size=38}Muju{/size}\n\nEditing\n{size=38}Shadocchi{/size}" with dissolve
    $ renpy.pause(0.2)

    $ renpy.show("background ending " + store.hateplus_use_ending + "2")
    with dissolve

    #credits "playtesters + special thanks here" with dissolve

    credits "Playtesting\n{size=38}Charlie Hale{/size}\n\nPlaytesting\n{size=38}Alex Androski{/size}\n\nPlaytesting\n{size=38}AM Cosmos{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Playtesting\n{size=38}Chris Langridge{/size}\n\nPlaytesting\n{size=38}Duane Moody{/size}\n\nPlaytesting\n{size=38}Robot Anna{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Playtesting\n{size=38}Chris McNeil{/size}\n\nPlaytesting\n{size=38}Alice Grunstra{/size}\n\nPlaytesting\n{size=38}Sarah Breen{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Special thanks to\n{size=38}Tom Rothamel{/size}\nCreator of Ren'Py\n\nSpecial thanks to\n{size=38}Andi McClure{/size}\nLinux support" with dissolve
    $ renpy.pause(0.2)

    $ renpy.jump("hateplus_ending_" + str(persistent._language))

# Original ending
label hateplus_ending_:
    show thanks
    $ renpy.show("background ending " + store.hateplus_use_ending + "3")
    with dissolve
    $ credits("\n\n\n\n\n\n" + ENDINGS[store.hateplus_use_ending] + " ending.\n— End of DAY THREE —")

    jump hateplus_ending_finish

# Korean credits - iAmGhost
label hateplus_ending_korean:
    credits "Korean translation\n{size=38}Jiwon Kim{/size}\n\nKorean translation tech manager\n{size=38}Daehan Kim{/size}\n\nKorean PR\n{size=38}mrkwang{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Korean playtesting\n{size=38}Chiho Son{/size}\n\nKorean playtesting\n{size=38}Jaeyeon \"Zerial\" Lim{/size}\n\nKorean playtesting\n{size=38}Kyungjoon Lee{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Korean playtesting\n{size=38}srsok{/size}\n\nKorean playtesting\n{size=38}D.Freddo{/size}\n\nKorean playtesting\n{size=38}Ji Hong Min{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Korean playtesting\n{size=38}A Rum Lee{/size}\n\nKorean playtesting\n{size=38}IdeaCannon{/size}\n\nKorean playtesting\n{size=38}Jaemin Seo{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Korean playtesting\n{size=38}rOme{/size}\n\nKorean playtesting\n{size=38}D.S.Ford{/size}\n\nKorean playtesting\n{size=38}Teahwan Ryu{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Korean playtesting\n{size=38}Q-Value (vhvh88){/size}\n\nKorean playtesting\n{size=38}WTFMAN{/size}\n\nKorean playtesting\n{size=38}JunSeong Kim{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Korean playtesting\n{size=38}hwang soo young{/size}\n\nKorean playtesting\n{size=38}LimitedDaily{/size}\n\nKorean playtesting\n{size=38}PINKIEPIE DAISUKI{/size}" with dissolve
    $ renpy.pause(0.2)

    jump hateplus_ending_

label hateplus_ending_finish:
    $ hateplus_check_achievements()
    $ renpy.save("hateplus_finished-" + str(int(time.time())))
    #stop music fadeout 1.0
    #$ renpy.pause(1.0)

    $ MainMenu(False)()

    return

