label sleepingtable:

$ randnum = Random()

hide ethan
show ethan uniform with dis

ethan closedbrow @frownmouth "...Mmrmph. Zzz... "

if (randnum < 0.2):
    ethan @talkingmouth "No, don't... What a ghastly wail..."

    red uniform @thinking "Looks like he's having a nightmare..."

elif (randnum < 0.4):
    ethan @talkingmouth "This boss is bullshit..."

    red uniform @thinking "He's having trouble with his boss? Maybe he has a part-time job."

elif (randnum < 0.6):
    ethan @talkingmouth "Megidolaon... Can't be resisted..."

    red uniform @thinking "Megidolaon? What's that? Can't be a Pokémon, I'd know it. A move, maybe...?"

elif (randnum < 0.8):
    ethan @talkingmouth "Blocking... Tartarus..."

    red uniform @thinking "Tartarus? What's that? Sounds like toothpaste."

else:
    ethan @talkingmouth "Death... is not a hunter unbenownst to its prey..."

    red uniform @thinking "Huh... for some reason, I feel like I've heard that a lot."

narrator "You watch over Ethan's slumbering form as lunch draws to a close."

ethan "...zzzZ? Snrk."
ethan surprised "Huh? [first_name]?"
ethan happy "Oh, did I fall asleep again? Thanks for watching out for me, buddy!"
red happy "Anytime."

$ ValueChange("Ethan", 1, 0.5)

return