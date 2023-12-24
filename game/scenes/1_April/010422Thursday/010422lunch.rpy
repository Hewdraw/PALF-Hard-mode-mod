label lunch010422:

if (starterobj in playerparty):
    red uniform @talking2mouth "Hey, you know how much you matter to me, right, [starter_name]?"

    play sound "audio/pokemon/cries/{}.wav".format(starter_id)

    starter "[starter_species_name]!"

    red @happy "Cool. Just checking."
    red @talkingmouth "Now, let's go get some grub! I'll see if I can sneak you some under the table."

    if (readheight(starter_id) > 48):
        red @thinking "Although... you're kinda massive. I'm not sure you'll fit under the table, come to think of it."

else:
    redmind uniform @thinking "Hearing Alder chew Misty out for not paying enough attention to her Psyduck reminds me... I should get [starter_name] from the PC."
    redmind @thinking "They're one of the evaluation criteria at the end of the year, and it wouldn't be good if I left them in the PC for a long time and forgot to train them."
    redmind @happy "Maybe after school. For now, I'll get some grub!"

jump PickTable