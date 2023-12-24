init python:
    def TiaHasUnseenScene():
        if (GetCharValue("Tia") >= 10 and GetRelationship("Tia") != "{font=fonts/sign.ttf}Trainer{/font}"):
            return "Tia1"
        return False

label Tia1:#FIX THIS: DO MASSIVE REWRITE OF THIS SCENE FOR WEEK 5

if (not IsBefore(1, 5, 2004)):
    $ persondex["Tia"]["Events"].append("Level2SceneVer2")

$ renpy.music.queue("Audio/Music/TiaTheme.mp3", channel='music', loop=True, tight=None)

scene garden:
    zoom 0.625
show clouds behind garden

if (IsBefore(17, 4, 2004)):
    show tia closedbrow with Dissolve(2.0):
        xpos 0.5 ypos 1.0 xzoom 1.0
        parallel:
            ease 4.0 xpos 0.25
            ease 4.0 xpos 0.5
            ease 4.0 xpos 0.75
            ease 4.0 xpos 0.5
            repeat
        parallel:
            ease 2.0 ypos 1.05
            ease 2.0 ypos 1.0
            ease 2.0 ypos 0.95
            ease 2.0 ypos 1.0
            repeat
        parallel:
            pause 3.7 
            ease 0.3 xzoom -1
            pause 3.7
            ease 0.3 xzoom 1
            repeat
else:
    show tia hat closedbrow with Dissolve(2.0):
        xpos 0.5 ypos 1.0 xzoom 1.0
        parallel:
            ease 4.0 xpos 0.25
            ease 4.0 xpos 0.5
            ease 4.0 xpos 0.75
            ease 4.0 xpos 0.5
            repeat
        parallel:
            ease 2.0 ypos 1.05
            ease 2.0 ypos 1.0
            ease 2.0 ypos 0.95
            ease 2.0 ypos 1.0
            repeat
        parallel:
            pause 3.7 
            ease 0.3 xzoom -1
            pause 3.7
            ease 0.3 xzoom 1
            repeat

narrator "You walk into the garden and are greeted by the amusing sight of what looks like Tia performing a solo waltz."

pause 2.0

narrator "She bounces her head along to some music that only she can hear."

pause 2.0

narrator "You take a deep breath and flex your hands out before revealing what you've been practicing."

red @happy "<Hello, Tia.>"

pause 1.0

redmind @thinking "Wait. Eyes closed. She can't see me. I'm an idiot."

show tia surprised with dis 

red @talkingmouth "Hey, Tia."

show tia happy with dis

pause 1.0

show tia surprised with dis

red "<You dance?>"

pause 1.0

show tia happy:
    ease 0.5 xpos 0.5 ypos 1.0 xzoom 1
    parallel:
        ease 0.3 ypos 1.0
        ease 0.3 ypos 1.1
        repeat

tia "You learned JSL? That's {font=fonts/sign.ttf}great{/font}! I'm so {font=fonts/sign.ttf}happy{/font}! Now we can {font=fonts/sign.ttf}talk{/font} and {font=fonts/sign.ttf}play{/font} and I {font=fonts/sign.ttf}don't{/font} {font=fonts/sign.ttf}need{/font} {font=fonts/sign.ttf}Whitney{/font}!"

red @surprisedbrow frownmouth "<Slow down, very slow. I cannot speak that fast.>"

pause 1.0

red @thinking "<I meant I cannot {i}read{/i} that fast.>"

show tia happy:
    ease 0.5 xpos 0.5 ypos 1.0 xzoom 1

tia -happy @surprised "Oh. Well, I'm still {font=fonts/sign.ttf}happy{/font}!"
tia @sadbrow happymouth "But it's okay if you want to just speak."
tia @happy "I really {font=fonts/sign.ttf}appreciate{/font} you making the effort, {font=fonts/sign.ttf}[first_name]{/font}!"

red @happy "I might just take you up on that. I'll try to sign and speak at the same time, though. Whitney makes it look easy!"

pause 1.0

red @talkingmouth "Anyway, those were some sick dance moves. Or... I guess 'sick' isn't the right word. Elegant?"
red @happy "Where'd you learn to dance, spacewoman? The moon?"

tia @happy "In A-L-T-O M-A-R-E! My sister and I used to dance {font=fonts/sign.ttf}all{/font} {font=fonts/sign.ttf}the{/font} time."

red @talking2mouth "Right... and your Sister is 'Bianca,' right?"

tia @frownmouth "That's right. I miss her..."

red @talkingmouth "...She must love you a lot, to let you get into this school under her name."

tia @happy "She does! She was my first {font=fonts/sign.ttf}human{/font} friend. Before I {font=fonts/sign.ttf}met{/font} {font=fonts/sign.ttf}her{/font} it was just my brother and I hiding in the city."

red @talkingmouth "Oh, so your brother and you came before your Sister? So I guess Bianca is a younger sister, then."

red @confused "Wait... {i}hiding{/i} in the city? Were you homeless?"

tia @surprised "No! Alto Mare was my home."

red @thinking "Uh... but where did you sleep at night? Before your Sister, I mean."

tia @happy "Under a bridge!"

pause 1.0

red @confused "Tia, that's called being homeless."

tia @angrybrow poutmouth "{font=fonts/sign.ttf}Nuh-uh{/font}! Alto Mare was my home."

pause 1.0

red @closedbrow talking2mouth "Well, I'm glad you got out of that situation, anyway."
red @confused "I've got a question, though. If she was willing to let you take her place at Kobukan, why didn't she want to go herself?"

tia @happy "Oh, she's busy helping {font=fonts/sign.ttf}grampy{/font} run Alto Mare. My grandpa is the city's {font=fonts/sign.ttf}mayor{/font}!"
tia @talkingmouth "And someone needs to run the {font=fonts/sign.ttf}Defense{/font} {font=fonts/sign.ttf}Mechanism{/font} of Alto Mare, of course."

red @confused "The... what?"

tia @happy "The {font=fonts/sign.ttf}Defense{/font} {font=fonts/sign.ttf}Mechanism{/font} of Alto Mare!"

red @sadbrow happymouth "Gimme a hint here. The food court of Alto Mare? The tourism bureau of Alto Mare? The sewer system of Alto Mare?"

tia @thinking "Hm."
tia @talkingmouth "D-M-A."

red @thinking "DMA? Uh... the dirty manhole of Alto Mare? The dogmatic militia of Alto Mare?"

tia @thinking "The second one is {i}kinda{/i} right."

tia @happy "The DMA keeps the bad people away from us!"

red @surprised "Oh, bad people... like the one you said you were hiding from."

tia @happy "Yes, {font=fonts/sign.ttf}exactly{/font}! Grandpa said he knew the bad person would appear in Kobukan {i}months{/i} ago, so that's why I'm here."

show tia:
    ease 0.2 ypos 1.2 zoom 1.3

tia @angrybrow happymouth "I'm here to protect you!"

show tia:
    ease 0.2 ypos 1.0 zoom 1.0

red @happy "Aw. I thought I was protecting {i}you{/i}, though?"

tia @lightblush talkingmouth "I... might need that for a little bit longer."
tia @angrybrow happymouth "The {font=fonts/sign.ttf}bad{/font} {font=fonts/sign.ttf}person{/font} is much stronger than grandpa thought. I could only barely {font=fonts/sign.ttf}fight{/font} {font=fonts/sign.ttf}them{/font}, and I got really tired after..."
tia @talkingmouth "Normally my brother {font=fonts/sign.ttf}handles{/font} stuff like that, though."

red @thinking "Your grandpa and your sister engaged in a conspiracy to get your sister into this school so that you could take her place and be here to protect the population of Kobukan from... a bad person?"

tia @happy "Yep! I'm going to be a hero!"

pause 1.0

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

show tia surprised with dis

red @closedbrow "I don't think you're lying, but it's kinda hard to believe what you're saying."

tia sadbrow frownmouth "It is...?"

red @sad "Aw, don't feel bad, Tia. I {i}did{/i} say I don't think you're lying. It's just... if there was any actual threat, why would they send a tiny eighteen-year-old girl to face it?"

show tia angrybrow poutmouth with dis

red @happy "I mean... I'm pretty sheltered, growing up in Pallet Town, but I, at least, know how to use a phone."

tia "Mrgrgr!"

"{color=#000}TL Note{/color}" "There is no sign for 'Mrgrgr.' And yet, that is the only possible translation for Tia's hands in this moment."

tia "You don't need to know how to use a dumb ol' {font=fonts/sign.ttf}phone{/font} to protect people!"

show tia happy with dis

red @thinking "Hm... Alright. I don't get it, but I choose to believe you."

tia "Yay! Thank you, [first_name]!"

red @happy "So. What do you need to do to get better at protecting people?"

tia @surprised "Huh?"

red @talkingmouth "Y'know. If you're really here to defend us against a bad person, then you probably need to train, right? What's your battle strategy?"

tia @talkingmouth "Oh, I like to help my brother! I give him a helping hand in his battles, and, if he's tired or hurt, I use heal pulse!"

red @thinking "Hm. That's... that's kinda..."

pause 1.0

show tia sadbrow frownmouth with dissolve

tia "...I know. My brother isn't {font=fonts/sign.ttf}here{/font}..."

red @thinking "Also, I was kinda asking more about your solo battle strategy. Like, what you do when it's just one trainer against another."

tia -sadbrow -frownmouth @talkingmouth "Well, I just ask my friends to do their best! And they always do!"

red @thinking "Hm... why don't you send one of your friends out? Maybe I can take a look at them."

python:
    if ('tiamimejrobj' not in globals()):
        playerlevel = max(8, GetHighestLevel() - 3)
        tiamimejrobj = Pokemon(pokedexlookupname("Mime Jr.", DexMacros.Id), moves=[GetMove("Barrier"), GetMove("Tickle"), GetMove("Copycat"), GetMove("Confusion")], level=playerlevel - 1, gender=Genders.Male, ability="Filter")

    mimeid = tiamimejrobj.GetId()
    sidemonnum = mimeid

play sound "audio/Pokemon/Ball sound.ogg"
queue sound "audio/Pokemon/Cries/{}.wav".format(mimeid)

show sideportraitfull at dormdesk, pokeball
show tia:
    ease 0.5 xpos 0.75

$ hideside = True

sidemon "Mime!~"

pause 1.0

$ hideside = False

red @happy "Hi, there, buddy. You're looking good."

$ hideside = True

sidemon "Mi-mi-mime!~"

pause 1.0

$ hideside = False

show sideportraitfull:
    xpos 0.5 ypos 0.78 xzoom 1.0
    parallel:
        ease 4.0 xpos 0.25
        ease 4.0 xpos 0.5
        ease 4.0 xpos 0.75
        ease 4.0 xpos 0.5
        repeat
    parallel:
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.05
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.05
        repeat
    parallel:
        pause 3.7 
        ease 0.3 xzoom -1
        pause 3.7
        ease 0.3 xzoom 1
        repeat

red @happy "Aw, the little guy's cute. He..."

pause 2.0

red @surprised "Wait! He's doing the same dance you did!"

tia @happybrow lightblush "Yes! I taught him this dance!"

red @surprised "Woah. You taught your Pokémon how to dance?"

tia @happy "Yeh! It's a good way to learn how to dodge!"

show tia closedbrow:
    xpos 0.75 ypos 1.0 xzoom 1.0
    parallel:
        ease 4.0 xpos 0.25
        ease 4.0 xpos 0.5
        ease 4.0 xpos 0.75
        ease 4.0 xpos 0.5
        repeat
    parallel:
        ease 2.0 ypos 1.05
        ease 2.0 ypos 1.0
        ease 2.0 ypos 0.95
        ease 2.0 ypos 1.0
        repeat
    parallel:
        pause 3.7 
        ease 0.3 xzoom -1
        pause 3.7
        ease 0.3 xzoom 1
        repeat

pause 2.0 

redmind @thinking "Huh... Pokémon have an instinct to battle. Not so much to dance. Training a Pokémon to dance would take some serious skill, or at least some serious ability to communicate with your Pokémon. I wonder what's going on here...?"

pause 2.0

show tia -closedbrow with dis:
    ease 0.5 xpos 0.5 xzoom 1.0 ypos 1.0

red @talkingmouth "I'm impressed. You're a better trainer than I've given you credit for."

tia @sadbrow happymouth "Aw, thanks. But I think I need a {font=fonts/sign.ttf}trainer{/font} myself..."

red @confused "A what?"

tia @closedbrow frownmouth "Hm... you know, a {i}you!{/i}"

red @thinking "Me? A... student? A Champion?"

tia @angrybrow poutmouth "No, no! The person who throws the {font=fonts/sign.ttf}poke{/font} Balls!"

red @happy "Oh, a trainer!"

tia @happy "Yeah! There's a lot I don't know about {font=fonts/sign.ttf}humans{/font}. I want to learn how to be a better {font=fonts/sign.ttf}human{/font}."

red @talkingmouth "Well, I might be able to help you with that. I mean, I don't know much about being a trainer myself, yet, but I guess I know a little bit more than you."

tia angrybrow happymouth "Yay! Thank you, {color=#0048ff}{font=fonts/sign.ttf}Trainer{/font}!{/color}"

$ ValueChange("Tia", 5, 0.5)

$ persondex["Tia"]["Relationship"] = "{font=fonts/sign.ttf}Trainer{/font}"
$ persondex["Tia"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Tia evolve from '{color=#0048ff}Protector{/color}' to '{color=#0048ff}{font=fonts/sign.ttf}Trainer{/font}{/color}'!"

return