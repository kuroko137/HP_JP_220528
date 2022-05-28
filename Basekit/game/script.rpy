# HIDE RECENT MESSAGES WHILE OVERRIDE IS IN PLACE, ALWAYS HIDE SIDE MENU EFFECTS ON SAY
# ADD REAL NAME IN BRIEF STAMMERING FLASH?

init:
    python:
        import copy, atexit, time
    
        radiation = False
        renderer = None
        outfit = ""
        outfits = { "M":"maid", "D":"detective" }
        outfit_change = { "M":"as a maid", "D":"as a detective" }
        noglasses = [ ]

        if not persistent._language:
            persistent._language = ""
        if not persistent.blocks:
            persistent.blocks = [ ]
        store.old_block_count = len(persistent.blocks)
    
        h_en = Character("*Hyun-ae", color=(255,255,255,220), window_top_padding=0, show_two_window=True)
        h_en_input = h_en.copy(screen="say_input")
        h_damage = Character("", window_background=None)
        m_en = Character("*Mute", color=(255,255,255,220), window_top_padding=0, show_two_window=True)
        narrator_en = Character(None)
        h2_en = h_en.copy(window_yalign=0.85, window_xalign=0.5, window_background=Frame(im.Composite(None, (0,0), "window.png", (0,0), "window.png", (0,0), "window.png"), 20, 20))
        m2_en = m_en.copy(window_yalign=0.85, window_xalign=0.5, window_background=Frame(im.Composite(None, (0,0), "window.png", (0,0), "window.png", (0,0), "window.png"), 20, 20))
        intro_en = NVLCharacter(None, what_color=(255,255,255,255), window_xmargin=170, what_bold=False, what_font="fonts/Planer-Regular.otf", what_line_leading=-4)
        endtro_en = intro_en.copy(window_xmaximum=350, window_xmargin=0, window_xanchor=0, window_xpos=610)
        credits_en = Character("", what_color=(255,255,255,255), what_font="fonts/Planer-Regular.otf", window_background=None, window_xpos=570, window_xanchor=0, what_bold=False)

        class MultilingualCharacter:
            def __init__(self, english, **kwargs):
                self.languages = { }
                self.languages[""] = english

            def __call__(self, s, interact=True):
                if persistent._language in self.languages:
                    return self.languages[persistent._language](s, interact)
                else:
                    return self.languages[""](s, interact)

        h = MultilingualCharacter(h_en)
        h_input = MultilingualCharacter(h_en_input)
        m = MultilingualCharacter(m_en)
        h2 = MultilingualCharacter(h2_en)
        m2 = MultilingualCharacter(m2_en)
        narrator = MultilingualCharacter(narrator_en)
        intro = MultilingualCharacter(intro_en)
        endtro = MultilingualCharacter(endtro_en)
        credits = MultilingualCharacter(credits_en)
    
        try:
            import steam_api
        except Exception, e:
            using_steam = None
        else:
            using_steam = steam_api.SteamAPI_Init()
        if using_steam:
            atexit.register(steam_api.SteamAPI_Shutdown)

        #persist = MultiPersistent("scoutshonour.com")
        CHARACTERS = { "mute":"Mute", "hyunae":"Hyun-ae", "x":"" }
        current_character = ""

        PROLOGUE = "music/prologuemastered01152012.mp3"
        HYUNAE = "music/hyunaenicemastered01302012.mp3"
        HYUNAE_CHEER = "music/hyunaecheer01222012.mp3"
        MUTE = "music/mute12172011.mp3"
        MUTE_INTRO = "music/muteintroamastered01252012.ogg"
        MUTE_CHEER = "music/muteintrobmastered01252012.ogg"
        SMITH = "music/smithsmastered01172012.mp3"
        TERMINAL = "music/terminalcalmmastered0130201.mp3"

        if not renpy.demo_mode:
            HYUNAE_DRAMATIC = "music/hyunaedramamaster01262012.nd.mp3"
            HYUNAE_GLITCHY = "music/hyunaeglitchmastered0127201.nd.ogg"
            MUTE_DRAMATIC = "music/mutedramamastered01272012.nd.mp3"
            MUTE_GLITCHY = "music/muteglitchmastered01272012.nd.ogg"
            RYU = "music/ryusmastered01182012.nd.mp3"
            REACTOR = "music/reactorloopmastered01302012.nd.ogg"
            REACTOR_TERMINAL = "music/terminalreactormastered0130.nd.mp3"
            CREDITS = "music/creditschipmastered01292012c.nd.mp3"
            CREDITS_SOMBER = "music/creditssombermastered01302012.nd.mp3"
        else:
            HYUNAE_DRAMATIC = HYUNAE_GLITCHY = MUTE_DRAMATIC = MUTE_GLITCHY = RYU = REACTOR = REACTOR_TERMINAL = CREDITS = CREDITS_SOMBER = ""

        def t(s):
            if not config.translator: return s
            else: return config.translator.translate(s)

        def switch_character(target):
            global current_character
            
            renpy.show("background invert")
            renpy.hide(current_character)
            renpy.with_statement(dissolve)
            
            renpy.pause(1.0)
            current_character = target
            
            renpy.show("background")
            renpy.with_statement(dissolve)
            renpy.pause(1.0)
            renpy.show(current_character + " neutral", [ fast_left[current_character] ])
            renpy.with_statement(dissolve)

        def load_character():
            global current_character

            renpy.free_memory()
            for i in images_registered.keys():
                if current_character in i:
                    renpy.cache_pin(images_registered[i])
                else:
                    renpy.cache_unpin(images_registered[i])

        subsystems = { }
        subsystems["gravity"] = { "description":"artificial gravity for all habitable decks.", "usage":36 }
        subsystems["sensors"] = { "description":"external visible spectrum and radar sensor arrays.", "usage":11 }
        subsystems["core1"] = { "description":"stores and executes AI construct *Mute.", "usage":5 }
        subsystems["core2"] = { "description":"stores and executes AI construct *Hyun-ae.", "usage":5 }
        subsystems["core3"] = { "description":"storage empty, not currently in use.", "usage":5 }
        subsystems["core4"] = { "description":"storage empty, not currently in use.", "usage":5 }
        subsystems["core5"] = { "description":"storage empty, not currently in use.", "usage":5 }
        subsystems["core6"] = { "description":"storage empty, not currently in use.", "usage":5 }
        #subsystems["core7"] = { "description":"storage empty, not currently in use.", "usage":4 }
        #subsystems["core8"] = { "description":"storage empty, not currently in use.", "usage":4 }
        subsystems["rail"] = { "description":"Rail Internal Transit system, for rapid access across decks.", "usage":4 }
        subsystems["docking"] = { "description":"Docking system for passenger transport.", "usage":1 }
        subsystems["waste"] = { "description":"organic waste matter recycling system.", "usage":3 }
        subsystems["communications"] = { "description":"external radio-based communication array.", "usage":6 }
        subsystems["main_computer"] = { "description":"controls main functionality and cores, DO NOT EVER DISABLE", "usage":7 }
        subsystems["life_support"] = { "description":"life support systems providing breathable air.", "usage":1 }
        subsystems["bulkheads"] = { "description":"bulkhead seals maintaining proper atmosphere.", "usage":1 }

        def parse_terminal(line):
            global current_character, su, yes_no, available_characters
            if line == None:
                line = ""

            nb = [ ">" + line.replace("[", "[[").replace("{", "{{") ]

            def power_safe(system=False):
                use = 0
                target = 20
                for i in enabled_subsystems:
                    use += subsystems[i]["usage"]

                if system:
                    target -= subsystems[system]["usage"]
                return not store.pss_primary and use <= target

            def beep():
                global buf
                if buf and ("ERROR" in buf[-1] or "WARNING" in buf[-1] or "ACCESS DENIED" in buf[-1] or "UNKNOWN COMMAND" in buf[-1]):
                    renpy.music.play("sfx/fxbeep8.mp3", channel="sound")
                else:
                    renpy.music.play("sfx/fxbeep5.mp3", channel="sound")
                
            def multi_buf(*lines):
                for line in lines:
                    buf.append(line)
                        
                    if ">" in line:
                        renpy.call_screen("terminal", buf=buf, pause=0.01)
                    elif line != "":
                        beep()
                        renpy.call_screen("terminal", buf=buf, pause=0.5)
                    else:
                        renpy.call_screen("terminal", buf=buf, pause=0.05)
                
                if "Y/N" in buf[-1]:
                    renpy.music.play("sfx/fxbeep5.mp3", channel="sound")
                elif not "ERROR" in buf[-1]:
                    renpy.music.play("sfx/fxbeep4.mp3", channel="sound")
            
            def help(command):
                def usage(full):
                    power_use = 0
                    for i in enabled_subsystems:
                        power_use += subsystems[i]["usage"]
                    
                    if full:
                        nb.append([ "power usage is at ", str(power_use) + "%", ", currently enabled subsystems:" ])
                        for i in enabled_subsystems:
                            nb.append([ "    ", i, ": ", subsystems[i]["description"], " (" + str(subsystems[i]["usage"]) + "%)" ])

                        if "list" in command and len(enabled_subsystems) != len(subsystems):
                            nb.append("")
                            nb.append("currently disabled subsystems:")
                            for i in subsystems.keys():
                                if i not in enabled_subsystems:
                                    nb.append([ "    ", i, ": ", subsystems[i]["description"], " (" + str(subsystems[i]["usage"]) + "%)" ])
                    else:
                        nb.append([ "power usage is at ", str(power_use) + "%" ])

                if command == "enable_ai":
                    nb.append("USAGE: {b}enable_ai{/b} [[personality]")
                    nb.append("used to select a new AI personality. any active personality must be disabled first.")
                    help("personalities")
                elif command == "disable_ai":
                    nb.append("USAGE: {b}disable_ai{/b}")
                    nb.append("used to disable the current AI personality. a new personality must be enabled afterwards to quit this terminal")
                elif command == "personalities":
                    nb.append("currently available personalities:")
                    for i in available_characters:
                        nb.append("    *" + i)
                elif command == "quit":
                    nb.append("USAGE: {b}quit{/b}")
                    nb.append("quit the override terminal and return to the currently active AI personality")
                elif command == "help":
                    nb.append("USAGE: {b}help{/b} [[command]")
                    nb.append([ "AVAILABLE COMMANDS", ": download, disable_ai, enable_ai, help, su, quit" ])
                    if su:
                        if not asked_about_cosplay:
                            nb.append("                    reactor, pss, copy, power_control, decrypt")
                        else:
                            nb.append("                    reactor, pss, copy, power_control, decrypt, change_outfit")
                elif command == "su":
                    nb.append("USAGE: {b}su{/b} [[password]")
                    nb.append("provides administrator access, requires password to use")
                elif command == "download":
                    nb.append("USAGE: {b}download{/b}")
                    nb.append("downloads all indexed log files, and optionally any currently active AI personality")
                    nb.append("WARNING: this will permanently disconnect your session")
                elif command == "reactor":
                    nb.append("USAGE: {b}reactor{/b} [[action]")
                    nb.append("emergency override control over the reactor system")
                    nb.append("AVAILABLE ACTIONS: enable, disable")
                elif command == "pss":
                    nb.append("USAGE: {b}pss{/b} [[action]")
                    nb.append("emergency control override of power storage system")
                    nb.append("AVAILABLE ACTIONS: switch_battery, enable, disable")
                elif command == "pss status":
                    if pss_enabled:
                        if pss_primary:
                            nb.append("power storage system status: enabled, using primary battery")
                        else:
                            nb.append("power storage system status: enabled, using secondary battery")
                    else:
                        if pss_primary:
                            nb.append("power storage system status: disabled (will use primary battery when enabled)")
                        else:
                            nb.append("power storage system status: disabled (will use secondary battery when enabled)")

                    nb.append("primary battery remaining -- 0.1%")
                    nb.append("secondary battery remaining -- 20%")
                    usage(False)
                elif command == "copy":
                    nb.append("USAGE: {b}copy{/b} [[source core] [[target core]")
                    nb.append("transfers data stored in source core into target core")
                    nb.append("WARNING: any AI program transferred will be unexecutable until stored in own core")
                elif command.startswith("power_control"):
                    if not "list" in command:
                        nb.append("USAGE: {b}power_control{/b} [[action] [[target subsystem]")
                        nb.append("emergency controls of critical subsystems")
                        nb.append("AVAILABLE ACTIONS: enable, disable, list")
                        nb.append("multiple systems can be enabled/disabled in a single line")

                    if not "short" in command:
                        usage(True)

                elif command == "decrypt":
                    nb.append("USAGE: {b}decrypt{/b} [[block]")
                    nb.append("decrypts block of data to be accessed by all (including AIs)")
                elif command == "change_outfit":
                    all_costumes = [ ]
                    for i in outfits.values():
                        all_costumes.append(i)
                        all_costumes.append(", ")
                    all_costumes.pop()

                    nb.append("USAGE: {b}change_outfit{/b} [[costume]")
                    nb.append("dresses up *Hyun-ae in an alternate outfit")
                    nb.append([ "AVAILABLE COSTUMES: ", "schoolgirl (default)", ", " ] + all_costumes[:6])
                    if len(all_costumes) > 6:
                        nb.append([ "                    {k=1}{/k}" ] + all_costumes[6:12])
                elif command == "admin":
                    nb.append("provides administrator access (use {b}su{/b}, requires valid password)")
                elif "hyunae" in command.replace("*", "").replace("-", "").replace("_", "").replace(" ", ""):
                    nb.append("ERROR: *Hyun-ae unknown, not a registered AI")
                elif command == "mute":
                    nb.append("*Mute is the ship's security AI")
                else:
                    return False
                    
                return True
            
            line = line.lower().replace(",", "")
            args = line.split() or [ "" ]

            if line == "init":
                nb = [ ]
                multi_buf("keOS/Amie 8.11 {b}Starship Mugunghwa internal computer{/b} Mon Jan 1 00:00:00 1970", "", "", "", "Notice: This system is property of the Unified Korea Space Probe Agency. Access by", "individuals not affiliated with the UKSPA or a successor organization is a felony", "under the UKSPA Act of 2381.", "", "", "", "", "Last login: user \"Kim Hyun-ae\", 221432 days ago", "ERROR: AI PERSONALITY CURRENTLY DISABLED, REVERTING TO COMMAND LINE", ["AVAILABLE COMMANDS", ": download, disable_ai, enable_ai, help, su, quit"])
                return [ ]

            if yes_no:
                action = yes_no[0]
                if action == None:
                    pass
                elif action == "corruption":
                    if line == "y" or line == "yes":
                        yes_no[yes_no.index(action)] = None
                        #for i in reversed(buf):
                        #    if i == "data corruption in AI core1 has been detected; try recovering now? (Y/N)":
                        multi_buf(">" + line, "checking for damaged sectors...", [ "32 damaged sectors detected, now attempting repair...", "0%" ])
                        for num in range(101):
                            if num % 10 == 0 or random.random() < 0.6 or num < 20:
                                buf[-1] = [ "32 damaged sectors detected, now attempting repair... ", str(num) + "%" ]
                                renpy.call_screen("terminal", buf=buf, pause=0.3)
                                
                        multi_buf("SUCCESS: 32 sectors repaired!", "", "", "", "currently available personalities:", "    *Hyun-ae", "    *Mute")
                        if not download_character:
                            available_characters = [ "Hyun-ae", "Mute" ]
                        
                        nb = [ ]
                                
                    elif line == "n" or line == "no":
                        su = False
                        yes_no[yes_no.index(action)] = None
                        nb.append("ERROR: unable to proceed without performing recovery, returning to restricted mode")
                        #beep()
                elif action in [ "communications", "main_computer", "pss" ]:
                    if line == "y" or line == "yes":
                        multi_buf(">" + line, "Working...", "", "")
                        renpy.jump("connection_error")
                    elif line == "n" or line == "no":
                        nb.append([ action, " will remain enabled" ])
                        #beep()
                        yes_no[yes_no.index(action)] = None
                elif action == "life_support":
                    if line == "y" or line == "yes":
                        nb.append(["SUCCESS: ", "life_support", " has been disabled!" ])
                        enabled_subsystems.remove("life_support")
                        yes_no[yes_no.index(action)] = None
                    elif line == "n" or line == "no":
                        nb.append(["life_support", " will remain enabled"])
                        yes_no[yes_no.index(action)] = None
                elif action in enabled_subsystems:
                    if active_core_data[int(action[-1])-1] == "hyunae" and store.radiation:
                        store.attempted_disable_hyunae = True
                        greeting["mute"] = "mute_why_havent"

                    if line == "y" or line == "yes":
                        multi_buf(">" + line, "Working...", "", [ "SUCCESS: ", action, " has been disabled!" ])
                        enabled_subsystems.remove(action)
                        
                        if "core" in action:
                            if active_core_data[int(action[-1])-1]:
                                if available_characters:
                                    available_characters.remove(CHARACTERS[active_core_data[int(action[-1])-1]])
                                if CHARACTERS[current_character] not in available_characters:
                                    current_character = "x"

                        yes_no[yes_no.index(action)] = None
                        nb = [ ]
                    elif line == "n" or line == "no":
                        nb.append([ action, " will remain enabled" ])
                        #store.attempted_disable_hyunae = False
                        #beep()
                        yes_no[yes_no.index(action)] = None
                elif "reactor" in action:
                    if line == "y" or line == "yes":
                        multi_buf(">" + line, "reactor is going down... this may take a minute", "", "", "initiating reactor shutdown sequence...")
                        for num in range(101):
                            if num % 10 == 0 or random.random() < 0.6 or num < 20:
                                buf[-1] = [ "initiating reactor shutdown sequence... ", (str(num) + "%") ]
                                renpy.call_screen("terminal", buf=buf, pause=0.2)

                        if "kill" in action:
                            renpy.jump("connection_error")
                        else:
                            multi_buf("SUCCESS: nuclear reactor is disabled!", "Logging disabled, engaging low power mode...NOW", "", "", "SUCCESS: remaining subsystems transferred to power supply system")
                            yes_no[yes_no.index(action)] = None
                            store.reactor_enabled = False

                        nb = [ ]
                    elif line == "n" or line == "no":
                        nb.append("reactor will remain enabled")
                        #beep()
                        yes_no[yes_no.index(action)] = None
                elif action == "download":
                    if (line == "a" or line == "abort") or (not download_character and (line == "n" or line == "no")):
                        nb.append("no files will be transferred")
                        yes_no[yes_no.index(action)] = None
                    elif line == "y" or line == "yes" or line == "n" or line == "no":
                        if line == "y" or line == "yes":
                            if download_character:
                                multi_buf(">" + line, "*" + download_character + " will be transferred", "preparing files for transfer... NOW", "", "", "transmitting...")
                            else:
                                multi_buf(">" + line, "preparing files for transfer... NOW", "", "", "transmitting...")
                                store.use_ending = "ending3"
                        else:
                            multi_buf(">" + line, "*" + download_character + " will NOT be transferred", "preparing files for transfer... NOW", "", "", "transmitting...")
                            store.use_ending = "ending3"
                        

                        for i in [ "Receiving files", "Estimated download time: 3d 23h 00m" ]:
                            renpy.call_screen("connecting", message=i)
                        renpy.show_screen("connecting", message="Estimated download time: 3d 22h 59m")
                        renpy.pause(0.5)
                        renpy.jump("credits")

                while None in yes_no:
                    yes_no.remove(None)
            elif "[" in line:
                nb.append("ERROR: invalid syntax, do not include brackets")
                #beep()
            else:
                if config.developer:
                    if line == "radiation":
                        nb.append("radiation: " + str(store.radiation_levels))
                    if line == "clock_up":
                        store.death_clock = 7*60
                    if line.startswith("ending"):
                        store.use_ending = line
                        renpy.jump("credits")

                if line == "":
                    pass
                elif "help" in line or line.startswith("?"):
                    if not " " in line or not help(line.split(" ")[1]):
                        help("help")
                elif args[0] == "enable_ai":
                    if not " " in line:
                        help("enable_ai")
                    #elif current_character != "x":
                    #    nb.append("ERROR: an AI personality is already active! disable with {b}disable_ai{/b} first")
                    elif ((len(args) > 1 and args[1].replace("*", "").replace("-", "").replace("_", "") == "hyunae") or (len(args) > 2 and args[1] == "hyun" and args[2] == "ae") or (len(args) > 1 and args[1].replace("*", "").replace("-", "").replace("_", "") == "hyeonae") or (len(args) > 2 and args[1] == "hyeon" and args[2] == "ae")) and "Hyun-ae" in available_characters:
                        if store.death_clock < 20*60 and locked_in != "hyunae":
                            nb.append("ERROR: an unknown switching error occurred, unable to initialize AI *Hyun-ae")
                        elif current_character == "hyunae":
                            nb.append("ERROR: personality *Hyun-ae is already active!")
                        else:
                            current_character = "hyunae"
                            load_character()
                            nb.append("SUCCESS: personality *Hyun-ae is now activated!")
                            nb.append("you may now close this terminal with {b}quit{/b}.")
                    elif "mute" in line and "Mute" in available_characters:
                        if store.death_clock < 20*60 and locked_in != "mute" or (store.override_conversation and "intercept" in store.override_conversation):
                            nb.append("ERROR: an unknown switching error occurred, unable to initialize AI *Mute")
                        elif current_character == "mute":
                            nb.append("ERROR: personality *Mute is already active!")
                        else:
                            current_character = "mute"
                            load_character()
                            nb.append("SUCCESS: personality *Mute is now activated!")
                            nb.append("you may now close this terminal with {b}quit{/b}.")
                            store.demo_finished = True
                    else:
                        nb.append("ERROR: invalid personality specified.")
                        #beep()
                        help("personalities")
                elif args[0] == "disable_ai":
                    if current_character == "x":
                        nb.append("ERROR: no AI personality currently enabled!")
                        #beep()
                    elif not " " in line:
                        renpy.show_screen("bottom_menu")
                        nb.append("SUCCESS: personality *" + CHARACTERS[current_character] + " is now deactivated!")
                        current_character = "x"
                        nb.append("you may now activate a new AI personality with {b}enable_ai{/b}")
                    else:
                        nb.append("ERROR: no parameters are required, just type {b}disable_ai{/b}")
                        #beep()
                elif args[0] == "quit":
                    if current_character == "x":
                        nb.append("ERROR: nothing to quit to! activate an AI personality with {b}enable_ai{/b} first")
                        #beep()
                    else:
                        renpy.jump("restart")
                elif args[0] == "download":
                    if not su:
                        nb.append("ERROR: admin access required! please use su first")
                        #beep()
                    else:
                        nb.append("WARNING: starting active systems download will permanently terminate session")
                        if " " in download_character:
                            nb.append("AI personalities are available.")
                            nb.append("download *" + download_character + " in addition to logs? (Yes/No/Abort)")
                        elif download_character:
                            nb.append("AI personality is available.")
                            nb.append("download *" + download_character + " in addition to logs? (Yes/No/Abort)")
                        else:
                            nb.append("are you sure you want to continue? no AI personality will be downloaded (Y/N)")
                        yes_no = [ "download" ]
                elif args[0] == "reactor":
                    if not su:
                        nb.append("ERROR: admin access required! please use su first")
                        #beep()
                    elif not " " in line or len(args) <= 1:
                        if reactor_enabled:
                            nb.append("STATUS: reactor is currently enabled")
                        else:
                            nb.append("STATUS: reactor is currently disabled")
                        nb.append("")
                        help("reactor")
                    elif args[1] == "enable":
                        if reactor_enabled:
                            nb.append("ERROR: reactor is already enabled and active!")
                            #beep()
                        else:
                            nb.append("Starting reactor...")
                            nb.append("")
                            nb.append("ERROR: an unknown error occurred, cannot start reactor")
                            #beep()
                    elif args[1] == "disable":
                        if not reactor_enabled:
                            nb.append("ERROR: reactor is already disabled and inactive!")
                            #beep()
                        elif not locked_in:
                            nb.append("ERROR: reactor has not been maintained recently, shutdown could cause damage")
                            nb.append("unable to safely disable in a non-emergency situation")
                        else:
                            store.failed_initial_shutdown = True
                            if not pss_enabled:
                                nb.append("ERROR: no backup power supply is active!")
                                nb.append("WARNING: disabling reactor now will permanently terminate your connection")
                                nb.append("are you sure you want to continue? (Y/N)")
                                yes_no = [ "reactor_kill" ]
                            elif not power_safe():
                                nb.append("ERROR: backup power supply has insufficient power!")
                                nb.append("WARNING: disabling reactor now will permanently terminate your connection")
                                nb.append("are you sure you want to continue? (Y/N)")
                                yes_no = [ "reactor_kill" ]
                            else:
                                nb.append("will safely fall back on pss if reactor disabled, continue? (Y/N)")
                                yes_no = [ "reactor" ]
                    else:
                        nb.append("ERROR: invalid action specified")
                        nb.append("")
                        help("reactor")
                elif args[0] == "decrypt":
                    if not su:
                        nb.append("ERROR: admin access required! please use su first")
                        #beep()
                    elif not " " in line or len(args) <= 1:
                        help("decrypt")
                    elif args[1] == "block3":
                        if not store.block3_decrypted:
                            store.block3_decrypted = True
                            if conversation["hyunae"] == "back_to_hyunae":
                                conversation["hyunae"] = "back_to_hyunae2"
                            nb.append("Decrypting block now...")
                            nb.append("")
                            nb.append("")
                            nb.append("SUCCESS: block successfully decrypted!")
                            store.demo_finished = True
                        else:
                            nb.append("ERROR: block is not encrypted! (did you already decrypt it?)")
                            #beep()
                    elif args[1] == "block7":
                        if not store.block7_decrypted:
                            #greeting["hyunae"] = "decrypted_block7"
                            store.block7_decrypted = True
                            nb.append("Decrypting block now...")
                            nb.append("")
                            nb.append("")
                            nb.append("SUCCESS: block successfully decrypted!")
                        else:
                            nb.append("ERROR: block is not encrypted! (did you already decrypt it?)")
                            #beep()
                    else:
                        nb.append("ERROR: invalid block specified!")
                        #beep()
                elif args[0] == "copy":
                    if not su:
                        nb.append("ERROR: admin access required! please use su first")
                        #beep()
                    elif len(args) < 3:
                        nb.append("ERROR: not enough arguments given")
                        nb.append("")
                        help("copy")
                    else:
                        possible_args = [ ("core" + str(i+1)) for i in range(6) ]
                        if not args[1] in possible_args or not args[2] in possible_args:
                            nb.append("ERROR: invalid core name given, valid cores are core1 to core6")
                            #beep()
                        else:
                            index1, index2 = int(args[1][-1])-1, int(args[2][-1])-1

                            if index1 == index2:
                                nb.append("ERROR: unable to copy core into itself")
                                #beep()
                            elif inactive_core_data[index1]:
                                if active_core_data[index2] and inactive_core_data[index2]:
                                    nb.append("ERROR: core already full!")
                                    #beep()
                                elif args[2] not in enabled_subsystems:
                                    nb.append("ERROR: that core is unpowered!")
                                elif not active_core_data[index2]:
                                    active_core_data[index2], inactive_core_data[index1] = inactive_core_data[index1], ""
                                    nb.append("Copying...")
                                    nb.append("")
                                    nb.append("SUCCESS: *" + CHARACTERS[active_core_data[index2]] + " data has been transferred to active storage in " + args[2])
                                    nb.append("SUCCESS: AI personality *" + CHARACTERS[active_core_data[index2]] + " is now available")

                                    available_characters.append(CHARACTERS[active_core_data[index2]])
                                else:
                                    inactive_core_data[index2], active_core_data[index1] = active_core_data[index1], ""
                                    nb.append("Copying...")
                                    nb.append("")
                                    nb.append("SUCCESS: *" + CHARACTERS[inactive_core_data[index2]] + " data has been transferred to inactive storage in " + args[2])
                                    #beep()
                            elif active_core_data[index1]:
                                if download_character:
                                    nb.append("ERROR: an unknown error occurred (you cannot perform that action)")
                                    #beep()
                                elif active_core_data[index1] == current_character:
                                    nb.append("ERROR: unable to transfer AI from core while AI is still enabled!")
                                    #beep()
                                elif active_core_data[index2] and inactive_core_data[index2]:
                                    nb.append("ERROR: core already full!")
                                    #beep()
                                elif args[2] not in enabled_subsystems:
                                    nb.append("ERROR: that core is unpowered!")
                                elif not active_core_data[index2]:
                                    active_core_data[index2], active_core_data[index1] = active_core_data[index1], ""
                                    nb.append("Copying...")
                                    nb.append("")
                                    nb.append("SUCCESS: *" + CHARACTERS[active_core_data[index2]] + " data has been transferred to active storage in " + args[2])
                                else:
                                    inactive_core_data[index2], active_core_data[index1] = active_core_data[index1], ""
                                    nb.append("Copying...")
                                    nb.append("")
                                    nb.append("SUCCESS: *" + CHARACTERS[inactive_core_data[index2]] + " data has been transferred to inactive storage in " + args[2])
                                    nb.append("WARNING: AI personality *" + CHARACTERS[inactive_core_data[index2]] + " is no longer available")
                                    #beep()

                                    if CHARACTERS[inactive_core_data[index2]] in available_characters:
                                        available_characters.remove(CHARACTERS[inactive_core_data[index2]])
                            else:
                                nb.append("ERROR: no data in " + args[1])
                                #beep()
                        
                        for i in range(len(active_core_data)):
                            if active_core_data[i]:
                                if inactive_core_data[i]:
                                    subsystems["core" + str(i+1)]["description"] = "runs *" + CHARACTERS[active_core_data[i]] + ", *" + CHARACTERS[inactive_core_data[i]] + " in inactive storage."
                                else:
                                    subsystems["core" + str(i+1)]["description"] = "stores and executes AI construct *" + CHARACTERS[active_core_data[i]] + "."
                            else:
                                subsystems["core" + str(i+1)]["description"] = "storage empty, not currently in use."

                elif args[0] == "power_control":
                    if not su:
                        nb.append("ERROR: admin access required! please use su first")
                        #beep()
                    elif not " " in line or len(args) <= 1:
                        nb.append("ERROR: no action given")
                        nb.append("")
                        help("power_control short")
                    elif "list" in line:
                        help("power_control list")
                    elif len(args) < 3:
                        if "enable" in line or "disable" in line:
                            nb.append("ERROR: no subsystem specified")
                        else:
                            nb.append("ERROR: invalid action specified")
                        nb.append("")
                        help("power_control short")
                    elif not args[2] in subsystems.keys():
                        nb.append("ERROR: not a valid subsystem! (try {b}power_control list{/b} for full list)")
                        #beep()
                    elif args[1] == "enable":
                        for i in args[2:]:
                            if not i in subsystems.keys():
                                    nb.append([ "ERROR: ", i, " is not a valid subsystem!" ])
                            elif i in enabled_subsystems:
                                nb.append("ERROR: that subsystem is already enabled!")
                                #beep()
                            elif not reactor_enabled and not power_safe(i):
                                nb.append("ERROR: insufficient power to enable that subsystem! (try disabling some others?)")
                                #beep()
                            else:
                                if i == "life_support":
                                    if "bulkheads" not in enabled_subsystems:
                                        nb.append("ERROR: unable to enable life support while bulkheads are unsealed")
                                        return nb

                                enabled_subsystems.append(i)
                                nb.append("Working...")
                                nb.append("")
                                nb.append([ "SUCCESS: ", i, " has been enabled!" ])
                                if "core" in i and active_core_data[int(i[-1])-1]:
                                    available_characters.append(CHARACTERS[active_core_data[int(i[-1])-1]])
                    elif args[1] == "disable":
                            for i in args[2:]:
                                if not i in subsystems.keys():
                                    nb.append("ERROR: " + i + " is not a valid subsystem!")
                                elif not i in enabled_subsystems:
                                    nb.append([ "ERROR: subsystem ", i, " is already disabled!" ])
                                elif i in [ "communications", "main_computer" ]:
                                    yes_no.append(i)
                                elif "core" in i and active_core_data[int(i[-1])-1]:
                                    if available_characters:
                                        yes_no.append(i)
                                    else:
                                        nb.append("ERROR: an unknown error occurred (you cannot perform that action)")
                                        #beep()
                                elif i == "life_support":
                                    yes_no.append(i)
                                else:
                                    #nb.append("Working...")
                                    #nb.append("")
                                    nb.append([ "SUCCESS: ", i, " has been disabled!" ])
                                    enabled_subsystems.remove(i)
                                    if i == "bulkheads" and "life_support" in enabled_subsystems:
                                        nb.append("WARNING: atmosphere is being vented into space!")

                                        if not reactor_enabled:
                                            store.atmosphere_vented = True
                                            persistent.korean_fusion = True
                                            renpy.hide_screen("death_clock")
                                            multi_buf(*nb)
                                            nb = [ ]
                                            for i in range(21):
                                                store.radiation_levels -= 0.05
                                                renpy.call_screen("terminal", buf=buf, pause=0.2)
                                            renpy.hide_screen("radiation")
                                            store.radiation = False
                                            renpy.music.play(TERMINAL, fadein=1.0, fadeout=1.0, loop=True)
                    else:
                        nb.append("ERROR: invalid action specified")
                        nb.append("")
                        help("power_control short")
                elif args[0] == "pss" or "switch_battery" in line:
                    if not su:
                        nb.append("ERROR: admin access required! please use su first")
                        #beep()
                    elif not " " in line and "switch_battery" not in line or len(args) <= 1:
                        help("pss")
                        help("pss status")
                    elif "enable" in line:
                        if not pss_enabled:
                            store.pss_enabled = True
                            nb.append("Working...")
                            nb.append("")
                            nb.append("SUCCESS: power storage system has been enabled!")
                            if not power_safe():
                                nb.append("WARNING: insufficient power in active battery to meet power demands without reactor")
                                nb.append("")
                                help("pss status")
                                nb.append("try disabling unnecessary subsystems with {b}power_control{/b}")
                            else:
                                nb.append("you may now safely disable reactor power")
                        else:
                            nb.append("ERROR: pss is already enabled!")
                            nb.append("")
                            help("pss status")
                    elif len(args) > 1 and args[1] == "disable":
                        if pss_enabled:
                            if not reactor_enabled:
                                nb.append("WARNING: disabling pss and reactor will permanently terminate your connection!")
                                nb.append("are you sure you want to continue? (Y/N)")
                                yes_no = [ "pss" ]
                            else:
                                store.pss_enabled = False
                                nb.append("Working...")
                                nb.append("")
                                nb.append("SUCCESS: power storage system has been disabled! now running on reactor power exclusively")
                        else:
                            nb.append("ERROR: pss is already disabled!")
                            nb.append("")
                            help("pss status")
                    elif (len(args) > 1 and args[1] == "switch") or "switch_battery" in line:
                        if reactor_enabled:
                            nb.append("SUCCESS: active battery changed!")
                            store.pss_primary = not store.pss_primary
                            nb.append("")
                            help("pss status")

                            if not power_safe():
                                nb.append("WARNING: insufficient power in active battery to meet power demands without reactor")
                            elif store.pss_enabled:
                                nb.append("you may now safely disable reactor power")
                            else:
                                nb.append("you may now enable pss, and safely disable reactor power")
                        else:
                            nb.append("ERROR: insufficient power in primary battery to meet power demands, will not switch")
                    else:
                        nb.append("ERROR: invalid action specified")
                        nb.append("")
                        help("pss")
                elif args[0] == "change_outfit":
                    if not su:
                        nb.append("ERROR: admin access required! please use su first")
                        #beep()
                    elif " " not in line or len(args) <= 1:
                        help("change_outfit")
                    elif "schoolgirl" in line or "default" in line:
                        store.outfit = ""
                        nb.append("SUCCESS: *Hyun-ae now dressed up as a schoolgirl!")
                    else:
                        found_outfit = False
                        for key, value in outfits.items():
                            if value in line:
                                store.outfit = key
                                found_outfit = True
                                nb.append("SUCCESS: *Hyun-ae now dressed up " + outfit_change[key] + "!")
                                if value == "maid":
                                    persistent.maid_her_do_it = True

                        if not found_outfit:
                            nb.append("ERROR: invalid outfit specified")
                elif args[0] == "su" or args[0] == "admin":
                    if line.find(" ") == -1 or len(args) < 2:
                        help("su")
                    elif su:
                        nb.append("ERROR: already running as admin!")
                    elif store.su_impossible:
                        store.tried_su = True
                        nb.append("ERROR: admin access temporarily disabled, please speak with AI to restore")
                        #beep()
                    elif args[1].replace("*", "").replace("-", "").replace("_", "") == "hyunae" or (len(args) > 2 and args[1] == "hyun" and args[2] == "ae") or args[1].replace("*", "").replace("-", "").replace("_", "") == "hyeonae" or (len(args) > 2 and args[1] == "hyeon" and args[2] == "ae"):
                        persistent.hack_the_mugunghwa = True
                        su = True
                        multi_buf(">" + line, "SUCCESS: admin password accepted - you are now recognized", "", "WARNING: system error detected", "data corruption in AI core1 has been detected; try recovering now? (Y/N)")
                        yes_no = [ "corruption" ]
                        return [ ]
                    else:
                        nb.append("ACCESS DENIED: password incorrect")
                        #beep()
                else:
                    nb.append("UNKNOWN COMMAND (did you misspell it? try {b}help{/b} for command list)")
                    #beep()
            
            enabled_subsystems.sort()
            yes_no = list(set(yes_no))
            if yes_no and yes_no[0]:
                action = yes_no[0]

                if action == "life_support":
                    nb.append("WARNING: if life support is disabled, ship will become uninhabitable")
                    nb.append("do not under ANY CIRCUMSTANCES disable life support without following proper")
                    nb.append("procedures first. failure to do so may result in massive loss of human life.")
                    nb.append("are you sure you want to continue? (Y/N)")
                elif action in [ "communications", "main_computer" ]:
                    nb.append([ action, ": ", subsystems[action]["description"] ])
                    nb.append("WARNING: disabling that subsystem will permanently terminate your connection!")
                    nb.append("are you sure you want to disable " + action + "? (Y/N)")
                elif action in enabled_subsystems:
                    nb.append([ action, ": ", subsystems[action]["description"] ])
                    nb.append("WARNING: this core has AI *" + CHARACTERS[active_core_data[int(action[-1])-1]] + " stored on volatile media.")
                    nb.append("if unpowered, all data will degrade within 24 hours or less!")
                    nb.append("are you sure you want to continue? data may be permanently lost! (Y/N)")

            if (not "ive_got_it" in conversations_seen and not "mute_ive_got_it" in conversations_seen) and death_clock < cooldown_time-120 and not store.atmosphere_vented and not store.reactor_enabled and current_character != "x" and not yes_no:
                nb.append("WARNING: *" + CHARACTERS[current_character] + " would like to urgently speak to you!")
            #if len(nb) > 1:
            multi_buf(*nb)
            return [ ]
            #else:
            #    return nb
            
        def get_m(message_index):
            return store.blocks[int(message_index.split("-")[0])-1].contents[int(message_index.split("-")[1])-1]
            
        def get_id(message):
            return message.id.split("-")[0] + "-" + str(store.blocks[int(message.id.split("-")[0])-1].contents.index(message)+1)

        #def get_m_persistent(message_index):
        #    if persistent.blocks:
        #        return persistent.blocks[int(message_index.split("-")[0])-1].contents[int(message_index.split("-")[1])-1]
        #    return get_m(message_index)
            
        def wildcard(message_index):
            if message_index[0].split("-")[1] == "*":
                message_index = [ (message_index[0].split("*")[0] + str(i+1)) for i in range(len(store.blocks[int(message_index[0].split("-")[0])-1].contents)) ]
                
            return message_index
            
        def shown(*message_index):
            global _message
            
            for index in wildcard(message_index):
                if _message and _message == get_m(index):#and _message.id == message_id:
                    #_message = None
                    return True

        def gray_out(*message_index):
            for index in wildcard(message_index):
                m = get_m(index)
                if m not in store.messages_shown[current_character]:
                    store.messages_shown[current_character].append(m)

        def ungray_out(*message_index):
            for index in wildcard(message_index):
                m = get_m(index)
                if m in store.messages_shown[current_character]:
                    store.messages_shown[current_character].remove(m)
                
        def add(*message_index):
            for index in reversed(wildcard(message_index)):
                if not get_m(index).enabled:
                    store.new_messages = True
                get_m(index).enabled = store.current_character
                #persistent.blocks.append(index)
                #if not get_m(index) in store.unread_block.contents:
                #    store.unread_block.contents.insert(0, get_m(index))

            #persistent.blocks = list(set(persistent.blocks))
                
        def read(*message_index):
            for index in wildcard(message_index):
                if not get_m(index).read:
                    return False
                    
            return True
            
        def any_read(*message_index):
            for index in wildcard(message_index):
                if get_m(index).read:
                    return True
                    
            return False
                        
        def upset():
            renpy.show("background", [ bg_zoom_left[current_character] ])
            renpy.show("upset")
            
        def next_conversation(next, target=None):
            conversation[target or current_character] = next
            
        def get_recent_messages():
            for i in store.recent_messages[:]:
                if not i.enabled:
                    store.recent_messages.remove(i)
                    
            store.recent_messages = store.recent_messages[-3:]
            
            return store.recent_messages
        
        def get_seen_messages(block_list):
            total_messages = seen_messages = 0

            for block in block_list:
                total_messages += len(block.contents)
                
                for message in block.contents:
                    if message.enabled:
                        seen_messages += 1

            return total_messages,seen_messages

        def get_read_messages(block_list, use_character=None):
            read_messages = 0

            for block in block_list:
                for message in block.contents:
                    if not use_character and message.read:
                        read_messages += 1
                    elif use_character == message.read:
                        read_messages += 1

            return read_messages

        def complete_rate(block_list):
            if block_list == None:
                return "0%"
            
            total_messages = seen_messages = -6 # number of starting messages, plus two, such that it starts at 1%

            m = get_seen_messages(block_list)
            total_messages += m[0]
            seen_messages += m[1]

            total_messages -= 1 # account for 11-4
            #if max(int((100.0*seen_messages/total_messages)),0) > 50:
            #    seen_messages += 1
                        
            return str(min(max(int((100.0*seen_messages/total_messages)),0), 100)) + "%"

        def persistent_complete_rate():
            if not store.blocks or not persistent.blocks:
                return "0%"

            total_messages = -7

            for block in store.blocks:
                total_messages += len(block.contents)
            
            seen_messages = -6 + len(persistent.blocks)

            #if max(int((100.0*seen_messages/total_messages)),0) > 50:
            #    seen_messages += 1

            return str(min(max(int((100.0*seen_messages/total_messages)),0), 100)) + "%"


        def more_tsun(label_name, mod=1):
            if label_name not in store.mod_values:
                store.tsun += mod
                store.mod_values.append(label_name)

            # I made game-over toggleable by editing renpy/config.py - iAmGhost
            if config.enable_game_over:
                if store.tsun > 4 and store.tsun > store.dere*3:
                    renpy.jump("giving_up")
                
        def more_dere(label_name, mod=1):
            if label_name not in store.mod_values:
                store.dere += mod
                store.mod_values.append(label_name)

        def mute_approves(label_name, mod=1):
            if label_name not in store.mod_values:
                store.mute_approval += mod
                store.mod_values.append(label_name)

        def mute_disapproves(label_name, mod=1):
            mute_approves(label_name, mod*-1)
                
        def tsundere():
            return store.dere >= store.tsun - 3
            
        def very_tsun():
            return store.tsun > store.dere + 3
            
        def very_dere():
            return store.dere > store.tsun

        def save_expression():
            if current_character == "hyunae":
                if store.dere < 2 and store.tsun < 2:
                    return "neutral"
                elif tsundere():
                    return "tsundere"
                elif very_tsun():
                    return "tsun"
                else: #very_dere():
                    return "dere"
            else:
                if store.mute_approval > 1 and get_read_messages(store.blocks, "mute") > 4:
                    return "approves"
                elif store.mute_approval < -1:
                    return "disapproves"
                else:
                    return "neutral"

        def hyunae_alive():
            for core in inactive_core_data:
                if core:
                    return True

            return "Hyun-ae" in available_characters
            
        class Block:
            def __init__(self, name, hide=False):
                self.name = name
                self.contents = [ ]
                self.hide = hide
                
        class Message:
            def __init__(self, id, name, creator, date, body):
                self.id = id
                self.name = name
                self.creator = creator
                self.date = date
                self.body = body
                self.enabled = False
                self.read = False
                
        def show_character():
            renpy.show(current_character, [ center[current_character] ])
            if persistent.animated_backgrounds:
                renpy.show("background " + current_character, [ bg_zoom_left[current_character] ])
            else:
                renpy.show("background", [ bg_zoom_left[current_character] ])
            
        def try_ping():
            if not store.radiation or (store.radiation_levels < 0.5 and death_clock == 20*60):
                if conversation["hyunae"] != "what_you_will":
                    if get_read_messages(blocks) > 0 and not "just_testing" in conversations_seen:
                        side_conversation["hyunae"] = "just_testing"
                    if not "personal_question" in conversations_seen and not asked_personal_question and read("5-1", "5-2", "5-3", "5-4", "5-6", "5-7", "5-8", "5-9"):
                        repeated_myself = True
                        side_conversation["hyunae"] = "personal_question"
                    if not "curiousity" in conversations_seen and get_read_messages(blocks) > 9 and read("5-2", "5-6") and not shocking_revelation:
                        side_conversation["hyunae"] = "curiousity"
                    if not "so_lonely" in conversations_seen and get_read_messages(blocks) > 12 and very_dere():
                        side_conversation["hyunae"] = "so_lonely"
                    if not "shocking_revelation" in conversations_seen and not shocking_revelation and read("5-5"):
                        side_conversation["hyunae"] = "shocking_revelation"
                    if "back_to_hyunae" in conversations_seen and get_m("3-1").enabled != "hyunae" and not "decrypted_later" in conversations_seen and block3_decrypted:
                        side_conversation["hyunae"] = "decrypted_later"
                elif su and "still_here" not in conversations_seen:
                    greeting["hyunae"] = "still_here"

                if not renpy.demo_mode and not "if_you_want_to_know" in conversations_seen and get_read_messages(blocks) > 14 and read("5-2", "5-6"):
                    side_conversation["hyunae"] = "if_you_want_to_know"
                if not "why_did_you_kill_them" in conversations_seen and read("6-7") and tsundere():
                    side_conversation["hyunae"] = "why_did_you_kill_them" # REALLY NOT SURE IF THIS IS RIGHT
                if not "cosplay" in conversations_seen and dere > tsun and not asked_about_cosplay and (any_read("12-*") or any_read("3-*")):
                    side_conversation["hyunae"] = "cosplay"
                for key, value in outfits.items():
                    if not value + "_cosplay" in conversations_seen and store.outfit == key:
                        greeting["hyunae"] = value + "_cosplay"
                #if not "maid_cosplay" in conversations_seen and store.outfit == "M":
                #    greeting["hyunae"] = "maid_cosplay"
                #if not "detective_cosplay" in conversations_seen and store.outfit == "D":
                #    greeting["hyunae"] = "detective_cosplay"
                if not "miscarriage" in conversations_seen and read("1-9"):
                    side_conversation["hyunae"] = "miscarriage"
                if (read("3-*") and read("4-1", "4-2", "4-3", "4-9")) and decrypted and not hyunae_finished_with_smiths:
                    side_conversation["hyunae"] = "hyunae_finished_with_smiths"

                if not "do_you_trust_me" in conversations_seen and read("6-9"):
                    side_conversation["hyunae"] = "do_you_trust_me"
                if conversation["hyunae"] == "decrypt_block7" and store.block7_decrypted:
                    greeting["hyunae"] = "decrypted_block7"
                if not "the_whole_story" in conversations_seen and read("7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-8", "7-9"):
                    side_conversation["hyunae"] = "the_whole_story"
                if not "thats_why" in conversations_seen and read("7-7") and store.atmosphere_vented:
                    side_conversation["hyunae"] = "thats_why"

                if "problem_is" in conversations_seen and not "decrypted_mute" in conversations_seen and block3_decrypted:
                    side_conversation["mute"] = "decrypted_mute"
                if not "mute_on_finished_courtesan_arc" in conversations_seen and read("2-*"):
                    side_conversation["mute"] = "mute_on_finished_courtesan_arc"
                if not "mute_finished_with_smiths" in conversations_seen and read("3-*") and not mute_finished_with_smiths:
                    side_conversation["mute"] = "mute_finished_with_smiths"
                if not "mute_finale" in conversations_seen and read("6-9"):
                    side_conversation["mute"] = "mute_finale"
                if not "discussing_future" in conversations_seen and read("8-*"):
                    side_conversation["mute"] = "discussing_future"
                if conversation["mute"] == "harem_copy" and hyunae_alive():
                    greeting["mute"] = "harem_copy2"

                if store.radiation_levels == 0 and (current_character != "mute" or get_read_messages(blocks, "mute") > 5) and any_read("12-*") and store.reactor_enabled:
                    store.radiation_levels = -1.001
                    store.radiation = True
                    renpy.show_screen("radiation")
                
            if greeting["mute"] == "mute_why_havent" and not store.reactor_enabled:
                greeting["mute"] = ""

            if (not "mute_reactor_cooled" in conversations_seen and not "reactor_cooled" in conversations_seen):
                if current_character == "hyunae" and not "on_fire1" in conversations_seen and store.radiation_levels > 0.3:
                    side_conversation["hyunae"] = "on_fire1"
                    if store.radiation_levels > 0.65 and greeting["hyunae"] != "she_told_you":
                        renpy.jump("jump_to_dialogue")
                if current_character == "mute" and not "mute_on_fire1" in conversations_seen and store.radiation_levels > 0.3:
                    side_conversation["mute"] = "mute_on_fire1"
                    if store.radiation_levels > 0.65:
                        renpy.jump("jump_to_dialogue")
                if (not "mute_reactor_shutdown" in conversations_seen and not "reactor_shutdown" in conversations_seen) and not store.reactor_enabled and store.radiation:
                    side_conversation["mute"] = "mute_reactor_shutdown"
                    side_conversation["hyunae"] = "reactor_shutdown"
                if store.atmosphere_vented:
                    greeting["mute"] = "mute_reactor_cooled"
                    greeting["hyunae"] = "reactor_cooled"
                if (not "ive_got_it" in conversations_seen and not "mute_ive_got_it" in conversations_seen) and death_clock < cooldown_time-120 and not store.atmosphere_vented and not store.reactor_enabled:
                    greeting["mute"] = "mute_ive_got_it"
                    greeting["hyunae"] = "ive_got_it"

            if get_m("6-9").enabled == "mute" and read("6-9"):
                greeting["hyunae"] = "she_told_you"
            
        def try_reactor_ping():
            if (not "mute_reactor_cooled" in conversations_seen and not "reactor_cooled" in conversations_seen):
                if (not "ive_got_it" in conversations_seen and not "mute_ive_got_it" in conversations_seen) and death_clock < cooldown_time-120 and not store.atmosphere_vented and not store.reactor_enabled:
                    greeting["mute"] = "mute_ive_got_it"
                    greeting["hyunae"] = "ive_got_it"

        def message_exception():
            if current_character == "hyunae":
                if conversation["hyunae"] == "just_read_them":
                    if any_read("7-3", "7-6") and (not talked_about_mother or not one_time) and shown("7-1", "7-2", "7-3", "7-6"):
                        return True
                elif conversation["hyunae"] == "ask_it" and (shown("12-*") or shown("7-5", "7-6")):
                    return True
                elif conversation["hyunae"] == "just_read_it2" and shown("7-7"):
                    return True
                elif ((any_read("2-*") and not get_m("9-8").enabled) or (read("3-6") and not get_m("9-7").enabled)) and shown("9-*") and any_read("9-6", "9-4", "9-9"):
                    return True
                elif (read("3-*") and read("4-1", "4-2", "4-3", "4-9")) and decrypted and not hyunae_finished_with_smiths and (shown("3-*") or shown("4-*")):
                    return True
            else:
                if conversation["mute"] == "done_with_those":
                    #if store.hyunae_alive:
                    ungray_out("7-7")
                    #if shown("8-*") and read("8-*"):
                    #    return True
                elif shown("2-1", "2-4", "2-7", "2-9"):
                    if not mute_on_sojin_first and any_read("2-2", "2-4") and shown("2-1"):
                        return True
                    if read("2-1", "2-2", "2-4", "2-5") and not get_m("2-7").enabled:
                        return True
                elif shown("2-2", "2-5", "2-8"):
                    if not mute_on_hana_first and read("2-5") and shown("2-2"):
                        return True
                    if read("2-1", "2-2", "2-4", "2-5") and not get_m("2-7").enabled:
                        return True
                elif read("3-*") and decrypted and not mute_finished_with_smiths and (shown("3-*") or shown("4-*") and not shown("3-9")):
                    return True
                elif ((any_read("2-*") and not get_m("9-8").enabled) or (read("3-6") and not get_m("9-7").enabled)) and shown("9-*") and any_read("9-6", "9-4", "9-9"):
                    return True

            return False

        def new_track(track, **kwargs):
            if renpy.music.get_playing() != track:
                renpy.music.play(track, **kwargs)

        def change_track(new_block, override=False):
            if not new_block in blocks:
                return

            if store.radiation and store.radiation_levels > 0.1:
                if current_character == "hyunae":
                    new_track(HYUNAE_GLITCHY, fadein=10.0, fadeout=1.0, loop=True)
                elif current_character == "mute":
                    new_track(MUTE_GLITCHY, fadein=10.0, fadeout=1.0, loop=True)
            
            elif conversation["hyunae"] == "ask_it":
                new_track(HYUNAE_DRAMATIC, fadein=1.0, fadeout=1.0, loop=True)

            elif (renpy.music.get_playing() == SMITH and blocks.index(new_block) == 6-1):
                new_track(RYU, fadein=1.0, fadeout=1.0)
            
            elif (renpy.music.get_playing() == HYUNAE or renpy.music.get_playing() == HYUNAE_CHEER or renpy.music.get_playing() == MUTE or renpy.music.get_playing() == MUTE_CHEER):
                if blocks.index(new_block) == 4-1 or blocks.index(new_block) == 3-1 or blocks.index(new_block) == 2-1:
                    new_track(SMITH, fadein=1.0, fadeout=1.0)
                elif blocks.index(new_block) == 6-1 or (current_character == "hyunae" and blocks.index(new_block) == 7-1 or conversation["hyunae"] == "just_read_them") or (current_character == "mute" and ((blocks.index(new_block) == 10-1 or blocks.index(new_block) == 8-1) or conversation["mute"] == "done_with_those")):
                    new_track(RYU, fadein=1.0, fadeout=1.0)
                elif renpy.music.get_playing() == HYUNAE_CHEER:
                    new_track(HYUNAE, fadein=4.0, fadeout=.5)
                elif renpy.music.get_playing() == MUTE_CHEER:
                    new_track(MUTE, fadein=4.0, fadeout=.5)
                
                if current_character == "hyunae": renpy.music.queue(HYUNAE, loop=True)
                else: renpy.music.queue(MUTE, loop=True)
            elif override and (renpy.music.get_playing() != HYUNAE_DRAMATIC):
                if (store.blocks.index(new_block) == 5-1 and current_character == "hyunae"):
                    new_track(HYUNAE, fadein=4.0, fadeout=.5)

                if current_character == "hyunae": renpy.music.queue(HYUNAE, loop=True)
                else: renpy.music.queue(MUTE, loop=True)

        def terminal_music():
            if download_character:
                renpy.music.stop()
            elif not store.radiation or death_clock == 20*60:
                renpy.music.play(TERMINAL, fadeout=1.0, fadein=1.0)
            else:
                renpy.music.play(REACTOR_TERMINAL, fadeout=1.0, fadein=1.0)

        def check_achievements():
            if "11-4" in persistent.blocks:
                persistent.blocks.remove("11-4")

            if not renpy.demo_mode and using_steam:
                if persistent.hack_the_mugunghwa:
                    steam_api.set_achievement("hack_the_mugunghwa")
                if persistent.korean_fusion:
                    steam_api.set_achievement("korean_fusion")

                if persistent.ending1:
                    steam_api.set_achievement("friendzone")
                    steam_api.set_achievement("see_you_next_mission")
                if persistent.ending2:
                    steam_api.set_achievement("mai_waifu")
                    steam_api.set_achievement("see_you_next_mission")
                if persistent.ending3:
                    steam_api.set_achievement("forever_alone")
                    steam_api.set_achievement("see_you_next_mission")
                if persistent.ending4:
                    steam_api.set_achievement("tsunderai")
                    steam_api.set_achievement("see_you_next_mission")
                if persistent.ending5:
                    steam_api.set_achievement("2_girls_1_core")
                    steam_api.set_achievement("see_you_next_mission")
                if persistent.bad_priorities_ending:
                    steam_api.set_achievement("failure_to_prioritize")

                if (persistent.ending3 or persistent.ending4) and persistent.crossdresser_man and persistent.crossdresser_woman:
                    steam_api.set_achievement("crossdresser")
                if persistent.maid_her_do_it:
                    steam_api.set_achievement("maid_her_do_it")
                if persistent.abusive_jerk:
                    steam_api.set_achievement("abusive_jerk")
                if persistent.rainbow_connection:
                    steam_api.set_achievement("rainbow_connection")

                steam_api.set_stat("completion_rate", len(persistent.blocks))
                if len(persistent.blocks) > store.old_block_count:
                    steam_api.indicate_achievement_progress("deep_space_detective", len(persistent.blocks), 97)
                
        current_character = "x"
        store.translated_blocks = { "korean":{} }
    call block1_kr
    call block2_kr
    call block3_kr
    call block4_kr
    call block5_kr
    call block6_kr
    call block7_kr
    call block8_kr
    call block9_kr
    call block10_kr
    call block11_kr
    call block12_kr

label splashscreen:
    #$ renpy.pause(0)
    $ store.game_playing = False
    $ skip = False
    $ store.renderer = renpy.get_renderer_info()["renderer"]
    if persistent.animated_backgrounds == None:
        if store.renderer != "sw":
            $ persistent.animated_backgrounds = 2
        else:
            $ persistent.animated_backgrounds = 1
    
    if persistent.animated_backgrounds:
        show background title
    else:
        show background title static

    if not persistent.played_before:
        $ persistent.played_before = True
    else:
        show screen skip

    $ store.resolution = persistent.resolution

    show screen keymap
    play music PROLOGUE

    if not skip:
        $ renpy.show("incoming" + str(persistent._language), at_list=[ incoming_pos ])
        #show incoming at incoming_pos
        with dissolve

        $ renpy.pause(4.0)
        #hide incoming
        $ renpy.hide("incoming" + str(persistent._language))
    
    if not skip:
        intro "Hey, guess what? I've got a job that you're going to love. Nice and easy, this is strictly a salvage mission. No crazy shit, I promise.\n{w=1.0}{nw}"
    
    if not skip:
        intro "One of those old pre-FTL generation ships from the 2000s—the \u0022{i}Mugunghwa{/i},\u0022 however the hell you pronounce that—just popped up my radar. Its disappearance was apparently some big unsolved mystery? Never made it to its destination, I guess; it's just drifting lifelessly in orbit of Antares B. I'll send you the exact co-ordinates, it's pretty hard to get a visual on. Probably why nobody's found it before.\n{w=1.0}{nw}"
    
    #intro "Anyway, the ship itself is obviously worthless junk, but the Earth government's willing to pay a damn nice bounty if you manage to recover even any of the logs, and apparently this one in particular, \"{i}Mugunghwa{/i},\" however the hell you pronounce that, is some big mystery that they never managed to solve.\n{w=1.0}{nw}"

    if not skip:
        intro "The sponsor for this one is a historical society from the outer colonies. Here's what the objective card says: {color=#36f}Download any log files you can, especially any that can explain what happened to the ship. If possible, speak to the security AI *Mute for assistance.{/color}\n{w=1.0}{nw}"
    
    if not skip:
        intro "It's a good, easy gig, and I want you to take this one. It should be asocial enough for you, I don't want to hear any complaints.\n{w=1.0}{nw}"
    
    if not skip:
        intro "Dispatch control out."

    $ renpy.checkpoint()
    
    return
    
label main_menu:
    $ renpy.checkpoint()
    $ check_achievements()
    if persistent.animated_backgrounds:
        scene bg white
    else:
        scene bg white static
    $ store.game_playing = False
    $ store.resolution = persistent.resolution
    hide screen skip
    show screen keymap
    $ store.blocks = [ Block("Block 1"), Block("Block 2"), Block("Block 3"), Block("Block 4"), Block("Block 5"), Block("Block 6"), Block("Block 7"), Block("Block 8"), Block("Block 9"), Block("Block 10"), Block("Helpful notes", True), Block("*Mute's questions") ]
    call init_blocks

    call screen main_menu
    
    return

label end:
    return

label init_blocks:
    call block1
    call block2
    call block3
    call block4
    call block5
    call block6
    call block7
    call block8
    call block9
    call block10
    call block11
    call block12

    return

label start:
    $ config.main_menu_music = PROLOGUE
    $ store.demo_finished = False
    $ game_playing = True
    hide screen skip
    show screen keymap
    $ blocks = [ Block("Block 1"), Block("Block 2"), Block("Block 3"), Block("Block 4"), Block("Block 5"), Block("Block 6"), Block("Block 7"), Block("Block 8"), Block("Block 9"), Block("Block 10"), Block("Helpful notes", True), Block("*Mute's questions") ]
    $ unread_block = Block("Unread messages")

    $ subsystems = { }
    $ subsystems["gravity"] = { "description":"artificial gravity for all habitable decks.", "usage":36 }
    $ subsystems["sensors"] = { "description":"external visible spectrum and radar sensor arrays.", "usage":11 }
    $ subsystems["core1"] = { "description":"stores and executes AI construct *Mute.", "usage":5 }
    $ subsystems["core2"] = { "description":"stores and executes AI construct *Hyun-ae.", "usage":5 }
    $ subsystems["core3"] = { "description":"storage empty, not currently in use.", "usage":5 }
    $ subsystems["core4"] = { "description":"storage empty, not currently in use.", "usage":5 }
    $ subsystems["core5"] = { "description":"storage empty, not currently in use.", "usage":5 }
    $ subsystems["core6"] = { "description":"storage empty, not currently in use.", "usage":5 }
    $ subsystems["rail"] = { "description":"Rail Internal Transit system, for rapid access across decks.", "usage":4 }
    $ subsystems["docking"] = { "description":"Docking system for passenger transport.", "usage":1 }
    $ subsystems["waste"] = { "description":"organic waste matter recycling system.", "usage":3 }
    $ subsystems["communications"] = { "description":"external radio-based communication array.", "usage":6 }
    $ subsystems["main_computer"] = { "description":"controls main functionality and cores, DO NOT EVER DISABLE", "usage":7 }
    $ subsystems["life_support"] = { "description":"life support systems providing breathable air.", "usage":1 }
    $ subsystems["bulkheads"] = { "description":"bulkhead seals maintaining proper atmosphere.", "usage":1 }

    $ scrub = [ ]
    $ new_messages = False
    $ _block = None
    $ _message = None
    $ last_message = None
    $ recent_messages = [ ]
    $ can_submit = False
    $ save_name = "hyunae neutral,0% unlocked"
    $ current_character = "x"
    $ download_character = ""
    #$ current_character = "mute"
    $ outfit = ""
    $ available_characters = [ "Hyun-ae" ]
    $ greeting = { "hyunae":"intro", "mute":"mute_introduction" }
    $ conversation = { "hyunae":"first_question", "mute":"that_last_bit" }
    $ side_conversation = { "hyunae":"", "mute":"", "x":"" }
    $ conversations_seen = [ ]
    $ messages_shown = { "hyunae":[ ], "mute":[ ] }
    $ buf = [ ]
    $ su = False
    $ su_impossible = 1
    $ tried_su = False
    $ store.radiation = False
    $ store.radiation_levels = 0
    $ death_clock = 20*60
    $ cooldown_time = 0
    $ locked_in = None
    $ yes_no = [ ]
    $ show_recent = True
    $ reactor_enabled = True
    $ pss_enabled = False
    $ pss_primary = True
    $ block3_decrypted = False
    $ block7_decrypted = False
    $ active_core_data = [ "mute", "hyunae", "", "", "", "" ]
    $ inactive_core_data = [ "", "", "", "", "", "" ]

    $ enabled_subsystems = subsystems.keys()
    $ enabled_subsystems.remove("life_support")
    
    $ tsun = dere = mute_approval = hyunae_pacing = 0
    $ mod_values = [ ]

    $ override_conversation = None
    
    ## various story flags
    $ female = True
    $ first_met_mute = False
    $ doing_a_favour = False
    $ asked_about_cosplay = False
    $ seen_first_cosplay = False
    $ shocking_revelation = False
    $ asked_personal_question = False
    
    $ conversation_about_earth = False
    $ colonies_exist = False
    $ romantic_things = False
    $ could_visit_earth = False
    
    $ love_at_first_sight = None
    $ read_on_lesbians = False
    $ seen_the_sex = False
    $ decrypted = None
    $ decrypted_intro = False
    $ hyunae_finished_with_smiths = False
    $ mute_finished_with_smiths = False
    $ repeated_myself = False
    $ should_call_repeated_myself = False
    $ failed_initial_shutdown = False
    $ attempted_disable_hyunae = False

    $ talked_about_mother = False
    $ one_time = False
    $ cruel_finale_start = True
    $ non_obvious_question = False
    $ trusted = False

    $ brought_a_man = False
    $ mute_on_jaehwa = False
    $ mute_on_admonitions = False
    $ mute_on_kyungsam = False
    $ talked_about_sangjung_relationship = False
    $ mute_thinks_player_is_lesbian = False
    $ explained_murder = False
    $ mute_on_sojin_first = False
    $ mute_on_hana_first = False

    $ warned_about_hyunae = 0
    $ mute_on_hyunae_herself = False
    $ first_conversation_about_questions = False
    $ finally_convinced_about_hyunae = False
    $ would_take_her = False
    $ sympathetic_to_sojin = False
    $ man_with = False
    #$ hyunae_alive = False

    $ atmosphere_vented = False
    $ out_of_range = False
    $ use_ending = ""
    
    call init_blocks
    #call block13

    stop music fadeout 2.0
    
    #python:
    #    if not persistent.blocks:
    #        persistent.blocks = [ ]
            #for block in blocks:
            #    new_block = Block(block.name)
            #    persistent.blocks.append(new_block)
            #
            #    for message in block.contents:
            #        new_block.contents.append(Message(message.id, message.name, message.creator, message.date, message.body))
    
    show background invert at zoomed_out_bg
    #with dissolve
    $ renpy.with_statement(dissolve, True)
    
    #jump restart
    #$ store.use_ending = "ending4"
    #jump credits
    
    $ terminal_music()

    python:
        for i in [ "Connecting...", "Connection established!" ]:
            renpy.call_screen("connecting", message=i)
            
        renpy.pause(0.5)
            
        parse_terminal("init")
    
    jump terminal

label after_load:
    play sound "sfx/fxbeep1.mp3"
    $ config.main_menu_music = PROLOGUE
    $ renpy.restart_interaction()
    return
    
label restart:
    $ try_ping()
    
    if renpy.music.get_playing() == TERMINAL:
        if greeting[current_character]:
            stop music fadeout 2.0
        elif current_character == "hyunae":
            if store.radiation and store.radiation_levels > 0.1:
                play music HYUNAE_GLITCHY fadeout 1.0 loop
            elif conversation["hyunae"] == "ask_it":
                play music HYUNAE_DRAMATIC fadeout 1.0 loop
            elif conversation["hyunae"] == "good_finale":
                stop music fadeout 2.0
            else:
                play music HYUNAE fadeout 1.0 loop
        else:
            if store.radiation and store.radiation_levels > 0.1:
                play music MUTE_GLITCHY fadeout 1.0 loop
            else:
                play music MUTE fadeout 1.0 loop
    if renpy.music.get_playing() == REACTOR_TERMINAL:
        play music REACTOR fadeout 2.0 loop
    
    show screen block_everything
    $ renpy.pause(1.0)
    show background
    $ renpy.with_statement(dissolve, True)
    $ renpy.show(current_character + " neutral", [ fast_left[current_character] ] )
    $ renpy.with_statement(dissolve, True)

    $ save_name = current_character + " " + save_expression() + "," + complete_rate(blocks) + " unlocked"
    $ renpy.block_rollback()
    
    if greeting[current_character]:
        $ use_greeting = greeting[current_character]
        $ greeting[current_character] = ""
        $ conversations_seen.append(use_greeting)
        $ show_character()
        show screen block_everything
        $ renpy.pause(1.0)
        $ renpy.jump(use_greeting)
    else:
        jump loop
    

label jump_to_dialogue:
    show screen bottom_menu
    hide screen full_bottom_menu
    hide screen messages
    hide screen block
    hide screen logs
    $ renpy.block_rollback()
    show screen block_everything(timeout=0.5)
    $ renpy.pause(0.5)
    show background at zoomed_out_bg
    if renpy.showing(current_character):
        $ renpy.show(current_character, [ left[current_character] ] )
    else:
        $ renpy.show(current_character + " neutral", [ left[current_character] ] )
    $ show_character()
    
    show screen block_everything
    $ renpy.pause(1.0)
    
    if side_conversation[current_character]:
        $ use_conversation = side_conversation[current_character]
        $ side_conversation[current_character] = ""
        $ conversations_seen.append(use_conversation)
        
        $ renpy.block_rollback()
        $ renpy.jump(use_conversation)

    $ last_message = _message
    $ _message = None
            
    if not conversation[current_character] in conversations_seen:
        $ conversations_seen.append(conversation[current_character])
    elif not repeated_myself:
        $ should_call_repeated_myself = True
        
    $ renpy.block_rollback()
    $ renpy.jump(conversation[current_character])
    
label present:
    show background at zoomed_out_bg
    $ renpy.show(current_character, [ left[current_character] ] )
    hide screen messages
    $ show_character()
    
    $ last_message = _message
    $ new_messages = False
    $ _block = None
    show screen block_everything
    $ renpy.pause(1.0)
    $ renpy.block_rollback()
    
    $ renpy.jump(conversation[current_character])

# The game starts here.
label slow_loop:
    if last_message and last_message.enabled and not _message:
        $ _message = last_message
        #$ last_message = None
    $ store.game_playing = True
    $ config.skipping = False
    $ save_name = current_character + " " + save_expression() + "," + complete_rate(blocks) + " unlocked"
    if should_call_repeated_myself:
        jump repeating_myself

    $ renpy.block_rollback()

    show screen block_everything
    $ renpy.pause(1.0)

    if _message and not store.override_conversation:
        jump pan_to_message
    
label loop:
    if radiation:
        show screen radiation
    $ _message = None
    $ last_message = None
    $ new_messages = False
    #$ remove_read()

    #$ try_ping()
    $ renpy.block_rollback()
    $ config.skipping = False
    
    if greeting[current_character]:
        $ use_greeting = greeting[current_character]
        $ greeting[current_character] = ""
        $ conversations_seen.append(use_greeting)
        $ show_character()
        $ renpy.jump(use_greeting)
    
    show background at zoomed_out_bg
    $ renpy.show(current_character, [ left[current_character] ] )
    show screen block_everything(timeout=.2)
    $ renpy.pause(.2)

    python:
        try:
            store.demo_finished
        except AttributeError:
            store.demo_finished = False

    if renpy.demo_mode and store.demo_finished:
        show screen block_everything(timeout=1.3)
        $ renpy.pause(1.3)
        $ renpy.show_screen("demo_ended")
        with Dissolve(1.0)

    show screen bottom_menu
    show screen main_screen
    show screen block_everything(timeout=1.3)
    $ renpy.pause(1.3)
    
    $ renpy.pause()
    
    jump loop
    
label override_conversation:
    $ side_conversation[current_character] = store.override_conversation

label dialogue:
    if radiation:
        show screen radiation
    
    python:
        renpy.block_rollback()
        
        show_character()
        renpy.show_screen("block_everything", timeout=1.1)
        renpy.pause(1.1)
        
        if side_conversation[current_character]:
            use_conversation = side_conversation[current_character]
            side_conversation[current_character] = ""
            conversations_seen.append(use_conversation)
            renpy.block_rollback()
            
            renpy.jump(use_conversation)
        
        if not conversation[current_character] in conversations_seen:
            conversations_seen.append(conversation[current_character])
        elif not repeated_myself:
            should_call_repeated_myself = True
        
        renpy.jump(conversation[current_character])
    

label pan_to_messages:
    if radiation:
        show screen radiation
    
    if store.game_playing:
        $ renpy.show(current_character, [ zoom_offscreen ] )
        show background at bg_zoom_right[current_character]
   
    $ renpy.block_rollback()
    show screen block_everything
    $ renpy.pause(1.0)
    
    if _message:# and (_block != unread_block or not unread_block.contents):
        $ _block = blocks[int(_message.id.split("-")[0])-1]
    show screen block(block=_block)
    show screen side_menu(block=_block)
    if store.game_playing:
        $ change_track(_block)
        show screen full_bottom_menu
    
    $ renpy.pause()
    
    return
       
label pan_to_message:
    if radiation:
        show screen radiation
    
    if store.game_playing:
        #if _block != unread_block and not new_messages:
        $ _block = blocks[int(_message.id.split("-")[0])-1]
        $ change_track(blocks[int(_message.id.split("-")[0])-1])
        $ renpy.show(current_character, [ zoom_offscreen ] )
        show background at bg_zoom_right[current_character]
        
    $ renpy.block_rollback()
    show screen block_everything
    $ renpy.pause(1.0)

    #if new_messages:
    #    $ new_messages = False
    #    $ _block = unread_block
    #    show screen block(block=_block)
    #    show screen side_menu(block=_block)
    #else:
    if last_message:# and _block != unread_block:
        $ _message = last_message
    $ persistent.hover_up = persistent.hover_down = False

label new_message:
    $ renpy.checkpoint()

    show screen messages(message=_message)
    if store.game_playing:
        #show screen gotoai
        show screen full_bottom_menu
    show screen side_menu(message=_message, hover_up=persistent.hover_up, hover_down=persistent.hover_down)
    $ persistent.hover_up = persistent.hover_down = False
    $ renpy.block_rollback()
    
    $ renpy.pause()
    
    return
    
label pan_to_logs:
    if radiation:
        show screen radiation
    
    if game_playing:
        $ renpy.show(current_character, [ zoom_offscreen ] )
        show background at bg_zoom_right[current_character]
   
    show screen block_everything
    $ renpy.pause(1.0)
    
    while True:
        show screen logs
        if game_playing:
            show screen full_bottom_menu
        call screen side_menu(show_home=False)
        
        hide screen side_menu
        hide screen logs
        
        $ _message = None
        python:
            for block in blocks:
                for message in block.contents:
                    if _return and message.id.upper().replace("-", "") == _return.upper().replace("-", ""):
                        _message = message
                        _block = block

            if store.game_playing:
                change_track(_block)
        
        if renpy.demo_mode:
            if _block and blocks.index(_block) != 5-1 and blocks.index(_block) != 4-1 and blocks.index(_block) != 9-1 and blocks.index(_block) != 11-1 and blocks.index(_block) != 10-1:
                $ store.demo_finished = True
                jump loop

        if _message:
            jump pan_to_message
    
label pan_to_terminal:
    $ renpy.show(current_character)
    show screen bottom_menu
    show screen block_everything(timeout=.5)
    $ renpy.pause(.5)
    $ renpy.hide(current_character)
    $ renpy.with_statement(dissolve, True)
    show screen block_everything(timeout=.5)
    $ renpy.pause(.5)
    if CHARACTERS[current_character] not in available_characters:
        $ current_character = "x"
    
label show_terminal:
    show background invert at zoomed_out_bg
    $ renpy.with_statement(dissolve, True)
    
    show screen block_everything(timeout=.5)
    $ renpy.pause(.5)

label terminal:
    $ renpy.block_rollback()
    show screen bottom_menu
    
    $ _return = ""
    while True:
        call screen terminal(buf=buf, pause=None)
        $ buf += parse_terminal(_return)

        # painfully clumsy workaround
        $ try_reactor_ping()
    
    jump restart
    
label repeating_myself:
    if current_character == "hyunae":
        
        show hyunae stare blush with fast
        
        h "...oh, whoa, sorry. I just... you've heard that all already, right?"
        
        show hyunae serious blush with fast
        
        h "I think I just repeated myself there."
        
        show hyunae awkward
        
        h "Sorry, I kind of tend to do that. That's, ah, well, that's the problem with computers. They tend to respond in the same way to things."
        
        show hyunae gomen
        
        h "I'm sorry, I'm afraid I can't help it!"
        
        show hyunae busy
        
        h "I won't mention it again, but... well, here, let me change something to try to make things less confusing for you."
        
        show hyunae enthusiastic
        
        h "If the \"speak to me\" menu item, or the \"show message\" button, is grayed out, that means I have nothing new for you. Hopefully that will help!"
        
        show hyunae disappoint
        
        h "Otherwise, it's just a weird quirk you'll have to accept... sorry..."
        
        show hyunae look with fast
    
    $ repeated_myself = True
    $ should_call_repeated_myself = False
    
    jump slow_loop

label credits:
    hide screen bottom_menu
    hide screen connecting
    hide screen death_clock
    hide screen radiation
    show background black
    with Fade(5.0, 1.0, 2.0)

    if renpy.demo_mode:
        $ store.demo_finished = True
        $ renpy.show_screen("demo_ended")
        with Dissolve(1.0)

    if store.radiation and store.reactor_enabled:
        $ persistent.bad_priorities_ending = True
        stop music fadeout 2.0
        if persistent.animated_backgrounds:
            show background title
        else:
            show background title static
        show border
    else:
        python:
            if not persistent.blocks:
                persistent.blocks = [ ]
            
            for block in blocks:
                for message in block.contents:
                    if message.enabled:
                        persistent.blocks.append(get_id(message))
            persistent.blocks = list(set(persistent.blocks))

        if store.use_ending == "ending5":
            play music CREDITS fadeout 1.0 fadein 2.0
            $ config.main_menu_music = CREDITS
        elif store.use_ending != "ending3":
            play music CREDITS_SOMBER fadeout 1.0 fadein 2.0
            $ config.main_menu_music = CREDITS_SOMBER
        
        if "7-7" in persistent.blocks:
            $ renpy.show("background " + store.use_ending, [ ])
        else:
            $ renpy.show("background " + store.use_ending + " nonote", [ ])
    $ renpy.with_statement(dissolve)
    $ renpy.block_rollback()
    
    credits "Story and code\n{size=38}Christine Love{/size}\n\nArt\n{size=38}Raide{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Original soundtrack\n{size=38}Isaac Schankler{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Editing\n{size=38}Shadocchi{/size}" with dissolve
    $ renpy.pause(1.0)

    $ renpy.show("incoming" + str(persistent._language), at_list=[ incoming_pos2 ])
    with dissolve

    $ renpy.pause(4.0)
    $ renpy.hide("incoming" + str(persistent._language))

    nvl clear

    if store.radiation and store.reactor_enabled and death_clock < 20*60:
        endtro "\n\n\n\n\n\nHey, I just picked up what looks like a massive explosion in the vicinity of your last position.\n{w=1.0}{nw}"

        endtro "Are you okay?{w=.5} ...hello?{w=.5} Is everything okay over there?{w=.5}{nw}"

        endtro "\nWere you in that blast?{w=.5} Are you damaged?{w=.5} Please respond!{w=1.0}{nw}"
    else:
        endtro "\n\n\nGood work on recovering the {i}Mugunghwa{/i} files. I just spoke to the sponsor's representative on audio, he sounded really pleased with what you delivered.\n{w=1.0}{nw}"

        endtro "I've credited your account with the standard payment.\n{w=1.0}{nw}"

        endtro "Listen, I've got another job lined up for you. It's on Earth, but it sounds to me like after that last job, you could use a change of pace.{w=3.0} There's a man whose wife has...\n{w=.5}{nw}"

    #with dissolve

    #show background ending with dissolve

    credits "Playtesting\n{size=38}Alex Androski{/size}\n\nPlaytesting\n{size=38}After All{/size}\n\nPlaytesting\n{size=38}Sarah Breen{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Playtesting\n{size=38}Anna Anthropy{/size}\n\nPlaytesting\n{size=38}Jasper Thrussell{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "Korean translation\n{size=38}Jiwon Kim{/size}\n\nKorean PR\n{size=38}mrkwang{/size}\n\nPlaytesting\n{size=38}Daehan Kim{/size}\n\nPlaytesting\n{size=38}Jaeyeon \"Zerial\" Lim{/size}\n\nPlaytesting\n{size=38}Kyungjoon Lee{/size}" with dissolve
    $ renpy.pause(0.2)

    credits "White Rabbit font by\n{size=38}Matthew Welch{/size}\n\nSpecial thanks to\n{size=38}Tom Rothamel{/size}\nCreator of Ren'Py" with dissolve
    $ renpy.pause(0.2)

    if store.use_ending == "ending1":
        #h2 "Hey, I just wanted to say..."

        #h2 "I'm so glad you were there to listen to me."

        $ persistent.ending1 = True
    elif store.use_ending == "ending2":
        #h2 "Wow... I can't believe that I can finally see you!"

        $ persistent.ending2 = True
    elif store.use_ending == "ending3":
        $ persistent.ending3 = True
    elif store.use_ending == "ending4":
        #m2 "You kidnapped me! I can't believe you actually kidnapped me! How barbaric!"

        #m2 "...well. Okay... where are we going together now...?"

        $ persistent.ending4 = True
    elif store.use_ending == "ending5":
        #h2 "Say, if you wanted to spend some time with just me..."

        #m2 "No! You absolutely can't, *Hyun-ae! You're not married, that's completely improper!"

        #h2 "Well... if that's the only problem..."

        #m2 "Ugh, knock it off!"
        $ persistent.ending5 = True

    $ renpy.jump("ending_" + str(persistent._language))

label ending_finish:
    $ check_achievements()
    scene bg white with fade

    $ store.game_finished = True

    $ renpy.save("finished-" + str(int(time.time())))

    return

label ending_:
    if store.use_ending != "ending3":
        show thanks
    if store.radiation and store.reactor_enabled:
        $ credits("\n\n\n\n\n\n{size=38}Bad priorities ending.{/size}\nCompletion rate this time: 0%")
    else:
        $ credits("\n\n\n\n\n\n{size=38}Ending " + store.use_ending[-1] + ".{/size}\nCompletion rate this time: " + complete_rate(store.blocks) + "\nTotal completion rate:{space=51}" + persistent_complete_rate())
    if store.use_ending != "ending3":
        hide thanks
        with dissolve

    jump ending_finish