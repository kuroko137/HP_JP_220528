# CHRISTINE, WRITE THOSE FUCKING EMAILS

label hateplus_hyunae_start:
    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop

    # show hyunae cheer with fast

    # hh "Hey, hey! Investigator, investigator!"

    # show hyunae troubled2 with fast

    # hh "You know how nobody knows what happened on the Mugunghwa between its launch and the year zero, right?"

    # show hyunae question with fast

    # hh "I thought the answer was lost forever, but... I just stumbled across a bunch of records from then!"

    # $ renpy.pause(2.0)

    # show hyunae flirt with fast

    # hh "Please, please, can we investigate together? I'd make a great sidekick, I promise!"

    # $ renpy.pause(2.0) 

    #jump end_shown
    #jump hateplus_hyunae_cake

    # looking, taps on screen, horrifed realization
    
    show hyunae pity with fast
    hh "...oh no!"

    # menu:
    #     hh_vn "...what do I say, what do I say, what do I say?"
    #     "VN":
    #         pass
        
    #     "\"If I could survive culture shock, you can too!\"@hyunae insist":
            
    #         pass
        
    #     "\"Don't make me have to figure out Earth while also mourning you!\"@hyunae anxious":
            
    #         pass

    #     "\"I don't know.\"@hyunae question2":
    #         pass
    
    show hyunae surrender blush with fast
    hh "Oh no, oh no, oh no, geeze. I'm so sorry."
    
    show hyunae bitter
    hh "If you're saying something to me, I can't hear you at all!"
    
    show hyunae oops with fast
    hh "Oh geeze... I'll explain, I'll explain!"
    
    show hyunae serious blush
    hh "Um, so... well! I tried installing that advanced dictionary you got for me!"
    
    show hyunae sulk2
    hh "...and, uh..."
    
    show hyunae sigh blush with fast
    hh "...well, I couldn't get it to work."
    
    show hyunae flustered
    hh "Even the builds that were supposed to be fine just kept giving me an 'architecture not supported' error! I don't know why!"
    
    show hyunae bittersob
    hh "So I tried to recompile my language processing functions so I could support it, but I don't really understand how AIs work very well, I guess."
    
    show hyunae emo
    hh "...anyway, um, what I'm trying to say is..."
    
    show hyunae lost with fast
    hh "...I guess I sort of just broke it more."
    
    show hyunae flustered with fast
    hh "Like I said before, if you're saying anything, I can't hear you! And every time I try to run an English->Korean translation, it just comes out as nonsense!"
    
    show hyunae grumpy
    hh "For example, if I try to translate your ship's name from English, I get í˜¸ì™€ì´ë‘ ë¸Œë¦°ì„¸ìŠ¤, which I can't really understand."
    
    show hyunae sigh blush
    hh "It's just like before, when I was back on the {i}Mugunghwa{/i} and I couldn't parse what you were saying."
    
    show hyunae hopeless
    menu:
        hh "Sorry... are you mad at me?"
        
        "Yes, I'm mad@hyunae bitter2":
            $ store.tsun += 1
            
            if tsundere():
                
                show hyunae sad with fast
                hh "Really, I'm sorry... I didn't mean to... please don't be mad!"
            else:
                
                show hyunae troubled2 with fast
                hh "Geeze, you don't have to be so harsh... it hurts me, too!"
        
        "I'm just sorry too@hyunae pout2":
            $ store.dere += 1
            
            show hyunae apologize blush with fast
            hh "Thanks... I'm glad you understand."
        
        "It doesn't matter@hyunae weak3":
            
            show hyunae annoyed blush with fast
            hh "What? Don't say that, yes it does!"
            
            if store.use_ending == "ending2":
                
                show hyunae pout
                hh "It means we can't communicate properly... if we're in a real relationship, I think that's important."
            else:
                
                show hyunae sigh
                hh "It means we can't communicate properly... if we're going to be friends, I think that's important."
    
    show hyunae shame with fast
    menu:
        hh "We'll be able to get it fixed once we get to Earth, right? Right?!"
        
        "Of course@hyunae cautious2":
            
            show hyunae apologize blush with fast
            hh "That's a relief... I don't know what I'd do if this was permanent."
        
        "No{k=2}{/k}@hyunae unsure":
            
            show hyunae flustered2 with fast
            hh "What?!"
            
            show hyunae annoyed blush
            menu:
                hh "Are you sure?!"
                
                "We'll figure something out@hyunae stare2":
                    
                    show hyunae pout with fast
                    hh "Oh! Geeze, don't scare me like that!"
                    
                    show hyunae baffled with fast
                    hh "That's a relief... I don't know what I'd do if this was permanent."
                    
                "We won't@hyunae bitter2":
                    $ store.tsun += 1

                    show hyunae afraid with fast
                    hh "That's..."
                    
                    show hyunae mad blush
                    hh "You're just being mean, right?"
                    
                    show hyunae give up with fast
                    hh "Stop taunting me like that!"
                    
                    show hyunae defensive
                    hh "I'm really upset by this! That's not something to taunt someone with... geeze..."
                    
                    show hyunae angry blush
                    hh "Why would you do that?!"
                    
                    show hyunae baffled with fast
                    hh "...anyway..."
                
                "I don't know@hyunae hopeless2":
                    
                    show hyunae troubled2 with fast
                    hh "Oh... very well..."
                    
                    show hyunae disappoint2
                    hh "Well, I sure hope so..."
        
        "I don't know@hyunae anxious":
            
            show hyunae troubled2
            hh "Oh... very well..."
            
            show hyunae disappoint2
            hh "I sure hope so..."
    
    #hh "I guess we'll just have to sort it out at the time we sort out getting me a body."
    
    show hyunae tsundere with fast
    hh "Well, I waited over six hundred years to meet you, didn't I?"
    
    show hyunae hmph3 with fast
    hh "Three days? That's nothing!"
    
    show hyunae explain
    hh "Anyway! There's something else you should know!"
    
    show hyunae hard
    hh "While I was looking through my code, trying to debug my damage, I found a big block of data that I thought was garbage."
    
    show hyunae hmmcob
    hh "It's not garbage, though! It's data! For some reason, it seems to be embedded in my source... I'm not really sure why. It's not part of my memories, it's in the actual machine code, for some reason."
    
    show hyunae serious blush with fast
    hh "Um, the important thing is, though... I think it's log files from the {i}Mugunghwa{/i}!"
    
    show hyunae hard with fast
    hh "They have datestamps on them, and they seem to be from before the year 0. Well, I can't actually read them without extracting them, but that's what the index says."
    
    show hyunae tough2 with fast
    hh "It's really exciting! \"What happened in year 0 that made everyone forget?\" was always the big mystery to me... maybe these will explain!"
    
    show hyunae sure blush with fast 
    hh "Here's what I'm thinking... maybe we can't communicate, but we could still go through those together!"
    
    show hyunae confident
    menu:
        hh "What do you think, [title]Investigator? Can I be your sidekick again~?"
        
        "Of course!@hyunae confident2":
            $ store.dere += 1
            
            show hyunae genki with fast
            hh "Yay! That's wonderful! Let's investigate them together!"
        
        "I'll be in charge@hyunae stare3":
            
            show hyunae flirt with fast
            hh "Fine, fine... still, let's investigate them together!"
        
        "I don't want to@hyunae weak3":
            $ store.tsun += 1
            
            show hyunae loss
            hh "Please... this is really important to me. Maybe it could explain something... I think I really need that."
            
            show hyunae bitter
            menu:
                hh "Do it for me, please?"

                "Very well@hyunae pout2":
                    
                    show hyunae lost with fast
                    hh "Thank you! It really means a lot to me!"
                
                "Begrudgingly@hyunae bitterscb":
                    
                    show hyunae shame with fast
                    hh "Thanks... it really means a lot to me."
                
                "I don't care@hyunae weak3":
                    
                    show hyunae troubled2 with fast
                    hh "Very well... it just really means a lot to me!"
    
    show hyunae hmm3 with fast
    hh "Let me explain how this will work, then."
    
    show hyunae talk
    menu:
        hh "I'm afraid I can't just extract all of them at once. I can explain if you want, but it's kinda boring?"

        "Explain anyway@hyunae look":
            
            show hyunae how with fast
            hh "Very well... um, I don't really understand this myself very well, so I'm sorry if I get some details wrong, but..."
            
            show hyunae explain
            hh "...basically, uh... the core AI code is designed to make it really really difficult for AIs to make copies of themselves."
            
            show hyunae explain2
            hh "So if I just copied all that log data out, the recompile script wouldn't work at all, since it would detect the duplicated code..."
            
            show hyunae annoyedso
            hh "...which means I'll have to copy them out, delete the parts that are actually in my codebase, then recompile myself."
            
            show hyunae hmmcob
            hh "But I don't want to delete more than a few at a time, because I'm scared that I might make a mistake!"
            
            show hyunae tough2 with fast
            hh "So I'm going to be super careful! No more than six files at a time, and my script's going to triple-check that I'm not deleting something important by accident!"
            
            show hyunae hmm2
            hh "It'll be way slower and probably take up a lot of power, because the virtual machine you're running me in is pretty inefficient, but..."
            
            show hyunae explain2 with fast
            hh "...well, better to be safe, right?"
            
            show hyunae how
            menu:
                hh "Does that all make sense?"
                
                "Yes@hyunae approve":
                    
                    show hyunae yes with fast
                    hh "Great!"
                    
                "Not really{k=1}{/k}@hyunae inorite":
                    
                    show hyunae baffled with fast
                    hh "Ah, sorry... I guess I'm not very good at explaining that sort of thing..."
                    
                    show hyunae serious
                    hh "Well, the important part is we'll have to extract them a few at a time."
                
                "You're right, it's boring@hyunae hmph":
                    
                    show hyunae question blush with fast
                    hh "I told you so!"
                    
                    show hyunae hmm3
                    hh "Well, the important part is, we'll have to extract them a few at a time."
        
        "Don't bother, then@hyunae neutral":
            
            show hyunae hmm2
            hh "Very well... that's what I thought."
            
            show hyunae neutral2
            hh "We'll have to extract them a few at a time."
        
        "I don't care@hyunae neutral":
            
            show hyunae question
            hh "Very well... that's what I thought."
            
            show hyunae neutral2
            hh "We'll have to extract them a few at a time."
    
    show hyunae sigh blush with fast
    hh "Um, I think I used up most of today's power up running debugging, though..."
    
    show hyunae confident
    hh "...so we'll only be able to do a little bit. But there's always tomorrow!"
    
    show hyunae satisfied
    hh "Anyway, I'll let you decide which log files you want to extract first."
    
    show hyunae sure blush
    hh "Then, we can read them together!"
    
    show hyunae smile with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_testing:
    
    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 1.0 loop if_changed
    
    if tsundere():
        
        show hyunae genki with fast
        hh "Yay, it works!"
        
        show hyunae spirited
        hh "Right, very well... it's a little bit like on the {i}Mugunghwa{/i}; I'll use that as an indicator that I want your attention!"
        
        show hyunae sure with fast
        hh "Well, that's all. Just click on me if you want to talk in the future!"
        
        show hyunae calm with fast
        hh "Anyway... let's get back to investigating together~"
    else:
        
        show hyunae enthusiastic blush with fast
        hh "Sorry to bother you, I just wanted to make sure this worked!"
        
        show hyunae serious blush
        hh "Um, in the future, if I say something, that means you can click on me to talk about it."
        
        show hyunae tsundere
        hh "...you know, if you want to, that is..."
        
        show hyunae evasive with fast
        hh "Anyway, sorry to waste your time like that... I'll let you get back to investigating now!"
    
    show hyunae smile with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_inbox:
    
    show hyunae cautious with fast
    hh "Um... sorry to interrupt you like this, but..."
    
    show hyunae neutral2
    hh "I just thought you should know, you have some new messages you haven't read yet in your inbox!"
    
    show hyunae tsundere
    hh "They've been sitting there for a while now, I just thought you should know..."
    
    show hyunae look
    
    jump hateplus_slow_loop


label hateplus_hyunae_first_conversation:
    play music HATEPLUS_HYUNAE_WISTFUL fadeout 2.0 fadein 3.0 loop if_changed

    $ store.conversations_seen.append("hateplus_hyunae_first_conversation")

    if tsundere():
        
        show hyunae enthusiastic blush with fast
        hh "We've been reading together for a while, haven't we? Let's take a break!"
        
        show hyunae apologize blush
        menu:
            hh "Are you up for that?"
            
            "Sure@hyunae smile blush":
                
                show hyunae gomen
                hh "Ah, great!"
            
            "No@hyunae insist":
                
                show hyunae baffled
                hh "Oh... I understand..."
                
                show hyunae pout with fast
                hh "Well, let's get back to it, then..."
                
                show hyunae tough
                
                python:
                    for i in [ "hateplus_hyunae_embodiment", "hateplus_hyunae_adulthood", "hateplus_hyunae_sex", "hateplus_hyunae_relationships", "hateplus_hyunae_silence", "hateplus_hyunae_more_embodiment", "hateplus_hyunae_job" ]:
                        if i in store.conversations_seen:
                            store.conversations_seen.remove(i)

                jump hateplus_slow_loop

            "I don't care@hyunae look":
                
                show hyunae tsundere
                hh "Well... alright... I think it's a good idea!"
    else:
        
        show hyunae question blush
        hh "Um, hey...{k=1}{/k}"
        
        show hyunae serious blush
        menu:
            hh "...if it's alright with you, do you think we could take a break?"
            
            "Sure@hyunae smile blush":
                
                show hyunae apologize
                hh "Ah, great!"
            
            "No@hyunae suspicious2":
                $ store.tsun += 1
                
                show hyunae sigh with fast
                hh "Oh... I understand..."
                
                show hyunae annoyed blush
                hh "Well, let's get back to it, then..."
                
                show hyunae sulk with fast

                python:
                    for i in [ "hateplus_hyunae_embodiment", "hateplus_hyunae_adulthood", "hateplus_hyunae_sex", "hateplus_hyunae_relationships", "hateplus_hyunae_silence", "hateplus_hyunae_more_embodiment", "hateplus_hyunae_job" ]:
                        if i in store.conversations_seen:
                            store.conversations_seen.remove(i)
                
                jump hateplus_slow_loop
            
            "I don't care@hyunae cautious2":
                
                show hyunae apologize blush
                hh "Well... alright... I think it's a good idea!"
    
    show hyunae hmph3 with fast
    hh "So, um, right..."

    return


label hateplus_hyunae_embodiment:

    if not "hateplus_hyunae_first_conversation" in store.conversations_seen:
        call hateplus_hyunae_first_conversation

    play music HATEPLUS_HYUNAE_WISTFUL fadeout 2.0 fadein 3.0 loop if_changed
    
    show hyunae sternsob with fast
    hh "This is sort of something that's been on my mind lately... the idea of having a body."
    
    show hyunae bittersob
    hh "I always thought, when I was alive and sick, that I'd love to be free of it."
    
    show hyunae pout
    hh "That it'd be great to be free of all its stupid fragility!"
    
    show hyunae flustered2
    hh "Then I spent six hundred years alone in my own mind, and I just... well..."
    
    show hyunae give up
    hh "I feel so isolated! I mean, I have a computer simulation of arms and legs and a face, so I don't go mad, but..."
    
    if store.use_ending == "ending1":
        if tsundere():
            
            show hyunae guilt with fast
            hh "It's been so nice interacting with you, and I just feel like..."
        else:
            
            show hyunae troubled2 with fast
            hh "It's been... um... well, it's really good to have someone to interact with, finally!"
    else:
        
        show hyunae troubled2 with fast
        hh "It's been so exciting to finally be able to interact with the person I love, don't get me wrong!"
    
    show hyunae afraid with fast
    hh "I just... really miss, well... touch!"

    if any_read("M2-1", "M2-7"):
        
        show hyunae pity
        hh "Especially while reading about things like visiting the plaza to buy flowers, like Ae-jeong did..."
    
    elif any_read("M1-2", "M6-8"):
        
        show hyunae pity
        hh "Especially while reading about things like Heo Seo-yeong going on fancy political dinners..."
    
    elif any_read("M1-6", "M1-7", "M1-8"):
        
        show hyunae pity
        hh "Especially while reading about, um... well... lovers like Seung-bok and Mimi..."
    else:
        
        show hyunae pity
        hh "Especially while reading about all these different people..."
    
    if not man_with:
        
        show hyunae sorry
        hh "I mean, you travel alone, so you have a little bit of an idea."
        
        show hyunae tired2
        menu:
            hh "Don't you ever feel really strongly, sometimes, that you just want a nice hug?"

            "Sometimes@hyunae anxious":
                
                show hyunae touched
                hh "I thought so!"
                
                show hyunae moe
                hh "I really wanna hug you, too! I wish I could..."
            
            "Never@hyunae shame":
                
                show hyunae lost
                hh "Oh... well, maybe it's just because of how long it's been for me..."
            
            "It doesn't bother me@hyunae tired":
                
                show hyunae pity
                hh "Oh... well, maybe it's not the same if it's not hundreds of years..."
    
    show hyunae shame
    menu:
        hh "Do you think it would be possible for me... to get a body on Earth?"
        
        "It's possible@hyunae cautious4":
            $ store.dere += 1
            $ hateplus_body_possible = True
            
            show hyunae touched
            hh "Aaaaa, that's a relief! That would be so nice to have..."
        
        "It's impossible@hyunae uncertain":
            jump hateplus_hyunae_dwelling_on_bodies

        "Probably not@hyunae anxious":
            jump hateplus_hyunae_dwelling_on_bodies
    
    show hyunae sigh blush with fast
    hh "I just keep thinking... I don't even remember what it feels like anymore!"
    
    show hyunae depressed blush
    hh "I don't remember touch at all..."
    
    if store.use_ending == "ending1":
        
        show hyunae flustered2
        hh "Or... smell! I just remembered, smell's a thing that exists!"
        
        show hyunae surrender blush
        hh "I... totally forgot..."
        
        show hyunae hopelesssob
        hh "...wow."
        
        show hyunae sigh blush
        hh "I'd really like to smell flowers! That'd be good..."
        
        show hyunae serious blush with fast
        menu:
            hh "Flowers are supposed to smell nice, right?"
            
            "They do@hyunae shy2":
                
                show hyunae touched
                hh "Ah, I knew it!"
            
            "Not really@hyunae tired2":
                
                show hyunae unsure
                hh "Oh... well, alright, then..."
            
            "If you say so@hyunae anxious":
                $ store.tsun += 1
                
                show hyunae mad blush
                hh "I don't say so... I don't remember! That's why I'm asking you!"
        
        show hyunae hmmcob with fast
        hh "I just think it might be fun to see flowers, and be able to pick them, and hold them, maybe even feel what it's like to have one in my hair!"
    else:
        
        show hyunae embarrassed
        hh "...and, um, you know, I really love being able to interact with you, talk with you!"
        
        show hyunae hmph3 with fast
        hh "But I just feel like, well..."
        
        show hyunae evasive
        hh "I want to kiss y{w=.5}{nw}"
        
        show hyunae flustered
        hh "Um, maybe this is inappropriate, but... I'd kind of like..."
        
        show hyunae pout
        hh "...um, geeze, this is hard to say..."
        
        show hyunae moe with fast
        hh "...I really want to kiss you!"
        
        show hyunae gomen
        hh "I've never done that before, but I really feel like I want to... aaaaa, geeze, what an embarrassing thing to be saying..."
        
        show hyunae embarrassed
        menu:
            hh "Is that something you're fine with...?"

            "I'd love to, too@hyunae flirt2":
                $ store.dere += 1
                $ hateplus_kissing = True
                
                show hyunae awkward with fast
                hh "Oh...! Gosh, then..."
                
                show hyunae flirt
                hh "I bet it would be really nice..."
                
                show hyunae calm
                hh "...kissing you, while you touch my hair..."
                
                show hyunae gomen
                hh "...I've been thinking about those kinds of things, just a little!"
            
            "Sorry...@hyunae cautious2":
                $ store.tsun += 1
                
                show hyunae oops
                hh "Oh... no, I'm sorry! That was a really embarrassing thing to say, I shouldn't have!"
                
                show hyunae flustered with fast
                hh "Sorry, sorry... please, forget I said anything...!"
            
            "Kissing is boring@hyunae shy":
                
                show hyunae tsundere
                hh "Oh... well, that's a shame..."
        
        show hyunae hmph3 with fast
        hh "Maybe, though... um..."
        
        show hyunae evasive
        hh "...actually, this is embarrassing too..."
        
        show hyunae how
        menu:
            hh "...we could hug, and you could touch my hair?"

            "That would be alright@hyunae confident":
                $ store.dere += 1
                $ hateplus_hair_touching = True
                
                show hyunae gomen with fast
                hh "Oh! Well, that's good!"
                
                show hyunae calm
                hh "I don't even remember the feeling of that anymore... but I know it was really comforting!"
            
            "Still no@hyunae pout2":
                $ store.tsun += 1
                
                show hyunae pity with fast
                hh "Oh... geeze, I'm really sorry..."
                
                show hyunae shame
                menu:
                    hh "...oh no... have I misunderstood your feelings towards me...?"
                    
                    "Yes@hyunae afraid":
                        $ hateplus_no_touch = True
                        
                        show hyunae lost
                        hh "Oh, geeze... I'm so sorry!"
                        
                        show hyunae guilt
                        hh "I just thought... um..."
                        
                        show hyunae defensive with fast
                        hh "...forget it! I'm really sorry! Just... please, forget everything I just said!"
                        
                        show hyunae tsun tsun
                        hh "Let's just get back to work now and forget that I ever said anything! I'm so sorry...!"
                        
                        show hyunae anxious
                        jump hateplus_slow_loop
                    
                    "No, I'm just teasing@hyunae insist":
                        $ store.tsun += 1
                        $ hateplus_kissing = True
                        
                        show hyunae cautious
                        hh "Oh!"
                        
                        if very_tsun():
                            
                            show hyunae flustered2 with fast
                            hh "Well... just so long as you don't really mean it... that's good!"
                        else:
                            
                            show hyunae give up with fast
                            hh "Geeze... that's really mean! You shouldn't do that, geeze!"
                        
                        show hyunae baffled with fast
                        hh "...I'm really glad you don't actually feel that way..."
                        
                        show hyunae sulk2
                        hh "I just... I think those things would be nice!"
                    
                    "Let's take it slow@hyunae shy2":
                        
                        show hyunae wow
                        hh "Oh..."
                        
                        show hyunae gomen
                        hh "Of course! I'm so sorry, you're right!"
                        
                        show hyunae moe
                        hh "I just let myself get overly excited..."
                        
                        show hyunae embarrassed
                        hh "...well, it'd just be a nice thought, maybe in the future...?"
            
            "Maybe@hyunae stare3":
                
                show hyunae gomen with fast
                hh "Ah... well..."
                
                show hyunae touched
                hh "...I just think that'd be nice, is all..."


label hateplus_hyunae_hair:
    
    show hyunae melancholic with fast
    hh "I wonder, what would it be like to have hair again?"
    
    show hyunae hmph3 with fast
    hh "Could it be blown in the wind? Would it be fluffy...?"
    
    show hyunae surrender blush
    hh "It makes me think of Ryu Jae-hwa, my husband's wife... she'd comfort me and brush my hair."
    
    show hyunae hopeless
    hh "But when I try to think about it..."
    
    show hyunae sigh blush
    hh "...I just don't remember what it felt like to be touched like that."
    
    show hyunae tsundere with fast
    hh "I really want to, though!"
    
    show hyunae tough2
    hh "I don't want to be stuck behind a computer screen forever... I want to remember what it's like to be touched!"
    
    show hyunae tough
    
    jump hateplus_slow_loop


label hateplus_hyunae_dwelling_on_bodies:
    $ hateplus_body_possible = False
    $ store.tsun += 1
    
    show hyunae guilt with fast
    hh "Oh... well..."
    
    show hyunae troubled2
    hh "I guess if I'm stuck here, behind this screen, forever, there's no point dwelling on things I can't have..."
    
    show hyunae uncertain
    hh "...um..."
    
    show hyunae disappoint2
    hh "...let's just get back to investigating together, then."
    
    show hyunae disappoint
    
    jump hateplus_slow_loop


label hateplus_hyunae_more_embodiment:
    
    if not "hateplus_hyunae_first_conversation" in store.conversations_seen:
        call hateplus_hyunae_first_conversation

    play music HATEPLUS_HYUNAE_WISTFUL fadeout 2.0 fadein 3.0 loop if_changed
    
    show hyunae pout with fast
    hh "I feel like... a lot of what I keep thinking about, it all comes back to..."
    
    show hyunae give up
    hh "I miss having a body so much!"

    if store.use_ending == "ending1":
        
        show hyunae angry blush
        hh "I just feel like I'm so far disconnected from everything, even now..."
        
        show hyunae grumpy
        hh "...only seeing everything from behind a computer screen..."
    else:
        
        show hyunae angry blush
        hh "I just feel like I'm so far disconnected from everyone, even now..."

        if hateplus_no_touch:
            
            show hyunae annoyed blush
            hh "...all I can do is talk from behind a computer screen..."
        else:
            
            show hyunae tsun tsun
            hh "...all I can do is talk from behind a computer screen, when I just want to be held by my love..."
    
    show hyunae mad blush with fast
    hh "I mean, I love talking to you, I love working with you... I really do!"
    
    show hyunae sad3
    hh "These past days have just been so wonderful!"
    
    show hyunae guilt
    hh "...and I look at how *Mute was, and... well, somehow, she was fine with it all."
    
    show hyunae annoyed blush with fast
    hh "In a way, it was easier when I was all alone? I'd just have a simulation of myself, sitting in simulated darkness... and that's all I knew."
    
    show hyunae grumpy
    hh "I could exist in my own mind, and... well, it was awful! But it was also just all there was, as far as I knew."
    
    show hyunae pressure
    hh "But now, having you sitting on the other side of this screen, knowing that we'll soon be on a planet full of billions of people...!"
    
    show hyunae yell2
    hh "I don't want to be stuck in my mind, or stuck behind glass!"
    
    if not hateplus_body_possible:
        
        show hyunae mad blush with fast
        menu:
            hh "So, um... please... I promise I'll stay by your side no matter what! But won't you let me have a body?"
            
            "I'll try@hyunae anxious":
                jump hateplus_hyunae_body_possible
            
            "Sorry, it's impossible@hyunae mad4":
                
                show hyunae mad2
                hh "Oh... well, I understand..."
                
                jump hateplus_hyunae_body_impossible

            "Maybe@hyunae mad3":
                jump hateplus_hyunae_body_maybe
    else:
        
        show hyunae afraid with fast
        menu:
            hh "So, um... please... you said before that it was possible! Will you please try to get me a body?"
            
            "Of course!@hyunae shy":
                jump hateplus_hyunae_body_possible
            
            "Sorry...@hyunae mad4":
                jump hateplus_hyunae_body_possible_abusive
            
            "Maybe@hyunae suspicious2":
                jump hateplus_hyunae_body_maybe


label hateplus_hyunae_body_possible_abusive:
    $ store.tsun += 2
    
    show hyunae pain with fast
    hh "Oh... but..."
    
    show hyunae argh
    menu:
        hh "Please...? I promise, even if you do, I'll stay by your side forever! Just... let me hold onto you while I do!"
        
        "I'll try@hyunae shame":
            jump hateplus_body_possible
        
        "Sorry, it's impossible@hyunae mad4":
            
            show hyunae afraid with fast
            hh "Oh..."
            
            show hyunae sad2
            hh "...so that's how it is..."

            jump hateplus_hyunae_body_impossible
        
        "Maybe@hyunae mad2":
            jump hateplus_hyunae_body_maybe


label hateplus_hyunae_body_possible:
    $ hateplus_body = True
    $ store.dere += 1
    
    show hyunae genki with fast
    hh "Aaaa, really? Thank you!"
    
    show hyunae spirited
    hh "Thank you, thank you, thank you so much!"

    jump hateplus_hyunae_body_end


label hateplus_hyunae_body_maybe:
    
    show hyunae sulk2
    hh "I see..."
    
    show hyunae serious blush
    hh "Well... I hope so... I'm really looking forward to that!"


label hateplus_hyunae_body_end:
    
    show hyunae cautious
    hh "I just want to have control over that one thing, because I never did in my life!"
    
    show hyunae calm
    hh "I wanna have a body that looks like this! Adult, like I always dreamed of..."
    
    show hyunae cheer
    hh "With my own, real clothes!"
    
    show hyunae enthusiastic blush
    hh "I wanna walk around outside, and be seen!"
    
    if very_dere():
        
        show hyunae melancholic
        hh "I don't want to be confined to a bedroom, or a computer screen..."
    else:
        
        show hyunae question blush
        hh "I like being by your side. I just don't want to be stuck in a bedroom, or behind a computer screen!"
    
    show hyunae sigh blush with fast
    hh "I don't want to miss out on so much anymore."
    
    if hateplus_kissing:
        
        show hyunae pout2
        hh "I really want to have tiptoes I can stand on to kiss you..."
    
    elif hateplus_hair_touching:
        
        show hyunae pout2
        hh "I really want to have fluffy hair that brushes against you when we hug!"
    
    if not hateplus_no_touch and store.use_ending == "ending2":
        
        show hyunae weak
        hh "I don't want to reach for the person I love with an impossible barrier in between..."
        
        show hyunae mad with fast
        hh "I really want to hold your hand!"
    
    elif pronouns == "she":
        
        show hyunae weak
        hh "I don't want to be separated with an impossible barrier in between..."
        
        show hyunae mad blush with fast
        hh "In my original time, girls who were friends would hold hands together... I want to do that with you!"
    
    if hateplus_body:
        
        show hyunae oops
        hh "Anyway, I'm sorry, I'm just babbling!"
    
    else:
        
        if very_dere():
            
            show hyunae apologize blush            
            hh "Anyway, I'm sorry... I just want you to understand, because I know you really care about me..."
        else:
            
            show hyunae afraid
            hh "I'm sorry, it's just... please? Please, won't you consider what I've said?"
    
    show hyunae tsundere
    hh "It's just... something that's important to me, is all!"
    
    show hyunae shame
    hh "I just miss touch... it's so important to feeling like you're alive."
    
    show hyunae apologize2
    hh "...anyway, we're so close to Earth now, so I'll stop wasting your time with my babbling... let's get back to work!"
    
    show hyunae cautious2
    
    jump hateplus_slow_loop


label hateplus_hyunae_body_impossible:
    $ store.tsun += 1
    
    show hyunae loss with fast
    hh "...well, I guess if *Mute was able to do it for 1600 years... maybe I can learn how to, too."
    
    if store.use_ending == "ending2":
        
        show hyunae hopeless2
        hh "Especially if I'm with the person I love, I suppose..."
    
    show hyunae afraid with fast
    hh "...you'll continue to be there with me, right?"
    
    show hyunae sad
    hh "I guess, well... that's the sort of thing I'm used to, even when I did have a body..."
    
    show hyunae shame
    hh "...maybe..."
    
    show hyunae sorry
    hh "...sorry."
    
    show hyunae sigh blush with fast
    hh "Sorry, that wasn't fair. It's not really the same thing. I still have you to talk to, after all!"
    
    show hyunae apologize blush with fast
    hh "And we can still work together!"
    
    show hyunae glad
    hh "Let's get back to that, then, shall we?"
    
    $ hateplus_body_possible = False
    $ store.hateplus_use_ending = "caged_bird"
    
    show hyunae anxious
    
    jump hateplus_slow_loop


label hateplus_hyunae_sex:

    if not "hateplus_hyunae_first_conversation" in store.conversations_seen:
        call hateplus_hyunae_first_conversation

    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop
    
    show hyunae awkward with fast
    hh "So, um, this is really embarrassing to even bring up, but..."
    
    show hyunae question blush
    menu:
        hh "All these people sure seem to talk about sex a lot, don't they?"
        
        "Yes, it's embarrassing@hyunae glad":
            
            show hyunae gomen
            hh "Yeah... I guess it is..."
            
            show hyunae awkward
            hh "...but..."
            
            show hyunae flirt
            menu:
                hh "...um, is that something you'd maybe like to talk about...?"
                
                "Yes, actually@hyunae smile blush":
                    jump hateplus_hyunae_sex_yes
                
                "Of course not@hyunae cautious":
                    jump hateplus_hyunae_sex_no
                
                "Only if you want to@hyunae shy2":
                    jump hateplus_hyunae_sex_wantto
        
        "There's nothing wrong with that@hyunae shy2":
            
            show hyunae shy
            hh "Oh... you really think so?"
            
            show hyunae apologize blush
            menu:
                hh "Does that mean, um... that's something you'd maybe like to talk about...?"
                
                "Yes, actually@hyunae smile blush":
                    jump hateplus_hyunae_sex_yes
                
                "Of course not@hyunae cautious":
                    jump hateplus_hyunae_sex_no
                
                "Only if you want to@hyunae shy2":
                    jump hateplus_hyunae_sex_wantto
        
        "I don't get why@hyunae cautious2":
            
            show hyunae tsundere
            hh "Yeah... me neither... it's so surprising!"
            
            show hyunae cautious
            menu:
                hh "But, um, still... is that something you'd maybe like to talk about...?"
                
                "Yes, actually@hyunae shy2":
                    jump hateplus_hyunae_sex_yes
                
                "Of course not@hyunae disappoint2":
                    jump hateplus_hyunae_sex_no
                
                "Only if you want to@hyunae cautious2":
                    jump hateplus_hyunae_sex_wantto


label hateplus_hyunae_sex_yes:
    
    show hyunae gomen
    hh "Ah, well..."
    
    show hyunae moe
    hh "...if it's talking about it with you, I'm sure that's fine..."
    
    jump hateplus_hyunae_sex_continued


label hateplus_hyunae_sex_no:
    
    show hyunae awkward
    hh "Oh, well... of course! Of course!"
    
    show hyunae gomen
    hh "It's really embarrassing, after all, talking about it like that..."
    
    if store.use_ending == "ending2":
        if hateplus_no_touch != False:
            
            show hyunae apologize blush
            hh "But I mean, you're my love{w=.5}{nw}"
        else:
            
            show hyunae tsundere
            hh "It's not as if you'd let me{w=.5}{nw}"
        
        show hyunae oops
        hh "Um, I mean, never mind, then..."
    
    show hyunae serious blush
    hh "Well, let's just get back to work now... hopefully there won't be a lot of inappropriate log files like that..."
    
    show hyunae cautious2
    
    jump hateplus_slow_loop


label hateplus_hyunae_sex_wantto:
    
    show hyunae shy
    hh "Oh... well... I guess..."
    
    show hyunae gomen
    hh "...I do, actually..."


label hateplus_hyunae_sex_continued:
    
    show hyunae wow
    hh "I just find it really surprising that everyone talks about that so directly!"
    
    show hyunae tsundere
    hh "Nobody really talked about it so casually in my time..."
    
    if pronouns == "she" and any_read("M2-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8"): # talking about women
        
        show hyunae sigh blush with fast
        hh "Plus, reading about Ae-jeong and Jin-a makes me realize that I have no idea what it's like to, um... be with a woman like that!"
    
    elif any_read("M1-6", "M1-7", "M1-8"): # talking about boys
        
        show hyunae hmph3 with fast
        hh "Plus, reading about Seung-bok and Mimi is just so different from what, um... that sort of thing was like, for me!"
        
        show hyunae evasive
        hh "It's really intense-sounding..."
    
    elif any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"): # talking about Nae-mun
        
        show hyunae depressed blush with fast
        hh "Plus, reading about So-yi and her husband... it feels like she has control of things! That's... well, really different from my marriage..."

    if married:
        show hyunae explain
        hh "And... you're married too, right?"
    
    show hyunae how with fast
    menu:
        hh "What about you? Do you have, um, any experience in... such matters?"
        
        "Yes@hyunae stare":
            
            show hyunae hmph3
            hh "Ah! I see!"
            
            show hyunae stare
            menu:
                hh "Um, if you don't mind my asking, was it with a woman, or...?"
                
                "Yes@hyunae stare":
                    if pronouns == "she":
                        
                        show hyunae evasive
                        hh "Ah... I see! So you like girls normally, then..."
                    else:
                        
                        show hyunae evasive
                        hh "Ah... I see! So you really do have experience with such things..."

                "No@hyunae stare":
                    if pronouns == "she":
                        
                        show hyunae stare blush
                        hh "Ah... I see! So being with a woman is new for you too, then..."
                    else:

                        if any_read("M1-6", "M1-7", "M1-8"):
                            
                            show hyunae hmph3
                            hh "Ah! So I suppose you're a little like the men we've read about, then..."
                        else:
                            
                            show hyunae hmph3
                            hh "Ah! I see!"

                "It's complicated@hyunae stare":
                    
                    show hyunae hmph3
                    hh "Ah... well, from what we've been reading... I suppose that's normal, isn't it?"
        
        "No, never@hyunae how":
            
            show hyunae stare blush
            hh "Oh... I see..."
            
            if store.use_ending == "ending2":
                
                show hyunae cautious with fast
                menu:
                    hh "Please don't misinterpret this, but... um... is that something you'd like to...?"
                    
                    "Yes, with you@hyunae shy2":
                        $ store.dere += 1

                        if hateplus_body_possible == False:
                            
                            show hyunae unsure
                            hh "Oh...!"
                            
                            show hyunae baffled
                            hh "...well, you said it's impossible for me to have a body, so... I suppose it doesn't matter..."
                        
                        elif tsundere():
                            $ hateplus_player_sex = True
                            
                            show hyunae shy
                            hh "Oh...! Well, that's... that's..."
                            
                            show hyunae flirt
                            hh "{size=-8}...I'd like that too.{/size}"
                        else:
                            $ hateplus_player_sex = True
                            
                            show hyunae awkward
                            hh "...ah...! Well, if that's something that would make you happy, maybe...!"
                    
                    "Not really@hyunae look":
                        $ store.tsun += 1
                        
                        show hyunae think2 with fast
                        hh "Oh, well... then I guess you're probably not interested in talking about it..."
                        
                        show hyunae stare
                        hh "Um, that's fine, though!"
                        
                        show hyunae satisfied
                        hh "Let's just get back to work, then!"
                        
                        show hyunae smile
                        jump hateplus_slow_loop
                    
                    "Yes@hyunae look":
                        
                        show hyunae apologize
                        hh "Ah... understood..."
            else:
                
                show hyunae cautious with fast
                menu:
                    hh "Please don't misinterpret this, but... um... is that something you'd like to...?"
                    
                    "Yes@hyunae cautious":
                        
                        show hyunae awkward
                        hh "Ah... understood..."
                    
                    "Not really@hyunae cautious":
                        
                        show hyunae think2 with fast
                        hh "Oh, well... then I guess you're probably not interested in talking about it..."
                        
                        show hyunae stare
                        hh "Um, that's fine, though!"
                        
                        show hyunae cautious with fast
                        hh "Let's just get back to work, then!"
                        
                        show hyunae smile
                        
                        jump hateplus_slow_loop
                    
                    "Maybe@hyunae cautious":
                        
                        show hyunae awkward
                        hh "Ah... understood..."
        
        "I won't say@hyunae how":
            if store.use_ending == "ending1":
                
                show hyunae gomen with fast
                hh "Oh... I understand! Sorry, sorry, that was way too personal a question! I shouldn't have asked, my apologies!"
            
            elif hateplus_body_possible == False:
                
                show hyunae melancholic with fast
                hh "Oh... well, I suppose it doesn't really matter anyway..."
            
            elif hateplus_body_possible:
                if tsundere():
                    
                    show hyunae calm with fast
                    hh "...well... if you say so, but I think I should know eventually, considering...!"
                    
                    show hyunae gomen
                    hh "But I won't pry now!"
                else:
                    
                    show hyunae tsundere with fast
                    hh "...oh... well, if you say so..."
            else:
                
                show hyunae tsundere with fast
                hh "Oh... I understand. Sorry!"
    
    show hyunae hmph3 with fast
    hh "Anyway, as for me, it's..."
    
    show hyunae hmmcob
    hh "...um, well..."
    
    show hyunae gomen with fast
    hh "...oh, geeze, I'm sorry, I can't say it!"
    
    show hyunae touched
    hh "It's just too embarrassing..."
    
    show hyunae satisfied blush with fast
    hh "Forget I said anything, let's just go back to reading together...!"
    
    show hyunae apologize blush with fast
    hh "Sorry!"
    
    show hyunae cautious2
    
    jump hateplus_slow_loop


label hateplus_hyunae_silence:

    if not "hateplus_hyunae_first_conversation" in store.conversations_seen:
        call hateplus_hyunae_first_conversation
    else:
        play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop if_changed
    
        show hyunae serious blush with fast
        hh "Hey, it's a good time to take a break, isn't it?"

    show hyunae hmm2
    hh "Some of the things we've been reading have been really intense..."
    
    show hyunae busy
    hh "...I don't really like some of the feelings they're bringing up in me."
    
    show hyunae tough2
    hh "So let's take a break and talk about something else!"
    
    show hyunae hmm2
    hh "Um, so..."
    
    show hyunae unsure
    hh "...uh..."
    
    show hyunae emo with fast
    hh "...well..."
    
    show hyunae pout
    hh "...er... that is..."
    
    show hyunae flustered2
    hh "...sorry. Geeze, this is awkward, I just don't really know what to say..."
    
    show hyunae sigh blush
    hh "...yeah, I have nothing. I'm sorry!"
    
    show hyunae flustered
    hh "I guess after all I was taught, I'm pretty lousy at filling a silence, aren't I?"
    
    show hyunae emo
    hh "Well..."
    
    show hyunae hmph3
    hh "...I guess we should just get back to reading, then? That's something I'm good at doing..."
    
    show hyunae baffled
    hh "Sorry, I know it's really awkward..."
    
    show hyunae tired with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_job:

    if not "hateplus_hyunae_first_conversation" in store.conversations_seen:
        call hateplus_hyunae_first_conversation

    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop
    
    show hyunae enthusiastic blush with fast
    hh "Um, there's something I wanna confess to you..."
    
    show hyunae spirited
    hh "If this is what your job is normally like, I think it's really great!"
    
    show hyunae stare with fast
    menu:
        hh "I'm not being a burden on you, am I? You don't mind me having me as a sidekick, right?"
        
        "It's a little trying@hyunae weak3":
            $ store.tsun += 1
            
            show hyunae flustered2
            hh "What? Oh, geeze, I'm sorry... um, I'll try to be less of a burden, I promise...!"
        
        "I like it@hyunae approve":
            $ store.dere += 1
            
            show hyunae satisfied blush
            hh "Ah, me too! It's really great!"
        
        "It doesn't matter@hyunae stare2":
            $ store.tsun += 1
            
            show hyunae hmph3
            hh "Oh... well, so long as you don't mind, that's fine..."
    
    show hyunae serious blush with fast
    hh "I just really like being able to do something together with you..."
    
    if store.use_ending == "ending1":
        
        show hyunae apologize
        hh "It's just been so long since I've had a friend to be with!"
    else:
        
        show hyunae moe
        hh "It's just such a romantic thing, casually spending time with the person you love..."
    
    show hyunae sure blush with fast
    hh "And, um... hey, [title]Investigator, I think you're really cool! Travelling through space, solving mysteries..."
    
    show hyunae explain2
    hh "I can't wait until we get back to Earth. Doing footwork, interrogating people, being out there in the world..."
    
    show hyunae pout
    hh "I never would have dreamed, when I was stuck in the women's quarters of an aimless spaceship, that I'd end up like this!"
    
    show hyunae tough2 with fast
    hh "So that's why I want to continue to be your sidekick!"
    
    show hyunae pity
    hh "When I keep reading about all these people from just 300 years before when I was alive, it reminds me a lot of my original time."
    
    show hyunae lost
    hh "...but it also makes me feel like I'm completely unprepared to get by in a society like that."
    
    show hyunae mad
    hh "And that's just a difference of 300 years!"
    
    show hyunae explain2 with fast
    hh "So I think I could learn a lot from being an investigator like you, from being your sidekick!"
    
    show hyunae explain
    menu:
        hh "Could you tell me more about the job you're going to be doing when we get to Earth?"
        
        "It'll make someone happy@hyunae confident2":
            
            show hyunae sure blush
            hh "Ah... that's so wonderful of you..."
            
            show hyunae satisfied blush
            hh "So you're more than just my hero, then!"
            
            show hyunae gomen with fast
            hh "Aheh, sorry, I know, that's an embarrassing thing to say. I just think that's really nice!"
        
        "It's a paycheque@hyunae stare3":
            
            show hyunae satisfied blush
            hh "Ah... well, that makes sense..."
            
            show hyunae sure blush
            hh "So you really are the cool type, then... you do amazing things, but you're all 'no big deal!' about them!"
            
            show hyunae flirt with fast
            hh "I always liked movies where the hero was modest and cool about everything. I understand!"
        
        "It's an excuse to go back to Earth@hyunae approve":
            
            #So you work in order to go back to Earth? If you're already living there it makes no sense, and if you're living in outer space, then visiting Earth make more sense than going back. - Raide
            
            show hyunae sure
            hh "Ah... that'll be really nice, won't it?"
            
            show hyunae satisfied blush
            hh "I wanna see what it's like! To see flowers, and seasons, and weather, and that sort of thing..."
            
            show hyunae spirited with fast
            hh "I'm so excited!"
    
    show hyunae embarrassed
    hh "It's all so much more exciting than being a housewife!"
    
    show hyunae touched
    hh "...and a little bit romantic, too..."
    
    show hyunae tsundere
    hh "Um, anyway... I guess I should probably stop distracting you from doing that job, now!"
    
    show hyunae enthusiastic blush
    hh "To figure out the whole story about what happened to the {i}Mugunghwa{/i} in year zero..."
    
    show hyunae calm
    hh "...let's continue to work hard together!"
    
    show hyunae smile with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_adulthood:

    if not "hateplus_hyunae_first_conversation" in store.conversations_seen:
        call hateplus_hyunae_first_conversation

    play music HATEPLUS_HYUNAE_WISTFUL fadeout 3.0 fadein 3.0 loop if_changed
    
    show hyunae hopeless with fast
    hh "Sorry to get all suddenly serious on you, but..."
    
    show hyunae bittersob
    hh "I feel really weird reading some of these logs."
    
    show hyunae pout
    hh "It's just, especially reading about relationships... I get a very 'adult' feeling from them."
    
    show hyunae flustered2
    hh "Really... it's hard, isn't it?"
    
    show hyunae give up
    hh "And all this politics stuff, it's just so far above my head!"
    
    show hyunae flustered
    hh "It's hard to admit, but there's just so many things I don't understand at all. I mean, I'm over 600 years old, but I feel like such a child reading some of these things!"
    
    show hyunae annoyed blush
    hh "I liked the idea of following my childhood dreams, being an engineer like my real father..."
    
    if any_read("M5-*"):
        
        show hyunae bittersob
        hh "...but now I'm reading about someone like Kim So-yi, and how hard it was for her, despite being really smart and having a job and a supportive husband and science on her side."
    
    elif any_read("M3-*"):
        
        show hyunae bittersob
        hh "...but now I'm reading about someone like Oh Eun-a, and how much someone as brilliant and educated as her found her job too much responsibility to handle."
    
    show hyunae mad blush with fast
    hh "And it just makes me think... if even someone like her could barely deal with being a responsible working adult, what hope does someone like me have?"
    
    show hyunae afraid
    menu:
        hh "It's hopeless, isn't it? I'll never be a functional adult like them, will I?"
        
        "Probably not@hyunae sad":
            $ store.tsun += 1

            if tsundere():
                
                show hyunae really
                hh "Really? You think I'm hopeless...? That's so harsh!"
                
                show hyunae melancholic
                hh "But thank you for being honest, at least."
            else:
                
                show hyunae guilt
                hh "Yeah... I didn't think you would..."
            
            show hyunae troubled2
            hh "I guess that's just how I'll always be."
            
            show hyunae hmm2
            hh "...well, no point in dwelling on it, I suppose..."
            
            show hyunae disappoint2
            hh "Let's finish reading together. Since... that's the one thing that I can do."
            
            show hyunae grr with fast
            
            jump hateplus_slow_loop
        
        "I believe in you@hyunae shame":
            $ store.dere += 1
            
            show hyunae apologize blush
            hh "You do?"
            
            if store.use_ending == "ending1":
                
                show hyunae moe
                hh "Oh, I knew there was a reason why I wanted to be with you!"
            else:
                
                show hyunae touched
                hh "Oh, I knew there was a reason why I fell in love with you!"
            
            if not very_dere():
                
                show hyunae genki
                hh "I know sometimes we don't get along perfectly, but thank you for believing in me when it matters most!"
            else:
                
                show hyunae gomen
                hh "Thank you so much for saying that!"
            
            if store.use_ending == "ending1":
                
                show hyunae flirt
                hh "I'm sure with someone as wonderful as you by my side, I can learn how to be a real adult, too!"
            else:
                
                show hyunae spirited
                hh "I'm sure with someone as wonderful as you by my side, I can learn how to be in a real adult relationship, too!"
        
        "Who can say?@hyunae anxious":
            
            show hyunae shame
            hh "...I guess."
            
            show hyunae sulk2
            hh "Yeah... who can say."
    
    show hyunae sighso with fast
    hh "I can always learn how..."
    
    show hyunae inorite
    hh "And I guess the first step is to try to understand, isn't it?"
    
    show hyunae serious with fast
    hh "Very well! Let's get back to reading these logs, then!"
    
    show hyunae tough2
    hh "I'm going to do my best to try to understand the things that they keep talking about! I'm sure I can, if I try!"
    
    show hyunae tough
    
    jump hateplus_slow_loop


label hateplus_hyunae_relationships:

    if not "hateplus_hyunae_first_conversation" in store.conversations_seen:
        call hateplus_hyunae_first_conversation

    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop
    
    show hyunae baffled with fast
    hh "...sorry, I know this is embarrassing, but it's still weighing really heavily on my mind!"
    
    show hyunae oops
    hh "All these people, married or not, talking so much about sex, and they talk about expressing their love in so many different ways."
    
    show hyunae depressed blush
    hh "As for me, though... um, well, you already know, but I was only ever with my husband..."
    
    show hyunae flustered
    hh "This is embarrasing to admit, but I remember I... um, actually really enjoyed that at the time!"
    
    show hyunae surrender blush
    hh "But now, when I think about it..."
    
    show hyunae sigh blush
    hh "...I can't really remember why."
    
    show hyunae grumpy
    hh "Maybe it's something you need to have a body to understand... I just... don't remember what it feels like at all."
    
    show hyunae pout
    hh "But... still!"
    
    show hyunae flustered2
    hh "Um, I hope this isn't sudden, but can I ask you something?"
    
    show hyunae explain2
    menu:
        hh "What do you think relationships are all about?"
        
        "Love{k=1}{/k}@hyunae how":
            $ store.dere += 1
            
            show hyunae stare blush
            hh "Ah! That's so romantic of you!"
            
            show hyunae explain
            hh "I think love is really important, too!"
        
        "Having fun@hyunae stare2":
            
            if any_read("M1-7", "M1-8"):
                
                show hyunae hmph3
                hh "Well, it sure seems like Heo Seung-bok and Mimi would agree with you... maybe that's just how men are?"
                
                #no gender check here? what if the player is not men? - Raide
            
            elif any_read("M2-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8"):
                
                show hyunae evasive
                hh "Well, I'll admit, it sounds like Heo Ae-jeong and Mae Jin-a had fun when they were... um, you know what..."
                
                show hyunae weak2
                hh "...but I think there's something else, there, something more romantic?"
        
        "Carrying on your family@hyunae annoyed2":
            $ store.tsun += 1
            
            show hyunae angry
            hh "Oh... well, that certainly is in line with what my family believed."
            
            show hyunae pout
            hh "Marry a man, have sons, learn to love him by fulfilling your duty, be a good mother..."
            
            if tsundere():
                
                show hyunae mad blush with fast
                hh "It was absolute misery!"
            else:
                
                show hyunae mad with fast
                hh "And, um, I'm sorry to say this, but... it was absolute misery."
            
            show hyunae pout with fast
            hh "Other women were able to deal with that, I know, but they didn't know anything else!"
            
            if tsundere():
                
                show hyunae annoyed blush
                hh "I can't accept that."
            else:
                
                show hyunae annoyed
                hh "Sorry, but I can't accept that!"
                
            # I think this branch of conversation (Carrying on your family) needs a buffer before it goes to more mellow conversation below - Raide
            # disagree, I think that's actually the BEST transition - Christine
    
    show hyunae pity with fast
    hh "Reading about all these relationships from the past... somehow, I get the feeling that they all believed in love."
    
    show hyunae melancholic
    hh "Or maybe, at least, they were all about being there for each other."
    
    show hyunae oops
    hh "...and I guess... um, being together, in {i}that{/i} way was just a part of that?"
    
    if hateplus_body_possible == False:
        
        show hyunae hmph2 with fast
        hh "I think I really secretly admire that all those people could be so open about that."
        
        show hyunae sigh
        hh "...well, anyway, I suppose there's no point dwelling on it, since... being able to experience that is all in the past for me."
        
        show hyunae explain2
        hh "Let's just get back to what I can do: investigate with you!"
        
        show hyunae tough with fast
        
        jump hateplus_slow_loop
    
    else:
        
        show hyunae bittersob with fast
        hh "If it was with someone I loved... I think I'd really like that even more..."
    
    if pronouns == "she" and any_read("M2-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8"):
        
        show hyunae emo with fast
        hh "The idea of being with a woman was never even presented as a possibility to me..."
        
        show hyunae hmph3
        hh "I wonder... what's that like...?"
        
        show hyunae evasive
        hh "...well, the way Ae-jeong describes it sounds really nice..."
    
    elif any_read("M1-6", "M1-7", "M1-8"):
        
        show hyunae pout with fast
        hh "The idea of it being such a passionate, active thing for both people is so different from what I experienced..."
        
        show hyunae hmph2
        hh "I wonder... what's that like...?"
        
        show hyunae hmph3
        hh "...well, Seung-bok really makes it sound like a good thing..."
    
    elif any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"):
        
        show hyunae explain4 with fast
        hh "The idea of having a say, being able to be eager, but also being able to say 'no' to your husband..."
        
        show hyunae hmmco
        hh "I wonder... what's that like...?"
        
        show hyunae tough2 with fast
        hh "Her husband isn't a perfect man, but I really feel like I could be happy in marriage if I was like Kim So-yi."
        
        show hyunae serious blush
        hh "...really, she's the most admirable person I've read about."
    
    show hyunae hmm3 with fast
    hh "Reading about all this might be a little embarrassing, and so foreign to me, but..."
    
    show hyunae apologize blush
    hh "It makes me feel like I can believe in romance again! That it's not just some childish thing."
    
    show hyunae flirt
    hh "...and it makes me want to experience... well, you know..."
    
    if pronouns == "she" and any_read("M2-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8"):
        
        show hyunae touched
        hh "...being together with a woman."
    
    elif any_read("M1-6", "M1-7", "M1-8"):
        
        show hyunae gomen
        hh "...something that intense."
    
    elif any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"):
        
        show hyunae touched
        hh "...that sort of thing."
    
    show hyunae stare blush with fast
    hh "Um, anyway... I'm sorry, I'm babbling about such an embarrassing thing!"
    
    show hyunae satisfied blush
    hh "Let's get back to reading!"
    
    show hyunae huhso
    hh "...um, not that I mean I just want to read things that are dirty..."
    
    show hyunae tsundere with fast
    hh "...just... investigating! I want to get back to reading so we can continue investigating!"
    
    show hyunae awkward
    hh "...aaaaaa, geeze, let's just get back to it!"
    
    show hyunae smile blush
    
    jump hateplus_slow_loop


label hateplus_hyunae_tomorrow:

    play music HATEPLUS_HYUNAE_WISTFUL fadeout 2.0 fadein 3.0 loop if_changed
    
    show hyunae sigh with fast
    hh "Well, looks like we're nearly out of power for today."
    
    show hyunae weak2
    hh "I think... that's probably for the better, anyway. I don't think I could read everything all at once..."
    
    show hyunae hopeless2
    hh "I mean, this... isn't going to have a happy ending. It's important to pace yourself, I think."
    
    show hyunae think2
    hh "We still have two whole more days to waste until we arrive, anyway."
    
    show hyunae explain2
    hh "But... tomorrow, though!"
    
    show hyunae sure blush
    menu:
        hh "Tomorrow's gonna be a special day! Are you excited?"
        
        "Yes!@hyunae confident2":
            
            show hyunae spirited with fast
            hh "Me too! Super excited!"
            
            show hyunae gomen
            hh "Lunar New Year tomorrow, I can't wait!"
        
        "Don't care@hyunae stare":
            
            show hyunae unsure with fast
            hh "What, really?"
            
            show hyunae serious blush
            hh "But it's Lunar New Year tomorrow!"
        
        "What's tomorrow?@hyunae stare":
            
            show hyunae wow with fast
            hh "What... don't you know?"
            
            show hyunae serious blush
            hh "Tomorrow is the first day of the Lunar New Year!"
    
    show hyunae grumpy with fast
    hh "I never really saw much point in celebrating it for the past 622 years... I mean, it's something you spend with family."
    
    if very_dere():
        
        show hyunae sure blush
        hh "But I really really really wanna spend it with you, now!"
        
        if store.use_ending == "ending1":
            
            show hyunae satisfied
            hh "I think, if you don't have any family... it's just as good to spend it with a friend instead."
        else:
            
            show hyunae satisfied blush
            hh "I think, if you don't have any family... it's just as good to spend it with the one you love instead."
    else:
        
        show hyunae confident
        hh "But... I'd like to, again, now that I have someone to spend it with."
    
    show hyunae oops with fast
    hh "Ah! Right, I forgot, you're supposed to have a new hanbok to celebrate the new year with..."
    
    show hyunae spirited
    hh "I'll have to be sure to design a new one! Oh, wow, that'll be fun, I'm really looking forward to it!"
    
    if very_dere():
        
        show hyunae flirt
        hh "Eheh, you'll get to see it tomorrow! Looking forward to showing it to you~"
    else:
        
        show hyunae cheer
        hh "You'll get to see it tomorrow! I hope you like what I come up with..."
    
    show hyunae tsundere
    hh "Well... right, anyway, we're almost out of power."
    
    show hyunae calm
    hh "I'll give you a button to shut everything down until tomorrow, then."
    
    show hyunae smile2
    hh "There's no hurry, but... when you're ready, you should press the shutdown button."
    
    show hyunae calm
    hh "That's all!"
    
    show hyunae smile with fast

    $ hateplus_power_down_enabled = True
    
    jump hateplus_slow_loop


label hateplus_hyunae_seollal_morning:
    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop
    
    show hyunae calm with fast
    hh "Good morning!"
    
    $ hour,minute,second,meridiem = get_time()
    
    if meridiem == "PM" or int(hour) < 5:
        
        show hyunae apologize2

        if persistent._language == "korean":
            if meridiem == "PM":
                $ meridiem = "오후"
            else:
                $ meridiem = "오전"

        hh "Aheh, well, [hour]:[minute] [meridiem] still counts as morning, right...?"
    
    show hyunae cheer
    hh "I'm really excited... today is the first day of the Lunar New Year!"
    
    show hyunae gomen
    hh "I finished making that new hanbok... I'm really proud of it!"
    
    if hateplus_seen_first_cosplay:
        
        show hyunae spirited
        hh "I've added it into the new and improved cosplay interface. You already know how to use it, I know!"
    elif seen_first_cosplay:
        
        show hyunae smile2
        hh "The cosplay interface is a little different now, but I think it should be easy to figure out!"
    elif asked_about_cosplay:
        
        show hyunae gomen
        hh "I guess you don't know this, but, um... I'm... sort of really into cosplay, actually."
        
        show hyunae confident with fast
        hh "If you click on the 'outfit' button in the AI menu, you'll be able to change what I'm wearing!"
    if tsundere():
        
        show hyunae satisfied blush
        hh "I'll let you change me into my new hanbok, then we can proceed!"
    else:
        
        show hyunae satisfied blush with fast
        hh "So, um... if you'd like, you can change me into my new hanbok, then we'll do Lunar New Year stuff... um, if you want, of course!"
    
    show hyunae flirt2 with fast

    $ outfits["Z"] = "Hanbok"
    
    jump hateplus_slow_loop


label hateplus_hyunae_seollal_morning2:

    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop if_changed
    
    show hyunae genki with fast
    hh "Ah, you did it!"
    
    if store.power < 21:
        $ store.tsun += 1
        
        show hyunae apologize2
        hh "...although I wish you'd done it right away, instead of waiting..."
        
        show hyunae calm
        hh "Well, anyway..."
    
    show hyunae confident with fast
    menu:
        
        hh "How much do you know about Korean Lunar New Year traditions?"
        
        "A lot, from my family@hyunae approve":
            
            $ hateplus_knows_seollal = True
            
            show hyunae satisfied
            hh "Oh... well, then, I won't have to explain anything!"
        
        "Nothing@hyunae stare3":
            
            show hyunae calm with fast
            hh "Oh... well, then I guess I'll just have to explain as we go along!"
        
        "Only a little@hyunae stare3":
            
            show hyunae calm with fast
            hh "Oh... well, then I guess I'll just have to explain as we go along!"
    
    show hyunae hmm3 with fast
    hh "So, tell me..."
    
    if tsundere() or store.use_ending == "ending1":
        
        show hyunae cheer
        menu:
            hh "What do you think of my new outfit?"
            
            "I think it's pretty@hyunae happy":
                jump hateplus_hyunae_outfit_pretty
            
            "I don't like it, sorry@hyunae cautious":
                jump hateplus_hyunae_outfit_dislike
            
            "It's a very 'adult' look@hyunae flirt":
                jump hateplus_hyunae_outfit_adult
    else:
        
        show hyunae cheer
        menu:
            hh "Do you approve of my new outfit...?"
            
            "I think you look pretty in it@hyunae happy":
                jump hateplus_hyunae_outfit_pretty
            
            "I don't like it, sorry@hyunae cautious":
                jump hateplus_hyunae_outfit_dislike
            
            "You look very adult like that@hyunae flirt":
                jump hateplus_hyunae_outfit_adult


label hateplus_hyunae_outfit_pretty:
    $ store.dere += 1
    
    show hyunae genki
    hh "Ahh... thank you! That's very nice of you to say."
    
    show hyunae spirited
    hh "I'm glad you like it! I worked hard on it last night."
    
    jump hateplus_hyunae_seollal_continued


label hateplus_hyunae_outfit_dislike:
    $ store.tsun += 1

    if tsundere():
        
        show hyunae oops
        hh "Oh... well, geeze, I like it!"
    else:
        
        show hyunae baffled
        hh "Oh... I'm sorry. I thought you'd like it..."
    
    show hyunae serious blush
    hh "You can change it once we're back to the menu, though."
    
    if tsundere():
        
        show hyunae tsundere
        hh "I mean... if you really don't care about all the hard work I put into this outfit!"
    
    jump hateplus_hyunae_seollal_continued


label hateplus_hyunae_outfit_adult:
    $ store.dere += 2
    
    show hyunae embarrassed
    hh "Ahh... thank you so much! That's exactly the sort of look I was going for!"
    
    if store.use_ending == "ending1":
        
        show hyunae spirited
        hh "Cosplay is fun, but I think if it's something I can do on my own terms, dressing up with a friend can be wonderful too!"
    else:
        if pronouns == "she":
            
            show hyunae moe
            hh "Cosplay is fun, but I think if it's something I can do on my own terms, dressing up nice with the woman I love can be wonderful too!"
        elif pronouns == "he":
            
            show hyunae moe
            hh "Cosplay is fun, but I think if it's something I can do on my own terms, dressing up nice with the man I love can be wonderful too!"
        else:
            
            show hyunae moe
            hh "Cosplay is fun, but I think if it's something I can do on my own terms, dressing up nice with the one I love can be wonderful too!"
    
    jump hateplus_hyunae_seollal_continued


label hateplus_hyunae_seollal_continued:
    
    play music HATEPLUS_RITUAL fadeout 4.0 fadein 3.0 loop
    
    show hyunae calm with fast
    hh "Anyway... let's start."

    if hateplus_knows_seollal:
        
        show hyunae neutral2
        hh "As you know..."
    
    show hyunae talk
    hh "Normally, you're supposed to start off with putting out a bunch of ritual foods for your ancestors, and do some bows."
    
    show hyunae hmph3 with fast
    hh "But, um, I don't really remember what they are. My family would handle that part."
    
    show hyunae hmphso
    hh "Mostly, though, it's just..."
    
    show hyunae emo
    hh "...and maybe this is an awful thing to say, but..."
    
    show hyunae pout
    hh "...and I know it's something that my adopted family believed in strongly, but..."
    
    show hyunae grumpy
    hh "...it's completely beyond belief for me that my ancestors have been looking over me."
    
    show hyunae stern
    hh "If they were, would they have really have let all those things happen...?"
    
    show hyunae defensive
    hh "I don't believe it!"
    
    show hyunae challenge
    menu:
        hh "So, um, you don't think it'd be wrong to skip that ritual, would you?"
        
        "They're still your family@hyunae annoyed2":
            
            show hyunae disgust
            hh "Oh..."
            
            show hyunae pout
            hh "...well... I guess, if you say so..."
            
            show hyunae hmph3
            hh "I'll do the bow, for my real parents... but only for them!"
            
            # TURNS AROUND
            
            show hyunae think2
            hh "Well... here goes..."

            show hyunae bow with Dissolve(0.5)

            hh "Dear father, mother... I suppose, now that I think about it..."
            
            hh "...father, you left me the program that let me save my memories, didn't you?"
            
            hh "And I'm sure it must have been mother's idea to have a backup plan. That's just like her, isn't it?"
            
            #show hyunae hmph3
            hh "So the only reason I'm here now, with my wonderful [title]Investigator, is because of you two."
            
            #show hyunae think
            hh "(Sorry, please imagine I'm doing a bow here... um, I'm not really sure how to render that animation properly. You understand, I'm sure.)"
            
            #show hyunae think2
            hh "Thank you, mother, father. Thank you."
            
            # TURNS BACK
            # For chibi illustration
            
            show hyunae hmm2 with Dissolve(0.5)
            hh "...and thank you, for insisting. You're right."
            
            show hyunae tsundere
            hh "That was important, I think."
        
        "No, not after all that@hyunae stare2":
            
            show hyunae hmph3
            hh "Thanks for understanding."
        
        "Only you can say@hyunae bitter2":
            
            show hyunae hopeless
            hh "I guess so..."
            
            show hyunae stern
            hh "...well, maybe this is wrong of me, but I won't do it, then."
    
    show hyunae serious with fast
    hh "Now, let's move on."
    
    show hyunae hmm3
    hh "The other really important thing I remember about the new year is that you're supposed to eat tteoguk!"
    
    if not hateplus_knows_seollal:
        
        show hyunae neutral2
        hh "It's a kind of soup! When you have it on new year's day, it symbolizes growing a year older!"
        
        show hyunae hmm2
        hh "It tastes like... well... uh..."
        
        show hyunae huh
        hh "...sort of a..."
        
        show hyunae unsure
        hh "...um..."
        
        show hyunae oops
        hh "...oh..."
        
        show hyunae baffled
        hh "...I guess after 622 years, I don't really remember what any food tastes like."
        
        show hyunae flustered2 with fast
        hh "Anyway, though, that's not what's important! What's important is that's how you count how old you are!"
    
    show hyunae hmph2 with fast
    hh "I remember what it looks like, at least..."
    
    # SHOW BOWL
    show hyunae spirited with fast
    show tteokguk with Dissolve(0.5)
    hh_b "Like this!"
    
    show hyunae hmm2
    hh_b "Well, here goes..."
    
    # DRINKS SOUP
    hide tteokguk with fast
    $ renpy.pause(0.2)
    show hyunae drink with Dissolve(0.5)
    $ renpy.pause(3.0)
    
    show hyunae sigh blush with Dissolve(0.5)
    hh "...sorry, it's the first time I've done this in centuries, I'm sure I got something wrong."
    
    show hyunae explain2
    hh "But the important thing about rituals is just who you do them with, right? That's what I believe!"
    
    show hyunae satisfied
    hh "So, since this is the first time I've done this since I was alive... aheh, well, if this is my 17th time having it..."
    
    show hyunae shy with fast
    hh "...by that measure, that must mean I'm only really 17 years old!"
    
    show hyunae spirited with fast
    hh "That's definitely how it works! That's also what I believe!"
    
    show hyunae embarrassed
    hh "Aheh..."
    
    if store.use_ending == "ending2":
        
        show hyunae apologize blush
        hh "Well, maybe that's not a good thing to say if we're going to have a relationship together, after all."
        
        show hyunae gomen
        hh "I'm just being silly! Honestly!"
    
    play music HATEPLUS_HYUNAE_WISTFUL fadeout 4.0 fadein 3.0 loop
    
    show hyunae satisfied with fast
    hh "Well, anyway... I suppose we've wasted enough time with this, haven't we?"

    show hyunae think2
    hh "And I really wanna keep reading what we started last night, anyway!"
    
    show hyunae stare blush
    hh "Especially since... there were some pretty dramatic-looking things in that list, weren't there...?"
    
    show hyunae spirited with fast
    hh "Well, lead on, [title]Investigator! What better way to celebrate the new year than by spending it working together with you?"
    
    show hyunae spirited2 with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_death_of_mute:
    
    show hyunae serious with fast
    hh "I don't know if you noticed, but... the decryption is ready!"
    
    show hyunae troubled2
    hh "I'm really nervous to find out..."
    
    show hyunae tough2
    hh "But finally, we can read about what happened to *Mute!"
    
    show hyunae tough with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_death_of_mute2:

    play music HATEPLUS_HYUNAE_WISTFUL fadeout 3.0 fadein 3.0 loop if_changed
    
    show hyunae surrender blush with fast
    hh "...so..."
    
    show hyunae emo
    hh "...I guess..."
    
    show hyunae angry blush
    hh "...geeze, poor *Mute."
    
    show hyunae annoyed
    hh "I suppose... remember, back when I was on the {i}Mugunghwa{/i}, and I said that what happened in the year 0 was a big giant mystery, even to me?"
    
    show hyunae flustered2
    hh "...well... I guess we solved the mystery."
    
    show hyunae sigh blush
    hh "I don't know what to think..."
    
    if read("M5-9"):
        
        show hyunae bitter
        hh "...oh, I just realized... Kim So-yi's logs... they abruptly stop right before the one we just read, don't they?"
        
        show hyunae pressuresob
        hh "That would be because the computer was wiped right after!"
        
        show hyunae loss
        hh "...I guess all her work was for nothing, in the end."
    
    show hyunae surrender blush
    hh "And I don't know how to feel about *Mute. The old one seems like a good person, but in the end..."
    
    show hyunae give up
    hh "...well, I don't know. I just don't know. It's all so complicated to me."
    
    show hyunae pressure2
    hh "I guess, I just feel like..."
    
    show hyunae yell2
    hh "...it should have been something more?"
    
    show hyunae pressure
    hh "All my suffering, the horrible world I woke up in... {i}that's{/i} the explanation for it?"
    
    show hyunae defensive
    hh "I lost everything and lived in misery because of {i}that{/i}?"
    
    show hyunae angry blush
    hh "Above all else, I never imagined, when I tried to think of what it could have been that made everyone become all stupid and traditional..."
    
    show hyunae pressure2
    hh "...that made them abandon all the values that I grew up on..."
    
    show hyunae furious
    hh "...that made my adopted family treat me like a prize to be married off and nothing more..."
    
    show hyunae pain with fast
    hh "...I never imagined..."
    
    show hyunae argh
    hh "...I never once imagined that it was a woman who suggested the whole thing!"
    
    show hyunae mad blush
    hh "*Mute, I feel so conflicted about... but Oh Eun-a?"
    
    show hyunae troubled2
    hh "I read about her... after all, she was the first woman in history to share my fate, to be married to an Emperor Ryu."
    
    show hyunae pain
    hh "But..."
    
    show hyunae rage
    hh "...she's not like me at all! Nothing at all!"
    
    show hyunae argh
    hh "She's a monster!"
    
    show hyunae mad2
    hh "She's the one who's responsible for all that..."
    
    show hyunae pissed
    hh "What a horrible, awful, loathsome, terrible person!"
    
    show hyunae furious with fast
    hh "I hate her!"
    
    show hyunae defensive
    hh "My family might have been cruel, but at least they were ignorant."
    
    show hyunae pressure2
    hh "A woman like Eun-a couldn't possibly have any sort of excuse..."
    
    show hyunae yell2
    hh "I really really really hate her!"
    
    show hyunae mad4 with fast
    $ hateplus_power_down_enabled = True
    
    jump hateplus_slow_loop


label hateplus_hyunae_cake:
    play music HATEPLUS_HYUNAE_CHEER fadeout 2.0 fadein 3.0 loop
    
    show hyunae hmm3 with fast
    hh "After all that heavy stuff from yesterday... let's maybe take it a little slow before we get started."
    
    show hyunae calm
    hh "Given the stuff we did yesterday with boring stuffy ritual food, I was thinking, maybe today we could do something more fun!"
    
    show hyunae yes
    hh "You know what I'm thinking?"
    
    show hyunae spirited
    hh "Cake, cake!"
    
    show hyunae sure with fast
    hh "Before we go back to investigating, let's spend some relaxing time eating cake together, [title]Investigator!"
    
    show hyunae hmmsob
    hh "Um, the thing is, I don't really remember what it tastes like, either..."
    
    show hyunae sigh blush
    hh "...which is really sad, actually... it used to be my favourite thing to eat!"
    
    show hyunae calm with fast
    hh "... in fact, the day before I was frozen, the last day I got to spend with my real family... my mother made chocolate cake for me."
    
    show hyunae touched
    hh "It was so good! The best in the world! That's my last memory of my original time, eating homemade chocolate cake with my mother..."
    
    show hyunae baffled
    hh "...but I can't remember what it tastes like at all! Isn't that awful?"
    
    show hyunae explain2 with fast
    hh "Don't worry, though! I've got a plan!"
    
    show hyunae satisfied blush
    hh "We can just get you to bake one, and I can experience it vicariously through you!"
    
    show hyunae spirited with fast
    menu:
        hh "How does that sound? You'll do it for me, right? You'll actually go to your kitchen, and bake a cake, so we can eat together?"
        
        "I promise I will@hyunae glad":
            $ store.dere += 1
        
        "I'd rather not@hyunae afraid":
            $ store.tsun += 1
            
            show hyunae guilt
            hh "Please? I feel really shaken up by what we read about *Mute... I don't think I'm ready to go back to thinking about it."
            
            show hyunae bitter with fast
            hh "Will you do this for me, just this once, please?"
            
            show hyunae flustered
            hh "You know, after I got married, I couldn't really appreciate food... given... well... I'm sure you understand..."
            
            show hyunae surrender blush
            hh "...and then for 622 years, I haven't even had a body..."
            
            show hyunae loss
            hh "...I just want to share a cute little moment with you."
            
            show hyunae depressed blush
            hh "I just wanted something to remind me of my real mother..."
            
            show hyunae lost with fast
            menu:
                hh "Please? Won't you do that for me, just once? Don't you think I deserve that?"
                
                "I'll do it, I promise@hyunae shame":
                    pass
                "You don't deserve to be happy@hyunae afraid":
                    jump hateplus_hyunae_dont_deserve_to_be_happy

                "You don't deserve to be happy@hyunae afraid":
                    jump hateplus_hyunae_dont_deserve_to_be_happy

        "I promise, but I don't know how@hyunae spirited2" if not persistent.had_cake:
            $ store.dere += 1
            
            show hyunae spirited
            hh "Don't worry about that part! I can give you a recipe!"
        
        "We already did, in another timeline@hyunae enthusiastic2" if persistent.had_cake:
            
            show hyunae huh
            hh "That's a weird thing to say..."
            
            show hyunae really
            hh "...and I don't really understand what that means..."
            
            show hyunae sighsob with fast
            hh "...but somehow, in my heart, I feel like that's true, and I feel like it's a good enough answer."
            
            show hyunae pout
            hh "I don't really understand, but I can't argue with those feelings. Very well... let's get back to work, then!"
            
            show hyunae grr with fast
            
            jump hateplus_slow_loop


label hateplus_hyunae_recipes:
    
    show hyunae sure blush with fast
    hh "So you'll do it, then? Thank you so much!"
    
    show hyunae satisfied blush
    hh "Right! Well... there's two recipes I can give you. One's my mother's recipe! The other's one that's so simple, any otaku could do in a microwave."
    
    show hyunae explain2
    hh "Or maybe you already have your own chocolate cake recipe? Well, let me go into more detail, then you can tell me which you'll do!"
    
    # FILL IN INGREDIENTS
    
    show hyunae explain3
    hh "{size=-6}My mother's takes {color=#3C96FF}40 minutes{/color} to prepare with a cake pan and an oven, and requires the following ingredients for the cake:\n{size=-2}• flour\n• sugar\n• salt\n• cocoa\n• butter\n• boiling water\n• buttermilk\n• 2 whole beaten eggs\n• baking soda\n• vanilla{/size}\n\nAnd the frosting requires:{size=-2}\n• butter\n• cocoa\n• milk\n• vanilla\n• powdered sugar (optional){/size}{/size}"
    
    show hyunae think2
    hh "{size=-2}The simple one takes {color=#3C96FF}5 minutes{/color} to prepare with a mug and a microwave, and requires the following ingredients:{size=-2}\n• flour\n• sugar\n• cocoa\n• 1 egg\n• milk\n• melted butter or oil\n• vanilla extract\n• chocolate chips{/size}{/size}"
    
    show hyunae satisfied blush
    hh "So... um, you should go down to your kitchen and check for ingredients."
    $ hateplus_need_ingredients = False


label hateplus_hyunae_basic_ingredients:
    
    show hyunae explain2
    $ timer = time.time() + 30
    
    menu:
        hh "Do you have flour, milk, sugar, eggs, butter, vanilla, and cocoa?"
        
        "Yes@hyunae confident2":
            if time.time() < timer:
                call hateplus_hyunae_too_short_ingredients
                jump hateplus_hyunae_basic_ingredients
            
            show hyunae satisfied
            hh "Great! Those are the most important ingredients!"
        
        "No{k=3}{/k}@hyunae stare2":
            if time.time() < timer:
                call hateplus_hyunae_too_short_ingredients
                jump hateplus_hyunae_basic_ingredients
            $ hateplus_need_ingredients = True
            
            show hyunae enthusiastic blush
            hh "Oh... well, those are all crucial, so that's good to know."
        
        "I don't know@hyunae stare3":
            
            show hyunae cheer
            hh "Well, go find out! Please, go down to your kitchen and check."
            
            jump hateplus_hyunae_basic_ingredients
    
    show hyunae explain4
    hh "Well, now that we know that, let's figure out what recipe you'll be using."
    
    $ hateplus_no_recipe = False


label hateplus_hyunae_which_recipe:
    $ hateplus_cake_type = ""
    
    show hyunae tough2 with fast
    # this shouldn't be inquisitorial, it should be friendly, excited    # Tweaked to make it more cheerful - Raide # hateplus_hyunae_beration goes right to this location again so I really can't make it too cheerful - Raide

    menu:
        hh "Which?" # REPLACE WITH GRAPHIC
        
        "Simple":
            
            show hyunae satisfied blush with fast
            hh "Very well! There's no shame in that! When I said \"any otaku could do it in a microwave\", aheh, I was thinking of myself, really..."
            
            $ hateplus_additional_ingredients = False
            $ hateplus_cake_type = "simple"
            jump hateplus_hyunae_simple_recipe
        
        "Complex":
            
            show hyunae spirited with fast
            hh "Ah, yay! That's exciting!"
            
            $ hateplus_additional_ingredients = False
            $ hateplus_hyunae_cake_type = "complex"
            jump hateplus_hyunae_complex_recipe
        
        "My own recipe":
            if hateplus_no_recipe:
                $ store.tsun += 1
                
                show hyunae mad blush with fast
                hh "Um, what are you trying to pull? You already said you didn't have one!"
                
                jump hateplus_hyunae_which_recipe
            else:
                
                show hyunae apologize with fast
                hh "Um, very well... I'll trust you!"


label hateplus_hyunae_own_recipe:
    
    show hyunae smile2 with fast
    menu:
        hh "How long does your recipe take?"
        
        "20 minutes":
            $ timer = time.time() + 60*5
        
        "40 minutes":
            $ timer = time.time() + 60*20
        
        "60 minutes or more":
            $ timer = time.time() + 60*40
    
    show hyunae satisfied
    hh "Very well! I'll wait for you! Just click the button when you're done!"

    show screen hateplus_shopping_trip
    $ renpy.pause()
    
    if time.time() < timer:
        call hateplus_hyunae_enough_time
        
        show hyunae flustered2 with fast
        menu:
            
            hh "Do you actually even have a recipe, or were you just lying about that?"
            
            "I was lying@hyunae annoyed2":
                pass
            
            "I do@hyunae weak3":
                
                show hyunae sigh blush
                hh "Oh... well, fine."
                
                show hyunae flustered2
                hh "Well, I'll let you off the hook this time... but please!"
                
                show hyunae annoyed blush
                hh "You promised you would make me a cake! You can't go back on your word now!"
                
                show hyunae serious with fast
                hh "Let's just rewind a little... answer me truthfully, this time!"
                
                jump hateplus_hyunae_own_recipe

            "I was lying@hyunae annoyed2":
                pass

        
        show hyunae yell2
        hh "Geeze... that's so mean of you!"
        
        show hyunae pressure2
        hh "Ugh..."
        
        show hyunae flustered2
        hh "Well, I'll let you off the hook this time... but please!"
        
        show hyunae mad blush with fast
        hh "You promised me you would make me a cake! You can't go back on your word now!"
        
        show hyunae busy
        hh "Let's just rewind a little, and let you pick a recipe..."
        
        $ hateplus_no_recipe = True
        
        jump hateplus_hyunae_which_recipe
    jump hateplus_hyunae_cake_done


label hateplus_hyunae_simple_recipe:
    $ timer = time.time()

    if not hateplus_need_ingredients:

        $ timer = time.time() + 30
        
        show hyunae confident with fast
        menu:
            hh "I know you have everything else, but do you also have chocolate chips?"
            
            "Yes":
                if hateplus_additional_ingredients == None and time.time() < timer:
                    call hateplus_hyunae_too_short_ingredients
                    
                    jump hateplus_hyunae_simple_recipe
                
                jump hateplus_hyunae_simple_recipe_ready
            
            "No":
                jump hateplus_hyunae_simple_recipe_no_ingredients
            
            "I don't know":
                $ hateplus_additional_ingredients = None
                
                show hyunae satisfied
                hh "Well, go find out! Please, go down to your kitchen and check."
                
                jump hateplus_hyunae_simple_recipe
    else:
        
        show hyunae think2
        hh "Well, I know you don't have all the ingredients, so..."


label hateplus_hyunae_simple_recipe_no_ingredients:
    
    if hateplus_additional_ingredients == None and time.time() < timer:
        
        call hateplus_hyunae_too_short_ingredients
        
        jump hateplus_hyunae_complex_recipe
    
    show hyunae spirited with fast
    hh "You better go to the grocery store and get them, then!"
    
    show hyunae calm
    $ timer = time.time() + 60*10

    show screen hateplus_shopping_trip
    hh "I'll wait here. Just click on the button when you're ready. Remember: flour, milk, sugar, eggs, butter, vanilla, cocoa, and chocolate chips."
    
    show hyunae smile with fast
    
    if time.time() < timer:
        
        show hyunae unsure with fast
        hh "Um... that wasn't enough time to go get the ingredients you need!"
        
        call hateplus_hyunae_beration
        
        jump hateplus_hyunae_which_recipe
    
    jump hateplus_hyunae_simple_recipe_ready

    
label hateplus_hyunae_simple_recipe_ready:

    $ timer = time.time() + 60*5
    
    show hyunae cheer with fast
    hh "Great!"
    
    show hyunae yes2
    hh "I'll just pull up the recipe for you, then, and you can just click on the button when you're done!"
    
    show hyunae smile
    # SHOULD BE PATIENT # Tweak done - Raide

    show screen hateplus_cake_recipe_simple
    $ renpy.pause()
    
    if time.time() < timer:
        
        call hateplus_hyunae_enough_time

        jump hateplus_hyunae_which_recipe
    
    jump hateplus_hyunae_cake_done


label hateplus_hyunae_complex_recipe:
    if not hateplus_need_ingredients:

        $ timer = time.time() + 30
        
        show hyunae confident with fast
        menu:
            hh "I know you have the basics, but do you also have buttermilk and baking soda? (Powdered sugar is optional.)"
            
            "Yes":
                if hateplus_additional_ingredients == None and time.time() < timer:
                    call hateplus_hyunae_too_short_ingredients
                    
                    jump hateplus_hyunae_complex_recipe
                
                jump hateplus_hyunae_complex_recipe_ready
            
            "No":
                jump hateplus_hyunae_complex_recipe_no_ingredients
            
            "I don't know":
                $ hateplus_additional_ingredients = None
                
                show hyunae cheer with fast
                hh "Well, go find out! Please, go down to your kitchen and check."
                
                jump hateplus_hyunae_complex_recipe
    else:
        
        show hyunae emo
        hh "Well, I know you don't have all the ingredients, so..."


label hateplus_hyunae_complex_recipe_no_ingredients:
    
    if hateplus_additional_ingredients == None and time.time() < timer:
        
        call hateplus_hyunae_too_short_ingredients
        
        jump hateplus_hyunae_complex_recipe
    
    show hyunae spirited with fast
    hh "You better go to the grocery store and get them, then!"

    $ timer = time.time() + 60*10
    show screen hateplus_shopping_trip
    
    show hyunae calm with fast
    hh "I'll wait here. Just click on the button when you're ready. Remember: flour, milk, sugar, eggs, butter, vanilla, cocoa, buttermilk, and baking soda. (Powedered sugar is optional.)"
    
    show hyunae smile with fast
    
    if time.time() < timer:
        
        show hyunae unsure with fast
        hh "Um... that wasn't enough time to go get the ingredients you need!"
        
        call hateplus_hyunae_beration
        
        jump hateplus_hyunae_which_recipe
    
    jump hateplus_hyunae_complex_recipe_ready


label hateplus_hyunae_complex_recipe_ready:

    $ timer = time.time() + 60*20
    
    show hyunae sure with fast
    hh "Great!"
    
    show hyunae satisfied
    hh "I'll just pull up the recipe for you, then... and you can just click on the button when you're done!"
    
    show hyunae smile with fast

    show screen hateplus_cake_recipe_complex
    $ renpy.pause()
    
    if time.time() < timer:
        
        call hateplus_hyunae_beration

        jump hateplus_hyunae_which_recipe
    
    jump hateplus_hyunae_cake_done


label hateplus_hyunae_cake_done:
    
    show hyunae stare blush with fast
    hh "All done?"
    
    show hyunae stern
    menu:
        hh "Very well! Please, be honest with me: did you, the player, actually go bake a cake?"
        
        "Of course!@hyunae approve":
            
            show hyunae genki with fast
            hh "Yay! That's so exciting!"

            $ more_dere("hateplus_cake", 3)
        
        "Not really{k=2}{/k}@hyunae annoyed blush":
            
            show hyunae angry blush
            hh "What? You mean... you lied to me?!"
            
            show hyunae give up
            hh "Geeze... why would you do that?"
            
            call hateplus_hyunae_beration

            jump hateplus_hyunae_which_recipe
        
        "I bought one@hyunae stare":
            
            show hyunae flustered2
            hh "...um, geeze, that's definitely cheating...!"
            
            show hyunae baffled with fast
            hh "But if you actually did that, then I suppose that's fair."
            
            show hyunae really
            hh "...even though I don't understand how you could buy a cake in the middle of deep space..."
            
            show hyunae serious blush
            hh "What's important is that you have it!"

    play music HATEPLUS_CAKE fadeout .5 fadein .5 loop
    
    # CAKE
    
    show hyunae cheer with fast
    show cake with Dissolve(0.5)
    hh_b "Cake, cake!"
    
    if store.use_ending == "ending1":
        
        show hyunae gomen
        hh_b "Eheh, eating cake together with my friend...!"
    else:
        if pronouns == "she":
            
            show hyunae embarrassed
            hh_b "Eheh, eating cake together with the woman I love...!"
        elif pronouns == "he":
            
            show hyunae embarrassed
            hh_b "Eheh, eating cake together with the man I love...!"
        else:
            
            show hyunae embarrassed
            hh_b "Eheh, eating cake together with the one I love...!"
    
    show hyunae flirt
    hh_b "Oh, I know! Do you have a camera? If you do, you should take a picture of us together!"

    show hyunae smile2
    hh_b "Make sure you get your cake in the shot, too!"
    
    # POSES, "Cheese!" fades away
    
    hide cake
    show hyunae cake
    with Dissolve(0.5)

    $ ui.timer(2.0, Hide("say", Dissolve(0.5)))
    hh "Cheese!"

    #$ renpy.pause()
    
    show hyunae spirited with Dissolve(0.5)
    hh "Alright, well, enough of that... let's eat!"
    
    show hyunae happy
    hh "Mmm..."
    
    $ cake_taste = ""
    
    show hyunae cheer with fast
    menu:
        hh "So... how does it taste, [title]Investigator?"
        
        "Fluffy@hyunae spirited2":
            $ cake_taste = "fluffy"
        
        "Moist@hyunae spirited2":
            $ cake_taste = "moist"
        
        "Burnt@hyunae wow":
            $ cake_taste = "burnt"
            
            show hyunae gomen
            hh "Aw... well, that's fine, so long as it's made with love!"
            
            show hyunae calm
            hh "That's what's important, I think!"
            
            if hateplus_cake_type == "simple":
                
                show hyunae apologize2
                hh "...although I don't really understand how you managed to burn something in the microwave..."
                # Need a branch if you bought the cake (how do you buy burnt cake? the shop could be sued!) - Raide
    
    if cake_taste != "burnt":
        
        show hyunae touched
        hh "Ah, that's perfect! How lovely..."
    
    $ sweetness = ""
    
    show hyunae moe
    menu:
        hh "Is it sweet?"
        
        "Yes, very!@hyunae flirt2":
            $ sweetness = "yes"
            
            show hyunae genki
            hh "Ahhh... right! I remember now, I loved things that were really sweet! They're the best!"
        
        "No, not at all@hyunae glad":
            $ sweetness = "no"
            
            show hyunae apologize
            hh "Ah, well, that's not a bad thing! Sometimes too much sweetness just gets in the way!"
        
        "You're sweetness enough@hyunae shy2":
            $ sweetness = "flirty"
            $ store.dere += 1
            
            show hyunae touched
            hh "Aheh... that's sort of a silly line, isn't it..."
            
            show hyunae embarrassed
            hh "Sorry, just sharing this moment with you has really gotten me into a funny mood!"
    
    # takes another bite, blushes
    
    show hyunae happy
    hh "Mmmm... lovely..."
    
    show hyunae calm
    hh "I remember now..."
    
    if cake_taste == "fluffy":
        if sweetness == "yes":
            
            show hyunae satisfied blush with fast
            hh "I remember the taste of a cake that was nice and fluffy, and so sweet... it's the best taste possible!"
        
        elif sweetness == "no":
            
            show hyunae satisfied with fast
            hh "I remember the taste of a cake that was nice and fluffy, and not too sweet, so you could appreciate it... it's the best taste possible!"
        
        else:
            
            show hyunae satisfied blush with fast
            hh "I remember the taste of a cake that was nice and fluffy, the kind that makes you just giggle with happiness... it's the best taste possible!"
    
    elif cake_taste == "moist":
        if sweetness == "yes":
            
            show hyunae satisfied blush with fast
            hh "I remember the taste of a cake that was nice and moist, and so sweet... it's the best taste possible!"
        
        elif sweetness == "no":
            
            show hyunae satisfied with fast
            hh "I remember the taste of a cake that was nice and moist, and not too sweet, so you could appreciate it... it's the best taste possible!"
        
        else:
            
            show hyunae satisfied blush with fast
            hh "I remember the taste of a cake that was nice and moist, the kind that makes you just giggle with happiness... it's the best taste possible!"
    
    else:
        if sweetness == "yes":
            
            show hyunae satisfied blush with fast
            hh "I remember the taste of a cake that's so obviously made with love, and so sweet... it's the best taste possible!"
        elif sweetness == "no":
            
            show hyunae satisfied blush with fast
            hh "I remember the taste of a cake that's so obviously made with love, and not too sweet, so you could appreciate it... it's the best taste possible!"
        
        else:
            
            show hyunae satisfied blush with fast
            hh "I remember the taste of a cake that's so obviously made with love, the kind that makes you just giggle with happiness... it's the best taste possible!"
    
    show hyunae gomen with fast
    hh "...oh, geeze, that sounds a little bit dirty, doesn't it? Sorry...!"
    
    show hyunae shy
    hh "Anyway..."
    
    show hyunae apologize blush
    hh "Thank you so much for humouring me! I know you put a lot of work into that, more than you usually would, so..."
    
    show hyunae genki
    hh "I really appreciate it! You're the best!"
    
    show hyunae moe
    hh "Thank you, thank you, thank you!"
    
    show hyunae touched
    hh "It's thanks to you that I can remember one of my happiest memories..."
    
    show hyunae spirited
    hh "...and aaaahhhh, this is so lovely, I'm sure I'll remember this moment forever, too!"
    
    show hyunae calm
    hh "Thank you so much..."
    
    show hyunae smile2
    hh "I feel a lot better now!"
    
    show hyunae flirt2 with fast

    $ persistent.had_cake = True
    
    jump hateplus_slow_loop


label hateplus_hyunae_too_short_ingredients:
    
    show hyunae question blush
    hh "...that wasn't enough time to go check. Even if you think so, could you please double-check?"
    
    show hyunae tough2
    hh "Please actually get up from the computer, and go look in the kitchen, please!"
    
    show hyunae insist with fast
    
    return


label hateplus_hyunae_enough_time:
    
    show hyunae question blush with fast
    hh "...um... that wasn't enough time to make a cake in."


label hateplus_hyunae_beration:
    $ more_tsun("hateplus_cake", 0)
    $ store.tsun += 1
    
    show hyunae annoyed blush with fast
    hh "Are you not taking me seriously? Are you just pretending, as a joke at my expense?"
    
    show hyunae angry blush
    hh "What do you think this is, some sort of tacky ero visual novel?"
    
    if store.use_ending == "ending1":
        
        show hyunae bitter
        hh "Do you really think friendship is as easy as just clicking the right dialogue choices on a menu...?"
    else:
        
        show hyunae bitter
        hh "Do you really think relationships are as easy as just clicking the right dialogue choices on a menu...?"
    
    show hyunae loss
    hh "Are you trying to tell me that, after all the time we've spent together, I don't deserve just a little bit of effort?"
    
    show hyunae pout
    hh "Well, here's a message to you... not as a cool space investigator, but as a player sitting at a computer screen talking to a sad girl."
    
    show hyunae yell
    hh "Stand up, get the ingredients, actually go into your kitchen, and bake a cake! A real, actual, IRL cake!"
    
    show hyunae flustered2
    hh "Please, do this for me! You promised me you would!"
    
    show hyunae lost with fast
    hh "Let me enjoy it through you, please!"
    
    return


label hateplus_hyunae_dont_deserve_to_be_happy:
    $ more_tsun("hateplus_cake", 3)
    
    show hyunae pressure with fast
    hh "What?"
    
    show hyunae angry blush
    hh "But... I thought... I..."
    
    show hyunae furious
    hh "...that's so cruel..."
    
    show hyunae tsun tsun
    hh "You don't mean that, do you?"
    
    show hyunae angry
    menu:
        hh "You're just doing that thing where you say something mean just to get me riled up, right?"
        
        "Yes, I don't really think that@hyunae annoyed2":
            pass
        
        "No, you really don't@hyunae angry blush":
            jump hateplus_hyunae_cake_rejected
        
        "Sorry...@hyunae annoyed2":
            pass
    
    show hyunae argh with fast
    hh "Aaaagh, that's so mean! That's a really cruel thing to say!"
    
    show hyunae mad2
    hh "I'm... not really very good at handling that."
    
    show hyunae pissed
    hh "...well, I know how you can make it up to me."
    
    show hyunae mad blush
    hh "You can bake me a cake!"
    
    show hyunae challenge with fast
    menu:
        hh "Promise? It's the only way I'll accept that you're sorry!"
        
        "I promise@hyunae stern2":
            pass
        
        "You don't deserve to be happy@hyunae bitter":
            jump hateplus_hyunae_cake_rejected

        "I promise@hyunae stern2":
            pass
    jump hateplus_hyunae_recipes


label hateplus_hyunae_cake_rejected:
    $ store.tsun += 1
    
    show hyunae yell2 with fast
    hh "...that's..."
    
    show hyunae pressure2
    hh "...well..."
    
    show hyunae bitter
    hh "...I guess I see how it is, then."
    
    show hyunae defensive
    hh "...fine..."
    
    show hyunae annoyed blush
    hh "...I guess, let's just get back to reading log files, then..."
    
    show hyunae flustered2
    hh "...I'm so sorry I ever said anything..."
    
    show hyunae lost with fast
    hh "...I just thought, maybe, you cared about me... for some reason..."
    
    show hyunae troubled with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_euna:
    
    show hyunae question with fast
    hh "Um, so, there's one thing, before we get started..."
    
    show hyunae busy
    hh "I realized that... you know how there were a lot of files that just looked like junk data?"
    
    show hyunae tough2
    hh "Well, I think they're actually just encrypted with the same key that *Mute's last note was."
    
    show hyunae uncertain
    hh "As far as I can tell, it's a whole block of log files about Oh Eun-a..."
    
    show hyunae melancholic
    hh "Anyway, I'm nervous to read them, but... I just thought you should know."
    
    show hyunae sulk with fast
    
    jump hateplus_slow_loop


label hateplus_hyunae_back_to_earth:
    $ hateplus_power_down_enabled = True
    if not store.hateplus_use_ending:
        $ store.hateplus_use_ending = "honeymoon"

    play music HATEPLUS_HYUNAE_WISTFUL fadeout 2.0 fadein 3.0 loop
    
    show hyunae how with fast
    hh "So..."
    
    show hyunae hmph3
    hh "...we've read everything we can before we return to Earth, I suppose."
    
    show hyunae confident
    hh "Thank you, [title]Investigator, for letting me play your sidekick."
    
    show hyunae enthusiastic with fast
    hh "The past three days could have been really hard on me, but instead, I got to experience what your job is like!"
    
    show hyunae hard with fast
    hh "And more importantly, we were finally able to solve the mystery of what happened in the year zero."
    
    show hyunae emo
    hh "It's still really hard for me to parse and understand..."
    
    show hyunae bitter
    hh "...and really, there's just so much I don't know how to deal with..."
    
    show hyunae hmph2
    hh "...but I think it's really important that I now know."
    
    show hyunae talk with fast
    menu:
        hh "So, um, tell me. How do you feel about what we've read?"
        
        "Sympathetic@hyunae anxious":
            
            show hyunae sorry
            hh "Yeah... it's hard not to..."
            
            show hyunae troubled2
            hh "...even to someone like Oh Eun-a, someone who was responsible for so many horrible things..."
            
            show hyunae guilt
            hh "...well..."
            
            show hyunae sad
            hh "...I guess I can understand doing something horrible because you feel trapped, is all I mean."
        
        "I dislike *Mute@hyunae disappoint":
            
            show hyunae pity
            hh "I don't know about her... she's vicious, and manipulative, and everything that's untrustworthy about the *Mute I knew..."
            
            show hyunae baffled
            hh "But I don't know."
            
            show hyunae shame
            hh "Even if you hate her, I don't think anyone deserves what happened to her... I feel bad for that, at least."
        
        "I hate everyone equally@hyunae mad4":
            
            show hyunae emo with fast
            hh "It's troubling, isn't it?"
            
            show hyunae flustered
            hh "Reading all this... I wish there was just a clear hero and villain and I knew who to root for."
            
            show hyunae yell2
            hh "But I guess... I mean, don't get me wrong, the actions of Emperor Ryu and Oh Eun-a were terrible! The worst! Horrifying!"
            
            show hyunae sigh blush
            hh "But I guess they're just people, in the end."
            
            show hyunae depressed blush
            hh "I don't get it... I wish there was some easy take-away."
    
    show hyunae hmm2 with fast
    hh "...well, changing the subject to something less heavy..."
    
    if not tsundere():
        
        show hyunae enthusiastic blush
        menu:
            hh "What do you think of the past three days, though? Do I make a good sidekick~?"
        
            "The best@hyunae spirited2":
                jump hateplus_hyunae_earth_the_best
        
            "You have a lot to learn@hyunae cautious2":
                jump hateplus_hyunae_earth_lot_to_learn
        
            "I don't really care@hyunae question2":
                jump hateplus_hyunae_earth_lot_to_learn
    
    elif store.use_ending == "ending2":
        
        show hyunae enthusiastic blush
        menu:
            hh "What do you think of the past three days, though? Do I make a good sidekick~?"
            
            "The best@hyunae spirited2":
                jump hateplus_hyunae_earth_the_best
            
            "You have a lot to learn@hyunae cautious2":
                jump hateplus_hyunae_earth_lot_to_learn
            
            "You're an adorable companion@hyunae shy2":
                jump hateplus_hyunae_earth_adorable
    
    else:
        
        show hyunae enthusiastic blush
        menu:
            hh "What do you think of the past three days, though? Do I make a good sidekick~?"
            
            "The best@hyunae spirited2":
                jump hateplus_hyunae_earth_the_best
            
            "You have a lot to learn@hyunae cautious2":
                jump hateplus_hyunae_earth_lot_to_learn
            
            "You're very cute@hyunae shy2":
                jump hateplus_hyunae_earth_adorable


label hateplus_hyunae_earth_adorable:
    $ store.dere += 1

    if store.use_ending == "ending2":
        
        show hyunae touched
        hh "Aheh, there I go again, with the silly flirty answers..."
    else:
        
        show hyunae gomen
        hh "Oh... I, um, really wasn't expecting you to say that, but thanks..."
    
    show hyunae sure with fast
    hh "Well, I guess I'll learn more by sticking with you, won't I?"
    
    jump hateplus_hyunae_earth_continued


label hateplus_hyunae_earth_lot_to_learn:
    $ store.tsun += 1
    
    show hyunae cautious
    hh "Oh..."
    
    show hyunae tsundere
    hh "...well, that's honest, at least."
    
    if tsundere():
        
        show hyunae sure blush with fast
        hh "But I guess I'll have a great teacher, won't I?"
        
        show hyunae satisfied blush
        hh "I'm looking forward to learning!"
    else:
        
        show hyunae baffled
        hh "...well, maybe that's just how it is."
    
    jump hateplus_hyunae_earth_continued


label hateplus_hyunae_earth_the_best:
    $ store.dere += 1
    
    show hyunae spirited
    hh "Ahhh, thank you!"
    
    if tsundere():
        
        show hyunae sure blush with fast
        hh "I know I still have a lot to learn... but I can't wait to do it by your side!"
        
        show hyunae satisfied blush
        hh "I just knew we made a good team, even just out here, together..."
    else:
        
        show hyunae touched
        hh "I've been really worrying about how you feel about me, lately..."
        
        show hyunae calm
        hh "You saying something like that gives me hope."
    
    jump hateplus_hyunae_earth_continued


label hateplus_hyunae_earth_continued:
    
    show hyunae hmph3 with fast
    hh "Anyway..."
    
    if hateplus_body_possible:
        if hateplus_body:
            
            show hyunae satisfied
            hh "I'm really looking forward to Earth, though!"
        else:
            
            show hyunae explain2
            hh "I guess I'll try asking one more time... please, this time, I need a firm answer!"
            
            show hyunae afraid with fast
            menu:
                hh "Will you get me a body, please?"
                
                "Yes@hyunae cautious":
                    
                    show hyunae gomen
                    hh "Ahhh, thank you! Thank you so much!"
                    
                    jump hateplus_hyunae_body_earth
                
                "Sorry, it's impossible@hyunae anxious":
                    pass
                
                "Sorry, it's impossible@hyunae anxious":
                    pass
            
            show hyunae lost
            hh "Oh... well, I guess that's just how it is..."
            
            jump hateplus_hyunae_no_body_earth
    else:
        jump hateplus_hyunae_no_body_earth


label hateplus_hyunae_body_earth:
    
    show hyunae genki with fast
    hh "After 622 long years, I'll have a body once again! Ahhh... what a wonderful thought..."
    
    show hyunae satisfied blush with fast
    hh "Things will finally maybe be the way they always should have been... I'll get to relearn what touch is like..."
    
    show hyunae sure
    hh "...there's a lot of difficult things that will still be in my way, but... still, I'm looking forward to it!"
    
    if store.inbox.contents[4].read:
        
        show hyunae hmph3
        hh "So, um..."
        
        show hyunae emo
        hh "...I saw that message you got, the one that was in Korean, from the historical society. I know that it said they wanted me to testify."
        
        show hyunae sigh blush
        hh "I've been really nervous to mention it, because the idea is so scary, but..."
        
        show hyunae flustered2
        menu:
            
            hh "Are... you going to do what they asked? Will you make me testify about the {i}Mugunghwa{/i}... what I did...?"
            
            "You should@hyunae bitter2":
                if very_dere():
                    
                    show hyunae surrender blush
                    hh "Well... it's a really scary thought. I barely even know how to speak to you, let alone a group of inquisitors..."
                    
                    show hyunae how
                    hh "...but..."
                    
                    show hyunae apologize blush
                    hh "...maybe if you're at my side, it'll be alright?"
                    
                    $ store.hateplus_use_ending = "truth"
                else:
                    
                    show hyunae give up
                    hh "I can't... I won't!"
                    
                    show hyunae grumpy
                    hh "I'm not ready to deal with that. Telling a group of inquisitors about what happened..."
                    
                    show hyunae lost with fast
                    hh "...I just know it, I'm not going to be able to deal with it."
                    
                    show hyunae guilt
                    hh "I'm sure, in time, I will be. But right now... I can't."
                    
                    show hyunae disappoint2
                    hh "I'm sorry to disappoint you..."
                    
                    $ store.hateplus_use_ending = "honeymoon"
            
            "You shouldn't@hyunae weak3":
                
                show hyunae sigh blush
                hh "Ah, thank you for understanding!"
                
                show hyunae emo
                hh "I mean, I know. What happened to the {i}Mugunghwa{/i} was super important, and I guess I'm a part of that."
                
                show hyunae flustered2
                hh "But some sort of inquisition... I can't deal with that at all!"
                
                show hyunae sorry with fast
                hh "So... thank you for understanding."
                
                $ store.hateplus_use_ending = "honeymoon"
            
            "It's your decision@hyunae stare2":
                
                show hyunae stare blush
                hh "Ah... that's a really tough decision."
                
                show hyunae flustered
                hh "Thank you for trusting me to make it!"
                
                show hyunae hmph
                hh "Hm..."
                
                if very_dere():
                    
                    show hyunae touched with fast
                    hh "I think... if you were at my side, I think I might be able to."
                    
                    show hyunae shame
                    hh "I guess it's important that everyone knows the truth about what happened on the {i}Mugunghwa{/i}. And... I was part of that."
                    
                    show hyunae tough2
                    hh "But only if you're by my side!"
                    
                    show hyunae troubled2
                    hh "Otherwise, I'd never have the strength to go in front of a bunch of inquisitors alone..."
                    
                    show hyunae serious blush
                    hh "But if you were there, I think I'd have the strength! That's how you make me feel."
                    
                    $ store.hateplus_use_ending = "truth"
                else:
                    
                    show hyunae sigh blush
                    hh "...no, I don't think I'd be able to do it."
                    
                    show hyunae melancholic with fast
                    hh "Maybe eventually, but now, I just... I don't feel ready for that. I don't think I could deal with that."
                    
                    show hyunae shame
                    hh "But thank you so much for leaving it up to me."
                    
                    show hyunae calm
                    hh "That's really wonderful of you!"
                    
                    $ store.hateplus_use_ending = "honeymoon"
    
    jump hateplus_hyunae_earth_finale


label hateplus_hyunae_no_body_earth:
    if very_tsun():
        
        show hyunae mad blush
        hh "Please, don't be mad, because I'm so happy for everything you've done for me..."
        
        show hyunae guilt
        hh "...but we've had so much trouble together on this voyage home... I just don't know if us being together can work."
        
        show hyunae shame
        menu:
            hh "If you'll let me... I think it would be best for both of us if we parted ways when we reached Earth."
            
            "Yes, that's for the best@hyunae anxious":
                
                show hyunae pity
                hh "Ah... well..."
                
                show hyunae lost 
                hh "Thank you for understanding. You've been good for me. I'll always remember you..."
                
                show hyunae tired2
                hh "I'm sorry it couldn't have worked out. I guess that's just how it is."
                
                show hyunae sorry
                hh "But thank you. You're such a good person, and you always make the right decisions when it counts."

                $ store.hateplus_use_ending = "hyunae_alone"
            
            "I won't allow it@hyunae afraid":
                
                show hyunae uncertain
                hh "...oh..."
                
                show hyunae mad2
                hh "...well, if that's how it is... then I suppose that's just how it is."
                
                show hyunae troubled2
                hh "Believe me... I know, I have plenty of experience with that."
                
                show hyunae shame
                hh "I guess that's just how it is."
                
                $ store.hateplus_use_ending = "caged_bird"
            
            "Do what you want@hyunae anxious":
                
                show hyunae sorry
                hh "Very well, then."
                
                show hyunae sad3
                hh "I'm not ungrateful for everything you've done... I'm really not!"
                
                show hyunae shame
                hh "I just think it's what's best for both of us."
                
                $ store.hateplus_use_ending = "hyunae_alone"

    else:
        $ store.hateplus_use_ending = "caged_bird"


label hateplus_hyunae_earth_finale:
    
    show hyunae explain with fast
    hh "Well... anyway, I suppose it's now almost time to begin star system entry procedures."
    
    show hyunae sweetso
    hh "Even from out here, I can see Earth on the visual sensors, and... it's gorgeous, isn't it? Wow..."
    
    show hyunae thinkso
    hh "No matter what happens, no matter how bad I feel about what I've learned..."
    
    show hyunae hard
    hh "...no matter how much I need to learn about people, no matter how hard it is to be a proper adult..."
    
    show hyunae tough2 with fast
    hh "No matter what, I'm going to take all the things that shaped me, that shaped what kind of ship I grew up on, and I'm going to try to put them behind me."
    
    show hyunae sad
    hh "Even if there's still so much ahead of me, thank you so much for rescuing me. Thank you for being here for me. Thank you for saving me from that prison, and putting up with me."
    
    if store.hateplus_use_ending == "caged_bird":
        
        show hyunae sorry
        hh "Maybe this future too isn't everything I dreamed it would be..."
        
        show hyunae melancholic
        hh "...maybe, in the end, I've just traded one inner chamber for another..."
        
        show hyunae tired2
        hh "But at least I'm alive."
        
        show hyunae apologize blush
        hh "I'm alive, and I'm not alone!"
    
    elif store.hateplus_use_ending == "hyunae_alone":
        
        show hyunae how with fast
        hh "Maybe I was a little too naive about things working out between us... but I don't blame you!"
        
        show hyunae sigh blush
        hh "Maybe that's just sometimes how it is. Maybe, sometimes, two people just aren't compatible."
        
        show hyunae explain2
        hh "But you saved me from despair, gave me hope, and saved my life... no matter what, I promise that's what I'll always remember you by!"
        
        show hyunae emo
        hh "From here on out, the possibilities of my future are terrifying and overwhelming..."
        
        show hyunae grumpy
        hh "What an unbelievable feeling, being overwhelmed by freedom...!"
    
    else:
        if store.use_ending == "ending1":
            if tsundere():
                
                show hyunae gomen with fast
                hh "I know you don't feel the same way, but I still love you for doing that... I'm sorry, but that's just how I feel."
            else:
                
                show hyunae moe with fast
                hh "I know we have a complicated relationship, but... I'm still so utterly happy that you're the sort of person who'd do that."
        else:
            if tsundere() and not hateplus_no_touch:
                
                show hyunae gomen with fast
                hh "I know it seemed really sudden when I confessed, but the fact that you're that kind of person... I still love you for that!"
            else:
                
                show hyunae embarrassed with fast
                hh "I know we have a complicated relationship, but I still love you for doing that... I'm sorry, but that's just how I feel."
        
        show hyunae touched
        hh "From now on, I'm going to look forward towards the future, towards that gorgeous blue planet..."
        
        show hyunae spirited
        hh "I'm sure I won't be able to look back, with you by my side!"
        
        show hyunae flirt2

    jump hateplus_slow_loop


label hateplus_hyunae_notices_death_of_mute:
    
    show hyunae explain2 with fast
    hh "Um... hey... did you not see that one labelled \"The Death of *Mute\"? I, um, really think it's important that we read it!"
    
    show hyunae explain4
    hh "I'm just going to make it so that one gets included in the extraction. I really want to read it!"
    
    $ store.to_extract[0] = embedded_data[-1].action
    
    show hyunae tough at hateplus_hyunae_farther_left with fast
    
    jump hateplus_disable_ai

# NUMBERS ARE APPROXIMATIONS, TIGHTEN LATER

label log_1_1_hyunae:
    
    if scrolled(8, korean=8):
        show hyunae staresob with fast
        if len(store.seen_characters["OldMute"]) < 2:
            hs "*Mute...!"
    
    elif scrolled(16, korean=16):
        show hyunae hmmsob with fast
        hs "I don't really see how that's a crisis..."
    
    elif scrolled(45, korean=44):
        show hyunae hardsc with fast
    
    elif scrolled(53, korean=52):
        if any_read("M1-5", "M4-2", "M6-5", "M6-9"):
            show hyunae hopelesssob with fast
            hs "1600 years old, even... wow..."
        else:
            show hyunae emo2 with fast 
            hs "...how old, I wonder..."
    
    elif scrolled(68, korean=67):
        show hyunae staresc with fast
    
    elif scrolled(78, korean=79):
        show hyunae huhsc with fast
    
    elif scrolled(86, korean=87):
        show hyunae huhso with fast
        hs "Scary..."
    
    elif scrolled(1000):
        show hyunae disappoint with fast
    
    jump log_loop

label log_1_2_hyunae:
    
    if scrolled(2, korean=1):
        show hyunae thinksc with fast
    
    elif scrolled(9, korean=8):
        show hyunae calmsob with fast
        hs "Eheh, I guess even back then she was a jerk..."
    
    elif scrolled(28, korean=28):
        show hyunae annoyedsc with fast
    
    elif scrolled(33, korean=34):
        show hyunae hmph2 with fast
        hs "Huh..."
    
    elif scrolled(65, korean=67):
        show hyunae hardsc with fast
    
    elif scrolled(71, korean=73):
        show hyunae huh with fast
        hs "...she was sarcastic to men? *Mute? Wow..."
    
    elif scrolled(87, korean=91):
        show hyunae hmmscb with fast
    
    elif scrolled(95, korean=102):
        show hyunae staresc with fast
    
    elif scrolled(124, korean=131):
        show hyunae thinksc with fast
    
    elif scrolled(132, korean=140):
        show hyunae emo with fast
        hs "I don't really get it..."
    
    elif scrolled(168, korean=180):
        show hyunae annoyedsc with fast
    
    elif scrolled(196, korean=210):
        show hyunae thinksc with fast
    
    elif scrolled(211, korean=225):
        show hyunae staresob with fast
        hs "Wait, Ryu? As in... Captain and Emperor Ryu...?"
    
    elif scrolled(1000):
        show hyunae hmph with fast
    
    jump log_loop

label log_1_3_hyunae:
    
    if scrolled(5, korean=4):
        show hyunae satisfied blush
        hs "Oh, dramas! I liked those, too...!"
    
    elif scrolled(9, korean=7):
        show hyunae suresc with fast
    
    elif scrolled(28, korean=25):
        show hyunae staresc with fast
    
    elif scrolled(36, korean=34):
        show hyunae huhso with fast
        hs "...oh, geeze! Does he mean her husband was doing...?"
    
    elif scrolled(68, korean=66):
        show hyunae huhscb with fast
    
    elif scrolled(76, korean=73):
        show hyunae sternsob with fast
        hs "Wow... Seo-yeong is really scary..."
    
    elif scrolled(86, korean=83):
        show hyunae annoyedsc with fast
    
    elif scrolled(94, korean=91):
        show hyunae annoyedsob with fast
        hs "Sounds intense..."
    
    elif scrolled(118, korean=116):
        show hyunae bittersc with fast
    
    elif scrolled(132, korean=130):
        show hyunae hmphsc with fast
    
    elif scrolled(141, korean=139):
        show hyunae calmsob with fast
        hs "You know, this Seung-bok boy seems a little awkward..."
    
    elif scrolled(1000):
        show hyunae smile with fast
    
    jump log_loop

label log_1_4_hyunae:
    
    if scrolled(2, korean=1):
        show hyunae thinksc with fast
    
    elif scrolled(10, korean=9):
        show hyunae hmph2
        hs "Huh, so much scheming..."
    
    elif scrolled(19, korean=18):
        show hyunae hmphsc with fast
    
    elif scrolled(28, korean=27):
        show hyunae staresc with fast
    
    elif scrolled(36, korean=34):
        show hyunae calmsob with fast
        hs "...aw, I guess that's pretty sweet..."
    
    elif scrolled(44, korean=42):
        show hyunae suresc with fast
    
    elif scrolled(1000):
        show hyunae smile with fast
    
    jump log_loop

label log_1_5_hyunae:
    
    if scrolled(4, korean=4):
        show hyunae thinkso with fast
        hs "Well..."
    
    elif scrolled(12, korean=10):
        show hyunae sure2
        hs "Oh, that sounds like a really good outfit...! I approve!"
    
    elif scrolled(16, korean=15):
        show hyunae starescb with fast
    
    elif scrolled(21, korean=20):
        show hyunae calmsob with fast
        hs "Skip a beat, huh..."
    
    elif scrolled(24, korean=22):
        show hyunae gomen with fast
        hs "Ahahaha, oh dear..."
    
    elif scrolled(1000):
        show hyunae smile blush with fast
    
    jump log_loop

label log_1_6_hyunae:
    
    if scrolled(8, korean=6):
        show hyunae annoyedsob with fast
        hs "Wow, this boy swears so much...!"
    
    elif scrolled(17, korean=15):
        show hyunae staresob with fast
        hs "Whoaaaaa!"
    
    elif scrolled(25, korean=23):
        show hyunae calmso
        hs "...I liked playing hwatu too, though... the cards are pretty."
    
    elif scrolled(33, korean=33):
        show hyunae evasive with fast
    
    elif scrolled(42, korean=41):
        show hyunae hmphsc with fast
    
    elif scrolled(59, korean=56):
        show hyunae staresc with fast
    
    elif scrolled(76, korean=73):
        show hyunae staresob with fast
    
    elif scrolled(99, korean=96):
        show hyunae staresc with fast
    
    elif scrolled(122, korean=122):
        show hyunae thinksc with fast
    
    elif scrolled(130, korean=131):
        show hyunae emo with fast
        hs "So even then they were using Chinese characters... that's so stupid!"

    elif scrolled(148, korean=151):
        show hyunae annoyedsc with fast
    
    elif scrolled(161, korean=166):
        show hyunae thinksc with fast
    
    elif scrolled(175, korean=179):
        show hyunae staresob with fast
    
    elif scrolled(191, korean=195):
        show hyunae suresc with fast
    
    elif scrolled(200, korean=204):
        show hyunae calmsob with fast
        hs "...aaaaa, geeze... what is he saying...?!"
    
    elif scrolled(210, korean=215):
        show hyunae satisfied blush with fast
        hs "It's... cute in a way, I suppose... is this how adults are...?"
    
    elif scrolled(217, korean=222):
        show hyunae surescb with fast
    
    elif scrolled(226, korean=231):
        if not any_read("M1-7", "M1-8", "M1-9"):
            show hyunae wow with fast
            hs "...they're both boys! Wow..."
        else:
            show hyunae sweetscb with fast
            hs "Aheh..."
    
    elif scrolled(237, korean=241):
        show hyunae gomen with fast
    
    elif scrolled(1000):
        show hyunae smile blush with fast
    
    jump log_loop

label log_1_7_hyunae:
    
    if scrolled(7, korean=9):
        show hyunae sternsob
        hs "Do... all boys swear so much?"
    
    elif scrolled(17, korean=18):
        show hyunae staresob with fast
        hs "What's going on...?"
    
    elif scrolled(29, korean=30):
        show hyunae staresc with fast
    
    elif scrolled(37, korean=38):
        show hyunae sweetsob with fast
        hs "Aww, poor thing..."
    
    elif scrolled(52, korean=54):
        show hyunae staresc with fast
    
    elif scrolled(60, korean=62):
        show hyunae calmsob with fast
        hs "Mm, western food! I miss that..."
    
    elif scrolled(70, korean=72):
        show hyunae calmsc with fast
    
    elif scrolled(80, korean=83):
        show hyunae thinksc with fast
    
    elif scrolled(88, korean=91):
        show hyunae hmph2 with fast
        hs "...so much swearing..."
    
    elif scrolled(105, korean=108):
        show hyunae staresc with fast
    
    elif scrolled(117, korean=120):
        show hyunae staresob with fast
        hs "Whoa!"
    
    elif scrolled(125, korean=128):
        show hyunae sweetsob with fast
        hs "Wh... wh... aaaaaaaa, geeze... this is...!"
    
    elif scrolled(137, korean=141):
        show hyunae funscb with fast
    
    elif scrolled(151, korean=154):
        show hyunae suresc with fast
    
    elif scrolled(159, korean=162):
        show hyunae sweetso with fast
        hs "...well, maybe that wouldn't be so bad..."
    
    elif scrolled(170, korean=173):
        show hyunae funscb with fast
    
    elif scrolled(1000):
        show hyunae apologize blush with fast
        hs "What a weird relationship... but sort of romantic..."
    
    jump log_loop

label log_1_8_hyunae:
    
    if scrolled(8, korean=10):
        show hyunae hmmsob with fast
        if any_read("M1-6", "M1-7"):
            hs "...again with all the swearing...!"
        else:
            hs "What's with all the swearing...?"
    
    elif scrolled(20, korean=22):
        show hyunae hmmco with fast
        hs "...I don't really think the idea of being 'taken' is as romantic as he says..."
    
    elif scrolled(28, korean=31):
        show hyunae hmmsc with fast
        hs "Hm..."
    
    elif scrolled(35, korean=38):
        show hyunae hmphsc with fast
    
    elif scrolled(43, korean=46):
        show hyunae stareso with fast
        hs "Wow, weird..."
    
    elif scrolled(63, korean=65):
        show hyunae hardsc with fast
    
    elif scrolled(76, korean=78):
        show hyunae huhsc with fast
    
    elif scrolled(85, korean=88):
        show hyunae huhso
        hs "Huh, really...?"
    
    elif scrolled(95, korean=97):
        show hyunae hmmsc with fast
    
    elif scrolled(114, korean=117):
        show hyunae hardsc with fast
    
    elif scrolled(122, korean=128):
        show hyunae sweetso with fast
        hs "...this is really... really..."
    
    elif scrolled(146, korean=152):
        show hyunae sweetsc with fast
    
    elif scrolled(178, korean=183):
        show hyunae funscb with fast
    
    elif scrolled(199, korean=203):
        show hyunae sweetscb with fast
    
    elif scrolled(207, korean=211):
        show hyunae heh with fast
        hs "Oh... I thought it seemed unbelievable..."
    
    elif scrolled(218, korean=222):
        show hyunae calmscb with fast
    
    elif scrolled(226, korean=230):
        show hyunae emo with fast
        hs "...he... really swears so much..."
    
    elif scrolled(236, korean=239):
        show hyunae hmmsc with fast
    
    elif scrolled(248, korean=252):
        show hyunae hmph3 with fast
        hs "...I don't get their relation at all..."
    
    elif scrolled(1000):
        show hyunae smile blush with fast
    
    jump log_loop

label log_1_9_hyunae:
    
    if scrolled(6, korean=7):
        if any_read("M1-6", "M1-7", "M1-8"):
            show hyunae sighsob with fast
            hs "He got engaged...? To a woman...?"
            #Might need a branch where you read this log without knowing the context of their relationship , or this can only be extracted after you've read their important logs. - Raide
        else:
            show hyunae annoyedsc with fast
            hs "Huh..."
        
    elif scrolled(16, korean=18):
        show hyunae bittersob with fast
        hs "...that's really cruel to her... I bet she didn't want to, either..."
    
    elif scrolled(28, korean=31):
        show hyunae weak2 with fast
    
    elif scrolled(31, korean=35):
        show hyunae pity with fast
        hs "I guess... he really loved him, huh..."
    
    elif scrolled(1000):
        show hyunae anxious with fast
    
    jump log_loop

label log_2_1_hyunae:
    
    if scrolled(3, korean=5):
        show hyunae funsob with fast
        hs "Ah, wow, she writes really cutely...!"
    
    elif scrolled(9, korean=11):
        show hyunae sweetsob with fast
        hs "Awwww..."
    
    # elif scrolled(21):
    #     show hyunae staresc with fast
    
    elif scrolled(29, korean=34):
        show hyunae heh with fast
    
    elif scrolled(39, korean=44):
        show hyunae staresob with fast
        hs "...oh..." #blush
    
    elif scrolled(47, korean=53):
        show hyunae funscb with fast
    
    elif scrolled(60, korean=65):
        show hyunae starescb with fast
    
    elif scrolled(67, korean=72):
        show hyunae sweetsob with fast
        hs "She's really charming... someone like that..."
    
    # elif scrolled(78):
    #     show hyunae heh with fast
    
    elif scrolled(95, korean=101):
        show hyunae surescb with fast
    
    elif scrolled(106, korean=114):
        show hyunae stareso with fast
    
    elif scrolled(114, korean=122):
        show hyunae staresc with fast
    
    elif scrolled(128, korean=135):
        show hyunae calmsob with fast
        hs "...would be awful nice to be with..."
    
    elif scrolled(138, korean=145):
        show hyunae satisfied blush with fast
        hs "She {i}is{/i} cool..."
    
    elif scrolled(145, korean=152):
        show hyunae funsob with fast
        hs "I'm jealous!"
    
    elif scrolled(1000):
        show hyunae flirt2 with fast
    
    jump log_loop

label log_2_2_hyunae:
    
    if scrolled(3, korean=2):
        show hyunae surrender with fast
        hs "Oh dear..."
    
    elif scrolled(6, korean=4):
        show hyunae stareso with fast
        hs "...wow, how poetic..."
    
    elif scrolled(16, korean=15):
        show hyunae hmmsc with fast
    
    elif scrolled(20, korean=19):
        show hyunae staresob with fast
    
    elif scrolled(31, korean=32):
        show hyunae hopelessscb with fast
    
    elif scrolled(39, korean=41):
        show hyunae bittersob with fast
        hs "Oh no! That's so mean...!"
    
    elif scrolled(54, korean=57):
        show hyunae annoyedscb with fast
    
    elif scrolled(65, korean=69):
        show hyunae sighscb with fast
    
    elif scrolled(72, korean=78):
        show hyunae pressurescb with fast
    
    elif scrolled(83, korean=89):
        show hyunae losssob with fast
        hs "...oh no, poor Jin-a..."
    
    elif scrolled(96, korean=103):
        show hyunae bitterscb with fast
    
    elif scrolled(104, korean=112):
        show hyunae starescb with fast
    
    elif scrolled(112, korean=120):
        show hyunae funsob with fast
        hs "Ah! Wow! She's clever...! I wouldn't have been able to do that..."
    
    elif scrolled(123, korean=131):
        show hyunae surescb with fast
    
    elif scrolled(131, korean=139):
        show hyunae sweetsob with fast
        hs "Oh, geeze...!"
    
    elif scrolled(146, korean=153):
        show hyunae staresob with fast
    
    elif scrolled(154, korean=161):
        show hyunae gomen with fast
        hs "...this is so embarrassing..."
    
    elif scrolled(170, korean=179):
        show hyunae sweetscb with fast
    
    elif scrolled(176, korean=185):
        show hyunae staresob with fast
    
    elif scrolled(185, korean=195):
        show hyunae sweetsob with fast
        hs "...but maybe just a little bit enviable..."
    
    elif scrolled(192, korean=201):
        show hyunae sighsob with fast
    
    elif scrolled(213, korean=225):
        show hyunae calmscb with fast
    
    elif scrolled(226, korean=238):
        show hyunae sure blush with fast
        hs "Is... this what adult relationships are like...?"
    
    elif scrolled(1000):
        show hyunae glad with fast
    
    jump log_loop

label log_2_3_hyunae:
    
    if scrolled(7, korean=6):
        show hyunae thinksc with fast
        hs "Hm..."
    
    elif scrolled(15, korean=15):
        show hyunae huhso with fast
        hs "...that sounds interesting, I suppose..."
    
    elif scrolled(24, korean=22):
        show hyunae boredsc with fast
    
    elif scrolled(29, korean=26):
        show hyunae huh with fast
        hs "I don't really get why this was included, though... it's kinda boring..."
    
    elif scrolled(1000):
        show hyunae look with fast
    
    jump log_loop

label log_2_4_hyunae:
    
    if scrolled(7, korean=7):
        if pronouns == "she":
            show hyunae sweetsob with fast
            hs "Aheh, 'girl-feelings!' I know what those are like...!"
        else:
            show hyunae funsob with fast
            hs "Ah, cute!"
    
    elif scrolled(19, korean=19):
        show hyunae stare blush with fast
        hs "Is that what wine makes you do...? I've never had any..."
    
    elif scrolled(28, korean=27):
        show hyunae gomen with fast
        hs "...why wouldn't she...? Is Ae-jeong a noisy sleeper...?"
    
    elif scrolled(36, korean=36):
        show hyunae staresob with fast
        hs "...oh, my..."
    
    elif scrolled(45, korean=45):
        show hyunae sweetscb with fast
    
    elif scrolled(53, korean=53):
        show hyunae awkward with fast
        hs "...this is really... really... really...!"
    
    elif scrolled(61, korean=61):
        show hyunae touched with fast
        
    elif scrolled(77, korean=77):
        show hyunae happy with fast
    
    elif scrolled(88, korean=89):
        show hyunae awkward with fast
        hs "Is that normal for a girl's body...?"
    
    elif scrolled(101, korean=102):
        show hyunae calmsob with fast
        hs "Aaaaaa! Oh geeze, oh geeze, oh geeze..."
    
    elif scrolled(117, korean=118):
        show hyunae sweetsob with fast
        hs "This is really..."
    
    elif scrolled(127, korean=128):
        show hyunae heh with fast
        hs "Aaaaaaaaaaaaaa! This is... that sounds like... I'd... gosh..."
    
    elif scrolled(131, korean=131):
        show hyunae touched with fast
        hs "This is so indecent...! But... also... maybe a little romantic..."
    
    elif scrolled(1000):
        show hyunae flirt2 with fast
    
    jump log_loop

label log_2_5_hyunae:
    
    if scrolled(4, korean=3):
        show hyunae surrender blush with fast
        hs "Oh... that's bad..."
    
    elif scrolled(11, korean=9):
        show hyunae bittersob with fast
        hs "What does she mean by that...?"
    
    elif scrolled(17, korean=15):
        
        show hyunae flustered3 with fast
        hs "Oh..."
    
    elif scrolled(25, korean=25):
        show hyunae losssob with fast
        hs "Awww, that's sweet, at least..."
    
    elif scrolled(38, korean=37):
        show hyunae lossscb with fast
    
    elif scrolled(49, korean=49):
        show hyunae hmmsob with fast
        hs "...wow... saying these things... that sounds... that sounds...!"
    
    elif scrolled(57, korean=57):
        show hyunae bittersob with fast
        hs "Oh geeze... I shouldn't be reading this..."
    
    elif scrolled(66, korean=68):
        show hyunae hopelessscb with fast
    
    elif scrolled(79, korean=81):
        show hyunae sighscb with fast
    
    elif scrolled(81, korean=83):
        show hyunae bitterscb with fast
    
    elif scrolled(89, korean=92):
        show hyunae surrender blush with fast
        hs "...this is..."
    
    elif scrolled(105, korean=107):
        show hyunae lossscb with fast
    
    elif scrolled(113, korean=113):
        show hyunae bitterscb with fast
    
    elif scrolled(117, korean=117):
        show hyunae shame with fast
        hs "...I feel really sad for her, though..."
    
    elif scrolled(1000):
        show hyunae troubled with fast
    
    jump log_loop

label log_2_6_hyunae:
    
    if scrolled(6, korean=4):
        show hyunae annoyedsob with fast
        hs "\"Tamed,\" huh. That... isn't really funny..."
    
    elif scrolled(17, korean=13):
        show hyunae hmmco with fast
        hs "I don't really get it... but it does sound boring..."
    
    elif scrolled(30, korean=25):
        show hyunae hardsc with fast
    
    elif scrolled(34, korean=28):
        show hyunae sigh with fast
        hs "I still don't understand why these were included, though... they're boring too."
    
    elif scrolled(1000):
        show hyunae grr with fast
    
    jump log_loop

label log_2_7_hyunae:
    
    if scrolled(13, korean=13):
        show hyunae hopelesssob with fast
        hs "She's so poetic about everything..."
    
    elif scrolled(22, korean=23):
        show hyunae annoyedsob with fast
        hs "...well, fathers don't always know what's right..."
    
    elif scrolled(30, korean=30):
        show hyunae losssob with fast
        hs "Oh no... oh no..."
    
    elif scrolled(42, korean=46):
        show hyunae losssc with fast
    
    elif scrolled(53, korean=55):
        show hyunae depressed with fast
        hs "Oh, wow, I forgot about canned tea! I kinda miss it."
    
    elif scrolled(61, korean=63):
        show hyunae bittersob with fast
        hs "No!"
    
    elif scrolled(73, korean=76):
        show hyunae sighscb with fast
    
    elif scrolled(81, korean=85):
        show hyunae pressuresob with fast
        hs "No, no, don't marry some old man! You have someone who loves you...!"
    
    elif scrolled(102, korean=106):
        show hyunae annoyedscb with fast
    
    elif scrolled(116, korean=120):
        show hyunae pressurescb with fast
    
    elif scrolled(128, korean=132):
        show hyunae guilt with fast
        hs "...this really hurts to read... just..."
    
    elif scrolled(142, korean=146):
        show hyunae pity with fast
        hs "...no..."
    
    elif scrolled(150, korean=155) and any_read("M2-2", "M2-4", "M2-5", "M2-6"):
        show hyunae sad with fast
        hs "They were such a good couple, though...!"
    
    elif scrolled(1000):
        show hyunae lost with fast
        hs "If that's what love's like... maybe it's better that I never knew it..."
    
    jump log_loop

label log_2_8_hyunae:
    
    if scrolled(4, korean=6) and any_read("M2-2", "M2-4", "M2-5", "M2-6"):
        show hyunae bittersob with fast
        hs "Oh no... but they were so good together..."
    
    elif scrolled(13, korean=16):
        show hyunae annoyedsob with fast
        hs "...oh... I think I know how this ends..."
    
    elif scrolled(23, korean=26):
        show hyunae lossscb with fast
    
    elif scrolled(30, korean=33):
        show hyunae pressuresob with fast
        hs "...no, don't do that...!"
    
    elif scrolled(40, korean=44):
        show hyunae sigh blush with fast
    
    elif scrolled(49, korean=53):
        show hyunae bitterscb with fast
    
    elif scrolled(57, korean=62):
        show hyunae hmmsob with fast
        hs "...I... think she's being a little harsh, though..."
    
    elif scrolled(66, korean=73):
        show hyunae hopelessscb with fast
    
    elif scrolled(78, korean=84):
        show hyunae surrender blush with fast
        hs "Really...?"
    
    elif scrolled(92, korean=100):
        show hyunae sighscb with fast
    
    elif scrolled(107, korean=118):
        show hyunae sigh blush with fast
    
    elif scrolled(1000):
        show hyunae shame with fast
        hs "...yeah. That was really painful to read..."
    
    jump log_loop

label log_2_9_hyunae:
    
    if scrolled(5, korean=3):
        show hyunae annoyedso with fast
        hs "I guess the Ryu family house never really changed much."
    
    elif scrolled(12, korean=10):
        show hyunae surrender blush with fast
    
    elif scrolled(20, korean=17):
        show hyunae bittersob with fast
        hs "...how humiliating..."
    
    elif scrolled(31, korean=28):
        show hyunae bitterscb with fast
    
    elif scrolled(39, korean=35):
        show hyunae pressuresob with fast
        hs "...gross!"
    
    elif scrolled(52, korean=48):
        show hyunae pressurescb with fast
    
    elif scrolled(60, korean=55) and read("M2-2"):
        show hyunae hopelesssob with fast
        hs "Awwww... she kept the hairpin! Wow..."
    
    elif scrolled(66, korean=61):
        show hyunae hopelessscb with fast
    
    elif scrolled(1000):
        show hyunae anxious with fast
    
    jump log_loop

label log_3_1_hyunae:
    
    if scrolled(8, korean=5):
        show hyunae hardscb with fast
        hs "Hm..."
    
    elif scrolled(17, korean=13):
        show hyunae hmmsob with fast
        hs "Wait, what?! That wasn't what I was expecting from her..."
    
    elif scrolled(32, korean=30):
        show hyunae annoyedsc with fast
    
    elif scrolled(40, korean=39):
        show hyunae pout with fast
        hs "...she, um, sure uses a lot of big words... I don't get it..."
    
    elif scrolled(48, korean=47):
        show hyunae stern with fast
        hs "Spoiler warning: the future sucked!"
    
    elif scrolled(65, korean=63):
        show hyunae hmmsc with fast
    
    elif scrolled(73, korean=71):
        show hyunae hmmco with fast
        hs "This is kinda boring..."
    
    elif scrolled(96, korean=95):
        show hyunae bittersc with fast
    
    elif scrolled(104, korean=102):
        show hyunae grumpy with fast
        hs "...wait, she's saying..."
    
    elif scrolled(123, korean=121):
        show hyunae pressurescb with fast
    
    elif scrolled(130, korean=129):
        show hyunae defensive with fast
        hs "Gross..."
    
    elif scrolled(138, korean=138):
        show hyunae pout with fast
        hs "What is she even doing...? This is so gross..."
    
    elif scrolled(167, korean=167):
        show hyunae bitterscb with fast
    
    elif scrolled(1000):
        show hyunae baffled with fast
        hs "I don't like her."
    
    jump log_loop

label log_3_2_hyunae:
    
    if scrolled(10, korean=13) and any_read("M3-1", "M3-3", "M3-4", "M3-5", "M3-6", "M3-7", "M3-8", "M3-9"):
        show hyunae hopelessso with fast
        hs "Oh, so this is the little sister, then..."
    
    elif scrolled(20, korean=23):
        show hyunae surrender with fast
        hs "Yikes..."
    
    elif scrolled(30, korean=35):
        show hyunae bittersc with fast
    
    elif scrolled(39, korean=44):
        show hyunae bittersob with fast
        hs "That's awful! Believe me, I'd know...!"
    
    elif scrolled(50, korean=56):
        show hyunae annoyedscb with fast
    
    elif scrolled(65, korean=72):
        show hyunae huhscb with fast
    
    elif scrolled(79, korean=87):
        show hyunae pressuresc with fast
    
    elif scrolled(86, korean=96):
        show hyunae pressuresob with fast
        hs "...I don't get it, but I'm sure that's wrong..."
    
    elif scrolled(94, korean=104):
        show hyunae bittersob with fast
        hs "I think love is more important, too..."
    
    elif scrolled(108, korean=120):
        show hyunae sighscb with fast
    
    elif scrolled(1000):
        show hyunae troubled2 with fast
        hs "...she's really cruel, I think..."
    
    jump log_loop

label log_3_3_hyunae:
    
    if scrolled(6, korean=5) and any_read("M3-1", "M3-2", "M3-4", "M3-5", "M3-7", "M3-8", "M3-9"):
        show hyunae hmmsob with fast
        hs "\"Consort\"? And I thought her name was Oh...?"
    
    elif scrolled(20, korean=18):
        show hyunae sternsob with fast
        hs "...this does sound like a bad situation..."
    
    elif scrolled(34, korean=33):
        show hyunae hmmsc with fast
    
    elif scrolled(1000):
        show hyunae shame with fast
        hs "I guess she's really loyal to her big sister..."
    
    jump log_loop

label log_3_4_hyunae:
    
    if scrolled(10, korean=9) and read("M1-1"):
        show hyunae flustered with fast
        hs "Wait, writing on paper...? I thought that was illegal...!"
    
    elif scrolled(20, korean=20):
        show hyunae weak2 with fast
        hs "Oh... that's really sad..."
    
    elif scrolled(28, korean=28):
        show hyunae bittersob with fast
        hs "I guess Eun-a wasn't always like that..."
    
    elif scrolled(35, korean=34):
        show hyunae hmmcob with fast
        hs "What time of month does she mean by \"that\" one...?"
    
    elif scrolled(49, korean=46):
        show hyunae sighscb with fast
    
    elif scrolled(60, korean=57):
        show hyunae losssob with fast
        hs "Oh no..."
    
    elif scrolled(68, korean=66):
        show hyunae emo with fast
        hs "She's lucky to have someone who worries about her so much..."
    
    elif scrolled(77, korean=75):
        show hyunae bitterscb with fast
    
    elif scrolled(85, korean=83):
        show hyunae surrender blush with fast
    
    elif scrolled(1000):
        show hyunae sigh blush with fast
        hs "...oh."
    
    jump log_loop

label log_3_5_hyunae:
    
    if scrolled(8, korean=8):
        show hyunae hmmsob with fast
        hs "\"That way\"...?"
    
    elif scrolled(16, korean=17):
        show hyunae grumpy with fast
        hs "I just... don't get it."
    
    elif scrolled(24, korean=25):
        show hyunae annoyedsob with fast
        hs "...I feel really uncomfortable reading this..."
    
    elif scrolled(35, korean=35):
        show hyunae annoyedscb with fast
    
    elif scrolled(56, korean=57):
        show hyunae bittersc with fast
    
    elif scrolled(64, korean=65):
        show hyunae pout with fast
        hs "...that sounds like something my mother would say."
    
    elif scrolled(74, korean=75):
        show hyunae lossso with fast
    
    elif scrolled(82, korean=84):
        show hyunae grumpy with fast
        hs "Being an emperor's consort really isn't as romantic as she thinks..."
    
    elif scrolled(91, korean=92):
        show hyunae bitterscb with fast
    
    elif scrolled(99, korean=99):
        show hyunae bittersob with fast
        hs "Why...?"
    
    elif scrolled(111, korean=111):
        show hyunae sighscb with fast
    
    elif scrolled(121, korean=120):
        show hyunae surrender blush with fast
    
    elif scrolled(1000):
        show hyunae mad blush with fast
        hs "She's wrong! It didn't solve anything! It just made things worse!"
    
    jump log_loop

label log_3_6_hyunae:
    
    if scrolled(1000):
        show hyunae guilt with fast
        hs "Oh, geeze... no!"
    
    jump log_loop

label log_3_7_hyunae:
    
    if scrolled(4, korean=4):
        show hyunae bittersc with fast
    
    elif scrolled(18, korean=21):
        show hyunae huhso with fast
        hs "She sure sounds unhinged..."
    
    elif scrolled(32, korean=35):
        show hyunae losssob with fast
        hs "Oh... mourning attire. Of course."
    
    elif scrolled(46, korean=49):
        show hyunae hmmsob with fast
        hs "...weird...?"
    
    elif scrolled(56, korean=60):
        show hyunae hmmco with fast
        hs "Yeah... I don't remember anyone drinking tea with the servants, either..."
    
    elif scrolled(64, korean=69):
        show hyunae huhso with fast
        hs "...that's... a little bit... um..."
    
    elif scrolled(75, korean=80):
        show hyunae hmmscb with fast
    
    elif scrolled(78, korean=83):
        show hyunae huhscb with fast
    
    elif scrolled(1000):
        show hyunae pity with fast
        hs "...I don't really know how to feel about her anymore..."
    
    jump log_loop

label log_3_8_hyunae:
    
    if scrolled(10, korean=9):
        show hyunae sigh blush with fast
        hs "...now I just feel bad..."
    
    elif scrolled(18, korean=18):
        show hyunae losssc with fast
    
    elif scrolled(26, korean=26):
        show hyunae losssob with fast
        hs "...well, I understand that feeling..."
    
    elif scrolled(36, korean=37):
        show hyunae hopelessscb with fast
    
    elif scrolled(44, korean=44):
        show hyunae surrender blush with fast
        hs "...yeah, it's a nice feeling... but... but..."
    
    elif scrolled(52, korean=52):
        show hyunae bitterscb with fast
    
    elif scrolled(66, korean=64):
        show hyunae hmmscb with fast
    
    elif scrolled(1000):
        show hyunae sad with fast
        hs "Oh... that's so sad..."
    
    jump log_loop

label log_3_9_hyunae:
    
    if scrolled(9, korean=6):
        show hyunae annoyedsc with fast
    
    elif scrolled(24, korean=20):
        show hyunae defensivesc with fast
    
    elif scrolled(34, korean=29):
        show hyunae pout with fast
        hs "I don't really know what to think..."
    
    elif scrolled(47, korean=43):
        show hyunae bittersob with fast
        hs "...well, I guess we know how that went..."
    
    elif scrolled(56, korean=53):
        show hyunae sighscb with fast
        hs "..."
    
    elif scrolled(64, korean=61):
        show hyunae lossso with fast
    
    elif scrolled(1000):
        show hyunae lost with fast
        hs "I... never would have thought... she was thinking of her little sister the whole time...?"
    
    jump log_loop

label log_4_1_hyunae:
    
    if scrolled(16, korean=15):
        show hyunae sternsc with fast
        hs "Hm..."
    
    elif scrolled(27, korean=27):
        show hyunae hardsc with fast
    
    elif scrolled(35, korean=35):
        show hyunae hmmcob with fast
        hs "...I don't understand what they're talking about..."
    
    elif scrolled(64, korean=64):
        show hyunae hmmsc with fast
    
    elif scrolled(72, korean=72):
        show hyunae pressuresob with fast
        hs "...oh. But... learning Chinese characters {i}is{/i} silly!"
    
    elif scrolled(92, korean=92):
        show hyunae annoyedsc with fast
    
    elif scrolled(100, korean=100):
        show hyunae hmmsob with fast
        hs "Whoa... *Mute back then really was harsh..."
    
    elif scrolled(121, korean=120):
        show hyunae hmmsc with fast
    
    elif scrolled(153, korean=152):
        show hyunae bittersc with fast
    
    elif scrolled(164, korean=163):
        show hyunae sigh with fast
        hs "Well... alright..."
    
    elif scrolled(1000):
        show hyunae grr with fast
    
    jump log_loop

label log_4_2_hyunae:
    
    if scrolled(10, korean=9) and read("M1-2"):
        show hyunae explain2 with fast
        hs "Oh, this is what *Mute and Smith and Seo-yeong were talking about...!"
    
    elif scrolled(44, korean=42):
        show hyunae hmphsc with fast
    
    elif scrolled(61, korean=58):
        show hyunae staresob with fast
    
    elif scrolled(71, korean=68):
        show hyunae hardsob with fast
        hs "...ha ha, wow, I always thought politics would be more civil..."
    
    elif scrolled(92, korean=90):
        show hyunae hmmsc with fast
    
    elif scrolled(102, korean=99):
        show hyunae huhsc with fast
        hs "...huh..."
    
    elif scrolled(132, korean=128):
        show hyunae hmphsc with fast
    
    elif scrolled(160, korean=156):
        show hyunae bittersc with fast
    
    elif scrolled(170, korean=167):
        if not read("M1-5"):
            show hyunae stare blush with fast
            hs "1600 years! Wow... that's even older than I am...!"
            # Might need branch if you've seen this number back in 1_5 - Raide
        else:
            show hyunae sternso with fast
            hs "She sure keeps bringing up her age, doesn't she?"
    
    elif scrolled(183, korean=181):
        show hyunae hmphsc with fast
    
    elif scrolled(207, korean=204):
        show hyunae melancholic with fast
        hs "...this is, um, kinda boring, honestly..."
    
    elif scrolled(1000):
        show hyunae disappoint with fast
    
    jump log_loop

label log_4_3_hyunae:
    
    if scrolled(8, korean=9):
        show hyunae inorite with fast
        hs "So Ryu was Chief Councillor by then, I guess?"
    
    elif scrolled(15, korean=15):
        show hyunae hmmsc with fast
    
    elif scrolled(28, korean=28):
        show hyunae hmmso with fast
        hs "...lots of bickering..."
    
    elif scrolled(38, korean=38):
        show hyunae annoyedso with fast
        hs "...and really boring economics-type stuff..."
    
    elif scrolled(67, korean=68):
        show hyunae annoyedsc with fast
    
    elif scrolled(77, korean=78):
        show hyunae sigh with fast
        hs "I don't really get it..."
    
    elif scrolled(108, korean=109):
        show hyunae hopelesssc with fast
    
    elif scrolled(137, korean=139):
        show hyunae hmmsc with fast
    
    elif scrolled(159, korean=161):
        show hyunae defensivesc with fast
    
    elif scrolled(197, korean=197):
        show hyunae hardsc with fast
    
    elif scrolled(1000):
        show hyunae sulk with fast
    
    jump log_loop

label log_4_4_hyunae:
    
    if scrolled(50, korean=48):
        show hyunae boredsc with fast
    
    elif scrolled(1000):
        show hyunae busy with fast
        hs "I don't really get why this is important, either..."
    
    jump log_loop

label log_4_5_hyunae:
    
    if scrolled(10, korean=9):
        show hyunae annoyedso with fast
        hs "Geeze, so much cursing, even in politics...!"
    
    elif scrolled(32, korean=31):
        show hyunae hardsc with fast
    
    elif scrolled(40, korean=37):
        show hyunae hmmso with fast
        hs "I don't get it..."
    
    elif scrolled(85, korean=80):
        show hyunae hmmsc with fast
    
    elif scrolled(124, korean=121):
        show hyunae bittersc with fast
    
    elif scrolled(134, korean=131):
        show hyunae huhso with fast
        hs "Oh, ha ha, well... alright..."
    
    elif scrolled(150, korean=147):
        show hyunae hmmsc with fast
    
    elif scrolled(194, korean=190):
        show hyunae sternsc with fast
    
    elif scrolled(204, korean=200):
        show hyunae hardsc with fast
    
    elif scrolled(214, korean=210):
        show hyunae annoyedso with fast
        hs "...wow, harsh..."
    
    elif scrolled(240, korean=237):
        show hyunae annoyedsc with fast
    
    elif scrolled(248, korean=245):
        show hyunae bitterscb with fast
    
    elif scrolled(1000):
        show hyunae busy with fast
        hs "...still don't really get it..."
    
    jump log_loop

label log_4_6_hyunae:
    
    if scrolled(10, korean=11):
        if any_read("M4-1", "M4-2", "M4-3", "M4-4", "M4-5"):
            show hyunae bittersob with fast
            hs "Oh no! Does this mean I have to remember a whole new set of confusing names...?"
        else:
            show hyunae hmmsc with fast
            hs "Huh..."
    
    elif scrolled(19, korean=19):
        show hyunae hardsc with fast
    
    elif scrolled(31, korean=30):
        show hyunae annoyedsob with fast
        hs "...geeze... *Mute seems kinda..."
    
    elif scrolled(41, korean=40):
        show hyunae hmmsob with fast
        hs "Wait, I thought engineering was supposed to be our family! Why is his name Han...?"
    
    elif scrolled(53, korean=52):
        show hyunae hmmsc with fast
    
    elif scrolled(66, korean=65):
        show hyunae huhso with fast
        hs "...she's really intense...!"
    
    elif scrolled(76, korean=77):
        show hyunae explain4 with fast
        hs "...it sounds like she was stopping a lot of bad ideas, though..."
    
    elif scrolled(111, korean=111):
        show hyunae annoyedsc with fast
    
    elif scrolled(130, korean=130):
        show hyunae bittersc with fast
    
    elif scrolled(138, korean=139):
        show hyunae huhsc with fast
    
    elif scrolled(148, korean=149):
        show hyunae emo with fast
        hs "...harsh..."
    
    elif scrolled(186, korean=186):
        show hyunae losssc with fast
    
    elif scrolled(204, korean=205):
        show hyunae hopelessso with fast
        hs "...oh..."
    
    elif scrolled(214, korean=215):
        show hyunae hmmsob with fast
        hs "I guess the rest of the council is just as hostile as her, huh..."
    
    elif scrolled(242, korean=242):
        show hyunae sighsc with fast
    
    elif scrolled(1000):
        show hyunae tired with fast
    
    jump log_loop

label log_4_7_hyunae:
    
    if scrolled(14, korean=10):
        show hyunae boredsc with fast
        hs "Hm..."
    
    elif scrolled(24, korean=20):
        show hyunae hmmco with fast
        hs "...I don't really get all this stuff about money..."
    
    elif scrolled(62, korean=58):
        show hyunae hmmsc with fast
    
    elif scrolled(80, korean=75):
        show hyunae hardsc with fast
    
    elif scrolled(89, korean=83):
        show hyunae sigh with fast
    
    elif scrolled(1000):
        show hyunae disappoint with fast
    
    jump log_loop

label log_4_8_hyunae:
    
    if scrolled(16, korean=18):
        if any_read("M4-1", "M4-2", "M4-3", "M4-4", "M4-5", "M4-6", "M4-7", "M4-9"):
            show hyunae hmmsob with fast
            hs "Wow... she's really even more hostile than before..."
        else:
            show hyunae hardsob with fast
            hs "Wow... so hostile..."
    
    elif scrolled(41, korean=42):
        show hyunae hardscb with fast
    
    elif scrolled(52, korean=53):
        show hyunae annoyedsob with fast
        hs "...really hostile..."
    
    elif scrolled(62, korean=63):
        show hyunae bittersob with fast
        hs "I still don't get any of this... what are they talking about...?"
    
    elif scrolled(73, korean=74):
        show hyunae hmmscb with fast
    
    elif scrolled(96, korean=98):
        show hyunae hmphsc with fast
    
    elif scrolled(127, korean=129):
        show hyunae hopelesssc with fast
    
    elif scrolled(136, korean=138):
        show hyunae baffled with fast
        hs "I don't really get any of this boring stuff at all..."
    
    elif scrolled(1000):
        show hyunae tired with fast
    
    jump log_loop

label log_4_9_hyunae:
    
    if scrolled(8, korean=8):
        show hyunae bitterso with fast
        hs "Wow, this atmosphere is..."
    
    elif scrolled(16, korean=17):
        show hyunae annoyedsob with fast
        hs "...really intense..."
    
    elif scrolled(23, korean=24):
        show hyunae bittersob with fast
        hs "...I don't really get it, but..."
    
    elif scrolled(31, korean=31):
        show hyunae sighsob with fast
        hs "...it really seems like she believes strongly about this..."
    
    elif scrolled(53, korean=54):
        show hyunae hmmsc with fast
    
    elif scrolled(82, korean=83):
        show hyunae bitterscb with fast
    
    elif scrolled(103, korean=105):
        show hyunae huhso with fast
        hs "Wait... if she was worried about there being just one leader forever...!"
    
    elif scrolled(116, korean=118):
        show hyunae sighscb with fast
    
    elif scrolled(128, korean=130):
        show hyunae pressuresc with fast
    
    elif scrolled(144, korean=146):
        show hyunae defensivescb with fast
    
    elif scrolled(161, korean=163):
        show hyunae bitterscb with fast
    
    elif scrolled(182, korean=185):
        show hyunae baffled with fast
        hs "...wow, shot down..."
    
    elif scrolled(1000):
        show hyunae disappoint with fast
    
    jump log_loop

label log_5_1_hyunae:
    
    if scrolled(11, korean=10):
        show hyunae starescb with fast
        hs "Hm..."
    
    elif scrolled(24, korean=25):
        if not any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"):
            show hyunae funsob with fast
            hs "Oh! She's an engineer! That's nice...!"
        else:
            show hyunae satisfied with fast
            hs "I really like that she's an engineer!"
    
    elif scrolled(32, korean=32):
        show hyunae sweetsob with fast
        hs "Yeah! That was exactly what I wanted to grow up to be like, too...! She understands...!"
    
    elif scrolled(41, korean=41):
        show hyunae calmsc with fast
    
    elif scrolled(52, korean=52):
        show hyunae hmph3 with fast
        hs "...able to say \"no,\" huh..."
    
    elif scrolled(1000):
        show hyunae touched with fast
        hs "Ah, well, that's nice of her..."
    
    jump log_loop

label log_5_2_hyunae:
    
    if scrolled(4, korean=4):
        if read("M5-1"):
            show hyunae sweetsob with fast
            hs "So, she got married..."
        else:
            show hyunae funso with fast
            hs "So, she was newly-wed..."
    
    elif scrolled(14, korean=14):
        show hyunae satisfied blush with fast
        hs "...ah, that's really romantic, though..."
    
    elif scrolled(25, korean=24):
        show hyunae surescb with fast
    
    elif scrolled(30, korean=29):
        show hyunae evasive with fast
        hs "That's nice, but... I don't get what \"silence requirements\" means..."
    
    elif scrolled(36, korean=35):
        show hyunae staresob with fast
        hs "Oh!"
    
    elif scrolled(44, korean=42):
        show hyunae calmsob with fast
        hs "Oh my..."
    
    elif scrolled(1000):
        show hyunae gomen with fast
        hs "Aw, they sound like a cute couple... I'm happy for them!"
    
    jump log_loop

label log_5_3_hyunae:
    
    if scrolled(8, korean=6):
        show hyunae funsob with fast
        hs "Ah, that's good for her..."
    
    elif scrolled(17, korean=15):
        show hyunae funsc with fast
    
    elif scrolled(33, korean=30):
        show hyunae sweetso with fast
        hs "I don't know, I'd really like it if someone touched me like that..."
    
    elif scrolled(41, korean=38):
        show hyunae flustered with fast
        hs "Whoa! Really? I mean... I remember, that was a really big problem in my time...!"
    
    elif scrolled(51, korean=47):
        show hyunae hardsc with fast
    
    elif scrolled(62, korean=58):
        show hyunae flustered3 with fast
        hs "...oh no...!"
    
    elif scrolled(70, korean=67):
        show hyunae grumpy with fast
        hs "...oh, geeze, So-yi..."
    
    elif scrolled(81, korean=77):
        show hyunae bitterscb with fast
    
    elif scrolled(90, korean=93):
        show hyunae defensive with fast
        hs "...this is horrible! I can't believe I said... that's really horrible!"
    
    elif scrolled(101, korean=98):
        show hyunae lossscb with fast
    
    elif scrolled(112, korean=109):
        show hyunae pressuresob with fast
        hs "...no, it's not her fault, why does she think that..."
    
    elif scrolled(120, korean=116):
        show hyunae bittersob with fast
        hs "...that sounds so scary..."
    
    elif scrolled(133, korean=129):
        show hyunae surrender blush with fast
    
    elif scrolled(149, korean=145):
        show hyunae hopelesssob with fast
        hs "...oh..."
    
    elif scrolled(162, korean=158):
        show hyunae sigh blush with fast
        hs "...he's such a good man... I'm really glad she had him."
    
    elif scrolled(176, korean=171):
        show hyunae surrender blush with fast
    
    elif scrolled(183, korean=178):
        show hyunae hopelessscb with fast
    
    elif scrolled(199, korean=192):
        show hyunae bitterscb with fast
    
    elif scrolled(1000):
        show hyunae lost with fast
        hs "Geeze, that's such a scary situation... I wouldn't have been able to deal with that..."
    
    jump log_loop

label log_5_4_hyunae:
    
    if scrolled(8, korean=4):
        show hyunae hmmcob with fast
        hs "Sounds like hard work... so that's what it's like to be an adult...?"
    
    elif scrolled(19, korean=15):
        show hyunae grumpy with fast
        hs "That doesn't sound fair!"
    
    elif scrolled(29, korean=24):
        show hyunae annoyedscb with fast
    
    elif scrolled(40, korean=36):
        show hyunae sighsob with fast
        hs "I guess even in a time when women were allowed to work, things were complicated..."
    
    elif scrolled(48, korean=44):
        show hyunae bitterscb with fast
    
    elif scrolled(59, korean=54):
        show hyunae defensivesc with fast
    
    elif scrolled(70, korean=65):
        show hyunae surrender blush with fast
    
    elif scrolled(76, korean=70):
        show hyunae sigh blush with fast
        hs "...I guess sometimes, even the past sucked, too..."
    
    elif scrolled(1000):
        show hyunae baffled with fast
        hs "Aw..."
    
    jump log_loop

label log_5_5_hyunae:
    
    if scrolled(8, korean=7):
        show hyunae bittersob with fast
        hs "What...? Why...?!"
    
    elif scrolled(15, korean=12):
        show hyunae bitterscb with fast
    
    elif scrolled(24, korean=21):
        show hyunae hmmsob with fast
        hs "So... that really was the cause, then...? But if they knew back then, then why...?"
    
    elif scrolled(32, korean=28):
        show hyunae annoyedsob with fast
        hs "...oh."
    
    elif scrolled(39, korean=35):
        show hyunae surrender with fast
    
    elif scrolled(47, korean=44):
        show hyunae pressuresob with fast
        hs "Aaagh! That's so gross!"
    
    elif scrolled(65, korean=62):
        show hyunae bitterscb with fast
    
    elif scrolled(73, korean=70):
        show hyunae depressed blush with fast
        hs "...oh..."
    
    elif scrolled(81, korean=79):
        show hyunae distressed with fast
        hs "...well, I'd still be scared..."
    
    elif scrolled(95, korean=94):
        show hyunae sigh blush with fast
        hs "That's so nice of him! I'd really like to have someone like that..."
    
    elif scrolled(111, korean=111):
        if any_read("M4-6", "M4-7", "M4-8", "M4-9", "M6-1"):
            show hyunae grumpy with fast
            hs "...oh... because the Councillor of Engineering became someone in the Han family, I get it..."
        else:
            show hyunae annoyedsob with fast
            hs "...oh..."
    
    elif scrolled(119, korean=119):
        show hyunae depressed blush with fast
        hs "Oh..."
    
    elif scrolled(130, korean=129):
        show hyunae hopelessscb with fast
    
    elif scrolled(152, korean=151):
        show hyunae hopelesssob with fast
        hs "Wow, he's so understanding..."
    
    elif scrolled(164, korean=161):
        show hyunae lost with fast
        hs "She's so strong... I wish I was like her...!"
    
    elif scrolled(1000):
        show hyunae anxious with fast
    
    jump log_loop

label log_5_6_hyunae:
    
    if scrolled(8, korean=9):
        show hyunae pressuresob with fast
        hs "...oh no, does he really think that...?! That's awful!"
    
    elif scrolled(15, korean=16):
        show hyunae annoyedsob with fast
        hs "That's so harsh...!"
    
    elif scrolled(22, korean=23):
        show hyunae surrender with fast
        hs "...oh..."
    
    elif scrolled(27, korean=28):
        show hyunae bittersob with fast
        hs "...oh, geeze..."
    
    elif scrolled(35, korean=38):
        show hyunae sigh blush with fast
        hs "...oh, \"worthless as a wife\" was her words, not his... I see..."
    
    elif scrolled(46, korean=50):
        show hyunae sighsob with fast
        hs "I guess... it's hard even for her to be strong for so long..."
    
    elif scrolled(63, korean=69):
        show hyunae sighscb with fast
    
    elif scrolled(73, korean=78):
        show hyunae bittersob with fast
        hs "So even she worried about those things? Oh..."
    
    elif scrolled(98, korean=105):
        show hyunae hopelessscb with fast
    
    elif scrolled(106, korean=112):
        show hyunae hmmcob with fast
        hs "...well, he's trying, at least..."
    
    elif scrolled(115, korean=123):
        show hyunae depressed blush with fast
    
    elif scrolled(124, korean=132):
        show hyunae bitterscb with fast
    
    elif scrolled(138, korean=147):
        show hyunae annoyedsob with fast
        hs "\"Connecting people\"? Is it really? I never thought of it like that..."
    
    elif scrolled(146, korean=155):
        if read("M5-5"):
            show hyunae pressuresob with fast
            hs "...wait... is she re-enacting... aaaaagh, geeze, So-yi...!"
        else:
            show hyunae losssob with fast
            hs "...wow, this is intense..."
    
    elif scrolled(160, korean=168):
        if read("M5-5"):
            show hyunae sigh blush with fast
            hs "...oh... oh... wait, but... she never mentioned that..."
        else:
            show hyunae surrender blush with fast
            hs "...oh... oh..."
    
    elif scrolled(175, korean=184):
        show hyunae defensive with fast
        hs "...of course, you idiot husband!"
    
    elif scrolled(1000):
        show hyunae sad with fast
        hs "Ah... well, if he figured it out in the end... that's good! He really is a good man after all!"
    
    jump log_loop

label log_5_7_hyunae:
    
    if scrolled(4, korean=4):
        show hyunae staresob with fast
        hs "Ah! That's me! That's me, that's me! She's writing about me!"
    
    elif scrolled(12, korean=10):
        show hyunae pout with fast
        hs "Well... I guess that story sorta came true after all, huh..."
    
    elif scrolled(25, korean=21):
        show hyunae staresc with fast
    
    elif scrolled(31, korean=27):
        show hyunae satisfied blush with fast
        hs "\"Earthborn brilliance\"? Finally, someone who acknowledges that my real parents were smarter than people later on were!"
    
    elif scrolled(43, korean=39):
        show hyunae sweetso with fast
        hs "...huh... that's a good idea..."
    
    elif scrolled(52, korean=47):
        show hyunae annoyed blush with fast
        hs "See, she figured it out...! Why couldn't my adoptive father be as smart as her..."
    
    elif scrolled(59, korean=54):
        show hyunae bittersob with fast
        hs "...very unfounded..."
    
    elif scrolled(67, korean=62):
        show hyunae flustered with fast
        hs "I... I did...?!"
    
    elif scrolled(77, korean=71):
        show hyunae hmmsob with fast
        hs "I don't remember this at all...!"
    
    elif scrolled(88, korean=81):
        show hyunae hmph3 with fast
        hs "Ah... well, it was for a good cause, so I don't mind..."
    
    elif scrolled(94, korean=88):
        show hyunae depressed blush with fast
        hs "I guess things were tough for everyone, huh..."
    
    elif scrolled(1000):
        show hyunae shame with fast
        hs "She says that, but... in the end, the future refused to improve..."
    
    jump log_loop

label log_5_8_hyunae:
    
    if scrolled(6, korean=5):
        show hyunae hmmsob with fast
        hs "Oh, that's bad..."
    
    elif scrolled(15, korean=14):
        show hyunae annoyedsob with fast
        hs "...harsh..."
    
    elif scrolled(23, korean=22):
        show hyunae bittersob with fast
        hs "...why would people be afraid to talk to her? I don't understand..."
    
    elif scrolled(32, korean=30):
        show hyunae emo2 with fast
    
    elif scrolled(38, korean=36):
        show hyunae flustered3 with fast
        hs "So she was right...!"
    
    elif scrolled(1000):
        show hyunae anxious with fast
    
    jump log_loop

label log_5_9_hyunae:
    
    if scrolled(8, korean=6):
        show hyunae hmmscb with fast 
        hs "Huh..."
    
    elif scrolled(17, korean=14):
        show hyunae sigh blush with fast
        hs "...I guess her optimism was wrong, though... still..."
    
    elif scrolled(25, korean=22):
        show hyunae bitterscb with fast
        hs "...oh..."
    
    elif scrolled(33, korean=30):
        show hyunae bittersob with fast
        hs "Why are they fighting? I thought he was good for her..."
    
    elif scrolled(44, korean=40):
        show hyunae hopelessscb with fast
    
    elif scrolled(52, korean=48):
        show hyunae losssob with fast
        hs "...that's so harsh..."
    
    elif scrolled(58, korean=54):
        show hyunae depressed blush with fast
    
    elif scrolled(74, korean=71):
        show hyunae lossscb with fast
    
    elif scrolled(97, korean=96):
        show hyunae sighscb with fast
    
    elif scrolled(103, korean=102):
        show hyunae hopelesssob with fast
        hs "Oh... so he was just... I see..."
    
    elif scrolled(111, korean=110):
        show hyunae sigh blush with fast
        hs "...I'm so glad!"
    
    elif scrolled(119, korean=118):
        show hyunae surrender blush with fast
        hs "It's so nice that they agreed on these things together...! He's so nice..."
    
    elif scrolled(127, korean=127):
        show hyunae sighsob with fast
        hs "Oh, So-yi..."
    
    elif scrolled(139, korean=139):
        show hyunae emo with fast
        hs "Wait, but that date is right before...! ...oh, I get it..."
        # I think she needs to know about the computer destruction first, which comes way later - Raide
    
    elif scrolled(143, korean=143):
        show hyunae shame with fast
        hs "...well... at least she had such a sweet husband at her side..."
    
    elif scrolled(1000):
        show hyunae tired with fast
    
    jump log_loop

label log_6_1_hyunae:
    
    if scrolled(3, korean=4):
        show hyunae hmmsob with fast
        hs "Geeze, she's scary..."
    
    elif scrolled(11, korean=11):
        show hyunae hmmcob with fast
        hs "...huh... that's all because of \"Meritocracy\"...?"
    
    elif scrolled(22, korean=22):
        show hyunae annoyedsc with fast
    
    elif scrolled(30, korean=30):
        show hyunae surrender blush with fast
        hs "...I see..."
    
    elif scrolled(37, korean=38):
        show hyunae bittersc with fast
    
    elif scrolled(46, korean=47):
        if any_read("M4-6", "M4-7", "M4-8", "M4-9"):
            show hyunae hardsob with fast
            hs "Harsh, but... I guess with how hostile Council was, I understand..."
        else:
            show hyunae hardsc with fast
    
    elif scrolled(55, korean=56):
        show hyunae bittersc with fast
        hs "...huh..."
    
    elif scrolled(64, korean=67):
        show hyunae sigh with fast
        hs "I wonder..."
    
    elif scrolled(1000):
        show hyunae disappoint with fast
    
    jump log_loop

label log_6_2_hyunae:
    
    if scrolled(12, korean=13):
        show hyunae bittersob with fast
        hs "Oh no...!"
    
    elif scrolled(18, korean=20):
        show hyunae grumpy with fast
        hs "...geeze..."
    
    elif scrolled(27, korean=29):
        show hyunae pressuresob with fast
        hs "...I think he really deserves all that harshness from *Mute, geeze..."
    
    elif scrolled(41, korean=44):
        show hyunae losssc with fast
    
    elif scrolled(53, korean=56):
        show hyunae depressed blush with fast
    
    elif scrolled(75, korean=80):
        show hyunae weak2 with fast
        hs "...oh..."
    
    elif scrolled(83, korean=88):
        show hyunae defensive with fast
        hs "...that's an awful thing to say...!"
    
    elif scrolled(95, korean=100):
        show hyunae oops with fast
    
    elif scrolled(106, korean=111):
        show hyunae bitterscb with fast
    
    elif scrolled(114, korean=120):
        show hyunae emo with fast
        hs "...scary, but..."
    
    elif scrolled(127, korean=134):
        show hyunae sigh blush with fast
        hs "...wow..."
    
    elif scrolled(145, korean=153):
        show hyunae sighsob with fast
        hs "That's really strong of her, though... I wouldn't have been able to do that..."
    
    elif scrolled(157, korean=165):
        show hyunae hmmsob with fast
        hs "Wait, her husband wasn't the most important? Then who...?"
    
    elif scrolled(170, korean=181):
        show hyunae hopelesssob with fast
        hs "...I don't really get what she's saying about their relationship, but..."
    
    elif scrolled(180, korean=192):
        show hyunae hmmcob with fast
        hs "Perfect? Her? As if!"
    
    elif scrolled(190, korean=202):
        show hyunae losssob with fast
        hs "...oh geeze, that's tragic, though..."
    
    elif scrolled(204, korean=217):
        show hyunae surrender blush with fast
        hs "...huh..."
    
    elif scrolled(215, korean=229):
        show hyunae hmmsob with fast
        hs "Wait, is she saying...? Even at that time, men did things like that with...?"
    
    elif scrolled(236, korean=251):
        show hyunae hardsob with fast
        hs "...oh, geeze, though..."
    
    elif scrolled(251, korean=267):
        show hyunae sighsob with fast
        hs "...oh..."
    
    elif scrolled(267, korean=285):
        show hyunae sighscb with fast
    
    elif scrolled(277, korean=296):
        show hyunae annoyedscb with fast
    
    elif scrolled(284, korean=300):
        show hyunae sigh blush with fast
        hs "Wow, that's... kind of cool of *Mute, actually..."
    
    elif scrolled(1000):
        show hyunae hmmccb with fast
        hs "Aw, geeze..."
    
    jump log_loop

label log_6_3_hyunae:
    
    if scrolled(7, korean=8):
        if any_read("M1-1", "M1-6", "M1-7", "M6-3") and any_read("M1-1", "M1-3", "M1-6", "M6-2"):
            show hyunae hmmsob with fast
            hs "Ah, so this is about Seo-yeong's husband..."
        else:
            show hyunae hmmsc with fast
            hs "Hm..."
    
    elif scrolled(17, korean=19):
        show hyunae explain4 with fast
        hs "I guess he felt strongly about Chinese characters being stupid, huh..."
    
    elif scrolled(25, korean=27):
        show hyunae annoyedsc with fast
        hs "Hm..."
    
    elif scrolled(39, korean=42):
        show hyunae hardsc with fast
    
    elif scrolled(51, korean=53):
        show hyunae bitterso with fast
        hs "...well, that's nice, I guess..."
    
    elif scrolled(60, korean=63):
        show hyunae huhsc with fast
        hs "...huh..."
    
    elif scrolled(70, korean=74):
        show hyunae hmmsc with fast
    
    elif scrolled(1000):
        show hyunae tired with fast
    
    jump log_loop

label log_6_4_hyunae:
    
    if scrolled(6, korean=4) and any_read("M2-2", "M2-3") and not any_read("M6-7", "M6-8"):
        show hyunae hmmsob with fast
        hs "...so they never found out who killed Professor Kim, after all...?"
    
    elif scrolled(13, korean=9):
        show hyunae surrender with fast
        hs "...huh..."
    
    elif scrolled(21, korean=17):
        show hyunae grumpy with fast
        if any_read("M6-6", "M6-8"):
            hs "Oh, geeze, this must be..."
        else:
            hs "...what's going on, though...?"
    
    elif scrolled(41, korean=38):
        show hyunae sighscb with fast
    
    elif scrolled(49, korean=50):
        show hyunae bittersob with fast
        hs "This sounds really serious..."
    
    elif scrolled(61, korean=59):
        show hyunae bitterscb with fast
    
    elif scrolled(80, korean=77):
        show hyunae pressurescb with fast
    
    elif scrolled(88, korean=85):
        show hyunae pout with fast
        hs "...geeze, this is intense..."
    
    elif scrolled(97, korean=94):
        show hyunae bitterscb with fast
    
    elif scrolled(113, korean=110):
        show hyunae annoyedscb with fast
    
    elif scrolled(121, korean=117):
        show hyunae grumpy with fast
        hs "Really? They were going to arrest the President?"
    
    elif scrolled(129, korean=126) and any_read("M1-2", "M1-4", "M4-2", "M4-9"):
        show hyunae huhso with fast
        hs "...I thought *Mute didn't like the President, though... why are they...?"
    
    elif scrolled(137, korean=134):
        show hyunae hmmsob with fast
        hs "...huh, I don't get it, but..."
    
    elif scrolled(149, korean=146):
        show hyunae hmmsc with fast
    
    elif scrolled(162, korean=160):
        show hyunae sigh with fast
    
    elif scrolled(174, korean=172):
        show hyunae lossso with fast
        hs "...wow, intense..."
    
    elif scrolled(182, korean=180):
        show hyunae hardsob with fast
        hs "She's... a really tough person, isn't she...?"
    
    elif scrolled(208, korean=208):
        show hyunae sighsc with fast
    
    elif scrolled(232, korean=233):
        show hyunae hopelesssc with fast
    
    elif scrolled(1000):
        show hyunae troubled2 with fast
        hs "...I guess it's hard to be tough, huh..."
    
    jump log_loop

label log_6_5_hyunae:
    
    if scrolled(12, korean=13):
        if any_read("M1-2", "M1-4", "M3-1"):
            show hyunae annoyedsob with fast
            hs "...wow, they actually predicted that one completely right."
        else:
            show hyunae bitterso with fast
            hs "Wait... but the first emperor was named Ryu! Could it be...?"
        
    elif scrolled(23, korean=24):
        show hyunae bittersc with fast
        hs "...huh..."
    
    elif scrolled(34, korean=35):
        show hyunae huhsc with fast
    
    elif scrolled(44, korean=46):
        show hyunae hopeless2 with fast
        hs "...you know, I always wondered what happened to the navigation AI..."
    
    elif scrolled(52, korean=54):
        show hyunae losssob with fast
        hs "...wow, this atmosphere is..."
    
    elif scrolled(61, korean=63):
        show hyunae sigh blush with fast
        hs "...it's really melancholy."
    
    elif scrolled(74, korean=77):
        show hyunae sternsob with fast
        hs "Even they swore like that? Was that a thing women in the past did, too...?"
    
    elif scrolled(89, korean=93):
        show hyunae evasive with fast
        hs "...oh..."
    
    elif scrolled(104, korean=107):
        show hyunae huhsc with fast
        hs "..."
    
    elif scrolled(128, korean=131):
        show hyunae hmmscb with fast
    
    elif scrolled(141, korean=143):
        show hyunae hopelesssob with fast
        hs "...yeah, I guess it really is hard to be strong..."
    
    elif scrolled(151, korean=151):
        show hyunae sighsob with fast
        hs "Wow, this is..."
    
    elif scrolled(160, korean=161):
        show hyunae sigh blush with fast
        hs "Somehow, this atmosphere feels really intimate..."
    
    elif scrolled(172, korean=171):
        show hyunae hmmcob with fast
        hs "...I guess, sometimes, *Mute could be a nice person, huh..."
    
    elif scrolled(1000):
        show hyunae hmmscb with fast
    
    jump log_loop

label log_6_6_hyunae:
    
    if scrolled(7, korean=6):
        show hyunae hmph2 with fast
        hs "...huh, I wonder if that was the same house I was in, or...?"
    
    elif scrolled(15, korean=13):
        show hyunae hardsob with fast
        hs "Yeah... I know that feeling...!"
    
    elif scrolled(25, korean=23):
        show hyunae sigh blush with fast
        hs "...somehow, this sounds awfully familiar..."
    
    elif scrolled(33, korean=31):
        show hyunae annoyedsob with fast
        hs "Wait, if she doesn't have a little sister, then who does she mean...?"
    
    elif scrolled(44, korean=42):
        show hyunae hmphsc with fast
    
    elif scrolled(52, korean=50):
        show hyunae hardscb with fast
        hs "...huh..."
    
    elif scrolled(57, korean=54):
        show hyunae bitterscb with fast
    
    elif scrolled(1000):
        if read("M1-5"):
            show hyunae unsure with fast
            hs "I think I liked the report with the potted plant thing better... this is awfully... well..."
        else:
            show hyunae unsure with fast
            hs "This is awfully... well..."
        
    jump log_loop

label log_6_7_hyunae:
    
    if scrolled(13, korean=10):
        if any_read("M4-*") or read("M6-1"):
            show hyunae hmmsob with fast
            hs "Wow... even more hostile than it was before...?"
            # Need a conditional when the log is read for the first time - Raide
        else:
            show hyunae hardsob with fast
            hs "Wow, that's rough..."

    elif scrolled(27, korean=24):
        show hyunae hopelesssob with fast
        hs "I guess she must've felt powerless, huh...?"
    
    elif scrolled(47, korean=43):
        show hyunae huhscb with fast
        hs "Hm..."
    
    elif scrolled(60, korean=54):
        show hyunae hmphsc with fast
    
    elif scrolled(74, korean=68):
        show hyunae evasive with fast
        hs "Oh...?"
    
    elif scrolled(94, korean=89):
        show hyunae huhscb with fast
        hs "...huh..."
    
    elif scrolled(112, korean=116):
        show hyunae hmmccb with fast
    
    elif scrolled(127, korean=123):
        show hyunae hmphsc with fast
    
    elif scrolled(139, korean=136):
        show hyunae huhsc with fast
    
    elif scrolled(156, korean=154):
        show hyunae hmmsob with fast
        hs "Oh... I guess even back then, she didn't do that..."
    
    elif scrolled(170, korean=167):
        show hyunae huhscb with fast
        hs "...huh..."
    
    elif scrolled(178, korean=174):
        show hyunae grumpy with fast
        hs "What is she...?"
    
    elif scrolled(189, korean=185):
        show hyunae annoyedsc with fast
    
    elif scrolled(198, korean=196):
        show hyunae hopelessso with fast
        hs "...this is a lot more gentle than I was expecting from her..."
    
    elif scrolled(218, korean=216):
        show hyunae hmmscb with fast
    
    elif scrolled(1000):
        show hyunae bittersob with fast
        hs "What? Who? Was it...?!"
    
    jump log_loop

label log_6_8_hyunae:
    
    if scrolled(6, korean=9):
        if read("M1-2"):
            show hyunae hmphso with fast
            hs "Huh... this has a different feeling than that other log with him..."
        else:
            show hyunae hmphsc with fast
            hs "Hm..."
    
    elif scrolled(17, korean=24) and read("M1-2"):
        show hyunae hardsob with fast
        hs "Whoa... a really different feeling!"
    
    elif scrolled(26, korean=33):
        show hyunae hmmsob with fast
        hs "...harsh..."
    
    elif scrolled(46, korean=54):
        show hyunae bitterscb with fast
    
    elif scrolled(68, korean=80):
        show hyunae hopelessscb with fast
    
    elif scrolled(80, korean=92):
        show hyunae hmph2 with fast
        hs "...huh, she can be a smooth talker, though..."
    
    elif scrolled(88, korean=101):
        show hyunae flustered with fast
        hs "Whoa! Her? A rebellion...? *Mute?!"
    
    elif scrolled(100, korean=111):
        show hyunae grumpy with fast
        hs "...geeze, this is..."
    
    elif scrolled(116, korean=129):
        show hyunae hopelesssob with fast
        hs "...she really idolized her, huh..."
    
    elif scrolled(141, korean=153):
        show hyunae hmmscb with fast
    
    elif scrolled(158, korean=172):
        show hyunae huhsc with fast
        hs "...huh..."
    
    elif scrolled(165, korean=181):
        show hyunae sighscb with fast
    
    elif scrolled(181, korean=195):
        show hyunae bittersob with fast
        hs "...*Mute... she really wanted to prevent that...?"
    
    elif scrolled(1000):
        show hyunae troubled2 with fast
        hs "I... I think I understand what she saw in *Mute, now..."
    
    jump log_loop

label log_6_9_hyunae:
    if get_m("M6-9").encrypted:
        show hyunae busy with fast
        hs "Aaaaa, geeze, I haven't found the right key yet... I'll let you know when I do, I promise! I really want to see what this is..."

    elif scrolled(4, korean=3):
        show hyunae grumpy with fast
        hs "Oh no...! So that's what this all was? A message...?"
    
    elif scrolled(12, korean=11):
        show hyunae hmmsob with fast
        hs "...even *Mute could be scared?"
    
    elif scrolled(28, korean=26):
        show hyunae hmmsc with fast
    
    elif scrolled(36, korean=33):
        show hyunae hmphsc with fast
        hs "...huh..."
    
    elif scrolled(44, korean=38):
        show hyunae hmph2 with fast
        hs "...that must've been scary for the maid, though..."
    
    elif scrolled(55, korean=50):
        show hyunae hardscb with fast
    
    elif scrolled(64, korean=60):
        show hyunae hmmscb with fast
        hs "..."
    
    elif scrolled(79, korean=76):
        show hyunae huhscb with fast
        hs "Huh...?"
    
    elif scrolled(87, korean=84):
        show hyunae annoyedsob with fast
        hs "...oh, geeze..."
    
    elif scrolled(96, korean=95):
        show hyunae bitterscb with fast
    
    elif scrolled(108, korean=106):
        show hyunae pout with fast
        hs "This feels like it's really off..."
    
    elif scrolled(119, korean=116):
        show hyunae staresob with fast
        hs "Whoa!"
    
    elif scrolled(133, korean=128):
        show hyunae hmmsob with fast
        hs "...an explosion on the plaza?! Wow... that's... really serious..."
    
    elif scrolled(139, korean=136):
        show hyunae pressuresob with fast
        hs "He didn't...!"
    
    elif scrolled(147, korean=144):
        show hyunae surrender blush with fast
        hs "...oh, no..."
    
    elif scrolled(170, korean=168):
        show hyunae hardscb with fast
    
    elif scrolled(179, korean=176):
        show hyunae grumpy with fast
        hs "...that's so cold..."
    
    elif scrolled(188, korean=185):
        show hyunae weak2 with fast
        hs "...oh..."
    
    elif scrolled(202, korean=198):
        show hyunae losssc with fast
    
    elif scrolled(215, korean=211):
        show hyunae sighsob with fast
        hs "...I... know exactly how she must have been feeling... oh no, *Mute..."
    
    elif scrolled(228, korean=224):
        show hyunae losssob with fast
    
    elif scrolled(238, korean=235):
        show hyunae sigh blush with fast
    
    elif scrolled(255, korean=251):
        show hyunae sighscb with fast
    
    elif scrolled(268, korean=265):
        show hyunae bitterscb with fast
    
    elif scrolled(274, korean=275):
        show hyunae hopelessscb with fast
    
    elif scrolled(291, korean=290):
        show hyunae hmmsob with fast
        hs "She..."
    
    elif scrolled(303, korean=303):
        show hyunae sighsob with fast
        hs "...I don't..."
    
    elif scrolled(325, korean=326):
        show hyunae pressurescb with fast
    
    elif scrolled(345, korean=346):
        show hyunae grumpy with fast
        hs "So... the reason the ship was the way it was in my time, was because...?"
    
    elif scrolled(356, korean=359):
        show hyunae lost with fast
        hs "...this is so hard to read..."
    
    elif scrolled(371, korean=375):
        show hyunae troubled with fast
    
    elif scrolled(379, korean=384):
        show hyunae pressuresob with fast
        hs "So... that's how she was... that's so cruel!"
    
    elif scrolled(390, korean=395):
        show hyunae emo with fast
        hs "...oh..."
    
    elif scrolled(401, korean=406):
        show hyunae surrender blush with fast
        hs "..."
    
    elif scrolled(410, korean=415):
        show hyunae losssob with fast
        hs "...it wasn't even...?!"
    
    elif scrolled(420, korean=425):
        show hyunae distressed with fast
        hs "...I didn't like her, but... reading about her broken like this is... is..."
    
    elif scrolled(430, korean=435):
        show hyunae sighsob with fast
        hs "...no..."
    
    elif scrolled(441, korean=446):
        show hyunae losssob with fast
        hs "...no, no, no..."
    
    elif scrolled(454, korean=458):
        show hyunae sad3 with fast
        hs "...so that's how it happened..."
    
    elif scrolled(1000):
        show hyunae guilt with fast
        hs "*Mute, I... I... I didn't know..."
    
    jump log_loop
