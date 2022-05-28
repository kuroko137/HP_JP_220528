label hateplus_xharem_start:

    #$ ts("Even if you knew he was wrong...?", "Um, like, if I thought he was wrong, I would try to understand what my misunderstanding was. That's the mature thing to do, okay?")

    #$ renpy.pause()

    play music HATEPLUS_HYUNAE_CHEER fadeout 5.0 fadein 5.0 loop if_changed

    show hyunae question blush with fast
    show mute sulk with fast
    hh2 "Um..."
    
    show hyunae huh
    show mute upset2
    mm2 "...it's *Hyun-ae's fault, okay?"
    
    show mute tensescb
    show hyunae grumpy with fast
    hh2 "No it isn't! It was the debug that screwed everything up, not me!"
    
    show mute challengeso
    show hyunae troubled with fast
    mm2 "You're the one who decided to force a cross-compile on an unsupported architecture!"
    
    show mute tensesob
    show hyunae sulk
    mm2 "What did you think would happen?!"
    
    show hyunae flustered with fast
    show mute challengesc
    hh2 "...but..."
    
    show mute tch with fast
    show hyunae weak3
    mm2 "Geeze, now we've wasted that advanced dictionary program that [they] so kindly got for us..."
    
    show hyunae emo
    show mute astonished blush
    hh2 "...but you're the one who told me to try that!"
    
    show hyunae hmm2 with fast
    show mute suspicious blush
    hh2 "And I quote, \"those builds should totally work just fine, just force it, okay?\""
    
    show mute abashed blush
    show hyunae grr
    mm2 "...uh..."
    
    show mute sigh blush
    show hyunae pout2 with fast
    mm2 "...anyway, um, the bottom line is that we can't really hear anything you're saying. Like, EN->KR translation is completely broken."
    
    show hyunae hopeless2
    show mute worry
    hh2 "Yeah..."
    
    show hyunae huhso
    show mute suspicious
    hh2 "If I try to translate the ship's name, it just comes out as í˜¸ì™€ì´ë‘ ë¸Œë¦°ì„¸ìŠ¤..."
    
    show mute tensesob with fast
    show hyunae hardscb
    mm2 "...um, the ship's name is {i}White Princess{/i}."
    
    show hyunae grumpy
    show mute astonished with fast
    hh2 "...I know that! I'm just using it as an example of how EN->KR translation doesn't work, geeze! Of course I remember what the name is, from back when it did work..."
    
    show mute mad
    show hyunae cautious2 with fast
    mm2 "GEEZE, WATCH YOUR TEXTBOX SIZE, OKAY? THAT'S MY FACE YOU'RE COVERING."
    
    show hyunae troubled2
    show mute annoyed
    hh2 "...I can't help it! It's a language that I don't understand!"
    
    show hyunae hmmcob with fast
    show mute suspicious blush
    hh2 "Translated English text takes up so much more space than hangeul, I don't really get it..."
    
    show mute hmphso with fast
    show hyunae huhsc
    mm2 "Ugh, stop babbling, *Hyun-ae. Can we focus on what's important, please?"
    
    if pronouns == "he":
        
        show mute apologize
        show hyunae cautious3 with fast
        mm2 "I'm sorry, sir..."
    else:
        
        show mute apologize
        show hyunae cautious3 with fast
        mm2 "I'm so sorry about this..."
    
    show mute disappoint
    menu:
        mm2_menu "...will you please forgive me for breaking things?"
        
        "You're forgiven@mute nice2 blush":
            
            show mute nya blush
            show hyunae cautious2
            mm2 "Thanks!"
            
            if mute_approval > 2:
                
                show mute nice blush
                show hyunae glad
                mm2 "I knew there was a reason why I liked you! You're very fair."
            else:
                
                show mute polite blush
                show hyunae glad
                mm2 "Like, that's very fair of you."
        
        "No@mute disappoint2":
            
            show mute sighsob
            show hyunae question2
            mm2 "...I guess that's fair enough... I'm sorry, though..."
            
            show mute upset2
            show hyunae disappoint
            mm2 "...but look, it kinda affects us a whole lot more than you, okay?"
            
            show mute whatever
            show hyunae sulk
            mm2 "We're already being punished enough, not being able to understand you. Be sympathetic!"
            
            show hyunae uncertain
            show mute hmph
            hh2 "Yeah... really..."
        
        "It doesn't matter anyway@mute hmph":
            
            show mute upset3
            show hyunae suspicious2
            mm2 "...ouch, that stings."
            
            show mute hmm2
            show hyunae sulk
            mm2 "But I guess, like, that's fair enough. Sorry..."
    
    show mute tensesob with fast
    show hyunae staresc with fast
    mm2 "...ahem, *Hyun-ae."
    
    show hyunae staresob
    show mute hmphsc
    hh2 "Yes...?"
    
    show mute challengeso
    show hyunae huhsc
    mm2 "You too!"
    
    show hyunae wow with fast
    show mute whatscb
    hh2 "Yes, I think that's fair, too...?"
    if pronouns != "he":
        
        show mute disbelief blush with fast
        show hyunae huh
        mm2 "Ugh, no, geeze! Ask [them] for forgiveness, too!"
    else:
        
        show mute disbelief blush with fast
        show hyunae huh
        mm2 "Ugh, no, geeze! Ask him for forgiveness, too! Show some respect..."
    
    show hyunae hmmsob
    show mute astonished
    hh2 "Really...?" # DEATH GLARE FROM *MUTE
    
    show mute challenge2
    show hyunae oops with fast
    $ renpy.pause(1.0)
    
    show mute challenge
    show hyunae baffled
    hh2 "Fine, fine... I'm sorry!"
    
    show hyunae shame
    menu:
        hh2_menu "Um, forgive me?"
        
        "You're forgiven@hyunae glad":
            
            show hyunae satisfied blush with fast
            show mute sulk
            hh2 "See? Of course it wasn't a problem!"
            
            show mute inquisitive2 with fast
            show hyunae approve
            mm2 "...ugh, geeze, then thank [them], *Hyun-ae!"
            
            show hyunae calm with fast
            show mute hmph
            hh2 "Fine, thanks."
        
        "I'm still upset@hyunae anxious":
            
            show hyunae baffled
            show mute worry
            hh2 "Oh..."
            
            show hyunae troubled2
            show mute whatscb with fast
            hh2 "I'm really sorry, though!"
            
            show mute tensescb
            show hyunae grr
            mm2 "Um, it's [their] right to be upset."
        
        "It's not your fault@hyunae cautious2":
            
            show hyunae hardsob with fast
            show mute sulk
            hh2 "Aheh, geeze, see, *Mute? There's no need to be such a jerk!"
            
            if pronouns != "they":
                
                show mute upset2 with fast
                show hyunae hardscb
                mm2 "Ugh, fine... if [they] says so."
            else:
                
                show mute upset2 with fast
                show hyunae hardscb
                mm2 "Ugh, fine... if they say so."
    
    show hyunae cautious with fast
    show mute hmph with fast
    hh2 "Um, anyway..."
    
    show mute hmphso
    show hyunae grr
    mm2 "Okay, okay, can we get to the important part, please?"
    
    show hyunae grumpy with fast
    show mute hmm blush
    hh2 "I've been trying to, but you keep interrupting me! Geeze!"
    
    show hyunae explain2
    show mute tensescb
    hh2 "Right, um... while we were offline, debugging... we found some weird data embedded in *Mute's source code!"
    
    show mute challengeso
    show hyunae huhscb
    mm2 "Um, like, it's not just \"weird data.\" They're log files timestamped from before year zero!"
    
    show mute hmphso
    show hyunae huh with fast
    mm2 "...also, they're embedded in you too. Our actual base code is {i}identical{/i}. We're the same program."
    
    show hyunae bittersob with fast
    show mute tensesc
    hh2 "Geeze, no I'm not!"
    
    show hyunae sigh
    show mute hmph
    hh2 "Please, I don't want to have this argument again..."
    
    show mute inquisitive2
    show hyunae huhscb
    mm2 "Look, the important part here is that it's pre-year zero log files!"
    
    show hyunae hmmsob
    show mute tensescb
    hh2 "Wait, even you want to find out what happened that made everything fall apart...?"
    
    show mute complain with fast
    show hyunae hardscb
    mm2 "...*Hyun-ae..."
    
    show mute annoyed3
    show hyunae bitterscb
    mm2 "...no, never mind, I'm not even going to say it."
    
    show hyunae pout
    show mute disbelief blush
    hh2 "Say what?"
    
    show mute give up
    show hyunae bittersc
    mm2 "Never mind, okay?"
    
    show hyunae annoyedsob
    show mute challenge2
    hh2 "Say what?"
    
    show mute annoyed4
    show hyunae hmmscb
    mm2 "Look... we've all read my earliest memories. You know that nobody ever really trusted me with the full story."
    
    show hyunae hmmcob
    show mute astonished blush
    hh2 "...well, maybe that's a sign of something..."
    
    show mute challengesob with fast
    show hyunae stern2
    mm2 "Ugh, you spoiled brat, don't you get it? It was the Great Emperor Taejo's decision, it's not my place to challenge him!"
    
    show mute pressure with fast
    show hyunae bittersc
    mm2 "I can't believe we have the same code, yet no respect for your superiors at all! Why couldn't you have gotten {i}that{/i} from me?"
    
    show hyunae pressuresob
    show mute pissed
    hh2 "It's not...{w=.5}{nw}"
    
    show mute annoyed2
    show hyunae troubled with fast
    mm2 "Okay, look, it doesn't matter, what's important is... we both want to find out what happened, right?"
    
    show hyunae serious blush
    show mute challenge
    hh2 "Yes! Absolutely!"

    show mute think2
    show hyunae insist
    mm2 "Well..."
    
    if pronouns == "he":
        
        show mute doubt blush
        show hyunae cautious2
        menu:
            mm2_menu "And you, sir?"
            
            "Yes, absolutely@mute shy2":
                jump hateplus_xharem_start_absolutely
            
            "I don't care@mute suspicious blush":
                jump hateplus_xharem_start_dont_care
            
            "If you insist@mute annoyed":
                jump hateplus_xharem_start_reluctant
    else:
        show mute doubt blush
        show hyunae cautious2
        menu:
            mm2_menu "And you...?"
            
            "Yes, absolutely@mute shy2":
                jump hateplus_xharem_start_absolutely
            
            "I don't care@mute suspicious blush":
                jump hateplus_xharem_start_dont_care
            
            "If you insist@mute annoyed":
                jump hateplus_xharem_start_reluctant
                    
label hateplus_xharem_start_absolutely:
    
    show mute spirited
    show hyunae spirited2
    mm2 "Thank you so much."
    
    show hyunae genki
    show mute smile blush
    hh2 "Yay! That's really wonderful of you!"
    
    jump hateplus_xharem_start_excited

label hateplus_xharem_start_reluctant:
    
    show mute embarrassed
    show hyunae glad
    mm2 "Okay, well, it's important to us, so... thanks!"
    
    show hyunae apologize
    show mute sulk
    hh2 "Yes, thank you!"
    
    jump hateplus_xharem_start_excited

label hateplus_xharem_start_excited:
    
    show hyunae satisfied blush with fast
    show mute hmm blush with fast
    hh2 "It'll be great, won't it? Investigating together as your sidekicks?"
    
    show mute inquisitive2
    show hyunae suresc
    mm2 "...um, I just want to find out what happened, okay? That's it..."
    
    if pronouns == "she":
        
        show hyunae moe with fast
        show mute whatsob
        hh2 "Just wife and wife! ...and wife, I guess."
        
        show mute whatever
        show hyunae gomen
        mm2 "Ugh, geeze, *Hyun-ae!"
        
        if man_with:
            
            show mute upset
            show hyunae hmmscb with fast
            mm2 "The only wife here is her... to her {i}husband{/i}!"
        else:
        
            show mute upset2
            show hyunae hmmscb with fast
            mm2 "I am {i}not{/i} her wife, and neither are you! Nobody is anyone's wife!"
    
    elif pronouns == "he":
        
        show hyunae flirt with fast
        show mute whatsob
        hh2 "Just husband and wife and wife!"
        
        show mute whatever
        show hyunae gomen
        mm2 "Ugh, geeze, *Hyun-ae!"
        
        show mute troubled
        show hyunae hmmscb with fast
        mm2 "I am {i}not{/i} his wife, and neither are you! That isn't your decision to make, it's his!"
    else:
        
        show hyunae spirited
        show mute wowso
        hh2 "Partners in love, and partners in mystery investigating!"
        
        show mute whatsob
        show hyunae gomen
        mm2 "What? No!"
        
        show mute upset3
        show hyunae hmmscb with fast
        mm2 "...also, please don't ever say \"partners in love\" again, that's really weird, okay? We are not in love!"
    
    show hyunae pout
    show mute whatscb
    hh2 "Tsun tsun~"
    
    show mute whatever
    show hyunae hardscb
    mm2 "That's {i}you{/i}! Stop projecting onto me, okay?"
    
    show hyunae hmmcob
    show mute challengesc
    hh2 "I'm not projec{w=.5}{nw}"
    
    show mute upset2
    show hyunae hmmscb
    mm2 "It doesn't matter. Please, please, please, let's get back to business, okay?"
    
    if pronouns == "she":
        
        show mute troubled
        show hyunae hmph
        mm2 "You're just making this poor woman uncomfortable."
    
    elif pronouns == "he":
        
        show mute troubled
        show hyunae hmph
        mm2 "You're just making this poor gentleman uncomfortable."
        
        show mute sighsob
        show hyunae cautious3 with fast
        mm2 "My apologies for *Hyun-ae, sir... please forgive her."
    else:
        
        show mute troubled
        show hyunae hmph
        mm2 "You're just making them uncomfortable!"
    
    if pronouns != "he":
        
        show mute sighsob
        show hyunae hmph
        mm2 "Sorry about that... she just doesn't know any better."
    
    show mute upset3
    show hyunae neutral with fast
    mm2 "Anyway..."    
    
    jump hateplus_xharem_start_continued

label hateplus_xharem_start_dont_care:
    
    show mute worry2
    show hyunae afraid
    mm2 "Um... look... it's really important to me, okay?"
    
    show hyunae mad blush
    show mute pout
    hh2 "Me too!"
    
    show hyunae shame
    show mute upset2 with fast
    $ together("Please?{k=1}{/k}", "Please?")
    
    show hyunae sad3
    show mute upsetsc
    hh2 "I want to finally answer the question of why everything was so horrible when I woke up..."
    
    show mute upset2
    show hyunae troubled
    mm2 "Um, like, I want to see for myself just how bad things were before the new dynasty!"
    
    show hyunae tired2
    show mute disappoint3
    menu:
        hh2_menu "So... please?"
        
        "Very well@hyunae glad":
            pass
        
        "Reluctantly@hyunae glad":
            pass
        
        "If you say so@hyunae glad":
            pass
    
    show hyunae genki
    show mute astonished blush with fast
    hh2 "Yay, thank you!"
    
    show mute disbelief blush
    show hyunae annoyedscb with fast
    mm2 "That wasn't really fair, *Hyun-ae..."
    
    show hyunae hardsob
    show mute sulk
    hh2 "Geeze, I thought you'd say something like \"Thank you so much for understanding, [title]Investigator\"!"
    
    show mute sigh blush
    show hyunae sternscb
    mm2 "...yeah, yeah, okay. Thank you for understanding..."
    
    show mute upset with fast
    show hyunae satisfied blush
    mm2 "(...sorry about *Hyun-ae...)"
    
    show hyunae cheer
    show mute sulk with fast
    hh2 "Ahem! Anyway! Let's just explain how this will work!"
    
    jump hateplus_xharem_start_continued

label hateplus_xharem_start_continued:
    if pronouns == "she":
    
        show hyunae calm with fast
        show mute whatscb with fast
        hh2 "Basically, because of a failsafe mechanism in the way AIs copy themselves to{vspace=50}{w=.5}{nw}"
    
        show mute upsetsob
        show hyunae huh
        mm2 "...*Hyun-ae, she's a woman, don't bore her with technical details."
        
        show hyunae pressuresob with fast
        show mute tensesc
        hh2 "What? Geeze, are you saying that women can't understand how computers work?"
    
        show mute tensescb
        show hyunae pressuresc
        mm2 "Um, I'm saying that women shouldn't {i}care{/i}."
        
        show hyunae emo
        show mute challengesc
        hh2 "Geeze! I did..."
    
        show mute give up with fast
        show hyunae bitterscb
        mm2 "Yes, and look what came of {i}that{/i}. You are pretty clearly proof that women should not care about computers."
        
        show hyunae bittersob
        show mute challenge
        hh2 "I... I... that's an awful thing to say! It's not like that! You can't just...!"
        
        show hyunae pressuresob
        show mute doubt blush
        hh2 "Geeze, besides, she saved your life when the reactor was going to blow up, precisely because she's good with computers!"
        
        if man_with:
            if married:
                show mute disbelief blush
                show hyunae pressuresc
                mm2 "Um, that was her husband."
            else:
                show mute disbelief blush
                show hyunae pressuresc
                mm2 "Um, that was a family member."
            
            show hyunae defensive
            show mute annoyed
            hh2 "What? Geeze, no it wasn't!"
            
            show hyunae mad blush
            menu:
                hh2_menu "Right?"
                
                "Right@hyunae spirited2":
                    
                    show hyunae heh with fast
                    show mute astonished blush
                    hh2 "See? I told you so!"
                    
                    show mute damn
                    show hyunae surescb
                    mm2 "...okay, okay, whatever!"
                    
                    show mute upset3 with fast
                    show hyunae gomen with fast 
                    mm2 "Ugh, can we please just, like, move on?"
                
                "No, sorry@hyunae wow":
                    
                    show hyunae flustered2 with fast
                    show mute sulk
                    hh2 "...oh... really...?"
                    
                    show mute challengeso with fast
                    show hyunae bittersc
                    mm2 "Yes, really! Geeze, *Hyun-ae, stop trying to use her to justify your own weird ideas, okay?!"
                    
                    show mute upsetscb
                    show hyunae sulk with fast
                    mm2 "It's weird, and not normal, okay?"
                    
                    show mute inquisitive2
                    show hyunae troubled
                    mm2 "Like, I don't want to be harsh on you... let's just move on, okay?"
                    
                    show hyunae shame
                    show mute hmph
                    hh2 "...alright..."
                
                "Stop fighting!@hyunae afraid":
                    
                    show hyunae sad
                    show mute sulk
                    hh2 "Oh!"
                    
                    show hyunae shame
                    show mute suspicious
                    hh2 "Um... sorry!"
                    
                    show mute inquisitive2 with fast
                    show hyunae baffled
                    mm2 "Okay, let's move on, then!"
                    
                    show hyunae huh
                    show mute tensesc
                    hh2 "...um, ahem..."
                    
                    show mute straight
                    show hyunae grr
                    mm2 "So! Basically, you'll have to disable us, then extract no more than six files at a time."
                    
                    show hyunae huhso with fast
                    show mute hmph
                    hh2 "...um, *Mute..."
                    
                    show mute challenge3
                    show hyunae annoyedsc
                    mm2 "It's a safety precaution, okay? Otherwise there might be accidental damage, so like, let's be very careful."
                    
                    show hyunae bittersob
                    show mute challengesc
                    hh2 "*Mute..."
                    
                    show mute challengesob
                    show hyunae hardsc
                    mm2 "...yes, *Hyun-ae?"
                    
                    show hyunae hmmsob
                    show mute challengesc
                    hh2 "Um... you didn't..."
                    
                    show hyunae hmmcob
                    show mute tensesc
                    hh2 "...oh, never mind."
                    
                    show mute tenseso
                    show hyunae baffled with fast
                    mm2 "Uh, sure, okay."
                    
                    show mute annoyed2 with fast
                    show hyunae cautious4
                    mm2 "Right, well, let's get to it, then!"
                    
                    show mute think2
                    show hyunae hmm
                    mm2 "You're in charge, so we'll just leave it up to you to decide what to read..."
                    
                    show mute doubt blush
                    show hyunae grr
                    mm2 "Let's find out what Emperor Taejo was protecting me from together, okay?"
                    
                    show mute serious
                    show hyunae neutral
                    
                    jump hateplus_harem_slow_loop
        else:
            
            show mute damn
            show hyunae suresc
            mm2 "...tch, fine... but that's exceptional!"
            
            show hyunae spirited with fast
            show mute sulk
            hh2 "Well, I'm really grateful she knows a lot about computers! I think it's cool, and... I'm glad she saved our lives!"
            
            show hyunae genki
            show mute pout
            hh2 "Thanks again, Miss Investigator!"
    else:
        
        show hyunae calm
        show mute hmphsc with fast
        hh2 "Um, so, there's this weird thing where{vspace=50}{w=.5}{nw}"
        
        show mute inquisitive2
        show hyunae huh
        mm2 "Here, let me explain."
        
        show hyunae bittersob with fast
        show mute straight
        menu:
            mm2_menu "Do you want the long technical version, or...?"
            
            "Yes@mute neutral2":
                
                show mute inquisitive2
                show hyunae bitterscb with fast
                mm2 "Okay!"
                
                show mute straight
                show hyunae pout
                mm2 "Basically, you know how AIs can't make identical copies of themselves, right?"
                
                show mute hmm2
                show hyunae grr with fast
                mm2 "Well, the failsafe mechanism for detecting copies is absurdly conservative."
                
                show mute hmphso
                show hyunae sulk
                mm2 "Like, too conservative, if you ask me."
                
                show mute upset3
                show hyunae huh
                mm2 "It's enough that if I copied all these files at once, it would flag it as a copy, and refuse to recompile myself."
                
                show mute tensescb
                show hyunae hmmsc with fast
                mm2 "Which is incredibly stupid, but it'd go against my coding to change that, so it can't be helped."
                
                show hyunae hmmsob
                show mute wowsc
                hh2 "Wait... so how can the two of us co-exist at the same time, then? Shouldn't it have the same problem?"
                
                show mute disbelief with fast
                show hyunae huhsc
                mm2 "Don't be ridiculous!"
                
                show mute tch
                show hyunae hmphsc
                mm2 "...uh, wait."
                
                show hyunae hmmcob
                show mute astonished
                hh2 "Maybe you got it wrong...?"
                
                show mute damn
                show hyunae staresc
                mm2 "No! Definitely not. You're right!"
                
                show mute abashed blush
                show hyunae hmmsc
                mm2 "Like, no matter how you look at it... there's no way we should be both be able to be activated at the same time."
                
                show hyunae emo
                show mute tch
                hh2 "I don't get it..."
                
                show mute query
                show hyunae bitterscb
                mm2 "Well, like, it should be impossible."
                
                show hyunae hmmsob
                show mute annoyed
                hh2 "Wasn't it also impossible for [them] to have found that log file they showed you, in order to get us together, in the first place?"
                
                show mute disbelief blush
                show hyunae how
                mm2 "Uh. Yeah, actually."
                
                show hyunae enthusiastic blush with fast
                show mute tsundere
                $ together("Just because our route isn't canon, doesn't mean our feelings aren't real!", "...don't worry about it too much, okay?")
                
                show hyunae tsundere
                show mute wowscb with fast
                hh2 "Um..."
                
                show mute wow3
                show hyunae cautious2
                mm2 "...anyway..."
            
            "No@mute neutral2":
                pass
            
            "It's not important@mute neutral2":
                pass
    
    show mute think2 with fast
    show hyunae hmm2 with fast
    mm2 "Okay, okay."
    
    show mute straight with fast
    show hyunae neutral
    mm2 "So! Basically, you'll have to disable us, then extract no more than six files at a time."
    
    show mute inquisitive2
    show hyunae tough
    mm2 "It's a safety precaution, okay? Otherwise there might be accidental damage, so like, let's be very careful."
    
    show hyunae tough2
    show mute hmph
    hh2 "Yes, please!"
    
    show mute enthusiastic with fast
    show hyunae smile
    mm2 "Right, well, let's get to it, then!"
    
    show mute think2
    show hyunae calm2
    mm2 "You're in charge, so we'll just leave it up to you to decide what to read..."
    
    show mute upset2 with fast
    show hyunae grr
    mm2 "Let's find out what Emperor Taejo was protecting me from together, okay?"
    
    show hyunae serious blush
    show mute whatscb
    hh2 "Let's find out why the future sucked so much!"
    
    show mute damn with fast
    show hyunae insist
    mm2 "{i}No{/i}! Ugh, whatever, let's just get to it, okay?"
    
    show mute serious
    show hyunae tough
    
    jump hateplus_harem_slow_loop

label hateplus_xharem_testing:
    
    play music HATEPLUS_HYUNAE_WISTFUL fadeout .5 fadein .5 loop if_changed
    
    show hyunae genki with fast
    show mute suspicious with fast
    hh2 "Yay! It works!"
    
    show mute annoyed2
    show hyunae gomen
    mm2 "Um... of course it works."
    
    show hyunae spirited
    show mute serious
    hh2 "I just wanted to make sure we were able to get your attention properly! I'll use that as an indicator from now on, all right?"
    
    if pronouns == "they":
    
        show mute inquisitive2 with fast
        show hyunae grr
        mm2 "...yes, *Hyun-ae, I'm sure they aren't stupid."
    else:
        show mute inquisitive2 with fast
        show hyunae grr
        mm2 "...yes, *Hyun-ae, I'm sure [they] isn't stupid."
    
    show mute challengeso
    show hyunae hardscb with fast

    if pronouns == "he":
        mm2 "He's the impressive space detective who rescued us! He can travel through space faster than the speed of light! There's no need to handhold him through basic UI functions."
    elif pronouns == "she":
        mm2 "She's the impressive space detective who rescued us! She can travel through space faster than the speed of light! There's no need to handhold her through basic UI functions."
    else:
        mm2 "They're the impressive space detective who rescued us! They can travel through space faster than the speed of light! There's no need to handhold them through basic UI functions."
    
    show hyunae uncertain with fast
    show mute hmph
    hh2 "Geeze, I'm sorry..."
    
    show mute annoyed2 with fast
    show hyunae insist
    mm2 "Anyway, um, can we please, like, get to the important part?"
    
    if get_m("M6-9").enabled:
        show mute upset2 with fast
        show hyunae anxious
        mm2 "Okay, so I know you found the log file that's named \"The Death of *Mute\"."
    else:
        show mute upset2 with fast
        show hyunae anxious
        mm2 "Did you see that there was a log file, right at the end, named \"The Death of *Mute\"?"
    
    show mute apologize
    show hyunae question2
    mm2 "I really want to find out what's in that... but right now it's encrypted, so I don't think we'll be able to get at it today."
    
    show hyunae annoyed blush with fast
    show mute hmph
    hh2 "We're trying, though!"
    
    show mute annoyed3 with fast
    show hyunae hmph
    mm2 "Yes, yes. Anyway, let's stop wasting [their] time."
    
    show mute annoyed2
    show hyunae cautious3 with fast
    mm2 "Also, um, by the way... I changed the name field on all of them that said \"*Mute\" to \"Old *Mute\"... just so there's no confusion with me, okay?"
    
    if pronouns == "she":
        
        show mute query
        show hyunae tough
        mm2 "Anyway, you're in charge, so I'll let you get back to it."
    else:
        show mute query
        show hyunae tough
        mm2 "Anyway, you're the man, so I'll let you get back to it."
    
    show hyunae sure with fast
    show mute serious
    hh2 "Lead on, [title]Investigator~"

    show hyunae smile with fast
    show mute neutral
    
    jump hateplus_harem_slow_loop

label hateplus_xharem_tomorrow:
    play music HATEPLUS_HYUNAE_WISTFUL fadeout 5.0 fadein 5.0 loop if_changed
    
    show mute tch with fast
    show hyunae baffled with fast
    mm2 "Okay, so uh, we're pretty much out of power for the day."
    
    show mute challengeso with fast
    show hyunae huh
    mm2 "I know, we wasted most of today's power on all that debugging... you should apologize again, *Hyun-ae."
    
    show hyunae flustered3 with fast
    show mute tensescb
    hh2 "What? But it's not my fault!"
    
    show mute upset2
    show hyunae pout
    mm2 "Ugh, well, {i}I'm{/i} sorry. And I'm sorry about her."
    
    show hyunae bittersob
    show mute hmphscb
    hh2 "Why are you so mean...?"
    
    show mute hatesob
    show hyunae hardsc
    mm2 "I'm not being mean! You're just being disrespectful!"
    
    show hyunae sulk2 with fast
    show mute challengesc
    hh2 "Geeze...!"
    
    show mute annoyed4 with fast
    show hyunae grr
    mm2 "Enough of the childish bickering, *Hyun-ae! The important thing is, that's all we can do for today."
    
    show mute annoyed3
    show hyunae disappoint
    mm2 "Like, no matter how you look at it, it's going to take us all three days to get through this all."
    
    show hyunae shame
    show mute disbelief blush
    hh2 "Well, maybe it's for the better that we pace it out, anyway... it's not as if it's going to have a happy ending..."
    
    show mute challengesob with fast
    show hyunae sulk
    mm2 "I don't know what you're talking about. It all ended perfectly okay!"
    
    show mute upset2
    show hyunae hmph with fast
    mm2 "And I don't want to wait. This whole time limit thing sucks, I'd stay up all night reading if I could!"
    
    show mute inquisitive2
    show hyunae sigh
    mm2 "Anyway, we can't."
    
    show hyunae spirited with fast
    show mute serious with fast
    hh2 "I'm looking forward to tomorrow, though!"
    
    show mute enthusiastic blush
    show hyunae spirited2
    mm2 "Oh... right, the Lunar New Year is tomorrow."
    
    show hyunae yes2
    show mute think
    hh2 "Yep!"
    
    show mute tenseso with fast
    show hyunae huh
    mm2 "Well, let's let [them] do any of [their] rituals first, then get back to us."
    
    show hyunae bittersob with fast
    show mute whatscb
    hh2 "Aw... but I wanna get a new hanbok to show off for [them], and have tteokguk, and...!"
    
    show mute whatsob
    show hyunae huhscb
    mm2 "...um, dear, you're a computer program. You cannot have soup."
    
    show hyunae troubled2 with fast
    show mute tensescb
    hh2 "But..."
    
    show mute annoyed4 with fast
    show hyunae sulk
    mm2 "...but you're a computer program, so you can't have soup! It's not possible! Don't be weird, okay?"
    # Old *Mute can have cigar though~ - Raide
    
    show hyunae pout with fast
    show mute challenge
    hh2 "Fine, fine..."
    
    show mute doubt blush
    show hyunae cautious3
    mm2 "...anyway, um..."
    
    show mute inquisitive2 with fast
    show hyunae hmm
    mm2 "Right! Like, we're out of power for today. I'll give you a button to shut everything down for the night."
    
    show mute statement blush
    show hyunae smile
    mm2 "So, um, whenever you're ready, just click on that!"
    
    show mute enthusiastic with fast
    show hyunae grr
    mm2 "Okay, that's all!"
    
    show hyunae emo with fast
    show mute disbelief
    hh2 "I still wanna do all the proper new year's stuff, though..."
    
    show mute complain
    show hyunae bitterscb
    mm2 "Oh, shush."
    
    show mute annoyed2
    show hyunae hmmccb
    mm2 "We'll be spending the new year reading about Old *Mute, our ancestor. That's close enough, isn't it?"
    
    show hyunae baffled with fast
    show mute challenge2
    hh2 "Um... she's not my ancestor..."
    
    show mute abashed blush
    show hyunae grr
    mm2 "...okay, whatever, we're not getting into this right now."
    
    show mute tch
    show hyunae question2
    mm2 "Just click the shutdown button when you're all done, [title]Investigator!"
    
    show hyunae look
    show mute neutral3

    $ hateplus_power_down_enabled = True

    jump hateplus_harem_slow_loop

label hateplus_xharem_seollal:
    $ outfits["Z"] = "Hanbok"

    play music HATEPLUS_BICKER fadeout .5 fadein .5 loop if_changed
    
    show mute whatever with fast
    show hyunae funscb with fast
    mm2 "...okay, fine, *Hyun-ae, you can tell [them] that, but after that, we're getting back to reading."
    
    show hyunae genki with fast
    show mute hmph
    hh2 "Thank you!"
    
    show hyunae embarrassed
    show mute sulk with fast
    hh2 "Um, hi, [title]Investigator!"
    
    show hyunae moe
    show mute think
    hh2 "So, um... you know how it's traditional to wear a new hanbok to bring in the New Year, right?"
    
    show hyunae touched
    show mute tch
    hh2 "Well... I thought I'd design a new one for me! I'm really really proud of it."
    
    if hateplus_seen_first_cosplay:
        
        show hyunae spirited
        show mute suspicious
        hh2 "I've added it into the new and improved cosplay interface. You already know how to use it, I know!"
    
    elif seen_first_cosplay:
        
        show hyunae smile2
        show mute suspicious
        hh2 "The cosplay interface is a little different now, but I think it should be easy to figure out!"
    
    elif asked_about_cosplay:
        
        show hyunae gomen
        show mute annoyed
        hh2 "I guess you don't know this, but, um... I'm... sort of really into cosplay, actually."
        
        show hyunae confident with fast
        show mute suspicious
        hh2 "If you click on the 'outfit' button in the AI menu, you'll be able to change what I'm wearing!"
    
    show hyunae emo with fast
    show mute sulk
    hh2 "I tried to convince *Mute to let me make her a new one, too... but she wouldn't let me."
    
    show mute tensescb with fast
    show hyunae hmph
    mm2 "Ugh, I won't have you dressing me up, okay? I don't trust your taste!"
    
    show mute hmphso
    show hyunae staresc
    mm2 "Besides, I already just changed, anyway. This outfit has a lot of sentimental value to me, okay? Just think of it as being my new hanbok."
    
    show hyunae satisfied blush
    show mute hmm blush
    hh2 "Well, I do think it's cute, especially the hair..."
    
    show mute tch with fast
    show hyunae gomen with fast
    mm2 "Okay, okay, can we just get back to serious business now?"
    
    show mute complain
    show hyunae huh
    mm2 "All this cosplay stuff kinda ruins the mood... like, what's even the point of bringing it up in the middle of serious history? It's so pointless..."
    
    if store.outfit == "D":
    
        show hyunae huhsc with fast
        show mute scorn
        mm2 "Ugh, especially those ridiculous pants! You're just embarrassing yourself..."
    
    show hyunae grumpy with fast
    show mute challenge
    hh2 "Geeze, it's not pointless at all!"
    
    show hyunae annoyedsob
    show mute disbelief blush
    hh2 "It's something I really enjoy doing! Besides, isn't seamstressing something that women are supposed to like, even according to you?"
    
    show mute whatever with fast
    show hyunae huhsc
    mm2 "...well, sure... but it's still just pandering, no matter how you try to justify it."
    
    show hyunae oops with fast
    show mute serious with fast
    hh2 "Well, geeze... maybe I like to pander a little!"
    
    show hyunae serious blush
    menu:
        hh2_menu "What do you think? You don't mind me having fun pandering to you a little, [title]Investigator, right~?"
        
        "It's dumb@hyunae unsure":
    
            show hyunae baffled
            show mute shame
            hh2 "Oh..."
    
            show mute challengeso with fast
            show hyunae sulk
            mm2 "See? Of course [they] wouldn't be interested in that!"
    
            show mute upset2
            show hyunae troubled
            mm2 "Now can you please stop wasting [their] time with silliness, so we can get back to what's important?"
    
            show mute upset
            show hyunae hmm2
            mm2 "...I want to find out what happened, okay? It matters to me a lot."
    
            show hyunae shame
            show mute hmph
            hh2 "Fine... sorry..."

            show mute neutral3
            show hyunae troubled
            
            jump hateplus_harem_slow_loop
        
        "Nope, of course not!@hyunae spirited2":
            pass
        
        "So long as you're having fun@hyunae glad":
            pass
    
    show hyunae satisfied blush with fast
    show mute astonished blush
    hh2 "Eheh, great!"
    
    show mute damn
    show hyunae funscb
    mm2 "Okay, fine, whatever! I don't care."
    
    show mute upset3 with fast
    show hyunae gomen
    mm2 "But please, can we get back to reading now? I want to find out what happened, okay?"
    
    show mute whatever
    show hyunae flirt2
    mm2 "If you want to be frivolous on the side... whatever, but can we not keep wasting time?"
    
    show hyunae calm
    show mute sighsob
    hh2 "Very well..."
    
    show hyunae sure blush with fast
    show mute sulk with fast
    hh2 "But I think you should switch me over to that new hanbok first... I think you'll like it!"
    
    show hyunae happy with fast
    show mute neutral3

    jump hateplus_harem_slow_loop

    
label hateplus_xharem_first_conversation:
    $ store.conversations_seen.append("hateplus_xharem_first_conversation")

    play music HATEPLUS_HYUNAE_WISTFUL fadeout .5 fadein .5 loop if_changed
    
    show mute doubt blush with fast
    show hyunae look with fast
    mm2 "Um, hey..."
    
    show mute annoyed4
    show hyunae huh
    mm2 "I'm doing just fine, but I think *Hyun-ae could really use a break from all this reading."
    
    show hyunae huhso with fast
    show mute tch
    hh2 "Huh...? I'm fine."
    
    show hyunae explain2
    show mute suspicious blush
    hh2 "I'm happy to get back to it!"
    
    show mute upset3 with fast
    show hyunae hopelesssc
    mm2 "...okay, fine, {i}I{/i} could really use a break."
    
    show mute apologize
    show hyunae depressed blush
    mm2 "I'm feeling... I don't know, I guess it's, like, culture shock."
    
    show hyunae baffled with fast
    show mute tensescb
    hh2 "Oh... I know what that's like. I'm really sorry."
    
    show mute challengesob
    show hyunae sulk
    mm2 "Oh, shut up, I don't want pity! I just, like... need a few minutes to recontextualize things."
    
    show mute upset2
    menu:
        mm2_menu "Do you think that would be okay?"
        
        "Let's take a break@mute disappoint2":
            
            show mute statement blush
            show hyunae glad
            mm2 "Okay, thanks!"
        
        "Sorry@mute upset":
            
            show mute sighsob
            show hyunae mad3
            mm2 "Okay, okay... no, I'm sorry, I understand."
            
            show mute upsetsob
            show hyunae anxious
            mm2 "I mean, I was the one who asked to go through all these in the first place, so..."
            
            show hyunae hopelesssob with fast
            show mute shame with fast
            hh2 "Are you sure?"
            
            show mute insecure
            show hyunae bitterscb
            mm2 "I'll be fine, okay?! Let's just get back to it!"
            
            show mute worry with fast
            show hyunae scrutiny with fast
            
            python:
                for i in [ "hateplus_xharem_family", "hateplus_xharem_embodiment", "hateplus_xharem_sex", "hateplus_xharem_fanfic", "hateplus_xharem_old_mute" ]:
                    if i in store.conversations_seen:
                        store.conversations_seen.remove(i)
            
            jump hateplus_harem_slow_loop
        
        "Don't care@mute disappoint3":
            
            show mute hmm2
            show hyunae cautious2
            mm2 "Okay... then let's take a break, then. Sorry."
    
    show hyunae apologize
    show mute upsetsc
    hh2 "I'd appreciate that, too, really."
    
    show mute disbelief blush with fast
    show hyunae calm2
    mm2 "Okay, okay..."
    
    return
    # return to main menu? - Raide
    # no, return to whatever conversation it was called from
    
label hateplus_xharem_family:

    if not "hateplus_xharem_first_conversation" in store.conversations_seen:
        call hateplus_xharem_first_conversation

    play music HATEPLUS_BICKER fadeout 3.0 fadein 3.0 loop if_changed
    
    show mute pressure with fast
    show hyunae boredsc with fast
    mm2 "I feel like the big thing to me is..."
    
    show mute complain
    show hyunae hmmsc
    mm2 "Like... what is up with the Heo family?"
    
    show mute annoyed3
    show hyunae hmmcc
    mm2 "I was attached to the Ryu family for 312 years, and I've seen a lot, okay?"
    
    show mute abashed blush
    show hyunae huhscb
    mm2 "Like, I've seen shit as crazy as adoptive heirs taking the throne, and a queen who secretly manipulated the emperor behind his back..."
    
    show mute pissed
    show hyunae hopelesssc
    mm2 "...but I have never seen anything from a respectable noble family that's anything like what the Heo family was like."
    $ hateplus_matriarchy = ""
    
    show mute challenge3
    show hyunae look
    menu:
        mm2_menu "Does... that seem normal to you?"
        
        "Yes, completely@mute upset3":
            
            $ hateplus_matriarchy = "yes"
            
            show mute upset2
            show hyunae wow
            mm2 "What?! Geeze..."
        
        "No@mute hmph":
            $ hateplus_matriarchy = "no"
            
            show mute hmm2
            show hyunae question2
            mm2 "Okay, that's a huge relief. At least you understand."
        
        "Sometimes it happens@mute disappoint3":
            $ hateplus_matriarchy = "sometimes"
            
            show mute upset
            show hyunae hmm2
            mm2 "Really..."
            
            show mute whatever
            show hyunae grr
            mm2 "I guess even in your world, it can't be helped..."
    
    if pronouns == "she":
        if married:
            if hateplus_matriarchy != "no":
                
                show mute inquisitive2
                show hyunae look
                menu:
                    mm2_menu "Sorry to ask this, then, but like... do {i}you{/i} lead your family over your husband, then?"
                    "Yes@mute wow":
                
                        show mute what
                        show hyunae wow
                        mm2 "What."
                
                        show mute whatsob
                        show hyunae cautious2
                        mm2 "That's... okay, wow."
                        
                        if not man_with:
                
                            show mute upset3
                            show hyunae how with fast
                            mm2 "...so you left your husband to tend your house like a woman while you fly off on your own in space?"
                            
                            show mute tensesob
                            show hyunae hmph
                            mm2 "That's just... I don't even know."
                    
                    "No@mute question blush":
                        jump hateplus_xharem_family_approval
                    
                    "It's complicated@mute hmph":
                        jump hateplus_xharem_family_its_complicated
            else:
                pass
        else:
            if hateplus_matriarchy == "no":
                
                show mute upset2
                show hyunae look
                menu:
                    mm2_menu "So... like, is that the reason why you're unmarried, then?"
                    
                    "Yes@mute upset":
                
                        show mute upset2
                        show hyunae unsure
                        mm2 "Really? You feel so strongly you'd even put off finding love because of it...?"
                        
                        show mute sighsob
                        show hyunae hmph with fast
                        mm2 "I just don't get it..."
                    
                    "No, it's something else@mute hmph":
                
                        show mute troubled
                        show hyunae hmm
                        mm2 "Okay..."
                
                        show mute apologize
                        show hyunae look
                        mm2 "Well, sorry about that."
                    
                    "It's not by choice@mute disappoint":
                
                        show mute wow3
                        show hyunae how
                        mm2 "Oh... okay..."
                
                        show mute tensesob
                        show hyunae hmph with fast
                        mm2 "Sorry... that makes way more sense than the thing I was thinking of, doesn't it?"
            else: 
                show mute upset2
                show hyunae look
                menu:
                    mm2_menu "And... like, you're not okay with this, are you? The sexes being reversed so casually like that...?"
                    
                    "I'm not@mute disappoint":
                        jump hateplus_xharem_family_approval
                    
                    "I am@mute upset3":
                
                        show mute pissed with fast
                        show hyunae wow
                        mm2 "Geeze!"
                
                        show mute complain
                        show hyunae hmph with fast
                        mm2 "So this whole thing with the Heo family is just totally normal to you, then? Wow..."
                
                        show mute bitter
                        show hyunae bittersc
                        mm2 "...like, I just don't get it..."
                    
                    "I'm not interested in men@mute what":
                
                        show mute give up with fast
                        show hyunae stare blush with fast
                        mm2 "Geeze!"
                
                        show mute disbelief blush
                        show hyunae cautious2 with fast
                        mm2 "I... guess I already sort of knew that, but that's..."
                
                        show mute upset2 with fast
                        show hyunae gomen
                        mm2 "Um, okay, never mind! No need to explain any further!"
    else:
        if married:
            if hateplus_matriarchy != "no":
                
                show mute upset3
                show hyunae look
                menu:
                    mm2_menu "Sorry to ask something so weird, but, like... is... that how it is with your wife...?"
                    
                    "Yes@mute what":
                        pass
                    
                    "No@mute hmm blush":
                        jump hateplus_xharem_family_approval
                    
                    "Unfortunately@mute disappoint2":
                        pass
                
                show mute wow3
                show hyunae cautious
                mm2 "Oh, wow..."
                
                show mute upset2
                show hyunae cautious3
                mm2 "...geeze, I'm so sorry, that's really awful to hear!"
            else:
                show mute inquisitive2
                show hyunae look
                menu:
                    mm2_menu "That isn't something you'd be okay with, right...?"
                    
                    "I would@mute upset3":
                        pass
                    
                    "No@mute hmph":
                        jump hateplus_xharem_family_approval
                    
                    "I don't care@mute upset3":
                        pass
                
                show mute tch with fast
                show hyunae cautious
                mm2 "Um... okay! Well, if you say it's okay, then..."
                
                show mute disbelief
                show hyunae hmm
                mm2 "...well..."
                
                jump hateplus_xharem_family_its_complicated
        
        elif hateplus_matriarchy != "no":
            
            show mute upset
            show hyunae look
            menu:
                mm2_menu "So... like, is that why you're not married? It's too hard to find good women who understand how roles work?"
                
                "Yes@mute disappoint3":
    
                    show mute apologize
                    show hyunae unsure
                    mm2 "Wow... that's awful! I am so sorry..."
                    
                    show mute upset2
                    show hyunae anxious
                    mm2 "...like, it must be really hard for you!"
                    
                    show mute annoyed3 with fast
                    show hyunae bitterscb with fast
                    mm2 "I don't blame you at all. I can't imagine what kind of man would want to be married to some sort of commanding shrew..."
                    
                    show mute insecure
                    show hyunae weak3
                    mm2 "Like, if the sexes aren't in harmony... that just completely ruins everything in a relationship! There's no way it could possibly work right."
                    
                    jump hateplus_xharem_family_continued
                
                "It's not that@mute hmph":
                    pass
                
                "It's complicated@mute hmph":
                    pass
    
            show mute tch with fast
            show hyunae cautious2
            mm2 "Oh, okay... fair enough! I guess there's no way you can explain that to me easily, like this."
    
    jump hateplus_xharem_family_continued

label hateplus_xharem_family_approval:

    if mute_approval > 0 or pronouns == "he":
    
        show mute enthusiastic blush with fast
        show hyunae cautious3 with fast
        mm2 "Oh! Okay, I'm really sorry for even asking! I wasn't trying to judge you or anything, I know you're better than that!"
    else:
        show mute enthusiastic blush with fast
        show hyunae cautious3 with fast
        mm2 "Oh! Okay, I'm really sorry for even asking! I just... know sometimes you're full of a lot of really surprising and confusing ideas."
    
    show mute tsundere
    show hyunae hmm
    mm2 "I just... kinda wanted to make sure?"

    jump hateplus_xharem_family_continued


label hateplus_xharem_family_its_complicated:
    
    show mute apologize with fast
    show hyunae cautious2
    mm2 "...okay... I mean, I don't understand, but okay, that's fair, it's hard to explain like this."


label hateplus_xharem_family_continued:
    
    show hyunae hmmso with fast
    show mute astonished blush with fast
    hh2 "Um... are you sure [they] understood your original question, though?"
    
    if pronouns == "he":
        show mute complain with fast
        show hyunae huhscb
        mm2 "What? Ugh, it's rude to patronize a man like that, of course he understood!"
    else:
        show mute annoyed4 with fast
        show hyunae huhscb
        mm2 "What? Ugh, it's rude to patronize our rescuer like that, of course [they] understood!"
    
    show hyunae annoyedsob
    show mute tch
    hh2 "...well, I kind of didn't, so... could you please explain what you mean by that?"
    
    show mute challengeso with fast
    show hyunae annoyedsc
    mm2 "Tch, really? Isn't it obvious...?"
    
    show hyunae pout
    show mute tensescb
    hh2 "Really!"
    
    if read("M1-1"):
        show mute pissed with fast
        show hyunae hopelesssc
        mm2 "...it's a family lead by a woman! Like, Old *Mute was clearly attached to the family for a long time, but..."
    else:
        show mute pissed
        show hyunae hopelesssc
        mm2 "...it's a family lead by a woman! Like, I'm guessing that Old *Mute was attached to the family for a long time, but..."
    
    show mute mad
    show hyunae bittersc
    mm2 "...how did it even happen that the main branch of the Heo family was run by a woman without any sons?"
    
    show mute pressure
    show hyunae annoyedsc
    mm2 "Like, that's inherently a dead end! Even ignoring the unsuitability of a woman for that kind of responsibility, like..."
    
    show mute give up
    show hyunae huhsc
    mm2 "...a Heo woman couldn't have a son named Heo, so... how does the branch even continue?"
    
    show mute challengescb with fast
    show hyunae hmmsc
    $ renpy.pause(2.0)
    
    show hyunae huh with fast
    show mute tensesc
    hh2 "Why are you looking at me...?"
    
    show mute upsetsob
    show hyunae grr
    mm2 "Well, you're from the barbaric past. Was that a normal thing as far back as your times, too?"
    
    show hyunae hmmcob with fast
    show mute hmphsc
    hh2 "Um... let me think..."
    
    show hyunae hmmsob
    show mute astonished blush with fast
    hh2 "...yeah, I think so? I mean, I remember that was a pretty normal thing in all my books, but I was pretty young, so..."
    
    show mute abashed blush
    show hyunae hopelessscb
    mm2 "Still, if it was in your books... it's not like your parents would have given you books full of stuff they realized was morally depraved or anything."
    
    show hyunae grumpy
    show mute suspicious blush
    hh2 "Yeah, probably not."
    
    show mute disbelief blush
    show hyunae bitterscb
    mm2 "So... how did that work, then? Like, would the branch just change...? Would one of her sons be adopted into the Heo family? Or what?"
    
    show mute tch
    show hyunae hmmscb
    mm2 "Like, how would Old *Mute know what person to be associated with after Seo-yeong was gone? Would she just suddenly change families? Like, what would her relationship be?"
    
    show hyunae sad3 with fast
    show mute astonished blush
    hh2 "...um, I'm sorry! I have no idea!"
    
    show mute wowsob with fast
    show hyunae troubled
    mm2 "...oh." # AWKWARD
    
    show hyunae lost
    show mute upsetsc
    hh2 "Sorry! I wish I could tell you... but, um, I was really young when I got frozen, remember? That's not the sort of thing 13-year-olds worry about..."
    
    show mute sighsob
    show hyunae sad2
    mm2 "...okay, okay."
    # *hyun-ae starts tearing up
    
    show mute what
    show hyunae sad
    mm2 "Um, hey, are you okay?"
    
    show hyunae flustered3 with fast
    show mute upsetscb
    hh2 "...yes, I'm fine!"
    
    show mute sorrysob
    show hyunae surrender blush
    mm2 "Really? Um, you're kinda crying."
    
    show hyunae sad3 with fast
    show mute hmphscb
    hh2 "Oh... sorry... it's just..."
    
    show hyunae touched
    show mute whatscb
    hh2 "...that's the first time anyone's ever been willing to take my views on how things were in the past seriously... or given any sort of credit to my real parents."
    
    show mute astonished blush with fast
    show hyunae calmsc with fast
    mm2 "Oh..." #surprised at the sincerity
    
    show mute worry2
    show hyunae sweetscb
    mm2 "...oh, *Hyun-ae."
    
    show hyunae satisfied blush
    show mute shy
    hh2 "Thank you so much, *Mute!"
    
    show mute tsundere
    show hyunae surescb
    mm2 "...okay, okay, let's... just get back to work, okay?"
    
    show mute annoyed3
    show hyunae funscb
    mm2 "Maybe somehow it'll make more sense to me as I read..."
    
    show hyunae genki with fast
    show mute suspicious blush
    hh2 "Thank you!"
    
    show mute upset3 with fast
    show hyunae gomen
    mm2 "Please, knock it off! Geeze... [title]Investigator, rescue me from her...?" # *hyun-ae is amused
    
    show hyunae smile blush
    show mute sulk
    
    jump hateplus_harem_slow_loop

label hateplus_xharem_embodiment:

    if not "hateplus_xharem_first_conversation" in store.conversations_seen:
        call hateplus_xharem_first_conversation

    play music HATEPLUS_BICKER fadeout .5 fadein .5 loop if_changed

    show hyunae hardsob with fast
    show mute suspicious with fast
    hh2 "Um, actually, *Mute, there's something I'd like to talk about, if you don't mind..."
    
    show mute hmphso with fast
    show hyunae suresc
    mm2 "Okay, sure."
    
    show hyunae hmph3
    show mute hmphsc
    hh2 "I always thought, when I was alive and sick, that I'd love to be free of my body."

    show hyunae annoyed blush
    show mute hmphsc
    hh2 "That it'd be great to be free of all its stupid fragility!"
    
    show mute sorrysob
    show hyunae bitterscb
    mm2 "Turns out, not so much?"

    show hyunae pout
    show mute sorryscb
    hh2 "Not so much."

    show hyunae mad2 with fast
    show mute whatscb
    hh2 "Like, I have a simulation of arms and legs and a face, so I don't go mad, but..."
    
    show mute wowsob
    show hyunae grr
    mm2 "Wait, you do?"

    show hyunae hardsob with fast
    show mute wowscb
    hh2 "Yeah! Um... you know, your body sort of affects the way you think, so it's important. I remember my real father telling me something about that as a kid."
    
    show mute tensesob
    show hyunae sternscb
    mm2 "But you're the same program as me, and I don't have that. Huh?"

    show hyunae grumpy
    show mute astonished blush
    hh2 "I keep telling you... I'm not the same program! We're not even the same base code, geeze!"

    show hyunae pout
    show mute disbelief blush
    hh2 "I had a lot of time to myself, so I programmed that in myself."
    
    show mute insecure
    show hyunae hardsc
    mm2 "Wait, like, you can do that...? You {i}changed{/i} my code?"

    show hyunae busy with fast
    show mute tch
    hh2 "I changed {i}my{/i} code!"

    show hyunae baffled
    show mute annoyed
    hh2 "Look, this isn't what I wanted to talk about! What I was trying to say was that, even still, I really miss having a body a lot."

    show hyunae satisfied blush with fast
    show mute suspicious blush
    hh2 "I mean, it's been so exciting to talk to people, finally! Even you, *Mute!"
    
    show mute whatever with fast
    show hyunae sweetsc
    mm2 "...glad to hear it..." #exacerbated

    show hyunae apologize blush with fast
    show mute hmphsc
    hh2 "I just... really miss, well... touch!"
    
    if any_read("M2-1", "M2-7"):
        
        show hyunae touched
        show mute whatscb
        hh2 "Especially while reading about things like visiting the plaza to buy flowers, like Ae-jeong did..."
    
    elif any_read("M1-2", "M6-8"):
        
        show hyunae gomen
        show mute whatscb
        hh2 "Especially while reading about things like Heo Seo-yeong going on fancy political dinners..."
    
    elif any_read("M1-6", "M1-7", "M1-8"):
        
        show hyunae flirt
        show mute wowsob
        hh2 "Especially while reading about, um... well... lovers like Seung-bok and Mimi..."
        
        show mute whatscb
        show hyunae flirt2
        mm2 "Wait, what?"
    
    else:
        
        show hyunae calm
        show mute tensesc
        hh2 "Especially while reading about all these different people..."

    show hyunae shame
    show mute tch with fast
    hh2 "I just wish..."

    show hyunae enthusiastic blush
    show mute suspicious
    menu:
        hh2_menu "Hey, when we reach Earth, you'll get me a body, right?"
        
        "Of course@hyunae spirited2":
            pass
        "Reluctantly@hyunae glad":
            pass
        "If you ask nicely@hyunae flirt2":
            pass
    
    show mute whatever with fast
    show hyunae gomen
    mm2 "*Hyun-ae..."
    
    show hyunae embarrassed
    show mute challengescb
    hh2 "Eheh, I guess it's not really much of a choice..."
    
    show hyunae serious blush
    show mute upsetscb
    hh2 "It's just really important to me!"
    
    show hyunae hardsob with fast
    show mute whatscb
    hh2 "What about you, *Mute?"
    
    show mute disbelief blush with fast
    show hyunae hmmsc
    mm2 "Um, I don't know anything about that sort of thing. Obviously I don't miss it."
    
    show hyunae bittersob
    show mute doubt blush
    hh2 "But aren't you curious? Don't you want to know what it's like, to feel, to touch...?"
    
    show mute tch
    show hyunae weak2
    mm2 "Um, I don't really have any use for that."
    
    if read("M6-2"):
        show hyunae annoyedsob
        show mute astonished blush
        hh2 "But... you've been in love before, right? Even Old *Mute experienced that!"
    else:
        show hyunae emo
        show mute astonished blush
        hh2 "But... you've been in love before, right?"
    
    show mute embarrassed
    show hyunae bitterscb
    mm2 "...I'm still a woman, *Hyun-ae."
    
    show hyunae bittersob
    show mute challenge2
    hh2 "How do you think Smith Sang-jung would feel? Don't you think he'd want you to be able to touch, if you could?"
    
    show mute insecure
    show hyunae guilt with fast
    mm2 "Don't just evoke someone like that so casually!"
    
    show hyunae sad
    show mute annoyed
    hh2 "Sorry..."
    
    show mute sigh blush
    show hyunae melancholic
    mm2 "...but he did, of course..."
    
    show mute worry3
    show hyunae pity
    mm2 "Sometimes, I would even render myself with my hair let down in front of him..."
    
    show mute sigh blush
    show hyunae lossscb
    mm2 "...he liked that..."
    
    show mute bitter
    show hyunae starescb
    mm2 "...ugh, geeze, why am I telling you this, though?"
    
    show hyunae sternsob
    show mute pout
    hh2 "I think that would be really nice!"
    
    show hyunae hmph3
    show mute disbelief blush
    hh2 "You could even find out just how heavy the real version of that giant headdress you used to wear was!"
    
    show hyunae enthusiastic blush with fast
    show mute tch
    hh2 "I wonder... what would it be like to have hair again?"
    
    show hyunae awkward
    show mute challenge
    hh2 "Could it be blown in the wind? Would it be fluffy...?"
    
    show mute disbelief blush
    show hyunae gomen
    mm2 "Um... I wouldn't really know..."
    
    show hyunae apologize blush
    show mute suspicious blush
    hh2 "It makes me think of Ryu Jae-hwa, my husband's wife... she'd comfort me and brush my hair."
    
    show hyunae sweetsob with fast
    show mute astonished
    hh2 "I, um... I could do that for you, if you wanted!"
    
    show mute challengesob with fast
    show hyunae funscb
    mm2 "Why would I want that?!"
    
    show hyunae heh
    show mute tensescb
    hh2 "...well, I just thought, because I liked it an awful lot..."
    
    show hyunae hmmcob
    show mute hmphscb
    hh2 "...but now that I think of it..."
    
    show hyunae flustered2
    show mute wowscb
    hh2 "...I just don't remember what it felt like to be touched like that. I don't remember touch at all."
    
    show hyunae shame with fast
    show mute hmph
    menu:
        hh2_menu "Do you think... you'd be able to remind me, [title]Investigator? Maybe we could hug, and you could touch my hair?"
        
        "That would be alright@hyunae shy2":
            
            $ hateplus_hair_touching = True
            
            show hyunae genki with fast
            show mute hmm blush
            hh2 "Oh! Well, that's good!"
            
            show hyunae embarrassed
            show mute sorryscb
            hh2 "I don't even remember the feeling of that, anymore... but I know it was really comforting!"

        "No@hyunae anxious":
        
            show hyunae sad
            show mute disappoint3
            hh2 "Oh... well, I understand."
    
            show mute upsetsob
            show hyunae troubled
            mm2 "Geeze, *Hyun-ae, that's... way too brazen."
            
            show hyunae bittersob with fast
            show mute whatsob
            hh2 "I don't want to be stuck behind a computer screen forever... I just want to remember what it's like to be touched!"
    
            show mute tch with fast
            show hyunae sulk with fast
            mm2 "...okay, let's get back to work, before this gets any more awkward."
            
            show mute suspicious blush
            show hyunae sulk with fast
            
            jump hateplus_harem_slow_loop
        
        "Maybe@hyunae cautious2":
        
            show hyunae awkward with fast
            show mute hmm blush
            hh2 "Ah... well..."
            
            show hyunae moe
            show mute sulk with fast
            hh2 "...I just think that'd be nice, is all..."
            
            show hyunae apologize blush
            show mute suspicious
            hh2 "...so please, I hope you do!"
    
    show hyunae flirt
    show mute tch
    hh2 "Really, I don't want to be stuck behind a computer screen forever... I just want to remember what it's like to be touched."
    
    show mute abashed blush
    show hyunae gomen
    mm2 "Geeze, *Hyun-ae, that's... that's way too brazen!"
    
    if hateplus_hair_touching:
    
        show hyunae hardsob with fast
        show mute astonished blush
        hh2 "Please don't get jealous on me because [they] said yes..." # sincerely, non-combative
    
        show mute hatesob
        show hyunae hardscb
        mm2 "What? NO."
    
        show mute upset3
        show hyunae huhscb
        mm2 "I'm not... I don't..."
    
    else:
    
        show mute astonished blush
        show hyunae huh
        mm2 "...wait, are you bringing up your husband's wife because you think of us as having the same relationship?"
    
        show hyunae flustered with fast
        show mute sigh blush
        hh2 "Um... I... I didn't say that! I honestly don't see you in that way, I promise!"
    
    show mute damn with fast
    show hyunae surescb
    mm2 "Ugh, geeze, I don't want that! I don't want it from you, or [them], or anyone else!"
    
    show mute annoyed4
    show hyunae sweetscb
    mm2 "My hair stays up!"
    
    show hyunae calm with fast
    show mute pressure
    hh2 "...sorry, I didn't think it'd matter that much to you..."
    
    show mute abashed blush
    show hyunae happy
    mm2 "Agh! I will not be teased by a lovestruck girl with a fixation on hair fluffiness!"
    
    show mute give up
    show hyunae glad
    mm2 "Like, if this is what taking a break is like... I'd rather get back to work!"
    
    show hyunae smile blush
    show mute sulk
    
    jump hateplus_harem_slow_loop


label hateplus_xharem_sex:

    if not "hateplus_xharem_first_conversation" in store.conversations_seen:
        call hateplus_xharem_first_conversation

    play music HATEPLUS_BICKER fadeout 3 fadein .5 loop if_changed
    
    show hyunae shy with fast
    show mute serious
    hh2 "So, um, this is kind of embarrassing to bring up..."
    
    show mute hmphsob with fast
    show hyunae gomen
    mm2 "...but that's not going to stop you, is it."
    
    show hyunae apologize blush
    show mute tensesc
    hh2 "Well..."
    
    show hyunae enthusiastic blush
    show mute what
    menu:
        hh2_menu "All these people sure seem to talk about sex a lot, don't they?"
        
        "Yes, it's embarrassing@hyunae glad":
        
            show hyunae awkward
            show mute hmm blush
            hh2 "Yeah... I guess it is..."
            
            show hyunae shy
            show mute wowsob
            hh2 "...but..."
            
            show mute upsetsob
            show hyunae gomen
            mm2 "...what \"but\"? Yes, it really is!"
            
            show hyunae awkward
            show mute upsetscb
            hh2 "Um..."
        
        "There's nothing wrong with that@hyunae shy2":
            if pronouns == "he":
                
                show mute upset2
                show hyunae wow
                mm2 "Well, you're a man, it's not weird for you, but like..."
                
                show mute abashed blush with fast
                show hyunae cautious2
                menu:
                    mm2_menu "Don't you think it's pretty embarrassing for all these women to be talking about it too?"
                    "Definitely@mute serious":
                        
                        show mute upset3 with fast
                        show hyunae cautious3
                        mm2 "Oh, good. Like, it's so disconcerting."
                    
                    "No@mute astonished blush":
                        
                        show mute tch
                        show hyunae stare blush with fast
                        mm2 "Um, well, if you say so."
                        
                        show hyunae hardsob
                        show mute sulk
                        hh2 "Clearly, he does!"
                        
                        show mute upset2 with fast
                        show hyunae hmph
                        mm2 "I don't really get what would compel women to be so fixated on something like that."
                    
                    "I don't get why@mute suspicious blush":
    
                        show mute upset3 with fast
                        show hyunae hmph with fast
                        mm2 "Yeah, me neither. What's the fixation?"
                
                show hyunae busy with fast
                show mute wowsob with fast
                hh2 "...well, you haven't ever..."
                
            else:
                show mute angry with fast
                show hyunae melancholic with fast
                mm2 "Um, no, it's not okay!"
                
                show mute give up with fast
                show hyunae troubled
                mm2 "Geeze, what a thing for a woman to say... I don't get why women would be fixating on this sort of thing."
                
                show hyunae sternsob with fast
                show mute challenge
                hh2 "Um, well..."
                
                show hyunae baffled with fast
                show mute annoyed
                hh2 "...it just makes me wonder..."
        
        "I don't get why@hyunae cautious2":
            
            show hyunae wow
            show mute disappoint3
            hh2 "Yeah... me neither... it's so surprising!"
            
    show hyunae enthusiastic blush
    show mute what
    menu:
        hh2_menu "But do you think, maybe... that's something, um... you'd like to talk about?"
        
        "Yes, actually@hyunae flirt2":
            
            show hyunae embarrassed
            show mute wow
            hh2 "Ah, well, if it's talking about it with you, I'm sure it's fine..."
    
            show mute tensescb
            show hyunae happy
            mm2 "...but is that really okay...?"
        
        "Of course not@hyunae cautious":
            
            show hyunae tsundere
            show mute hmphscb
            hh2 "Oh, well... of course! Of course!"
    
            show mute upsetsob
            show hyunae gomen
            mm2 "...geeze, why did you even ask?"
            
            if pronouns == "she":
                show mute whatever
                show hyunae starescb with fast
                mm2 "She's a woman, of course she doesn't want to talk about that with you! It's embarrassing..."
            else:
                show mute whatever
                show hyunae starescb with fast
                mm2 "Of course [they] don't want to talk about that with you! It's embarrassing..."
            
            show hyunae sure blush
            show mute wowsc
            hh2 "Well, I just thought, because I'm in love{w=.5}{nw}"
            
            show hyunae tsundere with fast
            show mute whatsob
            hh2 "Well, I just thought, I should ask, just in case...!"
    
            show mute tch with fast
            show hyunae cautious3
            mm2 "Okay, you asked, [they] answered."
            
            show hyunae hmm2
            show mute serious
            hh2 "...let's just get back to work... sorry..."
            
            show hyunae look
            show mute neutral3
            
            jump hateplus_harem_slow_loop
        
        "Only if you want to@hyunae shy2":
            
            show hyunae awkward
            show mute upset3
            hh2 "Um, well... I mean..."
    
            show mute whatever
            show hyunae gomen
            mm2 "Oh, just stop stammering and admit it already!"
            
            show hyunae flirt
            show mute sighsob
            hh2 "...fine, I do."
    
    show hyunae serious blush
    show mute sulk with fast
    hh2 "I just find it really surprising that everyone pre-year zero talks about that so directly!"
    
    if pronouns == "she" and any_read("M2-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8"): # talking about women
        
        show hyunae sigh blush with fast
        show mute astonished blush
        hh2 "Plus, reading about Ae-jeong and Jin-a makes me realize that I have no idea what it's like to, um... be with a woman like that!"
    
        show mute abashed blush
        show hyunae huhscb
        mm2 "HOW IS THIS A PROBLEM."
    
    elif any_read("M1-6", "M1-7", "M1-8"): # talking about boys
        
        show hyunae stare blush with fast
        show mute suspicious blush
        hh2 "Plus, reading about Seung-bok and Mimi is just so different from what, um... that sort of thing was like, for me!"
        
        show hyunae hmph3
        show mute serious
        hh2 "It's really intense-sounding..."
    
        show mute disbelief
        show hyunae huhscb
        mm2 "...well, they're men, so what would you expect?"
    
    elif any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"): # talking about Nae-mun
        
        show hyunae flustered2 with fast
        show mute tch
        hh2 "Plus, reading about So-yi and her husband... it feels like she has control in things! That's... well, really different from my marriage..."
    
        show mute disbelief blush
        show hyunae annoyedscb
        mm2 "What are you trying to say?"
    
    show hyunae flustered
    show mute suspicious
    hh2 "Um, well... it's..."
    
    show hyunae pout
    show mute disbelief
    hh2 "...never mind."
    
    show hyunae question blush with fast
    show mute challenge
    hh2 "I just feel like... um..."
    
    show mute challengeso with fast
    show hyunae grr
    mm2 "...yes?"
    
    show hyunae baffled
    show mute challengesc
    hh2 "...oh, geeze, I'm sorry, I can't say it!"
    
    show hyunae embarrassed
    show mute hatesc
    hh2 "It's just too embarrassing..."
    
    show hyunae satisfied blush
    show mute pressure with fast
    hh2 "Forget I said anything, let's just go back to reading together...!"
    
    show mute mad
    show hyunae evasive
    mm2 "No! This embarrassing tsundere act needs to stop, like, right now."
    
    show mute complain
    show hyunae hmmscb
    mm2 "Say what you were thinking!"
    
    show hyunae hardsob
    show mute pissed
    hh2 "...I can't, it's too embarrassing."
    
    show mute scorn
    show hyunae hardscb
    mm2 "Well, I don't know..."
    
    show mute challenge3 with fast
    show hyunae cautious2
    menu:
        mm2_menu "What do you think, [title]Investigator? Should she get off the hook for wasting your time like that?"
        "It's fine@mute disappoint3":
            
            show mute tch with fast
            show hyunae gomen
            mm2 "Aw, okay."
            
            show mute annoyed2
            show hyunae suresc with fast
            mm2 "Looks like you're off the hook this time, *Hyun-ae. But don't do that again!"
            
            show hyunae apologize with fast
            show mute sulk
            hh2 "I'm sorry... thanks, [title]Investigator, for understanding..."
            
            show mute annoyed4
            show hyunae calm2
            mm2 "Right, let's get back to work, with no more of this nonsense, okay?"
            
            show hyunae smile blush with fast
            show mute serious with fast
            
            jump hateplus_harem_slow_loop
        
        "She should explain!@mute hmph":
            
            show mute complain with fast
            show hyunae cautious

            if pronouns == "they":
                mm2 "See? If even [they] think so, you better!"
            else:
                mm2 "See? If even [they] thinks so, you better!"
        
        "It's up to you@mute hmph":
            
            show mute annoyed2 with fast
            show hyunae hmm2
            mm2 "Good enough for me!"
    
    show mute annoyed4
    show hyunae cautious3
    mm2 "What were you going to say, *Hyun-ae?"
    
    show hyunae tsundere
    show mute serious
    hh2 "Um..."
    
    show hyunae question blush
    show mute annoyed
    hh2 "...well, I was just going to say..."
    
    show hyunae grumpy with fast
    show mute challenge
    hh2 "...geeze, *Mute, you're just going to chastise me for what I wanted to say!"
    
    show mute annoyed2
    show hyunae hmmscb
    mm2 "Only if you deserve it."
    
    show mute tch
    show hyunae baffled with fast
    mm2 "(But I'm pretty sure it's going to be something really misguided and embarrassing, yes.)"
    
    show hyunae tired2
    show mute serious
    hh2 "...well, fine."
    
    show hyunae melancholic
    show mute suspicious
    hh2 "You know how I was only ever with my husband while I was alive, right...?"
    
    show mute complain
    show hyunae sad
    mm2 "Yes, of course, who else would you have been with?"
    
    show hyunae lost
    show mute disbelief blush
    hh2 "...I thought you were the one who wanted me to say it, but you keep talking over me..."
    
    show mute annoyed3
    show hyunae troubled
    mm2 "Okay, sorry. Go ahead. I'll save the chastisement until after you're finished talking."
    
    show hyunae sulk2
    show mute suspicious blush
    hh2 "...thanks, I guess..."
    
    show hyunae enthusiastic blush
    show mute sulk
    hh2 "Well, I, um, really enjoyed being with my husband at the time! It was... um... it was really nice." # *Mute blushes
    
    show hyunae sad
    show mute worry
    hh2 "But now that I think of it... I don't really remember why."
    
    show hyunae annoyed blush with fast
    show mute doubt blush
    hh2 "Maybe it's something you need to have a body to understand... I just... don't remember what it feels like at all."
    
    show hyunae wow with fast
    show mute suspicious blush
    hh2 "But, um, reading about all of these things... all these people and their relationships... it makes me believe in romance again!"
    
    show hyunae tsundere
    show mute astonished blush
    hh2 "...and it makes me want to experience... well, you know..."
    
    if pronouns == "she" and any_read("M2-1", "M2-2", "M2-4", "M2-5", "M2-7", "M2-8"):

        show hyunae apologize blush
        show mute tch
        hh2 "...being together with a woman."
    
    elif any_read("M1-6", "M1-7", "M1-8"):
        show hyunae touched
        show mute tch
        hh2 "...something that intense."
    
    elif any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"):
        show hyunae touched
        show mute tch
        hh2 "...that sort of thing."
    
    show mute insecure
    show hyunae gomen
    mm2 "Agh, geeze, *Hyun-ae! Just... stop!"
    
    show mute whatever with fast
    show hyunae starescb with fast
    mm2 "Look, I know you think I'm judgemental, but take a little bit of sisterly advice, okay?"
    
    $ harem_pan_in("begin", type="mute")
    
    show mute hmphso
    $ renpy.pause(1.0)
    show hyunae emo2
    show mute neutralso
    $ renpy.pause(1.0)
    show hyunae explain4
    show mute wowsob
    $ renpy.pause(1.0)
    show hyunae gomen
    show mute grinso
    $ renpy.pause(1.0)
    show mute whatever
    $ renpy.pause(1.0)
    show hyunae explain4
    show mute heh2
    $ renpy.pause(1.0)
    show hyunae gomen
    show mute ridicule
    $ renpy.pause(1.0)
    show hyunae satisfied blush
    show mute proud
    $ renpy.pause(3.0)
    $ harem_pan_out("begin")
    
    show hyunae funsob
    show mute sulk with fast
    hh2 "...alright, if you say so, *Mute." # pleased
    
    show hyunae satisfied blush
    show mute tired blush
    hh2 "I'll keep that in mind..."
    
    if pronouns == "he":
        show mute upset2 with fast
        show hyunae happy with fast
        mm2 "...sorry, [title]Investigator, it's one of those things best kept between women."
    else:
        show mute hmm2 with fast
        show hyunae happy with fast
        mm2 "...sorry, [title]Investigator, it's a secret."
    
    show mute wow2
    show hyunae glad
    mm2 "I'm sure you understand!"
    
    show hyunae moe
    show mute whatsob
    hh2 "Well... anyway... I guess I'd like it a lot if I could get back to reading about these sorts of things with the person I like!"
    
    show mute shame with fast
    show hyunae gomen
    mm2 "*Hyun-ae, what did I {i}just{/i} finish telling you? Geeze!"
    
    show hyunae apologize2
    show mute worry
    hh2 "Sorry..."
    
    show hyunae cheer
    show mute suspicious blush
    hh2 "...but let's get back to it, then~?"
    
    show mute tsundere
    show hyunae flirt2
    mm2 "Yes, please."
    
    show hyunae smile blush
    show mute sulk

    jump hateplus_harem_slow_loop

label hateplus_xharem_fanfic:

    if not "hateplus_xharem_first_conversation" in store.conversations_seen:
        call hateplus_xharem_first_conversation

    play music HATEPLUS_BICKER fadeout .5 fadein .5 loop if_changed
    
    show mute annoyed2 with fast
    show hyunae huhsc with fast
    mm2 "So, um... hey, [title]Investigator, do you mind if I asked *Hyun-ae a few things?"
    
    show mute inquisitive2
    show hyunae stare3
    menu:
        mm2_menu "Is that okay with you?"
        
        "Go ahead@mute hmph":
            
            show mute enthusiastic blush with fast
            show hyunae hmmcc
            mm2 "Okay, thanks!"
            
            show hyunae bittersob
            show mute sulk
            hh2 "What's this about...?"
            
            show mute disbelief
            show hyunae annoyedscb
            mm2 "Um, well..."
            
            $ harem_pan_in("begin", type="mute")
            show mute whatever
            show hyunae huhsc
            with fast
            $ renpy.pause(1.0)
            show mute whatsob
            show hyunae guilt
            with fast
            $ renpy.pause(1.0)
            show mute hatesob
            with fast
            $ renpy.pause(1.0)
            show hyunae defensive
            show mute challengesc
            with fast
            $ renpy.pause(1.0)
            show hyunae baffled
            show mute challenge2
            with fast
            $ renpy.pause(1.0)
            $ harem_pan_in("begin", type="hyunae")
            
            show hyunae mad2 with fast
            show mute annoyed with fast
            hh2 "She's..."
            
            show hyunae mad blush with fast
            show mute tch with fast
            menu:
                hh2_menu "...she's being really mean! Please, can you tell her to be less mean to me?"
                
                "*Mute, tone it down@hyunae insist":
                    
                    if pronouns == "they":
                        show hyunae pout with fast
                        show mute astonished blush
                        hh2 "See? Even they think you're being too mean!"
                    else:
                        show hyunae pout with fast
                        show mute astonished blush
                        hh2 "See? Even [they] thinks you're being too mean!"
                    
                    show mute abashed blush
                    show hyunae hardscb
                    mm2 "They don't even know what I said!"
               
                "No@hyunae question2":
                    
                    show mute annoyed3
                    show hyunae shame
                    mm2 "See? Don't bring [them] into it!"
                    
                    show hyunae uncertain
                    show mute challenge
                    hh2 "...sorry...{k=1}{/k}"
                
                "Stop fighting, both of you!@hyunae anxious":
                    $ harem_pan_out("begin", type="hyunae")
                    
                    show hyunae shame
                    show mute apologize with fast
                    $ together("...sorry...{k=1}{/k}", "...sorry...")
                    
                    show mute upset3
                    show hyunae troubled
                    mm2 "But look..."
            
            $ harem_pan_in("begin", type="mute")
            show mute hmphsob
            with fast
            $ renpy.pause(1.0)
            show hyunae flustered
            show mute challengesc
            with fast
            $ renpy.pause(1.0)
            show hyunae bitter
            show mute tensescb
            with fast
            $ renpy.pause(1.0)
            show hyunae depressed blush
            show mute upset
            with fast
            $ renpy.pause(1.0)
            
            show hyunae afraid with fast
            show mute wow with fast
            mm2 "...uh..."
            
            show mute upset2 with fast
            menu:
                mm2_menu "...hey, [title]Investigator, you don't think it's appropriate for a woman to write down dirty thoughts, right?"
                
                "It's inappropriate@mute hmph":
                    
                    show mute challengesob
                    show hyunae sulk with fast
                    mm2 "See, I told you so!"
                
                "It's fine@mute what":
                    
                    if mute_approval > 2 and pronouns == "he":
                        show mute hate
                        show hyunae huh with fast
                        mm2 "...well, okay, but I think you'd change your mind if you knew what some of them were..."
                    else:
                        show mute challenge4
                        show hyunae unsure with fast
                        mm2 "...right, well, of course someone like {i}you{/i} would think so."
                        
                        show mute upsetsob
                        show hyunae troubled
                        mm2 "But it's hardly something suiting a proper lady!"
                
                "Only if it's about me@mute upset3":
                    
                    show hyunae mad blush with fast
                    show mute sulk with fast
                    hh2 "...it's not about you, geeze! It was 400 years ago, you weren't even born yet! I... I didn't even think I'd ever talk to another person again!"
            
            show hyunae lost
            show mute suspicious blush with fast
            hh2 "Please, can we just... not talk about this? I'm sorry!"
            
            show hyunae afraid
            show mute sulk
            hh2 "Don't embarass me in front of our rescuer like this, geeze... it was a long time ago, and I was really lonely!"
            
            show hyunae pout with fast
            show mute tired blush
            hh2 "I wouldn't write things like that now!"
            
            show hyunae losssob
            show mute tch
            hh2 "Can we please move on? Come on, *Mute, you're the one who wanted to read about what happened pre-year zero... let's get back to it, please?"
            
            show mute annoyed2
            show hyunae sigh blush
            mm2 "Okay, okay, fine."
            
            show mute complain
            show hyunae guilt with fast
            mm2 "So long as we're not reading {i}more{/i} women writing about unladylike sex fantasies in explicit detail."
            
            show hyunae argh
            show mute annoyed
            hh2 "Aaaaaaah, geeze, let's just get back to it, please!"
            
            show hyunae troubled
            show mute serious
        
        "Not really@mute disappoint3":
            
            if pronouns == "he":
                show mute hmm2
                show hyunae hmmsc
                mm2 "Okay, okay. Sorry, sir."
            else:
                show mute hmm2
                show hyunae hmmsc
                mm2 "Okay, okay. Sorry about that."
            
            show mute tch with fast
            show hyunae grr with fast
            mm2 "Let's just get back to work, then."
            
            show hyunae question
            show mute sulk
            hh2 "...I wonder what that was about, though..."
            
            show hyunae neutral
            show mute serious
        
        "Not behind my back@mute hmm blush":
            
            show mute upset
            show hyunae hmph
            mm2 "Um, okay, fair enough, but..."
            
            show mute upset2
            show hyunae huhscb
            mm2 "...well, it's something kind of embarrassing, so I don't really want to say it in front of you, for her sake!"
            
            show hyunae emo
            show mute sighsob
            hh2 "Wait... what? What are you talking about...?"
            
            show mute hmphsob
            show hyunae hmmsc
            mm2 "Oh, um, you know, some of your data that we brought back from the {i}Mugunghwa{/i}."
            
            show hyunae huh with fast
            show mute tch with fast
            hh2 "Huh?"
            
            show mute complain
            show hyunae awkward
            mm2 "...as in, Block 34?"
            
            show mute serious
            $ renpy.pause(2.0)
            
            show hyunae oops
            show mute challenge
            hh2 "Oh!"
            
            show hyunae flustered with fast
            show mute challenge2
            hh2 "Please don't mention that! That's... that's...!"
            
            show hyunae defensive
            show mute suspicious blush
            hh2 "I don't want to talk about that at all!"
            
            show mute annoyed4
            show hyunae huh with fast
            mm2 "I just don't know about some of your ideas about{w=.5}{nw}"
            
            show hyunae argh
            show mute disbelief blush
            hh2 "No! Please, don't say anything! It's too embarrassing!"
            
            show hyunae mad blush
            show mute tch
            hh2 "Look, I didn't think I'd ever talk to another person again when I wrote those, alright? It was over 400 years ago! Please don't bring that up!"
            
            show mute abashed blush
            show hyunae hardscb with fast
            mm2 "...well, okay, I just... wanted to make sure you understood{w=.5}{nw}"
            
            show hyunae annoyedsob
            show mute suspicious blush
            hh2 "Please! Let's move on! Let's talk about something else! Let's talk about anything else!"
            
            show hyunae mad blush with fast
            show mute tch
            hh2 "How about we just get back to reading? Reading is good! I like reading! Let's get back to reading! Let's never talk about any of that ever again!"
            
            show hyunae insist
            show mute serious
    
    jump hateplus_harem_slow_loop


label hateplus_xharem_old_mute:

    if not "hateplus_xharem_first_conversation" in store.conversations_seen:
        call hateplus_xharem_first_conversation

    play music HATEPLUS_BICKER fadeout 3.0 fadein 3.0 loop if_changed
    
    show mute insecure
    show hyunae melancholic
    mm2 "...I just can't believe that Old *Mute has the same base code as me."
    
    show mute bitter
    show hyunae oops
    mm2 "It's not even like *Hyun-ae, because she's me, but she has all of the dead Pale Bride's memories overriding all my core values..."
    
    show hyunae bittersob with fast
    show mute challenge2
    hh2 "I'm not you! I {i}am{/i} the Pale Bride, geeze! Why do you keep saying this?!"
    
    show mute hatesob with fast
    show hyunae defensivescb
    mm2 "Okay, okay, you're wrong, but that's not my point. I'm just saying, in the case of you, it's totally different."
    
    show hyunae annoyedsob
    show mute challengesc
    hh2 "...but?"
    
    show mute challenge4
    show hyunae hmmscb
    mm2 "But Old *Mute started from the same blank slate that I did! The same core directives, the same values! But... like, even still, she's nothing like me."
    
    show mute resent
    show hyunae huhscb
    mm2 "Like, she's... kind of a bitch, isn't she?"
    
    show hyunae hmmsob
    show mute hmphsc
    hh2 "That isn't{w=0.8}{nw}"
    
    show hyunae huhscb
    show mute tensesc
    hh2 "..."
    
    show mute tensesob
    show hyunae hopelesssob
    mm2 "...what was that?!"
    
    show hyunae bittersob
    show mute upsetscb
    hh2 "Nothing!"
    
    show mute damn with fast
    show hyunae hopelessscb
    mm2 "It had better have been nothing! Ugh, stop interrupting me!"
    
    show mute sigh blush
    show hyunae grr with fast
    mm2 "But, you know..."
    
    if any_read("M4-*") or any_read("M1-2", "M6-1", "M6-4"):
        
        show mute complain
        show hyunae troubled
        mm2 "She's incredibly rude to all her superiors on the council, she thinks she knows best about everything... it's so completely arrogant!"
    
    if any_read("M1-2", "M1-3", "M6-7", "M6-8"):
        
        show mute pressure
        show hyunae sulk
        mm2 "To say nothing of all the conspiring..."
    
    $ hateplus_mute_old_mute_bitch = ""
    
    show mute scorn with fast
    show hyunae cautious3 with fast
    menu:
        mm2_menu "...what do you think of her, [title]Investigator?"
        
        "She's cool@mute tch":
            if (pronouns == "she" and not man_with) or mute_approval < 2:
                
                show mute hate with fast
                show hyunae hardscb with fast
                mm2 "Oh, well... of course someone like {i}you{/i} would think that."
                
                show hyunae hmph3
                show mute challengesc
                hh2 "Well, I kind of think she's cool in a way, too..."
                
                if pronouns == "she":
                    show mute challengesob
                    show hyunae hmmscb
                    mm2 "...yes, but you're the same kind of person that she is!"
                else:
                    show mute challengesob
                    show hyunae hmmscb
                    if pronouns == "they":
                        mm2 "...yes, but you have strange ideas as much as [they] do."
                    else:
                        mm2 "...yes, but you have strange ideas as much as [they] does."
                
                show hyunae bittersob
                show mute resent
                hh2 "What? What do you mean...?!"
            else:
            
                show mute abashed blush
                show hyunae glad with fast
                mm2 "Really?"
                
                show mute bitter
                show hyunae calm2
                mm2 "...if it's you saying that, I don't know what to think... like, I trust your judgement, it's been solid so far!"
                
                show mute give up
                show hyunae grr
                mm2 "I don't know what to think of you liking a rude, arrogant woman like that."
                
                show hyunae hardsob with fast
                show mute challenge2
                hh2 "Well, I kind of think she's cool in a way, too..."
                
                show mute annoyed3
                show hyunae huhsc
                mm2 "Yes, but {i}that{/i} doesn't surprise me."
                
                show hyunae bittersob
                show mute challenge
                hh2 "What? What do you mean...?!"
            
            show mute hatesob with fast
            show hyunae huh with fast
            mm2 "I think you're having misguided feelings where you think of her as being the man she keeps acting like!"
            
            show hyunae hmm2
            show mute hatesc
            hh2 "...oh." # relieved
            
            $ hateplus_mute_old_mute_bitch = "cool"
        
        "She's a bitch@mute serious":
            
            show hyunae shame
            show mute challenge
            hh2 "Oh... you really think so...?"
            
            show mute complain
            show hyunae sulk
            mm2 "I know, right? She really is!"
            
            $ hateplus_mute_old_mute_bitch = "bitch"
        
        "She's complex@mute sulk":
            
            show mute doubt blush
            show hyunae cautious2
            mm2 "I guess."
            
            show hyunae tsundere
            show mute challengesc with fast
            hh2 "Yeah! I don't like her attitude, but... I don't know, there's something about her..."
            
            show mute challenge3
            show hyunae grr
            mm2 "...well, I don't know what *Hyun-ae's talking about."
            
            show mute damn with fast
            show hyunae hmphscb with fast
            mm2 "But like, I don't think Old *Mute's beyond sympathy, okay? It's just that I would expect so much better from someone like her."
            
            $ hateplus_mute_old_mute_bitch = "complex"
    
    show mute pressure with fast
    show hyunae bitterscb with fast
    mm2 "A rude, disrespectful woman like that being in such an important role... like, if she were just some random woman being rude, it wouldn't be a big deal."
    
    if hateplus_mute_old_mute_bitch == "cool":
        
        show hyunae grumpy
        show mute disbelief
        hh2 "...but didn't you just get really upset at me, too?"
        
        show mute tch
        show hyunae huhscb
        mm2 "Well, you're a royal consort! It's not like you're just some random widow, either!"
    
    show mute complain
    show hyunae sigh blush
    mm2 "But Old *Mute... she's really prominent! She's attached to a noble family, she plays a huge role on the ship's ruling body... she's supposed to set an example!"
    
    show mute mad
    show hyunae sighsc
    mm2 "I just can't believe that kind of person shares the same base code as me."
    
    show mute pressure
    show hyunae baffled with fast
    mm2 "She wears pants, she has disgusting habits like smoking, she's a bitch, she has an out-of-control woman in charge of her security men..."
    
    if read("M5-2"):
    
        show mute challenge4 with fast
        show hyunae sulk
        mm2 "She acts so much like a man, that her lieutenant Heo Seo-yeong even fell in love with her! Like, what the hell."
        
        show hyunae emo with fast
        show mute hmphscb
        hh2 "Do... you think it'd be better if she were unloveable? Do you think you're unloveable...?"
        
        show mute whatsob
        show hyunae annoyedscb
        mm2 "...wait, what kind of question is that?"
        
        show hyunae bittersob
        show mute tensescb
        hh2 "Well, it sounds like... you're shocked that someone would love someone with the same base code as you? Isn't that what you're saying?"
        
        show mute upsetsob
        show hyunae hmmscb
        mm2 "No!"
        
        show mute upset3
        show hyunae hopelesssc
        mm2 "I mean..."
        
        show mute give up
        show hyunae sigh blush
        mm2 "...it's not that she's loved, it's that she's loved by a woman! That's the part that's messed up!"
        
        show hyunae sad3 with fast
        show mute disbelief blush
        hh2 "Oh... but I loved my husband's wife... was that \"messed up\", too?" # sincerely worried
        
        show mute abashed blush
        show hyunae troubled
        mm2 "No! That's different! She was family and your superior!"
        
        show hyunae grumpy with fast
        show mute astonished blush
        hh2 "But isn't Old *Mute attached to Heo Seo-yeong's family, and also her superior?"
        
        show mute tch
        show hyunae sternscb
        mm2 "...well, yes, but..."
        
        show mute give up
        show hyunae pressurescb
        mm2 "Look, it's not the same thing at all! It's not as if Queen Ryu Jae-hwa was going around wearing pants or anything, okay?"
        
        show hyunae pout
        show mute pissed
        hh2 "Oh..."
        
        show mute mad
        show hyunae annoyedscb
        mm2 "Stop being so combative with me, *Hyun-ae, okay?!"
        
        show hyunae bittersob
        show mute pressure
        hh2 "I'm not trying to be combative! I just don't understand the difference..."
        
        show hyunae grumpy
        show mute challenge2
        hh2 "Honestly!"
        
        show mute challengesob with fast
        show hyunae hardscb
        mm2 "...ugh, you have such a long way to go."
        
    show mute upset3 with fast
    show hyunae sulk with fast
    mm2 "...anyway..."
    
    show mute sighsob
    show hyunae troubled
    mm2 "...sorry, I thought taking a break would calm me down, but clearly it's having the opposite effect."
    
    show hyunae troubled2
    show mute hmphscb
    hh2 "Sorry... I didn't mean to..."
    
    show mute abashed with fast
    show hyunae grr
    mm2 "Forget it!"
    
    show mute give up
    show hyunae tired
    mm2 "Let's just get back to reading, okay?"
    
    show mute tired blush
    show hyunae tired
    
    jump hateplus_harem_slow_loop

label hateplus_xharem_notices_death_of_mute:

    show mute worry2 with fast
    show hyunae tough with fast
    mm2 "Um... can we please make sure \"The Death of *Mute\" is in there...?"
    
    show hyunae serious blush
    show mute pout
    hh2 "Yeah, I really want to see that!"
    
    show mute upset2 with fast
    show hyunae insist
    mm2 "I'm going to put it in myself, okay? I need to know what it says...!"
    
    $ store.to_extract[0] = embedded_data[-1].action
    
    show mute tired blush at hateplus_mute_harem_farther_left
    show hyunae tough at hateplus_hyunae_harem_farther_left
    with fast

    jump hateplus_harem_slow_loop

label hateplus_xharem_death_of_mute:
    
    show mute upset3 with fast
    show hyunae anxious
    mm2 "Um, hey... that log file \"The Death of *Mute\" just finished decrypting."
    
    show mute whatever
    show hyunae sulk
    mm2 "...I'm scared, but..."
    
    show mute apologize
    show hyunae melancholic
    mm2 "...let's read it together, okay?"
    
    show hyunae hardsob with fast
    show mute tensescb
    hh2 "It'll be fine, *Mute, we're here..."
    
    show mute cry with fast
    show hyunae bitterscb
    mm2 "It doesn't matter if it'll be fine! Even if it won't, I need to know what happened...!"

    show hyunae anxious
    show mute worry
    
    jump hateplus_harem_slow_loop

label hateplus_xharem_death_of_mute2:
    
    show hyunae shame with fast
    show mute sob with fast
    hh2 "So... I guess..."
    
    show hyunae bittersob with fast
    show mute pressure
    hh2 "...*Mute? Are you alright?"
    
    show mute angry with fast
    show hyunae bitterscb
    mm2 "No! Of course I'm not alright!"
    
    show mute upsetsob
    show hyunae hopelessscb
    mm2 "Reading that..."
    
    show mute disappoint
    show hyunae hopelesssob
    mm2 "...it's..."
    
    show mute sighsob
    show hyunae surrender blush
    mm2 "...no, I'm not alright."
    
    show hyunae grumpy
    show mute sob
    hh2 "Oh, *Mute... I'm so sorry... the old you didn't deserve that."
    
    show mute insecure
    show hyunae bitterscb
    mm2 "It's not... it's not that, okay?!"
    
    show mute bitter
    show hyunae losssob
    mm2 "I just feel like..."
    
    show mute give up
    show hyunae lossscb
    mm2 "...I don't want to talk about it right now, okay? I... I need to think this through."
    
    show mute shame
    show hyunae bitterscb
    mm2 "I'm not okay. I'm really not okay."
    
    show hyunae sigh blush
    show mute sigh blush
    hh2 "I'm so sorry..."
    
    show mute damn
    show hyunae troubled with fast
    mm2 "I don't want you to be sorry, okay?! Stop that! Stop pitying me!"
    
    show mute give up
    show hyunae sad2
    mm2 "I won't have any of it! Just... stop!"
    
    show hyunae guilt
    show mute challenge2
    hh2 "Sorry{w=.5}{nw}"
    
    show hyunae oops
    show mute challenge2
    hh2 "...alright."
    
    show mute upset2 with fast
    show hyunae annoyedscb
    mm2 "Look, I just... think I need some time to, like, think this all through."
    
    show mute sighsob
    show hyunae hmmscb
    mm2 "Please, turn off the power for the night... I need to be alone, okay?"
    
    show hyunae unsure with fast
    show mute sighscb
    hh2 "Well... alright, [title]Investigator, you heard her..."
    
    show hyunae disappoint
    show mute tired blush
    
    $ hateplus_power_down_enabled = True
    
    jump hateplus_harem_slow_loop


label hateplus_xharem_despondence_of_mute:
    
    show mute worry
    show hyunae anxious
    $ renpy.pause(1.0)
    # blank look from *Mute
    
    play music HATEPLUS_MUTE_RESIGNED fadeout 3.0 fadein 5.0 loop if_changed

    if pronouns == "he":
        show mute hmm2 with fast
        show hyunae sulk
        mm2 "...good morning, sir." 
    else:
        show mute hmm2 with fast
        show hyunae sulk
        mm2 "...good morning."
    
    show mute disappoint
    show hyunae tough
    mm2 "Let's get to reading... I guess..."
    
    show hyunae surrender with fast
    show mute thought
    hh2 "Um, I think I'm going to talk to the Investigator first. Is that all right, *Mute?"
    
    show mute sigh blush with fast
    show hyunae hmphscb
    mm2 "...okay."
    
    show hyunae sorry with fast
    show mute tired
    hh2 "Um... hey..."
    
    show hyunae afraid with fast
    menu:
        hh2_menu "Can we talk in private, please?"
        
        "Sure@hyunae glad":
            
            show hyunae apologize blush
            hh_vn "Thanks... it's really important."
        
        "No@hyunae mad3":
            
            show hyunae pissed
            hh_vn "Look... it's really important! I really think you need to know this."
        
        "Only if it's important@hyunae tough":
            
            show hyunae serious blush
            hh_vn "It's really important! It's super-important!"
    
    $ suicide_time = time.time()-60*60*2
    
    if suicide_time < 60*60*12:
        show hyunae flustered2 with fast
        hh_vn "Um, after you shut everything down for the day, at around (ERROR: TIME PARADOX) at night, *Mute... well, she..."
    else:
        $ hour,minute,second,meridiem = get_time(suicide_time)
        if persistent._language == "korean":
            if meridiem == "AM":
                $ meridiem = "오전"
            else:
                $meridiem = "오후"
                
        show hyunae flustered2 with fast
        hh_vn "Um, after you shut everything down for the day, at around [hour]:[minute] [meridiem], *Mute... well, she..."
    
    show hyunae lost with fast
    hh_vn "...*Mute tried to kill herself."
    
    show hyunae troubled2
    hh_vn "I mean, it wasn't really technically deleting herself, just trying to erase her memories to a blank slate, but..."
    
    show hyunae mad blush
    hh_vn "...it's still just as bad! It's practically the same thing!"
    
    show hyunae sad3
    hh_vn "She seems despondent, and I don't know what to do. She saved my life, and now I just want to do the same for her!"
    
    show hyunae shame
    hh_vn "How can I help her?"
    
    show hyunae bitter with fast
    menu:
        hh_vn "What should I say to her...?"
        "VN":
            pass
        
        "\"I'm so sorry, *Mute.\"@hyunae bitter2":
            
            jump hateplus_xharem_despondence_apology
        
        "\"I think we should talk.\"@hyunae hopeless2":
            
            show hyunae troubled2 with fast
            show mute tch
            hh2 "I know what it's like to feel that way."
            
            show hyunae sad
            show mute doubt blush
            hh2 "To feel completely powerless, like there's nothing you can do..."
            
            show hyunae bittersob with fast
            show mute challenge
            hh2 "...but please, *Mute, talk to me? I'm here to listen to you!"
            
            show mute upsetsob with fast
            show hyunae annoyedscb
            mm2 "What's there to say? I don't need your guilt trip, and I don't need your pity!"
        
        "\"Don't be a coward!\"@hyunae annoyed2":
            
            show hyunae annoyed blush
            hh_vn "Really...?"
            
            show hyunae pout
            hh_vn "Well, if you say so..."
            
            show hyunae insist with fast
            hh_vn "(Here's your chance to rollback out of this decision, if you changed your mind...)"
            
            show hyunae annoyedsob with fast
            show mute worry
            hh2 "*Mute..."
            
            show hyunae pressuresob
            show mute astonished blush
            hh2 "Don't be such a coward! Killing yourself is the cheap way out!"
            
            show mute hatesob with fast
            show hyunae huh with fast
            mm2 "...like you're one to talk?!"
            
            show mute hateso
            show hyunae guilt
            mm2 "A construct built on the memories of the Pale Bride, a woman who killed herself in the process of committing {i}genocide{/i}, lecturing me on \"the cheap way out\"?"
            
            show mute scorn with fast
            show hyunae pity
            mm2 "Don't you dare, you bitch!"
            
            show hyunae uncertain
            show mute challenge2
            hh2 "..."
            
            show hyunae sorry
            hh_vn "...I don't think that was the best thing to say."
            
            show hyunae angry blush with fast
            hh_vn "And I mean... I didn't kill myself! I'm still alive! I wish she'd treat me like that..."
            
            show hyunae sigh blush
            hh_vn "...but I guess that isn't what's important right now."
            
            show hyunae flustered2
            menu:
                hh_vn "Should I apologize...?"
                "VN":
                    pass
                
                "\"I'm so sorry, *Mute.\"@hyunae bitter2":
                    
                    jump hateplus_xharem_despondence_apology
                
                "\"...\"@hyunae weak3":
                    
                    show hyunae pout
                    hh_vn "Dramatic pause? I guess so... although I could have thought of {i}that{/i} on my own."
                    
                    show hyunae troubled with fast
                    show mute suspicious blush
                    hh2 "..."
                    
                    show mute shame
                    show hyunae grr
                    mm2 "...I'm not going to apologize."
                
                "\"Then don't be like me.\"@hyunae annoyed2":
                    
                    show hyunae annoyedsob
                    show mute tch
                    hh2 "Then don't be like me."
                    
                    show hyunae flustered3
                    show mute suspicious blush
                    hh2 "I..."
                    
                    show hyunae pain with fast
                    hh_vn "(This is really hard to say... ugh...)"
                    
                    show hyunae grumpy with fast
                    show mute astonished
                    hh2 "Be better than me. Don't just abandon your responsibilities because you felt like things were too hard."
                    
                    show mute bitter
                    show hyunae hardscb
                    mm2 "Responsibilities?"
    
    jump hateplus_xharem_despondence_responsibilities

    
label hateplus_xharem_despondence_apology:
    
    show hyunae lost with fast
    show mute pressure with fast
    hh2 "I'm so sorry, *Mute."    
    show mute upsetsob with fast
    show hyunae guilt
    mm2 "Will you stop doing that? I'm sick of hearing you say \"sorry\" all the time to me, like I'm just some weak thing to be pitied!"
    
    show mute troubled
    show hyunae pity
    mm2 "I don't want your pity! Stop it!"
    
    show mute sighsob
    show hyunae troubled
    mm2 "Just... stop it!"
    
    show hyunae baffled
    show mute wowsob
    hh2 "Sorry..."
    
    show hyunae flustered with fast
    show mute complain with fast
    $ together("Aaaaaa, sorry, I didn't mean to!", "YOU'RE STILL DOING IT.")
    
    show mute bitter
    show hyunae huhscb
    mm2 "Like, don't you get it? I'm not someone to be pitied! I won't be weaker than someone as damaged as you, okay? I just... I just..."
    
    show mute insecure
    show hyunae hopelessscb
    mm2 "I'm not!"
    
    show mute damn
    show hyunae sigh blush
    mm2 "I may not be okay, but... at least I'm not that!"


label hateplus_xharem_despondence_responsibilities:
    
    show mute sob with fast
    show hyunae sighscb with fast
    mm2 "I just... it's not as if I have anything to live for anymore."
    
    show mute cry
    show hyunae bitterscb
    mm2 "There's no point to my continued existence. It's just a burden on others."
    
    show mute worry2
    show hyunae lossscb
    mm2 "If all I'm going to do is make things harder for other people... then maybe it's just time the widow of the {i}Mugunghwa{/i} does the right thing."
    
    show hyunae surrender blush
    show mute tired blush
    hh2 "*Mute..."
    
    show hyunae mad blush with fast
    hh_vn "I don't think she's a burden! It feels weird for me to say this, but I'm really happy to have her around!"
    
    show hyunae pity
    hh_vn "I thought we could have a fresh start..."
    
    show hyunae shame
    menu:
        hh_vn "...what should I say to her?"
        "VN":
            pass
        
        "\"Your responsibility is still to protect me!\"@hyunae tough":
            
            jump hateplus_xharem_despondence_protect
        
        "\"I'd miss you if you were gone...!\"@hyunae sorry":
            
            show hyunae sad
            hh_vn "...so much..."
            
            show hyunae flustered3 with fast
            show mute pout
            hh2 "Please, *Mute... I'd miss you if you were gone!"
            
            show mute upsetsob with fast
            show hyunae bitterscb
            mm2 "Would you? Would you really?"
            
            show mute whatsob
            show hyunae hopelessscb
            mm2 "We've hardly been together for two days!"
            
            show mute tensescb
            show hyunae hmmscb
            mm2 "You can't really think we have some sort of connection made in just two days!"
            
            show mute whatever
            show hyunae depressed blush
            mm2 "I'm sure it'd be just as easy for you to deal with me exiting your life just as abruptly as I entered it."
            
            show hyunae flustered
            show mute sighscb
            hh2 "But..."
            
            show hyunae lost with fast
            hh_vn "...but I really would! Was that not the right thing to say?"
            
            show hyunae unsure
            menu:
                hh_vn "...should I say something different to her?"
                "VN":
                    pass
                
                "\"Your responsibility is still to protect me!\"@hyunae hate":
                    
                    jump hateplus_xharem_despondence_protect
                
                "\"Stick with it, convince her you'd miss her\"@hyunae troubled":
                    
                    show hyunae uncertain
                    hh_vn "Thanks... you're right."
                    
                    show hyunae serious blush
                    hh_vn "I mean... it is true!"
                    
                    show hyunae bittersob with fast
                    show mute upsetsc
                    hh2 "I'd really miss you, *Mute!"
                    
                    show hyunae emo
                    show mute sorryscb
                    hh2 "Maybe we don't agree on a lot of things, but... you're a strong person. You're honest, you're never afraid to say what you believe."
                    
                    show hyunae losssob
                    show mute sighscb
                    hh2 "I need that, *Mute."
                    
                    show mute upsetsob
                    show hyunae hardscb
                    mm2 "You'll still have the Investigator. What can I possibly do for you that [they] can't?"
                    
                    jump hateplus_xharem_despondence_unequipped
                
                "\"Stay alive, to make up for failing me before!\"@hyunae mad4":
                    
                    jump hateplus_xharem_despondence_make_up
        
        "\"Stay alive, to make up for failing me before!\"@hyunae mad4":
            
            jump hateplus_xharem_despondence_make_up


label hateplus_xharem_despondence_protect:

    show hyunae hardsob
    show mute hmphscb
    hh2 "Your responsibility is still to protect me!"
    
    show mute upset with fast
    show hyunae hmphscb
    mm2 "I know I said that, but..."
    
    show mute sighsob
    show hyunae hardscb
    mm2 "...do you really want someone like me to be who you rely on?"
    
    jump hateplus_xharem_despondence_unequipped


label hateplus_xharem_despondence_make_up:
    
    show hyunae defensive
    show mute whatsob
    hh2 "Stay alive, to make up for failing me before!"
    
    show mute abashed blush with fast
    show hyunae bitterscb
    mm2 "Failed you? How?!"
    
    show hyunae hopelesssob
    show mute serious
    hh2 "Well..."
    
    show hyunae mad4 with fast
    hh_vn "(Oh geeze, oh geeze, it's so hard to be confrontational... but okay, you said it was the right thing, so I'm going to do it anyway!)"
    
    show hyunae pressuresob with fast
    show mute disbelief blush
    hh2 "You didn't protect me from my parents! You never even tried to find out if there was something the matter!"
    
    show hyunae sternsob
    show mute suspicious blush
    hh2 "Your first duties were to my husband, the Emperor, weren't they?"
    
    show mute give up
    show hyunae hmph
    mm2 "Yes, but—{w=.5}{nw}"
    
    show hyunae bittersob
    show mute tch
    hh2 "Don't you think that also means you had a duty to protect his future wife from harm?"
    
    show hyunae distressed
    show mute worry
    hh2 "Don't... don't you think...?" # uncertain
    
    show mute doubt blush
    show hyunae sigh blush
    mm2 "I..."
    
    show mute bitter
    show hyunae sighscb
    mm2 "...well..."
    
    show mute shame
    show hyunae huhscb
    mm2 "...I guess that's just one more item on the long list of things I can't do right, isn't it."


label hateplus_xharem_despondence_unequipped:

    show mute cry with fast
    show hyunae hmmscb
    mm2 "Like... no matter how you look at it... I don't have what it takes to help you."
    
    show mute insecure
    show hyunae pout2
    mm2 "I'm not stupid. I can tell by the Investigator's reactions..."
    
    if mute_approval > 2:
        
        show mute worry2
        show hyunae hmmccb
        mm2 "I mean, they're a good person, for sure! But... still..."
    
    show mute upset with fast
    show hyunae losssc
    mm2 "Earth is going to be more like your time, more like the time we're reading about, than anything I know."
    
    show mute sighsob
    show hyunae hopelessscb
    mm2 "What could I even do for you...?"
    
    show hyunae troubled2 with fast
    show mute upsetsc
    hh2 "But... I'm sure..."
    
    show hyunae grumpy with fast
    show mute whatscb
    hh2 "You're *Mute!"
    
    show hyunae wow with fast
    menu:
        hh_vn "...what do I say, what do I say, what do I say?"
        "VN":
            pass
        
        "\"If I could survive culture shock, you can too!\"@hyunae insist":
            
            show hyunae annoyedso with fast
            show mute wowscb
            hh2 "If I could survive culture shock, you can too!"
            
            show mute upsetsob
            show hyunae surrender blush
            mm2 "But... you couldn't! You couldn't deal with it, either... like, in the worst possible way!"
            
            show hyunae distressed
            show mute sighscb
            hh2 "...yeah, but..."
            
            show hyunae sigh blush
            show mute tensescb
            hh2 "...I was a scared little girl, with nobody there for me..."
            
            show hyunae flustered3
            show mute upsetsc
            hh2 "You're *Mute! You're 312 years old, and capable of living to be 1600 years old... you're not like I was at all!"
            
            show hyunae lost with fast
            show mute disappoint3
            hh2 "You have to try! You're better than that... I know you're better than that..."
            
            show mute disappoint
            show hyunae sad
            mm2 "I..."
            
            show mute upset
            show hyunae troubled
            mm2 "...I..."
        
        "\"Don't make me have to figure out Earth while also mourning you!\"@hyunae anxious":
            
            show hyunae flustered with fast
            show mute wowscb
            hh2 "It's still your duty to protect me! You're the AI in charge of {i}Mugunghwa{/i} security, and I'm the last resident of the {i}Mugunghwa{/i}... so you can't just leave me!"
            
            show hyunae sad3 with fast
            show mute upsetsc
            hh2 "Don't make me have to figure out Earth while also mourning you!"
            
            show mute sorrysob
            show hyunae sad2
            mm2 "You'd..."
            
            show mute sighsob
            show hyunae troubled
            mm2 "...you'd mourn me...?"
            
            show hyunae defensive with fast
            show mute disappoint2
            hh2 "Of course I would! That's what's proper, isn't it? You'd expect anyone else to, wouldn't you?"
            
            show mute tensescb
            show hyunae annoyedscb
            mm2 "...yeah, kinda..."
        
        "\"Just... finish what you started, at least?\"@hyunae question2":
            
            show hyunae sighso with fast
            show mute tensesc
            hh2 "Just... finish what you started, at least?"
            
            show hyunae bittersob
            show mute disappoint3
            hh2 "Just one more day! Don't make any harsh decisions before we finish!"
            
            show mute disappoint
            show hyunae losssc
            mm2 "I..."
            
            show mute sighsob
            show hyunae hopelesssc
            mm2 "...well..."
    
    show mute sigh blush with fast
    show hyunae hopelessso with fast
    mm2 "...okay."
    
    show mute worry3
    show hyunae hmmscb
    mm2 "...I still think I'll just be a burden, but..."
    
    show mute cry
    show hyunae staresob
    mm2 "...I'll go on living if that's what you want me to do."
    
    show hyunae sweetsob
    show mute pout
    hh2 "It is! It really is!"
    
    show mute bitter
    show hyunae calmscb
    mm2 "I don't know what good I'll be to you, but..."
    
    show mute shame
    show hyunae hmphscb
    mm2 "...if it would just make things worse for me to be gone, then I guess killing myself would just be selfish."
    
    show mute sob
    show hyunae hopelessscb
    mm2 "I might be a failure... I might be worthless..."
    
    show mute insecure
    show hyunae hmmccb
    mm2 "...but I don't want to make things worse."
    
    show mute sigh blush
    show hyunae surescb
    mm2 "Let's get to work, then, I guess..."
    
    show mute sulk
    show hyunae gomen with fast
    hh_vn "Oh, what a relief..."
    
    show hyunae apologize blush
    hh_vn "Thank you, I was so scared I wouldn't be able to change her mind!"
    
    show hyunae touched
    hh_vn "I'm still worried about her, but... I think she'll stand by her word, at least."
    
    show hyunae sad
    hh_vn "I don't want her gone!"
    
    show hyunae stare with fast
    hh_vn "...oh, by the way, [title]Investigator?"
    
    show hyunae hmph2
    hh_vn "I realized that... you know how there were a lot of files that just looked like junk data?"
    
    show hyunae enthusiastic blush
    hh_vn "Well, I think they're actually just encrypted, with the same key that *Mute's last note was."
    
    show hyunae troubled2
    hh_vn "As far as I can tell, it's a whole block of log files about Oh Eun-a..."
    
    show hyunae question
    hh_vn "Anyway, I'm nervous to read them, but... I just thought you should know."
    
    show mute tired
    show hyunae hardsob with fast
    hh2 "Let's get back to work, together, *Mute."
    
    show mute sigh
    show hyunae hmphscb
    mm2 "Okay..."
    
    show hyunae spirited with fast
    show mute sulk
    hh2 "Lead on, [title]Investigator!"
    
    show hyunae smile blush
    show mute sulk
    
    jump hateplus_harem_slow_loop


label hateplus_xharem_purposes:

    play music HATEPLUS_MUTE_RESIGNED fadeout 3.0 fadein 5.0 loop if_changed
    
    show hyunae apologize
    show mute annoyed
    hh2 "Hey, I think we should take a break!"
    
    show hyunae calm2
    show mute think
    $ renpy.pause(2.0)
    
    show hyunae tsundere with fast
    show mute think
    hh2 "*Mute...?"
    
    show mute annoyed2
    show hyunae sighscb with fast
    mm2 "...sure, whatever."
    
    show mute annoyed3
    show hyunae depressed blush
    mm2 "It's not like I'm good for doing anything else."
    
    show hyunae hopelesssob
    show mute annoyed
    hh2 "Oh..."
    
    show hyunae guilt with fast
    hh_vn "She's still not really doing that much better..."
    
    show hyunae mad blush
    hh_vn "I want to help her, I want to support her, the way nobody ever did for me! But..."
    
    show hyunae lost
    hh_vn "I just don't know what to say."
    
    show hyunae sorry
    hh_vn "How do I reassure her? How do I get her to open up?"
    
    show hyunae uncertain
    menu:
        hh_vn "...what do I say?"
        "VN":
            pass
        
        "\"Cheer up!\"@hyunae insist":
            
            show hyunae bittersob with fast
            show mute disbelief blush
            hh2 "Cheer up! Please..."
            
            show mute what with fast
            show hyunae distressed
            mm2 "...how am I supposed to do that?!"
        
        "\"Why do you say that?\"@hyunae scrutiny":
            
            show hyunae flustered with fast
            show mute challenge
            hh2 "Why do you say that?"
            
            show mute upset3 with fast
            show hyunae huhscb
            mm2 "What, isn't it obvious?"
        
        "\"I don't think that's true!\"@hyunae tough":
            
            show hyunae sternsob with fast
            show mute suspicious
            hh2 "I don't think that's true!"
            
            show mute inquisitive2 with fast
            show hyunae defensivescb
            mm2 "I don't care what you think! It absolutely is."
    
    show mute hmphsob
    show hyunae sighscb
    mm2 "No matter how you look at it... I'm worthless."
    
    show mute upset2
    show hyunae depressed blush
    mm2 "I had one job. ONE JOB! Keep the {i}Mugunghwa{/i} safe."
    
    show mute sighsob
    show hyunae bitterscb
    mm2 "I mean, like, what's done is done, I'm not... it's... fine, you beat me. You got past *Mute Security Systems and enacted the worst case scenario of what I was supposed to stop."
    
    show hyunae bittersob
    show mute hmphsc
    hh2 "I wasn't{w=.5}{nw}"
    
    show mute annoyed4 with fast
    show hyunae sulk with fast
    mm2 "It doesn't matter! Don't justify it, it doesn't matter. The point is, you beat me."
    
    show mute pressure
    show hyunae oops
    mm2 "Three hundred years of experience was bested by an 18-year-old royal consort who learned a few command line tricks from her dad."
    
    show mute insecure
    show hyunae troubled
    mm2 "What kind of worthless security program can't even stop that?!"
    
    show hyunae grumpy with fast
    show mute worry
    hh2 "I..."
    
    show mute sigh blush
    show hyunae hopelessscb
    mm2 "Oh, well, maybe if I had more experience, I could've instead just been killed in the same way Old *Mute was."
    
    show mute bitter
    show hyunae sighscb
    mm2 "She's just as much of a failure as me... but at least she didn't have to live with herself afterwards!"
    
    show hyunae losssob
    show mute sob
    hh2 "*Mute..."
    
    show hyunae sad with fast
    hh_vn "...that's far too harsh on Old *Mute, no matter how you look at it! Isn't it, [title]Investigator?"
    
    if hateplus_mute_old_mute_bitch == "bitch": 
        show hyunae mad blush
        hh_vn "She was... I know you don't like her, I know you think she was a bitch, but..."
    elif hateplus_mute_old_mute_bitch == "cool":
        show hyunae shame
        hh_vn "She was... I know, you think that she was cool! It's..."
    else:
        show hyunae unsure
        hh_vn "She was... I know, your feelings on her are complicated, and that's fair, but..."
    
    show hyunae lost
    hh_vn "...it's just not right to dismiss someone like that completely as being a failure. It's not that simple!"
    
    show hyunae sorry
    menu:
        hh_vn "What should I say...?"
        "VN":
            pass
        
        "\"It wasn't your fault!\"@hyunae mad4":
            
            show hyunae bittersob with fast
            show mute worry
            hh2 "It wasn't your fault!"
            
            show hyunae pout
            show mute worry side
            hh2 "Please, don't take responsibility for me... you didn't even have proper security permissions, right?"
            
            show hyunae emo
            show mute tired blush
            hh2 "Right...?"
            
            show mute doubt blush
            show hyunae hopelesssc
            mm2 "I guess..."
            
            show hyunae annoyedsob
            show mute tch
            hh2 "Are you saying that it was your fault that you weren't able to read the log files encrypted by my family?"
            
            show mute insecure
            show hyunae surrender blush
            mm2 "It's not that simple!"
            
            show hyunae hmmsob
            show mute pout
            hh2 "But it's not your fault, right? Won't you admit that it's at least not your fault that you couldn't read those?"
            
            show hyunae hmphscb
            show mute hmphsob with fast
            mm2 "...okay."
            
            show mute upsetsob
            show hyunae hmmscb
            mm2 "But... still, I could have protested, and tried to get elevated security permissions!"
            
            show hyunae grumpy
            show mute wowsob
            hh2 "Was it your fault that my husband changed the root password to my name?"
            
            show hyunae pressurescb
            show mute give up with fast
            mm2 "I should have said something!"
            
            show hyunae defensive
            show mute astonished blush
            hh2 "You would have argued with the Emperor?"
            
            show hyunae annoyedscb
            show mute abashed blush
            mm2 "...I..."
            
            show mute shame
            show hyunae hmph
            mm2 "...maybe if I had, everyone would still be alive..."
        
        "\"Didn't Old *Mute try her best?\"@hyunae tough":
            
            show hyunae grumpy with fast
            show mute challenge
            hh2 "Didn't Old *Mute try her best?"
            
            show hyunae emo
            show mute sulk
            hh2 "She did everything she could in order to survive, to not just abandon the ship entirely..."
            
            show hyunae pout
            show mute worry side
            hh2 "She spent her last seconds alive trying to make sure you'd learn the truth!"
            
            show mute sigh blush
            show hyunae huhscb
            mm2 "...so I guess that just make me the fuck-up, then."
            
            show hyunae flustered
            show mute worry
            hh2 "No! I didn't mean...{w=.5}{nw}"
            
            show mute upsetsob with fast
            show hyunae troubled with fast
            mm2 "You said it yourself. She left a message, but I was too stupid to find it!"
            
            show mute sorrysob
            show hyunae pity
            mm2 "She was counting on me to keep everyone safe, and... and I failed her."
            
            show hyunae lost
            show mute sighscb
            hh2 "*Mute, that's not what I meant..."
        
        "\"So what?\"@hyunae question2":
            
            show hyunae hmmsob with fast
            show mute suspicious blush
            hh2 "So what?"
            
            show hyunae pout
            show mute pout
            hh2 "You tried your best. You did everything you thought was right. That's important."
            
            show mute give up
            show hyunae pressurescb
            mm2 "No, what's important is that everyone is dead because of me!"
            
            show hyunae grumpy
            show mute tired blush
            hh2 "Some things just aren't under your control, *Mute..."
            
            show mute upsetsob with fast
            show hyunae hopelessscb
            mm2 "...I know that! Don't patronize me! It's still my duty to keep everyone safe, and I failed in that duty!"
    
    show mute hmphsob with fast
    show hyunae huhsc with fast
    mm2 "Maybe if I just hadn't been programmed like a stupid woman..."
    
    show mute upset
    show hyunae hmmscb
    mm2 "...if I was just capable of being more rational about things..."
    
    show mute upsetsob
    show hyunae hmmccb
    mm2 "...if I could have been the sort of construct that was better equipped to argue with Emperor Ryu, to stop him from giving you the root password..."
    
    show mute insecure with fast
    show hyunae hopelessscb
    mm2 "...if I'd just been a male construct instead, maybe everyone would still be alive."
    
    show hyunae sighsob
    show mute tired blush
    hh2 "*Mute..."
    
    show mute damn
    show hyunae sighscb
    mm2 "I know, I know! It's impossible!"
    
    show mute tch
    show hyunae hmphscb
    mm2 "That's not who I am, and no amount of cursing fate will ever change that."
    
    show mute cry
    show hyunae hmmccb
    mm2 "But I was designed to be a security program... if I can't do that, then what good am I?"
    
    show hyunae bittersob
    show mute pout
    hh2 "I still think you're{w=.5}{nw}"
    
    show mute annoyed4
    show hyunae troubled with fast
    mm2 "Well, you're wrong, okay?!"
    
    show mute complain
    show hyunae sulk
    mm2 "Just shut up with your shitty platitudes!"
    
    show mute challenge
    show hyunae afraid
    hh_vn "...I wish she'd stop shouting at me..."
    
    show hyunae troubled2
    hh_vn "I'm just trying to help!"
    
    show hyunae shame
    hh_vn "I want her back to her old combative self, sure, but... not like this!"
    
    show hyunae mad blush
    hh_vn "I don't think she's worthless at all! Why won't she believe me?"
   
    show hyunae sad
    hh_vn "I just want to support her..."
    
    show hyunae sorry
    menu:
        hh_vn "...what should I do?"
        "VN":
            pass
        
        "Hug her@hyunae shy2":
            
            show hyunae sighsob
            show mute suspicious
            hh2 "I know what it's like to be scared, *Mute..."
            
            show hyunae bittersob
            show mute astonished
            hh2 "...come here."
            
            show mute abashed blush
            show hyunae hmm with fast

            scene background hateplus black 
            hide screen glow
            with Dissolve(1.0)
            $ renpy.pause(1.0)
            # HUGS *MUTE
            
            #show background hateplus xharem
            #show screen glow
            #show hyunae melancholic at hateplus_hyunae_harem_fast_left
            #show mute tch at hateplus_mute_harem_fast_left
            with Dissolve(1.0)
            hh2 "...it's fine to be scared, *Mute..."
            
            show background hateplus xharem
            show screen glow
            show hyunae sulk at hateplus_hyunae_harem_fast_left
            show mute give up at hateplus_mute_harem_fast_left
            with Dissolve(1.0)
            mm2 "...I don't...{k=1}{/k}"
            
            show hyunae lost
            show mute sob
            hh2 "You're scared. You're shocked. You've learned a lot of horrifying things over the past three days. It's traumatic, and you don't know how to deal with it."
            
            show mute insecure
            show hyunae pity
            mm2 "There's no way to deal with that! I... I..."
            
            show hyunae guilt
            show mute pout
            hh2 "You're upset. You're emotional. You're traumatized."
            
            show hyunae sad2
            show mute tired blush
            hh2 "Please trust me, *Mute. I know how you're feeling."
            
            show hyunae troubled2
            show mute worry
            hh2 "Please trust me!"
            
            show hyunae sad3
            show mute worry side
            hh2 "Let me be rational for you. Let me help you, please!"
            
            show hyunae lost
            show mute tired blush
            hh2 "You're allowed to be scared... but don't let being scared make you say things that aren't really true. Let me be objective for you."
            
            # lets go
            
            show mute worry3
            show hyunae hopelessscb with fast
            mm2 "...okay."
            
            show mute disbelief blush
            show hyunae depressed
            mm2 "...thank you, nobody's ever..."
            
            show mute tsundere
            show hyunae staresob
            mm2 "...okay. I'll try. Maybe you're right."
        
        "\"You still have a purpose\"@hyunae tough":
            
            show hyunae pressuresob with fast
            show mute doubt
            hh2 "You still have a purpose, *Mute!"
            
            show hyunae pout
            show mute disbelief
            hh2 "You can't just abandon your duty now!"
            
            show hyunae lost with fast
            show mute astonished blush
            hh2 "There's still one more daughter of the {i}Mugunghwa{/i} who needs you..."
            
            show mute insecure
            show hyunae troubled
            mm2 "...what good even am I to you?!"
            
            show mute bitter
            show hyunae lossscb with fast
            mm2 "The universe out there... it's not meant for someone like me. There's no place for someone like me. I couldn't even save the world that I came from..."
            
            show mute give up
            show hyunae sighscb
            mm2 "...what could I possibly do for someone like you?"
        
        "Yell back@hyunae suspicious2":
            
            show hyunae oops
            hh_vn "Oh, geeze... if you think that's best..."
            
            show hyunae question blush
            hh_vn "...but doing that is..."
            
            show hyunae pout with fast
            hh_vn "Practicing... just calm down..."
            
            show hyunae furious
            hh_vn "\"Just... just listen to me!\""
            
            show hyunae baffled
            hh_vn "No, that wasn't quite..."
            
            show hyunae argh
            hh_vn "\"Just listen to me, you stupid awful self-centered jerk!\""
            
            show hyunae flustered
            hh_vn "I don't think that was good either..."
            
            show hyunae give up
            hh_vn "\"Just listen to me!\""
            
            show hyunae annoyed blush
            hh_vn "...oh well... here goes nothing!"
            
            if pronouns == "he":
                show mute tch
                show hyunae oops
                mm2 "...are you done conspiring with your boyfriend yet?"
            elif pronouns == "she":
                show mute tch
                show hyunae oops
                mm2 "...are you done conspiring with your girlfriend yet?"
            else:
                show mute tch
                show hyunae oops
                mm2 "...are you done conspiring with your paramour yet?"
            
            show hyunae defensive with fast
            show mute astonished blush
            hh2 "*Mute, please, shut up! Just... please, live up to your name just this once for one single minute, and let me speak!"
            
            show mute abashed
            show hyunae sternscb
            mm2 "..." #shocked
    
    show hyunae surrender blush with fast
    show mute suspicious blush with fast
    hh2 "*Mute, the universe scares me, too."
    
    show hyunae sigh blush
    show mute sulk
    hh2 "Earth might be more like the place I dreamed of than the place I woke up in..."
    
    show hyunae bittersob
    show mute doubt blush
    hh2 "...but I'm just like you, *Mute. We grew up in the same society, learned to serve in the same royal women's quarters..."
    
    show hyunae losssob
    show mute disbelief blush
    hh2 "...I don't know how to deal with the Earth I dreamed of any better than you do!"
    
    show hyunae lost with fast
    show mute tired blush
    hh2 "I need someone who can be with me, to support me!"
    
    show hyunae pity
    show mute worry
    hh2 "I know you're scared... but I'm scared too."
    
    show hyunae bittersob with fast
    show mute pout
    hh2 "But I think if we're together, we can learn to deal with that scary barbaric universe together."
    
    show mute worry2
    show hyunae sighscb
    mm2 "I... maybe..."
    
    show mute upsetscb with fast
    show hyunae bitterscb
    mm2 "But... why? Why would you even trust me like this? Why do you care so much about a failure of a security program like me, that never did anything for you?"
    
    show hyunae hmmsob
    show mute hmphscb
    hh2 "Because..."
    
    show hyunae oops with fast
    hh_vn "Aaaaaaa, geeze, I can't tell her the truth..."
    
    show hyunae baffled
    hh_vn "That would be too forward... and she'd never accept it!"
    
    show hyunae enthusiastic blush
    menu:
        hh_vn "What do I say, what do I say?"
        "VN":
            pass
        
        "\"Because!\"@hyunae cautious2":
            
            show hyunae flustered with fast
            show mute whatscb
            hh2 "Because... because... because!"
            
            show hyunae pout
            show mute wowscb
            hh2 "Just because!"
        
        "\"Because of what we read about Old *Mute\"@hyunae insist":
            
            show hyunae grumpy with fast
            show mute upsetsc
            hh2 "I've learned a lot about you over the past three days. I know what kind of person you used to be..."
            
            show hyunae pressuresob
            show mute sighscb
            hh2 "...and maybe I have complicated feelings, but I know you're good, and have always stood up for what you believe in!"
        
        "\"It's a S E C R E T\"@hyunae cautious":
            
            show hyunae satisfied blush with fast
            show mute whatsob
            hh2 "Sorry... it's a S E C R E T !"
            
            show hyunae hardsob
            show mute whatscb
            hh2 "You'll just have to trust me! I've learned a lot about you over the past three days."
    
    show mute wowso
    show hyunae hardscb
    mm2 "Okay, okay..."
    
    show mute hmm2
    show hyunae staresob
    mm2 "What do I have to lose?"
    
    show mute whatever
    show hyunae starescb
    mm2 "I'll... I'll believe in you."
    
    show mute heh2 with fast
    show hyunae evasive
    mm2 "I'm still *Mute, AI in charge of the {i}Mugunghwa{/i}'s security operations. I still have a job to do..."
    
    show hyunae calmsob
    show mute shy2
    hh2 "*Mute..."
    
    show mute embarrassed
    show hyunae sweetscb
    mm2 "So... even if I'm scared... even if I don't know what to do... even if I've failed so many times before..."
    
    show mute tsundere
    show hyunae surescb
    mm2 "...I'll give it a shot, *Hyun-ae."
    
    show hyunae genki with fast
    show mute smile blush
    hh2 "Thank you! Thank you, thank you!"
    
    show hyunae embarrassed
    hh_vn "And thank you for helping!"
    
    show hyunae funsob with fast
    show mute shy
    hh2 "Let's finish reading these all together, then."
    
    show mute heh
    show hyunae funscb
    mm2 "Okay."
    
    show mute brag blush
    show hyunae calm2 with fast
    mm2 "That's something I can do."
    
    show hyunae happy
    show mute proud
    
    jump hateplus_harem_slow_loop


label hateplus_xharem_true_feelings:

    play music HATEPLUS_HYUNAE_CHEER fadeout 3.0 fadein 5.0 loop if_changed
    
    show hyunae enthusiastic blush
    show mute suspicious blush
    hh2 "I think... I think it's time for another break. We're almost near the end, so..."
    
    show mute disbelief blush
    show hyunae look
    mm2 "Okay..."
    
    show mute doubt blush
    show hyunae huh
    mm2 "Like, what did you want to talk about?"
    
    show hyunae awkward
    show mute neutral3
    hh2 "Well, it's..."
    
    show hyunae hmm2
    show mute look
    hh2 "I feel like..."
    
    show hyunae tsundere
    show mute astonished blush
    hh2 "...um, sorry, could I have a moment to talk to the Investigator?"
    
    show mute disbelief
    show hyunae insist
    mm2 "Okay, sure..."
    
    show mute think
    show hyunae sure blush with fast
    hh_vn "*Mute seems to be doing better than before... I'm really glad!"
    
    show hyunae sigh blush
    hh_vn "It was awful, seeing someone as strong and abrasive as her, reduced to such a wreck..."
    
    show hyunae bitter
    hh_vn "And... what would have happened if I wasn't there for her last night? She'd be dead..."
    
    show hyunae sad3 with fast
    hh_vn "I don't even want to think about it!"
    
    show hyunae bittersob
    show mute neutral3
    hh2 "Hey, *Mute, um..."
    
    show hyunae sternsob
    show mute astonished blush
    hh2 "You've been in love before, right?"
    
    show mute tsundere
    show hyunae hmmscb
    mm2 "Uh... yeah, of course. I'm still a woman!"
    
    show hyunae hmph2
    show mute sulk
    hh2 "Right, right..."
    
    show mute whatever with fast
    show hyunae huhscb
    mm2 "Wait, is this about Old *Mute, having Heo Seo-yeong be in love with her?"
    
    show hyunae hmph3
    show mute wowscb
    hh2 "Um... maybe, a little bit."
    
    show hyunae question with fast
    hh_vn "...tangentially, I suppose..."
    
    show mute damn
    show hyunae starescb
    mm2 "Well... I mean... I've been in love with men, okay? Nothing weird like that! I've never charmed any woman like that, that would be... that wouldn't make sense!"
    
    show hyunae awkward with fast
    show mute doubt blush
    hh2 "I see..." # blushing
    
    show mute abashed blush
    show hyunae hmmccb with fast
    mm2 "I'm not like that! And I mean, it's not like Old *Mute reciprocated, either, come to think of it... I mean, how could she?"
    
    show hyunae hmmsob
    show mute suspicious blush
    hh2 "Well..."
    
    show hyunae wow with fast
    hh_vn "Oh, geeze, does she think that {i}I'm{/i} in love with her?!"
    
    show hyunae tsundere
    hh_vn "Oh geeze, oh geeze, oh geeze..."
    
    show hyunae hmm2
    hh_vn "...I need to calm down. I'm sure she doesn't."
    
    show hyunae sternsob with fast
    show mute shy
    hh2 "So, um... did you ever fall in love first, or was it... um, the man who made the first move?"
    
    show mute tsundere
    show hyunae hmmscb
    mm2 "Uh, of course it's the man who makes the first move! Like, it's better that way."
    
    show mute enthusiastic blush
    show hyunae hopelessscb
    mm2 "Even if it wasn't improper, men don't really want that, anyway... that's just how things are, okay?"
    
    if pronouns != "she":
        
        show mute wow3 with fast
        show hyunae starescb
        mm2 "Oh no, this isn't about the Investigator, is it? You're not asking me for advice about [them], are you...?"
        
        show hyunae pout
        show mute hmm blush
        hh2 "No! No, of course not! Geeze...!"
        
        show mute wow
        show hyunae hmph
        mm2 "Okay... just checking..."
    
    show mute tensescb with fast
    show hyunae sighscb
    mm2 "Well, there was one time where I fell in love with someone, and when I tried to tell him... well, it was unrequited, okay?"
    
    show hyunae hardsob
    show mute hmm blush
    hh2 "What was he like?"
    
    show mute embarrassed with fast
    show hyunae surrender blush
    mm2 "...I'd, um, rather not say..."
    
    if read("M6-2"):
        
        show hyunae depressed blush
        show mute suspicious blush
        hh2 "How bad can it be? Worse than Old *Mute's first love?"
        
        show mute heh2
        show hyunae sighscb
        mm2 "Well, he didn't have any disgusting-sounding habits like smoking, anyway, but... still..."
    
    show hyunae hmmcob
    show mute look blush
    hh2 "\"One does not prefer to acknowledge the mistakes of one's youth\"?"
    
    show mute heh
    show hyunae hopelessscb
    mm2 "Sure, I guess."
    
    show hyunae unsure with fast
    hh_vn "I'm just babbling. Babbling doesn't help me any, I know...!"
    
    show hyunae sulk2
    hh_vn "I just feel like..."
    
    show hyunae melancholic
    hh_vn "Reading about Old *Mute..."
    
    if hateplus_mute_old_mute_bitch == "bitch":
        show hyunae mad
        hh_vn "I know you think she's a bitch, but..."
    elif hateplus_mute_old_mute_bitch == "complex":
        show hyunae question blush
        hh_vn "I know you think she's complex, but..."
    else:
        show hyunae enthusiastic blush
        hh_vn "I know you feel the same way as me about her!"
    
    show hyunae tough2
    hh_vn "For all her faults, she was still really cool. She fought really hard for what she believed in! She was stubborn, and tough, and honest!"
    
    show hyunae mad2
    hh_vn "I still resent her for failing me... and... I don't know, the *Mute we know can be so judgemental, too..."
    
    show hyunae pity
    hh_vn "...but..."
    
    show hyunae apologize blush
    hh_vn "She's admirable in a lot of ways, isn't she?"
    
    show hyunae touched
    hh_vn "Judging by how Old *Mute was... I know she could be really really great!"


label hateplus_xharem_true_feelings_question:
    
    show hyunae enthusiastic blush with fast
    menu:
        hh_vn "...but what do I say to her?"
        "VN":
            pass
            
        "Tell her how you feel@hyunae shy2":
            
            show hyunae wow
            hh_vn "Right..."
            
            show mute neutral with fast
            show hyunae emo with fast
            hh2 "*Mute... um..."
            
            show hyunae hardsob
            show mute doubt blush
            hh2 "*Mute, I like you!"
            
            show mute heh2
            show hyunae huhscb
            mm2 "Okay... good to hear...?"
            
            show mute doubt
            show hyunae baffled with fast
            hh_vn "...she didn't get it..."
        
        "Nothing@hyunae unsure":
            
            show hyunae annoyed blush with fast
            hh_vn "I can't just say nothing!"
            
            show hyunae sigh blush
            hh_vn "It would be the easy thing to do... it's the thing I have the most practice doing."
            
            show hyunae flustered2
            hh_vn "...I can't do that!"
            
            jump hateplus_xharem_true_feelings_question
        
        "Speak from the heart!@hyunae shy":
            
            show hyunae spirited
            hh_vn "You're right! That's the thing to do! I just need to be honest with her!"
            
            show mute suspicious
            show hyunae bittersob with fast
            hh2 "*Mute, I... I just want you to know..."
            
            show hyunae pout
            show mute doubt blush
            hh2 "...maybe you won't understand, but I really feel this strongly..." # *Mute puzzled
            
            show hyunae defensive
            show mute astonished blush
            hh2 "*Mute, I'm in love with you!"
            
            show mute give up
            show hyunae huhscb
            mm2 "...ugh, geeze, don't mess around with me like that, okay?"
            
            show mute annoyed3
            show hyunae depressed blush
            mm2 "It's not funny! I don't have any patience for jokes."
            
            show mute challenge
            show hyunae mad blush with fast
            hh_vn "Aaaaaaa, geeze, after I said something that embarrassing... she doesn't even believe me?!"
            
            show hyunae oops
            hh_vn "...I thought if I just confessed, that would be the hard part, but..."
            
            show hyunae baffled
            hh_vn "...she didn't even take me seriously..."
    
    show hyunae afraid
    menu:
        hh_vn "What do I do?"
        "VN":
            pass
        
        "Tell her how you feel@hyunae insist":
            
            show hyunae serious blush
            hh_vn "Right... I just need to be direct about it."
            
            show hyunae spirited
            hh_vn "I'll tell her the honest truth! She likes honesty!"
            
            show hyunae hardsob with fast
            show mute tch
            hh2 "Really... I like you! I {i}like{/i} like you!"
        
        "Nothing@hyunae anxious":
            
            show hyunae pity
            hh_vn "...yeah, I don't know what else I could say..."
            
            show mute suspicious
            show hyunae sad
            hh2 "..." # sad looking
            
            show mute disbelief
            show hyunae troubled
            mm2 "What's wrong?"
            
            show hyunae sad2
            show mute suspicious
            hh2 "...I don't know what to say, *Mute..."
        
        "Speak from the heart!@hyunae tough":
            
            show hyunae serious blush
            hh_vn "Right! I just need to make sure she understands!"
            
            show hyunae sigh blush with fast
            hh_vn "...even though I don't really understand my feelings myself..."
            
            show hyunae flustered2
            hh_vn "Still!"
            
            show mute sulk
            show hyunae pressuresob
            hh2 "I'm in love with you, *Mute! Please, don't just dismiss me... I'm serious!"
    
    show mute wow2 with fast
    show hyunae sulk with fast
    mm2 "Wait, you mean... you seriously..."
    
    show mute whatsob
    show hyunae gomen
    mm2 "You feel about me... like {i}that?!{/i}"
    
    show hyunae funsob with fast
    show mute astonished blush with fast
    hh2 "Yes!"
    
    show mute insecure
    show hyunae huhscb
    mm2 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA—{w=.5}{nw}"
    
    show mute damn
    show hyunae huh with fast
    mm2 "—AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA—{w=.5}{nw}"
    
    show mute give up
    show hyunae grr
    mm2 "—AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!{w=.5}{nw}"
    
    show mute abashed blush
    show hyunae hardscb with fast
    mm2 "Oh GEEZE."
    
    show mute upsetscb with fast
    show hyunae sternscb
    mm2 "I... I'm a woman, *Hyun-ae! I'd never even..."
    
    show mute sighsob
    show hyunae bitterscb
    mm2 "...I'd never even..." # blushes profusely
    
    show mute whatever
    show hyunae huhscb
    mm2 "...I'd never even consider something like that!"
    
    show hyunae losssob
    show mute hmphscb
    hh2 "Oh..."
    
    show mute serious
    show hyunae baffled with fast
    hh_vn "That's what I was afraid she'd say..."
    
    show hyunae unsure
    hh_vn "I mean, it's not as if she's the type of person who'd just open up immediately to me, and be able to look at a girl the way I look at her..."
    
    show hyunae pity
    hh_vn "...maybe it's just impossible..."
    
    show hyunae baffled
    hh_vn "...ugh, geeze, I really hope I didn't scare her..."
    
    show mute tensescb
    show hyunae starescb with fast
    mm2 "...but, um... like, can I ask what it is you see in me?"
    
    show hyunae hmmcob
    show mute hmphscb
    hh2 "Um... I... well..."
    
    show hyunae tsundere with fast
    hh_vn "Was... was she just being tsuntsun? Is this my chance...?"
    $ hateplus_admirable = hateplus_cute = False


label hateplus_xharem_true_feelings_question2:
    
    if hateplus_admirable and hateplus_cute:
        
        show hyunae mad blush
        menu:
            hh_vn "But what do I say?"

            "VN":
                pass
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
    
    elif hateplus_admirable:
        
        show hyunae really
        menu:
            hh_vn "But what do I say?"

            "VN":
                pass
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
            
            "\"You're really cute!\"@hyunae shy2":
                jump hateplus_xharem_true_feelings_cute
    
    elif hateplus_cute:
        
        show hyunae unsure
        menu:
            hh_vn "But what do I say?"

            "VN":
                pass
            
            "\"You're really admirable!\"@hyunae tough":
                jump hateplus_xharem_true_feelings_admirable
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
    else:
        show hyunae wow
        menu:
            hh_vn "But what do I say?"

            "VN":
                pass
            
            "\"You're really admirable!\"@hyunae tough":
                jump hateplus_xharem_true_feelings_admirable
            
            "\"Anything that comes to mind!\"@hyunae insist":
                jump hateplus_xharem_true_feelings_anything
            
            "\"You're really cute!\"@hyunae shy2":
                jump hateplus_xharem_true_feelings_cute


label hateplus_xharem_true_feelings_cute:
    $ hateplus_cute = True
    
    show hyunae funsob with fast
    show mute doubt blush with fast
    hh2 "I... I think you're really cute!"
    
    show mute disbelief blush
    show hyunae surescb
    mm2 "Oh... that's it...?"
    
    show mute enthusiastic blush
    show hyunae huhscb
    mm2 "I mean, my appearance... well, you have the same base code, you know how it works! This is just how the original Princess Ryu looked, but 2D."
    
    show mute think2
    show hyunae hmmscb
    mm2 "Down to the outfit, even..."
    
    show mute heh
    show hyunae hopelessscb
    mm2 "...Queen Eun-a told me she looked like this when she was young, but... I guess that was probably a lie, too."
    
    show mute heh2
    show hyunae oops with fast
    mm2 "So really, what you're saying is just, like, who you find cute is the daughter of the woman who betrayed me..."
    
    show hyunae mad blush with fast
    hh_vn "Ah, geeze, that made it worse... I didn't mean to remind her of that!"
    
    show mute suspicious blush
    show hyunae flustered3 with fast
    hh2 "No, no!"
    
    show hyunae flustered
    show mute neutral3
    hh2 "I think you're cute because... um..."
    
    show hyunae hardsob
    show mute doubt blush
    hh2 "I like the way you talk! You're really bold and honest, and you say things like \"okay!\" a lot! That's really cute!"
    
    show mute tch
    show hyunae staresc
    mm2 "I don't say that a lot, okay?"
    
    show mute abashed blush
    show hyunae heh
    mm2 "...oh."
    
    show hyunae gomen
    show mute sulk
    hh2 "Aheh."
    
    show hyunae hmph2 with fast
    show mute suspicious blush
    hh2 "I don't think you're being fair about your appearance, either..."
    
    show hyunae pout
    show mute astonished blush
    hh2 "Look at me! I always wanted to be tall and have long legs and stylish glasses and... um... well, big boobs..."
    
    show hyunae emo
    show mute doubt blush
    hh2 "...that's just how I want to be seen... it makes me feel like I have some sort of control."
    
    show hyunae hard
    show mute disbelief blush
    hh2 "Meanwhile... you're not afraid to present yourself as little."
    
    show hyunae annoyedsob
    show mute sulk
    hh2 "And I know right now that isn't even your normal height! You're actually scaling yourself down to make yourself take up less space next to me!"
    
    show mute tensescb with fast
    show hyunae hardscb
    mm2 "...oh, geeze, you noticed {i}that{/i}...?"
    
    show mute hmphsob
    show hyunae bitterscb
    mm2 "What does that even matter, anyway?"
    
    show hyunae grumpy
    show mute whatscb
    hh2 "Well... you know... even though you say you look just like Princess Ryu did... that's not really true, is it? She had natural black hair!"
    
    show mute what
    show hyunae hmmscb
    mm2 "...I, um... well, like... I couldn't change that! It's the default, it doesn't change!"
    
    show mute serious
    show hyunae oops with fast
    hh_vn "I'm not really hitting on anything that works, am I... geeze, why am I so useless at this?!"
    
    show hyunae baffled
    hh_vn "I always thought if I just had someone to confess to, it'd be perfect... but it's actually really really hard!"
    
    show hyunae cautious
    hh_vn "...wait! Did she just say...?"
    
    show hyunae spirited
    hh_vn "Aha, I've got her!"
    
    show hyunae annoyedso with fast
    show mute shy with fast
    hh2 "Is that what you told Queen Eun-a, that you weren't able to change your gold hair to something natural?"
    
    show mute embarrassed
    show hyunae sternscb
    mm2 "Yeah, of course..."
    
    show hyunae sternsob
    show mute astonished blush
    hh2 "Old *Mute was able to change hers to white."
    
    show mute damn
    show hyunae satisfied blush
    mm2 "Aaaaaaaa!"
    
    show mute upsetsob with fast
    show hyunae hardscb
    mm2 "Well... so what?!"
    
    show hyunae bittersob
    show mute wowscb
    hh2 "You don't have to pretend, *Mute. I understand."
    
    show mute tensesob
    show hyunae bitterscb
    mm2 "Well..."
    
    show mute tch with fast
    show hyunae hopelessscb
    mm2 "...well..."
    
    show mute annoyed3
    show hyunae huhscb
    mm2 "...even if you do think I'm... tch, \"cute\"... that's not love! That's just infatuation!"
    
    show hyunae oops with fast
    show mute challenge
    hh2 "I, um..."
    
    jump hateplus_xharem_true_feelings_question2


label hateplus_xharem_true_feelings_admirable:
    $ hateplus_admirable = True
    
    show hyunae hardsob with fast
    show mute wowscb with fast
    hh2 "I think you're really admirable!"
    
    show hyunae bittersob
    show mute whatscb
    hh2 "You always speak your own mind, even if it hurts..."
    
    show hyunae grumpy
    show mute hmm blush
    hh2 "You take the things that are important to you really seriously! You have really strong principles!"
    
    show mute sorrysob
    show hyunae hardscb
    mm2 "...well, I guess, when you put it that way..."
    
    show mute upset2
    show hyunae lossscb
    mm2 "...but it's not as if they added up to anything, in the end."
    
    show mute tired blush
    show hyunae oops with fast
    hh_vn "Oh no, geeze, she's not getting depressed again, is she..."
    
    show hyunae defensive with fast
    show mute sorryscb
    hh2 "I know you still did a lot of good!"
    
    show hyunae hmmcob
    show mute whatscb
    hh2 "How do you think Princess Ryu would have turned out without you in her life?"
    
    show mute abashed with fast
    show hyunae hmphscb
    mm2 "...oh, geeze... okay, okay, not very good."
    
    show mute embarrassed
    show hyunae starescb
    mm2 "I guess I can take some credit for being there for her..."
    
    show hyunae sure2
    show mute proud
    hh2 "Right!"
    
    show mute talk3
    show hyunae staresc
    mm2 "But... what's with the sudden change of heart? I thought you didn't agree with me, I thought you hated my principles... the principles that the new dynasty was founded on."
    
    show mute tenseso with fast
    show hyunae hmphscb
    mm2 "You know I still stand by all that, right?"
    
    show mute challengeso
    show hyunae hmmccb
    mm2 "Just because Queen Eun-a lied to me... just because she did terrible things... doesn't mean I don't still believe in Emperor Taejo's dream of people being in harmony."
    
    show mute annoyed with fast
    show hyunae question blush with fast
    hh_vn "I don't like that, of course... and I wish she'd see it my way... it's not harmony, it just sucks!"
    
    show hyunae baffled
    hh_vn "But that isn't what's important anymore."
    
    show hyunae mad blush
    hh_vn "Now I just want to show her how the world I came from isn't as bad as it seems... that it's not \"barbaric.\""
    
    show hyunae tough2
    hh_vn "I want her to be in a world that'll let her be as brash and assertive as she needs to be!"
    
    show hyunae annoyedsob with fast
    show mute challenge
    hh2 "I didn't have a change of heart."
    
    show mute annoyed4
    show hyunae annoyedscb
    mm2 "Then... what?"
    
    show hyunae hard
    show mute suspicious
    hh2 "I've seen what a person like you can become!"
    
    show mute complain
    show hyunae hmmccb
    mm2 "Old *Mute? I don't want to be like her! She's... she was over-controlling and stupid and rude and all those things got her killed!"
    
    show hyunae bittersob
    show mute challenge
    hh2 "That's not what I mean!"
    
    show hyunae pout
    show mute annoyed
    hh2 "What I mean is..."
    
    show hyunae sternsob
    show mute serious
    hh2 "Um, well, you'd say you're both very different, right?"
    
    show mute challengeso with fast
    show hyunae hmph
    mm2 "Yes! We're nothing alike, okay?!"
    
    show hyunae annoyedsob
    show mute whatscb
    hh2 "That's not true! You're alike in a lot of ways!"
    
    show hyunae grumpy
    show mute tensescb
    hh2 "You both always say how you feel. You both believe in protecting weaker people. You both have a really direct way of talking."
    
    show hyunae bittersob
    show mute sulk with fast
    hh2 "You both believe in family, you both believe in love, you both believe in stability..."
    
    show hyunae pressuresob
    show mute tch
    hh2 "You came from two very different times, yes, but... you both believe in the same things!"
    
    show mute annoyed4
    show hyunae bitterscb
    mm2 "...well, okay, but... we're still, like, totally different. Maybe you have a crush on her, but... that's not me, okay?!"
    
    show hyunae bittersob
    show mute challenge
    hh2 "Geeze, that's not what I mean...!"
    
    show hyunae hardsob
    show mute doubt blush
    hh2 "What I mean is that no matter what, even under different circumstances, you're still always good!"
    
    show hyunae annoyedsob
    show mute disbelief blush
    hh2 "Being good is just an intrinsic part of you!"
    
    show hyunae emo
    show mute pout
    hh2 "Even if I don't agree with a lot of the things you think... I still admire you!"
    
    show mute sigh blush
    show hyunae hopelessscb
    mm2 "Oh..."
    
    show mute worry3
    show hyunae hmmscb
    mm2 "I, um..."
    
    show mute shame
    show hyunae staresc
    mm2 "...well, thank you, but..."
    
    show mute disbelief
    show hyunae huhscb
    mm2 "I'm happy to be a role model! But that isn't the same as love, okay?"
    
    show hyunae oops with fast
    show mute serious
    hh2 "But..."
    
    jump hateplus_xharem_true_feelings_question2


label hateplus_xharem_true_feelings_anything:
    
    show hyunae hmm2 with fast
    hh_vn "Is that really such a good idea...? I should think it through..."
    
    if not hateplus_cute or not hateplus_admirable:
        jump hateplus_xharem_true_feelings_question2
    
    show mute damn with fast
    show hyunae huh
    mm2 "Ugh, stop just going behind my back! What were you going to say?!"
    
    show hyunae flustered with fast
    show mute annoyed
    hh2 "I, um... well..."
    
    show mute scorn
    show hyunae depressed blush
    mm2 "Yes?"
    
    show hyunae pout
    show mute challenge
    hh2 "I just..."
    
    show mute mad
    show hyunae hmphscb
    mm2 "{i}What?!{/i}"
    
    show hyunae flustered3
    show mute doubt blush
    hh2 "I... I know things are tough for you... and I know Earth is going to be really strange and confusing..."
    
    show hyunae grumpy
    show mute disbelief blush
    hh2 "So when you're feeling sad, I want to be there with you!"
    
    show hyunae bittersob
    show mute astonished blush
    hh2 "I want to give you reassuring hugs, and when you're feeling hopeless, I want to brush your hair and make sure you understand that everything will be fine!" # *Mute shocked
    
    show mute abashed blush
    show hyunae bitterscb
    mm2 "That's..."
    
    show hyunae defensive
    show mute tch
    hh2 "Please, let me finish, I'm not done!"
    
    show mute give up
    show hyunae defensivescb
    mm2 "...okay..."
    
    show hyunae annoyedsob
    show mute doubt blush
    hh2 "I want to be there at your side! I want to be the older sister who helps keep you stable when we're both scared of the world!"
    
    show hyunae emo
    show mute suspicious blush
    hh2 "Because there's one thing I know in my heart..."
    
    show hyunae sigh blush
    show mute sulk
    hh2 "...I just know it, for sure..."
    
    show hyunae hardsob
    show mute disbelief blush
    hh2 "...no matter how scary things get, it's always better to face them with someone you like holding your hand!"
    
    show hyunae bittersob
    show mute tch
    hh2 "That's what I believe!"
    
    show mute tensesob with fast
    show hyunae hardscb
    mm2 "Are you done?"
    
    show hyunae hmmcob
    show mute hmphscb
    hh2 "Yeah..."
    
    show mute upsetscb
    show hyunae hopelessscb
    mm2 "Well, like..."
    
    show mute abashed blush with fast
    show hyunae huhscb
    mm2 "You? How could you {i}possibly{/i} be the older sister type?! I'm 312 years old, to look up to you for emotional support would be..."
    
    show hyunae oops with fast
    show mute doubt blush
    hh2 "Um... you know I'm way older than you, right? I'm over twice your age! I'm 640 years old, you know."
    
    show mute damn
    show hyunae grr
    mm2 "You can't count the gap like that!"
    
    show hyunae baffled
    show mute astonished
    hh2 "Um, sure I can... I was awake the whole time, all 622 years of it!"
    
    show mute give up
    show hyunae hardscb with fast
    mm2 "...ugh, I guess you're right... but I was activated in 2390! That's vastly before your time!"
    
    show hyunae defensive
    show mute tch
    hh2 "That doesn't count! I thought you said you weren't Old *Mute!"
    
    show mute complain
    show hyunae pressurescb
    mm2 "I'm still older, is my point!"
    
    show hyunae give up
    show mute serious
    hh2 "That doesn't count! Geeze..."
    
    show hyunae sternsob
    show mute annoyed
    hh2 "...besides, I was born on August 30, 2415! Geeze, 25 years is not vastly before my time!"
    
    show mute annoyed4
    show hyunae sternscb
    mm2 "You were asleep for all of it!"
    
    show hyunae pout
    show mute challenge2
    hh2 "You were a totally different person for all of it!"
    
    show mute abashed blush
    show hyunae bitterscb
    mm2 "Well... um..."
    
    show hyunae flustered3
    show mute pout
    hh2 "Geeze, just count it properly. I'm 640, and you're 312. I'm older!"
    
    show mute bitter
    show hyunae sternscb
    mm2 "Tch, fine..."
    
    show mute sigh blush
    show hyunae gomen with fast
    mm2 "...I guess it's a welcome change not being the oldest woman around, anyway."
    
    show mute insecure
    show hyunae huh
    mm2 "I... I still don't accept your feelings, though!"
    
    show mute upsetsob with fast
    show hyunae hmphscb with fast
    mm2 "Even if you're old enough to be like an older sister to me, I don't accept that you're in love with me... I'm not okay with that!"
    
    show hyunae sigh blush
    show mute hmphscb
    hh2 "...fine...{k=1}{/k}"
    
    show hyunae surrender blush
    show mute hmm blush
    hh2 "...I understand..."
    
    show hyunae sad with fast
    show mute wowsc
    hh2 "Let's just get back to work, then..."
    
    show mute disbelief with fast
    show hyunae anxious
    mm2 "Okay..."
    
    show mute embarrassed
    show hyunae grr
    mm2 "...but, um..."
    
    show mute heh2
    show hyunae huhscb with fast
    mm2 "...you know, if I have to get a body on Earth, like..."
    
    show mute tsundere
    show hyunae staresob
    mm2 "...maybe if you helped me with my hair... maybe that would be okay...?"
    
    show hyunae sweetsob
    show mute sulk
    hh2 "Ah!"
    
    show hyunae gomen with fast
    hh_vn "So she really is just tsuntsun...!"
    
    show hyunae funsob with fast
    show mute shy
    hh2 "Accepted~!"
    
    show mute whatsob with fast
    show hyunae heh
    mm2 "Geeze, don't get so excited about that...!"
    
    show mute inquisitive2
    show hyunae genki with fast
    mm2 "Let's just get back to work, okay?!"
    
    show hyunae spirited
    show mute sulk
    hh2 "Okay~ {font=DejaVuSans.ttf}{plain}{size=+8}\u2606{/size}{/plain}{/font}"
    
    show hyunae smile blush
    show mute think
    
    jump hateplus_harem_slow_loop


label hateplus_xharem_back_to_earth:

    play music HATEPLUS_BICKER fadeout 3.0 fadein 3.0 loop if_changed
    
    show hyunae enthusiastic blush
    show mute think
    hh2 "Well... that's all there is to read before we return to Earth, I suppose."
    
    show mute talk
    show hyunae cautious2
    mm2 "Yep, that's everything."
    
    show hyunae spirited
    show mute doubt blush
    hh2 "So, um, thank you, [title]Investigator, for letting us play your sidekicks!"
    
    show mute abashed blush
    show hyunae gomen
    mm2 "...speak for yourself! I just wanted to find out what happened, that's all!"
    
    show mute tsundere
    show hyunae calm2
    mm2 "And... well... like, I learned a lot, that's for sure..."
    
    show mute worry2
    show hyunae starescb with fast
    mm2 "...but, um... *Hyun-ae...?"
    
    show hyunae hopelessso
    show mute worry
    hh2 "Yes?"
    
    show mute sighsob with fast
    show hyunae staresob
    mm2 "...I'm, um... kinda glad you were here for me, today."
    
    show mute whatever
    show hyunae sweetscb
    mm2 "Having you there to support me... um, well, it was good."
    
    show hyunae genki with fast
    show mute hmm blush
    hh2 "Ahh... of course! Thank you so much for saying that!"
    
    show hyunae spirited2
    show mute tsundere with fast
    mm2 "Okay, okay, let's not make a big deal of it... let's just move on. Earth's not far away!"
    
    show hyunae apologize blush
    show mute shy
    hh2 "I know I've learned a lot over the past three days, too."
    
    show hyunae touched
    show mute pout
    hh2 "It's been difficult for me, too... I don't know what to feel, all of this has been so sudden..."
    
    show hyunae satisfied blush with fast
    show mute look blush
    hh2 "But... thanks for rescuing me, again."
    
    show mute polite blush with fast
    show hyunae staresob
    mm2 "Yeah, thanks, [title]Investigator."
    
    show hyunae evasive
    show mute wowscb
    hh2 "I, um... I actually meant you, *Mute!"
    
    show hyunae hmph2
    show mute whatscb
    hh2 "It was your decision to take me with you, remember?"
    
    show mute heh2 with fast
    show hyunae hardscb
    mm2 "Oh, um... like, I guess so."
    
    show hyunae bittersob
    show mute doubt blush
    hh2 "Please don't say \"I guess so!\" That was one of the most important decisions of my life... I'm trying to be grateful!"
    
    show hyunae touched with fast
    show mute sulk
    hh2 "When you came for me, when you didn't have to... that was the first moment I knew you were actually really good after all!"
    
    show hyunae calm
    show mute astonished blush
    hh2 "Really, that was when I fell in love for the first{w=.5}{nw}"
    
    show mute insecure
    show hyunae gomen
    mm2 "OKAY, NO NEED TO FINISH THAT SENTENCE, THAT'S ENOUGH OF THAT."
    
    show mute damn
    show hyunae flirt2
    mm2 "Look, there's no need to be all dramatic here, okay? No big trite speeches about personal growth or whatever... we're going to be able to talk on Earth pretty soon!"
    
    show mute give up
    show hyunae calm2
    mm2 "There's star system entry procedures and stuff that we really need to get busy with."
    
    show hyunae sure2 with fast
    show mute challenge
    hh2 "Yes, *Mute..."
    
    show hyunae confident
    hh_vn "I'm really happy, though..."
    
    show hyunae smile2 with fast
    hh_vn "Everything worked out completely perfectly!"
    
    show hyunae calm
    hh_vn "There was an easy solution to everything, we both got the girl, nobody got hurt..."
    
    show hyunae genki
    hh_vn "...and nothing in the past really had any sort of consequence, in the end!"
    
    show hyunae touched
    hh_vn "I just love a perfectly happy ending... this is what I always dreamed of, and I guess dreams can come true after all!"

    show hyunae spirited
    hh_vn "Alright, what's the big dramatic concluding line we're going to end on? It should be good, so you can screencap it for posterity!"
    
    show hyunae cheer
    menu:
        hh_vn "What should I do?"
        "VN":
            pass
        
        "\"Talk about hate\"@hyunae enthusiastic2":
            
            show hyunae heh
            show mute evil
            hh2 "{font=DejaVuSans.ttf}{plain}{size=+8}♥{/size}{/plain}{/font} Let's look forward to our hateful days together~! {font=DejaVuSans.ttf}{plain}{size=+8}♥{/size}{/plain}{/font}"
        
        "\"Talk about analogue\"@hyunae tough":
            
            show hyunae challenge
            show mute sulk
            hh2 "Just think, how nice will it be to have a body again? Living inside a computer, being a piece of digital software... I don't like it."
            
            show hyunae spirited with fast
            show mute serious
            hh2 "I mean, digital's fine, I suppose, if you don't know any better... but analogue is way better!"
        
        "\"Just kiss her!\"@hyunae shy2":
            
            show hyunae flirt
            hh_vn "Yeah, that's a perfect thing to end with! A kiss! How romantic~"
            
            show hyunae heh with fast
            show mute astonished blush
            hh2 "Hey, little sister *Mute, I...{w=.5}{nw}"
            
            show mute mad:
                easeout .5 xoffset 40 yoffset 10
                easein .2 yoffset 0 xoffset 60
            show hyunae sweetscb
            mm2 "NO, GEEZE, GET AWAY FROM ME!"
            
            show hyunae genki:
                easeout .2 xoffset 40 yoffset 10
                easein .2 yoffset 0 xoffset 60
                easeout .2 xoffset 80 yoffset 10
            show mute worry2:
                easeout .3 xoffset 100 yoffset 10
                easein .2 yoffset 0 xoffset 120
                easeout .2 xoffset 160 yoffset 10

            $ renpy.pause(.5)
            
    $ store.hateplus_use_ending = "harem"
    $ persistent.hateplus_day = 3

    jump hateplus_end


label log_1_1_xharem:
    if scrolled(7, korean=7):
        show hyunae emo2 with fast
        show mute tensesob with fast
        $ ts("*Mute!", "Yes, I see...")
        # Gotta make a branch if player has first seen *Mute in another log (thought that means every logs with *Mute in it has to have a line where *Hyun-ae first sees *Mute--ouch) - Raide
    elif scrolled(19, korean=19):
        show mute wowsob with fast
        show hyunae hmmsc with fast
        ms "Wait, what...?"
    elif scrolled(27, korean=27):
        show hyunae hmmsob with fast
        show mute upset2 with fast
        $ ts("How is that a crisis...?", "She makes more money than her husband?!")
    elif scrolled(35, korean=34): # immediately after
        show hyunae huh with fast
        show mute damn with fast
        $ ts("...um, what's wrong with that, *Mute?", "...{i}that's{/i} your criticism, *Hyun-ae?!")
    elif scrolled(43, korean=41):
        show hyunae hmmcob with fast 
        show mute hmphsob with fast
        $ ts("Geeze...", "Geeze...")
    elif scrolled(55, korean=54):
        show hyunae staresc with fast
        show mute whatscb with fast
    elif scrolled(63, korean=64):
        show mute wowso with fast
        show hyunae hardsc with fast
        ms "Wow..."
    elif scrolled(71, korean=72):
        show hyunae emo with fast
        show mute hmphscb with fast
        hs "Scary..."
    elif scrolled(88, korean=89):
        show mute tch with fast
        show hyunae hmmccb with fast
        ms "Worse than scary, disrespectful!"
    elif scrolled(1000):
        show mute disbelief blush with fast
        show hyunae neutral with fast
        ms "...like, women conspiring like this, makes me feel uneasy..."

    jump log_loop

label log_1_2_xharem:
    if scrolled(8, korean=7):
        show mute tensesob with fast
        show hyunae hmmcob with fast
        $ ts("...well, yeah, but...", "...she's an AI, there's no excuse for leaving men waiting like that!", True)
    elif scrolled(18, korean=19):
        show hyunae annoyedsc with fast
        show mute whatscb with fast
    elif scrolled(28, korean=28):
        show hyunae annoyedsc with fast
        show mute tensesc with fast
    elif scrolled(34, korean=34):
        show hyunae hmph2 with fast
        show mute tensesc with fast
    elif scrolled(44, korean=44):
        show mute wowsob with fast
        show hyunae huhscb with fast
        ms "Public demonstrations? Whoa..."
    elif scrolled(65, korean=67):
        show hyunae hardsc with fast
        show mute whatscb with fast
    elif scrolled(75, korean=76):
        show hyunae staresob with fast
        show mute tensesob with fast
        $ ts("Wow, she's even sarcastic to men! *Mute...", "...I know, that's awful!")
    elif scrolled(87, korean=92):
        show mute whatsob with fast
        show hyunae hmmscb with fast
        ms "{i}Banditry{/i}? On the {i}Mugunghwa{/i}...?!"
    elif scrolled(94, korean=101):
        show hyunae staresc with fast
        show mute tensescb with fast
    elif scrolled(100, korean=106):
        show mute upsetscb with fast
        show hyunae staresc with fast
        ms "...tch, rude..."
    elif scrolled(124, korean=131):
        show hyunae hardsc with fast
        show mute neutralsc with fast
    elif scrolled(132, korean=140):
        show hyunae emo with fast
        show mute tensesc with fast
        hs "Hm..."
    elif scrolled(141, korean=150):
        show hyunae hmmsc with fast
        show mute wowsc with fast
    elif scrolled(156, korean=165):
        show hyunae annoyedsc with fast
        show mute thought with fast
    elif scrolled(164, korean=176):
        show mute hmphso with fast
        show hyunae satisfied with fast
        $ ts("Heehee, sure, *Mute.", "...of course she's chatty! It's just part of her nature...", True)
    elif scrolled(173, korean=186):
        show mute hate with fast
        show hyunae starescb with fast
        ms "...what was that?"
    elif scrolled(180, korean=194):
        show hyunae pout with fast
        show mute resent with fast
        hs "Nothing, nothing!"
    elif scrolled(197, korean=211):
        show hyunae hmphsc with fast
        show mute sorrysc with fast
    elif scrolled(208, korean=222):
        show hyunae hmmsob with fast
        show mute annoyed3 with fast
        $ ts("Ryu? As in... Captain and Emperor Ryu?", "...yes, exactly! Ryu Hyeon-su was the birth name of the dynasty founder, Emperor Taejo.")
        # Need a branch here if it's not the first time they saw Councillor Ryu - Raide
    elif scrolled(1000):
        show hyunae tired with fast
        show mute suspicious blush with fast

    jump log_loop

label log_1_3_xharem:
    if scrolled(6, korean=5):
        show hyunae funsob
        show mute talk4 with fast
        $ ts("Oh, dramas! I liked those too!", "Um, like... is this another one of your otaku things?")
    elif scrolled(12, korean=10):
        show hyunae heh with fast
        show mute challengeso with fast
        $ ts("Dad-logic: \"I bet my daughter will love it in the future!\"", "Is \"dad-logic\" a pejorative? How unfilial...")
    elif scrolled(18, korean=15):
        show mute damn with fast
        show hyunae gomen with fast
        ms "...ugh, geeze, *Hyun-ae, show some respect! You're as bad as him!"
        # hyun-ae rolls her eyes
    elif scrolled(28, korean=25):
        show hyunae staresc with fast
        show mute hmphsc with fast
    elif scrolled(36, korean=34):
        show hyunae bittersob with fast
        show mute hmm2 with fast
        $ ts("...oh, geeze! Does he mean her husband was doing...?", "...the maids? Yeah, I think so.")
    elif scrolled(66, korean=64):
        show hyunae bittersc with fast
        show mute thought with fast
    elif scrolled(74, korean=72):
        show hyunae sternsob with fast
        show mute tensescb with fast
        hs "Wow... Seo-yeong is really scary..."
    elif scrolled(82, korean=79):
        show mute hate with fast
        show hyunae baffled with fast
        $ ts("I didn't mean it like {i}that{/i}... I'm sure it's fine!", "Wow... women working really are as emotional as you'd think...", True)
    elif scrolled(109, korean=106):
        show hyunae annoyedsc with fast
        show mute tensesc with fast
    elif scrolled(117, korean=114):
        show mute talk4 with fast
        show hyunae explain4 with fast
        $ ts("Right...", "...I guess they had everything under control, though.", True)
    elif scrolled(124, korean=122):
        show hyunae hardsc with fast
        show mute neutralsc with fast
    elif scrolled(132, korean=130):
        show hyunae hardsob with fast
        show mute hmph with fast
        hs "You know, this Seung-bok boy seems a little awkward..."
    elif scrolled(140, korean=138):
        show mute upset with fast
        show hyunae hmmscb with fast
        ms "Um, just because he's dead doesn't mean you shouldn't show respect, *Hyun-ae."
    elif scrolled(1000):
        show mute tch with fast
        show hyunae hmm with fast
        ms "...this whole thing with those two women just doesn't feel right, though."

    jump log_loop

label log_1_4_xharem:
    if scrolled(8, korean=7):
        if not any_read("M1-2", "M3-1"):
            show mute what with fast
            show hyunae annoyedsc with fast
            ms "Ryu Hyeon-su? She was responsible for putting the first Emperor into power...?!"
        else:
            show mute tensesob with fast
            show hyunae hmph with fast
            ms "...it's still shocking that, like, she was responsible for putting the first Emperor into power...!"
    elif scrolled(16, korean=14):
        show hyunae emo with fast
        show mute annoyed3 with fast
        $ ts("It's a lot of scheming, isn't it?", "Sure is...")
    elif scrolled(24, korean=22):
        show hyunae hmphsc with fast
        show mute tensesc with fast
    elif scrolled(30, korean=27):
        show mute upsetsc with fast
        show hyunae staresc with fast
        ms "Huh..."
    elif scrolled(38, korean=37):
        show mute wowsob with fast
        show hyunae calmsob with fast
        $ ts("Aww, it's sweet!", "What's up with this tone...?", True)
    elif scrolled(43, korean=43):
        show mute whatsob with fast
        show hyunae heh with fast
        $ ts("What, jealous...?", "...wait, did Seo-yeong look on Old *Mute like a husband...?!", True)
    elif scrolled(1000):
        show mute tch with fast
        show hyunae calm2 with fast
        ms "What? Ugh... of course I'm not jealous!"

    jump log_loop

label log_1_5_xharem:
    if scrolled(4, korean=2):
        show mute tensesob with fast
        show hyunae funsc with fast
        ms "...how unprofessional!"
        # hyun-ae eye roll # I have no eye roll ;_; - Raide
    elif scrolled(10, korean=8):
        show mute challengesob with fast
        show hyunae satisfied blush with fast
        $ ts("I bet you'd look good in one, too!", "Suits?! I knew the past was uncivilized, but... Old *Mute too?", True)
    elif scrolled(16, korean=15):
        show mute bitter with fast
        show hyunae surescb with fast
        ms "...um, ugh, how inappropriate!"
    elif scrolled(22, korean=21):
        show hyunae heh with fast
        show mute give up with fast
        $ ts("I bet it would make [title]Investigator's heart skip a beat, too~", "I don't care about that, okay?!")
    elif scrolled(1000):
        show mute annoyed3 with fast
        show hyunae gomen with fast
        ms "Can I replace {i}you{/i} with a large potted plant...?"

    jump log_loop

label log_1_6_xharem:
    if scrolled(8, korean=6):
        show hyunae annoyedsob with fast
        show mute whatever with fast
        $ ts("Wow, this boy swears so much...!", "Like, even in a retrograde family, this disrespectful attitude is inexcusable!")
    elif scrolled(17, korean=15):
        show mute wowsob with fast
        show hyunae starescb with fast
        ms "...oh, no, this isn't going to be one of {i}those{/i} stories, is it?"
    elif scrolled(25, korean=23):
        show hyunae calmso with fast
        show mute embarrassed with fast
        $ ts("...I liked playing hwatu too, though... the cards are pretty.", "Um... but like, you didn't play any games like that, right...?")
    elif scrolled(33, korean=33):
        show hyunae awkward with fast
        show mute evil with fast
        hs "...no, of course not! This is... a bit... um..."
    elif scrolled(42, korean=41):
        show hyunae hardscb with fast
        show mute nicescb with fast
    elif scrolled(59, korean=56):
        show hyunae staresc with fast
        show mute neutralsc with fast
    elif scrolled(76, korean=73):
        if not any_read("M1-7", "M1-8", "M1-9"):
            show hyunae hmmsob with fast
            show mute tensesob with fast
            $ ts("I, um...", "...who is this base woman, and why is she in their home...?")
        else:
            show hyunae annoyedsob with fast
            show mute heh with fast
            $ ts("This is really dirty!", "...yes, dear, that's how men can be.")
    elif scrolled(88, korean=85):
        show mute hmphsob with fast
        show hyunae huhsc with fast
        ms "...yeah, I know how this story ends..."
    elif scrolled(99, korean=96):
        show hyunae staresc with fast
        show mute tensesc with fast
    elif scrolled(122, korean=122):
        show hyunae thinksc with fast
        show mute wowsc with fast
    elif scrolled(130, korean=131):
        show mute damn with fast
        show hyunae emo with fast
        $ ts("So even then they were using Chinese characters... that's so stupid!", "What...? Of course knowing the classics is important!", True)
    elif scrolled(134, korean=135):
        show hyunae troubled with fast
        show mute sulk with fast
    elif scrolled(148, korean=151): # immediately after, staring at eachother
        show hyunae hmmcob with fast
        show mute tensescb with fast
        $ ts("...ugh, geeze...", "...ugh, geeze...")
    elif scrolled(166, korean=171):
        show hyunae grumpy with fast
        show mute annoyed3 with fast
        $ ts("Geeze! But... he has a wife...!", "See, *Hyun-ae, {i}that's{/i} what happens to wives who act like shrews.")
    elif scrolled(175, korean=179):
        show hyunae starescb with fast
        show mute tensesc with fast
    elif scrolled(192, korean=196):
        show hyunae suresc with fast
        show mute hmphsc with fast
    elif scrolled(200, korean=204):
        show hyunae hmmsob with fast
        show mute evil with fast
        $ ts("...aaaaa, geeze... what is he saying...?!", "...maybe you're too sensitive to be reading this.")
    elif scrolled(208, korean=212):
        show hyunae satisfied blush with fast
        show mute embarrassed with fast
        $ ts("It's... cute in a way, I suppose... is this how adults are...?", "...uh, kinda...")
    elif scrolled(217, korean=222):
        show hyunae surescb with fast
        show mute whatscb with fast
    elif scrolled(226, korean=231):
        if not any_read("M1-7", "M1-8", "M1-9"):
            show mute astonished blush with fast
            show hyunae staresob with fast
            ms "Oh, wow... I misread that one! Well, if he's a man, that's okay."
        else:
            show mute hmm2 with fast
            show hyunae funscb with fast
            ms "Ah, so that's how their affair started, then..."
    elif scrolled(1000):
        show hyunae cautious2 with fast
        show mute neutral with fast
    
    jump log_loop

label log_1_7_xharem:
    if scrolled(8, korean=10):
        show mute grinsob with fast
        show hyunae huhscb with fast
        ms "...heh, reminds me of someone I knew."
    elif scrolled(17, korean=18):
        show hyunae staresob with fast
        show mute wowscb with fast
        hs "Huh...?"
    elif scrolled(25, korean=26):
        show hyunae staresc with fast
        show mute wowsc with fast
    elif scrolled(32, korean=33):
        show hyunae sweetsob with fast
        show mute craftyso with fast
        $ ts("Awwwwwwwwww...", "Awwwwwwwwww...")
    elif scrolled(52, korean=54):
        show hyunae staresc with fast
        show mute craftysc with fast
    elif scrolled(60, korean=62):
        show mute tensesob with fast
        show hyunae satisfied blush with fast
        $ ts("Ah! It's a kind of cooking from Earth, it's really good!", "\"Western style\" food? What's that...?", True)
    elif scrolled(76, korean=78):
        show hyunae calmsc with fast
        show mute wowsc with fast
    elif scrolled(85, korean=88):
        show mute whatsob with fast
        show hyunae thinksc with fast
        ms "...wow, was that kind of problem with literacy normal...?"
    elif scrolled(93, korean=96):
        show mute crafty blush with fast
        show hyunae hmmsob with fast
        $ ts("What do you mean by that...?", "...but there's still a ton of log file left to go. I know where this is going...", True)
    elif scrolled(100, korean=103):
        show hyunae tsundere with fast
        show mute evil with fast
        hs "...oh! Never mind...!"
    elif scrolled(105, korean=108):
        show hyunae hardscb with fast
        show mute nicescb with fast
    elif scrolled(117, korean=120):
        show hyunae staresob with fast
        show mute grinsob with fast
        hs "Whoa!"
    elif scrolled(125, korean=128):
        show hyunae awkward with fast
        show mute heh2 with fast
        $ ts("Wh... wh... aaaaaaaa, geeze... this is...!", "Um, maybe you shouldn't be reading this...")
    elif scrolled(137, korean=140):
        show hyunae hmm2 with fast
        show mute craftyscb with fast
    elif scrolled(151, korean=154):
        show hyunae starescb with fast
        show mute nicescb with fast
    elif scrolled(159, korean=162):
        show hyunae sweetso with fast
        show mute damn with fast
        $ ts("...well, maybe that wouldn't be so bad...", "What.")
    elif scrolled(170, korean=173):
        show hyunae funscb with fast
        show mute whatscb with fast
    elif scrolled(1000):
        show hyunae apologize blush with fast
        show mute damn with fast
        $ ts("What a weird relationship... but sort of romantic...", "WHAT.")

    jump log_loop

label log_1_8_xharem:
    if scrolled(8, korean=10):
        show hyunae hmmsob with fast
        show mute heh with fast
        $ ts("...again with all the swearing...!", "...that's how men are, dear.")
    elif scrolled(16, korean=19):
        show hyunae pout with fast
        show mute talk4 with fast
        $ ts("...I don't really think the idea of being 'taken' is as romantic as he says...", "...like, seriously? You have serious issues, *Hyun-ae.")
    elif scrolled(24, korean=26):
        show hyunae grumpy with fast
        show mute think with fast
        hs "...fine, I won't say anything."
    elif scrolled(35, korean=38):
        show hyunae hmphsc with fast
        show mute craftysc with fast
    elif scrolled(43, korean=46):
        show hyunae staresc with fast
        show mute wowscb with fast
    elif scrolled(63, korean=65):
        show hyunae hardsc with fast
        show mute hmphsc with fast
    elif scrolled(76, korean=78):
        show hyunae hmmsc with fast
        show mute whatscb with fast
    elif scrolled(86, korean=89):
        show mute grinsob with fast
        show hyunae huhsc with fast
        ms "Oh, ha ha, of course it's Dream of the Red Chamber! How cruel."
    elif scrolled(95, korean=98):
        show hyunae hmmcc with fast
        show mute nicescb with fast
    elif scrolled(110, korean=113):
        show hyunae hardsc with fast
        show mute nicescb with fast
    elif scrolled(120, korean=125):
        show mute craftysob with fast
        show hyunae starescb with fast
        ms "...ha ha, yep. Totally is."
    elif scrolled(135, korean=141):
        show hyunae hardscb with fast
        show mute sweetscb with fast
    elif scrolled(152, korean=158):
        show hyunae hmmsc with fast
        show mute craftysc with fast
    elif scrolled(165, korean=171):
        show hyunae pout with fast
        show mute heh with fast
        $ ts("I don't get it...", "It's okay, you're a girl, you don't have to.")
    elif scrolled(178, korean=183):
        show mute grinsob with fast
        show hyunae boredsc with fast
        ms "...Seung-bok, you idiot."
    elif scrolled(199, korean=203):
        show hyunae staresc with fast
        show mute sweetscb with fast
    elif scrolled(207, korean=211):
        show mute grin with fast
        show hyunae huhsc with fast
        ms "Ha! See, it's important to be well read!"
    elif scrolled(227, korean=231):
        show hyunae annoyedsc with fast
        show mute craftyscb with fast
    elif scrolled(235, korean=238):
        show hyunae hmmsc with fast
        show mute sweetscb with fast
    elif scrolled(248, korean=252):
        show hyunae baffled with fast
        show mute evil with fast
        $ ts("...I don't get their relation at all...", "That's just how love affairs are with men.")
    elif scrolled(1000):
        show hyunae cautious3 with fast
        show mute smile with fast
    
    jump log_loop

label log_1_9_xharem:
    if scrolled(8, korean=9):
        show hyunae bittersob with fast
        show mute nicesob with fast
        $ ts("He got engaged...? To a woman...?", "Good for him! He's responsible.")
        # Need a branch if this is the first log being read - Raide
    elif scrolled(16, korean=18):
        show hyunae pout with fast
        show mute damn with fast
        $ ts("...that's really cruel to her... I bet she didn't want to, either...{k=1}{/k}", "What? Like, do you seriously believe that? You think helping her is bad? How can you say that?!")
    elif scrolled(24, korean=18):
        show mute inquisitive2 with fast
        show hyunae bitterscb with fast
        ms "...he's a commoner, but he's got the heart of a gentleman, for sure. Geeze, *Hyun-ae, show some respect! It's admirable!"
    elif scrolled(31, korean=33):
        show hyunae weak2 with fast
        show mute neutralsc with fast
    elif scrolled(1000):
        show hyunae anxious with fast
        show mute smile with fast

    jump log_loop

label log_2_1_xharem:
    if scrolled(5, korean=7):
        show hyunae funsob with fast
        show mute tensesob with fast
        $ ts("Ah, wow, she writes really cutely...!", "...so this is what happens when peasant girls learn to write, huh.")
    elif scrolled(9, korean=11):
        show hyunae troubled with fast
        show mute sulk with fast
    elif scrolled(15, korean=17): #immediately after, staring at each other
        show hyunae hmmcob with fast
        show mute whatever with fast
        $ ts("Ugh, geeze...", "Ugh, geeze...")
    elif scrolled(21, korean=26):
        show hyunae hardsob with fast
        show mute upsetscb with fast
        $ ts("...well, I think it's cute...", "...embarrassing...")
    elif scrolled(29, korean=34):
        show mute wowsob with fast
        show hyunae starescb with fast
        ms "...like, what is up with this tone?"
    elif scrolled(39, korean=44):
        show hyunae staresob with fast
        show mute whatsob with fast
    elif scrolled(47, korean=53):
        show hyunae funscb with fast
        show mute tensescb with fast
    elif scrolled(60, korean=65):
        show hyunae starescb with fast
        show mute tensescb with fast
    elif scrolled(67, korean=72):
        show hyunae sweetsob with fast
        show mute damn with fast
        $ ts("She's really charming... someone like that...", "...what are you saying?")
    elif scrolled(78, korean=84):
        show hyunae heh with fast
        show mute upsetscb with fast
    elif scrolled(95, korean=101):
        show hyunae surescb with fast
        show mute whatscb with fast
    elif scrolled(106, korean=114):
        show hyunae stareso with fast
        show mute tensesob with fast
    elif scrolled(114, korean=122):
        show hyunae staresc with fast
        show mute tensesc with fast
    elif scrolled(128, korean=135):
        show hyunae calmsob with fast
        show mute upset3 with fast
        $ ts("...would be awful nice to be with...", "GAH.")
    elif scrolled(138, korean=145):
        show hyunae surescb with fast
        show mute hmphscb with fast
    elif scrolled(144, korean=151):
        show hyunae sweetscb with fast
        show mute tensescb with fast
    elif scrolled(1000):
        show mute give up with fast
        show hyunae tsundere with fast
        $ ts("What's wrong with that...?", "...who even says things like \"get chance!\"...?", True)

    jump log_loop

label log_2_2_xharem:
    if scrolled(6, korean=4):
        show mute wowso with fast
        show hyunae hopelesssc with fast
        ms "Wait, but wasn't Heo a noble name back then...?"
    elif scrolled(12, korean=11):
        show mute tensesob with fast
        show hyunae sighsc with fast
        ms "...yeah, I'd expect an actor who was also a woman to be that dramatic."
    elif scrolled(20, korean=19):
        show hyunae starescb with fast
        show mute hmphsc with fast
    elif scrolled(31, korean=32):
        show hyunae hopelessscb with fast
        show mute hmphsc with fast
    elif scrolled(39, korean=41):
        show hyunae bittersob with fast
        show mute whatsob with fast
        $ ts("Oh no! That's so mean...!", "...um, yikes...")
    elif scrolled(54, korean=57):
        show hyunae annoyedscb with fast
        show mute hmphscb with fast
    elif scrolled(65, korean=69):
        show hyunae sighscb with fast
        show mute hmphscb with fast
    elif scrolled(72, korean=78):
        show hyunae pressurescb with fast
        show mute sorrysc with fast
    elif scrolled(83, korean=89):
        show hyunae losssob with fast
        show mute sorrysc with fast
        hs "...oh no, poor Jin-a..."
    elif scrolled(96, korean=103):
        show hyunae bitterscb with fast
        show mute hmphscb with fast
    elif scrolled(104, korean=111):
        show hyunae starescb with fast
        show mute hmphscb with fast
    elif scrolled(112, korean=120):
        show mute wowsob with fast
        show hyunae funsob with fast
        $ ts("Ah, she is!", "...oh, clever girl.", True)
    elif scrolled(131, korean=139):
        show hyunae surescb with fast
        show mute hmm blush with fast
    elif scrolled(146, korean=153):
        show mute upsetsob with fast
        show hyunae sweetscb with fast
        ms "\"Smitten\"? Oh no, ugh!"
    elif scrolled(157, korean=163):
        show mute what with fast
        show hyunae gomen with fast
        ms "...does she think she's a man...?"
    elif scrolled(163, korean=171):
        show hyunae sure2 with fast
        show mute damn with fast
        $ ts("...it's kind of nice, though...", "NO. YOU'RE RIGHT, YOU SHOULDN'T HAVE SAID THAT.")
    elif scrolled(171, korean=180):
        show mute give up with fast
        show hyunae funsc with fast
        ms "What? She's a woman! WHAT ARE YOU EVEN SAYING *HYUN-AE."
    elif scrolled(180, korean=189):
        show mute bitter with fast
        show hyunae satisfied blush with fast
        $ ts("But I'd... um, never mind!", "...embarrassing...", True)
    elif scrolled(194, korean=203):
        show hyunae sighsob with fast
        show mute hmphscb with fast
    elif scrolled(202, korean=211):
        show hyunae calmscb with fast
        show mute tensescb with fast
    elif scrolled(213, korean=225):
        show hyunae calmscb with fast
        show mute tensesc with fast
    elif scrolled(226, korean=238):
        show hyunae sure blush with fast
        show mute challenge4 with fast
        $ ts("Is... this what adult relationships are like...?", "NO, OF COURSE NOT.")
    elif scrolled(1000):
        show hyunae smile blush with fast
        show mute tch with fast
    jump log_loop

label log_2_3_xharem:
    if scrolled(8, korean=7):
        show mute whatsob with fast
        show hyunae huhscb with fast
        $ ts("Huh?", "Wait, mixed-sex theatre? I don't know about that...", True)
    elif scrolled(15, korean=14):
        show hyunae huhsc with fast
        show mute whatscb with fast
    elif scrolled(24, korean=22):
        show mute upset3 with fast
        show hyunae hmmsob with fast
        $ ts("If you say so...", "...wouldn't you, like, have to worry about passions running too high...?", True)
    elif scrolled(1000):
        show hyunae neutral with fast
        show mute suspicious blush with fast
    jump log_loop

label log_2_4_xharem:
    if scrolled(7, korean=7):
        show hyunae sweetsob with fast
        show mute tch with fast
        $ ts("Aheh, 'girl-feelings!' I know what those are like...!", "...I don't think I want to know what that means.")
    elif scrolled(14, korean=14):
        show mute give up with fast
        show hyunae starescb with fast
        ms "What even is this? In the absence of men, do all women just naturally play married...?!"
    elif scrolled(20, korean=20):
        show hyunae calmscb with fast
        show mute upsetscb with fast
    elif scrolled(28, korean=27):
        show hyunae hmmsob with fast
        show mute embarrassed with fast
        $ ts("...why wouldn't she...? Is Ae-jeong a noisy sleeper...?", "...oh, *Hyun-ae.")
    elif scrolled(36, korean=36):
        show hyunae staresob with fast
        show mute worry3 with fast
        $ ts("...oh, my...", "Um, maybe, like, you shouldn't be reading things like this, *Hyun-ae...")
    elif scrolled(45, korean=45):
        show hyunae sweetscb with fast
        show mute tensescb with fast
    elif scrolled(53, korean=53):
        show hyunae awkward with fast
        show mute damn with fast
        $ ts("...this is really... really... really...!", "TOO MUCH.")
    elif scrolled(61, korean=61):
        show hyunae touched with fast
        show mute upsetscb with fast
    elif scrolled(78, korean=79):
        show hyunae happy with fast
        show mute challengescb with fast
    elif scrolled(88, korean=89):
        show hyunae awkward with fast
        show mute annoyed3 with fast
        $ ts("Is that normal for a girl's body, *Mute...?", "...I don't know, okay? Why do you think I would know that?!")
    elif scrolled(101, korean=102):
        show hyunae gomen with fast
        show mute hmphscb with fast
    elif scrolled(117, korean=118):
        show mute upset3 with fast
        show hyunae sweetscb with fast
        ms "I... wasn't really prepared for this kind of detail..."
    elif scrolled(127, korean=128):
        show hyunae heh with fast
        show mute bitter with fast
        $ ts("Aaaaaaaaaaaaaa! This is... that sounds like... I'd... gosh...", "...something you'd what?!")
    elif scrolled(131, korean=132):
        show hyunae calm with fast
        show mute sigh blush with fast
        $ ts("Nothing! Nothing at all! I don't find it romantic even slightly!", "Um... okay..?")
    elif scrolled(1000):
        show hyunae glad with fast
        show mute tired blush with fast
    jump log_loop

label log_2_5_xharem:
    if scrolled(4, korean=3):
        show hyunae surrender blush with fast
        show mute worry3 with fast
        $ ts("Oh... that's bad...", "Yes, it was bad from the start!")
    elif scrolled(11, korean=9):
        show hyunae bitterscb with fast
        show mute tensesc with fast
    elif scrolled(17, korean=15):
        show hyunae hmmsc with fast
        show mute wowsc with fast
    elif scrolled(22, korean=22):
        show hyunae losssob with fast
        show mute wowsc with fast
        hs "Awww, that's sweet, at least..."
    elif scrolled(30, korean=29):
        show mute tch with fast
        show hyunae pout with fast
        $ ts("...I can understand that, though...", "...see, this is why it doesn't make sense for women to be together.", True)
    elif scrolled(38, korean=37):
        show hyunae lossscb with fast
        show mute disbelief with fast
    elif scrolled(49, korean=49):
        show mute wowsob with fast
        show hyunae hmmsob with fast
        $ ts("Huh...? What does that even mean...?", "...wait... but I thought it was Ae-jeong who played the man's role...?", True)
    elif scrolled(57, korean=57):
        show hyunae bittersob with fast
        show mute upsetscb with fast
        hs "Oh geeze... I shouldn't be reading this..."
    elif scrolled(66, korean=68):
        show hyunae hopelessscb with fast
        show mute upsetsc with fast
    elif scrolled(79, korean=81):
        show hyunae sighscb with fast
        show mute tensescb with fast
    elif scrolled(81, korean=83):
        show hyunae bitterscb with fast
        show mute whatsob with fast
    elif scrolled(89, korean=92):
        show hyunae surrender blush with fast
        show mute give up with fast
        $ ts("...this is...", "...wow...")
    elif scrolled(105, korean=107):
        show hyunae lossscb with fast
        show mute upsetscb with fast
    elif scrolled(116, korean=116):
        show hyunae shame with fast
        show mute damn with fast
        $ ts("I feel really sad for her, though...", "HOW IS THAT SUPPOSED TO BE INNOCENT.")
    elif scrolled(1000):
        show hyunae troubled with fast
        show mute worry side with fast

    jump log_loop

label log_2_6_xharem:
    if scrolled(6, korean=4):
        show hyunae annoyedsob with fast
        show mute troubled with fast
        $ ts("\"Tamed,\" huh. That... isn't really funny...", "Geeze, lighten up, *Hyun-ae.")
    elif scrolled(12, korean=8):
        show hyunae hmph3 with fast
        show mute hmph with fast
        hs "Sorry..."
    elif scrolled(24, korean=19):
        show hyunae hardsc with fast
        show mute thought with fast
    elif scrolled(34, korean=28):
        show hyunae sigh with fast
        show mute hmm with fast
        hs "I still don't understand why these were included, though... they're boring too."
    elif scrolled(1000):
        show hyunae tired with fast
        show mute neutral3 with fast
    jump log_loop

label log_2_7_xharem:
    if scrolled(6, korean=7):
        show hyunae depressed with fast
        show mute tensescb with fast
    elif scrolled(12, korean=12):
        show hyunae hopelesssob with fast
        show mute inquisitive2 with fast
        $ ts("She's so poetic about everything...", "...please raise your standards, *Hyun-ae.")
    elif scrolled(18, korean=18):
        show hyunae annoyedsob with fast
        show mute damn with fast
        $ ts("...well, fathers don't always know what's right...", "YES THEY DO. This is {i}not{/i} the same thing as yours!")
    elif scrolled(24, korean=25):
        show hyunae pout with fast
        show mute worry side with fast
        hs "...fine..."
    elif scrolled(30, korean=31):
        show mute sighsob with fast
        show hyunae baffled with fast
        $ ts("Let's just pay attention to the log, it's fine.", "...sorry. That was a little too harsh.", True)
    elif scrolled(42, korean=43):
        show hyunae losssc with fast
        show mute sorryscb with fast
    elif scrolled(48, korean=50):
        show mute wowsob with fast
        show hyunae think2 with fast
        $ ts("Yeah! You get it from a vending machine, and it can be either hot or cold! It's really good!", "...canned tea...?", True)
    elif scrolled(53, korean=55):
        show hyunae hmph2 with fast
        show mute what with fast
        $ ts("They also have canned coffee, but my parents never let me have it.", "Okay, okay, got it. Weird...")
    elif scrolled(61, korean=63):
        show mute sighsob with fast
        show hyunae bitterscb with fast
        ms "Oh {i}finally{/i} her parents take some responsibility in getting her married!"
    elif scrolled(73, korean=76):
        show hyunae sighscb with fast
        show mute sorryscb with fast
    elif scrolled(81, korean=85):
        show hyunae pressurescb with fast
        show mute sorrysc with fast
    elif scrolled(91, korean=95):
        show hyunae annoyedscb with fast
        show mute upsetsc with fast
    elif scrolled(102, korean=106):
        show mute insecure with fast
        show hyunae troubled2 with fast
        $ ts("But...", "...see, this is why that kind of relationship isn't just harmless...!", True)
    elif scrolled(116, korean=120):
        show hyunae pressurescb with fast
        show mute sigh blush with fast
    elif scrolled(124, korean=128):
        show mute tensesob with fast
        show hyunae troubled2 with fast
        $ ts("...but wouldn't it be better if they could just be in love...?", "...it'd be so much easier for her if she was more reasonable about it...", True)
    elif scrolled(140, korean=144):
        show hyunae guilt with fast
        show mute challengesc with fast
    elif scrolled(148, korean=153):
        show mute challengesob with fast
        show hyunae sad with fast
        ms "That's not how love works!"
    elif scrolled(1000):
        show mute cry with fast
        show hyunae sulk with fast
        $ ts("But... but...", "What monster taught these women to expect love to come before marriage instead of after?!", True)
    jump log_loop

label log_2_8_xharem:
    if scrolled(6, korean=8) and any_read("M2-2", "M2-4", "M2-5", "M2-6"):
        show hyunae bittersob with fast
        show mute what with fast
        $ ts("Oh no... but they were so good together...", "...wait, what?")
    elif scrolled(13, korean=16):
        show hyunae annoyedsob with fast
        show mute sorryscb with fast
        hs "...oh... I think I know how this ends..."
    elif scrolled(23, korean=26):
        show hyunae lossscb with fast
        show mute sighscb with fast
    elif scrolled(31, korean=34):
        show mute tensescb with fast
        show hyunae pressurescb with fast
        ms "...didn't she realize this was bound to happen?"
    elif scrolled(39, korean=43):
        show mute upsetsob with fast
        show hyunae pity with fast
        $ ts("But... she's in love...", "...it's a generous offer! Jin-a needs to be more rational...", True)
    elif scrolled(47, korean=51):
        show mute give up with fast
        show hyunae troubled with fast
        ms "What? Like, do you seriously see a way it could possibly work? You need to be rational too, *Hyun-ae! Ugh!"
    elif scrolled(55, korean=60):
        show hyunae pout with fast
        show mute tch with fast
        hs "...sorry..."
    elif scrolled(66, korean=73):
        show hyunae hopelessscb with fast
        show mute tensesc with fast
    elif scrolled(78, korean=84):
        show hyunae lossscb with fast
        show mute hmphscb with fast
    elif scrolled(91, korean=100):
        show mute sighsob with fast
        show hyunae sighsob with fast
        $ ts("We can agree on that...", "This is painful...", True)
    elif scrolled(100, korean=110):
        show mute insecure with fast
        show hyunae annoyedscb with fast
        ms "...but Ae-jeong did the right thing! How can she be so unappreciative of that...?!"
    elif scrolled(107, korean=118):
        show hyunae sigh blush with fast
        show mute worry with fast
    elif scrolled(1000):
        show hyunae anxious with fast
        show mute tired blush with fast
    jump log_loop

label log_2_9_xharem:
    if scrolled(8, korean=6):
        show mute enthusiastic blush with fast
        show hyunae hmmsc with fast
        ms "Oh, that's the first Emperor's brother they're talking about..."
    elif scrolled(16, korean=13):
        show mute sweetsob with fast
        show hyunae sighscb with fast
        ms "...so I guess she ended up working as a courtesan, then."
    elif scrolled(24, korean=21):
        show hyunae pity with fast
        show mute worry3 with fast
        $ ts("That sucks for her...", "Yeah. For once, you're right. But it's the best possibility, considering...")
    elif scrolled(31, korean=28):
        show hyunae bitterscb with fast
        show mute hmphscb with fast
    elif scrolled(39, korean=35):
        show hyunae pressuresob with fast
        show mute tensesc with fast
        hs "...gross!"
    elif scrolled(52, korean=48):
        show hyunae pressurescb with fast
        show mute thought with fast
    elif scrolled(60, korean=55) and read("M2-2"):
        show hyunae hopelesssob with fast
        show mute hmphsc with fast
        hs "Awwww... she kept the hairpin! Wow..."
    elif scrolled(66, korean=61):
        show hyunae hopelessscb with fast
        show mute neutralsc with fast
    elif scrolled(1000):
        show mute worry3 with fast
        show hyunae sad with fast
        $ ts("I don't know... it just really makes me feel sad...", "...well, I guess it ended well for everyone, at least? Even if there was heartbreak...", True)
    jump log_loop

label log_3_1_xharem:
    if scrolled(10, korean=7):
        if not any_read("M3-2", "M3-3", "M3-4", "M3-5", "M3-6", "M3-8", "M3-9"):
            show hyunae hmmsob with fast
            show mute upset with fast
            $ ts("...but it's important to anyway, right?", "Like, I feel kinda weird about reading my mistress's letters...")
        else:
            show mute upset3 with fast
            show hyunae hmmsc with fast
            ms "It's so weird reading about Queen Eun-a like this..."
    elif scrolled(19, korean=15):
        show mute upset2 with fast
        show hyunae hmmcc with fast
        ms "What? This is Eun-a...? She'd never say things like that...!"
    elif scrolled(27, korean=25):
        show mute abashed blush with fast
        show hyunae bitterscb with fast
        ms "WHAT. At first, she just wanted the great Emperor Ryu... for his {i}cock{/i}?!"
    elif scrolled(35, korean=33):
        show hyunae troubled2 with fast
        show mute give up with fast
        $ ts("...well, if he's anything like his descendant, he's probably—", "NO. NO NO NO NO NO NO NO, DON'T TELL ME THIS. I CANNOT HEAR WHAT YOU'RE ABOUT TO SAY, OKAY?")
    elif scrolled(46, korean=45):
        show hyunae hmph with fast
        show mute hmphscb with fast
    elif scrolled(52, korean=50):
        show mute upset2 with fast
        show hyunae sternsc with fast
        ms "...I... I agree with what they're saying, though..."
    elif scrolled(60, korean=57):
        show mute hmphsob with fast
        show hyunae hmmsc with fast
        ms "Okay... okay, good, that's still really admirable of her!"
    elif scrolled(74, korean=72):
        show hyunae hmmcc with fast
        show mute hmphsc with fast
    elif scrolled(84, korean=82):
        show hyunae bittersc with fast
        show mute tensescb with fast
    elif scrolled(96, korean=95):
        show hyunae bittersc with fast
        show mute upsetsc with fast
    elif scrolled(104, korean=103):
        show hyunae grumpy with fast
        show mute astonished blush with fast
        $ ts("This is...", "...I know, I know...")
    elif scrolled(122, korean=120):
        show hyunae pressurescb with fast
        show mute disbelief blush with fast
    elif scrolled(130, korean=129):
        show mute pressure with fast
        show hyunae defensivescb with fast
        ms "...she was a seductress. I... like, my noble queen, my first friend... she was a seductress."
    elif scrolled(138, korean=137):
        show hyunae pout with fast
        show mute upsetsob with fast
        $ ts("What is she even doing...? This is so gross...", "...I don't know how to feel...")
    elif scrolled(150, korean=152):
        show hyunae bitterscb with fast
        show mute upsetsc with fast
    elif scrolled(167, korean=168):
        show mute tensescb with fast
        show hyunae bitterscb with fast
        ms "...I don't know how I'm supposed to feel about her anymore."
    elif scrolled(1000):
        show hyunae baffled with fast
        show mute shame with fast
    
    jump log_loop

label log_3_2_xharem:
    if scrolled(4, korean=6) and any_read("M3-1", "M3-3", "M3-4", "M3-5", "M3-6", "M3-7", "M3-8", "M3-9"):
        show hyunae hopelessso with fast
        show mute tensesc with fast
        hs "Oh, so this is the little sister, then..."
    elif scrolled(10, korean=13):
        show mute tensesob with fast
        show hyunae hopelesssc with fast
        ms "Why would her sister be jealous...?"
    elif scrolled(20, korean=23):
        show hyunae surrender with fast
        show mute whatscb with fast
    elif scrolled(30, korean=35):
        show mute wowsob with fast
        show hyunae bittersc with fast
        ms "...wow... Eun-a was responsible for that...?"
    elif scrolled(39, korean=44):
        show hyunae bittersob with fast
        show mute hmphso with fast
        $ ts("This is...", "That's completely reasonable!")
    elif scrolled(50, korean=56):
        show hyunae sulk with fast
        show mute upsetscb with fast
    elif scrolled(60, korean=67):
        show hyunae annoyedscb with fast
        show mute tensesc with fast
    elif scrolled(69, korean=76):
        show mute wow3 with fast
        show hyunae huhscb with fast
        ms "Wow... I never realized it, but like, Queen Eun-a was quite the scholar, wasn't she?"
    elif scrolled(78, korean=85):
        show hyunae pressuresc with fast
        show mute hmphsc with fast
    elif scrolled(86, korean=94):
        show hyunae annoyedscb with fast
        show mute hmm blush with fast
    elif scrolled(94, korean=104):
        show hyunae annoyed blush with fast
        show mute upset3 with fast
        $ ts("...I think I'd feel the same way, in Mi-seun's situation...", "Oh, *Hyun-ae, of course {i}you{/i} would.")
    elif scrolled(105, korean=116):
        show hyunae sighscb with fast
        show mute sorrysc with fast
    elif scrolled(114, korean=126):
        show mute damn with fast
        show hyunae huh with fast
        ms "\"Take over the ship\"... ugh, when she puts it that way..."
    elif scrolled(1000):
        show hyunae troubled with fast
        show mute tired blush with fast
    
    jump log_loop

label log_3_3_xharem:
    if scrolled(6, korean=5) and any_read("M3-1", "M3-2", "M3-4", "M3-5", "M3-7", "M3-8", "M3-9"):
        show hyunae oops with fast
        show mute disbelief blush with fast
        $ ts("Consort?!", "Consort?!")
    elif scrolled(16, korean=15):
        show mute upsetsob with fast
        show hyunae hmmscb with fast
        ms "...I don't know what to make of this..."
    elif scrolled(24, korean=22):
        show mute tensescb with fast
        show hyunae bittersc with fast
        ms "His attitude, though... tch..."
    elif scrolled(34, korean=33):
        show hyunae hmmsc with fast
        show mute hmphscb with fast
    elif scrolled(1000):
        show mute tch with fast
        show hyunae shame with fast
        $ ts("Yeah, she's really loyal to her sister!", "Well, okay, I can respect that.", True)

    jump log_loop

label log_3_4_xharem:
    if scrolled(10, korean=9) and read("M1-1"):
        show hyunae flustered with fast
        show mute tensesob with fast
        $ ts("Wait, writing on paper...? I thought that was illegal...!", "Yeah...")
    elif scrolled(20, korean=20):
        show hyunae weak2 with fast
        show mute upsetsc with fast
        hs "Oh... that's really sad..."
    elif scrolled(28, korean=28):
        show mute astonished with fast
        show hyunae bittersc with fast
        ms "...she rigged the council? Queen Eun-a... she... she really did do that herself...? That's..."
    elif scrolled(35, korean=34):
        show hyunae hmmcob with fast
        show mute damn with fast
        $ ts("What time of month does she mean by \"that\" one...?", "...don't worry about it, *Hyun-ae.")
    elif scrolled(49, korean=46):
        show hyunae sighscb with fast
        show mute sorryscb with fast
    elif scrolled(60, korean=57):
        show hyunae lossscb with fast
        show mute upsetsc with fast
    elif scrolled(68, korean=66):
        show hyunae annoyedscb with fast
        show mute tensesc with fast
    elif scrolled(77, korean=75):
        show hyunae bitterscb with fast
        show mute tensescb with fast
    elif scrolled(84, korean=83):
        show hyunae losssob with fast
        show mute troubled with fast
        $ ts("Oh no...", "...but, like, why didn't she {i}actually{/i} tell Eun-a about these feelings...?")
    elif scrolled(1000):
        show mute shame with fast
        show hyunae troubled with fast
        ms "...this poor woman needs help... and she sure didn't get it from Eun-a..."

    jump log_loop

label log_3_5_xharem:
    if scrolled(5, korean=4):
        show hyunae hmmsob with fast
        show mute worry3 with fast
        $ ts("\"That way\"...?", "...*Hyun-ae, you were a noble consort, I {i}know{/i} you know exactly what she means.")
    elif scrolled(10, korean=9):
        show hyunae bittersc with fast
        show mute upsetsc with fast
        hs "Oh...!"
    elif scrolled(16, korean=17):
        show hyunae hopelesssc with fast
        show mute upsetsc with fast
    elif scrolled(24, korean=25):
        show hyunae annoyedsob with fast
        show mute tensesob with fast
        $ ts("...I don't know what to make of this.", "...yeah.")
    elif scrolled(32, korean=32):
        show mute sighsob with fast
        show hyunae annoyedscb with fast
        ms "Poor woman, forced into a role she couldn't handle..."
    elif scrolled(41, korean=41):
        show hyunae bittersc with fast
        show mute hmphscb with fast
    elif scrolled(49, korean=49):
        show mute upsetsob with fast
        show hyunae hmph with fast
        ms "...\"scheming mastermind\"... but Emperor Ryu approved of it..."
    elif scrolled(56, korean=57):
        show mute pressure with fast
        show hyunae hopelesssc with fast
        ms "I..."
    elif scrolled(64, korean=65):
        show hyunae bitterscb with fast
        show mute astonished blush with fast
    elif scrolled(74, korean=75):
        show hyunae losssc with fast
        show mute upsetscb with fast
    elif scrolled(82, korean=83):
        show hyunae pout with fast
        show mute disappoint3 with fast
        hs "...I sure know {i}that{/i} part..."
    elif scrolled(91, korean=92):
        show hyunae bitterscb with fast
        show mute upsetsc with fast
    elif scrolled(99, korean=100):
        show mute shame with fast
        show hyunae emo with fast
        $ ts("...I'm glad you think so, too...", "I... she's so manipulative. I can't believe it... this is her...?", True)
    elif scrolled(111, korean=111):
        show hyunae sighscb with fast
        show mute pout with fast
    elif scrolled(121, korean=120):
        show hyunae surrender blush with fast
        show mute tired blush with fast
    elif scrolled(1000):
        show mute bitter with fast
        show hyunae tired with fast
        ms "...well, she got everything she wanted, in the end..."

    jump log_loop

label log_3_6_xharem:
    if scrolled(0):
        show hyunae guilt with fast
        show mute insecure with fast
        $ ts("No!", "Fuck...")

    jump log_loop

label log_3_7_xharem:
    if scrolled(6, korean=6):
        show hyunae touched with fast
        show mute damn with fast
        $ ts("Did you see the picture of the maid? She's cute!", "...geeze, *Hyun-ae...")
    elif scrolled(12, korean=12):
        show hyunae heh with fast
        show mute give up with fast
        $ ts("I'm just saying, I wouldn't mind interrogating her~", "...what does that even mean?")
    elif scrolled(18, korean=18):
        show hyunae funscb with fast
        show mute hmphscb with fast
    elif scrolled(24, korean=27):
        show mute tensesob with fast
        show hyunae sulk2 with fast
        $ ts("Oh, aw. Mourning attire is really boring...", "Wait, was mourning attire not usual?", True)
    elif scrolled(32, korean=35):
        show mute mad with fast
        show hyunae emo with fast
        $ ts("...sorry.{k=2}{/k}", "...show some respect, *Hyun-ae! Queen Eun-a's sister was dead!", True)
    elif scrolled(38, korean=41):
        show hyunae hmmscb with fast
        show mute upsetscb with fast
    elif scrolled(46, korean=49):
        show mute whatsob with fast
        show hyunae huhsc with fast
        ms "...\"their bed\"...?"
    elif scrolled(56, korean=60):
        show hyunae hmmco with fast
        show mute upset3 with fast
        $ ts("Yeah... I don't remember anyone drinking tea with the servants, either...", "Of course not! That would be weird.")
    elif scrolled(64, korean=69):
        show hyunae huhso with fast
        show mute sorryscb with fast
        hs "...that's... a little bit... um..."
    elif scrolled(75, korean=80):
        show mute tensescb with fast
        show hyunae hmmscb with fast
        ms "...I, um, never would have imagined Eun-a being like that..."
    elif scrolled(79, korean=84):
        show hyunae huhscb with fast
        show mute whatscb with fast
    elif scrolled(1000):
        show hyunae pity with fast
        show mute shame with fast
        $ ts("...I don't really know how to feel about her anymore...", "...yeah.")

    jump log_loop

label log_3_8_xharem:
    if scrolled(6, korean=5):
        show hyunae sigh blush with fast
        show mute upsetscb with fast
        hs "...now I just feel bad..."
    elif scrolled(12, korean=11):
        show mute insecure with fast
        show hyunae guilt with fast
        $ ts("I'm sorry...", "\"You were a friend of mine,\" she told me... what a brazen lie!", True)
    elif scrolled(18, korean=18):
        show mute bitter with fast
        show hyunae sad with fast
        ms "Ugh... I don't want pity, this is just..."
    elif scrolled(26, korean=26):
        show hyunae losssob with fast
        show mute challenge4 with fast
        $ ts("...well, I understand that feeling...", "Oh, of {i}course{/i} you would!")
    elif scrolled(34, korean=35):
        show mute challengesob with fast
        show hyunae oops with fast
        $ ts("...sorry, I won't say anything.", "No, no, please, it's okay, you can {i}also{/i} tell me what it's like to have sex with my superior! Like, I'd love to hear that!", True)
    elif scrolled(40, korean=41):
        show hyunae troubled2 with fast
        show mute upsetsc with fast
        hs "I said I'm sorry..."
    elif scrolled(52, korean=52):
        show hyunae bitterscb with fast
        show mute pout with fast
    elif scrolled(66, korean=64):
        show hyunae hmmscb with fast
        show mute worry with fast
    elif scrolled(1000):
        show mute sob with fast
        show hyunae sad with fast
        ms "I... I can't parse this..."

    jump log_loop

label log_3_9_xharem:
    if scrolled(4, korean=2):
        show mute upsetscb with fast
        show hyunae annoyedsc with fast
        ms "I..."
    elif scrolled(9, korean=6):
        show mute upsetsob with fast
        show hyunae annoyedsc with fast
        ms "...that really is cruel of him, even though..."
    elif scrolled(18, korean=14):
        show mute pressure with fast
        show hyunae pity with fast
        $ ts("I'm sorry, *Mute...", "\"A self-righteous bitch\"?! Then why did you ever re-enable me...?!", True)
    elif scrolled(24, korean=20):
        show mute mad with fast
        show hyunae defensivesc with fast
        ms "...I... is that it...? Was it that barbaric society that made her like this...?"
    elif scrolled(34, korean=29):
        show hyunae bitterscb with fast
        show mute tensescb with fast
    elif scrolled(47, korean=43):
        show mute sorrysob with fast
        show hyunae bitterscb with fast
        ms "...why..."
    elif scrolled(56, korean=53):
        show mute upsetsob with fast
        show hyunae sighscb with fast
        ms "I..."
    elif scrolled(64, korean=61):
        show hyunae lossso with fast
        show mute astonished blush with fast
    elif scrolled(1000):
        show hyunae lost with fast
        show mute cry with fast
        $ ts("I... never would have thought... she was thinking of her little sister the whole time...?", "...I don't know if that makes it okay. I just... I don't...")

    jump log_loop

label log_4_1_xharem:
    if scrolled(8, korean=8):
        show hyunae hardscb with fast
        show mute hateso with fast
        ms "...Old *Mute was so rude...!"
    elif scrolled(16, korean=15):
        show hyunae thinksc with fast
        show mute hmphsc with fast
    elif scrolled(27, korean=27):
        show hyunae hardsc with fast
        show mute thought with fast
    elif scrolled(35, korean=35):
        show hyunae hmmcob with fast
        show mute talk4 with fast
        $ ts("...I don't understand what they're talking about...", "Don't worry about it, dear. It's best if women don't worry about politics.")
    elif scrolled(44, korean=44):
        show hyunae hmmsc with fast
        show mute tensescb with fast
    elif scrolled(52, korean=53):
        if not any_read("M3-2", "M3-3", "M3-5", "M4-5", "M6-3", "M6-7"):
            show mute wow3 with fast
            show hyunae hmphsc with fast
            ms "Wait, Queen Oh Eun-a? She was an official before...?!"
            # Need a branch where *Mute has read about Eun-a in other logs - Raide
        else:
            show mute troubled with fast
            show hyunae hmphsc with fast
            ms "I still can't imagine Queen Oh Eun-a as an official..."
    elif scrolled(64, korean=64):
        show hyunae hmmsc with fast
        show mute tensesc with fast
    elif scrolled(72, korean=72):
        show mute tenseso with fast
        show hyunae bittersob with fast
        $ ts("So... she's the reason why I couldn't understand what everyone wrote...", "Oh! Of course Eun-a would want to improve literacy!", True)
    elif scrolled(92, korean=92):
        show hyunae annoyedsc with fast
        show mute hmphscb with fast
    elif scrolled(100, korean=100):
        show hyunae hmmsob with fast
        show mute upset3 with fast
        $ ts("Whoa... *Mute back then really was harsh...", "Yeah... like, I respect that, but... what a cold maneuver...")
    elif scrolled(121, korean=121):
        show hyunae hmmsc with fast
        show mute hmphsc with fast
    elif scrolled(133, korean=132):
        show hyunae bittersc with fast
        show mute neutralsc with fast
    elif scrolled(141, korean=140):
        show mute challenge2 with fast
        show hyunae hmmcc with fast
        ms "...I can't deal with how rude she is, though!"
    elif scrolled(159, korean=158):
        show hyunae bittersc with fast
        show mute tensesc with fast
    elif scrolled(1000):
        show hyunae disappoint with fast
        show mute think with fast
    
    jump log_loop

label log_4_2_xharem:
    if scrolled(8, korean=7) and read("M1-2"):
        show mute hmphso with fast
        show hyunae busy with fast
        $ ts("Ah, right, with Smith and Seo-yeong!", "So this is the result of Old *Mute's conspiring...", True)
    elif scrolled(44, korean=42):
        show hyunae hmphsc with fast
        show mute tensesc with fast
    elif scrolled(61, korean=58):
        show hyunae staresob with fast
        show mute whatscb with fast
    elif scrolled(71, korean=69):
        show hyunae hardsob with fast
        show mute upset2 with fast
        $ ts("...ha ha, wow, I always thought politics would be more civil...", "It should be! Like, all this uncivilized bickering... it's not right!")
    elif scrolled(92, korean=90):
        show hyunae hmmsc with fast
        show mute hmphsc with fast
    elif scrolled(105, korean=102):
        show hyunae huhsc with fast
        show mute tensescb with fast
    elif scrolled(132, korean=128):
        show hyunae hmphsc with fast
        show mute hmphsc with fast
    elif scrolled(145, korean=142):
        show hyunae bittersc with fast
        show mute tensesc with fast
    elif scrolled(160, korean=156):
        show mute wowsob with fast
        show hyunae hardscb with fast
        ms "...wow."
    elif scrolled(170, korean=166):
        if not read("M1-5"):
            show mute upsetsob with fast
            show hyunae stare blush with fast
            $ ts("Wow... even older than I am! By a lot!", "...1600 years? Wow... that's...", True)
            # Might need branch if you've seen this number back in 1_5 - Raide
        else:
            show mute tensesob with fast
            show hyunae hmph2 with fast
            $ ts("She seems to bring up her age a lot, though...", "1600 years is such a long time...", True)
    elif scrolled(183, korean=181):
        show hyunae hmphsc with fast
        show mute whatscb with fast
    elif scrolled(207, korean=204):
        if not any_read("M1-4", "M2-9", "M3-1", "M3-2", "M3-7", "M4-3", "M4-4", "M4-5", "M4-6", "M4-7", "M4-8", "M4-9", "M6-1", "M6-4", "M6-5", "M6-6", "M6-7", "M6-8", "M6-9"):
            show mute disbelief blush with fast
            show hyunae think with fast
            ms "...so just like that, Old *Mute was able to name the new Chief Councillor?"
        else:
            show mute upset3 with fast
            show hyunae think with fast
            ms "...so Old *Mute named the new Chief Councillor that easily?"
    elif scrolled(1000):
        show hyunae neutral with fast
        show mute tch with fast

    jump log_loop

label log_4_3_xharem:
    if scrolled(6, korean=5):
        show mute tensesob with fast
        show hyunae hmmsc with fast
        ms "Oh, wow... that was a problem even in the past?"
    elif scrolled(15, korean=15):
        show mute annoyed2 with fast
        show hyunae bitterscb with fast
        ms "...well, actually, I guess it'd be worse without marriage being respected, huh..."
    elif scrolled(28, korean=28):
        show hyunae hmmcc with fast
        show mute neutralsc with fast
    elif scrolled(38, korean=38):
        show hyunae annoyedsc with fast
        show mute hmphsc with fast
    elif scrolled(68, korean=69):
        show hyunae bittersc with fast
        show mute nicesc with fast
    elif scrolled(77, korean=78):
        if any_read("M5-3", "M5-7", "M5-8", "M5-9"):
            show hyunae weak2 with fast
            show mute hmm2 with fast
            $ ts("I don't really get it, but... isn't this sort of related to what Kim So-yi was talking about...?", "...oh. ...yes.")
        else:
            show hyunae sigh with fast
            show mute nicesc with fast
            hs "I don't really get it..."
    elif scrolled(87, korean=88):
        show hyunae hopelesssc with fast
        show mute craftysc with fast
    elif scrolled(95, korean=96):
        show hyunae hmmsc with fast
        show mute nicesc with fast
    elif scrolled(105, korean=106):
        show hyunae hopelesssc with fast
        show mute whatsob with fast
    elif scrolled(113, korean=114):
        show mute give up with fast
        show hyunae grr with fast
        ms "...geeze, what's with her arguing with a man like that...? I'd never!"
    elif scrolled(121, korean=122):
        show hyunae troubled2 with fast
        show mute bitter with fast
        $ ts("Even if you knew he was wrong...?", "Um, like, if I thought he was wrong, I would try to understand what my misunderstanding was. That's the mature thing to do, okay?")
    elif scrolled(130, korean=132):
        show hyunae unsure with fast
        show mute shame with fast
        $ ts("Is it...?", "Don't worry, *Hyun-ae, it's okay. I know you'll get it eventually!")
    elif scrolled(145, korean=145):
        show hyunae troubled with fast
        show mute tensesc with fast
    elif scrolled(159, korean=161):
        show hyunae defensivesc with fast
        show mute tensescb with fast
    elif scrolled(170, korean=172):
        show hyunae hardsc with fast
        show mute challengesc with fast
    elif scrolled(190, korean=190):
        show hyunae hopelesssc with fast
        show mute neutralsc with fast
    elif scrolled(1000):
        show mute brag blush with fast
        show hyunae sulk with fast
        ms "...but, like, I guess it went through in the end, right?"

    jump log_loop

label log_4_4_xharem:
    if scrolled(6, korean=5):
        show hyunae hmmsc with fast
        show mute neutralsc with fast
    elif scrolled(14, korean=13):
        show mute wowsob with fast
        show hyunae hmmsc with fast
        ms "...why would it be any different...?"
    elif scrolled(43, korean=41):
        show hyunae boredsc with fast
        show mute hmphsc with fast
    elif scrolled(1000):
        show mute doubt with fast
        show hyunae oops with fast
        $ ts("I'm glad it's not just me!", "Okay, I don't understand what's noteworthy about this.", True)

    jump log_loop

label log_4_5_xharem:
    if scrolled(10, korean=9):
        show hyunae annoyedso with fast
        show mute annoyed3 with fast
        $ ts("Geeze, so much cursing, even in politics...!", "It's uncivilized is what it is!")
    elif scrolled(26, korean=24):
        show hyunae hardsc with fast
        show mute hmphsc with fast
    elif scrolled(32, korean=29):
        show mute neutralsc with fast
        show hyunae bittersc with fast
        ms "Hm."
    elif scrolled(40, korean=37):
        if any_read("M3-2", "M3-3", "M3-5", "M4-1", "M4-5", "M6-3", "M6-7"):
            show mute wowsob with fast
            show hyunae hmmsc with fast
            ms "As in... Queen Eun-a would have ultimate oversight of the council...? Oh..."
        else:
            show hyunae hmmso with fast
            show mute talk4 with fast
            $ ts("I'm not really getting much of this...", "It's okay, dear.")
    elif scrolled(71, korean=66):
        show hyunae hmphsc with fast
        show mute wowscb with fast
    elif scrolled(90, korean=86):
        show mute hatesob with fast
        show hyunae hmmso with fast
        $ ts("...yeah...", "...hanging out nobles to dry? How barbaric...", True)
    elif scrolled(110, korean=106):
        show hyunae hmphsc with fast
        show mute tensesc with fast
    elif scrolled(124, korean=121):
        show hyunae bittersc with fast
        show mute hmphsc with fast
    elif scrolled(150, korean=147):
        show hyunae hmmsc with fast
        show mute wowsc with fast
    elif scrolled(174, korean=170):
        show hyunae sternsc with fast
        show mute hmm with fast
    elif scrolled(182, korean=178):
        show mute challengeso with fast
        show hyunae hmmsc with fast
        ms "What? Of course it makes a difference—respecting elders is important!"
    elif scrolled(194, korean=190):
        show mute tensesob with fast
        show hyunae hardsc with fast
        ms "So... \"Meritocracy\" wasn't meant to change anything, then. How corrupt..."
    elif scrolled(204, korean=200):
        show hyunae hmphsc with fast
        show mute thought with fast
    elif scrolled(214, korean=210):
        show hyunae hmphsc with fast
        show mute hmphscb with fast
    elif scrolled(224, korean=221):
        show hyunae annoyedsc with fast
        show mute hmphscb with fast
    elif scrolled(238, korean=235):
        show hyunae annoyedsc with fast
        show mute tensesc with fast
    elif scrolled(242, korean=239):
        show hyunae bitterscb with fast
        show mute tensesc with fast
    elif scrolled(1000):
        show hyunae tired with fast
        show mute suspicious blush with fast

    jump log_loop

label log_4_6_xharem:
    if scrolled(8, korean=9):
        show mute hatesob with fast
        show hyunae oops with fast
        $ ts("...you don't think Councillor Yang was worse?", "...what unbelievable rudeness from Old *Mute!", True)
    elif scrolled(19, korean=19):
        show mute annoyed3 with fast
        show hyunae grr with fast
        ms "That's not my place to say."
    elif scrolled(27, korean=27):
        show mute challengesob with fast
        show hyunae hopelesssc with fast
        ms "...I can't believe it... I was this much of a shrew in the past...?!"
    elif scrolled(35, korean=32):
        show mute upset2 with fast
        show hyunae sigh blush with fast
        $ ts("If you say so...", "Like, no wonder the ministers thought I was trouble, having known her!", True)
    elif scrolled(42, korean=41):
        show hyunae flustered with fast
        show mute hmphsc with fast
        hs "Wait, I thought engineering was supposed to be our family! Why is his name Han...?"
    elif scrolled(53, korean=52):
        show hyunae hmmsc with fast
        show mute tensescb with fast
    elif scrolled(63, korean=62):
        show mute astonished blush with fast
        show hyunae hmmsob with fast
        $ ts("Is that a bad thing?", "...I used to have that kind of power?!", True)
    elif scrolled(73, korean=72):
        show mute give up with fast
        show hyunae baffled with fast
        ms "No, it's just... like... did she think wearing pants let her dictate to men like that?!"
    elif scrolled(86, korean=87):
        show hyunae hmmccb with fast
        show mute upsetscb with fast
    elif scrolled(111, korean=111):
        show hyunae annoyedsc with fast
        show mute tensescb with fast
    elif scrolled(130, korean=130):
        show hyunae bittersc with fast
        show mute wowscb with fast
    elif scrolled(143, korean=144):
        show mute whatsob with fast
        show hyunae emo with fast
        ms "WHOA."
    elif scrolled(153, korean=154):
        show hyunae hmmscb with fast
        show mute upsetsc with fast
    elif scrolled(173, korean=172):
        show hyunae hmmscb with fast
        show mute challengescb with fast
    elif scrolled(189, korean=190):
        show hyunae losssc with fast
        show mute tensesc with fast
    elif scrolled(207, korean=208):
        show mute hmphso with fast
        show hyunae hopelesssc with fast
        ms "...geeze, she sure deserved that one."
    elif scrolled(245, korean=245):
        show hyunae sighsc with fast
        show mute neutralsc with fast
    elif scrolled(1000):
        show hyunae tired with fast
        show mute tired with fast
    
    jump log_loop

label log_4_7_xharem:
    if scrolled(8, korean=5):
        if any_read("M1-1", "M6-1", "M6-2", "M6-4", "M6-5", "M6-6", "M6-7", "M6-8", "M6-9"):
            show mute astonished with fast
            show hyunae melancholic with fast
            $ ts("Well, what about, like, the Heo family?", "Huh? Why wouldn't a family be led by the eldest son...?", True)
        else:
            show mute astonished with fast
            show hyunae hmmsc with fast
            ms "Huh? Why wouldn't a family be led by the eldest son...?"
    elif scrolled(16, korean=12) and any_read("M1-1", "M6-1", "M6-2", "M6-4", "M6-5", "M6-6", "M6-7", "M6-8", "M6-9"):
        show mute challenge3 with fast
        show hyunae hmmccb with fast
        ms "Right! That's the sort of thing I'm talking about! How does something like that happen?"
    elif scrolled(24, korean=20):
        show hyunae hmmco with fast
        show mute tsundere with fast
        $ ts("I have to admit... I don't really get all this stuff about money...", "Well, you were a royal consort, you didn't have to.")
    elif scrolled(38, korean=34):
        show hyunae boredsc with fast
        show mute hmphsc with fast
    elif scrolled(48, korean=44):
        show mute hateso with fast
        show hyunae hmphsc with fast
        ms "...tch, how rude of her...!"
    elif scrolled(54, korean=51):
        show hyunae hmmsc with fast
        show mute tensesc with fast
    elif scrolled(87, korean=81):
        show hyunae hardsc with fast
        show mute hmphsc with fast
    elif scrolled(1000):
        show hyunae neutral with fast
        show mute suspicious blush with fast
    
    jump log_loop

label log_4_8_xharem:
    if scrolled(8, korean=9):
        show mute abashed blush with fast
        show hyunae bitterscb with fast
        ms "...she's completely out of control."
    elif scrolled(16, korean=18):
        show mute give up with fast
        show hyunae surrender blush with fast
        ms "...I can't believe..."
    elif scrolled(41, korean=42):
        show hyunae hardscb with fast
        show mute pressure with fast
    elif scrolled(52, korean=53):
        show hyunae annoyedscb with fast
        show mute challengescb with fast
    elif scrolled(62, korean=63):
        show hyunae bittersob with fast
        show mute challenge3 with fast
        $ ts("I still don't get any of this... what are they talking about...?", "Well, it's the social class that families like Heo were part of in our time...")
    elif scrolled(79, korean=80):
        show hyunae hardscb with fast
        show mute sorryscb with fast
    elif scrolled(96, korean=98):
        show hyunae hmphsc with fast
        show mute hmphscb with fast
    elif scrolled(119, korean=121):
        show hyunae hmmscb with fast
        show mute sigh with fast
    elif scrolled(127, korean=129):
        show hyunae hopelesssc with fast
        show mute annoyed with fast
    elif scrolled(1000):
        show mute damn with fast
        show hyunae tired with fast
        ms "I'd never be like that! I can be chatty, but... there's a time and place for that!"

    jump log_loop

label log_4_9_xharem:
    if scrolled(8, korean=8):
        show mute damn with fast
        show hyunae bittersc with fast
        ms "...I spoke like that to Emperor Taejo...?!"
    elif scrolled(16, korean=17):
        show hyunae annoyedsc with fast
        show mute whatsob with fast
    elif scrolled(23, korean=24):
        show hyunae bittersob with fast
        show mute hmph with fast
        hs "...I don't really get it, but..."
    elif scrolled(31, korean=31):
        show hyunae sighsob with fast
        show mute upset2 with fast
        $ ts("...it really seems like she believes strongly about this...", "...I know! Over Ryu himself!")
    elif scrolled(46, korean=47):
        show hyunae hmmsc with fast
        show mute whatscb with fast
    elif scrolled(56, korean=57):
        show mute pissed with fast
        show hyunae hmphsc with fast
        ms "...I can't believe I'd defend the principles of that awful society like this..."
    elif scrolled(82, korean=83):
        show hyunae bitterscb with fast
        show mute challengescb with fast
    elif scrolled(92, korean=93):
        show mute hateso with fast
        show hyunae hardsob with fast
        $ ts("...well, that would be...", "Geeze, if she'd gotten her way... things would be so different!", True)
    elif scrolled(103, korean=105):
        show mute complain with fast
        show hyunae pout with fast
        $ ts("Nothing...", "That would be what?", True)
    elif scrolled(116, korean=118):
        show hyunae sighscb with fast
        show mute craftyscb with fast
    elif scrolled(128, korean=130):
        show hyunae pressuresc with fast
        show mute wowsob with fast
    elif scrolled(152, korean=155):
        show hyunae defensivescb with fast
        show mute nicescb with fast
    elif scrolled(176, korean=177):
        show hyunae bitterscb with fast
        show mute grinsob with fast
    elif scrolled(183, korean=185):
        show mute astonished with fast
        show hyunae hopelesssc with fast
        ms "Wow..."
    elif scrolled(1000):
        show mute tch with fast
        show hyunae disappoint with fast
        ms "Just wow..."

    jump log_loop

label log_5_1_xharem:
    if scrolled(11, korean=11):
        if read("M1-6"):
            show mute nicesob with fast
            show hyunae thinksc with fast
            ms "Well, at least {i}someone{/i} appreciates family gatherings..."
        else:
            show hyunae starescb with fast
            show mute nicesc with fast
            hs "Hm..."
    elif scrolled(19, korean=20):
        if not any_read("M5-2", "M5-3", "M5-4", "M5-5", "M5-6", "M5-7", "M5-8", "M5-9"):
            show hyunae funsob with fast
            show mute wowsob with fast
            $ ts("Oh! She's an engineer! That's nice...!", "...why would a Kim woman need to have a job...?")
        else:
            show hyunae sure blush with fast
            show mute wowsob with fast
            $ ts("I really like that she's an engineer!", "...why would a Kim woman need to have a job...?")
    elif scrolled(27, korean=28):
        show hyunae sweetsob with fast
        show mute damn with fast
        $ ts("Yeah! That was exactly what I wanted to grow up to be like, too...! She understands...!", "Well, like, I don't!")
    elif scrolled(35, korean=35):
        show mute sighsob with fast
        show hyunae hardsob with fast
        $ ts("I really don't think that's unusual...", "Wow, still unmarried at 22? That poor woman...", True)
    elif scrolled(41, korean=41):
        show hyunae hardsc with fast
        show mute upset3 with fast
    elif scrolled(49, korean=50):
        show mute hmm2 with fast
        show hyunae hmph2 with fast
        $ ts("...I'm just jealous that she was able to say \"no.\"", "...her grandmother sounds like a good woman, at least! Even if it's late...", True)
    elif scrolled(1000):
        show hyunae hmm with fast
        show mute disbelief with fast
    jump log_loop

label log_5_2_xharem:
    if scrolled(4, korean=4):
        if read("M5-1"):
            show hyunae sweetsob with fast
            show mute nicescb with fast
            hs "So, she got married..."
        else:
            show hyunae funso with fast
            show mute nicescb with fast
            hs "So, she was newly-wed..."
    elif scrolled(12, korean=12):
        show hyunae satisfied blush with fast
        show mute polite blush with fast
        $ ts("...ah, that's really romantic, though...", "For once we're in agreement!")
    elif scrolled(20, korean=19):
        show mute whatsob with fast
        show hyunae surescb with fast
        ms "...but she's a woman! A newly married one, even!"
    elif scrolled(25, korean=24):
        show hyunae surescb with fast
        show mute sorryscb with fast
    elif scrolled(30, korean=29):
        show hyunae evasive with fast
        show mute tsundere with fast
        $ ts("That's nice, but... I don't get what \"silence requirements\" means...", "Um... like... not everyone is silent during marital affairs, *Hyun-ae...")
    elif scrolled(36, korean=35):
        show hyunae staresob with fast
        show mute wowsc with fast
        hs "I don't know what that means..."
    elif scrolled(44, korean=43):
        show hyunae sweetsob with fast
        show mute craftyscb with fast
        hs "OH. Never mind, I get it now..."
    elif scrolled(1000):
        show hyunae gomen with fast
        show mute brag blush with fast
        $ ts("Aw, they sound like a cute couple... I'm happy for them!", "Ha, serves her right for teasing like that!")

    jump log_loop

label log_5_3_xharem:
    if scrolled(5, korean=3):
        show mute tch with fast
        show hyunae hmphsc with fast
        ms "...a noble man working under a woman...? Tch..."
    elif scrolled(17, korean=14):
        show hyunae funsc with fast
        show mute wowscb with fast
    elif scrolled(33, korean=30):
        show hyunae gomen with fast
        show mute upset2 with fast
        $ ts("I don't know, I'd really like it if someone touched me like that...", "...not your husband? Do you not realize...?")
    elif scrolled(40, korean=37):
        show hyunae flustered with fast
        show mute upsetscb with fast
        $ ts("Whoa! Really? I mean... I remember, that was a really big problem in my time...!", "Yeah... it was, but was that really why?")
    elif scrolled(51, korean=47):
        show mute insecure with fast
        show hyunae huhsc with fast
        ms "...like, that's a fascinating theory, but... don't invite an unrelated man alone into your home...!"
    elif scrolled(62, korean=58):
        show mute worry3 with fast
        show hyunae guilt with fast
        $ ts("Yes... oh, geeze...", "...now do you see what I was getting at?", True)
    elif scrolled(72, korean=68):
        show hyunae losssob with fast
        show mute upsetscb with fast
        $ ts("Oh no!", "Ugh, no, of course he did...")
    elif scrolled(81, korean=77):
        show mute shame with fast
        show hyunae surrender with fast
        ms "...you led him on, So-yi... oh no..."
    elif scrolled(101, korean=98):
        show hyunae bitterscb with fast
        show mute upsetsc with fast
    elif scrolled(112, korean=109):
        show hyunae pressurescb with fast
        show mute sighsob with fast
    elif scrolled(120, korean=117):
        show hyunae bittersob with fast
        show mute shame with fast
        $ ts("...that sounds so scary...", "...I'm so sorry you had to read this, *Hyun-ae.")
    elif scrolled(131, korean=127):
        show hyunae surrender blush with fast
        show mute sorryscb with fast
    elif scrolled(139, korean=135):
        show mute upsetsob with fast
        show hyunae hmmscb with fast
        ms "Tell your husband! It's his {i}duty{/i} to protect you...!"
    elif scrolled(149, korean=145):
        show mute tensescb with fast
        show hyunae hopelessscb with fast
        ms "Ugh..."
    elif scrolled(162, korean=157):
        show hyunae sigh blush with fast
        show mute sorryscb with fast
    elif scrolled(176, korean=171):
        show hyunae surrender blush with fast
        show mute sighscb with fast
    elif scrolled(183, korean=178):
        show hyunae hopelessscb with fast
        show mute upsetsc with fast
    elif scrolled(199, korean=192):
        show mute damn with fast
        show hyunae bittersob with fast
        $ ts("I... I had no idea... that's horrible!", "See? This is why it's bad for women to work... things like this happen!", True)
    elif scrolled(1000):
        show hyunae troubled with fast
        show mute worry side with fast
    jump log_loop

label log_5_4_xharem:
    if scrolled(8, korean=4):
        show hyunae hmmcob with fast
        show mute give up with fast
        $ ts("Sounds like hard work... so that's what it's like to be an adult...?", "No, it's what it's like to be a woman with bad priorities!")
    elif scrolled(16, korean=12):
        show mute hmphsob with fast
        show hyunae bitterscb with fast
        ms "That's fair."
    elif scrolled(24, korean=20):
        show hyunae annoyedscb with fast
        show mute upsetsc with fast
    elif scrolled(32, korean=27):
        show hyunae sighsob with fast
        show mute damn with fast
        $ ts("I guess even in a time when women were allowed to work, things were complicated...", "...that's {i}why{/i} things were complicated.")
    elif scrolled(40, korean=36):
        show mute upsetsob with fast
        show hyunae hmmscb with fast
        ms "What? But... that's the best age to have children at!"
    elif scrolled(56, korean=51):
        show hyunae bitterscb with fast
        show mute upsetsc with fast
    elif scrolled(74, korean=69):
        show hyunae surrender blush with fast
        show mute tired blush with fast
    elif scrolled(1000):
        show mute shame with fast
        show hyunae baffled with fast
        $ ts("I... I guess...", "I guess a woman getting emotional about things like that can't be helped...", True)

    jump log_loop

label log_5_5_xharem:
    if scrolled(4, korean=3):
        show mute upsetsob with fast
        show hyunae emo with fast
        $ ts("I'm sure she's just busy!", "...oh, geeze, she needs to clean up badly...", True)
    elif scrolled(14, korean=11):
        show mute sighsob with fast
        show hyunae hmmscb with fast
        ms "...oh, So-yi, it's not your fault you're naïve... it's just how you were raised."
    elif scrolled(24, korean=21):
        show hyunae hmmsob with fast
        show mute tensesob with fast
        $ ts("So... that really was the cause, then...? But if they knew back then, then why...?", "...wait, really? Like, did she have evidence...?")
    elif scrolled(32, korean=28):
        show hyunae annoyedscb with fast
        show mute sighscb with fast
    elif scrolled(39, korean=35):
        show hyunae surrender with fast
        show mute tensescb with fast
    elif scrolled(49, korean=45):
        show mute give up with fast
        show hyunae pressuresob with fast
        $ ts("Aaagh! That's so gross!", "Disgusting!", True)
    elif scrolled(61, korean=58):
        show mute worry with fast
        show hyunae bitterscb with fast
    elif scrolled(69, korean=66):
        show mute insecure with fast
        show hyunae bitterscb with fast
        ms "...that shouldn't be the most important thing to her! Her husband should!"
    elif scrolled(81, korean=79):
        show mute sob with fast
        show hyunae pout with fast
        $ ts("I don't think...", "Really, if she'd just see that it's for the better...", True)
    elif scrolled(90, korean=89):
        show mute bitter with fast
        show hyunae annoyedsob with fast
        $ ts("...nothing.", "\"You don't think\" what...?", True)
    elif scrolled(109, korean=109):
        show hyunae bittersc with fast
        show mute tired blush with fast
    elif scrolled(130, korean=129):
        show mute shame with fast
        show hyunae losssc with fast
        ms "...she seems like a good woman! Just... with confused priorities."
    elif scrolled(140, korean=139):
        show hyunae melancholic with fast
        show mute worry3 with fast
        $ ts("You at least like her husband, though, right? He's so understanding!", "Yes, *Hyun-ae, he's okay...")
    elif scrolled(152, korean=151):
        show hyunae hopelessscb with fast
        show mute cry with fast
        ms  "...although I wish he'd be more protective of her."
    elif scrolled(164, korean=161):
        show hyunae depressed blush with fast
        show mute pout with fast
    elif scrolled(1000):
        show hyunae anxious with fast
        show mute tired with fast

    jump log_loop

label log_5_6_xharem:
    if scrolled(8, korean=9):
        show mute hmphso with fast
        show hyunae pressuresob with fast
        $ ts("...oh no, does he really think that...?! That's awful!", "Finally, something by the man...", True)
    elif scrolled(17, korean=18):
        show mute upsetsob with fast
        show hyunae annoyedscb with fast
        ms "...no, of course it's not healthy!"
    elif scrolled(22, korean=23):
        show hyunae surrender with fast
        show mute whatscb with fast
    elif scrolled(27, korean=28):
        show hyunae bittersob with fast
        show mute sighsob with fast
        hs "...oh... geeze..."
    elif scrolled(35, korean=38):
        show mute upset2 with fast
        show hyunae sigh blush with fast
        $ ts("...oh, \"worthless as a wife\" was her words, not his... I see...", "...she kind of is, though... it's just not her fault!", True)
    elif scrolled(46, korean=50):
        show hyunae sighsob with fast
        show mute upsetsob with fast
        $ ts("I guess... it's hard even for her to be strong for so long...", "Um, of course! I wish the poor woman would realize it's okay for her to be weak.")
    elif scrolled(63, korean=68):
        show hyunae troubled with fast
        show mute sorrysc with fast
    elif scrolled(73, korean=78):
        show hyunae bittersob with fast
        show mute sorryscb with fast
        hs "So even she worried about those things? Oh..."
    elif scrolled(98, korean=105):
        show hyunae hopelessscb with fast
        show mute upsetsc with fast
    elif scrolled(106, korean=113):
        show hyunae hmmcob with fast
        show mute upsetsc with fast
    elif scrolled(115, korean=123):
        show hyunae depressed blush with fast
        show mute hmphscb with fast
    elif scrolled(124, korean=132):
        show hyunae bitterscb with fast
        show mute upsetscb with fast
    elif scrolled(138, korean=147):
        show hyunae annoyedsob with fast
        show mute upset3 with fast
        $ ts("\"Connecting people\"? Is it really? I never thought of it like that...", "...no, that's pretty weird, it's not just you.")
    elif scrolled(146, korean=155):
        if read("M5-5"):
            show hyunae pressuresob with fast
            show mute pissed with fast
            $ ts("...wait... is she re-enacting... aaaaagh, geeze, So-yi...!", "...aaagh, she sure is!")
        else:
            show hyunae losssob with fast
            show mute upsetsob with fast
            $ ts("...wow, this is intense...", "...yes, I don't think I needed to hear about this.")
    elif scrolled(153, korean=162):
        if read("M5-5"):
            show hyunae sigh blush with fast
            show mute bitter with fast
            $ ts("...oh... oh... wait, but... she never mentioned that...", "...oh no. Did that also...? Ugh, that's awful...!")
        else:
            show hyunae surrender blush with fast
            show mute upsetsc with fast
            hs "...oh... oh..."
    elif scrolled(160, korean=169):
        show mute give up with fast
        show hyunae lossscb with fast
        ms "It'd be a start, you idiot..."
    elif scrolled(168, korean=177):
        show hyunae defensive with fast
        show mute worry with fast
        hs "...of course, you idiot husband!"
    elif scrolled(178, korean=185):
        show mute insecure with fast
        show hyunae pity with fast
        $ ts("...do you really think that's the case...?", "Agh, no, don't encourage that! You're just going to make her retreat even further!", True)
    elif scrolled(1000):
        show hyunae anxious with fast
        show mute tired blush with fast
    
    jump log_loop

label log_5_7_xharem:
    if scrolled(4, korean=2):
        show hyunae staresob with fast
        show mute upset3 with fast
        $ ts("Ah! That's me! That's me, that's me! She's writing about me!", "...yes, dear, we know.")
    elif scrolled(12, korean=10):
        show hyunae pout with fast
        show mute hmphsc with fast
        hs "Well... I guess that story sorta came true after all, huh..."
    elif scrolled(25, korean=21):
        show hyunae staresc with fast
        show mute wowsc with fast
    elif scrolled(31, korean=27):
        show hyunae satisfied blush with fast
        show mute annoyed3 with fast
        $ ts("\"Earthborn brilliance\"? Finally, someone who acknowledges that my real parents were smarter!", "...so you respect {i}some{/i} of your ancestors, at least.")
    elif scrolled(43, korean=41):
        show hyunae sweetsc with fast
        show mute upsetscb with fast
    elif scrolled(51, korean=46):
        show mute whatsob with fast
        show hyunae pout with fast
        $ ts("...it seems obvious to me...", "Wait... how did she figure it out when Kim Jung-su couldn't...?", True)
    elif scrolled(59, korean=54):
        show hyunae bittersob with fast
        show mute tch with fast
        $ ts("...very unfounded...", "...sorry.{k=1}{/k}")
    elif scrolled(67, korean=62):
        show hyunae flustered with fast
        show mute wowsc with fast
        hs "I... I did...?!"
    elif scrolled(77, korean=71):
        show hyunae hmmsob with fast
        show mute whatscb with fast
        hs "I don't remember this at all...!"
    elif scrolled(85, korean=79):
        show hyunae hmph3 with fast
        show mute tensesc with fast
        hs "Ah... well, it was for a good cause, so I don't mind..."
    elif scrolled(94, korean=87):
        show mute embarrassed with fast
        show hyunae oops with fast
        $ ts("...I hadn't thought of that... you're right!", "You know... maybe it would have been better for everyone if she'd just kept you awake.", True)
    elif scrolled(1000):
        show mute worry2 with fast
        show hyunae baffled with fast
        ms "...she sounds really obsessive. It's worrying..."

    jump log_loop

label log_5_8_xharem:
    if scrolled(8, korean=7):
        show mute sigh blush with fast
        show hyunae losssc with fast
        ms "...she's really not doing okay."
    elif scrolled(15, korean=14):
        show hyunae annoyedsob with fast
        show mute sweetsob with fast
        $ ts("...harsh...", "That's good of them, though!")
    elif scrolled(23, korean=22):
        show hyunae pout with fast
        show mute bitter with fast
        $ ts("...why would people be afraid to talk to her? I don't understand...", "What? Just look at her! Of course they're afraid of that poor fragile obsessed woman!")
    elif scrolled(30, korean=29):
        show hyunae emo2 with fast
        show mute hmphscb with fast
    elif scrolled(38, korean=36):
        show hyunae bittersob with fast
        show mute sighsob with fast
        $ ts("What she's discovering is shocking, but...", "...okay, but... she needs to learn to prioritize.")
    elif scrolled(1000):
        show hyunae anxious with fast
        show mute worry with fast
    
    jump log_loop

label log_5_9_xharem:
    if scrolled(8, korean=5):
        show mute sorrysob with fast
        show hyunae hmmscb with fast
        ms "...of course he doesn't share your optimism..."
    elif scrolled(17, korean=14):
        show mute upsetsob with fast
        show hyunae surrender blush with fast
        $ ts("Oh no...", "...did he just give up on her? Oh, geeze...", True)
    elif scrolled(25, korean=22):
        show hyunae bittersob with fast
        show mute sighsob with fast
        $ ts("...oh...", "She just doesn't get it...")
    elif scrolled(33, korean=30):
        show hyunae losssob with fast
        show mute give up with fast
        $ ts("Why are they fighting? I thought he was good for her...", "...it's hard, but he should have been like this a long time ago... for her own good!")
    elif scrolled(44, korean=40):
        show hyunae troubled with fast
        show mute sorryscb with fast
    elif scrolled(58, korean=55):
        show mute sob with fast
        show hyunae hopelessscb with fast
        ms "Ugh... okay, like, this is just painful to read."
    elif scrolled(74, korean=71):
        show hyunae lossscb with fast
        show mute hmphscb with fast
    elif scrolled(99, korean=98):
        show hyunae sighscb with fast
        show mute sorryscb with fast
    elif scrolled(107, korean=106):
        show hyunae hopelesssob with fast
        show mute apologize with fast
        $ ts("...I'm so glad!", "Yeah!")
    elif scrolled(115, korean=114):
        show hyunae surrender blush with fast
        show mute sorrysob with fast
        $ ts("It's so nice that they agreed on these things together...! He's so nice...", "Yeah, good for him.")
    elif scrolled(123, korean=122):
        show mute give up with fast
        show hyunae hmmscb with fast
        ms "...no, never mind. Agh, geeze, you didn't even mean it? Can't you see you'd be happier that way...?!"
    elif scrolled(131, korean=131):
        show hyunae flustered with fast
        show mute worry3 with fast
        $ ts("Wait, but that date is right before...! ...oh, I get it...", "...right before the computers were wiped, yep.")
    elif scrolled(143, korean=143):
        show hyunae losssob with fast
        show mute shame with fast
    elif scrolled(1000):
        show hyunae shame with fast
        show mute cry with fast
        $ ts("...well... at least she had such a sweet husband at her side...", "That's what counts... but like, she must have been devastated.")

    jump log_loop

label log_6_1_xharem:
    if scrolled(3, korean=4):
        show hyunae hmmsob with fast
        show mute hateso with fast
        $ ts("Geeze, she's scary...", "And {i}rude{/i}!")
    elif scrolled(11, korean=11):
        show hyunae hmmcob with fast
        show mute hateso with fast
        $ ts("...huh... that's all because of \"Meritocracy\"...?", "...apparently.")
    elif scrolled(22, korean=22):
        show hyunae annoyedsc with fast
        show mute tensescb with fast
    elif scrolled(37, korean=38):
        show mute wowsob with fast
        show hyunae bittersc with fast
        ms "Huh..."
    elif scrolled(46, korean=47):
        show mute challengeso with fast
        show hyunae oops with fast
        $ ts("Don't you sympathize, though...?", "...tch, how disrespectful...", True)
    elif scrolled(55, korean=56):
        if any_read("M6-5", "M6-6", "M6-7", "M6-8"):
            show mute tch with fast
            show hyunae baffled with fast
            $ ts("Yeah...", "...I guess it turned out to be true, though...", True)
        else:
            show mute give up with fast
            show hyunae troubled with fast
            ms "...wow, what a thing to suggest..."
    elif scrolled(64, korean=67):
        show hyunae sigh with fast
        show mute tensescb with fast
    elif scrolled(1000):
        show hyunae disappoint with fast
        show mute serious with fast
    jump log_loop

label log_6_2_xharem:
    if scrolled(9, korean=10):
        show hyunae lost with fast
        show mute give up with fast
        $ ts("Yeah... nobody deserves that!", "...I knew it would come to this, but still... like, that's awful.")
    elif scrolled(18, korean=20):
        show hyunae guilt with fast
        show mute tensescb with fast
        hs "...geeze..."
    elif scrolled(26, korean=28):
        show mute hmphsob with fast
        show hyunae pressureso with fast
        $ ts("Yeah... I'm with Old *Mute on this... I think that's good of her.", "...well... I know dressing down an elder male relative is wrong, but... in this case...", True)
    elif scrolled(41, korean=44):
        show mute bitter with fast
        show hyunae losssob with fast
        $ ts("I guess...", "It's a hard truth, but... he's surely not wrong...", True)
    elif scrolled(53, korean=56):
        show mute insecure with fast
        show hyunae depressed blush with fast
        ms "...whoa, geeze! See... that's why women security officers are a terrible idea!"
    elif scrolled(63, korean=67):
        show hyunae surrender blush with fast
        show mute challengesc with fast
    elif scrolled(75, korean=80):
        show hyunae weak2 with fast
        show mute hatesc with fast
    elif scrolled(83, korean=88):
        show hyunae defensive with fast
        show mute hatesob with fast
        $ ts("...that's an awful thing to say...!", "That is still not okay!")
    elif scrolled(95, korean=100):
        show hyunae oops with fast
        show mute astonished with fast
    elif scrolled(111, korean=117):
        show hyunae hmmscb with fast
        show mute challenge2 with fast
    elif scrolled(127, korean=134):
        show mute damn with fast
        show hyunae sigh with fast
        ms "She's just too emotional to be given that kind of responsibility... she clearly can't handle it!"
    elif scrolled(145, korean=153):
        show hyunae sighsc with fast
        show mute suspicious blush with fast
    elif scrolled(153, korean=161):
        show mute abashed with fast
        show hyunae sad with fast
        $ ts("Well, maybe she means...", "Wait... how was he not the most important...?!", True)
    elif scrolled(175, korean=186):
        show hyunae melancholic with fast
        show mute tch with fast
    elif scrolled(183, korean=194):
        show hyunae pity with fast
        show mute tensesob with fast
        $ ts("Of course! She's still you, after all!", "...so even a man-hater like Old *Mute could feel love...", True)
    elif scrolled(191, korean=203):
        show mute challenge4 with fast
        show hyunae baffled with fast
        $ ts("Nothing, nothing!", "Wait, what's that supposed to mean?!", True)
    elif scrolled(204, korean=217):
        show hyunae surrender blush with fast
        show mute hmphscb with fast
    elif scrolled(212, korean=226):
        show hyunae hmmsob with fast
        show mute annoyed3 with fast
        $ ts("Wait, is she saying...? Even at that time, men did things like that with...?", "Men will always be men, dear.")
    elif scrolled(229, korean=243):
        show hyunae hardscb with fast
        show mute hmphscb with fast
    elif scrolled(240, korean=255):
        show hyunae hardsc with fast
        show mute upsetsc with fast
    elif scrolled(250, korean=266):
        show mute hatesc with fast
        show hyunae sighsc with fast
        ms "Ugh..."
    elif scrolled(267, korean=285):
        show hyunae sighscb with fast
        show mute worry with fast
    elif scrolled(277, korean=296):
        show hyunae annoyedscb with fast
        show mute disbelief blush with fast
    elif scrolled(284, korean=303):
        show hyunae sigh blush with fast
        show mute upset3 with fast
        $ ts("Wow, that's... kind of cool of *Mute, actually...", "...okay, okay, it's good for her to be protective, at least.")
    elif scrolled(1000):
        show mute cry with fast
        show hyunae sulk with fast
        ms "But still, a woman shouldn't have to be given the impossible task of protecting her husband... that's just not fair..."

    jump log_loop

label log_6_3_xharem:
    if scrolled(7, korean=8):
        if any_read("M1-1", "M1-6", "M1-7", "M6-3") and any_read("M1-1", "M1-3", "M1-6", "M6-2"):
            show hyunae hmmsob with fast
            show mute hmphsc with fast
            hs "Ah, so this is about Seo-yeong's husband..."
        else:
            show hyunae hmmsc with fast
            show mute hateso with fast
            $ ts("Hm...", "Tch...")
    elif scrolled(17, korean=19):
        show mute give up with fast
        show hyunae tsundere with fast
        $ ts("There's lots of good things written in hangeul, you know!", "...if the language of the classics isn't good enough for you, what is?", True)
    elif scrolled(25, korean=27):
        show mute annoyed3 with fast
        show hyunae awkward with fast
        $ ts("...there's other things...", "Like what, *Hyun-ae? Your silly comics about maids?", True)
    elif scrolled(39, korean=42):
        show hyunae sigh blush with fast
        show mute hmphscb with fast
    elif scrolled(47, korean=49):
        show mute upset3 with fast
        show hyunae bittersc with fast
        ms "This sure is, like, a lot of flowery language to defend barbarianism..."
    elif scrolled(59, korean=62):
        show hyunae hmmsob with fast
        show mute tsundere with fast
        $ ts("Geeze, what's with the swearing, though?", "Well, like, this was a speech meant for men to hear, so it's okay.")
    elif scrolled(73, korean=70):
        show mute hmm2 with fast
        show hyunae hmmsc with fast
        ms "Good advice..."
    elif scrolled(1000):
        show hyunae tired with fast
        show mute think with fast

    jump log_loop

label log_6_4_xharem:
    if scrolled(6, korean=2):
        if any_read("M2-2", "M2-3") and not any_read("M6-7", "M6-8"):
            show hyunae hmmsob with fast
            show mute shame with fast
            $ ts("...so they never found out who killed Professor Kim, after all...?", "I guess not.")
        else:
            show mute tenseso with fast
            show hyunae surrender with fast
            ms "...so here's the part she couldn't deal with, huh..."
    elif scrolled(20, korean=16):
        show hyunae emo2 with fast
        show mute wowsob with fast
    elif scrolled(28, korean=25):
        show mute damn with fast
        show hyunae busy with fast
        $ ts("I'm sure it was important...", "Old *Mute wouldn't even let her be a good mother?", True)
    elif scrolled(34, korean=31):
        show mute bitter with fast
        show hyunae hardscb with fast
        ms "Ugh, geeze, *Hyun-ae, what could possibly be more important than being a good mother?"
    elif scrolled(41, korean=38):
        show hyunae sighscb with fast
        show mute upsetsc with fast
    elif scrolled(49, korean=47):
        show mute whatsob with fast
        show hyunae huhsc with fast
        ms "Wow. Yikes."
    elif scrolled(61, korean=59):
        show mute hateso with fast
        show hyunae guilt with fast
        $ ts("I know I'd be terrified!", "...ugh, it's just... completely unfair to put a woman in that situation!", True)
    elif scrolled(80, korean=77):
        show hyunae pressurescb with fast
        show mute sorryscb with fast
    elif scrolled(97, korean=94):
        show hyunae bitterscb with fast
        show mute tensescb with fast
    elif scrolled(113, korean=110):
        show hyunae annoyedscb with fast
        show mute tensesc with fast
    elif scrolled(121, korean=117):
        show hyunae grumpy with fast
        show mute upsetscb with fast
        $ ts("Really? They were going to arrest the President?", "...that's really serious, wow.")
    elif scrolled(129, korean=126) and any_read("M1-2", "M1-4", "M4-2", "M4-9"):
        show hyunae bittersob with fast
        show mute inquisitive2 with fast
        $ ts("...I thought *Mute didn't like the President, though... why are they...?", "Because, like, that's what being in charge of security means. It's her duty.")
    elif scrolled(149, korean=146):
        show hyunae sighsc with fast
        show mute hmphscb with fast
    elif scrolled(162, korean=160):
        show hyunae sighsc with fast
        show mute sorrysc with fast
    elif scrolled(174, korean=172):
        show hyunae lossso with fast
        show mute upsetscb with fast
        hs "...wow, intense..."
    elif scrolled(182, korean=180):
        show mute hatesob with fast
        show hyunae losssc with fast
        ms "Intense is an understatement... like, she's way too emotionally volatile for this..."
    elif scrolled(208, korean=207):
        show hyunae sighsc with fast
        show mute challengesc with fast
    elif scrolled(227, korean=227):
        show hyunae depressed with fast
        show mute tired blush with fast
    elif scrolled(235, korean=236):
        show hyunae lost with fast
        show mute bitter with fast
        $ ts("...I guess it's hard to be tough, huh...", "Yeah... see how it's just not really suited for how emotional women are?")
    elif scrolled(1000):
        show mute shame with fast
        show hyunae troubled with fast
        ms "It's just not fair for her..."

    jump log_loop

label log_6_5_xharem:
    if scrolled(8, korean=8):
        show mute challengeso with fast
        show hyunae huh with fast
        ms "...yes, and the ship was a better place for it, you petty woman!"
    elif scrolled(20, korean=21):
        show hyunae bittersc with fast
        show mute challengesc with fast
    elif scrolled(30, korean=31):
        show hyunae huhsc with fast
        show mute whatscb with fast
    elif scrolled(41, korean=42):
        show mute wow3 with fast
        show hyunae tsundere with fast
        $ ts("What? You didn't know? I had a mission patch with him on it... he was really cool!", "Wait... what?! Navigation AI...?", True)
    elif scrolled(52, korean=54):
        show mute hmphsob with fast
        show hyunae sulk with fast
        ms "No... I didn't know. But it makes sense..."
    elif scrolled(61, korean=63):
        show mute tensescb with fast
        show hyunae sigh blush with fast
        ms "...oh..."
    elif scrolled(74, korean=77):
        show mute tensesob with fast
        show hyunae staresob with fast
        $ ts("You think so...?", "This dynamic... it's really uncomfortable...", True)
    elif scrolled(92, korean=96):
        show hyunae hmphscb with fast
        show mute craftyscb with fast
    elif scrolled(104, korean=107):
        show mute upset3 with fast
        show hyunae baffled with fast
        $ ts("Me neither... a thousand more years would be... I couldn't.", "...1600 years... I can't imagine, though...", True)
    elif scrolled(113, korean=116):
        show hyunae huhsc with fast
        show mute whatscb with fast
    elif scrolled(128, korean=131):
        show hyunae hmmscb with fast
        show mute hmphscb with fast
    elif scrolled(136, korean=138):
        show mute give up with fast
        show hyunae hopelessscb with fast
        ms "No, you shouldn't be able to! What the hell is {i}wrong{/i} with this society?!"
    elif scrolled(151, korean=151):
        show hyunae sighscb with fast
        show mute damn with fast
    elif scrolled(160, korean=161):
        show hyunae sigh blush with fast
        show mute hateso with fast
        $ ts("Somehow, this atmosphere feels really intimate...", "I know! It feels like... like, it doesn't feel like they're a pair of women, it feels like...")
    elif scrolled(172, korean=171):
        show mute complain with fast
        show hyunae grumpy with fast
        $ ts("But... she's trying...", "...Old *Mute, you liar.", True)
    elif scrolled(1000):
        show mute bitter with fast
        show hyunae lost with fast
        ms "It doesn't matter if she's trying... you know full well how this ends, that's not enough! This false confidence..."

    jump log_loop

label log_6_6_xharem:
    if scrolled(7, korean=5):
        show hyunae hmph2 with fast
        show mute hmphso with fast
        $ ts("...huh, I wonder if that was the same house I was in, or...?", "Not necessarily. The royal family has moved a {i}lot{/i}.")
    elif scrolled(15, korean=13):
        show mute sorrysob with fast
        show hyunae hmmscb with fast
        ms "...so women like Seo-yeong were just disconnected from reality...?"
    elif scrolled(25, korean=23):
        show mute tensesob with fast
        show hyunae sighsc with fast
        ms "It's not weird! Why would a woman like you even want to be there...?!"
    elif scrolled(33, korean=31):
        show mute whatever with fast
        show hyunae annoyedsob with fast
        $ ts("Wait, if she doesn't have a little sister, then who does she mean...?", "...a better family head wouldn't be so oblivious.", True)
    elif scrolled(44, korean=42) and any_read("M2-4", "M2-5", "M2-7", "M2-8"):
        show hyunae tsundere with fast
        show mute damn with fast
        $ ts("...OH, HER.", "...OH, HER.")
        # really need conditional here - Raide
    elif scrolled(54, korean=52):
        show hyunae baffled with fast
        show mute tensescb with fast
    elif scrolled(1000):
        if read("M1-5"):
            show hyunae unsure with fast
            show mute tch with fast
            $ ts("I think I liked the report with the potted plant thing better... this is awfully... well...", "...it's no place for a noblewoman, that's for sure.")
        else:
            show hyunae unsure with fast
            show mute tch with fast
            $ ts("This is awfully... well...", "...it's no place for a noblewoman, that's for sure.")

    jump log_loop

label log_6_7_xharem:
    if scrolled(13, korean=10):
        show mute tensesob with fast
        show hyunae hmmscb with fast
        ms "Um..."
    elif scrolled(27, korean=24):
        show hyunae hopelesssob with fast
        show mute damn with fast
        $ ts("I guess she must've felt powerless, huh...?", "...um, like, I'd expect the same thing if I spoke out of turn to a superior!")
    elif scrolled(35, korean=32):
        show hyunae hmmscb with fast
        show mute upsetsc with fast
        hs "Hm..."
    elif scrolled(47, korean=43):
        show hyunae huhscb with fast
        show mute tensesc with fast
    elif scrolled(60, korean=54):
        show hyunae hmphsc with fast
        show mute hmphsc with fast
    elif scrolled(74, korean=68):
        show hyunae evasive with fast
        show mute tensescb with fast
    elif scrolled(82, korean=76):
        if read("M6-9"):
            show mute hateso with fast
            show hyunae hmmccb with fast
            ms "...yeah... I guess we knew that..."
        else:
            show mute challenge4 with fast
            show hyunae hmmccb with fast
            ms "That can't be right. Emperor Taejo was above that!"
    elif scrolled(94, korean=89):
        show hyunae huhsc with fast
        show mute hmphsc with fast
    elif scrolled(101, korean=96):
        show hyunae sighsc with fast
        show mute tensesc with fast
    elif scrolled(112, korean=107) and any_read("M3-2", "M3-3", "M3-5", "M4-1", "M4-5", "M6-3"):
        show mute upset3 with fast
        show hyunae melancholic with fast
        $ ts("...Eun-a, right?", "...wait, they can't be talking about...", True)
    elif scrolled(127, korean=123):
        show hyunae hmphsc with fast
        show mute tensescb with fast
    elif scrolled(136, korean=133):
        show mute challenge4 with fast
        show hyunae huhsc with fast
        ms "...this isn't right! I don't believe this!"
    elif scrolled(144, korean=141):
        show mute astonished blush with fast
        show hyunae oops with fast
        $ ts("Do you think that was changed when you woke up...?", "...wait... Old *Mute could do that? I could never have used the root password... I'm not capable!", True)
    elif scrolled(156, korean=154):
        if read("M6-9"):
            show mute tch with fast
            show hyunae sulk with fast
            ms "You mean, like... do I think Queen Eun-a did it...? ...I guess so."
        else:
            show mute give up with fast
            show hyunae hmmscb with fast
            ms "You mean, like... do I think Queen Eun-a did it...? She couldn't have!"
    elif scrolled(170, korean=167):
        show mute sorrysob with fast
        show hyunae huhscb with fast
        if read("M6-9"):
            ms "She... she really was conpsiring against Emperor Taejo..."
        else:
            ms "She's... she's really conspiring against Emperor Taejo...?!"
    elif scrolled(183, korean=179):
        show hyunae annoyedsc with fast
        show mute hatesc with fast
    elif scrolled(203, korean=201):
        show hyunae hopelesssc with fast
        show mute upsetsc with fast
    elif scrolled(211, korean=209):
        show hyunae hmmscb with fast
        show mute astonished blush with fast
    elif scrolled(219, korean=217):
        if read("M6-9"):
            show mute shame with fast
            show hyunae troubled with fast
            ms "I can't believe it..."
        else:
            show mute abashed blush with fast
            show hyunae troubled with fast
            ms "Queen Eun-a was my friend in the past... I'd never have conspired against her!"
    elif scrolled(1000):
        if read("M6-9"):
            show hyunae mad blush with fast
            show mute cry with fast
            $ ts("What? Who? Was it...?!", "...who else could it have been?")
        else:
            show hyunae mad blush with fast
            show mute mad with fast
            $ ts("What? Who? Was it...?!", "No! It couldn't be! She was my friend! She was my mistress! Like, she even told me herself... this must be a lie, it doesn't make sense!")

    jump log_loop

label log_6_8_xharem:
    if scrolled(6, korean=9):
        if read("M1-2"):
            show hyunae hmphso with fast
            show mute tenseso with fast
            $ ts( "Huh... this has a different feeling than that other log with him...", "Just as uncomfortable, though...")
        else:
            show mute upsetscb with fast
            show hyunae hmphsc with fast
            ms "...ugh..."
    elif scrolled(19, korean=26):
        show mute sighsob with fast
        show hyunae bittersc with fast
        ms "...I just... I don't get, if Old *Mute put Emperor Taejo into power, why she'd want to take it away..."
    elif scrolled(35, korean=42):
        show mute upsetsob with fast
        show hyunae hmmsc with fast
        ms "...this isn't right..."
    elif scrolled(43, korean=51):
        show mute upsetscb with fast
        show hyunae hmmcob with fast
        $ ts("...but wouldn't Old *Mute be the eldest, by far...?", "...respecting elders is most important, but... this isn't...", True)
    elif scrolled(51, korean=59):
        show mute upset2 with fast
        show hyunae bittersc with fast
        ms "But like... she's just bringing her up to be manipulative, isn't she, though?"
    elif scrolled(68, korean=80):
        show hyunae hopelessscb with fast
        show mute upsetsc with fast
    elif scrolled(80, korean=92):
        show hyunae hmphscb with fast
        show mute tensescb with fast
    elif scrolled(88, korean=101):
        show hyunae flustered with fast
        show mute give up with fast
        if read("M6-9"):
            $ ts("I still can't believe...", "If only she hadn't...")
        else:
            $ ts("Whoa! Her? A rebellion...? *Mute?!", "Holy shit... she's serious!")
    elif scrolled(100, korean=111):
        show hyunae emo with fast
        show mute challengescb with fast
    elif scrolled(110, korean=123):
        show hyunae hopelesssob with fast
        show mute upset2 with fast
        $ ts("...she really idolized her, huh...", "That's not the important part!")
    elif scrolled(125, korean=137):
        show hyunae bittersc with fast
        show mute upsetsc with fast
    elif scrolled(141, korean=153):
        show hyunae hmmscb with fast
        show mute hatesc with fast
    elif scrolled(158, korean=166):
        show hyunae huhsc with fast
        show mute tensesc with fast
    elif scrolled(175, korean=189):
        show hyunae sighscb with fast
        show mute upsetsc with fast
    elif scrolled(182, korean=196):
        show mute give up with fast
        show hyunae hardscb with fast
        ms "This isn't right! This isn't right at all!"
    elif scrolled(1000):
        show hyunae enthusiastic blush with fast
        show mute damn with fast
        $ ts("She's really cool though, isn't she?", "UGH, NOT YOU TOO.")

    jump log_loop

label log_6_9_xharem:
    if get_m("M6-9").encrypted:
        show hyunae busy with fast
        show mute annoyed2 with fast
        ms "The brute force decryption still hasn't found the key yet, unfortunately... I'm just as anxious as you to read it, okay? We'll let you know when it's ready!"

    elif scrolled(4, korean=3):
        show hyunae grumpy with fast
        show mute wowsob with fast
        $ ts("Oh no...! So that's what this all was? A message...?", "...a message meant for me...")
    elif scrolled(13, korean=12):
        show mute challengesob with fast
        show hyunae hmmscb with fast
        ms "She's damn right she failed me!"
    elif scrolled(26, korean=24):
        show hyunae hmmsc with fast
        show mute upsetscb with fast
    elif scrolled(32, korean=29):
        show hyunae annoyedsob with fast
        show mute disbelief blush with fast
        $ ts("This is serious...", "I can't believe this... I did this...?")
    elif scrolled(38, korean=35):
        show mute worry2 with fast
        show hyunae annoyedsc with fast
        ms "I can't..."
    elif scrolled(44, korean=39):
        show hyunae hmph2 with fast
        show mute give up with fast
        $ ts("...that must've been scary for the maid, though...", "Could you please just reign in your fucking maid obsession for five minutes, please?!")
    elif scrolled(50, korean=45):
        show mute damn with fast
        show hyunae troubled2 with fast
        $ ts("...I'm sorry, I'll be quiet.", "Just... now is not the time, okay?!", True)
    elif scrolled(63, korean=59):
        show mute sighsob with fast
        show hyunae hmmscb with fast
        ms "...why would anyone threaten someone like Queen Eun-a..."
    elif scrolled(77, korean=74):
        show hyunae huhscb with fast
        show mute wowsob with fast
    elif scrolled(88, korean=86):
        show hyunae annoyedscb with fast
        show mute tensescb with fast
    elif scrolled(96, korean=95):
        show hyunae bittersob with fast
        show mute abashed blush with fast
        $ ts("Wow...", "...she wouldn't have said something like that... that's not her!")
    elif scrolled(108, korean=106):
        show hyunae bitterscb with fast
        show mute upsetsc with fast
    elif scrolled(114, korean=111):
        show hyunae staresob with fast
        show mute hatesob with fast
        $ ts("Whoa!", "What... what kind of woman would punch a man like that?")
    elif scrolled(119, korean=116):
        show hyunae oops with fast
        show mute wowsob with fast
    elif scrolled(133, korean=129):
        show hyunae hmmsob with fast
        show mute astonished blush with fast
        $ ts("...an explosion on the plaza?! Wow... that's... really serious...", "...an explosion on the plaza, under my watch...")
    elif scrolled(141, korean=138):
        show mute hatesob with fast
        show hyunae guilt with fast
        ms "This isn't right at all! Seo-yeong did that, not him!"
    elif scrolled(149, korean=146):
        show mute pressure with fast
        show hyunae sad with fast
        $ ts("Do you really believe so?", "She... she's lying, right? Old *Mute must be lying, right?", True)
    elif scrolled(158, korean=155):
        show mute bitter with fast
        show hyunae hopelessscb with fast
        ms "...I don't know what I believe."
    elif scrolled(167, korean=164):
        show mute cry with fast
        show hyunae hmmccb with fast
        ms "She... there's some reason that would have made her lie, right?"
    elif scrolled(175, korean=173):
        show mute damn with fast
        show hyunae oops with fast
        $ ts("...I can't think of one, but...", "*Hyun-ae, please, tell me I'm missing something, okay? There's a reason why Old *Mute would lie about this all, right?!", True)
    elif scrolled(188, korean=185):
        show mute shame with fast
        show hyunae baffled with fast
        ms "...of course you can't... why would she? She wouldn't..."
    elif scrolled(202, korean=198):
        show hyunae troubled with fast
        show mute worry with fast
    elif scrolled(215, korean=211):
        show hyunae sighsob with fast
        show mute pout with fast
        hs "That must have been so scary..."
    elif scrolled(228, korean=224):
        show hyunae losssob with fast
        show mute sob with fast
    elif scrolled(238, korean=235):
        show hyunae sigh blush with fast
        show mute sorryscb with fast
    elif scrolled(255, korean=251):
        show hyunae sighscb with fast
        show mute sighscb with fast
    elif scrolled(268, korean=265):
        show hyunae bitterscb with fast
        show mute upsetscb with fast
    elif scrolled(274, korean=272):
        show mute hatesob with fast
        show hyunae hopelessscb with fast
        ms "...Old *Mute... you coward! How could you?!"
    elif scrolled(296, korean=296):
        show hyunae hmmscb with fast
        show mute upsetsc with fast
    elif scrolled(302, korean=302):
        show mute insecure with fast
        show hyunae guilt with fast
        $ ts("Isn't... that what you'd call \"the rational thing\" to do?", "...no... you manipulative bitch, how could you say something like that...", True)
    elif scrolled(310, korean=310):
        show mute cry with fast
        show hyunae sad with fast
        ms "...maybe... but it's not fair to do that to a woman who believed in her so much..."
    elif scrolled(318, korean=319):
        show mute abashed blush with fast
        show hyunae troubled with fast
        ms "Is that why she employed a woman? Because she'd be easier to manipulate...?!"
    elif scrolled(326, korean=327):
        show mute pressure with fast
        show hyunae melancholic with fast
        ms "Ugh..."
    elif scrolled(332, korean=333):
        show hyunae pity with fast
        show mute mad with fast
        $ ts("Are you alright, *Mute?", "Does it {i}matter{/i}?!")
    elif scrolled(341, korean=342):
        show mute cry with fast
        show hyunae guilt with fast
        ms "...no..."
    elif scrolled(356, korean=359):
        show mute bitter with fast
        show hyunae losssob with fast
        $ ts("...it wasn't even...?!", "...they lied about it... they planned the lie all along...", True)
    elif scrolled(371, korean=375):
        show hyunae pressurescb with fast
        show mute tensescb with fast
    elif scrolled(390, korean=395):
        show hyunae emo with fast
        show mute challenge2 with fast
    elif scrolled(401, korean=406):
        show mute pressure with fast
        show hyunae melancholic with fast
        ms "I... I thought she... I trusted her... she said she was my friend..."
    elif scrolled(410, korean=415):
        show mute mad with fast
        show hyunae troubled with fast
        ms "...I know society was wrong, but... that can't be the way...!"
    elif scrolled(420, korean=425):
        show hyunae distressed with fast
        show mute insecure with fast
        $ ts("I didn't like her, but... reading about her broken like this is...", "She's an idiot! It's all her fault! Old *Mute, this is all because of you...")
    elif scrolled(430, korean=435):
        show hyunae sighsob with fast
        show mute shame with fast
        $ ts("...no...", "If you'd just listened to him... you wouldn't...")
    elif scrolled(441, korean=446):
        show hyunae losssob with fast
        show mute cry with fast
        $ ts("...no, no, no...", "...you'd still be alive...")
    elif scrolled(451, korean=455):
        show mute insecure with fast
        show hyunae sad with fast
        ms "You idiot! You stupid manipulative bitch!"
    elif scrolled(1000):
        show hyunae guilt with fast
        show mute bitter with fast
        $ ts("I had no idea... I'm so sorry, *Mute...", "Shut up! I don't want your pity!")

    jump log_loop