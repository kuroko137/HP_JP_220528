init 6 python:
    persistent.hateplus_languages.add("korean")

    hh.languages["korean"] = hh_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    h_side.languages["korean"] = h_side_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    mm.languages["korean"] = mm_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    m_side.languages["korean"] = m_side_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    nm.languages["korean"] = nm_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    n_side.languages["korean"] = n_side_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")

    mm2.languages["korean"] = mm2_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    mm2_menu.languages["korean"] = mm2_menu_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    hh_vn.languages["korean"] = hh_vn_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    a.languages["korean"] = a_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    hh_b.languages["korean"] = hh_b_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")

    # These were missing! - iAmGhost
    hh2_menu.languages["korean"] = hh2_menu_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")
    hh2.languages["korean"] = hh2_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc")

    en_name = {"*Hyun-ae":"*Hyun-ae", "*Mute":"*Mute", "New *Mute":"New *Mute"}
    en_name["*현애"] = "*Hyun-ae"
    en_name["*뮤트"] = "*Mute"
    en_name["새 *뮤트"] = "New *Mute"

    style.say_label["korean"].font = "2@fonts/NanumGothic.ttc"
    style.side_text = Style(style.text)
    style.side_text["korean"].font = "0@fonts/NanumGothic.ttc"
    style.text["hatepluskorean"].take(style.text["hateplus"])
    style.text["hatepluskorean"].font = "0@fonts/NanumGothic.ttc"

    # I have added many missing styles below here - iAmGhost
    style.text["hateplus-body-hyunaekorean"].take(style.text["hateplus-body-hyunae"])
    style.text["hateplus-body-mutemkorean"].take(style.text["hateplus-body-mutem"])
    style.text["hateplus-body-mutewkorean"].take(style.text["hateplus-body-mutew"])
    style.text["hateplus-body-xharemkorean"].take(style.text["hateplus-body-xharem"])

    style.text["hateplus-hyunaekorean"].take(style.text["hateplus-hyunae"])
    style.text["hateplus-hyunae-noselectedkorean"].take(style.text["hateplus-hyunae-noselected"])
    style.text["hateplus-mutemkorean"].take(style.text["hateplus-mutem"])
    style.text["hateplus-mutem-noselectedkorean"].take(style.text["hateplus-mutem-noselected"])
    style.text["hateplus-mutewkorean"].take(style.text["hateplus-mutew"])
    style.text["hateplus-mutew-noselectedkorean"].take(style.text["hateplus-mutew-noselected"])
    style.text["hateplus-xharemkorean"].take(style.text["hateplus-xharem"])
    style.text["hateplus-xharem-noselectedkorean"].take(style.text["hateplus-xharem-noselected"])

    style.text["hateplus-oldstylekorean"].take(style.text["hateplus-oldstyle"])
    style.text["hateplus-oldstyle-body-hyunaekorean"].take(style.text["hateplus-oldstyle-body-hyunae"])
    style.text["hateplus-oldstyle-body-mutemkorean"].take(style.text["hateplus-oldstyle-body-mutem"])
    style.text["hateplus-oldstyle-body-mutewkorean"].take(style.text["hateplus-oldstyle-body-mutew"])
    style.text["hateplus-oldstyle-body-xharemkorean"].take(style.text["hateplus-oldstyle-body-xharem"])

    # and font settings too - iAmGhost

    style.text["hateplus-oldstyle-body-xharemkorean"].font = style.text["hateplus-oldstyle-body-mutewkorean"].font = style.text["hateplus-oldstyle-body-mutemkorean"].font = style.text["hateplus-oldstyle-body-hyunaekorean"].font = style.text["hateplus-oldstylekorean"].font = style.text["hateplus-body-hyunaekorean"].font = style.text["hateplus-body-mutemkorean"].font = style.text["hateplus-body-mutewkorean"].font = style.text["hateplus-hyunaekorean"].font = style.text["hateplus-hyunae-noselectedkorean"].font = style.text["hateplus-oldstylekorean"].font = style.text["hateplus-mutemkorean"].font = style.text["hateplus-mutem-noselectedkorean"].font = style.text["hateplus-mutewkorean"].font = style.text["hateplus-mutew-noselectedkorean"].font = style.text["hateplus-body-xharemkorean"].font = style.text["hateplus-xharemkorean"].font = style.text["hateplus-xharem-noselectedkorean"].font = "0@fonts/NanumGothic.ttc"

    style.text["hateplus-hyunaekorean"].layout = style.text["hateplus-mutemkorean"].layout = style.text["hateplus-mutewkorean"].layout = style.text["hateplus-xharemkorean"].layout = "greedy"


    style.hateplus_title["korean"].font = "2@fonts/NanumGothic.ttc"
    style.hateplus_title["korean"].bold = False
    style.hateplus_title["korean"].size = 24

    import locale
    import sys
    import os
    import re

    def set_locale_to_korean():
        persistent._language = "korean"

    def check_locale_is_korean():
        if persistent.auto_detected_language is None:
            persistent.auto_detected_language = True

            if sys.platform == "darwin":  # I'm going to treat darwin as osx, sorry darwin guys!
                cmd = "osascript -e 'return user locale of (get system info)'"

                if os.popen(cmd).read().strip() == "ko_KR":
                    set_locale_to_korean()

            else:
                if locale.getdefaultlocale()[0] == "ko_KR":
                    set_locale_to_korean()

    check_locale_is_korean()

init 2:
    python:
        def new_load_local_messages(translations):
            for i in store.hateplus_blocks[0].contents + store.hateplus_blocks[1].contents + store.hateplus_blocks[2].contents + store.hateplus_blocks[3].contents + store.hateplus_blocks[4].contents + store.hateplus_blocks[5].contents + store.hateplus_blocks[6].contents:
                if i not in store.hateplus_blocks[0].contents:
                    translations["//" + i.clean_creator()] = "//" + local_message(i).clean_creator()
                    translations["// " + i.clean_creator()] = "//" + local_message(i).clean_creator()
                    translations[i.name] = local_message(i).name

            return translations

        load_local_messages = new_load_local_messages

init 1:
    python early:
        import string
        OldTranslator = renpy.Translator

        def load_local_messages(translations):
            return translations

        class NewTranslator(OldTranslator):
            def __init__(self, language):
                """
                Loads the translation from the file `language`.rpt
                """

                self.language = language
                self.translations = { }
                
                f = renpy.loader.load(language + ".rpt")
                
                old = None
                
                for l in f:
                    l = l.decode("utf-8")
                    l = l.rstrip()
                    
                    if not l:
                        continue
                    
                    if l[0] == '#':
                        continue
                    
                    s = self.unquote(l[2:])
                    
                    if l[0] == '<':
                        if old:
                            raise Exception("String {0!r} does not have a translation.".format(old))
                        
                        old = s
                        
                    if l[0] == ">":
                        if old is None:
                            raise Exception("Translation {0!r} doesn't belong to a string.".format(s))
                        
                        if old in self.translations and self.translations[old] != s:
                            raise Exception("Multiple translations for {0!r}.".format(old))

                        self.translations[old] = s        
                        old = None

                    if l[0] == "^":
                        if old is None:
                            raise Exception("Translation {0!r} doesn't belong to a string.".format(s))
                        
                        if old in self.translations:
                            raise Exception("Multiple translations for {0!r}.".format(old))

                        new_line = ""
                        for i in s:
                            if i in string.printable:
                                new_line += i
                            else:
                                new_line += "{font=fonts/gulim.ttf}{size=-3}{b}" + i + "{/b}{/size}{/font}"

                        self.translations[old] = new_line
                        old = None
                
                f.close()

                translations = load_local_messages(self.translations)
                
                if old is not None:
                    raise Exception("String {0!r} does not have a translation.".format(old))

        renpy.Translator = NewTranslator
