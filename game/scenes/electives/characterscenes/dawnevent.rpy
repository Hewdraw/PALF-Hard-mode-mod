label dawnevent:

if (not persondex["Dawn"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet her."
    
    show dawn uniform with dis

    red uniform happy "Hi th--"

    dawn surprised "Hi there! You're Dawn, what's my name?"
    dawn "..."

    red surprised "...Uh, come again?"

    dawn closedbrow sadmouth "I... I was thinking about what I was going to say to you for five minutes, and..."

    red happy "Ah, you got tongue-tied? That's alright!"
    red -happy "So, may I guess that your name's Dawn?"

    $ BecomeNamed("Dawn")
    dawn sadbrow "Yes..."

    red "Cool. I'm [first_name]. Where're you from?"

    dawn happy "Oh, I live in Snowpoint City! In Sinnoh!"
    dawn -happy "W-wait... no, I don't. I {i}lived{/i} there. I actually live here. Because I'm a student. Who goes to this school."
    dawn sad "{size=30}Help me.{/size}"

    red sadeyes sadeyebrows "Seems like you're a bit nervous."

    dawn closedbrow frownmouth "I'm... I'm not. I just... think about what I should say before I say it. But I think about it so hard that I say the wrong thing when it's time to actually say it."

    red happy "Shouldn't affect your skills as a trainer. Your Pokémon only need to understand a couple words when you're commanding them in battle, right?"

    dawn sad "...In battle? Yeah..."

    red -happy "You don't sound enthused. Not into battling?"

    dawn closedbrow frownmouth "Not really."

    red "Huh. I guess you're more of a Contest Coordinator, then?"

    dawn "My Mom would love that, but... no."

    red surprised "Uh, you want to study Pokemon? Like, as a Professor or Research Assistant!"

    dawn sad "{size=30}...No.{/size}"

    red "Uh... Musical coordinator? Ranger? Groomer? Breeder?"

    show dawn:
        ypos 1.0
        ease 0.5 ypos 1.2

    dawn closedbrow frownmouth "{size=30}Can you please stop?{/size}"

    red sadeyes sadeyebrows -surprisedmouth "Oh, geez, sorry. Hey, I didn't mean to harass you."

    dawn sadbrow happymouth "It's... not your fault. I'm just... a freak."

    red @angry "Woah, hey, what? I'm sure that's not true."
    red "..."
    red "Hey, why don't you tell me what you want to do with Pokémon, huh?"

    dawn "{size=30}...I don't.{/size}"

    red "Huh?"

    show dawn: 
        ypos 1.2
        ease 0.2 ypos 1.0

    dawn @angry "{size=50}I don't, okay!{/size} I don't want to do anything with Pokémon."

    red confusedeyebrows ".{w=0.5}.{w=0.5}.{w=0.5}I don't understand."

    dawn sadbrow frownmouth "No-one does. Even I don't. I get that I should love them. Everyone else does. And I don't, like, have a good reason to not be into them. But... I just want to..."

    pause 1.0

    dawn closedbrow frownmouth "I'm sorry for taking your time! And I'm sorry for oversharing! And I'm sorry for overapologizing! And I'm sorry for running away!"

    hide dawn with dis

    pause 2.0

    narrator "Dawn quickly skips away and takes a new seat at the far corner of the classroom."

    red "...That could've gone better."

    hide dawn

return