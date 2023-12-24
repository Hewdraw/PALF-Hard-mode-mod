init python:
    def FormatText(text):
        return text.replace("!", "! ").replace(".", ". ").replace("  ", " ").replace(". . .", "...")

    def LastResortWorks(actionlog, user):
        movesused = []
        nummovesneeded = max(len(user.GetMoves()) - 1, 1)
        for action in reversed(actionlog):
            if (action.GetActionType() == ActionTypes.Move 
                and not action.GetMove().Name in movesused 
                and action.GetUser() == user 
                and action.GetMove().Name != "Last Resort"):
                movesused.append(action.GetMove().Name)
            elif (action.GetActionType() == ActionTypes.Pokemon and action.GetTargets() == user):#if this 'mon ever switched in at some point, stop counting before here
                return nummovesneeded <= len(movesused)
        return nummovesneeded <= len(movesused)

    def PaybackDoubles(user, target):
        for action in reversed(ActionLog):
            if (action.GetUser() == target and action.GetActionType() in [ActionTypes.Move, ActionTypes.Bag] and action.GetTurn() == Turn):
                return True
        return False

    def RoundDoubles(user):
        for action in reversed(ActionLog):
            if (action.GetActionType() == ActionTypes.Move and action.GetTurn() == Turn and action.GetMove().Name == "Round" and action.GetUser() != user):
                return True
        return False

    def GetLastMove(actionlog, user=None, target=None, ignorepp=False, ignoremoves=[], returnnonemoves=[], ignorefailures=True, lookformoves=[], returnaction=False):
        for action in reversed(actionlog):
            if (action.GetActionType() == ActionTypes.Move 
                and (user == None or (action.GetUser() == user and action.GetTurn() >= user.GetTurnSwitchedIn()))
                and (target == None or target in action.GetTargets())
                and action.GetMove().Name not in ignoremoves
                and action.GetMove().Name not in returnnonemoves
                and (not ignorefailures or action.GetSuccess())
                and (lookformoves == [] or action.GetMove().Name in lookformoves)):
                if (ignorepp):
                    thismove = copy.deepcopy(action.GetMove())
                    thismove.PP = thismove.MaxPP
                    return thismove
                elif (returnaction):
                    return action
                else:
                    return action.GetMove()
            elif (action.GetActionType() == ActionTypes.Move 
                and (user == None or action.GetUser() == user)
                and action.GetMove().Name not in ignoremoves
                and action.GetMove().Name in returnnonemoves):
                return None
        return None

    def JustSwitchedIn(actionlog, pkmn):
        if (Turn == 1):
            return True
        for action in reversed(actionlog):
            if (action.GetActionType() == ActionTypes.Pokemon and pkmn in action.GetTargets() and action.GetTurn() == Turn):
                return True
        return False

    def BattlefieldExists(battlefield):
        try:
            return battlefield in BattlefieldEffects.keys()
        except:
            return False        

    #I know this could be simplified, but I'm doing it like this for legibility
    def IsGrounded(pkmn):
        if (pkmn.HasStatus("smacked down") or BattlefieldExists("Gravity")):
            return True
        if ("Flying" in pkmn.GetTypes() or pkmn.HasAbility("Levitate", False) or pkmn.HasStatus("levitating") or pkmn.HasStatus("roosted")):
            return False
        return True

    def IsGroundedSimpleWorld(pkmn, flyingcheck):
        if (pkmn.HasStatus("smacked down") or BattlefieldExists("Gravity")):
            return True
        if (flyingcheck or pkmn.HasAbility("Levitate", False) or pkmn.HasStatus("levitating") or pkmn.HasStatus("roosted")):
            return False
        return True

    def GetImprisonedMoves(mon):
        imprisoningfoe = StatusOnFoes(mon, "imprisoning")
        if (imprisoningfoe != None):
            return imprisoningfoe.GetMoveNames()
        else:
            return []

    def MoveValid(user, maybemove):
        name = maybemove.Name
        return not (maybemove.PP == 0
            or (GetLastMove(ActionLog, user) != None and maybemove != GetLastMove(ActionLog, user) and user.HasAbility("Gorilla Tactics", False))
            or (user.HasStatus("taunted") and maybemove.Category == "Status") 
            or (user.HasStatus("encored") and maybemove != GetLastMove(ActionLog, user))
            or (user.HasStatus("rollout") and name != "Rollout")
            or (user.HasStatus("ice ball") and name != "Ice Ball")
            or (user.HasStatus("biding") and name != "Bide")
            or (user.HasStatus(".disabling") and name == user.GetStatusCount(".disabling"))
            or (user.HasStatus("uproaring") and name != "Uproar")
            or (user.HasStatus("tormented") and maybemove == GetLastMove(ActionLog, user))
            or (user.HasStatus("dug in") and name != "Dig")
            or (user.HasStatus("diving") and name != "Dive")
            or (user.HasStatus("airborne") and name not in ["Fly", "Bounce"])
            or (user.HasStatus("cloaked in light") and name != "Sky Attack")
            or (user.HasStatus("charging light") and name != "Solar Beam")
            or (user.HasStatus("thrashing") and name != "Thrash")
            or (user.HasStatus("gasping") and IsSoundMove(name))
            or (name in GetImprisonedMoves(user)))

    def HasValidMoves(user):
        for move in user.GetMoves():
            if (MoveValid(user, move)):
                return True
        return False

    def WeatherIs(weather):
        if (weather == None and CurrentWeather == None):
            return True
        return (CurrentWeather != None and CurrentWeather[0] == weather) and not AbilityOnField("Cloud Nine")

    def IsExplosion(movename):
        return movename in ["Self-Destruct", "Explosion", "Mind Blown", "Misty Explosion"]

    def IsPunchMove(movename):
        return "Punch" in movename or movename in ["Meteor Mash", "Headlong Rush", "Plasma Fists", "Rage Fist", "Surging Strikes", "Wicked Blow", "Meteor Mash", "Sky Uppercut", "Ice Hammer", "Hammer Arm", "Double Iron Bash", "Headlong Rush"]

    def IsSliceMove(movename):
        return movename in ["Aerial Ace", "Air Cutter", "Air Slash", "Aqua Cutter", "Behemoth Blade", "Bitter Blade", "Ceaseless Edge", "Cross Poison", "Cut", "Fury Cutter", "Kowtow Cleave", "Leaf Blade", "Night Slash", "Population Bomb", "Psyblade", "Psycho Cut", "Razor Leaf", "Razor Shell", "Sacred Sword", "Slash", "Solar Blade", "Stone Axe", "X-Scissor"]

    def IsSoundMove(movename):
        return movename in ["Boomburst", "Bug Buzz", "Chatter", "Clanging Scales", "Clangorous Soul", "Clangorous Soulblaze", "Confide", "Disarming Voice", "Echoed Voice", "Eerie Spell", "Grass Whistle", "Growl", "Heal Bell", "Howl", "Hyper Voice", "Metal Sound", "Noble Roar", "Overdrive", "Parting Shot", "Perish Song", "Relic Song", "Roar", "Round", "Screech", "Shadow Panic*", "Sing", "Snarl", "Snore", "Sparkling Aria", "Supersonic", "Torch Song", "Uproar"]

    def IsBiteMove(movename):
        return "Fang" in movename or movename in ["Bite", "Crunch", "Fishious Rend", "Jaw Lock"]

    def AbilityOnField(abilityname):
        for mon in Battlers():
            if mon.HasAbility(abilityname):
                return True
        return False

    def StatusInBattlers(statusname):
        for mon in Battlers():
            if mon.HasStatus(statusname):
                return True
        return False

    def StatusOnFoes(mon, statusname):
        if (mon in FriendlyBattlers()):
            for othermon in EnemyBattlers():
                if othermon.HasStatus(statusname):
                    return othermon
        else:
            for othermon in FriendlyBattlers():
                if othermon.HasStatus(statusname):
                    return othermon
        return None

    def EffectOnField(effectname):
        return effectname in FriendlyEffects.keys() + EnemyEffects.keys()

    def EffectOnOwnField(mon, effectname):
        if (mon.GetTrainerType() != TrainerType.Enemy):
            return effectname in FriendlyEffects.keys()
        else:
            return effectname in EnemyEffects.keys()

    def EffectOnOpponentField(mon, effectname):
        if (mon.GetTrainerType() == TrainerType.Enemy):
            return effectname in FriendlyEffects.keys()
        else:
            return effectname in EnemyEffects.keys()

    def GetFieldEffects(mon):
        if (mon.GetTrainerType() == TrainerType.Enemy):
            return EnemyEffects
        else:
            return FriendlyEffects

    def GetBattlers(mon, reverse = False):
        if (mon.GetTrainerType() == TrainerType.Enemy):
            return EnemyBattlers() if not reverse else FriendlyBattlers()
        else:
            return FriendlyBattlers() if not reverse else EnemyBattlers()

    def IsHealingMove(move):
        return move.Name in ['Draining Kiss', 'Floral Healing', 'Giga Drain', 'Rest', 'Synthesis', 'Absorb', 'Drain Punch', 'Dream Eater', 'Heal Order', 'Heal Pulse', 'Healing Wish', 'Horn Leech', 'Leech Life', 'Lunar Dance', 'Mega Drain', 'Milk Drink', 'Moonlight', 'Morning Sun', 'Oblivion Wing', 'Parabolic Charge', 'Purify', 'Recover', 'Roost', 'Shore Up', 'Slack Off', 'Soft-Boiled', 'Strength Sap', 'Swallow', 'Wish']

    def AbilityOnOpponentField(mon, abilityname):
        if (mon.GetTrainerType() != TrainerType.Enemy):
            for mon in EnemyBattlers():
                if mon.HasAbility(abilityname):
                    return True
        else:
            for mon in FriendlyBattlers():
                if mon.HasAbility(abilityname):
                    return True
        return False

    def AbilityOnOwnField(mon, abilityname):
        if (mon.GetTrainerType() == TrainerType.Enemy):
            for mon in EnemyBattlers():
                if mon.HasAbility(abilityname):
                    return True
        else:
            for mon in FriendlyBattlers():
                if mon.HasAbility(abilityname):
                    return True
        return False

    def MakesContact(move):
        contact = True
        if (move.Category != "Physical"):
            contact = False

        if (move.Name in ["Aqua Cutter", "Attack Order", "Aura Wheel", "Barrage", "Beak Blast", "Beat Up", "Bone Club", "Bone Rush", "Bonemerang", "Bulldoze", "Bullet Seed", "Diamond Storm", "Dragon Darts", "Drum Beating", "Earthquake", "Egg Bomb", "Explosion", "Feint", "Fissure", "Flower Trick", "Freeze Shock", "Fusion Bolt", "Gigaton Hammer", "Grav Apple", "Gunk Shot", "Ice Shard", "Icicle Crash", "Icicle Spear", "Land's Wrath", "Last Respects", "Leafage", "Magnet Bomb", "Magnitude", "Metal Burst", "Meteor Assault", "Natural Gift", "Order Up", "Pay Day", "Petal Blizzard", "Pin Missile", "Poison Sting", "Poltergeist", "Precipice Blades", "Present", "Psycho Cut", "Pyro Ball", "Razor Leaf", "Rock Blast", "Rock Slide", "Rock Throw", "Rock Tomb", "Rock Wrecker", "Sacred Fire", "Salt Cure", "Sand Tomb", "Scale Shot", "Secret Power", "Seed Bomb", "Self-Destruct", "Shadow Bone", "Sky Attack", "Smack Down", "Sinister Arrow Raid", "Spike Cannon", "Spirit Shackle", "Splintered Stormshards", "Stone Edge", "Thousand Arrows", "Thousand Waves", "Twineedle", "Electro Drift", "Infestation", "Draining Kiss", "Grass Knot", "Wring Out", "Trump Card", "Petal Dance"]):
            contact = not contact
        return contact

    def IsIgnorable(ability):
        return ability in ["Battle Armor", "Clear Body", "Damp", "Dry Skin", "Filter", "Flash Fire", "Flower Gift", "Heatproof", "Hyper Cutter", "Immunity", "Inner Focus", "Insomnia", "Keen Eye", "Leaf Guard", "Levitate", "Lightning Rod", "Limber", "Magma Armor", "Marvel Scale", "Motor Drive", "Oblivious", "Own Tempo", "Sand Veil", "Shell Armor", "Shield Dust", "Simple", "Snow Cloak", "Solid Rock", "Soundproof", "Sticky Hold", "Storm Drain", "Sturdy", "Suction Cups", "Tangled Feet", "Thick Fat", "Unaware", "Vital Spirit", "Volt Absorb", "Water Absorb", "Water Veil", "White Smoke", "Wonder Guard", "Big Pecks", "Contrary", "Friend Guard", "Heavy Metal", "Light Metal", "Magic Bounce", "Multiscale", "Sap Sipper", "Telepathy", "Wonder Skin", "Aura Break", "Aroma Veil", "Bulletproof", "Flower Veil", "Fur Coat", "Overcoat", "Sweet Veil", "Dazzling", "Disguise", "Fluffy", "Queenly Majesty", "Water Bubble", "Ice Scales", "Ice Face", "Mirror Armor", "Pastel Veil", "Punk Rock", "Armor Tail", "Earth Eater", "Good as Gold", "Purifying Salt", "Well-Baked Body", "Wind Rider"]

    def ActivateMoody(pkmn):
        canraise = []
        canlower = []
        returnable = ""

        for i in range(Stats.Attack, Stats.Speed + 1):
            statmod = pkmn.GetStatChanges(i)
            if (statmod != -6):
                canlower.append(i)
            if (statmod != 6):
                canraise.append(i)
        
        raising = (None if len(canraise) == 0 else RandomChoice(canraise))
        if (raising != None):
            returnable += pkmn.ChangeStats(raising, 2, pkmn)
            if (raising in canlower):
                canlower.remove(raising)

        lowering = (None if len(canlower) == 0 else RandomChoice(canlower))
        if (lowering != None):
            returnable += pkmn.ChangeStats(lowering, -1, pkmn)

        return returnable

    def IsSpecialAbility(ability):
        return ability in ["Truant", "Multitype", "Stance Change", "Schooling", "Comatose", "Shields Down", "Disguise", "RKS System", "Battle Bond", "Power Construct", "Ice Face", "Gulp Missile", "Zero to Hero", "Commander", "Trace", "Forecast", "Flower Gift", "Zen Mode", "Illusion", "Imposter", "Power of Alchemy", "Receiver", "Disguise", "Power Construct", "Ice Face", "Hunger Switch", "Gulp Missile", "Neutralizing Gas", "Zero to Hero", "Commander"]

    def CanSwitch(pkmn, forced):
        if ((forced and not pkmn.HasStatus("ingrained")) or pkmn.HasType("Ghost") or pkmn.GetHealthPercentage() <= 0.0):
            return True
        return not (
        pkmn.HasStatus("blocked")
        or pkmn.HasStatus("menaced")
        or pkmn.HasStatus("webbed")
        or pkmn.HasStatus("ingrained") 
        or pkmn.HasStatus("firespun") 
        or pkmn.HasStatus("whirlpooled") 
        or pkmn.HasStatus("bound") 
        or pkmn.HasStatus("clamped") 
        or pkmn.HasStatus("infested") 
        or pkmn.HasStatus("wrapped") 
        or pkmn.HasStatus("anchored") 
        or pkmn.HasStatus("entombed")
        or pkmn.HasStatus("no retreat")
        or (IsGrounded(pkmn) and AbilityOnOpponentField(pkmn, "Arena Trap"))
        or (AbilityOnOpponentField(pkmn, "Shadow Tag") and not (pkmn.HasAbility("Shadow Tag"))) 
        or (pkmn.HasType("Steel") and AbilityOnOpponentField(pkmn, "Magnet Pull")))

    def MoveIsIn(move):
        return move in movesin
    
    def AbilityIsIn(ability):
        return ability in abilitiesin
    
    def GetCamoType():
        camotype = "Normal"
        if (BattlefieldExists("Electric Terrain")):
            camotype = "Electric"
        elif (BattlefieldExists("Misty Terrain")):
            camotype = "Fairy"
        elif (BattlefieldExists("Burial Ground")):
            camotype = "Ghost"
        elif (location == "fields" or BattlefieldExists("Grassy Terrain")):
            camotype = "Grass"
        elif (location == "alley"):
            camotype = "Poison"
        elif (location == "seaport"):
            camotype = "Water"
        elif (location.title() in typenums.keys()):
            camotype = location.title()
        return camotype

    def IsGenderless(mon):
        return pokedexlookup(mon.GetId(), DexMacros.Name) in ["Arceus", "Arctovish", "Arctozolt", "Articuno", "Aura Trio", "Azelf", "Baltoy", "Beldum", "Blacephalon", "Bronzong", "Bronzor", "Brute Bonnet", "Buzzwole", "Calyrex", "Carbink", "Celebi", "Celesteela", "Chi-Yu", "Chien-Pao", "Claydol", "Cobalion", "Cosmoem", "Cosmog", "Cryogonal", "Darkrai", "Deoxys", "Dhelmise", "Dialga", "Diancie", "Ditto", "Dracovish", "Dracozolt", "Electrode", "Entei", "Eternatus", "Falinks", "Fezandipiti", "Flutter Mane", "Genesect", "Gholdengo", "Gimmighoul", "Giratina", "Glastrier", "Golett", "Golurk", "Great Tusk", "Groudon", "Guzzlord", "Ho-Oh", "Hoopa", "Iron Bundle", "Iron Hands", "Iron Jugulis", "Iron Leaves", "Iron Moth", "Iron Thorns", "Iron Treads", "Iron Valiant", "Jirachi", "Kartana", "Keldeo", "Klang", "Klink", "Klinklang", "Koraidon", "Kyogre", "Kyurem", "Lugia", "Lunala", "Lunatone", "Magearna", "Magnemite", "Magneton", "Magnezone", "Manaphy", "Marshadow", "Maushold", "Melmetal", "Meloetta", "Meltan", "Mesprit", "Metagross", "Metang", "Mew", "Mewtwo", "Minior", "Miraidon", "Moltres", "Munkidori", "Naganadel", "Necrozma", "Nihilego", "Ogerpon", "Okidogi", "Palkia", "Pheromosa", "Phione", "Poipole", "Polteageist", "Porygon", "Porygon-Z", "Porygon2", "Raikou", "Rayquaza", "Regice", "Regidrago", "Regieleki", "Regigigas", "Regirock", "Registeel", "Reshiram", "Roaring Moon", "Rotom", "Sandy Shocks", "Scream Tail", "Shaymin", "Shedinja", "Silvally", "Sinistea", "Slither Wing", "Solgaleo", "Solrock", "Spectrier", "Stakataka", "Starmie", "Staryu", "Suicune", "Tandemaus", "Tapu Bulu", "Tapu Fini", "Tapu Koko", "Tapu Lele", "Terapagos", "Terrakion", "Ting-Lu", "Type: Null", "Unown", "Uxie", "Victini", "Virizion", "Volcanion", "Voltorb", "Walking Wake", "Wo-Chien", "Xerneas", "Xurkitree", "Yveltal", "Zacian", "Zamazenta", "Zapdos", "Zarude", "Zekrom", "Zeraora", "Zygarde"]

    def Battlers(speedsort = False):
        battlers = []
        for trainer in Trainers:
            battlers += trainer.GetLead(False)
        if (speedsort):
            battlers.sort(key=(lambda entry : (-entry.GetStat(Stats.Speed, triggerAbilities=False))))
        return battlers

    def AssignOwners():
        for trainer in Trainers:
            for mon in trainer.GetTeam():
                mon.Owner = trainer
                mon.TrainerType = trainer.GetType()
                mon.ItemHistory = [("Started", mon.GetItem(), 0)]
                mon.ResetCaught()

    def PlayerBattlers():
        players = []
        for mon in Battlers():
            if (mon.GetTrainerType() == TrainerType.Player):
                players.append(mon)
        return players

    def PlayerPokemon():
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Player):
                return trainer.GetTeam()
        return []

    def EnemyPokemon():
        enemies = []
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy):
                enemies += trainer.GetTeam()
        return enemies

    def FriendlyPokemon():
        enemies = []
        for trainer in Trainers:
            if (trainer.GetType() != TrainerType.Enemy):
                enemies += trainer.GetTeam()
        return enemies

    def FriendlyUnfainteds():
        unfainteds = []
        for trainer in Trainers:
            if (trainer.GetType() != TrainerType.Enemy):
                unfainteds += trainer.GetUnfaintedTeam()
        return unfainteds

    def AllyBattlers():
        allies = []
        for mon in Battlers():
            if (mon.GetTrainerType() == TrainerType.Ally):
                allies.append(mon)
        return allies

    #prioritize foes with less health. 
    #prioritize foes with attack buffs
    #prioritize foes with defense debuffs.
    #prioritize foes with less speed
    #prioritize foes over allies

    def RankTargets(mon):
        targets = {}
        possiblemoves = GetValidMoves(mon)
        for move in possiblemoves:
            movetype = typeints[math.ceil(mon.GetPersonality() * 17)] if move.Name == "Hidden Power" else move.Type
            onlyenemies = GetMoveRange(move) in [Range.Adjacent, Range.Any]
            onlyenemies = False if move.Name in ["Steady Flame", "Will-O-Wisp"] else onlyenemies
            subtargets = GetTargets(mon, GetMoveRange(move), onlyenemies)
            spreadmoveunresisted = True
            if (GetMoveRange(move) in [Range.AllAdjacent, Range.AllAdjacentFoes, Range.AllFoes, Range.AllAllies, Range.All]):
                for enemies in subtargets:
                    if (GetTypeBonus(move.Name, move.Type, enemies, mon) < 1) and (enemies.TrainerType != mon.TrainerType) and (move.Power > 0):
                        spreadmoveunresisted = False
                    if MoveCanFail(move.Name, mon, enemies):
                        spreadmoveunresisted = False
            if move.Name in ["Stealth Rock", "Toxic Spikes", "Spikes"]:
                enemycounttotal = 0
                toxicspikesremoval = False
                for trainer in FriendlyTrainers():
                    enemycounttotal += len(trainer.Team)
                    for enemy in trainer.Team:
                        toxicspikesremoval == (enemy.HasType("Poison") and enemy.GetHealth() > 0)
            if move.Name in ["Light Screen", "Reflect"]:
                enemyatk = 0
                enemyspatk = 0
                for enemymon in FriendlyBattlers():
                    enemyatk = enemyatk + enemymon.GetStat(Stats.Attack, absolute=True)
                    enemyspatk = enemyspatk + enemymon.GetStat(Stats.SpecialAttack, absolute=True)
            for target in subtargets:
                targets[(target, move)] = (
                    (
                        (
                            move.Power / 10.0
                            * ((2 if mon.HasAbility("Adaptability", False) else 1.5) if mon.HasType(movetype) else 1)
                            * (max(mon.GetStatChanges(Stats.Attack)+2, 2)/(min(mon.GetStatChanges(Stats.Attack)-2, -2)*-1) if move.Category == "Physical" else 1)
                            / (max(target.GetStatChanges(Stats.Defense)+2, 2)/(min(target.GetStatChanges(Stats.Defense)-2, -2)*-1) if move.Category == "Physical" else 1)
                            * (max(mon.GetStatChanges(Stats.SpecialAttack)+2, 2)/(min(mon.GetStatChanges(Stats.SpecialAttack)-2, -2)*-1) if move.Category == "Special" else 1)
                            / (max(target.GetStatChanges(Stats.SpecialDefense)+2, 2)/(min(target.GetStatChanges(Stats.SpecialDefense)-2, -2)*-1) if move.Category == "Special" else 1)
                            * (2 if movetype == "Electric" and mon.HasStatus("charged") else 1)
                            * (4 if (move.Name == "Rollout" or move.Name == "Ice Ball") and mon.HasStatus(".curling") else 1)
                            * (1.5 if movetype == "Water" and WeatherIs("rainy") else 1)
                            * (0.5 if movetype == "Fire" and WeatherIs("rainy") else 1)
                            * (1.5 if movetype == "Fire" and WeatherIs("sunny") else 1)
                            * (0.5 if movetype == "Water" and WeatherIs("sunny") else 1)
                            * ((0.5 if not mon.HasAbility("Guts", False) else 1.5) if move.Category == "Physical" and mon.HasStatus("burned") else 1)
                            * (1.5 if move.Power <= 60 and mon.HasAbility("Technician", False) else 1)
                            * (1.1 if mon.Item in elementitems and elementitems[mon.Item] == move.Type else 1)
                        )
                        +
                        (
                            (
                                (8 if move.Category == "Status" else 0)
                                + (5 * move.Accuracy if move.Name in ["Slow Freeze", "Dark Void", "Grass Whistle", "Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Yawn"] else 0)
                                + (5 * target.GetHealthPercentage() if move.Name in ["Leech Seed", "Bad Breath", "Toxic", "Poison Gas", "Poison Powder", "Toxic Thread"] else 0)
                                + (5 if move.Name in ["Nuzzle", "Thunder Wave", "Glare", "Stun Spore"] and (target.GetStat(Stats.Speed)/2 < mon.GetStat(Stats.Speed) <= target.GetStat(Stats.Speed)) else 0)
                                + (5 if (move.Name in ["Will-O-Wisp", "Steady Flame"] and target.GetStat(Stats.Attack, absolute=True) > (target.GetStat(Stats.SpecialAttack, absolute=True)*1.1)) else 0)
                                + (5 if (IsSetupMove(move.Name, mon) and (mon.GetHealthPercentage() >= 0.7)) else 0)
                                + (5 if IsDebuffStatusMove(move.Name) and target.GetTotalStatChanges() >= 0 else 0) #split this up into the different stats later
                                + (5 * (1 - mon.GetHealthPercentage()) if IsHealingMove(move) else 0) #replace the healingmove function with a different check later, triage boosted moves doesnt cover everything
                                + (5 if move.Name == "Refresh" and (mon.HasNormalStatus() and mon.GetHealthPercentage() >= 0.5) else 0)
                                + (10*math.ceil(2-(target.GetHealth()/40)) if move.Name == "Dragon Rage" else 0)
                                + (2*(enemycounttotal-len(EnemyBattlers())-1) if move.Name in ["Stealth Rock", "Toxic Spikes", "Spikes"] else 0)
                                + (max(target.GetStat(Stats.SpecialAttack), target.GetStat(Stats.Attack)) if (move.Name == "Fake Out" or move.Name == "Legacy") else 0)
                                + (5 if move.Name == "Reflect" and enemyatk > enemyspatk else 0)
                                + (5 if move.Name == "Light Screen" and enemyspatk > enemyatk else 0)
                                + (5 * max(target.GetTotalStatChanges(), 0) if move.Name == "Clear Smog" else 0)
                                + (5 if move.Name == "Recycle" else 0)
                                + (5 if move.Name == "Tailwind" and (len(EnemyBattlers()) > 1 or (target.GetStat(Stats.Speed)/2 < mon.GetStat(Stats.Speed) <= target.GetStat(Stats.Speed))) else 0)
                            )
                            * (2 if (mon.EVs[Stats.Health] + mon.EVs[Stats.Defense] + mon.EVs[Stats.SpecialDefense]) > (mon.EVs[Stats.Attack] + mon.EVs[Stats.SpecialAttack] + mon.EVs[Stats.Speed]) else 1)
                        )
                        +
                        (
                            (
                                (5 if IsSetupMove(move.Name, mon) and (Turn == 1 or Turn - mon.GetTurnSwitchedIn() <= 1) else 0)
                                + (5 if move.Name == "Healing Spring" and (mon.HasAbility("Swift Swim", False) or (mon.HasAbility("Hydration", False) and (mon.HasNormalStatus() or mon.HasStatus("drowsy")))) else 0)
                                + (5 * (1 - target.GetHealthPercentage()) if not move.Category == "Status" else 0)
                                + (max(10 - math.sqrt(target.GetHealthPercentage() * 200), 0) if IsPriorityDamageMove(move, mon) and (target.GetStat(Stats.Speed) >= mon.GetStat(Stats.Speed)) else 0)
                                + ((5 * (len(subtargets) - 1)) if ((GetMoveRange(move) in [Range.AllAdjacent, Range.AllAdjacentFoes, Range.AllFoes, Range.AllAllies, Range.All]) and spreadmoveunresisted) else 0)
                            )
                            * (2 if (mon.EVs[Stats.Attack] + mon.EVs[Stats.SpecialAttack] + mon.EVs[Stats.Speed]) > (mon.EVs[Stats.Health] + mon.EVs[Stats.Defense] + mon.EVs[Stats.SpecialDefense])  else 1)
                        )
                        +
                        (
                            (
                                (len(mon.Moves) - 1 if move.Name == mon.Moves[0].Name else 0)
                                + (len(mon.Moves) - 2 if (len(mon.Moves) > 1 and move.Name == mon.Moves[1].Name) else 0)
                                + (len(mon.Moves) - 3 if (len(mon.Moves) > 2 and move.Name == mon.Moves[2].Name) else 0)
                            )
                            * (0 if mon.GetTrainer().GetName() == "ethan" else 1)
                        ) 
                    )
                    * ((2 if target.HasAbility("Guts", False) and not target.HasNormalStatus() else 0) if target in EnemyBattlers() and move.Name in ["Will-O-Wisp", "Steady Flame"] else 1)
                    * (0.75 ** mon.GetTotalStatChanges() if IsSetupMove(move.Name, mon) and move.Category == "Status" else 1)
                    * (0.75 ** (-1 * target.GetTotalStatChanges()) if IsDebuffStatusMove(move.Name) else 1)
                    * (2*(1 - (math.sqrt(mon.GetHealthPercentage())*1.5)+0.5) if IsHealingMove(move) and move.Category == "Status" else 1) #replace the healingmove function with a different check later, triage boosted moves doesnt cover everything
                    * (0 if MoveCanFail(move.Name, mon, target) else 1)
                    * (0 if move.Name in ["Stealth Rock", "Toxic Spikes", "Spikes"] and enemycounttotal == len(EnemyBattlers()) else 1)
                    * (0 if (move.Category == "Status" and mon != target and target.HasStatus("substitute") and not IsSoundMove(move.Name) and not target.HasAbility("Infiltrator", False)) else 1) #technically not correct but the battle code does this check as well
                    * (0.5 if (move.Name == "Legacy") and (target.HasType("Electric") or target.HasNormalStatus()) else 1)
                    * (2 if move.Name in ["Fake Out", "Legacy"] and (Turn == 1 or Turn - mon.GetTurnSwitchedIn() <= 1) and target.GetMoveByName("Legacy") != None and mon.GetStat(Stats.Speed) > target.GetStat(Stats.Speed) else 1)
                    * (0.5 if move.Name == "Toxic Spikes" and toxicspikesremoval == True else 1)
                    * (2 if move.Name in ["Reflect", "Light Screen", "Aurora Veil"] and mon.HasItem("Light Clay") else 1)
                    * (GetTypeBonus(move.Name, movetype, target, mon) if move.Power > 0 else 1.0)
                )

                print(mon.GetNickname() + " uses " + move.Name + " on " + target.GetNickname() + " for " + str(targets[(target, move)]) + " points")
            
        print("\n\n\n")       

        return sorted(targets, key=targets.get, reverse=True)

    def MoveCanFail(movename, mon, target):
        if movename == "Recycle":
            if (mon.GetItem() == None):
                for itemaction, item, turn in reversed(mon.GetItemHistory()):
                    if (itemaction == "Used"):
                        return False
            return True
        return True if (
            (movename in ["Will-O-Wisp", "Steady Flame"] and (target.HasType("Fire") or target.HasAbility("Thermal Exchange", False) or target.HasAbility("Water Veil", False) or (target.HasAbility("Guts", False) and target in FriendlyBattlers()) or target.HasAbility("Flash Fire", False)))
            or (movename == "Leech Seed" and (target.HasStatus("seeded") or target.HasType("Grass")))
            or (IsNonVolatileStatus(movename, mon) and (target.HasNormalStatus() or target.HasStatus("drowsy") or (BattlefieldExists("Misty Terrain") and target.IsGrounded()) or (WeatherIs("sunny") and target.HasAbility("Leaf Guard", False)) or EffectOnOpponentField(mon, "safeguard") or target.HasAbility("Purifying Salt", False) or target.HasAbility("Comatose", False)))
            or (movename == "Confuse Ray" and target.HasStatus("confused"))
            or (movename in ["Legacy", "Fake Out", "First Impression"] and not (Turn == 1 or Turn - mon.GetTurnSwitchedIn() <= 1))
            or (movename in ["Cotton Spore", "Magic Powder", "Poison Powder", "Powder", "Sleep Powder", "Spore", "Stun Spore"] and (target.HasType("Grass") or target.HasAbility("Overcoat", False) or target.HasItem("Safety Goggles")))
            or (movename == "Spikes" and (EffectOnOwnField(target, "spikes") and GetFieldEffects(target)["spikes"] >= 3))
            or (movename == "Toxic Spikes" and (EffectOnOwnField(target, "toxic spikes") and GetFieldEffects(target)["toxic spikes"] >= 2))
            or (movename == "Stealth Rock" and EffectOnOpponentField(mon, "stealthy rocks"))
            or (movename == "Bad Breath" and ((((target.HasType("Steel") or target.HasType("Poison") or target.HasAbility("Immunity"), False) and (target.HasType("Electric") or target.HasAbility("Limber", False))) or target.HasNormalStatus() or BattlefieldExists("Misty Terrain") or (WeatherIs("sunny") and target.HasAbility("Leaf Guard", False)) or EffectOnOpponentField(mon, "safeguard")) and (target.HasStatus("confused") or target.HasAbility("Own Tempo", False))))
            or (movename in ["Protect", "Detect", "Wide Guard", "Mat Block", "Enshroud", "Crafty Shield", "Spiky Shield", "Splinter Shield", "Baneful Bunker", "King's Shield", "Max Guard", "Obstruct", "Silk Trap", "Endure", "Quick Guard", "Wide Guard"] and mon.GetStatusCount(".protections") > 0)
            or (movename == "Refresh" and (mon.HasStatus("Sleep") or mon.HasStatus("Freeze") or not mon.HasNormalStatus()))
            or (movename in ["Healing Spring", "Rain Dance"] and WeatherIs("rainy"))
            or ((movename == "Reflect" and EffectOnOwnField(mon, "reflect")) or (movename == "Light Screen" and EffectOnOwnField(mon, "light screen")) or (movename == "Aurora Veil" and EffectOnOwnField(mon, "aurora veil")))
            or (movename in ["Poison Gas", "Poison Powder", "Toxic Thread", "Toxic"] and (target.HasType("Steel") or target.HasType("Poison") or target.HasAbility("Immunity"), False))
            or (movename == "Tailwind" and EffectOnOwnField(mon, "tailwind"))
            or (movename in ["Nuzzle", "Thunder Wave", "Glare", "Stun Spore"] and (target.HasType("Electric") or target.HasAbility("Limber", False)))
            or (IsDebuffStatusMove(movename) and (target.HasAbility("Clear Body", False) or target.HasAbility("White Smoke", False) or target.HasAbility("Full Metal Body", False) or target.HasAbility("Contrary", False) or target.HasAbility("Defiant", False) or target.HasAbility("Competitive", False)))
            ) else False

    def IsPriorityDamageMove(move, mon):
        if move.Name == "Grassy Glide" and BattlefieldExists("Grassy Terrain"): return True
        if move.Type == "Flying" and mon.GetHealthPercentage() >= 1 and mon.HasAbility("Gale Wings", False): return True
        if IsHealingMove(move) and mon.HasAbility("Triage", False) and move.Power > 0: return True
        return move.Name in ["Extreme Speed", "First Impression", "Accelerock", "Aqua Jet", "Bullet Punch", "Ice Shard", "Jet Punch", "Mach Punch", "Quick Attack", "Shadow Sneak", "Vacuum Wave", "Water Shuriken"]

    def IsSetupMove(movename, mon):
        if (movename in ["Protect", "Detect"] and (mon.HasAbility("Speed Boost", False) or mon.HasAbility("Moody", False))): return True
        return movename in ["Energize", "Bark Up", "Healing Spring", "Calm Mind", "Swords Dance", "Dragon Dance", "Nasty Plot", "Bulk Up", "Clangorous Soul", "Coil", "Curse", "Growth", "Hone Claws", "Howl", "Meditate", "No Retreat", "Power-Up Punch", "Sharpen", "Shift Gear", "Tidy Up", "Victory Dance", "Quiver Dance", "Work Up", "Fillet Away", "Shell Smash", "Belly Drum", "Cosmic Power", "Defend Order", "Defense Curl", "Harden", "Psyshield Bash", "Skull Bash", "Stockpile", "Withdraw", "Acid Armor", "Barrier", "Diamond Storm", "Iron Defense", "Shelter", "Stuff Cheeks", "Cotton Guard", "Fiery Dance", "Meteor Beam", "Torch Song", "Geomancy", "Tail Glow", "Take Heart", "Charge", "Amnesia", "Aqua Step", "Aura Wheel", "Esper Wing", "Flame Charge", "Rapid Spin", "Scale Shot", "Trailblaze", "Agility", "Autotomize", "Rock Polish", "Tailwind", "Double Team", "Minimize", "Trailblaze", "Charge Beam", "Flame Charge"]

    def IsDebuffStatusMove(movename):
        return movename in ["Baby-Doll Eyes", "Growl", "Noble Roar", "Play Nice", "Tearful Look", "Tickle", "Charm", "Feather Dance", "Leer", "Tail Whip", "Screech", "Confide", "Captivate", "Fake Tears", "Metal Sound", "Tar Shot", "Cotton Spore", "Scary Face", "String Shot", "Sweet Scent", "Flash", "Kinesis", "Sand Attack", "Smokescreen"]

    def IsNonVolatileStatus(movename, mon):
        if movename == "Psycho Shift" and mon.HasNormalStatus(): return True
        return movename in ["Steady Flame", "Slow Freeze", "Will-O-Wisp", "Glare", "Stun Spore", "Thunder Wave", "Poison Gas", "Poison Powder", "Toxic Thread", "Dark Void", "Grass Whistle", "Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Yawn", "Nuzzle"]

    def FriendlyStatChanges():
        totalval = 0
        for mon in FriendlyBattlers():
            totalval += mon.GetTotalStatChanges()
        return totalval

    def EnemyStatChanges():
        totalval = 0
        for mon in EnemyBattlers():
            totalval += mon.GetTotalStatChanges()
        return totalval

    def GetValidMoves(mon):
        validmoves = []
        for enemymove in mon.GetMoves():
            if (MoveValid(mon, enemymove)):
                validmoves.append(enemymove)
        if (len(validmoves) == 0):
            validmoves = [struggle]
        return validmoves

    def FriendlyBattlers():
        return PlayerBattlers() + AllyBattlers()

    def EnemyBattlers():
        enemies = []
        for mon in Battlers():
            if (mon.GetTrainerType() == TrainerType.Enemy):
                enemies.append(mon)
        return enemies

    def FriendlyTrainers():
        friends = []
        for trainer in Trainers:
            if (trainer.GetType() != TrainerType.Enemy):
                friends.append(trainer)
        return friends

    def EnemyTrainers():
        enemies = []
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy):
                enemies.append(trainer)
        return enemies

    def GetGrid():
        pkmngrid = [[], []]
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy):
                pkmngrid[1] += trainer.GetLead(False)
            else:
                pkmngrid[0] += trainer.GetLead(False)
        return pkmngrid

    def GetTargets(mon, range = Range.Adjacent, forceenemy = False):
        xcoord = -1
        ycoord = -1
        for i, sublist in enumerate(GetGrid()):
            for j, othermon in enumerate(GetGrid()[i]):
                if (mon == othermon):
                    xcoord = i
                    ycoord = j
        adjacents = []

        for i, sublist in enumerate(GetGrid()):
            for j, othermon in enumerate(GetGrid()[i]):
                if (othermon != None):
                    mygrid = []
                    othergrid = []
                    if (mon in GetGrid()[0]):
                        mygrid = GetGrid()[0]
                        othergrid = GetGrid()[1]
                    else:
                        mygrid = GetGrid()[1]
                        othergrid = GetGrid()[0]
                    verticality = j
                    isself = othermon == mon
                    
                    overwriteadjacency = 0
                    if (len(mygrid) + len(othergrid) == 5):
                        if (len(mygrid) == 2 and mygrid.index(mon) == 1 and othermon not in mygrid):
                            j -= 1
                        elif (len(mygrid) == 3 and mygrid.index(mon) != 1 and othermon not in mygrid):
                            if (mygrid.index(mon) == 0 and othergrid.index(othermon) == 1):
                                j += 1
                            elif (mygrid.index(mon) == 2 and othergrid.index(othermon) == 0):
                                j -= 1
                    elif (len(GetGrid()[0]) + len(GetGrid()[1]) <= 4 and mon in mygrid and othermon in othergrid):
                        overwriteadjacency = -99

                    isadjacent = overwriteadjacency + abs(j - ycoord) <= 1 and not isself
                    isenemy = (mon.GetTrainerType() == TrainerType.Enemy and othermon.GetTrainerType() != TrainerType.Enemy) or (mon.GetTrainerType() != TrainerType.Enemy and othermon.GetTrainerType() == TrainerType.Enemy)

                    if ((range == Range.Adjacent and isadjacent and (not forceenemy or isenemy)
                        or range == Range.AdjacentFoe and isadjacent and isenemy
                        or range == Range.Any and not isself and (not forceenemy or isenemy)
                        or range == Range.AnyOrSelf
                        or range == Range.AdjacentAllyOrSelf and (isadjacent or isself) and not isenemy
                        or range == Range.AllAdjacentFoes and isadjacent and isenemy
                        or range == Range.AllAdjacent and isadjacent
                        or range == Range.AllAllies and not isself and not isenemy
                        or range == Range.AllFoes and isenemy
                        or range == Range.All
                        or range == Range.AdjacentAlly and isadjacent and not isenemy
                        or range == Range.Self and isself
                        or range == Range.AllAlliesAndSelf and not isenemy)
                        or range == Range.AnyAlly and not isenemy):
                            adjacents.append(othermon)
                
        return adjacents

    def GetRandomAdjacentFoe(mon):
        return RandomChoice(GetTargets(mon))

    def GetMoveRange(move):
        ranges = {
            Range.AdjacentFoe : ["Doodle","G-Max Befuddle","G-Max Cannonade","G-Max Centiferno","G-Max Chi Strike","G-Max Cuddle","G-Max Depletion","G-Max Drum Solo","G-Max Finale","G-Max Fireball","G-Max Foam Burst","G-Max Gold Rush","G-Max Gravitas","G-Max Hydrosnipe","G-Max Malodor","G-Max Meltdown","G-Max One Blow","G-Max Rapid Flow","G-Max Replenish","G-Max Resonance","G-Max Sandblast","G-Max Smite","G-Max Steelsurge","G-Max Stonesurge","G-Max Stun Shock","G-Max Sweetness","G-Max Tartness","G-Max Terror","G-Max Vine Lash","G-Max Volcalith","G-Max Volt Crash","G-Max Wildfire","G-Max Wind Rage","Max Airstream","Max Darkness","Max Flare","Max Flutterby","Max Geyser","Max Hailstorm","Max Knuckle","Max Lightning","Max Mindstorm","Max Ooze","Max Overgrowth","Max Phantasm","Max Quake","Max Rockfall","Max Starfall","Max Steelspike","Max Strike","Max Wyrmwind","Me First"],
            Range.Any : ["Struggle","Acrobatics","Aerial Ace","Aeroblast","Air Slash","Aura Sphere","Bounce","Brave Bird","Chatter","Dark Pulse","Dragon Pulse","Drill Peck","Fly","Flying Press","Gust","Heal Pulse","Hurricane","Oblivion Wing","Peck","Pluck","Shadow Blast","Shadow Blitz","Shadow Bolt","Shadow Break","Shadow Chill","Shadow End","Shadow Fire","Shadow Rush","Sky Attack","Sky Drop","Water Pulse","Wing Attack"],
            Range.AnyOrSelf : ["Clear Mind", "Metallize"],
            Range.AdjacentAllyOrSelf : ["Acupressure"], 
            Range.AllAdjacentFoes : ["Breaking Swipe", "Acid","Air Cutter","Astral Barrage","Bleakwind Storm","Blizzard","Bouncy Bubble","Breaking Swipe","Bubble","Burning Jealousy","Captivate","Clanging Scales","Clangorous Soulblaze","Core Enforcer","Cotton Spore","Dark Void","Dazzling Gleam","Diamond Storm","Disarming Voice","Dragon Energy","Electroweb","Eruption","Fiery Wrath","G-Max Snooze","Glacial Lance","Glaciate","Growl","Heal Block","Heat Wave","Hyper Voice","Icy Wind","Incinerate","Land's Wrath","Leer","Make It Rain","Mortal Spin","Muddy Water","Origin Pulse","Overdrive","Poison Gas","Powder Snow","Precipice Blades","Razor Leaf","Razor Wind","Relic Song","Rock Slide","Sandsear Storm","Shell Trap","Snarl","Splishy Splash","Springtide Storm","String Shot","Struggle Bug","Sweet Scent","Swift","Tail Whip","Thousand Arrows","Thousand Waves","Twister","Venom Drench","Water Spout","Wildbolt Storm"], 
            Range.AllAdjacent : ["Boomburst","Brutal Swing","Bulldoze","Corrosive Gas","Discharge","Earthquake","Explosion","Lava Plume","Magnitude","Mind Blown","Misty Explosion","Parabolic Charge","Petal Blizzard","Searing Shot","Self-Destruct","Sludge Wave","Sparkling Aria","Surf","Synchronoise","Teeter Dance"], 
            Range.AllAllies : ["Coaching"],
            Range.AllFoes : ["Shadow Down","Shadow Hold","Shadow Mist","Shadow Panic","Shadow Rave","Shadow Storm","Shadow Wave","Spikes","Stealth Rock","Sticky Web","Toxic Spikes"],
            Range.All : ["Healing Spring", "Simple World", "Burial Ground", "Chilly Reception","Court Change","Electric Terrain","Fairy Lock","Flower Shield","Grassy Terrain","Gravity","Hail","Haze","Ion Deluge","Magic Room","Misty Terrain","Mud Sport","Perish Song","Psychic Terrain","Rain Dance","Rototiller","Sandstorm","Shadow Half","Shadow Shed","Shadow Sky","Snowscape","Sunny Day","Teatime","Trick Room","Water Sport","Wonder Room"],
            Range.AdjacentAlly : ["Aromatic Mist","Helping Hand","Hold Hands"],
            Range.Self : ["Discard", "Splinter Shield", "Buffet", "Bark Up", "Deathless", "Wing It", "Energize", "Chrysalize", "Enshroud", "Buffet","Acid Armor","Agility","Ally Switch","Amnesia","Aqua Ring","Assist","Autotomize","Baneful Bunker","Barrier","Baton Pass","Belly Drum","Bide","Bulk Up","Calm Mind","Camouflage","Celebrate","Charge","Clangorous Soul","Coil","Comeuppance","Conversion","Copycat","Cosmic Power","Cotton Guard","Counter","Curse","Defend Order","Defense Curl","Destiny Bond","Detect","Double Team","Dragon Dance","Endure","Extreme Evoboost","Fillet Away","Focus Energy","Follow Me","Geomancy","Growth","Grudge","Harden","Heal Order","Healing Wish","Helping Hand","Hone Claws","Howl","Imprison","Ingrain","Iron Defense","King's Shield","Laser Focus","Lunar Dance","Magic Coat","Magnet Rise","Max Guard","Meditate","Metal Burst","Metronome","Milk Drink","Minimize","Mirror Coat","Moonlight","Morning Sun","Nasty Plot","Nature Power","No Retreat","Obstruct","Outrage","Petal Dance","Power Shift","Power Trick","Protect","Quiver Dance","Rage Powder","Raging Fury","Recover","Recycle","Refresh","Rest","Revival Blessing","Rock Polish","Roost","Sharpen","Shed Tail","Shell Smash","Shelter","Shift Gear","Shore Up","Silk Trap","Slack Off","Sleep Talk","Snatch","Soft-Boiled","Spiky Shield","Splash","Stockpile","Struggle","Stuff Cheeks","Substitute","Swallow","Swords Dance","Synthesis","Tail Glow","Take Heart","Teleport","Thrash","Tidy Up","Uproar","Victory Dance","Wish","Withdraw","Work Up"],
            Range.AllAlliesAndSelf : ["Aromatherapy","Aurora Veil","Crafty Shield","Gear Up","Happy Hour","Heal Bell","Howl","Jungle Healing","Life Dew","Light Screen","Lucky Chant","Lunar Blessing","Magnetic Flux","Mat Block","Mist","Quick Guard","Reflect","Safeguard","Tailwind","Wide Guard"],
            Range.AnyAlly : []
        }

        for key in ranges.keys():
            if move.Name in ranges[key]:
                return key
        return 0

    def GetTrainers(monlist):
        owners = []
        for mon in monlist:
            owners.append(mon.GetTrainer())
        return owners

    def GetSlots(monlist):
        slots = []
        for mon in monlist:
            slots.append(mon.GetTrainer().GetTeam().index(mon))
        return slots

    def HasFaintedLead(trainer):
        hasFaintedLead = False
        for mon in trainer.GetTeam()[:trainer.GetNumber()]:
            if (mon.GetHealth() <= 0):
                hasFaintedLead = True
        return hasFaintedLead

    def IsSnatchable(movename):
        return movename in ["Acid Armor", "Agility", "Amnesia", "Aqua Ring", "Aromatherapy", "Aurora Veil", "Autotomize", "Barrier", "Belly Drum", "Bulk Up", "Calm Mind", "Camouflage", "Charge", "Coil", "Conversion", "Cosmic Power", "Cotton Guard", "Defend Order", "Defense Curl", "Double Team", "Dragon Dance", "Focus Energy", "Gear Up", "Growth", "Harden", "Heal Bell", "Heal Order", "Healing Wish", "Hone Claws", "Howl", "Imprison", "Ingrain", "Iron Defense", "Laser Focus", "Light Screen", "Lucky Chant", "Lunar Dance", "Magnet Rise", "Magnetic Flux", "Mat Block", "Meditate", "Milk Drink", "Minimize", "Mist", "Moonlight", "Morning Sun", "Nasty Plot", "Power Trick", "Quick Guard", "Quiver Dance", "Recover", "Recycle", "Reflect", "Refresh", "Rest", "Rock Polish", "Roost", "Safeguard", "Sharpen", "Shell Smash", "Shift Gear", "Shore Up", "Slack Off", "Soft-Boiled", "Stockpile", "Substitute", "Swallow", "Swords Dance", "Synthesis", "Tail Glow", "Tailwind", "Wide Guard", "Wish", "Withdraw", "Work Up"]

    def AssistCanCall(movename):
        return movename not in ["Assist", "Baneful Bunker", "Beak Blast", "Belch", "Bestow", "Celebrate", "Chatter", "Circle Throw", "Copycat", "Counter", "Covet", "Destiny Bond", "Detect", "Dragon Tail", "Endure", "Feint", "Focus Punch", "Follow Me", "Helping Hand", "Hold Hands", "King's Shield", "Mat Block", "Me First", "Metronome", "Mimic", "Mirror Coat", "Mirror Move", "Phantom Force", "Protect", "Rage Powder", "Shell Trap", "Sketch", "Sleep Talk", "Snatch", "Spiky Shield", "Spotlight", "Struggle", "Switcheroo", "Thief", "Transform", "Trick"]

    def GetMovePower(move):
        if (move.Name in ["Eruption", "Water Spout", "Fissure", "Guillotine", "Horn Drill", "Sheer Cold"]):
            return 150
        elif (move.Name in ["Counter", "Metal Burst", "Mirror Coat"]):
            return 120
        elif (move.Name in ["Crush Grip", "Dragon Rage", "Electro Ball", "Endeavor", "Final Gambit", "Flail", "Frustration", "Grass Knot", "Guardian of Alola", "Gyro Ball", "Heat Crash", "Heavy Slam", "Hidden Power", "Low Kick", "Natural Gift", "Nature's Madness", "Night Shade", "Present", "Psywave", "Punishment", "Return", "Reversal", "Seismic Toss", "Sonic Boom", "Spit Up", "Super Fang", "Trump Card", "Wring Out"]):
            return 80
        elif (move.Name in ["Stored Power", "Power Trip"]):
            return 20
        else:
            return (0 if isinstance(move.Power, str) else move.Power)

    def GetFriendGuardCount(mon):
        count = 0
        for othermon in GetBattlers(mon):
            if (othermon.HasAbility("Friend Guard") and othermon != mon):
                count += 1
        return count

    def NaturalGiftData(berry):
        if (berry == "Cheri Berry"):
            return ("Fire", 80)
        elif (berry == "Chesto Berry"):
            return ("Water", 80)
        elif (berry == "Pecha Berry"):
            return ("Electric", 80)
        elif (berry == "Rawst Berry"):
            return ("Grass", 80)
        elif (berry == "Aspear Berry"):
            return ("Ice", 80)
        elif (berry == "Leppa Berry"):
            return ("Fighting", 80)
        elif (berry == "Oran Berry"):
            return ("Poison", 80)
        elif (berry == "Persim Berry"):
            return ("Ground", 80)
        elif (berry == "Lum Berry"):
            return ("Flying", 80)
        elif (berry == "Sitrus Berry"):
            return ("Psychic", 80)
        elif (berry == "Figy Berry"):
            return ("Bug", 80)
        elif (berry == "Wiki Berry"):
            return ("Rock", 80)
        elif (berry == "Mago Berry"):
            return ("Ghost", 80)
        elif (berry == "Aguav Berry"):
            return ("Dragon", 80)
        elif (berry == "Iapapa Berry"):
            return ("Dark", 80)
        elif (berry == "Razz Berry"):
            return ("Steel", 80)
        elif (berry == "Bluk Berry"):
            return ("Fire", 90)
        elif (berry == "Nanab Berry"):
            return ("Water", 90)
        elif (berry == "Wepear Berry"):
            return ("Electric", 90)
        elif (berry == "Pinap Berry"):
            return ("Grass", 90)
        elif (berry == "Pomeg Berry"):
            return ("Ice", 90)
        elif (berry == "Kelpsy Berry"):
            return ("Fighting", 90)
        elif (berry == "Qualot Berry"):
            return ("Poison", 90)
        elif (berry == "Hondew Berry"):
            return ("Ground", 90)
        elif (berry == "Grepa Berry"):
            return ("Flying", 90)
        elif (berry == "Tamato Berry"):
            return ("Psychic", 90)
        elif (berry == "Cornn Berry"):
            return ("Bug", 90)
        elif (berry == "Magost Berry"):
            return ("Rock", 90)
        elif (berry == "Rabuta Berry"):
            return ("Ghost", 90)
        elif (berry == "Nomel Berry"):
            return ("Dragon", 90)
        elif (berry == "Spelon Berry"):
            return ("Dark", 90)
        elif (berry == "Pamtre Berry"):
            return ("Steel", 90)
        elif (berry == "Watmel Berry"):
            return ("Fire", 100)
        elif (berry == "Durin Berry"):
            return ("Water", 100)
        elif (berry == "Belue Berry"):
            return ("Electric", 100)
        elif (berry == "Occa Berry"):
            return ("Fire", 80)
        elif (berry == "Passho Berry"):
            return ("Water", 80)
        elif (berry == "Wacan Berry"):
            return ("Electric", 80)
        elif (berry == "Rindo Berry"):
            return ("Grass", 80)
        elif (berry == "Yache Berry"):
            return ("Ice", 80)
        elif (berry == "Chople Berry"):
            return ("Fighting", 80)
        elif (berry == "Kebia Berry"):
            return ("Poison", 80)
        elif (berry == "Shuca Berry"):
            return ("Ground", 80)
        elif (berry == "Coba Berry"):
            return ("Flying", 80)
        elif (berry == "Payapa Berry"):
            return ("Psychic", 80)
        elif (berry == "Tanga Berry"):
            return ("Bug", 80)
        elif (berry == "Charti Berry"):
            return ("Rock", 80)
        elif (berry == "Kasib Berry"):
            return ("Ghost", 80)
        elif (berry == "Haban Berry"):
            return ("Dragon", 80)
        elif (berry == "Colbur Berry"):
            return ("Dark", 80)
        elif (berry == "Babiri Berry"):
            return ("Steel", 80)
        elif (berry == "Chilan Berry"):
            return ("Normal", 80)
        elif (berry == "Liechi Berry"):
            return ("Grass", 100)
        elif (berry == "Ganlon Berry"):
            return ("Ice", 100)
        elif (berry == "Salac Berry"):
            return ("Fighting", 100)
        elif (berry == "Petaya Berry"):
            return ("Poison", 100)
        elif (berry == "Apicot Berry"):
            return ("Ground", 100)
        elif (berry == "Lansat Berry"):
            return ("Flying", 100)
        elif (berry == "Starf Berry"):
            return ("Psychic", 100)
        elif (berry == "Enigma Berry"):
            return ("Bug", 100)
        elif (berry == "Micle Berry"):
            return ("Rock", 100)
        elif (berry == "Custap Berry"):
            return ("Ghost", 100)
        elif (berry == "Jaboca Berry"):
            return ("Dragon", 100)
        elif (berry == "Rowap Berry"):
            return ("Dark", 100)
        elif (berry == "Roseli Berry"):
            return ("Fairy", 80)
        elif (berry == "Kee Berry"):
            return ("Fairy", 100)
        elif (berry == "Maranga Berry"):
            return ("Dark", 100)

    def IsBerry(item):
        return item != None and "Berry" in item

    def ReactivateAbility(mon, fromTrace = False):
        returnmessage = ""
        if (mon.GetAbility() not in ["Intimidate", "Anticipation", "Download", "Drizzle", "Drought", "Snow Warning", "Sand Stream", "Forewarn", "Frisk", "Imposter", "Intimidate", "Schooling", "Shields Down", "Screen Cleaner", "Trace"]):
            return returnmessage

        if (not fromTrace):
            if (mon.HasAbility("Trace")):
                tracedmon = random.choice(GetTargets(mon, Range.AdjacentFoe))
                if (not IsSpecialAbility(tracedmon.GetAbility())):
                    mon.ApplyStatus(".tracing", tracedmon.GetAbility())
                    returnmessage += "{} traced the ability {}!".format(mon.GetNickname(), tracedmon.GetAbility())
        
        if (mon.HasAbility("Intimidate")):
            for othermon in GetTargets(mon, Range.AllAdjacentFoes):
                if (not (othermon.HasAbility("Own Tempo") or othermon.HasAbility("Oblivious") or othermon.HasAbility("Inner Focus") or othermon.HasAbility("Scrappy"))):
                    returnmessage += othermon.ChangeStats(Stats.Attack, -1, mon) + " "
                if (othermon.HasAbility("Rattled")):
                    returnmessage += othermon.ChangeStats(Stats.Speed, 1, mon) + " "

        if (mon.HasAbility("Screen Cleaner")):
            removeeffects += ["light screen", "reflect", "aurora veil"]
            effectdel = []
            for cleareffect in EnemyEffects.keys():
                if (cleareffect in removeeffects):
                    effectdel.append(cleareffect)
            for clearingeffect in effectdel:
                del EnemyEffects[clearingeffect]
            if (len(effectdel) > 0):
                returnmessage += "Wiped down the screens! "
            effectdel = []
            for cleareffect in FriendlyEffects.keys():
                if (cleareffect in removeeffects):
                    effectdel.append(cleareffect)
            for clearingeffect in effectdel:
                del FriendlyEffects[clearingeffect]
            if (len(effectdel) > 0):
                returnmessage += "Wiped down the screens! "
        
        if (mon.HasAbility("Frisk")):
            for othermon in GetBattlers(mon, True):
                if (othermon.GetItem() != "" and othermon.GetItem() != None):
                    returnmessage += "{} frisked the foe {} and found one {}! ".format(mon.GetNickname(), othermon.GetNickname(), othermon.GetItem())

        if (mon.HasAbility("Anticipation")):
            for othermon in GetBattlers(mon, True):
                for move in othermon.GetMoves():
                    typebonus = 1.0
                    for type in mon.GetTypes():                
                        typebonus *= GetEffectiveness(move.Type, type)
                        if (typebonus > 1 and "shuddered" not in returnmessage):
                            returnmessage += "{} shuddered!".format(mon.GetNickname())
        
        if (mon.HasAbility("Forewarn")):
            maxpower = 0
            movelist = []
            for othermon in GetBattlers(mon, True):
                for move in othermon.GetMoves():
                    movepower = GetMovePower(move)
                    if (movepower > maxpower):
                        maxpower = movepower
                        movelist = [move.Name]
                    elif (movepower == maxpower):
                        movelist.append(move.Name)
            chosenmove = random.choice(movelist)
            returnmessage += "{} was forewarned of {}!".format(mon.GetNickname(), chosenmove)

        if (mon.HasAbility("Sand Stream")):
            returnmessage += ApplyWeather("sandstorm", 5)
        elif (mon.HasAbility("Drizzle")):
            returnmessage += ApplyWeather("rainy", 5)
        elif (mon.HasAbility("Drought")):
            returnmessage += ApplyWeather("sunny", 5)
        elif (mon.HasAbility("Snow Warning")):
            returnmessage += ApplyWeather("hail", 5)

        return returnmessage

