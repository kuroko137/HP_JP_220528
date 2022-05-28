# Christine's code follows
init 1 python:
    style.terminal_line = Style(style.text)
    style.terminal_box = Style(style.vbox)

    # h.languages["japanese"] = Character("*Hyun-ae", color=(255,255,255,220), window_top_padding=0, show_two_window=True, what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc", yoffset=2)
    h.languages["japanese"] = Character("*Hyun-ae", color=(255,255,255,220), window_top_padding=0, show_two_window=True, what_font="fonts/mplus-2c-regular.ttf", what_bold=False, font="fonts/mplus-2c-medium.ttf", yoffset=2, what_language="eastasian")
    h_input.languages["japanese"] = h.languages["japanese"].copy(screen="say_input")
    # m.languages["japanese"] = Character("*Mute", color=(255,255,255,220), window_top_padding=0, show_two_window=True, what_font="0@fonts/NanumGothic.ttc", what_bold=False, font="2@fonts/NanumGothic.ttc", yoffset=2)
    m.languages["japanese"] = Character("*Mute", color=(255,255,255,220), window_top_padding=0, show_two_window=True, what_font="fonts/mplus-2c-regular.ttf", what_bold=False, font="fonts/mplus-2c-medium.ttf", yoffset=2, what_language="eastasian")
    h2.languages["japanese"] = h.languages["japanese"].copy(window_yalign=0.85, window_xalign=0.5, window_background=Frame(im.Composite(None, (0,0), "window.png", (0,0), "window.png", (0,0), "window.png"), 20, 20))
    m2.languages["japanese"] = m.languages["japanese"].copy(window_yalign=0.85, window_xalign=0.5, window_background=Frame(im.Composite(None, (0,0), "window.png", (0,0), "window.png", (0,0), "window.png"), 20, 20))
    # narrator.languages["japanese"] = narrator_en.copy(what_font="0@fonts/NanumGothic.ttc", what_bold=False)
    narrator.languages["japanese"] = narrator_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_layout="greedy", what_language="eastasian")
    # intro.languages["japanese"] = intro_en.copy(what_font="fonts/gulim.ttf", what_line_leading=0, what_size=21)
    intro.languages["japanese"] = intro_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_line_leading=0, what_size=21, what_layout="greedy", what_language="eastasian")
    endtro.languages["japanese"] = endtro_en.copy(what_font="fonts/gulim.ttf", what_line_leading=0, what_size=21)
    # credits.languages["japanese"] = credits_en.copy(what_font="fonts/gulim.ttf")
    credits.languages["japanese"] = credits_en.copy(what_font="fonts/mplus-2c-regular.ttf")

    config.font_replacement_map["fonts/mplus-2c-regular.ttf", True, False] = ("fonts/mplus-2c-medium.ttf", False, False)

    style.button["loadjapanese"].background = style.button["loadjapanese"].selected_background = Frame("mainmenubutton.png", 30, 30)
    style.button["loadjapanese"].hover_background = Frame("mainmenubutton-hover.png", 30, 30) 
    style.button["loadjapanese"].bottom_padding = 30
    style.button["loadjapanese"].top_padding = 20
    style.button["loadjapanese"].insensitive_background = Frame("mainmenubutton-idle.png", 30, 30)

    style.text["japanese"].font = "fonts/mplus-2c-regular.ttf"
    style.text["japanese"].size = 18
    style.text["japanese"].language = "eastasian"
    # style.text["japanese"].line_spacing = -2

    style.title["japanese"].font = "fonts/mplus-2c-medium.ttf"
    style.title["japanese"].size = 24
    style.title["japanese"].yoffset = 4

    style.message_button["japanese"].size = 18

    style.message_button_small["japanese"].size = 16

    style.menu_button["japanese"].size = 38
    style.menu_button["japanese"].bold = False

    style.terminal["japanese"].font = "fonts/ume-tgo4.ttf"

    style.preferences["japanese"].size = 28
    style.preferences["japanese"].bold = False

    style.preferences_button["japanese"].size = 17.5

    style.objective["japanese"].font = "fonts/mplus-2c-regular.ttf"
    style.objective["japanese"].line_leading = 5
    style.objective["japanese"].size = 16

    style.pages["japanese"].size = 16

    style.load["japanese"].size = 20
    style.load["japanese"].kerning = -2

    style.button["loadjapanese"].xpadding = 30
    style.button["loadjapanese"].xmargin = -10

    style.skip["japanese"].size = 16
    style.skip["japanese"].bold = False
    style.load["japanese"].bold = False

    style.main_screen["japanese"].line_spacing = 4
    # style.main_screen["japanese"].size = 19

    style.plain["japanese"].bold = False

    style.block["japanese"].size = 20

    style.log_pages["japanese"].size = 14

init:
    image incomingjapanese = Text("メッセージ受信中", font="fonts/mplus-2c-regular.ttf", color=(255,255,255,255))
