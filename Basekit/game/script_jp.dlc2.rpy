# baekansi@naver.com / 백안시 / 2011.7.13
# Slightly modded by iAmGhost(@ReallyiAmGhost), 2014-08-13
# Japanese Hiragana modded by achi, 2018-08-30
# Original file Downloaded from: http://www.renpy.org/wiki/renpy/doc/cookbook/Korean_Inputter

init python:
    class HiraganaInput(renpy.Displayable):
        
        vow = cns = cns_i = cns_sutegana = cns_i_sutegana = step = pre_i = pre_i2 = pre_reset = 0

        def __init__(self, prompt = '', italic=False, default = '', length = 100, allow=None, exclude='{}', style = 'default', color="808080DC", font="fonts/gulim.ttf", **properties):
            self.properties = properties
            renpy.Displayable.__init__(self, "", style=style, **properties)
            self.italic = italic
            self.color = color
            self.font = font
            self.ptext = unicode(prompt)
            self.prompt = Text(prompt, style=style, color=color, font=font, **properties)
            self.content = unicode(default)
            
            self.length = length
            self.allow = allow
            self.exclude=  exclude
            self.caret = unicode('')
            
            self.state = 'start'
            
        def flush(self):
            self.content = self.content + self.caret
            self.caret = ''
            self.update_text(self.content, self.caret)
            
            self.vow = self.cns = self.cns_i = self.cns_sutegana = self.cns_i_sutegana = self.step = self.pre_i = self.pre_i2 = self.pre_reset = 0
            self.state = 'start'
            store.search_string = self.content

        def done(self):
            import re
            self.flush()
            final = False
            temp = self.content
            expr = re.compile(r'([a-zA-Z0-9\s~!@#$%^&*()_+|}{:"<>?`\-=\\\[\];\',./])')
            temp = expr.sub('', temp)
            if temp == '':
                return self.content, final
                
            last_alphabet = repr(temp[-1])
            dec = int(str(last_alphabet[4:-1]), 16)
                
            # unicodeの上限未満
            # while dec < 0x3164:
            while dec < 0x3094:
                temp = temp[:-1]
                if not temp:
                    final = False
                    return self.content, final
                    
                last_alphabet=repr(temp[-1])
                dec = int(str(last_alphabet[4:-1]), 16)
                
            dec= (dec-44032) % 588 % 28
            
            if dec == 0: 
                final = False
            else: 
                final = True
        
            return self.content, final
            
        def etoh(self, state, input):
            vowels = (0, 4, 8, 14, 20) # あいうえお
            vowelValue = (1, 7, 3, 9, 5)
            vowelPos = (0, 3, 1, 4, 2)

            consonants = (1, 3, 6, 7, 10, 11, 12, 13, 15, 17, 18, 19, 23, 25) # 子音
            consonantValue = (47, 31, 11, 46, 10, 0, 61, 41, 48, 72, 20, 30, 0, 21) # コードの起点（行）
            consonantStep = (3, 2, 2, 3, 2, 2, 1, 1, 3, 1, 2, 2, 2, 2) # 段のステップ数

            consonants2 = (2, 5, 9, 16, 21, 22, 24)
            consonant2Pos = (0, 1, 2, 3, 4, 5, 6, 7, 8) 
            consonant2Value = ((0x304B, 0x3057, 0x304F, 0x305B, 0x3053), (0x3075, 0x3075, 0x3075, 0x3075, 0x3075), (0x3058, 0x3058, 0x3058, 0x3058, 0x3058), (0x304F, 0x304F, 0x304F, 0x304F, 0x304F), (0x30F4, 0x30F4, 0x30F4, 0x30F4, 0x30F4), 
            (0x308F, 0x3046, 0x3046, 0x3046, 0x3092), (0x3084, 0x3044, 0x3086, 0x3044, 0x3088))

            consonants2SubValue = ((-1, -1, -1, -1, -1), (0x3041, 0x3043, -1, 0x3047, 0x3049), (0x3083, -1, 0x3085, 0x3047, 0x3087), (0x3041, 0x3043, -1, 0x3047, 0x3049), (0x3041, 0x3043, -1, 0x3047, 0x3049), 
            (-1, 0x3043, -1, 0x3047, -1), (-1, -1, -1, 0x3047, -1))

            syValue = (0x3083, 0x3043, 0x3085, 0x3047, 0x3087) # 小文字の「や行」

            diphthongs = (1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 15, 16, 17, 18, 19, 21, 25) # 拗音（Ｙ）
            diphthongValue = (0x3073, 0x3061, 0x3062, 0x3075, 0x304E, 0x3072, 0x3058, 0x304D, 
            0x307F, 0x306B, 0x3074, 0x304F, 0x308A, 0x3057, 0x3061, 0x30F4, 0x3058) # 拗音の一文字目（Ｙ）

            diphthongsH = (2, 3, 18, 19, 22) # 拗音（Ｈ）
            diphthongHValue = (0x3061, 0x3067, 0x3057, 0x3066, 0x3046) # 拗音の一文字目（Ｈ）

            symbols = (52, 53, 54, 55, 56, 57, 58, 59, 60) # 記号
            symbolValue = (0x300C, 0x300D, 0x301C, 0x30FC, 0x3002, 0x3001, 0x30FB, 0xFF01, 0xFF1F) # 記号の置換コード


            input = int(input)
            
            if self.state == 'consonant' or self.state == 'consonant2':        # 子音
                if input in (0, 4, 8, 14, 20):  # 子音 → 母音

                    vowel_i = self.choose(input, vowels, vowelPos)

                    if self.pre_i == self.pre_i2: # 子音の連続による「っ」
                        self.caret = unichr(0x3063)
                        self.content = self.content[:-1]
                        self.content = self.content + self.caret

                    if self.state == 'consonant2': # 「ヴぁ」「ふぁ」「くぁ」「じゃ」「や」「わ」の入力

                        temp = self.choose(self.pre_i, consonants2, consonant2Pos)

                        self.cns = consonant2Value[temp][vowel_i]
                        self.caret = unichr(self.cns)
                        if consonants2SubValue[temp][vowel_i] != -1:
                            self.content = self.content + self.caret
                            self.cns = consonants2SubValue[temp][vowel_i]
                            self.caret = unichr(self.cns)
                    else:
                        self.vow = self.choose(input, vowels, vowelValue)
                        self.step = self.step * ((self.vow - 1) / 2)

                        if self.cns in (30, 31) and input in (4, 14, 20): # た行の「っ」以降は一つ飛ばす
                            self.cns = self.cns + 1
                        self.caret = unichr(0x3041+self.cns+self.step)

                    if (self.pre_i2 == 11 or self.pre_i2 == 23) and self.pre_i == 19 and input == 20: # 「っ」
                        self.caret = unichr(0x3063)
                        self.content = self.content[:-1]
                    elif (self.pre_i2 == 11 or self.pre_i2 == 23) and self.pre_i == 24: # 「ゃ」「ゅ」「ょ」「っ」
                        self.cns = syValue[vowel_i]

                        self.caret = unichr(self.cns)
                        self.content = self.content[:-1]
                        if vowel_i == 3:
                            self.content = self.content[:-1]
                    elif self.pre_i == 24 or (self.pre_i == 7 and self.pre_i2 in (2, 3, 18, 19, 22)): # 拗音
                        temp = self.choose(self.pre_i2, diphthongs, diphthongValue)

                        if self.pre_i == 7 and self.pre_i2 in (2, 3, 18, 19, 22): # 「H」の拗音
                            temp = self.choose(self.pre_i2, diphthongsH, diphthongHValue)

                        if temp:
                            if vowel_i == 3:
                                self.content = self.content[:-1]
                            self.content = self.content[:-1]
                            self.cns = temp

                            self.caret = unichr(self.cns)
                            self.content = self.content + self.caret
                            self.cns = syValue[vowel_i]
                            self.caret = unichr(self.cns)
                    self.state='vowel'
                    self.flush()
                elif input >= 26 and input <= 51: # 全角英語
                    input = int(input - 26)
                    self.content = self.content + self.caret
                    self.caret = unichr(0x41+input)
                    self.state='english'
                    self.flush()
                    self.pre_reset = 1
                elif input >= 52: # 記号
                    self.content = self.content + self.caret
                    self.caret = unichr(self.choose(input, symbols, symbolValue))
                    self.state='symbols'
                    self.flush()
                    self.pre_reset = 1
                else:
                    if self.pre_i == 13 and input == 13: # 「ん」の連続
                        self.cns = self.choose(input, consonants, consonantValue)
                        self.caret = unichr(0x3093)
                        self.flush()
                        self.pre_reset = 1
                    else:
                        if self.pre_i == 13 and input != 24: # 「ん」
                            self.caret = unichr(0x3093)

                        if input in (2, 5, 9, 16, 21, 22, 24): # 「ヴぁ」「ふぁ」「くぁ」「じゃ」「や」「わ」
                            self.state='consonant2'
                        else:
                            self.cns = self.choose(input, consonants, consonantValue)
                            self.step = self.choose(input, consonants, consonantStep)
                            self.state='consonant'
                        self.content = self.content + self.caret
                        self.caret = unichr(0x61 + input)

            elif self.state == 'vowel':        # 母音
                if input < 26 and not (input in (0, 4, 8, 14, 20)): # 母音 → 子音
                    self.content = self.content + self.caret
                    self.caret = unichr(0x61 + input)
                    if input in (2, 5, 9, 16, 21, 22, 24): # 「ヴぁ」「ふぁ」「くぁ」「じゃ」「や」「わ」
                        self.state='consonant2'
                    else:
                        self.state='consonant'
                        self.cns = self.choose(input, consonants, consonantValue)
                        self.step = self.choose(input, consonants, consonantStep)
                elif input in (0, 4, 8, 14, 20):    # 母音を入力
                    self.vow = self.choose(input, vowels, vowelValue)
                    self.content = self.content + self.caret
                    self.caret = unichr(0x3041+self.vow)
                    self.state='vowel'
                    self.flush()
                    self.pre_reset = 1
            else:
                if input < 26 and not (input in (0, 4, 8, 14, 20)):
                    self.content = self.content + self.caret
                    self.caret = unichr(0x61 + input)
                    if input in (2, 5, 9, 16, 21, 22, 24): # 「ヴぁ」「ふぁ」「くぁ」「じゃ」「や」「わ」
                        self.state='consonant2'
                    else:
                        self.state='consonant'
                        self.cns = self.choose(input, consonants, consonantValue)
                        self.step = self.choose(input, consonants, consonantStep)
                    self.cns = self.choose(input, consonants, consonantValue)
                    self.step = self.choose(input, consonants, consonantStep)
                elif input in (0, 4, 8, 14, 20):    # 母音を入力
                    self.vow = self.choose(input, vowels, vowelValue)
                    self.content = self.content + self.caret
                    self.caret = unichr(0x3041+self.vow)
                    self.state='vowel'
                    self.flush()
                    self.pre_reset = 1
                elif input >= 26 and input <= 51: # 全角英語
                    input = int(input - 26)
                    self.content = self.content + self.caret
                    self.caret = unichr(0x41+input)
                    self.state='english'
                    self.flush()
                    self.pre_reset = 1
                elif input >= 52: # 記号
                    self.content = self.content + self.caret
                    self.caret = unichr(self.choose(input, symbols, symbolValue))
                    self.state='symbols'
                    self.flush()
                    self.pre_reset = 1
                        
            # if input == 24 and self.pre_i == self.pre_i2:
            #     input = input
            if self.pre_reset:
                self.pre_i = self.pre_i2 = self.pre_reset = 0
            else:
                self.pre_i2 = self.pre_i # 二文字前のinput値
                self.pre_i = input # 直前のinput値

        def choose(self, key, array, array2):
            for i, k in enumerate(array):
                    if key == k:
                            return array2[i]
            return None
                
        def choose_index(self, key, array):
            for i, k in enumerate(array):
                    if key == k:
                            return i
            return None
            
        def atov(self, alphabet):
            # キーの返り値
            dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 
            'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25,
            'A':26, 'B':27, 'C':28, 'D':29, 'E':30, 'F':31, 'G':32, 'H':33, 'I':34, 'J':35, 'K':36, 'L':37, 'M':38, 'N':39, 
            'O':40, 'P':41, 'Q':42, 'R':43, 'S':44, 'T':45, 'U':46, 'V':47, 'W':48, 'X':49, 'Y':50, 'Z':51, 
            '[':52, ']':53, '^':54, '-':55, '.':56, ',':57, '/':58, '!':59, '?':60, 
                }
            if dict.has_key(alphabet):
                v = dict[alphabet]
                return v
            else:
                return alphabet
                
        def update_text(self, content, caret):
            renpy.redraw(self, 0)
            
            if content != self.content:
                self.content = content
            if caret != self.caret:
                self.caret = caret
                
        def render(self, width, height, st, at):
            
            pw = ph = 0
            
            if self.ptext:
                prompt = renpy.render(self.prompt, 800, 600, st, at)
                pw, ph = prompt.get_size()
            
            if self.caret:
                self.text = Text('%s{u}%s{/u}' %(self.content, self.caret), style = 'input', color=self.color, font=self.font, italic=self.italic, **self.properties)
            else:
                self.text = Text('%s|' %(self.content), style = 'input', color=self.color, font=self.font, italic=self.italic, **self.properties)
            
            text = renpy.render(self.text, 800, 600, st, at)
            tw, th = text.get_size()
            
            r = renpy.Render(pw+ tw, ph + th)
            
            if self.ptext:
                r.blit(prompt, (0, 0))
                
            r.blit(text, (0, ph))
            return r
            

        def event(self, ev, x, y, st):
            import pygame
            # Enterキーを押した
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                self.flush()
                final = 0
                if self.content:
                    self.content, final = self.done()
                return self.content, final
            
            # バックスペースを押した
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_BACKSPACE:
                if self.caret:
                    self.caret = unicode('')
                    self.state = 'start'
                else:
                    self.content = self.content[:-1]
                        
                renpy.redraw(self, 0)
                
            elif ev.type is pygame.KEYDOWN and ev.unicode:
                
                if ord(ev.unicode[0]) <32:
                    return None
                
                if self.length and len(self.content) >= self.length:
                    raise renpy.IgnoreEvent()
                    
                if self.allow and ev.unicode not in self.allow:
                    raise renpy.IgnoreEvent()
                    
                if self.exclude and ev.unicode in self.exclude:
                    raise renpy.IgnoreEvent()
                    
                else:
                    result = self.atov(ev.unicode)
                    
                    if result <= 60:
                        self.etoh(self.state, result)
                        
                    elif (result >= 'a' and result <='z') or (result >= 'A' and result <= 'Z'):
                        raise renpy.IgnoreEvent()
                        
                    else:
                        self.flush()
                        self.content = self.content + ev.unicode
                        
                    
                self.update_text(self.content, self.caret)
                
                raise renpy.IgnoreEvent()
        
# Christine's code follows
# Japanese UI tweaks is Based on iAmGhost's tweaks. Thank you!
init 6 python:
    persistent.hateplus_languages.add("japanese")
    persistent.hateplus_languages.add("japanese_for_search")

    hh.languages["japanese"] = hh_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    h_side.languages["japanese"] = h_side_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=22, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    mm.languages["japanese"] = mm_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    m_side.languages["japanese"] = m_side_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=22, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    nm.languages["japanese"] = nm_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    n_side.languages["japanese"] = n_side_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=22, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")

    mm2.languages["japanese"] = mm2_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    mm2_menu.languages["japanese"] = mm2_menu_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    hh_vn.languages["japanese"] = hh_vn_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    a.languages["japanese"] = a_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    hh_b.languages["japanese"] = hh_b_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")

    # These were missing! - iAmGhost
    hh2_menu.languages["japanese"] = hh2_menu_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")
    hh2.languages["japanese"] = hh2_en.copy(what_font="fonts/mplus-2c-regular.ttf", what_bold=False, what_size=24, window_bottom_padding=20, what_yoffset=-5, font="fonts/mplus-2c-medium.ttf", what_language="eastasian")

    # 名前欄
    style.say_label["japanese"].font = "fonts/mplus-2c-medium.ttf"
    # 本文 (ログファイル中の相槌)
    style.side_text = Style(style.text)
    style.side_text["japanese"].font = "fonts/mplus-2c-regular.ttf"
    style.side_text["japanese"].size = 20
    # style.side_text["japanese"].line_spacing = -4
    # style.side_text["japanese"].line_leading = -4
    style.side_text["japanese"].bold = False
    # 本文
    style.text["hateplusjapanese"].take(style.text["hateplus"])
    style.text["hateplusjapanese"].font = "fonts/mplus-2c-regular.ttf"
    style.text["hateplusjapanese"].size = 18
    style.text["hateplusjapanese"].language = "eastasian"

    style.text["hateplus-body-hyunaejapanese"].take(style.text["hateplus-body-hyunae"])
    style.text["hateplus-body-mutemjapanese"].take(style.text["hateplus-body-mutem"])
    style.text["hateplus-body-mutewjapanese"].take(style.text["hateplus-body-mutew"])
    style.text["hateplus-body-xharemjapanese"].take(style.text["hateplus-body-xharem"])

    style.text["hateplus-hyunaejapanese"].take(style.text["hateplus-hyunae"])
    style.text["hateplus-hyunae-noselectedjapanese"].take(style.text["hateplus-hyunae-noselected"])
    style.text["hateplus-mutemjapanese"].take(style.text["hateplus-mutem"])
    style.text["hateplus-mutem-noselectedjapanese"].take(style.text["hateplus-mutem-noselected"])
    style.text["hateplus-mutewjapanese"].take(style.text["hateplus-mutew"])
    style.text["hateplus-mutew-noselectedjapanese"].take(style.text["hateplus-mutew-noselected"])
    style.text["hateplus-xharemjapanese"].take(style.text["hateplus-xharem"])
    style.text["hateplus-xharem-noselectedjapanese"].take(style.text["hateplus-xharem-noselected"])

    style.text["hateplus-oldstylejapanese"].take(style.text["hateplus-oldstyle"])
    style.text["hateplus-oldstyle-body-hyunaejapanese"].take(style.text["hateplus-oldstyle-body-hyunae"])
    style.text["hateplus-oldstyle-body-mutemjapanese"].take(style.text["hateplus-oldstyle-body-mutem"])
    style.text["hateplus-oldstyle-body-mutewjapanese"].take(style.text["hateplus-oldstyle-body-mutew"])
    style.text["hateplus-oldstyle-body-xharemjapanese"].take(style.text["hateplus-oldstyle-body-xharem"])

    style.text["hateplus-body-hyunaejapanese"].size = style.text["hateplus-body-mutemjapanese"].size = style.text["hateplus-body-mutewjapanese"].size = style.text["hateplus-body-xharemjapanese"].size = 19

    style.text["hateplus-oldstyle-body-hyunaejapanese"].size = style.text["hateplus-oldstyle-body-mutemjapanese"].size = style.text["hateplus-oldstyle-body-mutewjapanese"].size = style.text["hateplus-oldstyle-body-xharemjapanese"].size = 19

    # style.text["hateplus-oldstyle-body-hyunaejapanese"].line_spacing = style.text["hateplus-oldstyle-body-mutemjapanese"].line_spacing = style.text["hateplus-oldstyle-body-mutewjapanese"].line_spacing = style.text["hateplus-oldstyle-body-xharemjapanese"].line_leading = -18

    style.text["hateplus-oldstylejapanese"].size = 19
    style.text["hateplus-oldstylejapanese"].line_leading = -1

    style.text["hateplusjapanese"].size = 19
    style.text["hateplusjapanese"].line_leading = -1


    style.text["hateplus-hyunaejapanese"].layout = style.text["hateplus-mutemjapanese"].layout = style.text["hateplus-mutewjapanese"].layout = style.text["hateplus-xharemjapanese"].layout = "greedy"
    style.text["hateplus-oldstyle-body-xharemjapanese"].language = style.text["hateplus-oldstyle-body-mutewjapanese"].language = style.text["hateplus-oldstyle-body-mutemjapanese"].language = style.text["hateplus-oldstyle-body-hyunaejapanese"].language = style.text["hateplus-oldstylejapanese"].language = style.text["hateplus-body-hyunaejapanese"].language = style.text["hateplus-body-mutemjapanese"].language = style.text["hateplus-body-mutewjapanese"].language = "eastasian"


    style.text["hateplus-oldstyle-body-xharemjapanese"].font = style.text["hateplus-oldstyle-body-mutewjapanese"].font = style.text["hateplus-oldstyle-body-mutemjapanese"].font = style.text["hateplus-oldstyle-body-hyunaejapanese"].font = style.text["hateplus-oldstylejapanese"].font = style.text["hateplus-body-hyunaejapanese"].font = style.text["hateplus-body-mutemjapanese"].font = style.text["hateplus-body-mutewjapanese"].font = style.text["hateplus-hyunaejapanese"].font = style.text["hateplus-hyunae-noselectedjapanese"].font = style.text["hateplus-mutemjapanese"].font = style.text["hateplus-mutem-noselectedjapanese"].font = style.text["hateplus-mutewjapanese"].font = style.text["hateplus-mutew-noselectedjapanese"].font = style.text["hateplus-body-xharemjapanese"].font = style.text["hateplus-xharemjapanese"].font = style.text["hateplus-xharem-noselectedjapanese"].font = "fonts/mplus-2c-regular.ttf"


    # style.text["hateplus-oldstyle-body-xharemjapanese"].size = style.text["hateplus-oldstyle-body-mutewjapanese"].size = style.text["hateplus-oldstyle-body-mutemjapanese"].size = style.text["hateplus-oldstyle-body-hyunaejapanese"].size = style.text["hateplus-oldstylejapanese"].size = 18
    # style.text["hateplus-oldstylejapanese"].size = 18

    style.hateplus_title["japanese"].font = "fonts/mplus-2c-medium.ttf"
    style.hateplus_title["japanese"].bold = False
    style.hateplus_title["japanese"].size = 24
    # style.hateplus_title["japanese"].yoffset = 4

    import locale
    import sys
    import os
    import re

    def set_locale_to_japanese():
        persistent._language = "japanese"

    def check_locale_is_japanese():
        if persistent.auto_detected_language is None:
            persistent.auto_detected_language = True

            if sys.platform == "darwin":  # I'm going to treat darwin as osx, sorry darwin guys!
                cmd = "osascript -e 'return user locale of (get system info)'"

                if os.popen(cmd).read().strip() == "ja_JP":
                    set_locale_to_japanese()

            else:
                if locale.getdefaultlocale()[0] == "ja_JP":
                    set_locale_to_japanese()

    check_locale_is_japanese()


init:
    image thanks_jp:
        "endings/thanks.nd.png"
        #xalign 0.9 yalign 0.9
        alpha 0
        pause 2.0
        linear 2.0 alpha 1.0
