label end_demo:

narrator "{b}Wait!{/b} If you want your save to be compatible with the next version, then press \"Back\" at the bottom of the screen, and save before this dialogue box shows up."
narrator "I repeat, as of this textbox, {b}it is too late to save your game! You must reverse.{/b}"

pause 1.0

narrator "...Alright, let's continue."

$ renpy.pause(0.1, hard=True)

scene blank2

show red:
    xpos 700 alpha 0.0
    ease 0.5 alpha 1.0

stop music fadeout 1.0
play music "audio/music/SoaringDreams_Start.ogg" noloop
queue music "audio/music/SoaringDreams_Loop.ogg" 

$ renpy.pause(1.0, hard=True)

red @talkingmouth "The demo ends here, but there's a {i}lot{/i} more currently under development and on the way!"

pause 0.1

show blue behind red:
    alpha 0.0 xpos 450
    linear 0.5 alpha 1.0
    
$ renpy.pause(0.5, hard=True)

show leaf behind red:
    alpha 0.0 xpos 1050
    linear 0.5 alpha 1.0
    
show blue:
    xpos 450 alpha 1.0
    
blue @talkingmouth "Seriously?! We waited two goddamn months for {i}this?!{/i} We didn't even get to go to class {i}once!{/i}"
blue @angry "Did you forget this game is called Pokémon {i}Academy{/i} Life?!"

red @sadbrow happymouth "I'm just happy to be back again."

blue @angrymouth "Of course you are! Every time you show up, you get some new goddamn superpower! You're like Deku, but without having earned any of it!"

leaf @talkingmouth "Silence, weeb. We're supposed to be promoting the game, remember?"

blue @closedbrow talkingmouth "Whatever... {size=30}this is bullshit...{/size}"

leaf @talkingmouth "As the game goes on, the choices you make will have even more impact.{w=0.25}{nw}"
extend @flirt " We've barely scratched the surface!"

show leaf happy with dis

show gardenia:
    alpha 0.0 xpos 1250
    linear 0.75 alpha 1.0
show brendan behind red:
    alpha 0.0 xpos 1600
    pause 0.4
    linear 0.6 alpha 1.0
show dawn:
    alpha 0.0 xpos 1450
    pause 0.5
    linear 0.5 alpha 1.0 
show cheren behind leaf:
    alpha 0.0 xpos 200
    pause 0.25
    linear 0.4 alpha 1.0 
show serena behind gard1:
    alpha 0.0 xpos 875
    pause 0.6
    linear 0.7 alpha 1.0

red "Your choices will determine who you meet..."
    
show gardenia:
    xpos 1250 alpha 1.0
    ease 0.5 xpos 1280

gardenia @happy "And you can't just find everyone right away!"

dawn @sadbrow "Um... there's probably a bunch of people you haven't met in the electives... so, um, if you want to go back and do that?"

show gardenia:
    xpos 1280
    ease 0.5 xpos 1250

show dawn:
    xpos 1450
    pause 0.25
    ease 0.5 xpos 1420
    
cheren @sadmouth "Sometimes it comes down to your choices. And sometimes you just need to be patient."

brendan @thinking "Uhh...{w=0.5} I'm not really sure how to say this...{w=0.5}{nw}"
extend happy " But good luck!"

show dawn:
    xpos 1420
    ease 0.5 xpos 1450

show cheren:
    xpos 200
    pause 0.25
    ease 0.5 xpos 150

cheren @sadmouth "You can check on development updates via the {a=https://discord.gg/RRd2Srjp7n}official discord{/a} or the {a=https://www.pokecommunity.com/showthread.php?t=493106}PokéCommunity{/a} forum."

show cheren:
    xpos 150
    ease 0.5 xpos 200

show serena:
    xpos 875
    pause 0.25
    ease 0.5 xpos 905
    
serena @talkingmouth "Or if you prefer social media, follow the Pokémon Visual {a=https://twitter.com/pokemonvisual}Twitter{/a} account, or shoot a message to the {a=https://www.youtube.com/@PokemonVisual}YouTube Channel{/a}."

cheren @sadmouth "There are a few other platforms that might bear the project's name--a Facebook, or a website, for example..."

show serena surprised
show cheren surprised
with dis

blue @angry "But you won't get shit from those! We don't even own them anymore!" 

blue @closedbrow talkingmouth "Just jump on the discord, alright? {a=https://discord.gg/RRd2Srjp7n}Here's the link,{/a} again, in case you missed it the first time."

show cheren -surprised with dis
show serena -surprised with dis:
    xpos 905
    ease 0.5 xpos 875

show brendan:
    xpos 1600
    pause 0.25
    ease 0.5 xpos 1640

brendan @talkingmouth "Make sure you report any bugs or anything weird in general! You can reach out to the creator with the previous links."

brendan happy "Or you can send an email to 'pokemonvisualdev@gmail.com.'"

show brendan:
    xpos 1640
    ease 0.5 xpos 1600

red @talkingmouth "Suggestions are also more than welcome, by the way."
show red happy with dis

show serena happy
show blue happy
show dawn happy
show gardenia happy 
show cheren happy
with dis

leaf @happybrow talking2mouth "Thanks for playing!"

pause 0.25

window hide
stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_23

scene blank2 with transball
$ renpy.pause(1.0, hard=True)

$ renpy.music.stop(channel='crowd', fadeout=1.0)

$ renpy.movie_cutscene('videos/Credits.webm')

show screen credits with dissolve

pause 60

hide screen credits

stop music

$ MainMenu(confirm=False)()