label day010426:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_21

show morning at vspaz

pause 3.0

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

red @thinking "Mmph."

show brendan frownmouth with dis

brendan @talkingmouth "Hey, bro."

red @talkingmouth "Hey, Brendan. What's, uh, what's up?"

brendan @talkingmouth "I'm a bit concerned about Hilbert."

red @surprised "Huh?"

brendan @talkingmouth "He came back really late last night. And look, he's still asleep. He never sleeps 'til seven."

show calem uniform at leftside with dis

pause 0.5

calem @talkingmouth "Hilbert's hardly known for the consistency of his sleep schedule. I wouldn't spend an undue amount of time worrying about it."

pause 0.5

calem @surprised "Ah, my uniform? Yes, I dressed early again. Serena and I are trying to set up a last-minute event before the Student Council elections on Saturday."

red @thinking "Oh... right, those. Sorry. A lot's been happening. What can you tell me about those?"

calem @thinking "Well, Saturday afternoon, the former Student Council is going to host a round-table with everyone who wants to become part of the new Student Council."

red @talking2mouth "Uh-huh."

calem @talkingmouth "We'll give speeches, re-iterate what our positions are, and then the Student body will vote on who they want to admit into the council."

brendan @surprised "Wait, on Saturday, though? But what if someone is out-of-town for the weekend?"

calem @thinking "Yes, that's a possibility. The Student Council asks that people remain at the Academy for the voting process, but the fact of the matter is that not a lot of Kobukan bothers to vote on their Student Council."
calem @sad "We can't {i}force{/i} people to vote. Such is the weakness of democracy. The worst kind of government, except all others."

red @thinking "Mm... that's lame. How do we get people to get out and vote, then?"

calem @thinking "I suppose if we Student Council hopefuls were to campaign for the vote itself, as opposed to just ourselves, we might raise a bit of awareness." 
calem @talkingmouth "If we {i}told{/i} the Student Body what voting for us would get them, in concrete, brief, terms, we might get more turnout."

red @thinking "Well... let's do that, then. I mean, regardless of whether we win or not, {i}whoever{/i} wins will be making a bunch of decisions for people, right? People should have a say in those decisions."

calem @sad "Easier said than done. We only have six days. We can't just slap our campaign on a poster this time."

pause 1.0

show calem surprisedbrow with dis

red @confused "Why not?"

pause 1.0

calem -surprisedbrow @talkingmouth "Well... actually, come to think of it... that {i}might{/i} work. And if we all have similar posters, posters that are well-designed, this time, then we could present a unified front, and..."

pause 0.5

calem @happy "Why, [first_name], I've been unsure until now if you had actually expended {i}any{/i} effort in your campaign, but this is quite a good idea."
calem @thinking "We should gather all the people attempting to run for Student Council. I've some business this afternoon, but would you be free tonight, just before curfew?"

show ethan uniform at rightside with dis

ethan @thinking "Sorry, Calloway. We've got a Battle Team meeting tonight. Normally they'll be Friday nights, but I guess Janine wanted to talk to us sooner."

calem @surprised "{size=25}Oh? You're up early. {/size}{w=0.5}{nw}"
extend @talkingmouth "In any case, perhaps tonight would have been too soon. Tomorrow morning, then, in the cafeteria? That should give us enough time to make contact with everyone."

red @talkingmouth "Sure thing. I guess you can tell Serena about this pretty easily. Can you also tell Cheren? Things between Cheren and I have been a bit weird recently."

calem @talkingmouth "Certainly. May I ask you to do something in return, then?"

red @thinking "Man, I'm {i}pretty{/i} busy... but sure, what?"

calem @talkingmouth "Before the day is out, could you tell the former Student Council about this meeting? I'd like them to be present there, so we can negotiate for their endorsements."

red @talkingmouth "Oh, sure."

pause 0.5

calem @sad "And, er... one more thing. Would you mind making contact with Jasmine?"

red @thinking "Who?"

calem @talkingmouth "She's... running for Student Council. But it's... {i}difficult{/i} to talk to her."

red @confused "Huh, really? You don't seem to have problems talking with anyone. I mean, even Serena, you spend most of your day with, regardless of the awkwardness."

calem @sad "Yes, well, that's... that's the case. If you wouldn't mind."

red @talkingmouth "Yeah, no problem. Do you have, like, a description? Whitney can probably track her down, but maybe I'll run into her first."

calem @sad "She's... tall.{w=0.5} Quite tall.{w=0.5} Um... very thin.{w=0.5} Narrow-waisted.{w=0.5} Has thin brown hair.{w=0.5} Wears it up in two bunches."

brendan @thinking "...You're not gonna mention the cane?"

calem @surprised "What? Brendan, you know Jasmine?"

brendan @talkingmouth "Yeah, she's showed up in Professor Birch's homeroom a couple times."

$ KnowClasses("Jasmine", ["Steel"])

ethan @talkingmouth "Yeah, I know who you're talking about, too. Nacho said she shows up in Steel class every once in a while."

calem @angrybrow talking2mouth "Well, I would have {i}appreciated{/i} you helping me in my descriptors!"

brendan @surprised "Dude! I {i}said{/i} she used a cane! I just thought you were going to get around to the obvious part first."

calem @thinking "Jasmine is a strong-willed young woman who doubtlessly has many other qualities {i}besides{/i} her usage of a movement aid."
calem @talking2mouth "To immediately jump to describing her as a 'cane-user' would be diminutive and disrespectful."

pause 1.0

red @confused "But she {i}does{/i} use a--"

calem @closedbrow talking2mouth "Yes, she does."

red @happy "Alright! I'll be on the lookout, then."

brendan @talkingmouth "Yeah, she doesn't always show up to classes, but if she doesn't, she's probably at the infirmary."

red @surprised "Oh, geez. That bad?"

brendan @thinking "I dunno. Some kinda fatigue thing, I think."

red @thinking "And... she's running for Student Council while dealing with {i}all{/i} that?"

calem @talkingmouth "Oh, you'll understand as soon as you meet her."

red @happy "Looking forward to it. Think we've gotta go to homeroom now, though?"

calem @thinking "Yes, we probably should."

pause 1.0

show ethan surprised
show brendan surprised
with dis

calem @sad "Is anyone else going to volunteer to wake Hilbert up?"

pause 1.0

red ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 1.0

show ethan:
    xpos 0.75
    ease 0.2 xpos 1.2
show brendan:
    xpos 0.5
    ease 0.2 xpos 1.2

pause 0.2

show calem surprised with dis

$ PlaySound("Door_Slam.mp3")

pause 1.0

calem -surprised @sad "Oh, even [first_name]?"

pause 1.0

calem @sad "A diplomat's work is ever one of sacrifice..."

pause 1.0

show calem angrybrow with dis

show brendan sad:
    xpos 1.2
    ease 0.8 xpos 0.75

pause 1.0

brendan "I, uh... forgot to grab my uniform... I should probably grab [first_name]'s as well..."

scene blank2 with splitfade
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

$ renpy.pause(2.5, hard=True)

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show oakbg at dissolvein behind blank2
show homeroom behind oakbg

hide blank2 with splitfade

$ renpy.pause(0.6, hard=True)

oak "Good morning, ladies and gentlemen! As you may recall, we have a quiz later today--"

$ PlaySound("class_groan.ogg")

oak "--{i}But{/i}, first, we're all going to take a trip to the research lab! The baby Pokémon from Springsday are hatching!"

oak "Those of you who gathered up eggs on Saturday should be able to claim your Pokémon. And those of you who {i}didn't{/i} get any eggs... well..."

pause 0.5

oak "It'll be a learning experience."

leaf uniform @sarcastic "Why do I feel like he's being smug about that?"

pause 0.5

scene research with splitfade

pause 0.3

show oak with dis

pause 0.5

oak @closedbrow talking2mouth "Now, let's see... where are the eggs... I could've sworn that..."

while (HasEgg()):
    oak @happy "Ah! I believe this one hatched from one of your eggs."

    if HasEgg("Larvesta Egg"):
        $ del inventory["Larvesta Egg"]

        $ sidemonnum = 636
        $ PlaySound("pokemon/cries/636.wav")
        $ eggshatched.append("Larvesta")

        sidemon "Larv... Larvesta!"

        oak @talkingmouth "A newborn Larvesta! Its fuzzy mane is especially good at absorbing heat. As it gets closer to evolution, that heat will begin to sear, before it evolves into Volcarona!"

        show may angrybrow frownmouth uniform at leftside with dis

        pause 1.0

        red "Yeah, I think I can feel some of that heat already..."

        hide may with dis

        $ AddMon(Pokemon(pokedexlookupname("Larvesta", DexMacros.Id), level=1), True)

    elif HasEgg("Togepi Egg"):
        $ del inventory["Togepi Egg"]

        $ sidemonnum = 175
        $ PlaySound("pokemon/cries/175.wav")
        $ eggshatched.append("Togepi")

        sidemon "Togepipipipi!"

        oak @talkingmouth "A juvenile Togepi! Due to their weak defenses, the babies are well-known for using their egg as rudimentary armor."

        $ AddMon(Pokemon(pokedexlookupname("Togepi", DexMacros.Id), level=1), True)

    elif HasEgg("Tyrogue Egg"):
        $ del inventory["Tyrogue Egg"]

        $ sidemonnum = 236
        $ PlaySound("pokemon/cries/236.wav")
        $ eggshatched.append("Tyrogue")

        sidemon "Tyr. Rogue!"

        oak @talkingmouth "A young Tyrogue! They'll train relentlessly in three different styles until they evolve! It takes them a while to decide how they want to specialize."

        $ AddMon(Pokemon(pokedexlookupname("Tyrogue", DexMacros.Id), level=1), True)

    elif HasEgg("Smoochum Egg"):
        $ del inventory["Smoochum Egg"]

        $ sidemonnum = 238
        $ PlaySound("pokemon/cries/238.wav")
        $ eggshatched.append("Smoochum")

        sidemon "Smoo. Smoochum."

        oak @talkingmouth "A baby Smoochum! Their sense of touch is rather well-developed, so they tend to feel around most things with their thick, plush, lips." 
        oak @surprised "But their kisses can be dangerous! They can put you to sleep, confuse you, or even inflict you with mild frostbite."

        $ AddMon(Pokemon(pokedexlookupname("Smoochum", DexMacros.Id), level=1), True)

    elif HasEgg("Magby Egg"):
        $ del inventory["Magby Egg"]

        $ sidemonnum = 240
        $ PlaySound("pokemon/cries/240.wav")
        $ eggshatched.append("Magby")

        sidemon "Magmagmagmagby!"

        oak @talkingmouth "A juvenile Magby! Their ducklike anatomy is quite unusual amongst Fire-types. Certain scientists theorize that Turtonator are descendants of the same ancient species that birthed Magby, and its evolutions."

        $ AddMon(Pokemon(pokedexlookupname("Magby", DexMacros.Id), level=1), True)

    elif HasEgg("Wynaut Egg"):
        $ del inventory["Wynaut Egg"]

        $ sidemonnum = 360
        $ PlaySound("pokemon/cries/360.wav")
        $ eggshatched.append("Wynaut")

        sidemon "Wynaut?"

        oak @talkingmouth "A young Wynaut! These truly bizarre Pokémon are the subject of constant study. It's widely theorized that the 'true' Wynaut is the black 'tail' on its back, but we've yet been able to confirm that."

        $ AddMon(Pokemon(pokedexlookupname("Wynaut", DexMacros.Id), level=1), True)

    elif HasEgg("Bonsly Egg"):
        $ del inventory["Bonsly Egg"]

        $ sidemonnum = 438
        $ PlaySound("pokemon/cries/438.wav")
        $ eggshatched.append("Bonsly")

        sidemon "Bon... Bonsly..."

        oak @talkingmouth "A young Bonsly! These bonsai-like Pokémon are {i}not{/i} Grass-types, despite how their appearance may mislead." 
        oak @angrybrow talking2mouth "Be very wary of a Bonsly that appears to be crying. 'Crying' is their standard reaction to almost every form of stimuli."

        $ AddMon(Pokemon(pokedexlookupname("Bonsly", DexMacros.Id), level=1), True)

    elif HasEgg("Mantyke Egg"):
        $ del inventory["Mantyke Egg"]

        $ sidemonnum = 458
        $ PlaySound("pokemon/cries/458.wav")
        $ eggshatched.append("Mantyke")

        sidemon "Mantyke!~"

        oak @talkingmouth "A juvenile Mantyke! These small creatures tend to form schools with Remoraid in the wild. After a pair have learned to work together, and bonded, the Mantyke will evolve into Mantine!"

        red @confused "What happens when the Remoraid evolves, though?"

        oak @thinking "Well, Remoraid in the company of Mantine rarely do. But in exceedingly rare cases, the bond between a Mantine and Remoraid is so strong that not even evolution can change it."

        oak @talkingmouth "It's slightly more common in Kobukan, but still quite rare... but you can, occasionally, see a Mantine with an entire Octillery suctioned to its underside, acting as a portable, airborne, bombardment cannon."

        red @happy "That'd be cool. Maybe I can get one of those some day."

        $ AddMon(Pokemon(pokedexlookupname("Mantyke", DexMacros.Id), level=1), True)

    elif HasEgg("Toxel Egg"):
        $ del inventory["Toxel Egg"]

        $ sidemonnum = 848
        $ PlaySound("pokemon/cries/848.wav")
        $ eggshatched.append("Toxel")

        sidemon "Tox. Tox{i}el.{/i}"

        oak @talkingmouth "A baby Toxel! These creatures are quite moody and temperamental as youths." 
        oak @thinking "When they get older, and get closer to evolution, they'll either lose their apathy and become hotheaded and outgoing, or lose their temperamentality, and become far more mellow."

        red @thinking "Right. And whichever one they become decides what they evolve into, right?"

        oak @happy "Quite right!"

        $ AddMon(Pokemon(pokedexlookupname("Toxel", DexMacros.Id), level=1), True)

    elif HasEgg("Deino Egg"):
        $ del inventory["Deino Egg"]

        $ sidemonnum = 633
        $ PlaySound("pokemon/cries/633.wav")
        $ eggshatched.append("Deino")

        sidemon "Rawr! Deino!"

        oak @talkingmouth "A juvenile Deino! These Pokémon are aggressive, blind, and hungry. Raising one to adulthood will be quite a challenge."

        pause 0.5

        oak @thinking "Actually, come to think of it... I didn't know we were giving out Deino eggs, never mind two..."

        $ AddMon(Pokemon(pokedexlookupname("Deino", DexMacros.Id), level=1), True)

    oak @thinking "Now, let's see..."

$ happinyobj = Pokemon(pokedexlookupname("Happiny", DexMacros.Id), level=1)
$ whitneyhappinyobj = happinyobj

if (happinyegg != None):
    oak @surprised "Oh! I almost forgot about this little miss."

    $ sidemonnum = pokedexlookupname("Happiny", DexMacros.Id)

    $ PlaySound("pokemon/cries/440.wav")
    $ eggshatched.append("Happiny")

    sidemon "Happ, Happ~iny!"

    oak @happy "It seems quite fond of you. And it looks like it's brought a little gift!"

    $ GetItem("Lucky Egg")
    $ AddMon(happinyobj, True)

    oak @thinking "That egg is a 'Lucky Egg,' lad. They're quite rare, and very valuable for trainers. They're infused with a Pokémon's well-wishes, and actually {i}double{/i} the amount of experience a Pokémon gets from battle."

    red @confused "...Um. I gave it an actual egg, though. Something that was going to hatch. What happened to that?"

    oak @surprised "Eh?"

    oak @closedbrow talking2mouth "Well... I imagine, at some point, the incubator's staff quickly replaced this Happiny's egg with this Lucky Egg. The original Pokémon has most likely been released into the fields now."

    red @thinking "Oh, well. A Lucky Egg is a pretty cool trade, I guess."

    hide oak with dis

    show whitney uniform surprised with dis

    whitney "Wait. Shut the front door. Is that a {i}Happiny?!{/i}"

    red @talkingmouth "Uh, yep. She sure is."

    whitney @talkingmouth "I {i}need{/i} her. Please, please, please, can I have her?! I will {i}die{/i} if I can't have her!"

    red @confused "Well, I don't want to commit murder..."

    menu:
        "I'm planning on using her.":
            whitney -surprised @sad "Aw...{w=0.5} wait, wait, wait!"
            whitney angrybrow @happymouth "Okay, how about this. I can sweeten the pot."
            whitney -angrybrow @talkingmouth "I have a Munchlax. I'll trade you my Munchlax for your Happiny, alright?"
            red @thinking "Hm..."

            menu:
                "Still no, sorry.":
                    whitney angry "Ah, boo!"
                    hide whitney with dis
                    $ whitneyhashappiny = False

                "Oh, alright, then.":
                    $ whitneyhashappiny = True
                    whitney surprised "Really? I totally thought I was going to have to beg for that one!"

                    $ ValueChange("Whitney", 3, 0.5)

                    whitney happy "Thanks so much, [first_name]!"

                    if (happinyobj in playerparty):
                        $ playerparty.remove(happinyobj)
                    else:
                        red @talkingmouth "No problem. I'll submit a request to have it transferred from my PC to yours, next chance I get."
                        $ box.remove(happinyobj)

                    whitney -happy @talkingmouth "Here's my Munchlax! I didn't actually have a chance to nickname him yet, so I'll leave that up to you."

                    whitney thinking "{size=30}I was thinking 'Creosote', maybe...?{/size}"

                    hide whitney with dis

                    $ AddMon(Pokemon(pokedexlookupname("Munchlax", DexMacros.Id), level=1, gender=Genders.Male), True)

        "You can have her.":
            $ whitneyhashappiny = True
            show whitney surprised with dis

            whitney "Really? I totally thought I was going to have to beg for that one!"

            if (happinyobj in playerparty):
                $ playerparty.remove(happinyobj)
            else:
                red @talkingmouth "No problem. I'll submit a request to have it transferred from my PC to yours, next chance I get."
                $ box.remove(happinyobj)

            $ ValueChange("Whitney", 5, 0.5)

            whitney happy "Thanks so much, [first_name]!"

    hide whitney with dis

    pause 0.5

    show oak with dis

else:
    $ whitneyhashappiny = False

if (whitneyhashappiny):
    if (happinyobj.GetNickname() == "Happiny"):
        $ happinyobj.Nickname = "Joy"

oak @thinking "Hm... it seems it's about time for your elective classes, then. Hurry on, now!"

jump homeroom1transition