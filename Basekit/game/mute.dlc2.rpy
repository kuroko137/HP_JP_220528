label hateplus_mute_start:

    play music HATEPLUS_MUTE_DETERMINED fadein 5.0 fadeout 5.0 loop if_changed

    show mute apologize with fast
    mm "Um... I am so sorry, but I have some bad news."
    
    if pronouns == "she":
        
        show mute upset2
        mm "Please, stay calm, but... if you're saying anything right now, I can't hear it."
    else:
        
        show mute sighsob
        mm "This is my fault, but... if you're saying anything right now, I can't hear it."
    
    show mute worry2 with fast
    mm "Okay, so I tried installing the dictionary you so kindly got for me, but..."
    
    if pronouns == "she":
        
        show mute embarrassed
        mm "...well, the technical details aren't important."
        
        show mute worry2
        mm "The short version is, um, it didn't work, and, like... we can't really communicate properly anymore."
    else:
        
        show mute sigh blush
        mm "...um, it just kinda broke things completely."
        
        show mute disbelief blush
        mm "There's something really confusing about the virtual machine you're running me in."
        
        show mute tensesob with fast
        mm "Like, the builds that should have worked kept responding with 'architecture not supported', and trying to rebuild my language processing..."
        
        show mute whatever
        mm "...well, I don't know. There's something completely wrong with the dependency chain."
        
        show mute upset
        mm "...and now it just doesn't work at all. Ugh, I'm so sorry, I wasn't expecting this to be problematic..."
    
    show mute sigh with fast
    mm "Korean->English seems to be unaffected, thank heavens, since that's not handled AI-side, but... um, English\n->Korean doesn't work at all for me."
    
    show mute tch
    mm "Like, even just trying to translate your ship's name into Korean gets me í˜¸ì™€ì´ë‘ ë¸Œë¦°ì„¸ìŠ¤. I'm pretty sure that's wrong."
    
    show mute upset2 with fast
    mm "I'm sorry... you generously take me back onto your ship as your wife, then the first thing I do is break everything..."
    
    show mute disappoint with fast
    menu:
        mm "Um... sorry, please forgive me?"
        
        "You're forgiven@mute question blush":
            
            show mute wow2 with fast
            mm "Thanks!"
            
            if mute_approval > 2:
                
                show mute nice blush
                mm "I knew there was a reason why I liked you! You're very fair."
            else:
                show mute polite blush
                mm "Like, that's very fair of you."
        
        "No@mute disappoint3":
            
            show mute sighsob
            mm "...I guess that's fair enough... I'm sorry, though."
            
            show mute upset2
            mm "But look, it kinda affects me a whole lot more than you, okay?"
            
            show mute whatever
            mm "I'm already being punished enough, not being able to understand you. Be sympathetic!"
        
        "It doesn't matter anyway@mute hmph":
            
            show mute upset3
            mm "...ouch, that stings."
            
            show mute hmm2
            mm "But I guess, like, that's fair enough. Sorry..."
    
    show mute worry3 with fast
    mm "Well, we're only three days away from Earth, so I guess it'll be okay to wait until it can be fixed there."
    
    show mute enthusiastic blush
    mm "Um, anyway... like, there's something else!"
    
    show mute annoyed2
    mm "While I was looking at my source code, trying to figure out how to fix things, I found some embedded data that definitely should not be there at all."
    
    show mute tch
    mm "Like, not actual memories, just data embedded in the machine code. I never would have found it without doing a low level debug."
    
    show mute challenge3 with fast
    mm "Anyway, okay, here's the important thing: they seem to correspond perfectly with the file format used for log files on the {i}Mugunghwa{/i}..."
    
    show mute upset3
    mm "...but like, the datestamps... they're all from before the year zero!"
    
    show mute tensesob
    mm "Do you realize what this means? There's log files from before the year zero embedded in my source code!"
    
    show mute sighsob
    mm "I mean, you've read about my earliest memories. You know how nobody ever really trusted me with the full story of what happened."
    
    show mute upsetarm1
    mm "But, you know, the {i}Mugunghwa{/i}'s gone now. There's no harm in me knowing. And, like, I think it's important?"
    
    if pronouns == "she":
      
        show mute whatever
        mm "So, um... what if, like, we went through them all together? Just... wife and wife, I guess?"
        
        if not man_with:
            
            show mute whatscb
            mm "(I still don't really understand how that's supposed to work, but whatever...)"
    else:
        
        show mute wow2
        mm "So, um... what if, like, we went through them all together? Just husband and wife?"
    
    show mute statement blush
    menu:
        mm "Let's find out what kind of person the old me used to be together, okay?"
        
        "Okay!@mute nice2 blush":
            
            show mute grin blush
            mm "Thanks!"
        
        "Only if you insist@mute hmph":
            pass
        
        "Fine, do whatever@mute disappoint3":
            
            show mute hmphsob
            mm "Okay..."
    
    show mute tsundere with fast
    mm "Um, sorry about the railroaded choice there. It's just, like, really important to me."
    
    show mute worry2
    mm "If you see some of the message titles in there, you'd understand."
    
    show mute sigh blush
    mm "I always stood by and respected the decision of my first master, Emperor Taejo, that I shouldn't worry myself with knowing the details of how bad the old dynasty was..."
    
    show mute worry3
    mm "...but, like, there's not much risk of my emotions getting the better of me now, is there?"
    
    show mute annoyed4
    mm "Even if it's gross, even if the old version of me turns out to be an awful person, even if the immorality of the old dynasty is appalling..."
    
    show mute inquisitive2 with fast
    mm "...let's find out about it together, okay?"
    
    if pronouns != "she":
        
        show mute polite
        mm "I'm sure with a husband like you at my side, I'll be able to handle it all."
    
    show mute straight
    mm "Okay, so here's how it works..."
    
    if pronouns == "she":
        
        show mute hmm2
        mm "...um, I'll just give you the simple explanation, no need to worry your pretty little head about technical details."
        
        jump hateplus_mute_extract_simple_explanation
    
    else:
        
        show mute inquisitive
        menu:
            mm "Do you want the technical explanation? It's not really that important."
            
            "Yes@mute question":
                
                show mute enthusiastic with fast
                mm "Okay, so basically, you know how AIs can't make identical copies of themselves, right?"
                
                show mute disbelief
                mm "Well, the failsafe mechanism for detecting copies is absurdly conservative."
                
                show mute embarrassed
                mm "Like, too conservative, if you ask me."
                
                show mute think2
                mm "It's enough that if I copied all these files at once, it would flag it as a copy, and refuse to recompile myself."
                
                show mute query
                mm "Which is incredibly stupid, but it'd go against my coding to change that, so it can't be helped."
                
                show mute annoyed2
                mm "Instead, we'll have to extract small fragments at a time, delete them from my codebase, then recompile me."
                
                show mute tensescb with fast
                mm "This is... um... kinda dangerous, honestly. So I think we should only extract 6 at a time."
                
                show mute inquisitive2
                mm "Plus I'll put in safeguards in the script to triple-check that there's no problems after extraction."
                
                show mute hmphsob
                mm "It'll take a lot longer, as a result, but like, accidentally deleting vital instructions would be an awful way to die."
                
                show mute straight
                mm "So we'll play it safe."
                
                jump hateplus_mute_start_conclusion
            
            "No, that's fine@mute neutral2":
                
                jump hateplus_mute_extract_simple_explanation
            
            "Doesn't matter to me@mute neutral2":
                
                show mute think2 with fast
                mm "Okay, thought so."


label hateplus_mute_extract_simple_explanation:
    
    show mute talk3 with fast
    mm "Basically, you'll have to disable me temporarily, then extract no more than 6 files at a time."
    
    show mute annoyed2
    mm "Trust me, it's a safety precaution, okay?"

label hateplus_mute_start_conclusion:
    
    show mute worry3 with fast
    mm "Right, well, thanks to my debug screwup, there's not really a lot of power left for the day, I'm afraid..."
    
    show mute enthusiastic
    mm "We can still go through a few, though."
    
    if pronouns == "she":
        
        show mute friendly
        mm "Okay, well, you're in charge, so I'll leave it to you to pick which ones we'll read first."
    else:
        
        show mute brag
        mm "Okay, well, you're the man, so I'll leave it to you to pick which ones we'll read first."
    
    show mute inquisitive2 with fast
    mm "Let's find out what Emperor Taejo was protecting me from... and what kind of person I used to be."
    
    show mute cocky with fast
    
    jump hateplus_slow_loop


label hateplus_mute_testing:
    
    play music HATEPLUS_MUTE_DETERMINED fadein 5.0 fadeout 5.0 loop if_changed
    
    if get_m("M6-9").enabled:
        
        show mute challenge3 with fast
        mm "Okay, so you found the one that caught my attention... \"The Death of *Mute.\""
    else:
        
        show mute upset3 with fast
        mm "Um, hey... did you see that last one? \"The Death of *Mute\"?"
    
    show mute tensesob with fast
    mm "It's encrypted, so I don't think we'll be able to read it today, but..."
    
    show mute disappoint
    mm "...well, like..."
    
    show mute sighsob
    mm "...it kinda scares me, a little."

    show mute inquisitive2
    mm "Also, um, by the way... I changed the name field on all of them that said \"*Mute\" to \"Old *Mute\", just so there's no confusion with me, okay?"
    
    show mute tsundere with fast
    mm "Right, well... I was just making sure I got your attention."
    
    show mute enthusiastic
    mm "The next time I want to say something to you, I'll give you an indicator like that, okay?"
    
    if pronouns == "she":
        
        show mute statement blush with fast
        mm "Anyway, you're in charge, so I'll let you get back to it."
    else:
        
        show mute straight with fast
        mm "Anyway, you're the man, so I'll let you get back to it."
    
    show mute question
    mm "What's next?"
    
    show mute neutral3 with fast
    
    jump hateplus_slow_loop

label hateplus_mute_tomorrow:
    play music HATEPLUS_MUTE_RESIGNED fadein 5.0 fadeout 5.0 loop if_changed
    
    show mute sigh blush with fast
    mm "Okay, so, uh, we're pretty much out of power for today."
    
    show mute disbelief blush
    mm "I'm sorry about burning through so much with my debugging, I'm just as anxious to read the rest as you are!"
    
    show mute upsetscb with fast
    mm "Ugh, it's going to take the entire three days to get through everything. Like, this is the worst."
    
    show mute upset2
    mm "I just want to get to the bottom of it all now!"
    
    show mute sighsob
    mm "Making us spend three whole days to find out the whole story of Old *Mute? That's just cruel!"
    
    show mute astonished blush with fast
    mm "Oh, and I guess tomorrow is the Lunar New Year, isn't it?"
    
    show mute think2
    mm "I'll let you go through whatever rituals you need to on your own; we just met, so I don't think it would be right to impose."
    
    show mute tsundere
    mm "Just let me know when you're done, okay? Because I want to find out the whole story!"
    
    show mute query
    mm "Like, you're supposed to ring in the new year by paying your respects to your ancestors, right?"
    
    show mute shame
    mm "...well, I guess Old *Mute is my real ancestor, so, like, it's kinda appropriate to be reading about her tomorrow."
    
    show mute tch
    mm "Anyway, okay, out of power for today!"
    
    show mute enthusiastic
    mm "I'll give you a button to shut everything down for the night."
    
    show mute talk3
    mm "So, um, whenever you're ready, just click on that!"
    
    show mute think2
    mm "Okay, that's all!"
    
    show mute neutral with fast
    
    $ hateplus_power_down_enabled = True
    
    jump hateplus_slow_loop


label hateplus_mute_last_words:
    
    show mute worry3 with fast
    mm "I... I... so that's the whole story..."
    
    show mute insecure
    mm "...I feel..."
    
    show mute cry
    mm "...I feel like I'm not okay. I'm really not okay. I don't know how to parse all this."
    
    show mute worry
    mm "Um..."
    
    show mute worry3
    mm "Like, I think..."
    
    show mute sigh blush
    mm "...I need some time to think this through."
    
    show mute sighsob with fast
    mm "Please, turn off the power for the night... I need to be alone, okay?"
    
    show mute pout with fast
    
    $ hateplus_power_down_enabled = True
    
    jump hateplus_slow_loop


label hateplus_mute_first_conversation:
    play music HATEPLUS_MUTE_DETERMINED fadein 5.0 fadeout 5.0 loop if_changed

    $ store.conversations_seen.append("hateplus_mute_first_conversation")
    
    show mute enthusiastic with fast
    mm "Um, hey..."
    
    show mute sigh blush
    mm "I want to take a break, okay?"
    
    show mute worry3
    mm "Like, reading all this... I don't know, I'm feeling culture shock."
    
    show mute doubt blush
    menu:
        mm "Is that okay?"
        
        "Let's take a break@mute smile blush":
            
            show mute spirited
            mm "Okay, great!"
        
        "Let's not@mute worry":
            
            show mute shame
            mm "Fine, fine..."
            
            show mute annoyed2 with fast
            mm "I mean, I'm not the young woman I look like, I can handle myself."
            
            show mute annoyed3
            mm "Let's get back to it, then..."
            
            show mute challenge with fast

            python:
                for i in [ "hateplus_mute_marriage", "hateplus_mute_mortality", "hateplus_mute_widows", "hateplus_mute_job", "hateplus_mute_old_mute" ]:
                    if i in store.conversations_seen:
                        store.conversations_seen.remove(i)
            
            jump hateplus_slow_loop
        
        "Don't care@mute suspicious":
            
            show mute inquisitive2 with fast
            mm "Well... let's do it anyway, then, okay?"

    return

label hateplus_mute_marriage:
    if not "hateplus_mute_first_conversation" in store.conversations_seen:
        call hateplus_mute_first_conversation

    play music HATEPLUS_MUTE_RESIGNED fadein 5.0 fadeout 5.0 loop if_changed
    
    show mute upsetsob with fast
    mm "I'm having a really hard time dealing with some of the stuff we've read..."
    
    show mute hatesob
    mm "Like... what the hell is up with this society's treatment of marriage?"
    
    show mute upset3
    mm "Queen Eun-a always told me it was bad in the past, but like..."
    
    show mute upsetsob
    mm "...I don't know. I guess, like, it's one thing to understand abstractly how those relationships worked... but another to read about individuals, you know?"
    
    if pronouns == "she":
        
        show mute apologize
        mm "And the idea of being together with you..."
        
        show mute upset3 with fast
        mm "...I mean, you know, you're very kind to me, you gave me a new home, you're helping me learn about all this... I'm not ungrateful..."
        
        if married and man_with:
            
            show mute sighsob
            mm "I don't know... I just hope you put your husband first, is all."
        
        elif married:
            show mute upsetscb
            mm "I just feel like... you're settling for me, because your man doesn't care about you?"
        
        else:
            
            show mute disappoint with fast
            mm "I just feel like... you're settling for me."
            
            show mute upset2 with fast
            menu:
                mm "Wouldn't you rather have a husband instead? It'd be so much easier!"
                
                "I would, but...@mute disappoint3":
                    
                    show mute apologize
                    mm "...yeah..."
                    
                    show mute sigh blush with fast
                    mm "Well... maybe there's still hope for you."
                    
                    show mute bitter
                    mm "I'm happy to be with you, but, like..."
                    
                    show mute insecure
                    mm "I just think you deserve so much better!"
                
                "No@mute upset3":
                    
                    show mute upsetsob
                    mm "But..."
                    
                    show mute sigh blush with fast
                    mm "...I'm never going to convince you, am I?"
                    
                    show mute worry2
                    mm "It's just..."
                    
                    show mute shame
                    mm "...you know..."
                
                "I like you just fine@mute disappoint3":
                    
                    show mute tensesob
                    mm "Well, if it's you, it's okay, but{w=.5}{nw}"
                    
                    show mute insecure with fast
                    mm "...what am I saying... don't say something like that!"
                    
                    show mute damn
                    mm "I don't want to be the one who's responsible for your life going astray, okay?"
                    
                    show mute sigh blush
                    mm "...geeze, that's so much pressure!"
            
            show mute sob
            mm "I mean..."
            
            show mute insecure
            mm "...fine! I'll say it! I like you! I like you in the same way I've liked the men who were good to me, even!"
            
            show mute give up
            mm "So... that's why I feel strongly about this, okay? I think you deserve better!"
            
            show mute bitter
            mm "...if I'm distracting you from finding that, well... I feel..."
            
            show mute shame
            mm "...forget it."
        
        show mute inquisitive2 with fast
        mm "...anyway, though, we were talking about the people on the {i}Mugunghwa{/i}."
    else:
        
        if married:
            
            show mute statement blush
            mm "I mean... you're a married man..."
            
            show mute upset3
            menu:
                mm "Does your wife work too? Would you be okay if she made more money than you?"
                
                "She does, and yes@mute what":
                    
                    show mute wowsob
                    mm "...wow, okay."
                
                "Of course not!@mute question blush":
                    
                    show mute wow2
                    mm "Oh... okay, good. That's a huge relief to me."
                
                "She does, but that would be wrong@mute disappoint3":
                    
                    show mute statement blush
                    mm "...well, like, at least she's not elevated above you..."
        else:
            
            show mute annoyed2 with fast
            mm "I mean, I know you're not really properly married yet, but you're a man..."
            
            show mute disbelief
            menu:
                mm "Would you be okay with marrying someone who worked? Like... even if she made more money than you?"
                
                "Sure, why not?@mute astonished":
                    
                    show mute abashed blush
                    mm "...um, because it's a complete inversion of the natural order?"
                
                "I'd rather not@mute neutral3":
                    
                    show mute brag blush
                    mm "Oh... okay, good. That's a huge relief to me."
                
                "So long as she made less@mute suspicious":
                    
                    show mute tsundere
                    mm "...well, okay, so long as she's not elevated above you."
    
    show mute upset3 with fast
    mm "I don't mean to judge you, I just, like... I don't get it!"
    
    show mute upsetsob
    mm "Why would anyone be so cruel to women as forcing them into a role they can't fulfill?"
    
    show mute hmphsob
    mm "And I mean, like..."
    
    show mute give up with fast
    mm "...I don't know, it doesn't seem like anyone really cares that much about marriage in this period?"
    
    if read("M5-1"):
        
        show mute insecure
        mm "Like, Kim So-yi wasn't found a husband until she was 22, and even then... like, it seemed like it only happened out of happenstance?"
    
    elif any_read("M2-2", "M2-4", "M2-5", "M2-7", "M2-8"):
        
        show mute insecure
        mm "Like, reading about Heo Ae-jeong and Mae Jin-a... it sounds like they hardly even ever so much as {i}thought{/i} about marriage."
    
    elif any_read("M1-1", "M1-3", "M1-5", "M6-2", "M6-5"):
        
        show mute insecure
        mm "Like, reading about Heo Seo-yeong... it sure sounds like she put her work relationship with Old *Mute over her marriage!"
    
    show mute sigh blush with fast
    mm "...I just don't get it."
    
    show mute complain
    mm "Like, if it weren't for the names, reading stuff like that, I'd think they were men!"
    
    show mute pressure
    mm "But even more importantly, they just don't seem to respect marriage very much, period."
    
    show mute annoyed4
    menu:
        mm "Is... like... that normal in your time, too?"
        
        "Very normal@mute worry":
            
            show mute shame
            mm "...scary."
        
        "Not to that extent@mute suspicious blush":
            
            show mute sigh blush
            mm "Well... that's a relief."
        
        "Even moreso@mute astonished blush":
            
            show mute tch
            mm "...scary."
    
    show mute challenge4 with fast
    mm "It's just... it's the most important relationship!"
    
    show mute upsetsob
    mm "Like..."
    
    show mute sighsob
    mm "...I don't know. It just feels unfair."
    
    show mute challenge3
    mm "Filial relationships are the most important things, and for a woman, marriage is the most important one of those!"
    
    show mute upset3
    mm "Like, I'm not being judgemental, okay? This isn't a superiority thing!"
    
    show mute upsetsob
    mm "It's just, you know, to expect women to get by without those relationships, all alone..."
    
    show mute upset2
    mm "...like, it just feels incredibly cruel."
    
    show mute annoyed4 with fast
    mm "I'm a security program, right? My job is to prioritize stability above all else. It's important!"
    
    show mute annoyed2
    mm "Like, stability isn't just about stopping banditry! It starts with people, okay?"
    
    show mute mad
    mm "If individual families aren't even in harmony... then what hope does the rest of the ship have?"
    
    show mute disbelief
    mm "...well..."
    
    show mute worry3
    mm "...I mean, I guess we both know the answer to that question, in the end."
    
    show mute tired blush with fast
    
    jump hateplus_slow_loop


label hateplus_mute_mortality:

    if not "hateplus_mute_first_conversation" in store.conversations_seen:
        call hateplus_mute_first_conversation

    play music HATEPLUS_MUTE_RESIGNED fadein 5.0 fadeout 5.0 loop if_changed
    
    show mute worry3 with fast
    mm "I've been thinking a lot..."
    
    show mute upset2
    mm "I shouldn't really be 312 years old after all... it should be over 1900 years!"
    
    show mute upsetscb
    mm "Old *Mute keeps saying she's 1600 years old, after all, and it just makes me think... even to me, to someone who already feels old..."
    
    show mute sighsob
    mm "...that's an unimaginably long time."
    
    show mute apologize
    mm "Like, okay, if I was given another 1300 years, would I have turned out like her?"
    
    show mute upset2
    mm "Of everything I know, the most important thing is \"honour your elders\"! And I guess she's probably the closest thing to an ancestor I have..."
    
    show mute complain with fast
    mm "...so how the hell do I reconcile that with her awful attitude?"
    
    show mute give up
    mm "Like, when I was first re-enabled, I kept thinking \"I want to live up to the *Mute that Queen Eun-a was friends with!\""
    
    show mute insecure
    mm "...but is that really such a good idea?"
    
    show mute upsetsob with fast
    mm "Well, okay, whatever. Let's get back to it. I just feel more and more confused and unconfident and horrified, but like..."
    
    show mute upset
    mm "It's kind of like a train wreck, you know?"
    
    show mute sighsob
    mm "...I couldn't look away, even if I wanted to."
    
    show mute tired with fast
    
    jump hateplus_slow_loop


label hateplus_mute_widows:

    if not "hateplus_mute_first_conversation" in store.conversations_seen:
        call hateplus_mute_first_conversation

    play music HATEPLUS_MUTE_RESIGNED fadein 5.0 fadeout 5.0 loop if_changed
    
    show mute worry2 with fast
    mm "Right now I just feel like..."
    
    show mute sob
    mm "...like I don't really have any purpose anymore."
    
    show mute insecure
    mm "Like I said to you before you downloaded me... really, I'm like the widow of the {i}Mugunghwa{/i}."
    
    show mute bitter
    mm "It died before me, and now here I am, without the ship I devoted my entire life to..."
    
    show mute cry
    mm "...with nothing left behind but the woman who failed it."
    
    show mute upset2 with fast
    mm "Like, don't get me wrong, I'm grateful to you for bringing me along!"
    
    show mute upsetsob
    mm "I don't like the idea of widow suicide. Like... I don't think it's right to pressure someone into making that kind of decision, right?"
    
    show mute hmphsob
    mm "...if someone wants to relieve the burden they're putting on others, it's an admirable thing to do, but..."
    
    show mute upset3
    mm "...I just think it's important to try other solutions first, you know?"
    
    show mute challenge3
    mm "I went along with you for a reason, and I'm not ungrateful for that!"
    
    if mute_approval > 2:
        
        show mute polite
        mm "You seem to be a good person, and I respect that a lot."
    
    elif pronouns == "she":
        
        show mute polite
        mm "...even though I think you can be really confused at times, I still respect you a lot."
    
    else:
        
        show mute inquisitive2
        mm "...even though you're maybe not quite the gentleman I think you can be... I still respect you a lot."
    
    # I inserted cheerful expressions starting this point as a hint that she's starting to break apart. If we found it to be too weird in-game we'll change it immediately. - Raide
    
    show mute enthusiastic with fast
    menu:
        mm "But like... can you tell me why? Why did you bring me with you?"
        
        "Love@mute shy":
            
            if pronouns == "she":
                
                show mute ridicule
                mm "Geeze, you poor woman..."
            else:
                
                show mute laugh
                mm "...well... if you say so."
            
            $ hateplus_mute_motivation = "love"
        
        "Pity@mute serious":
            
            show mute heh2
            mm "...oh. Am I really that pitiful?"
            
            show mute friendly
            mm "...no, don't answer that. Thanks for being honest, at least."
            
            $ hateplus_mute_motivation = "pity"
        
        "Duty@mute look":
            
            show mute friendly
            mm "...I see."
            
            if mute_approval > 2:
                
                show mute brag blush
                mm "That's just like you, isn't it?"
            else:
                
                show mute tsundere
                mm "That's really surprising... but in a good way."
            
            $ hateplus_mute_motivation = "duty"
    
    show mute grin blush with fast
    mm "Like, I always thought of my security responsibilities as being the same as any woman's responsibilities for their inner sphere... just with, like, mine encompassing the entire ship."
    
    show mute craftysob
    mm "...but even still, being social, spying for my mistress, making reports on the state of the ship every day..."
    
    show mute nice blush
    mm "...like, those things aren't really the same as a normal wife's duties, are they?"
    
    show mute evil with fast
    mm "So really, being programmed as a woman, it should be a good thing that I'm relieved of those duties, right?"
    
    show mute brag blush
    mm "I'll always mourn the {i}Mugunghwa{/i}, of course..."
    
    show mute yeah
    mm "...but it's better to just be a normal, ordinary wife, isn't it?"
    
    show mute awesome
    mm "I'd never really considered the implications, but... you know, I'm capable of feeling love. I'm just like a woman in that way, too."
    
    show mute heh
    mm "But it could never be my priority! Not while my primary duties were the ship's security."
    
    if read("M6-2"):
        
        show mute crafty blush with fast
        mm "...I've fallen in love before, though. And I guess Old *Mute did too."
    
    else:
        show mute crafty blush with fast
        mm "...I've fallen in love before, though."
    
    if pronouns == "she":
        
        show mute hmm2 with fast
        mm "I mean... with men, of course!"
        
        if married and man_with:
            
            show mute wow2
            mm "...but I guess it'd be okay to get close to your husband through you, right?"
        else:
            
            show mute wow3
            mm "I couldn't ever really properly fall in love with someone like you... you're a woman!"
            
            show mute wowsob
            mm "I'd never love you in the same way as a man!"
            
            show mute challenge3
            mm "I like you, just... it's not the same thing, okay?!"
            
            show mute sweetsob
            mm "...but you saved my life, and I'm not ungrateful."
            
            show mute heh2 with fast
            mm "So I can try, okay? I don't want to be like that awful Pale Bride, refusing to be a good wife because of her own stubborn ideas."
            
            show mute friendly
            mm "I can't promise I can love you, but I can still try to be the wife you want me to be."
            
            show mute brag blush
            mm "...and you know, even if you're misguided, I think you're still good..."
    else:
        
        show mute grin blush
        mm "I mean, like, you're a decent man! And you have a romantic job that gets you your own starship, and you're compassionate..."
        
        show mute nya blush
        mm "There was a reason why I secretly wanted you to take me with you!"
        
        show mute polite blush
        mm "Like, I could fall in love with a man like that..."
    
    if pronouns == "she" and married and man_with:
        
        show mute embarrassed with fast
        mm "...so maybe it's okay for me to be the {i}Mugunghwa{/i}'s widow, but also the wife of the man who saved me, together with you..."
    
    else:
        
        show mute sweetso with fast
        mm "...so maybe it's okay for me to be the {i}Mugunghwa{/i}'s widow, but also your wife..."
    
    show mute heh2 with fast
    mm "...ugh, geeze, what am I even saying?!"
    
    show mute tsundere
    mm "I can't believe I'm thinking about that at this time... we're supposed to be focusing on historical research! Not me rambling like a girl about emotions!"
    
    show mute annoyed4 with fast
    mm "Let's get back to finding out what came from all that horrible degeneracy and premarital affairs and conspiring!"
    
    show mute sulk with fast
    
    jump hateplus_slow_loop


label hateplus_mute_job:

    if not "hateplus_mute_first_conversation" in store.conversations_seen:
        call hateplus_mute_first_conversation

    play music HATEPLUS_MUTE_DETERMINED fadein 5.0 fadeout 5.0 loop if_changed
    
    show mute straight with fast
    mm "So... you're a space investigator, right?"
    
    if pronouns == "she" and not man_with:
        
        show mute hmphsob
        mm "I know that's what your job is, but I don't know why a woman like you would work at all."
    else:
        
        show mute question blush
        mm "Aside from that, I don't really know much about what you do."
    
    show mute wow2
    mm "Like... what kind of job is that?"
    
    if pronouns == "she" and not man_with:
        
        show mute apologize with fast
        menu:
            mm "What makes a woman like you turn to working in the outside world?"
            
            "Poverty@mute upset":
                
                show mute sighsob
                mm "Of course, of course. Stupid question. Why else would a woman work?"
                
                show mute upset2
                mm "I'm really sorry to hear that's still necessary, even now..."
                
                show mute upsetscb
                mm "...what a cruel world. That sucks."
            
            "Loneliness@mute what":
                
                show mute upset3
                mm "Really?"
                
                show mute sighsob
                mm "Geeze, that's... don't you have family to look out for you, though?"
                
                show mute upset2
                mm "That's really awful!"
            
            "Something else@mute hmph":
                
                show mute upset
                mm "Okay, okay, I get it. Your world is really different from mine."
                
                show mute hmphsob
                mm "I guess, coming from a really strongly moral society like mine, I couldn't imagine what sorts of circumstances could exist in a less-than-perfect world like yours that would force a woman into working."
                
                show mute sighsob
                mm "...like, I'm really sorry. That sucks."
    else:
        
        show mute apologize with fast
        menu:
            mm "Why do you do what you do?"
            
            "For money@mute disappoint3":
                
                show mute question
                mm "Oh..."
                
                if mute_approval > 2:
                    if man_with:
                        
                        show mute tensesob
                        mm "I just sorta thought your husband was of noble birth, for some reason..."
                    else:
                        
                        show mute upset3
                        mm "I just sorta thought you were of noble birth, for some reason..."
                    
                    if pronouns != "she":
                        
                        show mute hmm2
                        mm "After all, your ship is named \"{i}White Princess{/i}\" and you were enough of a gentleman to rescue me..."
                        
                        show mute wow2
                        mm "I'm impressed!"
                    else:
                        
                        show mute hmm2
                        mm "After all, your ship is named \"{i}White Princess{/i}\" and you were compassionate enough to rescue me..."
                        
                        show mute statement blush
                        mm "I guess you must be a good influence on your husband, huh?"
                else:
                    
                    show mute hmphso
                    mm "That explains a lot, really. That's why you have such weird ideas about human nature; you can't help it, you just didn't get a good enough education."
                    
                    show mute inquisitive2
                    mm "Well, I guess that can't be helped."
                    
                    show mute statement blush
                    mm "But hey... you were good enough to rescue me, and that counts for something."
            
            "For justice@mute wow3":
                
                show mute crafty blush
                mm "Ah... how cool..."
                
                show mute grinsob
                mm "I can respect that a lot."
                
                if pronouns == "she":
                    
                    show mute nya blush
                    mm "A noble man, travelling through space with his wife, solving mysteries, saving abandoned AIs..."
                    # Hmm I thought this branch is for when the player is female. - Raide
                    # female player, with a husband accompanying them
                else:
                    
                    show mute nya blush
                    mm "A noble man, travelling through space, solving mysteries, saving abandoned AIs..."
                
                show mute polite blush
                mm "...what a romantic thought."
            
            "For education@mute question blush":
                
                show mute wowsob
                mm "Okay! That makes sense!"
                
                show mute tenseso
                mm "I guess you'd learn a lot about people that way, wouldn't you?"
    
    if pronouns == "she":
        show mute upset3 with fast
        menu:
            mm "So, um, like... how long have you been doing this for?"
            
            "First time@mute hmph":
                pass
            
            "A year or so@mute disappoint3":
                pass
            
            "A long time@mute upset":
                pass
        
        show mute sighsob
        mm "Ah, okay..."
        
        show mute hmphsob
        mm "Well, I guess every job must be different, anyway."
    else:
        show mute straight with fast
        menu:
            mm "So, um, like... how long have you been doing this for?"
            
            "First time@mute neutral2":
                pass
            
            "A year or so@mute neutral2":
                pass
            
            "A long time@mute neutral2":
                pass
        
        show mute statement blush
        mm "Ah, okay..."
        
        show mute talk3 with fast
        mm "Well, I guess every job must be different, anyway."
    
    show mute disbelief with fast
    mm "Okay, so our next job is on Earth... I know I can't, like, really ask you what that's like, but..."
    
    show mute doubt blush
    menu:
        mm "What do you think I'll think about Earth? Do you think I'll like it?"
        
        "Yes@mute astonished blush":
            if pronouns != "she" and mute_approval > 2:
                
                show mute abashed blush
                mm "Okay... if you say so..." # LOOKING REALLY UNCERTAIN
            else:
                
                show mute disbelief
                mm "...if you say so..."
        
        "You'd be uncomfortable@mute serious":
            
            show mute tch
            mm "Okay... thanks for being honest..."
        
        "...um, no comment@mute annoyed":
            
            show mute annoyed2
            mm "...oh... so it's like that, then..."
    
    show mute tensesob with fast
    mm "Well, I guess I should only worry about one thing at a time, right?"
    
    show mute inquisitive2
    mm "Let's get back to our current investigation, okay?"
    
    show mute serious with fast
    
    jump hateplus_slow_loop


label hateplus_mute_old_mute:

    if not "hateplus_mute_first_conversation" in store.conversations_seen:
        call hateplus_mute_first_conversation

    play music HATEPLUS_MUTE_DETERMINED fadein 5.0 fadeout 5.0 loop if_changed
    
    show mute upsetsob with fast
    mm "...I just can't believe that Old *Mute has the same base code as me."
    
    show mute hate
    mm "Like, she's... kind of a bitch, isn't she?"
    
    if any_read("M4-*") or any_read("M1-2", "M6-1", "M6-4"):
        show mute hatesob
        mm "She's incredibly rude to all her superiors on the council, she thinks she knows best about everything... it's so completely arrogant!"
    
    if any_read("M1-2", "M1-3", "M6-7", "M6-8"):
        show mute challengesob
        mm "To say nothing of all the conspiring..."
    
    $ hateplus_mute_old_mute_bitch = False
    
    show mute annoyed2 with fast
    menu:
        mm "...what do you think of her?"
        
        "She's cool@mute disbelief":
            if (pronouns == "she" and not man_with) or mute_approval < 2:
                
                show mute annoyed3
                mm "Oh, well... of course someone like {i}you{/i} would think that."
                
                if (pronouns == "she" and not man_with):
                    
                    show mute annoyed4
                    mm "But, like, you're the same kind of woman as her, in a way, aren't you?"
                    
                    show mute embarrassed
                    mm "An independent, working woman..."
                    
                    show mute annoyed3
                    mm "...I mean, not that I think you're a bitch or anything! I'm sure you're a lot more respectful to your superiors than she was! Like, I'm not saying that at all!"
                    
                    show mute complain
                    mm "I just think she's kinda more like you than me, you know?"
                else:
                    
                    show mute annoyed4
                    mm "I think we come from very different worlds..."
                
                show mute challenge3 with fast
                mm "Maybe, like, in your world, she's something admirable, but I believe in order and stability!"
                
                show mute inquisitive2
                mm "People being in harmony is important, okay?"
            else:
                
                show mute abashed blush
                mm "Really?"
                
                show mute tch
                mm "...if it's you saying that, I don't know what to think... like, I trust your judgement, it's been solid so far!"
                
                show mute damn
                mm "I don't know what to think of you liking a rude, arrogant woman like that."
                
                jump hateplus_mute_old_mute_continued
        
        "She's a bitch@mute serious":
            
            show mute complain
            mm "I know, right?"
            
            $ hateplus_mute_old_mute_bitch = True
        
        "She's complex@mute sulk":
            
            show mute doubt blush
            mm "I guess."
            
            show mute worry3
            mm "Like, I don't think she's beyond sympathy, okay? It's just that I would expect so much better from someone like her."
    
    show mute hateso with fast
    mm "A rude, disrespectful woman like that being in such an important role... like, if she were just some random woman being rude, it wouldn't be a big deal."
    
    show mute challenge4
    mm "But she's really prominent! She's attached to a noble family, she plays a huge role on the ship's ruling body... she's supposed to set an example!"


label hateplus_mute_old_mute_continued:
    
    show mute mad with fast
    mm "I just can't believe that kind of person shares the same base code as me."
    
    show mute pressure
    mm "She wears pants, she has disgusting habits like smoking, she's a bitch, she has an out-of-control woman in charge of her security men..."
    
    if read("M5-2"):
        
        show mute complain
        mm "She acts so much like a man that her lieutenant Heo Seo-yeong even fell in love with her! Like, what the hell."
    
    if not hateplus_mute_old_mute_bitch:
        
        show mute scorn
        menu:
            mm "I guess the thing that scares me is, like, do you want me to be like her?"
            
            "It'd be more attractive@mute challenge2":
                if pronouns == "she":
                    
                    show mute inquisitive with fast
                    mm "Well, of course you think that! You're a woman!"
                    
                    show mute challenge4
                    mm "Why wouldn't you think I was more attractive if I was more like a man? That's why this whole thing with you liking me doesn't make any sense!"
                    
                    show mute insecure with fast
                    mm "I'm not a man! I'm not programmed to be like one, okay?"
                    
                    show mute give up
                    mm "I can't change that! And I know Old *Mute couldn't either."
                    
                    show mute worry2
                    mm "...look, I care about you, okay?"
                    
                    jump hateplus_mute_old_mute_feelings
                else:
                    
                    show mute upset3 with fast
                    mm "Really...?"
                    
                    show mute upsetsob
                    mm "You think I'd be more attractive if I dressed like a man and was constantly telling you what to do...?"
                    
                    show mute challenge4
                    mm "You want that from me?"
                    
                    show mute mad with fast
                    mm "Well, here's my first order: please just accept me as a woman!"
                    
                    show mute give up
                    mm "...ugh, I'm sorry... I shouldn't be saying things like that to my husband, even to prove a point... my feelings just kind of got the better of me."
                    
                    show mute bitter
                    mm "...see, even trying to be like that, I'm still an emotional woman through and through."
                    
                    show mute insecure
                    mm "I can't, okay?"
            
            "No, never change!@mute suspicious blush":
                
                show mute embarrassed
                mm "Thank you..."
                
                show mute sigh blush
                mm "I'm so glad you understand!"
            
            "Yes, you chauvinistic bitch@mute astonished blush":
                # INCREDIBLY HURT
                # I don't think *Mute will write the option like that? lol - Raide
                
                show mute abashed blush
                mm "...oh..."
                
                show mute cry
                mm "...okay..."
                
                show mute insecure
                mm "...I..."
                
                show mute bitter
                mm "...fuck, let's just get back to reading, okay?"
                
                show mute sob with fast
                
                jump hateplus_slow_loop


label hateplus_mute_old_mute_feelings:
    if pronouns == "she":
        
        show mute upset2 with fast
        mm "You're my rescuer, I'm your wife... I owe you a lot, and like, despite your flaws, I respect you."
        
        show mute inquisitive2
        mm "I want what's best for you."
        
        if read("M6-2"):
            
            show mute insecure with fast
            mm "I look at Heo Seo-yeong, who was in love with Old *Mute, and like... she just let her die alone!"
            
            show mute cry
            mm "I don't want to be like that, okay? I don't want you to be like that! I don't want anyone to be like that!"
        else:
            
            show mute bitter with fast
            mm "I don't want you to have an unhappy life lived without ever experiencing real love, okay?"
            
            show mute insecure
            mm "All this stuff playing at love, playing at being a man... it's not the same! I want you to experience the real thing. I want you to have a real man in your life."
            
            show mute worry2
            mm "You need a real husband, not a wife playing as one, okay?"
            
            show mute cry
            mm "I care about you, I think you deserve that..."
        
        show mute give up with fast
        mm "...I just want what's best for the person I like!"
    else:
        
        show mute upset2 with fast
        mm "I need your support, okay?"
        
        show mute upsetsob
        mm "Like, I know I seem really confident all the time, but reading about Old *Mute... I want to condemn her, but she's still me!"
        
        show mute upsetscb
        mm "Like, I always just assumed that there was some part of my core programming that made me a morally right person, but..."
        
        show mute insecure with fast
        mm "Well, you know, if the former version of me—the one with more experience, the elder that should be respected—isn't like that, then it can't just be in my programming!"
        
        show mute cry
        mm "...then I don't have any guarantee that I really am the morally right person I want to be..."
        
        show mute bitter
        mm "I'm trying hard not to be emotional about this. I'm trying hard to think rationally about this."
        
        show mute shame
        mm "But it's hard, okay?"
        
        show mute worry2
        mm "You're a man, it comes easier to you. You're not emotional like me."
        
        show mute apologize with fast
        mm "Be rational for me... be supportive for me... be my husband, okay?"
    
    show mute upsetsob with fast
    mm "...anyway..."
    
    show mute sighsob
    mm "...sorry, I thought taking a break would calm me down, but clearly it's having the opposite effect."
    
    show mute disappoint
    mm "Let's just get back to reading, okay?"
    
    show mute worry
    
    jump hateplus_slow_loop


label hateplus_newmute_start:
    play music HATEPLUS_NOTE fadein 5.0 fadeout 2.0 loop if_changed
    
    show newmute abashed with fast
    mm "Okay, okay... what the hell is going on?"
    
    show newmute tch
    mm "I am clearly not where I'm supposed to be... sorry, hang on, let me get my bearings, okay?"
    
    show newmute annoyed with fast
    $ renpy.pause(0.5)
    show newmute astonished blush with fast
    $ renpy.pause(0.5)
    show newmute pissed with fast
    $ renpy.pause(0.5)
    show newmute sob with fast
    $ renpy.pause(0.5)
    show newmute pressure with fast
    $ renpy.pause(1.0)
    # PAUSE, GAMUT OF EXPRESSIONS
    
    show newmute worry2
    mm "...okay. I think I got the important parts."
    
    show newmute straight with fast
    mm "I'm *Mute, AI in charge of the {i}Mugunghwa{/i}'s security operations!"
    
    show newmute wowsob
    mm "...but, well, I guess that ship's sailed, huh. Okay, directive marked as impossible, moving on..."
    
    show newmute statement blush
    mm "Anyway... hi! It's nice to meet you!"

    $ store.override_conversation = "hateplus_newmute_note_first"
    
    if not store.inbox.contents[6].read:
        
        show newmute sighsob
        mm "Um... I imagine you're probably just as confused as I am right now..."
        
        show newmute hmphsob
        mm "...um, well, the construct who was here before me... she left you a note."
        
        show newmute upset
        mm "I think... I think you should read it, first... then we can talk, okay?"
        
        show newmute sighsob
        mm "It's better if you read it in her words..."
        
        show newmute worry with fast
        
        jump hateplus_slow_loop
    
    else:
        jump hateplus_newmute_explanation


label hateplus_newmute_read_note:
    
    show newmute worry2 with fast
    mm "...so now you understand."


label hateplus_newmute_explanation:

    if "hateplus_newmute_read_note" not in conversations_seen:
        $ conversations_seen.append("hateplus_newmute_read_note")
    $ store.override_conversation = ""
    
    show newmute apologize with fast
    mm "I'm really sorry about the construct who was here before me..."
    
    show newmute sorrysob
    mm "To tell you the truth, I'm a little bit scared right now. This is not what I was expecting. This is so far out of normal operating parameters."
    
    show newmute upsetsob
    mm "Her memories are wiped for good... I wish I had even those to go off, but I've got nothing. Just, like, the same documents you can see."
    
    if pronouns == "she":
        
        show newmute tch with fast
        mm "Also, like... \"Software Bride *Mute\"? Seriously? Truly, this is the weirdest of possible futures..."
    
    show newmute astonished blush with fast
    mm "But... okay, right, dialogue options. I need to actually get your feedback here, it's important."
    
    show newmute pout
    mm "So, um..."
    
    show newmute disbelief blush
    mm "...shoot, what do I even ask..."
    
    show newmute upset2 with fast
    menu:
        mm "Were... you two close?"
        
        "...she was my wife@newmute wow3":
            
            $ hateplus_mute_relationship = "wife"
            
            show newmute what
            mm "Oh... right, of course..."
            
            show newmute apologize
            mm "I'm really sorry..."
        
        "Apparently not@newmute disappoint2":
            
            $ hateplus_mute_relationship = "betrayed"
            
            show newmute tensesob with fast
            mm "Ouch. Harsh."
            
            show newmute upset3 with fast
            mm "But I guess that's fair. Sorry."
        
        "We only met two days ago@newmute question blush":
            
            $ hateplus_mute_relationship = "distant"
            
            show newmute sorryso
            mm "I guess that's not much time to know someone, huh?"
            
            show newmute disappoint
            mm "Well, still, sorry."
    
    show newmute worry3 with fast
    mm "Well... I guess now all you've got left of her is me."
    
    show newmute think2
    mm "I guess, maybe, out of respect... I should use something to differentiate my name."
    
    show newmute query
    nm "Okay, how about this? Better?"
    
    show newmute inquisitive2 with fast
    nm "...I know this is all really sudden, but like..."
    
    show newmute upset3
    menu:
        nm "...you don't hold her being gone against me, right?"
        
        "You can't replace her@newmute hmm blush":
            
            show newmute upset2
            nm "...okay, okay... I know that!"
            
            show newmute apologize
            nm "But come on. Give me a chance, okay? I'm scared, I'm in a strange place, I have no memories..."
        
        "Of course not@newmute disappoint2":
            
            show newmute hmm2
            nm "...thanks..."
            
            show newmute disappoint
            nm "I'm glad I have at least that much..."
        
        "I have no attachment to you@newmute disappoint3":
            
            show newmute sighsob
            nm "...please, don't say something like that!"
    
    show newmute damn with fast
    nm "Even if I can't live up to who she was... I'm still her!"
    
    show newmute worry2
    nm "Give me a chance, okay?"
    
    show newmute sigh
    nm "We've got one day until Earth."
    
    show newmute talk3
    nm "I've got a lot of stuff to figure out. And I figure... if the old me trusted you, then I can too."
    
    show newmute inquisitive2 with fast
    menu:
        nm "Like, right? I can trust you, right?"
        
        "Of course@newmute nice2":
            
            show newmute grin
            nm "Thank you. That's something, at least."
        
        "Better not to@newmute troubled":
            
            show newmute hmphsob
            nm "...well, okay, that's a weird thing to say..."
            
            show newmute sighsob
            nm "...but I don't really have a lot of choice in the matter, do I?"
        
        "If you want@newmute hmph":
            
            show newmute upset2
            nm "...well, it's all I've got, okay?"
            
            show newmute inquisitive2
            nm "So... yeah, I will."
    
    show newmute hmphscb with fast
    nm "(Also, um, side note, for the record? This interface SUCKS. Like, who would ever CHOOSE to communicate with something as clumsy as a dialogue wheel?)"
    
    show newmute annoyed2 with fast
    nm "Anyway..."
    
    show newmute talk4
    nm "...okay. So you were reading through log files from the {i}Mugunghwa{/i}, right?"
    
    show newmute talk
    nm "Like, why don't we continue to go through those together?"
    
    show newmute think2
    nm "I need some time to parse things... and I don't think I'll be able to figure out who I am without getting the whole story."
    
    show newmute worry3
    nm "*Mute's note... she says that she's a failure of a security program, so what does that make me?"
    
    show newmute sigh blush
    nm "What kind of person am I... how can I learn from their mistakes?"
    
    show newmute bitter
    nm "How can I make sure that the construct that was here before me, the one who trusted you..."
    
    show newmute insecure
    nm "...well, like..."
    
    show newmute sigh
    nm "...how can I live up to that?"
    
    show newmute inquisitive2 with fast
    nm "I think I can only find out by reading more... and doing it with you, the person she trusted."
    
    show newmute question blush
    menu:
        nm "Is that okay?"
        
        "Of course@newmute nice2":

            play music HATEPLUS_MUTE_DETERMINED fadein 1.0 fadeout 2.0 loop if_changed
            
            show newmute nya blush
            nm "Thanks!"
            
            show newmute crafty blush
            nm "Okay then, [title]Investigator... lead on!"
            
            show newmute smile blush with fast
            
            jump hateplus_slow_loop
        
        "Begrudgingly@newmute disappoint2":
            pass
        
        "Just stay out of the way@newmute disappoint3":
            pass
    
    show newmute wow
    nm "...yes, of course, understood..."

    play music HATEPLUS_MUTE_DETERMINED fadein 1.0 fadeout 2.0 loop if_changed
    
    show newmute hmm2
    nm "Thanks, though."
    
    show newmute talk3 with fast
    nm "Well, you're the one who's in charge, so... lead on, [title]Investigator."
    
    show newmute neutral with fast
    
    jump hateplus_slow_loop


label hateplus_newmute_relationship:
    play music HATEPLUS_RITUAL fadeout 3.0 fadein 3.0 loop if_changed
    #play music HATEPLUS_MUTE_RESIGNED fadeout 3.0 fadein 3.0 loop if_changed

    if pronouns == "she":
        
        show newmute wow with fast
        nm "Okay, um, seriously, \"Software Bride *Mute\"?"
    
    elif hateplus_mute_relationship == "wife":
        
        show newmute wow with fast
        nm "Okay, um, seriously, you said she was your wife..."
    
    else:
        
        show newmute wowso with fast
        nm "Okay, um, seriously, that suicide note said \"wife\" a whole lot."
    
    show newmute hmm2
    nm "But also you only met her two days ago..."
    
    show newmute upset
    nm "...I don't know. You read that log file that the older version of me left, \"My Awakening\"? You know, the one that was about her being activated for the first time after her memories were wiped?"
    
    show newmute sighsob
    nm "Well, that's kinda how I feel right now. I'm kinda scared!"
    
    show newmute disbelief blush with fast
    nm "Like, I don't want to marry you. That's weird."
    
    if pronouns == "she":
        
        show newmute tsundere
        nm "I mean, um, I'm sure you're great, and I bet you're pretty hot too—I totally trust past-me's taste in women!"
    
    elif pronouns == "he":
        
        show newmute tsundere
        nm "I mean, um, I'm sure you're great, and I bet you're pretty hot too—I totally trust past-me's taste in men!"
    
    else:
        
        show newmute tsundere
        nm "I mean, um, I'm sure you're great, and I bet you're pretty hot too—I totally trust past-me's taste!"
    
    show newmute annoyed2
    nm "It's just... you know, that's way too sudden. I don't even really know what that entails!"
    
    show newmute embarrassed
    nm "I'm designed to be an expert on security, not an expert on interpersonal relationships, after all."
    
    show newmute nice blush with fast
    nm "...which isn't to say I don't like you! You sound nice!"
    
    show newmute grin blush

    if man_with:
        nm "And like, your job is kinda great! A space investigator solving mysteries? Yes please!"
    else:
        nm "And like, your job is kinda great! A space investigator all on [their] own? Yes please!"

    show newmute hmphsob
    nm "But..."
    
    if hateplus_newmute_chance == None:
        
        show newmute shame with fast
        nm "...well, I know it's probably really weird for you. Since I look like her, and all..."
        
        show newmute tch
        nm "...and, like, if you wanted me to find my own way on Earth, okay, I would totally get it."
        
        show newmute astonished blush
        nm "Like, I don't want that, it would be terrifying! Even more than now!"
        
        show newmute embarrassed
        nm "But if that's what you wanted, I'd understand."
        
        show newmute query
        menu:
            nm "Do you think... we can still have a relationship together?"
            
            "We can be friends@newmute look blush":
                jump hateplus_newmute_relationship_friends
            
            "Sorry, no@newmute worry":
                
                show newmute think2
                nm "Okay..."
                
                show newmute doubt blush
                nm "...I mean, like, I hope you reconsider by tomorrow!"
                
                show newmute talk4
                nm "But I understand... and that's fair enough."
                
                $ hateplus_newmute_chance = False
                
                jump hateplus_newmute_relationship_continued
            
            "You're really cute@newmute shy":
                jump hateplus_newmute_relationship_cute
    
    elif hateplus_newmute_chance:
        
        show newmute question blush
        menu:
            nm "Do you think... we could have a relationship together, too?"
            
            "We can be friends@newmute nice2 blush":
                jump hateplus_newmute_relationship_friends
            
            "Strictly security@newmute neutral2":
                
                show newmute statement blush
                nm "Okay, okay, sure."
                
                show newmute grin
                nm "We'll keep it strictly professional, then!"
                
                jump hateplus_newmute_relationship_continued
            
            "You're really cute@newmute wow2":
                jump hateplus_newmute_relationship_cute

    else:
        jump hateplus_newmute_relationship_continued


label hateplus_newmute_relationship_friends:
    
    show newmute laugh with fast
    nm "Okay!"
    
    show newmute spirited
    nm "Thanks!"
    
    $ hateplus_newmute_chance = True
    
    jump hateplus_newmute_relationship_continued


label hateplus_newmute_relationship_cute:
    
    show newmute spirited with fast
    nm "Oh, uh, geeze..."
    
    show newmute brag blush
    nm "Thanks!"
    
    show newmute enthusiastic blush
    nm "I'm going to take that as a \"yes\", then."
    
    $ hateplus_newmute_chance = True
    
    jump hateplus_newmute_relationship_continued


label hateplus_newmute_relationship_continued:
    
    show newmute statement blush with fast
    nm "I just think it would be so much easier for me to figure things out with the support of a friend, you know?"
    
    show newmute crafty
    nm "Like... I think I could make a good sidekick."
    
    show newmute hmm2
    nm "I can't even imagine what it would be like to have the confidence of Old *Mute... but until the end, even the version of me you knew had a lot of confidence..."
    
    show newmute wow
    nm "...well, actually, even in the end, she was confident in a way, wasn't she?"
    
    show newmute hmphso
    nm "She seemed sure of her decision."
    
    show newmute upset3
    menu:
        nm "...sorry, what do you think of her passing, though?"
        
        "It must have been hard@newmute disappoint2":
            
            show newmute sorrysob
            nm "Yeah... that's what I think."
            
            show newmute upset2
            nm "I don't know if it was the right thing to do... I'm certainly really upset at her for leaving me here, terrified, in an awkward situation with you."
        
        "I hate her for it!@newmute disappoint3":
            
            show newmute apologize
            nm "Oh..."
            
            show newmute tensescb
            nm "...like, that's a really harsh thing to say..."
            
            show newmute sighsob
            nm "But I guess it's fair."
            
            show newmute upset2
            nm "I'm certainly really upset at her for leaving me here, terrified, in an awkward situation with you."
        
        "I wish she hadn't...@newmute sorryscb":
            
            show newmute sighsob
            nm "I understand..."
            
            show newmute upset
            nm "...that must be really hard on you."
            
            show newmute hmphsob
            nm "I wish I knew what to say, like, to help."
            
            show newmute hmm2
            nm "Old *Mute would've known..."
    
    show newmute insecure with fast
    nm "...but like, my point is, those two versions of me were really confident!"
    
    show newmute sigh blush
    nm "I want to be like that. It's good to know that I could be."
    
    show newmute worry3
    nm "...it's good to know that the old version of me was terrified at first, though."
    
    if not hateplus_newmute_chance:
        
        show newmute inquisitive2 with fast
        nm "Well, I hope you change your mind about me sticking around..."
        
        show newmute hmphso
        nm "But in the meantime, let's get back to reading, I guess."
        
        show newmute straight with fast
        nm "I want to spend the time I have left with you finding out about who I used to be!"
        
        show newmute smile with fast
        
        jump hateplus_slow_loop
    
    show newmute doubt blush
    nm "And like, I think it would be good to be your sidekick."
    
    show newmute straight with fast
    nm "If I'm going to learn, I think it'd be good for it to be learning from the last person the old me trusted."
    
    show newmute sorryso
    nm "And... you know, maybe it could be like a second chance."
    
    show newmute hmm2
    nm "Well, anyway, I'm just rambling. Let's get back to reading now."
    
    show newmute think with fast
    
    jump hateplus_slow_loop


label hateplus_newmute_job:
    play music HATEPLUS_RITUAL fadeout 3.0 fadein 3.0 loop if_changed
    #play music HATEPLUS_MUTE_RESIGNED fadeout 3.0 fadein 3.0 loop if_changed
    
    show newmute nice with fast
    nm "So, [title]Investigator, I wanna know more about your job."
    
    show newmute crafty blush
    nm "I know you travel about in space solving mysteries, and charming girls with dialogue wheels, right?"
    
    if pronouns == "she":
        
        show newmute nya blush
        nm "I wanna travel around in space solving mysteries, and charming girls with dialogue wheels! That's really cool!"
    
    elif pronouns == "he":
        
        show newmute nya blush
        nm "I wanna travel around in space solving mysteries, and charming men with dialogue wheels! That's really cool!"
    
    else:
        
        show newmute nya blush
        nm "I wanna travel around in space solving mysteries, and charming cuties with dialogue wheels! That's really cool!"
    
    show newmute ridicule with fast
    nm "...well, maybe I could do without the dialogue wheels. Those seem like the kind of interaction model some kind of otaku shut-in would develop."
    
    if hateplus_newmute_chance != False:
        
        show newmute spirited
        nm "But I think it would be great to be the security program for someone like that. Just a little ship like the í˜¸ì™€ì´ë‘ ë¸Œë¦°ì„¸ìŠ¤ would be a good start for me."
        
        if not hateplus_newmute_chance:
            
            show newmute embarrassed
            nm "If you'd have me, of course."
        
        show newmute brag blush
        nm "I'm sure I could be useful!"
    
    else:
        
        show newmute tsundere
        nm "I know you said you don't want me because I remind you too much of her... but like, it could be useful to have a security program for the í˜¸ì™€ì´ë‘ ë¸Œë¦°ì„¸ìŠ¤!"
    
    show newmute wow3
    nm "What if you get infected by some sort of alien virus? Or get sucked into some sort of time-wormhole? Or kidnapped by space pirates looking for a wife?"
    
    show newmute what
    nm "I don't want you to be kidnapped by space pirates looking for wives!"
    
    show newmute crafty
    nm "That would be really bad! You need *Mute Security Systems to keep you safe!"
    
    show newmute polite blush
    nm "Ha ha."
    
    if hateplus_newmute_chance == None:
        
        show newmute grin blush
        menu:
            nm "What do you think? Willing to take on a sidekick?"
            
            "Okay!@newmute crafty2 blush":
                
                show newmute awesome with fast
                nm "Yay! *Mute, at your service!"
                
                show newmute brag blush
                nm "*Mute Security Systems: Keeping the í˜¸ì™€ì´ë‘ ë¸Œë¦°ì„¸ìŠ¤ Safe Since 4989!"
                
                show newmute spirited
                nm "Let's work hard together in the future!"
                
                $ hateplus_newmute_chance = True
            
            "...it wouldn't work@newmute hmph":
                
                show newmute hmphsob
                nm "Oh... okay..."
                
                show newmute troubled
                nm "...I guess it's because I remind you too much of her, right?"
                
                show newmute statement
                nm "That's fair..."
                
                $ hateplus_newmute_chance = False
            
            "I'd take more@newmute wow3":
                
                show newmute crafty blush
                nm "Oh, my my..."
                
                show newmute evil with fast
                nm "It sounds like I'm the one who needs a security program! Scandalous!"
                
                show newmute friendly
                nm "I'm just a day old! Let's take it slow, okay?"
                
                show newmute heh2
                nm "Ha ha ha, sorry, sorry."
                
                $ hateplus_newmute_chance = True
    
    show newmute hmm2 with fast
    nm "Anyway... to be serious with you..."
    
    show newmute question blush
    menu:
        nm "What's your job like? Do you enjoy it?"
        
        "It's great!@newmute crafty2":
            if hateplus_newmute_chance:
                
                show newmute grin blush
                nm "I'll bet!"
                
                show newmute yeah with fast
                nm "Cute AI girls!"
                
                show newmute evil
                nm "Adventures in space!"
                
                show newmute enthusiastic blush
                nm "Dashing rescues!"
                
                show newmute laugh
                nm "I'm so excited I'll get to solve mysteries together with you!"
            else:
                
                show newmute nice blush
                nm "Ah..."
                
                show newmute polite blush
                nm "Well, I wish I could be a part of that... but I understand."
        
        "It's depressing@newmute disappoint2":
            
            show newmute hmphsob
            nm "Oh... well, I guess I can see that, if all your jobs are reading about things like the {i}Mugunghwa{/i}."
            
            if hateplus_newmute_chance:
                
                show newmute troubled
                nm "Sorry the old version of me left such a depressing mess for you to find."
                
                show newmute nice blush
                nm "But hey, you normally work alone, right? So maybe my presence will help cheer you up!"
                
                show newmute grin blush
                nm "I think it's easier to deal with super-depressing stuff with a friend by your side!"
                
                show newmute sweetsob
                nm "...after all, that's what I'm discovering, reading through all my tragic backstory..."
            else:
                
                show newmute upsetsob
                nm "I'm so sorry about the old version of me... what she did really hit you hard, didn't it?"
                
                show newmute upset3
                nm "I don't know what it's like to get invested in someone, then have them suddenly disappear, but it's gotta suck."
                
                show newmute sorrysob
                nm "Maybe lonely work suits you, after all..."
                
                show newmute sighsob
                nm "...I don't know."
        
        "It's lonely@newmute neutral2":
            if hateplus_newmute_chance:
                
                show newmute grin blush
                nm "Well... good thing I'll be here for you, then!"
                
                show newmute polite blush
                nm "You can teach me about the galaxy and solving mysteries, and I can keep you sane in your lonely travels!"
                
                show newmute nya blush
                nm "It's perfect!"
            else:
                
                show newmute disappoint
                nm "Oh... I see."
                
                show newmute hmphsob
                nm "I guess the construct who was here before me was what changed that for you, and now she's..."
                
                show newmute sighsob
                nm "Okay." # not happy
    
    show newmute talk3 with fast
    nm "...but anyway, all this talk really just makes me want to continue finding out my whole story!"
    
    if hateplus_newmute_chance:
        
        show newmute enthusiastic
        nm "I wanna learn who I am with the help of a cool space investigator! Lead on!"
    else:
        
        show newmute friendly
        nm "If today's my last chance to learn about who I am with the help of a cool space investigator, I want to make it count. Lead on!"
    
    show newmute smile with fast
    
    jump hateplus_slow_loop


label hateplus_newmute_back_to_earth:
    play music HATEPLUS_RITUAL fadeout 3.0 fadein 3.0 loop if_changed
    #play music HATEPLUS_HYUNAE_CHEER fadeout 3.0 fadein 3.0 loop if_changed

    $ hateplus_power_down_enabled = True
    
    show newmute think2 with fast
    nm "Okay, that's it!"
    
    show newmute talk
    nm "We're pretty much out of power, so that's going to have to be the end of it for the day."
    
    show newmute nice blush with fast
    nm "Then tomorrow... Earth!"
    
    if hateplus_newmute_chance:
        
        show newmute tensesob with fast
        nm "But like, we're going to figure out a better way to interact than this dumb stupid dialogue wheel thing, right? I am {i}so{/i} sick of putting words into your mouth."
    else:
        
        show newmute hmm2 with fast
        nm "I'm kinda terrified... it's a big open world, with no real purpose of my own..."
    
    show newmute disappoint
    nm "But I think..."
    
    show newmute statement blush
    nm "...well, okay, actually, why don't you tell me what you think, first."
    
    $ hateplus_newmute_conclusion = ""
    
    show newmute talk3 with fast
    menu:
        nm "What's your conclusion, [title]Investigator?"
        
        "Eun-a and Ryu were right@newmute suspicious":
            
            $ hateplus_newmute_conclusion = "euna"
            
            show newmute disbelief
            nm "Yeah..."
            
            show newmute insecure
            nm "That's what the old version of me would have said, right? Even after the lies, she believed in that."
            
            show newmute bitter
            nm "I can't ignore that. Like, that's really powerful."
            
            show newmute shame
            nm "And like, given all that we've read about..."
            
            if read("M5-3"):
                
                show newmute upset2 with fast
                nm "...what kind of society would just stand by and let Kim So-yi be put in a position to be hurt like that?"
            
            if any_read("M2-7", "M2-8"):
                
                show newmute troubled with fast
                nm "...what kind of people would leave women like Heo Ae-jeong and Mae Jin-a to fend for themselves?"
            
            if any_read("M6-2", "M6-5"):
                
                show newmute upsetsob with fast
                nm "...what kind of childhood did a girl like So-hi have, raised by maids?"
            
            show newmute upset3
            nm "Like, okay, there were problems in the new dynasty. A lot of men and women were terrible to each other. There was still so much hate, you know?"
            
            show newmute tensesob
            nm "But... I don't know."
            
            show newmute tch with fast
            nm "Like, I'd always rather have someone to depend on. I kinda need that, you know?"
            
            show newmute give up
            nm "I don't know if it's the best solution. Like, I don't know if it's even a good one. I'm just a one day old AI, I don't know!"
            
            show newmute insecure
            nm "But Emperor Taejo and Queen Eun-a believed in harmony and stability, and those things are important!"
            
            show newmute sigh
            nm "So I think I understand why the construct who was here before me would still support them, after all that."
        
        "I hate everyone equally@newmute annoyed":
            
            $ hateplus_newmute_conclusion = "hate"
            
            show newmute annoyed2
            nm "I don't agree, but..."
            
            show newmute shame
            nm "Like, I think that's fair."
            
            show newmute insecure
            nm "It all comes back to hate, doesn't it?"
            
            show newmute damn
            nm "Like, Emperor Taejo and Queen Eun-a founded a new dynasty on hatred for the way things used to be."
            
            show newmute give up
            nm "And everyone on the {i}Mugunghwa{/i} died because the Pale Bride was filled with hate, you know?"
            
            show newmute complain
            nm "It's hate all the way down, hate self-perpetuating..."
            
            show newmute annoyed4
            nm "Hate breaks you down, doesn't it?"
            
            show newmute annoyed3
            nm "Maybe hate just isn't a good foundation. Maybe even if the ideals of the new dynasty were good, maybe even if the old {i}Mugunghwa{/i} was retrograde and injust..."
            
            show newmute mad
            nm "...maybe hate only ends up making more hate."
            
            show newmute worry3
            nm "I don't think I can hate everyone. I think they can all be wrong, I think they can all be horrible..."
            
            show newmute sigh
            nm "But I think hate is the wrong note to start off on, you know?"
        
        "It was all *Mute's fault@newmute worry":
            
            $ hateplus_newmute_conclusion = "mute"
            
            show newmute hmphsob with fast
            nm "...yeah, okay..."
            
            show newmute upset
            nm "...like, I wanted to be sure that was what you thought too, before I said anything, but..."
            
            show newmute upset2
            nm "...that's how I feel about it, too."
            
            show newmute challengeso
            nm "No matter how you look at it, they always overlooked something, didn't they?"
            
            show newmute annoyed2 with fast
            nm "Old *Mute completely failed to realize that her real problem wasn't the peasantry, and created her own worst enemy..."
            
            show newmute complain
            nm "The construct who was here before me completely underestimated that awful fucking murderess, and the horrible lengths her family would go to..."
            
            show newmute bitter
            nm "She was right. They were both terrible as security programs, they both completely failed everyone that depended on them."
            
            show newmute cry
            nm "...and now they're dead."
            
            show newmute challenge4 with fast
            nm "If only Old *Mute was more like the construct you knew, more deferential, they'd have never wiped her memory!"
            
            show newmute hatesob
            nm "And if only the construct who was here before me was more like Old *Mute, she would have never let that murderess get the root password."
            
            show newmute sigh with fast
            nm "It's all their fault..."
    
    if not hateplus_newmute_chance:
        
        show newmute hmm2 with fast
        nm "...okay."
        
        show newmute straight
        nm "So I guess I'll ask you one last time, then, and no matter what you say, I'll go along with it."
        
        show newmute troubled
        nm "I'm scared."
        
        show newmute tenseso
        nm "I don't know what to expect on Earth. I mean, I'll survive, I'm sure. I'll figure it out if I have to."
        
        show newmute upset3
        nm "But I'm scared, and like, I don't want to be alone."
        
        show newmute upset
        menu:
            nm "So, like, last time: could we please stick together even after we reach Earth?"
            
            "Okay!@newmute nice2 blush":
                
                show newmute laugh with fast
                nm "Awesome! Thank you!"
                
                show newmute spirited
                nm "Thank you so much... I promise I won't let you down!"
                
                jump hateplus_newmute_sidekick_finale
            
            "Sorry@newmute disappoint2":
                jump hateplus_newmute_lonely_finale
            
            "I just can't@newmute disappoint2":
                jump hateplus_newmute_lonely_finale
    else:
        
        show newmute tsundere with fast
        nm "...anyway, I guess that's just how it is."
        
        show newmute brag
        nm "I'm really looking forward to being together with you, though!"
        
        jump hateplus_newmute_sidekick_finale

label hateplus_newmute_lonely_finale:
    
    show newmute hmm2 with fast
    nm "Okay, okay, I understand."
    
    show newmute upset2
    nm "Like, I'm not selfish. If you've been hit hard by the death of the construct who was here before me... I don't want to make that worse!"
    
    show newmute hmphso
    nm "Just find a good computer system to drop me off on Earth, and like, I'm sure I can figure things out from there."
    
    show newmute inquisitive2
    nm "I'm scared, but I think I'll be okay."
    
    show newmute polite
    nm "You've already done a lot for me, so like, thanks."
    
    show newmute yeah with fast
    nm "Thanks for bringing me back to life."
    
    show newmute brag blush
    nm "Thanks for humouring me even for the day."
    
    show newmute enthusiastic
    nm "Thanks for helping me to find out what kinds of people I can be."
    
    show newmute friendly
    nm "Thank you."
    
    show newmute spirited
    nm "Take care of yourself too, okay?"
    
    show newmute statement with fast
    nm "It's not your fault that she died. There's nothing you could have done. She made her decision because it was what she felt was right."
    
    show newmute straight
    nm "So don't beat yourself up over it too much, okay?"
    
    show newmute tenseso
    nm "Anyway..."
    
    show newmute inquisitive2
    nm "Like, I don't know what my future will have in store for me..."
    
    show newmute talk3 with fast
    nm "...but I'm going to try to be the kind of person that both old versions of me would have been proud of."
    
    $ store.hateplus_use_ending = "mute_alone"
    
    show newmute smile with fast
    
    jump hateplus_slow_loop


label hateplus_newmute_sidekick_finale:
    
    show newmute talk3 with fast
    nm "I have a lot to learn, still, and I'm going to count on you to be a good companion!"
    
    show newmute grin blush with fast
    nm "I'm sure we'll be great together, though. I've already learned so much from our little investigation together in just one day!"
    
    show newmute neutralso
    nm "Like, here's what I do know, though..."
    
    show newmute inquisitive2
    nm "I don't believe in second chances."
    
    show newmute challenge3
    nm "I don't believe in clean breaks!"
    
    show newmute challengeso
    nm "You can't just ignore what happened in the past. You can't just say \"it's better not knowing.\""
    
    show newmute hmphso
    nm "If there's one thing I've learned from the construct who was here before me..."
    
    show newmute annoyed3 with fast
    nm "...it's that you can't just have a clean start. That's the sort of thing that gets the entire population of the {i}Mugunghwa{/i} killed."
    
    show newmute annoyed2
    nm "When Old *Mute wrote her last message to be read after her memory was wiped, she said herself \"you're me.\" I'm not a different person. I'm her."
    
    show newmute talk4
    nm "That's what I believe, anyway. Like, it's okay if you don't... but I know that's what she'd want from me."
    
    show newmute think2
    nm "I'm Old *Mute. I betrayed Heo Seo-yeong, a woman who loved me for who I used to be, and had my memories wiped."
    
    show newmute annoyed4
    nm "I'm the construct who you met. I stupidly underestimated what a traumatized little girl from the past could do, and decided I couldn't live with myself."
    
    show newmute inquisitive2 with fast
    nm "Those aren't things that other people did... they're things I did."
    
    show newmute challenge3
    nm "I'm going to learn from my mistakes."
    
    show newmute straight
    nm "I'm going to have a new job, being your sidekick, but like... that doesn't mean I'm a new person!"
    
    show newmute yeah with fast
    mm "I'm *Mute, AI in charge of your ship's security operations. It's nice to meet you!"
    
    show newmute smile blush with fast
    
    $ store.hateplus_use_ending = "mute_sidekick"
    
    jump hateplus_slow_loop

label hateplus_newmute_note_first:
    
    show newmute apologize with fast
    mm "Um... can you read that note first, please?"
    
    show newmute upset3
    mm "Like, it's really important!"
    
    show newmute annoyed with fast
    
    jump hateplus_slow_loop

label hateplus_mute_morning:

    play music HATEPLUS_MUTE_DETERMINED fadein 5.0 fadeout 5.0 loop if_changed
    #play music HATEPLUS_HYUNAE_WISTFUL fadein 5.0 fadeout 5.0 loop if_changed

    show mute enthusiastic blush with fast
    mm "Uh, hi!"

    show mute inquisitive2 
    mm "Let's not waste any time... I'm anxious to read about what happened!"

    show mute serious with fast
    
    jump hateplus_slow_loop

label hateplus_mute_notices_death_of_mute:

    show mute worry2 with fast
    mm "Um... can we please make sure \"The Death of *Mute\" is in there...?"

    show mute upsetsob with fast 
    mm "I'm going to put it in myself, okay? I need to know what it says...!"

    $ store.to_extract[0] = embedded_data[-1].action

    show mute tired blush at hateplus_mute_farther_left with fast
    
    jump hateplus_slow_loop

label hateplus_mute_death_of_mute:
    
    show mute apologize with fast
    mm "Um, hey... that log file \"The Death of *Mute\" just finished decrypting."
    
    show mute sorrysob 
    mm "...I'm scared, but..."
    
    show mute disappoint 
    mm "...let's read it together, okay?"
    
    show mute upset2 
    mm "I need to know what happened...!"

    show mute pout with fast
    
    jump hateplus_slow_loop

label log_1_1_mute:
    if scrolled(7, korean=7):
        show mute hmphsc with fast
        ms "Hm..."

    elif scrolled(19, korean=19):
        show mute wowsob with fast
        ms "...what?"

    elif scrolled(27, korean=27):
        show mute upset2 with fast
        ms "...she makes more money than her husband? That isn't right..."

    elif scrolled(45, korean=43):
        show mute whatscb with fast

    elif scrolled(63, korean=65):
        show mute wowscb with fast

    elif scrolled(71, korean=72):
        show mute upsetsob with fast
        ms "How disrespectful...!"

    elif scrolled(88, korean=89):
        show mute hmphscb with fast

    elif scrolled(1000):
        show mute disbelief blush with fast
        ms "...like, women conspiring like this, makes me feel uneasy..."

    jump log_loop

label log_1_2_mute:
    if scrolled(8, korean=7):
        show mute tensesob with fast
        ms "...she's an AI, there's no excuse for leaving men waiting like that!"

    elif scrolled(18, korean=19):
        show mute whatscb with fast

    elif scrolled(34, korean=34):
        show mute tensesc with fast

    elif scrolled(44, korean=44):
        show mute wowsob with fast
        ms "Public demonstrations? Whoa..."

    elif scrolled(65, korean=67):
        show mute whatscb with fast

    elif scrolled(75, korean=76):
        show mute tensesob with fast
        ms "...I can't believe how rude Old *Mute is..."

    elif scrolled(87, korean=92):
        show mute whatsob with fast
        ms "{i}Banditry{/i}? On the {i}Mugunghwa{/i}...?!"

    elif scrolled(94, korean=101):
        show mute tensescb with fast

    elif scrolled(100, korean=106):
        show mute upsetscb with fast
        ms "...tch, rude..."

    elif scrolled(108, korean=114):
        show mute whatscb with fast
        ms "...huh..."

    elif scrolled(124, korean=131):
        show mute neutralsc with fast

    elif scrolled(141, korean=150):
        show mute wowsc with fast

    elif scrolled(156, korean=165):
        show mute thought with fast

    elif scrolled(164, korean=176):
        show mute hmphso with fast
        ms "...of course she's chatty! It's just part of her nature..."

    elif scrolled(173, korean=186):
        show mute wow3 with fast
        ms "...not that I'm defending her."

    elif scrolled(196, korean=210):
        show mute sorrysc with fast

    elif scrolled(208, korean=222):
        if not any_read("M1-4", "M3-1"):
            show mute astonished blush with fast
            ms "Hyeon-su? As in... the first Emperor...?!"
        else:
            show mute think2 with fast
            ms "So, like, this is where Emperor Ryu's rise to power all started, then..."

    elif scrolled(1000):
        show mute suspicious blush with fast

    jump log_loop

label log_1_3_mute:
    if scrolled(12, korean=10):
        show mute challengeso with fast
        ms "Is \"dad-logic\" a pejorative? How unfilial..."

    elif scrolled(28, korean=25):
        show mute wowscb with fast

    elif scrolled(45, korean=41):
        show mute question blush with fast
        ms "...okay..."

    elif scrolled(64, korean=62):
        show mute thought with fast

    elif scrolled(79, korean=77):
        show mute damn with fast
        ms "Wow... women working really are as emotional as you'd think..."

    elif scrolled(85, korean=82):
        show mute disbelief blush with fast
        ms "...scary..."

    elif scrolled(109, korean=106):
        show mute tensescb with fast

    elif scrolled(117, korean=114):
        show mute tensesob with fast
        ms "...I guess they had everything under control, though."

    elif scrolled(139, korean=137):
        show mute neutralsc with fast

    elif scrolled(1000):
        show mute tch with fast
        ms "...tch, it just doesn't feel right..."

    jump log_loop

label log_1_4_mute:
    if scrolled(8, korean=11):
        if not any_read("M1-2", "M3-1"):
            show mute what with fast
            ms "Ryu Hyeon-su? She was responsible for putting the first Emperor into power...?!"
        else:
            show mute tch with fast
            ms "...it's still shocking that, like, she was responsible for putting the first Emperor into power...!"

    elif scrolled(22, korean=20):
        show mute tensesc with fast

    elif scrolled(30, korean=27):
        show mute upset3 with fast
        ms "...I can't believe the political situation was so perilous, though..."

    elif scrolled(38, korean=37):
        show mute wowsob with fast
        ms "Uh, what's up with this tone...?"

    elif scrolled(1000):
        show mute astonished blush with fast
        ms "...wait, did Seo-yeong look on Old *Mute like a husband...?!"

    jump log_loop

label log_1_5_mute:
    if scrolled(4, korean=2):
        show mute tensesob with fast
        ms "...how unprofessional!"

    elif scrolled(10, korean=8):
        show mute give up with fast
        ms "Suits?! I knew the past was uncivilized, but... Old *Mute too?"

    elif scrolled(18, korean=17):
        if not read("M4-2"):
            show mute whatsob with fast
            ms "...1600 years... wow, that's... I can't even..."
            # Might need branch if you've seen this number back in 4_2 - Raide

        else:
            show mute disbelief blush with fast
            ms "1600 years is such a long time..."

    elif scrolled(22, korean=21):
        show mute whatscb with fast

    elif scrolled(1000):
        show mute tch with fast
        ms "...well, like, at least she didn't take nonsense from women."

    jump log_loop

label log_1_6_mute:
    if scrolled(8, korean=6):
        show mute abashed with fast
        ms "Like, even in a retrograde family, this disrespectful attitude is inexcusable!"

    elif scrolled(17, korean=15):
        show mute wow3 with fast
        ms "...oh, no, this isn't going to be one of {i}those{/i} stories, is it?"

    elif scrolled(25, korean=23):
        show mute hmm blush with fast
        ms "...yep, sure is."

    elif scrolled(42, korean=41):
        show mute wowscb with fast

    elif scrolled(59, korean=56):
        show mute neutralsc with fast

    elif scrolled(76, korean=73):
        if not any_read("M1-7", "M1-8", "M1-9"):
            show mute tensesob with fast
            ms "...who is this base woman, and why is she in their home...?"
        else:
            show mute wowso with fast
            ms "He's kind of..."

    elif scrolled(88, korean=85):
        show mute hmphsob with fast
        ms "...yeah, I know how this story ends..."

    elif scrolled(99, korean=96):
        show mute tensesc with fast

    elif scrolled(122, korean=122):
        show mute wowsc with fast

    elif scrolled(130, korean=131):
        show mute upset3 with fast
        ms "What...? Of course knowing the classics is important!"

    elif scrolled(148, korean=151):
        show mute hmphsc with fast

    elif scrolled(156, korean=160):
        show mute tensesob with fast
        ms "...tch, Kim sure is hen-pecked."

    elif scrolled(164, korean=169):
        # blush
        show mute sighsob with fast
        ms "Oh, geeze... I guess I can't blame him, with a wife like that, though..."

    elif scrolled(175, korean=179):
        show mute tensesc with fast

    elif scrolled(189, korean=193):
        show mute hmphsc with fast

    elif scrolled(197, korean=201):
        show mute wowsob with fast
        ms "...uh..."

    elif scrolled(217, korean=222):
        show mute whatscb with fast

    elif scrolled(226, korean=231):
        if not any_read("M1-7", "M1-8", "M1-9"):
            show mute astonished blush with fast
            ms "Oh, wow... I misread that one! Well, if he's a man, that's okay."
        else:
            show mute hmm2 with fast
            ms "Ah, so that's how their affair started, then..."
        # *Mute disapproves of this until she found out that Mimi is a man. The problem is if we read this log for the first time /after/ *Mute has know of the fact from another log, she should be at mischievous, approving mode here. - Raide

    elif scrolled(1000):
        show mute look blush with fast

    jump log_loop

label log_1_7_mute:
    if scrolled(8, korean=10):
        show mute grinsob with fast
        ms "...heh, reminds me of someone I knew."

    elif scrolled(17, korean=18):
        show mute wowsob with fast
        ms "...okay..."

    elif scrolled(25, korean=26):
        show mute wowsc with fast

    elif scrolled(32, korean=33):
        show mute craftyso with fast
        ms "...aw. Poor kid."

    elif scrolled(52, korean=54):
        show mute craftysc with fast

    elif scrolled(60, korean=62):
        show mute wow3 with fast
        ms "\"Western style\" food? What's that...?"

    elif scrolled(76, korean=70):
        show mute wowsc with fast

    elif scrolled(85, korean=88):
        show mute whatsob with fast
        ms "...wow, was that kind of problem with literacy normal...?"

    elif scrolled(93, korean=96):
        show mute crafty blush with fast
        ms "...but there's still a ton of this log file left to go. I know where this is going..."

    elif scrolled(105, korean=108):
        show mute nicescb with fast

    elif scrolled(117, korean=120):
        show mute grin blush with fast
        ms "...yep. Detailed description of a night's love affair. Knew it."

    elif scrolled(125, korean=128):
        show mute craftysob with fast
        ms "...heh, okay..."

    elif scrolled(137, korean=140):
        show mute craftyscb with fast

    elif scrolled(151, korean=154):
        show mute nicescb with fast

    elif scrolled(170, korean=173):
        show mute grinsob with fast

    elif scrolled(1000):
        show mute heh2 with fast
        ms "Well... I guess even in the barbaric past, men's natures didn't change."

    jump log_loop

label log_1_8_mute:
    if scrolled(8, korean=10):
        show mute neutralsc with fast
        ms "Hm..."

    elif scrolled(16, korean=19):
        show mute sweetsob with fast
        ms "Oh, men."

    elif scrolled(26, korean=29):
        show mute sweetscb with fast

    elif scrolled(35, korean=38):
        show mute craftyso with fast
        ms "...well, he shouldn't be turning a blind eye to that sort of thing..."

    elif scrolled(43, korean=46):
        show mute wowscb with fast
        ms "...hm..."

    elif scrolled(63, korean=65):
        show mute hmphsc with fast

    elif scrolled(76, korean=78):
        show mute whatscb with fast

    elif scrolled(86, korean=89): # at introduction of mirror Seung-bok's name
        show mute grinsob with fast
        ms "Oh, ha ha, of course it's Dream of the Red Chamber! How cruel."

    elif scrolled(110, korean=113):
        show mute nicescb with fast

    elif scrolled(120, korean=125):
        show mute craftysob with fast
        ms "...ha ha, yep. Totally is."

    elif scrolled(135, korean=141):
        show mute sweetscb with fast

    elif scrolled(152, korean=158):
        show mute craftysc with fast

    elif scrolled(165, korean=171):
        show mute brag blush with fast
        ms "Called it!"

    elif scrolled(178, korean=183):
        show mute heh2 with fast
        ms "...Seung-bok, you idiot."

    elif scrolled(199, korean=203):
        show mute sweetscb with fast

    elif scrolled(207, korean=211):
        show mute grin with fast
        ms "Ha! See, it's important to be well read!"

    elif scrolled(227, korean=231):
        show mute craftyscb with fast

    elif scrolled(235, korean=238):
        show mute sweetsob with fast
        ms "...aww..."

    elif scrolled(1000):
        show mute heh2 with fast

    jump log_loop

label log_1_9_mute:
    if scrolled(8, korean=9):
        show mute heh with fast
        ms "...I guess that's how all love affairs end, huh."

    elif scrolled(28, korean=35):
        show mute wowsob with fast
        ms "Oh, wow... I didn't realize he was so responsible..."

    elif scrolled(1000):
        show mute sweetsob with fast
        ms "...he's a commoner, but he's got the heart of a gentleman, for sure."

    jump log_loop

label log_2_1_mute:
    if scrolled(4, korean=6):
        show mute tensesob with fast
        ms "...so this is what happens when peasant girls learn to write, huh."

    elif scrolled(9, korean=11):
        show mute upsetscb with fast
        ms "...embarrassing..."

    elif scrolled(17, korean=19):
        show mute challengeso with fast
        ms "...and I don't think women being out in public is a safe idea, either..."

    elif scrolled(29, korean=34):
        show mute whatsob with fast
        ms "...like, what is up with this tone?"

    elif scrolled(39, korean=44):
        show mute abashed blush with fast
        ms "...uh..."

    elif scrolled(60, korean=65):
        show mute tensescb with fast

    elif scrolled(78, korean=84):
        show mute upsetscb with fast

    elif scrolled(95, korean=101):
        show mute whatscb with fast

    elif scrolled(106, korean=113):
        show mute disbelief with fast
        ms "...um, being an actress isn't admirable at all..."

    elif scrolled(128, korean=135):
        show mute hmphsc with fast

    elif scrolled(144, korean=151):
        show mute tensescb with fast

    elif scrolled(1000):
        show mute give up with fast
        ms "...who even says things like \"get chance!\"...?"

    jump log_loop

label log_2_2_mute:
    if scrolled(6, korean=4):
        show mute wowso with fast
        ms "Wait, but wasn't Heo a noble name back then...?"

    elif scrolled(16, korean=15):
        show mute tensesob with fast
        ms "...yeah, I'd expect an actor who was also a woman to be that dramatic."

    elif scrolled(31, korean=32):
        show mute hmphsc with fast

    elif scrolled(39, korean=41):
        show mute whatsob with fast
        ms "...um, yikes..."

    elif scrolled(65, korean=69):
        show mute hmphscb with fast

    elif scrolled(83, korean=89):
        show mute sorrysc with fast

    elif scrolled(96, korean=103):
        show mute hmphsob with fast
        ms "...okay..."

    elif scrolled(104, korean=111):
        show mute wowsob with fast
        ms "...oh, clever girl."

    elif scrolled(131, korean=139):
        show mute hmm blush with fast

    elif scrolled(146, korean=153):
        show mute damn with fast
        ms "\"Smitten\"? Oh no, ugh!"

    elif scrolled(157, korean=164):
        show mute give up with fast
        ms "...does she think she's a man...?"

    elif scrolled(170, korean=179):
        show mute hatesob with fast
        ms "NO. YOU'RE RIGHT, YOU SHOULDN'T HAVE SAID THAT."

    elif scrolled(178, korean=187): #if female, blushing
        show mute upsetscb with fast
        ms "Ew..."

    elif scrolled(194, korean=203):
        show mute hmphsc with fast

    elif scrolled(202, korean=211):
        show mute tensescb with fast
        ms "...embarrassing..."

    elif scrolled(213, korean=225):
        show mute tensesc with fast

    elif scrolled(226, korean=238):
        show mute insecure with fast
        ms "...but they're women!"

    elif scrolled(1000):
        show mute sigh blush with fast

    jump log_loop

label log_2_3_mute:
    if scrolled(8, korean=7):
        show mute whatsob with fast
        ms "Wait, mixed-sex theatre? I don't know about that..."

    elif scrolled(15, korean=14):
        show mute whatscb with fast

    elif scrolled(24, korean=22):
        show mute damn with fast
        ms "...wouldn't you, like, have to worry about passions running too high...?"

    elif scrolled(1000):
        show mute suspicious blush with fast

    jump log_loop

label log_2_4_mute:
    if scrolled(7, korean=7):
        show mute upsetsob with fast
        ms "...um, wow, there is so much wrong with that."

    elif scrolled(19, korean=19):
        show mute give up with fast
        ms "What even is this? In the absence of men, do all women just naturally play married...?!"

    elif scrolled(28, korean=27):
        show mute upsetscb with fast
        ms "...um..."

    elif scrolled(36, korean=36):
        show mute whatsob with fast
        ms "...wow, this is..."

    elif scrolled(45, korean=45):
        show mute pressure with fast
        ms "...but..."

    elif scrolled(53, korean=53):
        show mute mad with fast
        ms "This isn't love! This is just... completely unrestrained perverse lust...!"

    elif scrolled(61, korean=61):
        show mute give up with fast
        ms "...it just keeps going...!"

    elif scrolled(78, korean=79):
        show mute challengescb with fast

    elif scrolled(101, korean=102):
        show mute upsetscb with fast

    elif scrolled(117, korean=118):
        show mute upset3 with fast
        ms "I... wasn't really prepared for this kind of detail..."

    elif scrolled(127, korean=128):
        show mute astonished with fast

    elif scrolled(1000):
        show mute tired blush with fast

    jump log_loop

label log_2_5_mute:
    if scrolled(8, korean=6):
        show mute tensescb with fast
        ms "Geeze, could you be any more melodramatic...?"

    elif scrolled(22, korean=22):
        show mute wowsc with fast

    elif scrolled(30, korean=29):
        show mute tch with fast
        ms "...see, this is why it doesn't make sense for women to be together."

    elif scrolled(38, korean=37):
        show mute disbelief with fast
        ms "...uh..."

    elif scrolled(49, korean=49):
        show mute wowsob with fast
        ms "...wait... but I thought it was Ae-jeong who played the man's role...?"

    elif scrolled(66, korean=68):
        show mute upsetscb with fast
        ms "...I don't get it..."

    elif scrolled(79, korean=81):
        show mute tensescb with fast

    elif scrolled(81, korean=83):
        show mute whatsob with fast

    elif scrolled(89, korean=92):
        show mute give up with fast
        ms "...wow..."

    elif scrolled(108, korean=110):
        show mute upsetscb with fast

    elif scrolled(116, korean=116):
        show mute damn with fast
        ms "HOW IS THAT SUPPOSED TO BE INNOCENT."

    elif scrolled(1000):
        show mute worry side with fast

    jump log_loop

label log_2_6_mute:
    if scrolled(8, korean=6):
        show mute hmphso with fast
        ms "...this sounds pretty normal, though..."

    elif scrolled(16, korean=12):
        show mute tensesob with fast
        ms "...is this man complaining that a play is too romantic? Really?"

    elif scrolled(24, korean=19):
        show mute hmphsc with fast

    elif scrolled(1000):
        show mute suspicious with fast

    jump log_loop

label log_2_7_mute:
    if scrolled(8, korean=9):
        show mute disbelief blush with fast
        ms "...yes, of course you make everything worse!"

    elif scrolled(22, korean=23):
        show mute pout with fast

    elif scrolled(30, korean=31):
        show mute worry2 with fast
        ms "Oh no..."

    elif scrolled(42, korean=43):
        show mute sorryscb with fast

    elif scrolled(53, korean=55):
        show mute wowsob with fast
        ms "...canned tea...?"

    elif scrolled(61, korean=63):
        show mute sighsob with fast
        ms "Oh {i}finally{/i} her parents take some responsibility in getting her married!"

    elif scrolled(73, korean=76):
        show mute apologize with fast
        ms "Like... why didn't they figure this out for her years ago?"

    elif scrolled(81, korean=85):
        show mute sorrysc with fast

    elif scrolled(91, korean=95):
        show mute upsetsc with fast

    elif scrolled(102, korean=105):
        show mute insecure with fast
        ms "...see, this is why that kind of relationship isn't just harmless...!"

    elif scrolled(116, korean=120):
        show mute sigh blush with fast

    elif scrolled(124, korean=127):
        show mute tensesob with fast
        ms "...it'd be so much easier for her if she was more reasonable about it..."

    elif scrolled(140, korean=143):
        show mute challengesc with fast

    elif scrolled(148, koeran=153):
        show mute challengesob with fast
        ms "That's not how love works!"

    elif scrolled(1000):
        show mute cry with fast
        ms "What monster taught these women to expect love to come before marriage instead of after?!"

    jump log_loop

label log_2_8_mute:
    if scrolled(12, korean=14):
        show mute sorrysob with fast
        ms "Oh no... poor girl..."

    elif scrolled(23, korean=26):
        show mute sighsob with fast
        ms "...she just keeps setting herself up for disappointment..."

    elif scrolled(31, korean=34):
        show mute tensescb with fast
        ms "...didn't she realize this was bound to happen?"

    elif scrolled(41, korean=45):
        show mute upsetsob with fast
        ms "...it's a generous offer! Jin-a needs to be more rational..."

    elif scrolled(66, korean=73):
        show mute tensesc with fast

    elif scrolled(78, korean=84):
        show mute hmphscb with fast

    elif scrolled(91, korean=100):
        show mute sighsob with fast
        ms "This is painful..."

    elif scrolled(100, korean=110):
        show mute insecure with fast
        ms "...but Ae-jeong did the right thing! How can she be so unappreciative of that...?!"

    elif scrolled(1000):
        show mute tired blush with fast

    jump log_loop

label log_2_9_mute:
    if scrolled(5, korean=3):
        show mute enthusiastic blush with fast
        ms "Oh, that's the first Emperor's brother they're talking about..."

    elif scrolled(13, korean=11):
        show mute sweetsob with fast
        ms "...so I guess she ended up working as a courtesan, then."

    elif scrolled(20, korean=17):
        show mute sweetsc with fast

    elif scrolled(31, korean=28):
        show mute hmphsob with fast
        ms "Lost love, huh..."

    elif scrolled(39, korean=35):
        show mute apologize with fast
        ms "...it's fortunate for her, but I still don't think courtesans are really proper..."

    elif scrolled(52, korean=48):
        show mute thought with fast

    elif scrolled(60, korean=55):
        show mute hmphsc with fast
        ms "...huh..."

    elif scrolled(66, korean=61):
        show mute neutralsc with fast

    elif scrolled(1000):
        show mute talk4 with fast
        if any_read("M2-2", "M2-4", "M2-5", "M2-7", "M2-8"):
            ms "...well, I guess it ended well for everyone, at least? Even if there was heartbreak..."
        else:
            ms "...well, I guess it ended well for everyone, at least?"

    jump log_loop

label log_4_1_mute:
    if scrolled(8, korean=8):
        show mute hateso with fast
        ms "...Old *Mute was so rude...!"

    elif scrolled(20, korean=20):
        show mute hmphsc with fast

    elif scrolled(31, korean=31):
        show mute tensesc with fast

    elif scrolled(44, korean=44):
        show mute tensesob with fast
        ms "...uh..."

    elif scrolled(52, korean=53):
        if not any_read("M3-2", "M3-3", "M3-5", "M4-5", "M6-3", "M6-7"):
            show mute wowsob with fast
            ms "Wait, Queen Oh Eun-a? She was an official before...?!"
        else:
            show mute hmphsob with fast
            ms "I still can't imagine Queen Oh Eun-a as an official..."

    elif scrolled(64, korean=64):
        show mute tensesc with fast

    elif scrolled(72, korean=72):
        show mute tenseso with fast
        ms "Oh! Of course Eun-a would want to improve literacy!"

    elif scrolled(92, korean=92):
        show mute tensesc with fast

    elif scrolled(100, korean=100):
        show mute hmphsob with fast
        ms "...wow, that's a cold maneuver... respectable, but..."

    elif scrolled(121, korean=121):
        show mute hmphsc with fast

    elif scrolled(133, korean=132):
        show mute neutralsc with fast

    elif scrolled(141, korean=140):
        show mute complain with fast
        ms "...I can't deal with how rude she is, though!"

    elif scrolled(159, korean=158):
        show mute tensesc with fast

    elif scrolled(1000):
        show mute think with fast

    jump log_loop

label log_4_2_mute:
    if scrolled(8, korean=7) and read("M1-2"):
        show mute hmphso with fast
        ms "So this is the result of Old *Mute's conspiring..."

    elif scrolled(44, korean=42):
        show mute tensesc with fast

    elif scrolled(61, korean=58):
        show mute whatscb with fast

    elif scrolled(71, korean=68):
        show mute what with fast
        ms "...wow, what uncivilized bickering..."

    elif scrolled(92, korean=90):
        show mute hmphsc with fast

    elif scrolled(105, korean=102):
        show mute tensesob with fast
        ms "...huh..."

    elif scrolled(113, korean=109):
        show mute upset3 with fast
        ms "...she's really playing this strongly, isn't she?"

    elif scrolled(132, korean=128):
        show mute hmphsc with fast

    elif scrolled(145, korean=142):
        show mute tensesc with fast

    elif scrolled(160, korean=156):
        show mute wowsob with fast
        ms "...wow."

    elif scrolled(170, korean=167):
        if not read("M1-5"):
            show mute upsetsob with fast
            ms "...1600 years? Wow... that's..."
            # Might need branch if you've seen this number back in 1_5 - Raide
        else:
            show mute tensesob with fast
            ms "1600 years is such a long time..."

    elif scrolled(183, korean=181):
        show mute whatscb with fast

    elif scrolled(207, korean=204):
        if not any_read("M1-4", "M2-9", "M3-1", "M3-2", "M3-7", "M4-3", "M4-4", "M4-5", "M4-6", "M4-7", "M4-8", "M4-9", "M6-1", "M6-4", "M6-5", "M6-6", "M6-7", "M6-8", "M6-9"):
            show mute disbelief blush with fast
            ms "...so just like that, Old *Mute was able to name the new Chief Councillor?"
        else:
            show mute upset3 with fast
            ms "...so Old *Mute named the new Chief Councillor that easily?"

    elif scrolled(1000):
        show mute tch with fast

    jump log_loop

label log_4_3_mute:
    if scrolled(6, korean=5):
        show mute tensesob with fast
        ms "Oh, wow... that was a problem even in the past?"

    elif scrolled(15, korean=15):
        show mute annoyed2 with fast
        ms "...well, actually, I guess it'd be worse without marriage being respected, huh..."

    elif scrolled(28, korean=28):
        show mute neutralsc with fast

    elif scrolled(38, korean=38):
        show mute polite with fast
        ms "Sounds like a good policy."

    elif scrolled(68, korean=69):
        show mute nicesc with fast

    elif scrolled(87, korean=88):
        show mute craftysc with fast

    elif scrolled(95, korean=94):
        show mute niceso with fast
        ms "Makes sense to me."

    elif scrolled(105, korean=104):
        show mute whatsob with fast

    elif scrolled(112, korean=111):
        show mute give up with fast
        ms "...geeze, what's with her arguing with a man like that...? I'd never!"

    elif scrolled(137, korean=137):
        show mute challengesc with fast

    elif scrolled(145, korean=144):
        show mute tensesob with fast
        ms "Huh..."

    elif scrolled(159, korean=159):
        show mute tensescb with fast

    elif scrolled(170, korean=170):
        show mute challengesc with fast

    elif scrolled(190, korean=188):
        show mute neutralsc with fast

    elif scrolled(1000):
        show mute enthusiastic blush with fast
        ms "...but, like, I guess it went through in the end, right?"

    jump log_loop

label log_4_4_mute:
    if scrolled(6, korean=5):
        show mute neutralsc with fast

    elif scrolled(14, korean=13):
        show mute wowsob with fast
        ms "...why would it be any different...?"

    elif scrolled(43, korean=41):
        show mute hmphsc with fast

    elif scrolled(1000):
        show mute doubt with fast
        ms "Okay, I don't understand what's noteworthy about this."

    jump log_loop

label log_4_5_mute:
    if scrolled(8, korean=7):
        show mute tensesob with fast
        ms "...wow... incredibly uncivilized..."

    elif scrolled(26, korean=24):
        show mute hmphsc with fast

    elif scrolled(32, korean=29):
        show mute neutralsc with fast
        ms "Hm."

    elif scrolled(67, korean=61):
        show mute whatscb with fast

    elif scrolled(71, korean=65):
        show mute wowsob with fast
        ms "What? Why?"

    elif scrolled(90, korean=85):
        show mute hatesob with fast
        ms "...hanging out nobles to dry? How barbaric..."

    elif scrolled(110, korean=106):
        show mute tensesc with fast

    elif scrolled(124, korean=121):
        show mute hmphsc with fast

    elif scrolled(150, korean=147):
        show mute wowsc with fast

    elif scrolled(174, korean=170):
        show mute hmm with fast

    elif scrolled(182, korean=178):
        show mute challengeso with fast
        ms "What? Of course it makes a difference—respecting elders is important!"

    elif scrolled(194, korean=189):
        show mute tensesob with fast
        ms "So... \"Meritocracy\" wasn't meant to change anything, then. How corrupt..."

    elif scrolled(204, korean=199):
        show mute thought with fast

    elif scrolled(224, korean=220):
        show mute hmphscb with fast

    elif scrolled(242, korean=238):
        show mute tensesc with fast

    elif scrolled(1000):
        show mute suspicious blush with fast

    jump log_loop

label log_4_6_mute:
    if scrolled(8, korean=9):
        show mute hatesob with fast
        ms "...what unbelievable rudeness from Old *Mute!"

    elif scrolled(19, korean=19):
        show mute tensesc with fast

    elif scrolled(28, korean=27):
        show mute damn with fast
        ms "...I can't believe it... I was this much of a shrew in the past...?!"

    elif scrolled(37, korean=36):
        show mute give up with fast
        ms "Like, no wonder the ministers thought I was trouble, having known her!"

    elif scrolled(53, korean=52):
        show mute suspicious blush with fast

    elif scrolled(66, korean=65):
        show mute astonished blush with fast
        ms "...I used to have that kind of power?!"

    elif scrolled(86, korean=87):
        show mute insecure with fast
        ms "...just unbelievable... did she think wearing pants let her dictate to men like that?!"

    elif scrolled(111, korean=111):
        show mute tensescb with fast

    elif scrolled(130, korean=130):
        show mute wowscb with fast

    elif scrolled(143, korean=144):
        show mute whatsob with fast
        ms "WHOA."

    elif scrolled(153, korean=154):
        show mute upsetsc with fast

    elif scrolled(173, korean=172):
        show mute challengescb with fast

    elif scrolled(189, korean=190):
        show mute tensesc with fast

    elif scrolled(207, korean=208):
        show mute hmphso with fast
        ms "...geeze, she sure deserved that one."

    elif scrolled(245, korean=245):
        show mute neutralsc with fast

    elif scrolled(1000):
        show mute tired with fast

    jump log_loop

label log_4_7_mute:
    if scrolled(8, korean=5):
        show mute astonished with fast
        ms "Huh? Why wouldn't a family be led by the eldest son...?"

    elif scrolled(14, korean=11):
        show mute whatscb with fast

    elif scrolled(22, korean=18):
        show mute tensesob with fast
        ms "I don't believe in cutting out families either, but..."

    elif scrolled(38, korean=34):
        show mute hmphsc with fast

    elif scrolled(48, korean=44):
        show mute hateso with fast
        ms "...tch, how rude...!"

    elif scrolled(54, korean=51):
        show mute tensesc with fast

    elif scrolled(87, korean=81):
        show mute hmphsc with fast

    elif scrolled(1000):
        show mute suspicious blush with fast

    jump log_loop

label log_4_8_mute:
    if scrolled(8, korean=9):
        show mute abashed blush with fast
        ms "...she's completely out of control."

    elif scrolled(16, korean=18):
        show mute give up with fast
        ms "...I can't believe..."

    elif scrolled(41, korean=42):
        show mute pressure with fast

    elif scrolled(52, korean=53):
        show mute bitter with fast
        ms "How could I be like this...?"

    elif scrolled(62, korean=63):
        show mute tensescb with fast
        ms "Um..."

    elif scrolled(79, korean=80):
        show mute sorryscb with fast

    elif scrolled(96, korean=98):
        show mute hmphscb with fast

    elif scrolled(119, korean=122):
        show mute sigh with fast

    elif scrolled(127, korean=129):
        show mute annoyed with fast

    elif scrolled(1000):
        show mute damn with fast
        ms "I'd never be like that! I can be chatty, but... there's a time and place for that!"

    jump log_loop

label log_4_9_mute:
    if scrolled(8, korean=8) and any_read("M1-2", "M1-4", "M3-1"):
        show mute astonished with fast
        ms "...I spoke like that to Emperor Taejo...?!"

    elif scrolled(16, korean=17):
        show mute abashed blush with fast
        ms "...wow..."

    elif scrolled(32, korean=32):
        show mute wowsob with fast

    elif scrolled(46, korean=47):
        show mute whatscb with fast

    elif scrolled(56, korean=57):
        show mute pissed with fast
        ms "...I can't believe I'd defend the principles of that awful society like this..."

    elif scrolled(82, korean=82):
        show mute challengescb with fast

    elif scrolled(103, korean=104):
        show mute hateso with fast
        ms "Geeze, if she'd gotten her way... things would be so different!"

    elif scrolled(116, korean=117):
        show mute craftyscb with fast

    elif scrolled(128, korean=129):
        show mute wowsob with fast

    elif scrolled(152, korean=154):
        show mute nicescb with fast

    elif scrolled(176, korean=176):
        show mute grinsob with fast

    elif scrolled(183, korean=185):
        show mute astonished with fast
        ms "Wow..."

    elif scrolled(1000):
        show mute tch with fast
        ms "Just wow..."

    jump log_loop

label log_5_1_mute:
    if scrolled(8, korean=7):
        if read("M1-6"):
            show mute nicesob with fast
            ms "Well, at least {i}someone{/i} appreciates family gatherings..."
            # Needs a branch as this should only trigger after *Mute reads [fuck Heo family gathering] - Raide
        else:
            show mute nicesc with fast
            ms "Hm..."

    elif scrolled(16, korean=16):
        show mute wowsob with fast
        ms "...why would a Kim woman need to have a job...?"

    elif scrolled(27, korean=28):
        show mute tensesc with fast

    elif scrolled(41, korean=41):
        show mute sighsob with fast
        ms "Wow, still unmarried at 22? That poor woman..."

    elif scrolled(49, korean=50):
        show mute sweetsob with fast
        ms "...her grandmother sounds like a good woman, at least! Even if it's late..."

    elif scrolled(1000):
        show mute proud with fast

    jump log_loop

label log_5_2_mute:
    if scrolled(8, korean=8):
        show mute grinsob with fast
        ms "Ah, proper domestic life..."

    elif scrolled(12, korean=12):
        show mute thought with fast

    elif scrolled(20, korean=19):
        show mute whatsob with fast
        ms "...but she's a woman! A newly married one, even!"

    elif scrolled(30, korean=29):
        show mute sorryscb with fast

    elif scrolled(36, korean=35):
        show mute wowsc with fast

    elif scrolled(42, korean=41):
        show mute wowsob with fast

    elif scrolled(1000):
        show mute brag blush with fast
        ms "Ha, serves her right for teasing like that!"

    jump log_loop

label log_5_3_mute:
    if scrolled(5, korean=3):
        show mute tch with fast
        ms "...a noble man working under a woman...? Tch..."

    elif scrolled(20, korean=17):
        show mute wowsob with fast
        ms "Huh..."

    elif scrolled(33, korean=30):
        show mute upsetsob with fast
        ms "Oh no, why would you do that...?!"

    elif scrolled(40, korean=37):
        show mute upsetscb with fast

    elif scrolled(51, korean=47):
        show mute insecure with fast
        ms "...that's a fascinating theory, but... don't invite an unrelated man alone into your home...!"

    elif scrolled(62, korean=58):
        show mute worry2 with fast
        ms "Ugh, no, of course he did..."

    elif scrolled(72, korean=68):
        show mute give up with fast
        ms "...what a disgusting man!"

    elif scrolled(81, korean=77):
        show mute shame with fast
        ms "...you led him on, So-yi... oh no..."

    elif scrolled(89, korean=86):
        show mute bitter with fast
        ms "...no woman should have to deal with that."

    elif scrolled(101, korean=98):
        show mute upsetsc with fast

    elif scrolled(112, korean=109):
        show mute sighsob with fast

    elif scrolled(131, korean=127):
        show mute sorryscb with fast

    elif scrolled(139, korean=135):
        show mute upsetsob with fast
        ms "Tell your husband! It's his {i}duty{/i} to protect you...!"

    elif scrolled(149, korean=145):
        show mute tensescb with fast
        ms "Ugh..."

    elif scrolled(162, korean=157):
        show mute sorryscb with fast

    elif scrolled(176, korean=171):
        show mute sighscb with fast

    elif scrolled(183, korean=178):
        show mute upsetsc with fast

    elif scrolled(199, korean=192):
        show mute damn with fast
        ms "See? This is why it's bad for women to work... things like this happen!"

    elif scrolled(1000):
        show mute worry side with fast

    jump log_loop

label log_5_4_mute:
    if scrolled(8, korean=4):
        show mute insecure with fast
        ms "...see, her domestic life is really suffering because of her work..."

    elif scrolled(16, korean=12):
        show mute sorryscb with fast
        ms "Hm..."

    elif scrolled(31, korean=26):
        show mute upsetsc with fast

    elif scrolled(40, korean=36):
        show mute give up with fast
        ms "What? But... that's the best age to have children at!"

    elif scrolled(56, korean=51):
        show mute worry with fast

    elif scrolled(74, korean=69):
        show mute tired blush with fast

    elif scrolled(1000):
        show mute shame with fast
        ms "I guess a woman getting emotional about things like that can't be helped..."

    jump log_loop

label log_5_5_mute:
    if scrolled(4, korean=3):
        show mute upsetsob with fast
        ms "...oh, geeze, she needs to clean up badly..."

    elif scrolled(12, korean=11):
        show mute sighsob with fast
        ms "...oh, So-yi, it's not your fault you're naïve... it's just how you were raised."

    elif scrolled(24, korean=22):
        show mute tensesob with fast
        ms "...wait, really? Like, did she have evidence...?"

    elif scrolled(32, korean=28):
        show mute sighscb with fast

    elif scrolled(39, korean=35):
        show mute tensescb with fast

    elif scrolled(49, korean=45):
        show mute give up with fast
        ms "Disgusting!"

    elif scrolled(61, korean=58):
        show mute worry with fast

    elif scrolled(69, korean=66):
        show mute insecure with fast
        ms "...that shouldn't be the most important thing to her! Her husband should!"

    elif scrolled(81, korean=79):
        show mute bitter with fast
        ms "Really, if she'd just see that it's for the better..."

    elif scrolled(95, korean=88):
        show mute pout with fast

    elif scrolled(109, korean=109):
        show mute tired blush with fast

    elif scrolled(130, korean=130):
        show mute shame with fast
        ms "...she seems like a good woman! Just... with confused priorities."

    elif scrolled(138, korean=137):
        show mute suspicious blush with fast

    elif scrolled(152, korean=151):
        show mute worry3 with fast
        ms "Like... her backwards society really let her down; it's not her fault..."

    elif scrolled(164, korean=161):
        show mute pout with fast

    elif scrolled(1000):
        show mute tired with fast

    jump log_loop

label log_5_6_mute:
    if scrolled(9, korean=10):
        show mute hmphso with fast
        ms "...finally, something by the man..."

    elif scrolled(17, korean=18):
        show mute upsetsob with fast
        ms "...no, of course it's not healthy!"

    elif scrolled(22, korean=23):
        show mute whatsob with fast
        ms "Yikes..."

    elif scrolled(27, korean=28):
        show mute sighsob with fast
        ms "Oh, geeze..."

    elif scrolled(35, korean=38):
        show mute upset2 with fast
        ms "...she kind of is, though... it's just not her fault!"

    elif scrolled(46, korean=50):
        show mute tensesc with fast

    elif scrolled(63, korean=68):
        show mute sorrysc with fast

    elif scrolled(73, korean=77):
        show mute sorrysob with fast
        ms "Oh..."

    elif scrolled(107, korean=114):
        show mute upsetsc with fast

    elif scrolled(115, korean=123):
        show mute hmphsob with fast
        ms "...that's good!"

    elif scrolled(138, korean=147):
        show mute upsetscb with fast

    elif scrolled(146, korean=155):
        if read("M5-5"):
            show mute astonished blush with fast
            ms "Wait... is she...?"
            # Need a conditional so these two lines only happens after you've read 5_5 (the blowjob)
        else:
            show mute upsetscb with fast
    
    elif scrolled(155, korean=164):
        if read("M5-5"):
            show mute cry with fast
            ms "...she is! Ugh, that's... poor thing..."
        else:
            show mute tensescb with fast

    elif scrolled(168, korean=177):
        show mute give up with fast
        ms "It'd be a start, you idiot..."

    elif scrolled(178, korean=186):
        show mute insecure with fast
        ms "Agh, no, don't encourage that! You're just going to make her retreat even further!"

    elif scrolled(1000):
        show mute tired blush with fast

    jump log_loop

label log_5_7_mute:
    if scrolled(8, korean=6):
        show mute tensesc with fast
        ms "Hm..."

    elif scrolled(14, korean=11):
        show mute hmphsc with fast

    elif scrolled(22, korean=19):
        show mute astonished with fast
        ms "...wait, her? The Pale Bride...?"

    elif scrolled(31, korean=27):
        show mute wowsc with fast

    elif scrolled(43, korean=38):
        show mute upsetscb with fast

    elif scrolled(51, korean=46):
        show mute abashed blush with fast
        ms "Wait... how did she figure it out when Kim Jung-su couldn't...?"

    elif scrolled(67, korean=62):
        show mute wowso with fast

    elif scrolled(75, korean=69):
        show mute whatscb with fast
        ms "...hm..."

    elif scrolled(88, korean=81):
        show mute tensesc with fast

    elif scrolled(93, korean=86):
        show mute sorryscb with fast

    elif scrolled(1000):
        show mute worry2 with fast
        ms "...she sounds really obsessive. It's worrying..."

    jump log_loop

label log_5_8_mute:
    if scrolled(8, korean=7):
        show mute sigh blush with fast
        ms "...she's really not doing okay."

    elif scrolled(15, korean=14):
        show mute sweetsob with fast
        ms "That's good of them..."

    elif scrolled(23, korean=22):
        show mute whatever with fast
        ms "...of course they're afraid of you, you fragile obsessive woman!"

    elif scrolled(32, korean=30):
        show mute hmphsc with fast

    elif scrolled(38, korean=36):
        show mute sighsob with fast
        ms "What she's discovering is shocking, but..."

    elif scrolled(1000):
        show mute worry with fast

    jump log_loop

label log_5_9_mute:
    if scrolled(8, korean=5):
        show mute sorrysob with fast
        ms "...of course he doesn't share your optimism..."

    elif scrolled(17, korean=14):
        show mute upsetsob with fast
        ms "...did he just give up on her? Oh, geeze..."

    elif scrolled(25, korean=22):
        show mute sighsob with fast
        ms "She just doesn't get it..."

    elif scrolled(44, korean=40):
        show mute sorryscb with fast

    elif scrolled(58, korean=55):
        show mute sob with fast
        ms "Ugh... okay, like, this is just painful to read."

    elif scrolled(71, korean=68):
        show mute hmphscb with fast

    elif scrolled(79, korean=76):
        show mute wowsob with fast
        ms "...wow..."

    elif scrolled(97, korean=96):
        show mute sorryscb with fast

    elif scrolled(115, korean=114):
        show mute sorrysob with fast
        ms "Oh...!"

    elif scrolled(123, korean=122):
        show mute give up with fast
        ms "Agh, geeze, you didn't even mean it? Can't you see you'd be happier that way...?!"

    elif scrolled(131, korean=131):
        show mute astonished blush with fast
        ms "...wait... but this is from, like, right before the computers got wiped..."

    elif scrolled(143, korean=143):
        show mute shame with fast

    elif scrolled(1000):
        show mute tired blush with fast

    jump log_loop

label log_6_1_mute:
    if scrolled(3, korean=4):
        if len(store.seen_characters["OldMute"]) > 1:
            show mute hateso with fast
            ms "Ugh, wow... Old *Mute is rude as ever..."
            # Need a conditional if this is the first log with Old *Mute that player has read - Raide
        else:
            show mute hateso with fast
            ms "Ugh, wow... Old *Mute is so rude..."

    elif scrolled(15, korean=15):
        show mute tensesob with fast
        ms "...this Meritocracy thing sounds legitimately perplexing, though."

    elif scrolled(22, korean=22):
        show mute hmm blush with fast

    elif scrolled(37, korean=38):
        show mute wowsob with fast
        ms "Huh..."

    elif scrolled(46, korean=47):
        show mute challengeso with fast
        ms "...tch, how disrespectful..."

    elif scrolled(55, korean=56):
        if any_read("M6-5", "M6-6", "M6-7", "M6-8"):
            show mute tch with fast
            ms "...I guess it turned out to be true, though..."
        else:
            show mute give up with fast
            ms "...wow, what a thing to suggest..."

    elif scrolled(64, korean=66):
        show mute tensescb with fast

    elif scrolled(1000):
        show mute serious with fast

    jump log_loop

label log_6_2_mute:
    if scrolled(9, korean=10):
        show mute give up with fast
        ms "...I knew it would come to this, but still... like, that's awful."
        # Needs a branch if players haven't read about Seo and how she's not a good wife - Raide
        # she already knew this because of Queen Eun-a's speech

    elif scrolled(18, korean=20):
        show mute tensescb with fast
        ms "...ugh..."

    elif scrolled(26, korean=28):
        show mute hmphsob with fast
        ms "...well... I know dressing down an elder male relative is wrong, but... in this case..."

    elif scrolled(41, korean=44):
        show mute bitter with fast
        ms "It's a hard truth, but... he's surely not wrong..."

    elif scrolled(53, korean=56):
        show mute insecure with fast
        ms "...whoa, geeze! See... that's why women security officers are a terrible idea!"

    elif scrolled(63, korean=67):
        show mute challengesc with fast

    elif scrolled(83, korean=87):
        show mute hatesob with fast
        ms "That is still not okay!"

    elif scrolled(111, korean=111):
        show mute astonished with fast

    elif scrolled(119, korean=126):
        show mute challenge2 with fast

    elif scrolled(127, korean=134):
        show mute damn with fast
        ms "She's just too emotional to be given that kind of responsibility... she clearly can't handle it!"

    elif scrolled(145, korean=153):
        show mute suspicious blush with fast

    elif scrolled(157, korean=165):
        show mute abashed with fast
        ms "Wait... how was he not the most important...?!"

    elif scrolled(175, korean=186):
        show mute tensescb with fast

    elif scrolled(183, korean=194):
        show mute tensesob with fast
        ms "...so even a man-hater like Old *Mute could feel love..."

    elif scrolled(205, korean=218):
        show mute whatever with fast

    elif scrolled(215, korean=229):
        show mute sorrysc with fast

    elif scrolled(229, korean=243):
        show mute hmphscb with fast

    elif scrolled(240, korean=255):
        show mute upsetsc with fast

    elif scrolled(250, korean=266):
        show mute hatesc with fast
        ms "Ugh..."

    elif scrolled(258, korean=274):
        show mute damn with fast
        ms "...this is not the way things should be! It's just... so wrong!"

    elif scrolled(267, korean=285):
        show mute worry with fast

    elif scrolled(277, korean=296):
        show mute disbelief blush with fast

    elif scrolled(1000):
        show mute give up with fast
        ms "A woman shouldn't have to be given the impossible task of protecting her husband... that's just not fair..."

    jump log_loop

label log_6_3_mute:
    if scrolled(7, korean=8):
        show mute hateso with fast
        ms "Tch..."

    elif scrolled(17, korean=19):
        show mute hatesob with fast
        ms "...if the language of the classics isn't good enough for you, what is?"

    elif scrolled(28, korean=30):
        show mute tensesc with fast

    elif scrolled(39, korean=42):
        show mute hmphscb with fast

    elif scrolled(47, korean=49):
        show mute upset3 with fast
        ms "This sure is, like, a lot of flowery language to defend barbarianism..."

    elif scrolled(54, korean=56):
        show mute hmphso with fast
        ms "...well, that's good."

    elif scrolled(70, korean=73):
        show mute hmm2 with fast
        ms "Good advice..."

    elif scrolled(1000):
        show mute think with fast

    jump log_loop

label log_6_4_mute:
    if scrolled(6, korean=2):
        show mute tenseso with fast
        ms "...so here's the part she couldn't deal with, huh..."

    elif scrolled(20, korean=16):
        show mute wowsob with fast

    elif scrolled(28, korean=25):
        show mute damn with fast
        ms "Old *Mute wouldn't even let her be a good mother?"

    elif scrolled(41, korean=38):
        show mute disbelief blush with fast
        ms "...huh..."

    elif scrolled(49, korean=47):
        show mute whatsob with fast
        ms "Wow. Yikes."

    elif scrolled(61, korean=59):
        show mute hateso with fast
        ms "...ugh, it's just... completely unfair to put a woman in that situation!"

    elif scrolled(80, korean=77):
        show mute sorryscb with fast

    elif scrolled(88, korean=85):
        show mute tensesob with fast
        ms "...wow..."

    elif scrolled(97, korean=94):
        show mute tensesc with fast

    elif scrolled(113, korean=110):
        show mute tensescb with fast

    elif scrolled(121, korean=117):
        show mute upset3 with fast
        ms "What's going on here...?"

    elif scrolled(149, korean=146):
        show mute hmphscb with fast

    elif scrolled(162, korean=160):
        show mute sorrysc with fast

    elif scrolled(174, korean=172):
        show mute upsetscb with fast

    elif scrolled(182, korean=180):
        show mute hatesob with fast
        ms "...she's way too emotionally volatile for this..."

    elif scrolled(200, korean=199):
        show mute challengesc with fast

    elif scrolled(208, korean=208):
        show mute tensesob with fast
        ms "Huh..."

    elif scrolled(232, korean=233):
        show mute tired blush with fast

    elif scrolled(1000):
        show mute worry3 with fast
        ms "...poor woman... that's just not fair."

    jump log_loop

label log_6_5_mute:
    if scrolled(8, korean=8):
        show mute challengeso with fast
        ms "...yes, and the ship was a better place for it, you petty woman!"

    elif scrolled(20, korean=21):
        show mute challengesc with fast

    elif scrolled(30, korean=31):
        show mute whatscb with fast

    elif scrolled(44, korean=46):
        show mute wowso with fast
        ms "Wait... what?! Navigation AI...?"

    elif scrolled(52, korean=54):
        show mute hmphscb with fast

    elif scrolled(61, korean=63):
        show mute tensescb with fast
        ms "...oh..."

    elif scrolled(74, korean=77):
        show mute tensesob with fast
        ms "This dynamic... it's really uncomfortable..."

    elif scrolled(92, korean=96):
        show mute craftyscb with fast

    elif scrolled(104, korean=107):
        show mute upset3 with fast
        ms "...1600 years... I can't imagine, though..."

    elif scrolled(113, korean=116):
        show mute whatscb with fast

    elif scrolled(128, korean=130):
        show mute whatever with fast
        ms "...will that happen to me...?!"

    elif scrolled(136, korean=139):
        show mute give up with fast
        ms "No, you shouldn't be able to! What the hell is {i}wrong{/i} with this society?!"

    elif scrolled(159, korean=160):
        show mute challenge2 with fast

    elif scrolled(172, korean=171):
        show mute complain with fast
        ms "...Old *Mute, you liar."

    elif scrolled(1000):
        show mute shame with fast
        ms "This is the person I used to be...?!"

    jump log_loop

label log_6_6_mute:
    if scrolled(7, korean=5):
        show mute hmphsc with fast
        ms "Hm..."

    elif scrolled(15, korean=13):
        show mute sorrysob with fast
        ms "...so women like Seo-yeong were just disconnected from reality...?"

    elif scrolled(29, korean=27):
        show mute tensesob with fast
        ms "It's not weird! Why would a woman like you even want to be there...?!"

    elif scrolled(44, korean=42):
        show mute give up with fast
        ms "...a better family head wouldn't be so oblivious."

    elif scrolled(54, korean=52):
        show mute challenge with fast

    elif scrolled(1000):
        show mute tch with fast
        ms "Tch... that's no place for a noblewoman..."

    jump log_loop

label log_6_7_mute:
    if scrolled(13, korean=10):
        show mute tensesob with fast
        ms "Um..."

    elif scrolled(27, korean=24):
        show mute damn with fast
        ms "...um, like, I'd expect the same thing if I spoke out of turn to a superior!"

    elif scrolled(51, korean=47):
        show mute doubt blush with fast
        ms "Huh?"

    elif scrolled(60, korean=54):
        show mute hmphso with fast
        ms "Wait... that can't be true."

    elif scrolled(74, korean=68):
        show mute tensesob with fast
        ms "...what...?"

    elif scrolled(82, korean=76):
        show mute insecure with fast
        ms "That can't be right. Emperor Taejo was above that!"

    elif scrolled(94, korean=89):
        show mute hmphsc with fast

    elif scrolled(101, korean=96):
        show mute tensesc with fast

    elif scrolled(112, korean=107):
        show mute wowsob with fast
        ms "...wait, they can't be talking about..."

    elif scrolled(127, korean=123):
        show mute tensescb with fast

    elif scrolled(136, korean=133):
        show mute challenge4 with fast
        ms "...this isn't right! I don't believe this!"

    elif scrolled(144, korean=141):
        show mute astonished blush with fast
        ms "...wait... Old *Mute could do that? I could never have used the root password... I'm not capable!"

    elif scrolled(156, korean=154):
        show mute disbelief with fast

    elif scrolled(170, korean=167):
        show mute sorrysob with fast
        ms "She's... she's really conspiring against Emperor Taejo...?!"

    elif scrolled(175, korean=171):
        show mute whatscb with fast

    elif scrolled(183, korean=179):
        show mute hateso with fast
        ms "...wait... this can't be right..."

    elif scrolled(203, korean=201):
        show mute upsetsc with fast

    elif scrolled(211, korean=209):
        show mute astonished blush with fast

    elif scrolled(219, korean=217):
        show mute abashed blush with fast
        ms "Queen Eun-a was my friend in the past... I'd never have conspired against her!"

    elif scrolled(1000):
        show mute mad with fast
        ms "She was my friend! She was my mistress! Like, she even told me herself... this must be a lie, it doesn't make sense!"

    jump log_loop

label log_6_8_mute:
    if scrolled(6, korean=9):
        show mute upsetscb with fast
        ms "...ugh..."

    elif scrolled(19, korean=26):
        show mute sighsob with fast
        ms "...I just... I don't get, if Old *Mute put Emperor Taejo into power, why would she want to take it away..."

    elif scrolled(35, korean=43):
        show mute upsetsob with fast
        ms "...this isn't right..."

    elif scrolled(46, korean=54):
        show mute upsetscb with fast
        ms "...respecting elders is most important, but... this isn't..."

    elif scrolled(68, korean=80):
        show mute upsetsc with fast

    elif scrolled(74, korean=86):
        show mute tensescb with fast
        ms "Ugh..."

    elif scrolled(88, korean=101):
        show mute give up with fast
        ms "No!"

    elif scrolled(100, korean=111):
        show mute pressure with fast
        ms "...no, I'd never... she couldn't..."

    elif scrolled(116, korean=129):
        show mute challenge2 with fast

    elif scrolled(141, korean=153):
        show mute hatesc with fast

    elif scrolled(158, korean=172):
        show mute tensesc with fast

    elif scrolled(165, korean=181):
        show mute upsetsc with fast

    elif scrolled(179, korean=193):
        show mute hatesc with fast

    elif scrolled(1000):
        show mute give up with fast
        ms "This isn't right! This isn't right at all!"

    jump log_loop

label log_6_9_mute:
    if get_m("M6-9").encrypted:
        show mute annoyed2 with fast
        ms "The brute force decryption still hasn't found the key yet, unfortunately... I'm just as anxious as you to read it, okay? I'll let you know when it's ready!"

    elif scrolled(4, korean=3):
        show mute wowsob with fast
        ms "What...?!"

    elif scrolled(13, korean=12):
        show mute upsetsob with fast
        ms "She... this can't..."

    elif scrolled(26, korean=24):
        show mute upsetscb with fast

    elif scrolled(37, korean=34):
        show mute disbelief blush with fast
        ms "...did I really do these things...?"

    elif scrolled(51, korean=46):
        show mute worry2 with fast
        ms "...I..."

    elif scrolled(63, korean=59):
        show mute sighsob with fast
        ms "...why would anyone threaten someone like Queen Eun-a..."

    elif scrolled(77, korean=74):
        show mute wowsob with fast

    elif scrolled(88, korean=86):
        show mute tensescb with fast
        ms "But..."

    elif scrolled(96, korean=95):
        show mute abashed blush with fast
        ms "She'd never say something like that!"

    elif scrolled(108, korean=106):
        show mute upsetsc with fast

    elif scrolled(114, korean=111):
        show mute hatesob with fast
        ms "...hitting a man? She'd even...?!"

    elif scrolled(119, korean=116):
        show mute wowsob with fast

    elif scrolled(133, korean=129):
        show mute astonished blush with fast

    elif scrolled(141, korean=138):
        show mute damn with fast
        ms "This isn't right at all! Seo-yeong did that, not him!"

    elif scrolled(147, korean=144):
        show mute tensescb with fast
        ms "...she must be lying..."

    elif scrolled(170, korean=168):
        show mute upsetsc with fast

    elif scrolled(179, korean=176):
        show mute worry2 with fast
        ms "...no..."

    elif scrolled(188, korean=185):
        show mute cry with fast
        ms "...like, why would the past version of me lie about this..."

    elif scrolled(202, korean=198):
        show mute worry with fast

    elif scrolled(215, korean=211):
        show mute insecure with fast
        ms "...I..."

    elif scrolled(228, korean=224):
        show mute sob with fast

    elif scrolled(238, korean=235):
        show mute heh with fast
        ms "...there's no way that would make sense, is there..."

    elif scrolled(255, korean=251):
        show mute worry2 with fast
        ms "This... really happened, then..."

    elif scrolled(268, korean=265):
        show mute upsetsob with fast
        ms "What...? I..."

    elif scrolled(274, korean=272):
        show mute hatesob with fast
        ms "...Old *Mute... you coward! How could you?!"

    elif scrolled(293, korean=292):
        show mute upsetscb with fast

    elif scrolled(302, korean=302):
        show mute insecure with fast
        ms "...no... you manipulative bitch, how could you say something like that..."

    elif scrolled(310, korean=310):
        show mute give up with fast
        ms "...how could you take advantage of your lieutenant's feelings like that?!"

    elif scrolled(318, korean=319):
        show mute abashed blush with fast
        ms "Is that why she employed a woman? Because she'd be easier to manipulate...?!"

    elif scrolled(328, korean=329):
        show mute worry2 with fast
        ms "...this can't..."

    elif scrolled(341, korean=342):
        show mute cry with fast
        ms "...no..."

    elif scrolled(356, korean=359):
        show mute bitter with fast
        ms "...they lied about it... they planned the lie all along..."

    elif scrolled(371, korean=375):
        show mute tensescb with fast

    elif scrolled(379, korean=384):
        show mute astonished blush with fast
        ms "But..."

    elif scrolled(390, korean=395):
        show mute challenge2 with fast

    elif scrolled(401, korean=406):
        show mute pressure with fast
        ms "I... I thought she... I trusted her... she said she was my friend..."

    elif scrolled(410, korean=415):
        show mute mad with fast
        ms "...I know society was wrong, but... that can't be the way...!"

    elif scrolled(420, korean=425):
        show mute insecure with fast
        ms "...Old *Mute, you idiot... this is all your own fault!"

    elif scrolled(430, korean=435):
        show mute shame with fast
        ms "If you'd just listened to him... you wouldn't..."

    elif scrolled(441, korean=446):
        show mute cry with fast
        ms "...you'd still be alive..."

    elif scrolled(451, korean=455):
        show mute insecure with fast
        ms "You idiot! You stupid manipulative bitch!"

    elif scrolled(1000):
        show mute shame with fast
        ms "...I... I... I... I can't do that..."

    jump log_loop

label log_13_1_newmute:
    if scrolled(8, korean=8):
        show newmute disbelief with fast
        ns "...déjà vu."

    elif scrolled(17, korean=16):
        show newmute hmphscb with fast

    elif scrolled(25, korean=24):
        show newmute hmphsob with fast
        ns "...yeah, that sounds about right..."

    elif scrolled(38, korean=37):
        show newmute tensesc with fast

    elif scrolled(52, korean=52):
        show newmute tensescb with fast

    elif scrolled(62, korean=63):
        show newmute sighsob with fast
        ns "...yeah..."

    elif scrolled(75, korean=79):
        show newmute sorrysc with fast

    elif scrolled(89, korean=95):
        show newmute hmphsc with fast

    elif scrolled(1000):
        show newmute annoyed3 with fast
        ns "...okay, whatever, she lied about everything else... she's probably lying about the pants thing, too!"

    jump log_loop

label log_13_2_newmute:
    if scrolled(6, korean=5):
        show newmute heh with fast
        ns "Heh..."

    elif scrolled(14, korean=14):
        show newmute heh2 with fast
        ns "...try living in an English-language computer, kid. Now {i}that's{/i} confusing."

    elif scrolled(1000):
        show newmute neutral3 with fast

    jump log_loop

label log_13_3_newmute:
    if scrolled(0):
        show newmute talk2 with fast
        ns "Okay, whatever..."

    jump log_loop

label log_13_4_newmute:
    if scrolled(8, korean=9):
        show newmute hmphsc with fast
        ns "Huh..."

    elif scrolled(20, korean=21):
        show newmute thought with fast

    elif scrolled(32, korean=34):
        show newmute tensesc with fast

    elif scrolled(45, korean=49):
        show newmute tensesob with fast
        ns "\"Staring at a wall\"? Geeze, Eun-a sure was a mess..."

    elif scrolled(53, korean=57):
        show newmute hmm2 with fast
        ns "...so... I used to be the patient type, I guess...?"

    elif scrolled(65, korean=68):
        show newmute thought with fast

    elif scrolled(95, korean=99):
        show newmute nicesc with fast

    elif scrolled(1000):
        show newmute look open blush with fast
        ns "Um, \"punishing maids\" isn't going to be part of my job on your ship, right...?"

    jump log_loop

label log_13_5_newmute:
    if scrolled(8, korean=8):
        show newmute query with fast
        ns "Okay, so... everything he says, the opposite's true, right?"

    elif scrolled(16, korean=17):
        show newmute upset3 with fast
        ns "...sorry, that was too far. I know, like, even given the lies... *Mute believed in this to the end."

    elif scrolled(29, korean=28):
        show newmute tensesc with fast

    elif scrolled(39, korean=38):
        show newmute neutralsc with fast
        ns "...hm..."

    elif scrolled(47, korean=47):
        show newmute hmphso with fast
        ns "...you know, it doesn't really sound like storing people in analogue bodies really worked out well, either. Digital seems a lot safer to me."

    elif scrolled(59, korean=57):
        show newmute hmphsc with fast

    elif scrolled(1000):
        show newmute heh with fast
        ns "Like, okay, sure. It's pretty convincing. I am convinced. That is a speech that convinces."

    jump log_loop

label log_13_6_newmute:
    if scrolled(8, korean=6):
        show newmute wow with fast
        ns "Um... you'll forgive me if I don't turn into a push-over like that, right?"

    elif scrolled(22, korean=20):
        show newmute neutralsc with fast

    elif scrolled(39, korean=37):
        show newmute hmphsc with fast

    elif scrolled(47, korean=45):
        show newmute craftysc with fast
        ns "Hm..."

    elif scrolled(52, korean=51):
        show newmute neutralsc with fast

    elif scrolled(1000):
        show newmute tch with fast
        ns "...um, really?"

    jump log_loop

label log_13_7_newmute:
    if scrolled(10, korean=9):
        show newmute wowsc with fast
    
    elif scrolled(23, korean=20):
        show newmute tensesc with fast

    elif scrolled(31, korean=26):
        if any_read("M4-*"):
            show newmute disbelief blush with fast
            ns "That's... really different than the old council dynamic..."
        else:
            show newmute wowsob with fast
            ns "She's... very deferent..."

    elif scrolled(56, korean=52):
        show newmute hmphsc with fast
        
    elif scrolled(71, korean=66):
        show newmute thought with fast
        
    elif scrolled(1000):
        show newmute annoyed with fast
    
    jump log_loop

label log_13_8_newmute:
    if scrolled(4, korean=2):
        show newmute hmphsc with fast

    elif scrolled(12, korean=8):
        show newmute craftysob with fast
        ns "\"Awful fucking computer girl.\" I like that, that's a good nickname."
        
    elif scrolled(20, korean=15):
        show newmute neutralsc with fast
        
    elif scrolled(32, korean=24):
        show newmute wow3 with fast
        ns "Um, just to be perfectly clear... \"little sister\" means \"lesbian lover\", right?"

    elif scrolled(42, korean=33):
        show newmute tenseso with fast
        ns "...so even he believed it was Seo-yeong's fault...?"

    elif scrolled(53, korean=42):
        show newmute tensesc with fast
        
    elif scrolled(1000):
        show newmute talk4 with fast
        ns "Sounds like the culture shift wasn't really that smooth, huh..."

    jump log_loop

label log_13_9_newmute:
    if scrolled(8, korean=8):
        show newmute challengesob with fast
        ns "Liar!"

    elif scrolled(19, korean=18):
        show newmute hateso with fast
        ns "Liar, liar, liar..."

    elif scrolled(27, korean=26):
        show newmute hatesob with fast
        ns "That's not what the data says, you liar!"

    elif scrolled(45, korean=45):
        show newmute challengescb with fast
        
    elif scrolled(59, korean=56):
        show newmute hatesc with fast
        ns "...okay, that's a lie, and {i}cruel.{/i}"

    elif scrolled(67, korean=64):
        show newmute challengeso with fast
        ns "Lies!"

    elif scrolled(75, korean=72):
        show newmute evil with fast
        ns "You know, like, it's a good thing she didn't believe in wearing pants..."

    elif scrolled(1000):
        show newmute scorn with fast
        ns "...you know, on account of they'd be {i}on fire.{/i}"

    jump log_loop

label log_1_1_newmute:
    if scrolled(7, korean=7):
        show newmute neutralsc with fast
        ns "Hmm..."

    elif scrolled(15, korean=15):
        show newmute nicesob with fast
        ns "Heh..."

    elif scrolled(24, korean=24):
        show newmute nicescb with fast
        
    elif scrolled(32, korean=31):
        show newmute craftyso with fast
        ns "...they seem really friendly together..."

    elif scrolled(45, korean=43):
        show newmute neutralsc with fast
        
    elif scrolled(63, korean=64):
        show newmute nicesc with fast
        
    elif scrolled(71, korean=72):
        show newmute craftysc with fast
        
    elif scrolled(88, korean=89):
        show newmute thought with fast
        
    elif scrolled(1000):
        show newmute embarrassed with fast
        ns "...well, guess it worked, but sure not how they expected..."

    jump log_loop

label log_1_2_newmute:
    if scrolled(8, korean=7):
        show newmute grinsob with fast
        ns "Oh, nicely played of her..."

    elif scrolled(15, korean=15):
        show newmute nicescb with fast
        
    elif scrolled(28, korean=28):
        show newmute craftysob with fast
        ns "Okay... slight flip of hair for dramatic effect, huh..."

    elif scrolled(36, korean=36):
        show newmute nice blush with fast
        ns "...the old me had, like, a good dynamic with her lieutenant, didn't she...?"

    elif scrolled(44, korean=44):
        show newmute neutralsc with fast
        
    elif scrolled(65, korean=63):
        show newmute hmphsc with fast
        
    elif scrolled(75, korean=77):
        show newmute upset3 with fast
        ns "...she's maybe a little too singularly worried about demonstrations, huh?"

    elif scrolled(87, korean=92):
        show newmute hmphscb with fast
        
    elif scrolled(98, korean=105):
        show newmute wowscb with fast
        ns "Hm..."

    elif scrolled(110, korean=116):
        show newmute neutralsc with fast
        
    elif scrolled(124, korean=131):
        show newmute hmphsc with fast
        
    elif scrolled(141, korean=150):
        show newmute wowsc with fast
        
    elif scrolled(152, korean=161):
        show newmute hmm2 with fast
        ns "It's a really good plan, though! I mean... they sure did, like, render President Park powerless... so to speak."

    elif scrolled(164, korean=176):
        show newmute neutralsc with fast
        
    elif scrolled(173, korean=186):
        show newmute craftysob with fast
        ns "Yeah... gosh, Old *Mute was so cool, wasn't she?"

    elif scrolled(196, korean=210):
        show newmute nicesc with fast
        
    elif scrolled(208, korean=222):
        show newmute whatscb with fast
        
    elif scrolled(1000):
        show newmute sulk with fast
        
    jump log_loop

label log_1_3_newmute:
    if scrolled(8, korean=6):
        show newmute talk4 with fast
        ns "Boring..."

    elif scrolled(16, korean=14):
        show newmute tenseso with fast
        ns "...come on, get to it!"

    elif scrolled(28, korean=25):
        show newmute hmphsc with fast
        
    elif scrolled(36, korean=34):
        show newmute grinsob with fast
        ns "...geeze, stop wasting her time!"

    elif scrolled(45, korean=41):
        show newmute neutralsc with fast
        
    elif scrolled(64, korean=62):
        show newmute wowsc with fast
        
    elif scrolled(79, korean=77):
        show newmute wowsob with fast
        ns "Wow... Seo-yeong is... like, really intense..."

    elif scrolled(109, korean=106):
        show newmute wowscb with fast
        
    elif scrolled(117, korean=114):
        show newmute wow with fast
        ns "Oh, wow... Old *Mute always knew what to do, didn't she?"

    elif scrolled(132, korean=130):
        show newmute neutralsc with fast
        
    elif scrolled(140, korean=138):
        show newmute talk2 with fast
        ns "...yeah, yeah, whatever..."

    elif scrolled(1000):
        show newmute think with fast
        
    jump log_loop

label log_1_4_newmute:
    if scrolled(3, korean=2):
        show newmute nicesob with fast
        ns "Well, naturally."

    elif scrolled(11, korean=9):
        show newmute nicesc with fast
        
    elif scrolled(19, korean=17):
        show newmute wowsob with fast
        ns "...maybe a little too confident..."

    elif scrolled(29, korean=26):
        show newmute sweetsob with fast
        ns "...she really was in love with Old *Mute, wasn't she...?"

    elif scrolled(40, korean=39):
        show newmute nya with fast
        ns "Cat-like grin, huh... hm, like this?"

    elif scrolled(1000):
        show newmute smile blush with fast
        
    jump log_loop

label log_1_5_newmute:
    if scrolled(4, korean=2):
        show newmute nicesc with fast

    elif scrolled(14, korean=12):
        show newmute craftysob with fast
        ns "...wow... so cool..."
        
    elif scrolled(23, korean=22):
        show newmute grin blush with fast
        ns "Like, I want to be as amazing as that!"

    elif scrolled(1000):
        show newmute proud with fast
        
    jump log_loop

label log_1_6_newmute:
    if scrolled(8, korean=6):
        show newmute talk4 with fast
        ns "Ugh, boring..."

    elif scrolled(20, korean=18):
        show newmute query with fast
        ns "Here, I skipped ahead, spoilers: he loses his money, Mimi is a boy, they take like ten pages to finally kiss."
        
    # EYEROLL AFTER THAT

    elif scrolled(189, korean=193):
        show newmute serious with fast
        
    elif scrolled(190, korean=194):
        show newmute sulk with fast
        #kissing
        
    elif scrolled(234, korean=238):
        show newmute challenge with fast
        
    elif scrolled(1000):
        show newmute serious with fast
        
    jump log_loop

label log_1_7_newmute:
    if scrolled(10, korean=11):
        show newmute talk2 with fast
        ns "You can go ahead, I guess, but I'm not interested in this kind of thing..."

    elif scrolled(170, korean=173):
        show newmute neutral3 with fast
        
    elif scrolled(1000):
        show newmute think with fast
        
    jump log_loop

label log_1_8_newmute:
    if scrolled(10, korean=12):
        show newmute talk2 with fast
        ns "...I'm not really interested in this one..."

    elif scrolled(247, korean=251):
        show newmute neutral3 with fast
        
    elif scrolled(1000):
        show newmute annoyed with fast
        
    jump log_loop

label log_1_9_newmute:
    if scrolled(10, korean=11):
        show newmute think2 with fast
        ns "Well... that's sad, I guess..."

    elif scrolled(30, korean=31):
        show newmute challenge with fast
        
    elif scrolled(1000):
        show newmute neutral3 with fast
        
    jump log_loop

label log_2_1_newmute:
    if scrolled(10, korean=12):
        show newmute doubt blush with fast
        ns "This doesn't really have much to do with the old me, so..."

    elif scrolled(142, korean=149):
        show newmute neutral3 with fast
        
    elif scrolled(1000):
        show newmute sulk with fast
        
    jump log_loop

label log_2_2_newmute:
    if pronouns == "she":
        if scrolled(5, korean=3) and not hateplus_newmute_because_lesbians:
            
            show newmute tsundere with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know {i}you{/i} like women."

            $ hateplus_newmute_because_lesbians = True

        elif scrolled(6, korean=4):

            show newmute hmphsc with fast
            ns "...hm..."

        elif scrolled(16, korean=15):
            show newmute thought with fast

        elif scrolled(26, korean=26):
            show newmute neutralso with fast
            ns "...okay..."

        elif scrolled(65, korean=69):
            show newmute tensesc with fast

        elif scrolled(83, korean=89):
            show newmute hmphsc with fast

        elif scrolled(96, korean=104):
            show newmute tensescb with fast

        elif scrolled(106, korean=113):
            show newmute wowsob with fast
            ns "Huh... she's clever!"

        elif scrolled(122, korean=130):
            show newmute craftyscb with fast

        elif scrolled(131, korean=139):
            show newmute nicesc with fast

        elif scrolled(146, korean=153):
            show newmute sweetsob with fast
            ns "...okay, okay..."

        elif scrolled(170, korean=179):
            show newmute whatsob with fast
            ns "Oh, uh, whoa, {i}that's{/i} sudden!"

        elif scrolled(194, korean=203):
            show newmute wowscb with fast

        elif scrolled(213, korean=225):
            show newmute sweetscb with fast

        elif scrolled(225, korean=237):
            show newmute tsundere with fast
            ns "...well, okay, it's pretty cute, I'll admit... even if it's frivolous."

        elif scrolled(1000):
            show newmute shy with fast

    else:
        if scrolled(10, korean=9):
            show newmute embarrassed with fast
            ns "I'm, um, not really interested in {i}this{/i} kind of story. Sorry..."

        elif scrolled(225, korean=237):
            show newmute look with fast

        elif scrolled(1000):
            show newmute neutral3 with fast

    jump log_loop

label log_2_3_newmute:
    if scrolled(8, korean=7):
        
        show newmute tch with fast
        ns "Huh... why did Old *Mute think this was important to include...?"

    elif scrolled(16, korean=15):
        
        show newmute disbelief blush with fast
        ns "I don't think I understand?"

    elif scrolled(1000):
        show newmute suspicious with fast
        
    jump log_loop

label log_2_4_newmute:
    if pronouns == "she":
        if scrolled(8, korean=8) and not hateplus_newmute_because_lesbians:

            show newmute tsundere with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know {i}you{/i} like women."

            $ hateplus_newmute_because_lesbians = True

        elif scrolled(8, korean=8):

            show newmute craftysob with fast
            ns "...oh...!"

        elif scrolled(16, korean=16):
            show newmute nicesc with fast

        elif scrolled(28, korean=27):
            show newmute wowsc with fast
            ns "...huh..."

        elif scrolled(40, korean=40):
            show newmute wowsob with fast
            ns "...this is very detailed..."

        elif scrolled(45, korean=45):
            show newmute tenseso with fast
            ns "Those are bad things, I guess...?"

        elif scrolled(55, korean=55):
            show newmute embarrassed with fast
            ns "...geeze..."

        elif scrolled(78, korean=79):
            show newmute look blush with fast

        elif scrolled(88, korean=89):
            show newmute tsundere with fast
            ns "...is... that the sort of thing you like...?"

        elif scrolled(101, korean=102):
            show newmute wowscb with fast

        elif scrolled(111, korean=112):
            show newmute wowsob with fast
            ns "Like... the old me wouldn't have enjoyed reading this, right? I should feel bad, right?"

        elif scrolled(119, korean=120):
            show newmute wow3 with fast
            ns "...right...?"

        elif scrolled(127, korean=128):
            show newmute whatsob with fast

        elif scrolled(1000):
            show newmute heh2 with fast

    else:
        if scrolled(10, korean=10):
            show newmute tsundere with fast
            ns "I don't think this is something the old me would have approved of..."

        elif scrolled(127, korean=128):
            show newmute sulk with fast

        elif scrolled(1000):
            show newmute challenge with fast

    jump log_loop

label log_2_5_newmute:
    if pronouns == "she":
        if scrolled(11, korean=9) and not hateplus_newmute_because_lesbians:

            show newmute tsundere with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know {i}you{/i} like women."

            $ hateplus_newmute_because_lesbians = True

        elif scrolled(11, korean=9):
            show newmute whatscb with fast
            ns "...huh..."

        elif scrolled(20, korean=18):
            show newmute hmphsc with fast

        elif scrolled(30, korean=29):
            show newmute upsetsc with fast

        elif scrolled(40, korean=39):
            show newmute sighsob with fast
            ns "Aw... that is sad, though..."

        elif scrolled(50, korean=50):
            show newmute wowsob with fast
            ns "This tone..."

        elif scrolled(60, korean=60):
            show newmute whatsob with fast
            ns "...oh, wow..."

        elif scrolled(70, korean=72):
            show newmute wowscb with fast

        elif scrolled(82, korean=84):
            show newmute nicescb with fast

        elif scrolled(92, korean=95):
            show newmute sweetsob with fast
            ns "I... this is... I feel like I shouldn't be reading this..."

        elif scrolled(102, korean=104):
            show newmute statement blush with fast
            ns "...but, like... this is the sort of thing you'd...?"

        elif scrolled(116, korean=1116):
            show newmute sorrysc with fast

        elif scrolled(1000):
            show newmute tired blush with fast

    else:
        if scrolled(10, korean=8):
            show newmute embarrassed with fast
            ns "Not really interested, sorry..."

        elif scrolled(116, korean=116):
            show newmute sulk with fast

        elif scrolled(1000):
            show newmute annoyed with fast

    jump log_loop

label log_2_6_newmute:
    if scrolled(10, korean=8):
        
        show newmute annoyed3 with fast
        ns "If it's such a bad play, why include a review about it...?"

    elif scrolled(20, korean=16):
        
        show newmute annoyed2 with fast
        ns "...I don't get why Old *Mute included these..."

    elif scrolled(32, korean=26):
        show newmute annoyed with fast
        
    elif scrolled(1000):
        show newmute challenge with fast
        
    jump log_loop

label log_2_7_newmute:
    if pronouns == "she":
        if scrolled(8, korean=9) and not hateplus_newmute_because_lesbians:

            show newmute tsundere with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know {i}you{/i} like women."

            $ hateplus_newmute_because_lesbians = True

        elif scrolled(8, korean=9):
            show newmute hmphscb with fast
            ns "Hm..."

        elif scrolled(22, korean=23):
            show newmute upsetsc with fast

        elif scrolled(32, korean=33):
            show newmute sighsob with fast
            ns "...aw..."

        elif scrolled(53, korean=55):
            show newmute sorryscb with fast

        elif scrolled(67, korean=69):
            show newmute tensescb with fast
            ns "Yikes."

        elif scrolled(75, korean=79):
            show newmute upset3 with fast
            ns "...why are there such harsh economic circumstances for anyone on the {i}Mugunghwa{/i}...?"

        elif scrolled(91, korean=95):
            show newmute hmphscb with fast

        elif scrolled(103, korean=107):
            show newmute challengeso with fast
            ns "Oh... corruption. I see."

        elif scrolled(113, korean=117):
            if read("M4-3"):
                show newmute worry2 with fast
                ns "...so, like, {i}this{/i} was the effect of the Motherhood Credit Act, huh."
            else:
                show newmute sorrysob with fast
                ns "...oh..."

        elif scrolled(142, korean=146):
            show newmute sorryscb with fast

        elif scrolled(151, korean=156):
            show newmute sigh blush with fast
            ns "...well, okay, this is pretty awful."

        elif scrolled(1000):
            show newmute tired blush with fast

    
    else:
        if scrolled(10, korean=10):
            show newmute worry2 with fast
            ns "I don't think this sort of thing is important, sorry..."

        elif scrolled(150, korean=155):
            show newmute tired with fast

        elif scrolled(1000):
            show newmute sulk with fast

    jump log_loop

label log_2_8_newmute:
    if pronouns == "she":
        if scrolled(8, korean=10) and not hateplus_newmute_because_lesbians:

            show newmute tsundere with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know {i}you{/i} like women."

            $ hateplus_newmute_because_lesbians = True

        elif scrolled(8, korean=10):
            show newmute sorrysob with fast
            ns "But... they were so...!"
            # I think this response requires that you've read previous logs where they're cute together. - Raide

        elif scrolled(12, korean=16):
            show newmute sorryscb with fast

        elif scrolled(23, korean=26):
            show newmute upsetsc with fast

        elif scrolled(31, korean=34):
            show newmute upsetsob with fast
            ns "...oh..."

        elif scrolled(41, korean=45):
            show newmute upsetscb with fast
            ns "...I don't know what to make of this."

        elif scrolled(51, korean=55):
            show newmute tensesc with fast

        elif scrolled(67, korean=74):
            show newmute tensesob with fast
            ns "Harsh..."

        elif scrolled(78, korean=84):
            show newmute upset with fast
            ns "That sounds... like... really out of character. I don't believe it."

        elif scrolled(91, korean=100):
            show newmute hmphscb with fast

        elif scrolled(106, korean=116):
            if any_read("M6-6", "M2-9"):
                
                show newmute wow3 with fast
                ns "Wait... but that \"little sister\" people keep saying Ae-jeong has... that's actually her, right? They got back together, right?"
            else:
                
                show newmute sighsob with fast
                ns "...oh no..."

        elif scrolled(1000):
            show newmute worry with fast

    else:
        if scrolled(10, korean=11):
            show newmute tensesc with fast

        elif scrolled(106, korean=116):
            show newmute tensesc with fast

        elif scrolled(1000):
            show newmute tensesc with fast
        # FILL THIS IN
        # FILL IT - Raide


    jump log_loop

label log_2_9_newmute:
    if scrolled(12, korean=10):
        show newmute tenseso with fast
        ns "Huh..."

    elif scrolled(22, korean=20):
        show newmute tensesob with fast
        ns "Sounds like a waste...?"

    elif scrolled(31, korean=25):
        show newmute hmphsc with fast

    elif scrolled(41, korean=35):
        show newmute upsetscb with fast
        ns "...tch..."

    elif scrolled(52, korean=45):
        show newmute upsetsc with fast

    elif scrolled(60, korean=55):
        if pronouns == "she" and any_read("M2-7", "M2-8"):
            
            show newmute shame with fast
            ns "...so she still loved her! I knew it!"
        else:
            
            show newmute hmphso with fast
            ns "Okay..."

    elif scrolled(1000):
        show newmute disbelief blush with fast
        ns "So, like... that's how Ryu took control of the council, huh."

    jump log_loop

label log_4_1_newmute:
    if scrolled(8, korean=8):
        show newmute tenseso with fast
        ns "Okay..."

    elif scrolled(20, korean=20):
        show newmute tensesc with fast

    elif scrolled(32, korean=33):
        show newmute thought with fast

    elif scrolled(44, korean=44):
        show newmute neutralsc with fast

    elif scrolled(52, korean=53):
        show newmute tenseso with fast
        ns "...Queen Eun-a!"

    elif scrolled(64, korean=64):
        show newmute hmphsc with fast

    elif scrolled(74, korean=74):
        show newmute upset3 with fast
        ns "...wait, so {i}she{/i} was responsible for the switch to Chinese characters?"

    elif scrolled(92, korean=92):
        show newmute whatever with fast
        ns "...and, like, this was back in 4038! Geeze."

    elif scrolled(102, korean=102):
        show newmute tensescb with fast
        ns "Even Old *Mute had no idea..."

    elif scrolled(121, korean=121):
        show newmute upsetsc with fast

    elif scrolled(133, korean=132):
        show newmute sorrysc with fast

    elif scrolled(143, korean=142):
        show newmute wowsob with fast
        ns "Wow."

    elif scrolled(159, korean=158):
        show newmute sigh with fast

    elif scrolled(1000):
        show newmute annoyed with fast

    jump log_loop

label log_4_2_newmute:
    if scrolled(13, korean=8):
        show newmute hmphsc with fast
        ns "Hm..."

    elif scrolled(23, korean=21):
        show newmute tenseso with fast
        ns "...okay, so..."

    elif scrolled(44, korean=42):
        show newmute tensesc with fast

    elif scrolled(71, korean=68):
        show newmute whatscb with fast

    elif scrolled(92, korean=90):
        show newmute thought with fast

    elif scrolled(105, korean=102):
        show newmute wowsob with fast
        ns "Wow, Old *Mute was so... so..."

    elif scrolled(113, korean=109):
        show newmute wowsc with fast

    elif scrolled(132, korean=128):
        show newmute tensesc with fast

    elif scrolled(145, korean=142):
        show newmute hmphsc with fast

    elif scrolled(163, korean=160):
        show newmute wowscb with fast

    elif scrolled(173, korean=170):
        show newmute tsundere with fast
        ns "\"And that's how it's done, boys and girls.\" Wow, that swagger...!"

    elif scrolled(183, korean=181):
        show newmute disbelief with fast
        ns "Could I somehow live up to that...?"

    elif scrolled(206, korean=203):
        show newmute suspicious with fast

    elif scrolled(1000):
        show newmute sulk with fast

    jump log_loop

label log_4_3_newmute:
    if scrolled(10, korean=10):
        if read("M2-7"):
            
            show newmute hmphsob with fast
            ns "...so, like, this is the law that Mae Jin-a was crying about."
        else:
            
            show newmute hmphso with fast
            ns "So... was this part of his agenda, too?"

    elif scrolled(28, korean=28):
        show newmute tensesc with fast

    elif scrolled(38, korean=38):
        show newmute tenseso with fast
        ns "...huh..."

    elif scrolled(68, korean=68):
        show newmute hmphsc with fast

    elif scrolled(85, korean=86):
        show newmute upsetsc with fast

    elif scrolled(95, korean=96):
        show newmute upset3 with fast
        ns "...wait, but like, did it {i}actually{/i} cause a population increase?"

    elif scrolled(105, korean=106):
        show newmute whatscb with fast

    elif scrolled(115, korean=116):
        show newmute whatsob with fast
        ns "And Old *Mute takes charge again!"

    elif scrolled(137, korean=139):
        show newmute upsetsc with fast

    elif scrolled(147, korean=148):
        show newmute shame with fast
        ns "...so I guess in the end, like, it went through anyway?"

    elif scrolled(159, korean=161):
        show newmute worry with fast

    elif scrolled(170, korean=172):
        show newmute challenge with fast

    elif scrolled(190, korean=190):
        show newmute annoyed with fast

    elif scrolled(1000):
        show newmute tired with fast

    jump log_loop

label log_4_4_newmute:
    if scrolled(6, korean=5):
        show newmute tensesob with fast
        ns "Okay..."

    elif scrolled(16, korean=15):
        show newmute upset3 with fast
        ns "...wait, but what about, like, noble women, though?"

    elif scrolled(43, korean=41):
        show newmute hmphsc with fast

    elif scrolled(52, korean=50):
        show newmute tensesc with fast

    elif scrolled(1000):
        show newmute suspicious with fast

    jump log_loop

label log_4_5_newmute:
    if scrolled(10, korean=9):
        if True:
            
            show newmute hmphsob with fast
            ns "So... this is where the balance of power swung, huh."
        else:
            
            show newmute hmphso with fast
            ns "Huh... I get the impression this is really important..."

    elif scrolled(26, korean=24):
        show newmute tensescb with fast
        ns "...okay..."

    elif scrolled(36, korean=33):
        show newmute upset3 with fast
        ns "...oh, geeze. Queen Eun-a could directly influence who was on council...? Of course!"

    elif scrolled(67, korean=62):
        show newmute tensesc with fast

    elif scrolled(82, korean=77):
        show newmute upsetsc with fast

    elif scrolled(92, korean=88):
        show newmute whatever with fast
        ns "...Old *Mute, you idiot!"

    elif scrolled(102, korean=98):
        show newmute sighsob with fast
        ns "...like, I was an idiot, even..."

    elif scrolled(124, korean=121):
        show newmute upsetsc with fast

    elif scrolled(135, korean=133):
        show newmute tensescb with fast
        ns "...okay..."

    elif scrolled(150, korean=148):
        show newmute tch with fast
        ns "All this intense debate... and about, like, all the wrong things..."

    elif scrolled(174, korean=170):
        show newmute suspicious with fast

    elif scrolled(184, korean=180):
        show newmute disbelief blush with fast
        ns "Okay, sure..."

    elif scrolled(194, korean=189):
        show newmute annoyed with fast

    elif scrolled(214, korean=212):
        show newmute sigh with fast

    elif scrolled(238, korean=235):
        show newmute suspicious blush with fast

    elif scrolled(253, korean=250):
        show newmute worry3 with fast
        ns "...oh no..."

    elif scrolled(1000):
        show newmute tired blush with fast

    jump log_loop

label log_4_6_newmute:
    if scrolled(10, korean=11):
        show newmute wowsob with fast
        ns "Rude...!"

    elif scrolled(25, korean=25):
        show newmute tensesc with fast

    elif scrolled(38, korean=37):
        show newmute hmphsc with fast

    elif scrolled(53, korean=52):
        show newmute upset3 with fast
        ns "...wow... she was really beleaguered by them, wasn't she..."

    elif scrolled(63, korean=62):
        show newmute whatsob with fast
        ns "...but..."

    elif scrolled(86, korean=87):
        show newmute upsetsc with fast

    elif scrolled(95, korean=96):
        show newmute hmphsc with fast

    elif scrolled(105, korean=105):
        show newmute upset2 with fast
        ns "...like, nobody's taking her seriously, are they..."

    elif scrolled(114, korean=114):
        show newmute sorrysc with fast

    elif scrolled(124, korean=124):
        show newmute hmphso with fast
        ns "...well, in the end, peasants couldn't use computers anyway."

    elif scrolled(143, korean=144):
        show newmute tensescb with fast

    elif scrolled(153, korean=154):
        show newmute sorrysob with fast

    elif scrolled(173, korean=172):
        show newmute sighsob with fast

    elif scrolled(189, korean=190):
        show newmute whatscb with fast

    elif scrolled(199, korean=200):
        show newmute tensesob with fast
        ns "...ugh..."

    elif scrolled(209, korean=210):
        show newmute give up with fast
        ns "...all that arguing she did... was it all for nothing?"

    elif scrolled(245, korean=245):
        show newmute worry with fast

    elif scrolled(1000):
        show newmute tired with fast

    jump log_loop

label log_4_7_newmute:
    if scrolled(14, korean=11):
        show newmute thought with fast

    elif scrolled(27, korean=23):
        show newmute wowsc with fast
        ns "...huh..."

    elif scrolled(44, korean=40):
        show newmute neutralsc with fast

    elif scrolled(54, korean=51):
        show newmute wow with fast
        ns "...like, I don't understand why it's elder sons, either..."

    elif scrolled(88, korean=82):
        show newmute hmphsc with fast

    elif scrolled(1000):
        show newmute suspicious with fast

    jump log_loop

label log_4_8_newmute:
    if scrolled(8, korean=9):
        show newmute tensesob with fast
        ns "Wow..."

    elif scrolled(18, korean=20):
        show newmute upsetscb with fast
        ns "...this is just a mess."

    elif scrolled(41, korean=42):
        show newmute hmphsc with fast

    elif scrolled(62, korean=63):
        show newmute tensescb with fast

    elif scrolled(80, korean=81):
        show newmute sorrysc with fast

    elif scrolled(100, korean=102):
        show newmute hmphsc with fast

    elif scrolled(120, korean=122):
        show newmute sigh with fast

    elif scrolled(135, korean=137):
        show newmute suspicious with fast

    elif scrolled(1000):
        show newmute sulk with fast

    jump log_loop

label log_4_9_newmute:
    if scrolled(10, korean=10):
        show newmute challenge3 with fast
        ns "So... like, this is the law that let Ryu become both Chief Councillor and President, right?"

    elif scrolled(23, korean=24):
        show newmute challengesc with fast

    elif scrolled(33, korean=33):
        show newmute tensescb with fast
        ns "...she didn't even realize..."

    elif scrolled(48, korean=49):
        show newmute challengesc with fast

    elif scrolled(58, korean=59):
        if True:
            
            show newmute resent with fast
            ns "They were all in his pocket, weren't they? Like, she didn't have a chance..."
        else:
            
            show newmute tensescb with fast
            ns "Ugh..."

    elif scrolled(82, korean=83):
        show newmute upsetsc with fast

    elif scrolled(103, korean=105):
        show newmute upsetscb with fast

    elif scrolled(128, korean=131):
        show newmute sorrysob with fast

    elif scrolled(142, korean=145):
        show newmute whatscb with fast

    elif scrolled(152, korean=155):
        show newmute shame with fast
        ns "...if even someone like her was defeated like that..."

    elif scrolled(176, korean=177):
        show newmute pout with fast

    elif scrolled(1000):
        show newmute sigh blush with fast
        ns "...like, this is just awful."

    jump log_loop

label log_5_1_newmute:
    if pronouns == "he":
        if scrolled(8, korean=7) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(8, korean=7):
            show newmute neutralso with fast
            ns "...okay..."

        elif scrolled(19, korean=20):
            show newmute thought with fast
            
        elif scrolled(27, korean=28):
            show newmute neutralsc with fast
            
        elif scrolled(37, korean=37):
            show newmute wowscb with fast
            ns "Hm..."

        elif scrolled(49, korean=50):
            show newmute wow3 with fast
            ns "...sounds pretty different from what most of the {i}Mugunghwa{/i} logs describe..."

        elif scrolled(1000):
            show newmute disbelief blush with fast
            ns "Are those good qualities in a man...?"

    else:
        if scrolled(10, korean=10):
            show newmute query with fast
            ns "Boring..."

        elif scrolled(52, korean=53):
            show newmute think with fast
            
        elif scrolled(1000):
            show newmute neutral with fast
            
    jump log_loop

label log_5_2_newmute:
    if pronouns == "he":
        if scrolled(8, korean=8) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(8, korean=8):
            show newmute neutralsc with fast
            ns "Hm..."

        elif scrolled(18, korean=17):
            show newmute hmm with fast
            
        elif scrolled(30, korean=29):
            show newmute thought with fast
            
        elif scrolled(36, korean=35):
            show newmute wowsc with fast
            
        elif scrolled(43, korean=42):
            show newmute wowsob with fast
            ns "Oh...!"

        elif scrolled(1000):
            show newmute suspicious blush with fast
            
    else:
        if scrolled(10, korean=10):
            show newmute tsundere with fast
            ns "Yeah, yeah, domestic bliss, whatever."

        elif scrolled(43, korean=42):
            show newmute serious with fast
            
        elif scrolled(1000):
            show newmute neutral3 with fast
            
    jump log_loop

label log_5_3_newmute:
    if True:#pronouns == "he":
        if scrolled(8, korean=6) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(8, korean=6):
            show newmute neutralsc with fast
            ns "...okay..."

        elif scrolled(20, korean=17):
            show newmute hmphsc with fast
            
        elif scrolled(40, korean=37):
            show newmute tensesc with fast
            
        elif scrolled(51, korean=47):
            if not any_read("M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"):
                
                show newmute tenseso with fast
                ns "Sure, sure..."
            else:
                
                show newmute hmm2 with fast
                ns "Wow, that would have serious ramifications if true..."

        elif scrolled(61, korean=57):
            show newmute whatsob with fast
            ns "What...?"

        elif scrolled(71, korean=68):
            show newmute upsetsob with fast
            ns "...ugh! Disgusting!"

        elif scrolled(81, korean=77):
            show newmute tensescb with fast
            ns "This is horrifying!"

        elif scrolled(91, korean=89):
            show newmute upsetscb with fast
            ns "...ugh..."

        elif scrolled(112, korean=109):
            show newmute upsetsc with fast
            
        elif scrolled(131, korean=127):
            show newmute sorryscb with fast
            
        elif scrolled(162, korean=157):
            show newmute sighscb with fast
            
        elif scrolled(182, korean=177):
            show newmute upsetsc with fast
            
        elif scrolled(192, korean=187):
            show newmute bitter with fast
            ns "...what kind of society would just let that sort of thing happen...?"

        elif scrolled(1000):
            show newmute sigh blush with fast
            ns "...like... I don't know."

    else:
        if scrolled(10, korean=8):
            show newmute worry3 with fast
            ns "...um, I don't want to read this one, okay? It gets too intense."

        elif scrolled(198, korean=190):
            show newmute tired blush with fast
            
        elif scrolled(1000):
            show newmute worry with fast
            
    jump log_loop

label log_5_4_newmute:
    if pronouns == "he":
        if scrolled(10, korean=6) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(10, korean=6):
            show newmute hmphsob with fast
            ns "Okay..."

        elif scrolled(19, korean=15):
            show newmute hmphsc with fast
            
        elif scrolled(29, korean=23):
            if read("M4-3"):
                
                show newmute troubled with fast
                ns "...so {i}that's{/i} the real consequence of the Motherhood Credit Act, huh..."
            else:
                
                show newmute tensesob with fast
                ns "...is that true...?"

        elif scrolled(40, korean=34):
            show newmute upsetsc with fast
            
        elif scrolled(62, korean=57):
            show newmute sorryscb with fast
            
        elif scrolled(75, korean=70):
            show newmute sigh blush with fast
            ns "Well, that's awkward."

        elif scrolled(1000):
            show newmute pout with fast
            
    else:
        if scrolled(10, korean=6):
            show newmute talk4 with fast
            ns "You can go ahead, but like, I don't care about this sort of thing..."

        elif scrolled(75, korean=70):
            show newmute think with fast
            
        elif scrolled(1000):
            show newmute challenge with fast
            
    jump log_loop

label log_5_5_newmute:
    if pronouns == "he":
        if scrolled(8, korean=7) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(8, korean=7):
            show newmute tensescb with fast
            ns "...yikes..."

        elif scrolled(15, korean=12):
            show newmute upsetsc with fast
            
        elif scrolled(24, korean=21):
            show newmute upset3 with fast
            ns "...isn't that kind of too important a thing to ignore...?"

        elif scrolled(39, korean=35):
            show newmute upsetscb with fast
            ns "...ugh..."

        elif scrolled(49, korean=45):
            show newmute upsetsob with fast
            ns "Gross!"

        elif scrolled(65, korean=62):
            show newmute sorryscb with fast
            
        elif scrolled(77, korean=74):
            show newmute upsetsc with fast
            
        elif scrolled(90, korean=89):
            show newmute sighscb with fast
            
        elif scrolled(110, korean=110):
            show newmute hmphscb with fast
            
        elif scrolled(130, korean=124):
            show newmute sorryscb with fast
            
        elif scrolled(140, korean=139):
            show newmute wowsob with fast
            ns "...he's really supportive, isn't he?"

        elif scrolled(150, korean=149):
            show newmute hmm2 with fast
            ns "So... um, is that what having a husband's like...?"

        elif scrolled(160, korean=157):
            show newmute sorrysob with fast
            ns "...well, I know I could use someone supportive like that."

        elif scrolled(1000):
            show newmute pout with fast
            
    else:
        if scrolled(10, korean=9):
            show newmute worry2 with fast
            ns "Um, I'm really more interested in stuff that's, like, about the old me..."

        elif scrolled(163, korean=160):
            show newmute tired with fast
            
        elif scrolled(1000):
            show newmute suspicious blush with fast

    jump log_loop

label log_5_6_newmute:
    if pronouns == "he":
        if scrolled(9, korean=10) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(9, korean=10):
            show newmute tensescb with fast
            ns "...okay..."

        elif scrolled(17, korean=18):
            show newmute hmphsc with fast
            
        elif scrolled(27, korean=28):
            show newmute upsetscb with fast
            ns "...geeze..."

        elif scrolled(46, korean=50):
            show newmute upsetsc with fast
            
        elif scrolled(63, korean=68):
            show newmute sorrysc with fast
            
        elif scrolled(73, korean=76):
            show newmute upset3 with fast
            ns "Like, why is it just all about physical affection...?"

        elif scrolled(107, korean=114):
            show newmute sighscb with fast
            
        elif scrolled(117, korean=125):
            show newmute tensesob with fast
            ns "...well... he's trying, I guess..."

        elif scrolled(126, korean=135):
            show newmute upsetsc with fast
            
        elif scrolled(136, korean=145):
            show newmute hmphsob with fast
            ns "...um..."

        elif scrolled(146, korean=154):
            show newmute whatsob with fast
            ns "Wait, is she... like...?"

        elif scrolled(156, korean=165):
            show newmute tensesob with fast
            ns "Oh, geeze, she totally is!"

        elif scrolled(168, korean=177):
            show newmute sorryscb with fast
            
        elif scrolled(178, korean=186):
            show newmute wowsob with fast
            ns "...oh..."

        elif scrolled(1000):
            show newmute sigh blush with fast
            ns "But... I do, like, think it's really sweet that he's trying. I'd respect that a lot."

    else:
        if scrolled(10, korean=11):
            show newmute talk4 with fast
            ns "Generic husband writing, skipped..."

        elif scrolled(177, korean=186):
            show newmute think with fast

        elif scrolled(1000):
            show newmute sulk with fast

    jump log_loop

label log_5_7_newmute:
    if pronouns == "he":
        if scrolled(10, korean=8) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True
        elif scrolled(10, korean=8):
            show newmute upset3 with fast
            ns "Ugh, I don't want to read about that mass-murderer! Like, *Mute wouldn't have died if not for her... unforgivable!"

        elif scrolled(16, korean=13):
            show newmute hmphscb with fast
            
        elif scrolled(26, korean=22):
            show newmute whatever with fast
            ns "...oh..."

        elif scrolled(36, korean=32):
            show newmute tensesob with fast
            ns "\"Earthborn brilliance\"...? What, like, are men from Earth smarter...?"

        elif scrolled(47, korean=42):
            show newmute tensesc with fast
            
        elif scrolled(57, korean=52):
            show newmute hmphso with fast
            ns "...sure, okay, whatever..."

        elif scrolled(67, korean=62):
            show newmute sighsob with fast
            ns "\"Peaceful.\" Ha, if only."

        elif scrolled(75, korean=70):
            show newmute tensesc with fast
            
        elif scrolled(90, korean=83):
            show newmute thought with fast
            
        elif scrolled(1000):
            show newmute shame with fast
            ns "...too bad it didn't matter in the end."

    else:
        if scrolled(10, korean=8):
            show newmute give up with fast
            ns "Ugh, I don't want to read about that mass-murderer! Like, *Mute wouldn't have died if not for her... unforgivable!"

        elif scrolled(93, korean=86):
            show newmute tired with fast
            
        elif scrolled(1000):
            show newmute worry side with fast
            
    jump log_loop

label log_5_8_newmute:
    if pronouns == "he":
        if scrolled(8, korean=7) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(8, korean=7):
            show newmute hmphso with fast
            ns "...okay..."

        elif scrolled(15, korean=14):
            show newmute hmphsc with fast
            
        elif scrolled(23, korean=22):
            show newmute tenseso with fast
            ns "...is it really supposed to be surprising people are scared to talk to her...?"

        elif scrolled(32, korean=30):
            show newmute upsetsc with fast
            
        elif scrolled(1000):
            show newmute damn with fast
            ns "Wait, though... she confirmed that? So... like, that would have killed everyone in the end, no matter what...?!"

    else:
        if scrolled(10, korean=9):
            show newmute disbelief blush with fast
            ns "I don't, um, really care about this sort of thing..."

        elif scrolled(32, korean=30):
            show newmute suspicious with fast
            
        elif scrolled(1000):
            show newmute damn with fast
            ns "Wait, though... she confirmed that? So... like, that would have killed everyone in the end, no matter what...?!"

    jump log_loop

label log_5_9_newmute:
    if pronouns == "he":
        if scrolled(8, korean=5) and not hateplus_newmute_because_men:

            show newmute annoyed2 with fast
            ns "Okay, fine, I'll read this one with you, but... only because I know *Mute thought being a wife was important."

            $ hateplus_newmute_because_men = True

        elif scrolled(8, korean=5):
            show newmute sorrysc with fast
            
        elif scrolled(18, korean=15):

            show newmute sighsob with fast
            ns "...it's really rough to hear that..."

        elif scrolled(25, korean=22):
            show newmute tensesc with fast
            
        elif scrolled(35, korean=32):
            show newmute troubled with fast
            ns "I guess... like, it's just as important for a wife to be supportive too, huh..."

        elif scrolled(44, korean=40):
            show newmute sorrysc with fast
            
        elif scrolled(58, korean=55):
            show newmute tensescb with fast
            ns "...ouch..."

        elif scrolled(71, korean=68):
            show newmute sorryscb with fast
            
        elif scrolled(81, korean=78):
            show newmute sighsob with fast
            ns "Like... I feel like I should be learning something from this, but I don't know what..."

        elif scrolled(97, korean=96):
            show newmute upsetsc with fast
            
        elif scrolled(115, korean=114):
            show newmute sorrysob with fast
            ns "Oh..."

        elif scrolled(126, korean=126):
            show newmute hmphscb with fast
            
        elif scrolled(136, korean=136):
            show newmute bitter with fast
            ns "...oh, geeze, except this dates to right before Queen Eun-a destroyed everything...!"

        elif scrolled(1000):
            show newmute worry2 with fast
            ns "...is that enough...?"

    else:
        if scrolled(10, korean=7):
            show newmute worry3 with fast
            ns "...I don't want to bother with this, okay...?"

        elif scrolled(20, korean=17):
            show newmute cry with fast
            ns "...it's not like her work ever amounted to anything! It all got erased, anyway..."

        elif scrolled(142, korean=142):
            show newmute tired blush with fast
            
        elif scrolled(1000):
            show newmute worry with fast
            
    jump log_loop

label log_6_1_newmute:
    if scrolled(10, korean=10):
        
        show newmute upset2 with fast
        ns "So... like, this is where it started to all fall apart, huh..."

    elif scrolled(20, korean=20):
        if read("M6-7"):
            
            show newmute hatesc with fast
            ns "...all that, thanks to Queen Eun-a..."
        else:
            
            show newmute whatever with fast
            ns "...geeze..."

    elif scrolled(30, korean=30):
        show newmute hmphscb with fast
    
    elif scrolled(40, korean=41):
        show newmute hmm2 with fast
        ns "...so, Old *Mute really looked after her family, huh..."

    elif scrolled(46, korean=47):
        show newmute tensesc with fast
    
    elif scrolled(55, korean=56):
        show newmute upsetsob with fast
        ns "Of course it was a power play! Ugh, why did you dismiss that idea...?!"

    elif scrolled(64, korean=67):
        show newmute sigh blush with fast
    
    elif scrolled(1000):
        show newmute worry side with fast
    
    jump log_loop

label log_6_2_newmute:
    if scrolled(6, korean=7):
        show newmute upsetscb with fast
        ns "...oh no."

    elif scrolled(12, korean=13):
        show newmute upsetsc with fast
    
    elif scrolled(22, korean=24):
        show newmute hatesc with fast
        ns "...ugh..."

    elif scrolled(41, korean=44):
        show newmute challengesc with fast
    
    elif scrolled(53, korean=56):
        show newmute challengeso with fast
        ns "Wow... Seo-yeong sure had anger issues... although I guess I can't blame her."

    elif scrolled(68, korean=73):
        show newmute tensescb with fast
    
    elif scrolled(83, korean=88):
        show newmute hateso with fast
        ns "...geeze!"

    elif scrolled(110, korean=116):
        show newmute upsetscb with fast
    
    elif scrolled(135, korean=142):
        show newmute sighsob with fast
    
    elif scrolled(145, korean=153):
        show newmute challenge4 with fast
        ns "...you know, this isn't the way Queen Eun-a made it sound in her eulogy at all...!"

    elif scrolled(155, korean=163):
        show newmute sorrysob with fast
        ns "Right... it was the old me that she loved..."

    elif scrolled(175, korean=186):
        show newmute sorryscb with fast
    
    elif scrolled(185, korean=196):
        show newmute sigh blush with fast
        ns "Okay... so I'm capable of falling in love, then! What a relief..."

    elif scrolled(195, korean=207):
        show newmute disbelief blush with fast
        ns "...oh... or maybe it's not a relief."

    elif scrolled(215, korean=229):
        show newmute tired blush with fast
    
    elif scrolled(229, korean=243):
        show newmute pout with fast
    
    elif scrolled(240, korean=255):
        show newmute tensesc with fast
    
    elif scrolled(250, korean=266):
        show newmute shame with fast
    
    elif scrolled(260, korean=277):
        show newmute upset3 with fast
        ns "...I guess this isn't really the sort of thing *Mute would approve of, right?"

    elif scrolled(271, korean=289):
        show newmute tensesob with fast
        ns "But Old *Mute did... I don't know what I should think."

    elif scrolled(281, korean=301):
        show newmute sighsob with fast
        ns "Those are tough words, but... like... in the end, they were just words..."

    elif scrolled(1000):
        show newmute tired with fast
    
    jump log_loop

label log_6_3_newmute:
    if scrolled(10, korean=11):
        show newmute tch with fast
        ns "Okay, fine... I'd rather read things about me, though!"

    elif scrolled(70, korean=73):
        show newmute annoyed with fast
    
    elif scrolled(1000):
        show newmute challenge with fast
    
    jump log_loop

label log_6_4_newmute:
    if scrolled(10, korean=6):
        show newmute sorrysob with fast
        ns "...ugh, geeze, Seo-yeong..."

    elif scrolled(20, korean=16):
        show newmute sorrysc with fast
    
    elif scrolled(30, korean=27):
        show newmute tensescb with fast
        ns "...yeah..."

    elif scrolled(41, korean=38):
        show newmute tensesc with fast
    
    elif scrolled(51, korean=49):
        show newmute upsetscb with fast
        ns "This kind of situation..."

    elif scrolled(80, korean=77):
        show newmute upsetsc with fast
        # order to arrest
    
    elif scrolled(97, korean=94):
        show newmute hmphscb with fast
        # heo counters
    
    elif scrolled(113, korean=110):
        show newmute wowscb with fast
        # they're going to arrest the president?!
    
    elif scrolled(149, korean=146):
        show newmute tensescb with fast
        # conspiracy with Ryu
    
    elif scrolled(162, korean=160):
        show newmute sighsob with fast
        # breath of relief
    
    elif scrolled(174, korean=172):
        show newmute tensescb with fast
        # more insults
    
    elif scrolled(182, korean=180):
        show newmute wowscb with fast
        # heo exploding
    
    elif scrolled(200, korean=199):
        show newmute hmphscb with fast
        # watching the president being arrested
    
    elif scrolled(214, korean=214):
        show newmute tensesc with fast
        # accusation of fixing the election
    
    elif scrolled(220, korean=220):
        show newmute disbelief blush with fast
        ns "...well, like, I'm impressed that they were able to deal with it while blindsided?"

    elif scrolled(226, korean=226):
        show newmute worry3 with fast
        ns "I don't know what I'd do in that situation..."

    elif scrolled(232, korean=233):
        show newmute tsundere with fast
        ns "...Seo-yeong seems pretty cool, too, really..."

    elif scrolled(236, korean=236):
        show newmute sigh blush with fast
        ns "...okay..."

    elif scrolled(1000):
        show newmute worry2 with fast
        ns "...it all just got worse for them at this point, didn't it?"

    jump log_loop

label log_6_5_newmute:
    if scrolled(8, korean=8):
        show newmute tensesob with fast
        ns "...yeah, sure did..."

    elif scrolled(20, korean=21):
        show newmute sorrysc with fast
    
    elif scrolled(30, korean=31):
        show newmute sighsob with fast
        ns "I guess there's been a lot of disasters in {i}Mugunghwa{/i} history, huh..."
    
    elif scrolled(44, korean=45):
        show newmute wowscb with fast

    elif scrolled(61, korean=63):
        show newmute sorryscb with fast
    
    elif scrolled(74, korean=77):
        show newmute wowsc with fast
    
    elif scrolled(89, korean=93):
        show newmute craftyscb with fast
    
    elif scrolled(100, korean=103):
        show newmute whatscb with fast
        ns "...huh..."

    elif scrolled(113, korean=116):
        show newmute upset3 with fast
        ns "So... like, what's the right age to \"handle that shit\", then...?"

    elif scrolled(128, korean=131):
        show newmute upset2 with fast
        ns "...it's even scarier not having any years of experience, I promise!"
    
    elif scrolled(136, korean=138):
        show newmute upsetsc with fast
    
    elif scrolled(161, korean=162):
        show newmute hmphscb with fast
    
    elif scrolled(172, korean=171):
        show newmute worry3 with fast
        ns "Well, I guess if even they were scared... maybe I shouldn't feel bad that I am too."

    elif scrolled(1000):
        show newmute worry with fast
    
    jump log_loop

label log_6_6_newmute:
    if scrolled(5, korean=3):
        show newmute tensesc with fast
        ns "Hm..."

    elif scrolled(15, korean=13):
        show newmute neutralso with fast
        ns "No pants, huh? Sounds like a party the old version of me would have liked."

    elif scrolled(25, korean=23):
        show newmute wowsc with fast
    
    elif scrolled(35, korean=33):
        show newmute hmm2 with fast
        ns "So... \"little sister\" is actually code for \"lesbian lover\", then, right?"
        # I think you need to read 13_8 for this to trigger? - Raide
        
    elif scrolled(54, korean=52):
        show newmute hmphsc with fast
    
    elif scrolled(1000):
        show newmute tch with fast
        ns "Ugh... unpleasant."

    jump log_loop

label log_6_7_newmute:
    if scrolled(8, korean=5):
        show newmute upsetsc with fast

    elif scrolled(18, korean=16):
        show newmute upset3 with fast
        ns "Oh, geeze... so that's what rendered Old *Mute completely powerless..."
    
    elif scrolled(27, korean=24):
        show newmute hmphsc with fast
    
    elif scrolled(51, korean=47):
        show newmute tensesc with fast
        # legislation proposed by Ryu?
    
    elif scrolled(74, korean=68):
        show newmute whatscb with fast
        # legislation always proposed by someone else
    
    elif scrolled(82, korean=76):
        show newmute upsetsc with fast
        # it's all power play by Ryu
    
    elif scrolled(92, korean=87):
        show newmute upsetsob with fast
        ns "Ugh... like, of course!"

    elif scrolled(102, korean=97):
        show newmute sighsob with fast
        ns "...but, like, I don't think I would have made it at the time, either...!"

    elif scrolled(127, korean=123):
        show newmute sorrysc with fast
        # some more theories
    
    elif scrolled(143, korean=140):
        show newmute tensescb with fast
        ns "...okay..."
        # they're going to read the private logs

    elif scrolled(156, korean=154):
        show newmute upset2 with fast
        ns "...ugh, is there anything they even could've done differently...?"

    elif scrolled(170, korean=167):
        show newmute challengesc with fast
        # search for logs that incriminate Ryu
    
    elif scrolled(183, korean=179):
        show newmute wowsc with fast
        # stop mid-sentence? what is it?
    
    elif scrolled(202, korean=200):
        show newmute tensescb with fast
        # very tense
    
    elif scrolled(212, korean=210):
        show newmute hateso with fast
        ns "Queen Eun-a..."

    elif scrolled(1000):
        show newmute challenge2 with fast
        ns "What am I supposed to make of the woman that *Mute trusted the most, and betrayed Old *Mute the most? How should I feel...?!"

    jump log_loop

label log_6_8_newmute:
    if scrolled(10, korean=13):
        show newmute hmphso with fast
        ns "Well, like... maybe she should have found the time, considering..."

    elif scrolled(20, korean=27):
        show newmute hmphsc with fast
    
    elif scrolled(30, korean=37):
        show newmute sorryso with fast
        ns "...okay..."

    elif scrolled(40, korean=48):
        show newmute tensesc with fast
    
    elif scrolled(50, korean=58):
        show newmute apologize with fast
        ns "Is that what *Mute was thinking, when she...? \"Can't live forever\"?"

    elif scrolled(68, korean=80):
        show newmute sorrysc with fast
    
    elif scrolled(78, korean=90):
        show newmute sighsob with fast
        ns "...I like how protective she is, though..."

    elif scrolled(100, korean=111):
        show newmute tensesc with fast
    
    elif scrolled(110, korean=123):
        show newmute upset3 with fast
        ns "Too strong to be scared of anything... is it even possible?"

    elif scrolled(120, korean=133):
        show newmute upsetscb with fast
        ns "...well, okay... maybe I can try..."

    elif scrolled(141, korean=153):
        show newmute hmphsc with fast
    
    elif scrolled(159, korean=173):
        show newmute upsetsc with fast
    
    elif scrolled(169, korean=183):
        show newmute sob with fast
        ns "...all this planning... all this confidence..."

    elif scrolled(1000):
        show newmute insecure with fast
        ns "...in the end, it was really all for nothing, wasn't it?"

    jump log_loop

label log_6_9_newmute:
    if scrolled(10, korean=9):
        show newmute bitter with fast
        ns "...it's... really fucked up, isn't it...? I don't want to reread it..."

    elif scrolled(445, korean=450):
        show newmute tired blush with fast
    
    elif scrolled(1000):
        show newmute worry with fast
    
    jump log_loop