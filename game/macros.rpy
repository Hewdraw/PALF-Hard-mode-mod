init -1 python:
    import copy
    import random 
    import math
    import string

    class Stats:
        Health = 0
        Attack = 1
        Defense = 2
        SpecialAttack = 3
        SpecialDefense = 4
        Speed = 5
        Accuracy = 6
        Evasion = 7

    def StatToString(stat):
        if (stat == Stats.Health):
            return "HP"
        elif (stat == Stats.Attack):
            return "Attack"
        elif (stat == Stats.Defense):
            return "Defense"
        elif (stat == Stats.SpecialAttack):
            return "Special Attack"
        elif (stat == Stats.SpecialDefense):
            return "Special Defense"
        elif (stat == Stats.Speed):
            return "Speed"
        elif (stat == Stats.Accuracy):
            return "Accuracy"
        elif (stat == Stats.Evasion):
            return "Evasion"

    class DexMacros:
        Id = 0
        Name = 1
        Health = 2
        Attack = 3
        Defense = 4
        SpecialAttack = 5
        SpecialDefense = 6
        Speed = 7
        Total = 8
        Type1 = 9
        Type2 = 10
        Ability1 = 11
        Ability2 = 12
        HiddenAbility = 13
        Weight = 14
        Exp = 21
        Color = 22
        MaxExp = 28
        Evolve = 29
        Forme = 30
        Height = 31
        Prevo = 35
        Image = 36
        DexPos = 38
    
    class TrainerType:
        Player = 0
        Enemy = 1
        Ally = 2

    class Range:
        Adjacent = 0
        AdjacentFoe = 1
        Any = 2
        AdjacentAllyOrSelf = 3
        AllAdjacentFoes = 4
        AllAdjacent = 5
        AllAllies = 6
        AllFoes = 7
        All = 8
        AdjacentAlly = 9
        Self = 10
        AllAlliesAndSelf = 11
        AnyOrSelf = 12
        AnyAlly = 13

    class Infos:
        Name = 6

    class ActionTypes:
        Move = 0
        Pokemon = 1
        Bag = 2
        Run = 3

    class Types:
        Normal = 0
        Fire = 1
        Water = 2
        Grass = 3
        Electric = 4
        Ice = 5
        Fighting = 6
        Poison = 7
        Ground = 8
        Flying = 9
        Psychic = 10
        Bug = 11
        Rock = 12
        Ghost = 13
        Dark = 14
        Dragon = 15
        Steel = 16
        Fairy = 17

    typeints = {
        0: "Normal",
        1: "Fire",
        2: "Water",
        3: "Grass",
        4: "Electric",
        5: "Ice",
        6: "Fighting",
        7: "Poison",
        8: "Ground",
        9: "Flying",
        10: "Psychic",
        11: "Bug",
        12: "Rock",
        13: "Ghost",
        14: "Dark",
        15: "Dragon",
        16: "Steel",
        17: "Fairy"
    }

    def GetTypeNum(typestring):
        return typenums[typestring]

    def GetEffectiveness(offense, defense):
        return typechart[GetTypeNum(offense)][GetTypeNum(defense)]

    def GetTypeBonus(movename, movetype, target, user):
        typebonus = 1.0
        for type in target.GetTypes():
            temptypebonus = GetEffectiveness(movetype, type)
            if (movetype in ["Fighting", "Normal"] and type == "Ghost" and ((target.HasStatus("foreseen") or target.HasStatus("sniffed out") or user.HasAbility("Scrappy")))
                or movetype == "Ghost" and type == "Normal" and target.HasStatus("foreseen")
                or movetype == "Psychic" and type == "Dark" and target.HasStatus("miraculously seen")
                or movename == "Psywave" and temptypebonus != 0
                or movetype == "Ground" and temptypebonus == 0.0 and IsGrounded(target)):
                temptypebonus = 1.0
            elif (movetype == "Ground" and not IsGrounded(target)):
                temptypebonus = 0.0
            elif (movename == "Freeze-Dry" and type == "Water"):
                temptypebonus = 2.0
            typebonus *= temptypebonus
        return typebonus

    typenums = {
        "Normal": 0,
        "Fire": 1,
        "Water": 2,
        "Electric": 3,
        "Grass": 4,
        "Ice": 5,
        "Fighting": 6,
        "Poison": 7,
        "Ground": 8,
        "Flying": 9,
        "Psychic": 10,
        "Bug": 11,
        "Rock": 12,
        "Ghost": 13,
        "Dragon": 14,
        "Dark": 15,
        "Steel": 16,
        "Fairy": 17,
        "None": 18
    }

    def GetTypeColor(typestring):
        return typecolors[typestring]

    typecolors = {
        "Normal": "#9099A1",
        "Fire": "#FF9C54",
        "Water": "#4D90D5",
        "Electric": "#F3D23B",
        "Grass": "#63BB5B",
        "Ice": "#74CEC0",
        "Fighting": "#CE4069",
        "Poison": "#AB6AC8",
        "Ground": "#D97746",
        "Flying": "#92AADE",
        "Psychic": "#F97176",
        "Bug": "#90C12C",
        "Rock": "#C7B78B",
        "Ghost": "#5269AC",
        "Dragon": "#096DC4",
        "Dark": "#5A5366",
        "Steel": "#5A8EA1",
        "Fairy": "#EC8FE6",
        "None": "#000000"
    }

    class Natures:
        Adamant = 0
        Bashful = 1
        Bold = 2
        Brave = 3
        Calm = 4
        Careful = 5
        Docile = 6
        Gentle = 7
        Hardy = 8
        Hasty = 9
        Impish = 10
        Jolly = 11
        Lax = 12
        Lonely = 13
        Mild = 14
        Modest = 15
        Naive = 16
        Naughty = 17
        Quiet = 18
        Quirky = 19
        Rash = 20
        Relaxed = 21
        Sassy = 22
        Serious = 23
        Timid = 24

    def NatureToString(nature):
        naturestrings = ["Adamant", "Bashful", "Bold", "Brave", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid"]
        return naturestrings[nature]
        
    class Genders:
        Male = 0
        Female = 1
        Unknown = 2

    def NatureToBonus(nature, statindex):
        if (statindex == Stats.Attack and (nature == Natures.Lonely or nature == Natures.Adamant or nature == Natures.Naughty or nature == Natures.Brave) 
        or statindex == Stats.Defense and (nature == Natures.Bold or nature == Natures.Impish or nature == Natures.Lax or nature == Natures.Relaxed) 
        or statindex == Stats.SpecialAttack and (nature == Natures.Modest or nature == Natures.Mild or nature == Natures.Rash or nature == Natures.Quiet) 
        or statindex == Stats.SpecialDefense and (nature == Natures.Calm or nature == Natures.Gentle or nature == Natures.Careful or nature == Natures.Sassy) 
        or statindex == Stats.Speed and (nature == Natures.Timid or nature == Natures.Hasty or nature == Natures.Jolly or nature == Natures.Naive)):
            return 1.1
        
        if (statindex == Stats.Attack and (nature == Natures.Bold or nature == Natures.Modest or nature == Natures.Calm or nature == Natures.Timid) 
        or statindex == Stats.Defense and (nature == Natures.Lonely or nature == Natures.Mild or nature == Natures.Gentle or nature == Natures.Hasty) 
        or statindex == Stats.SpecialAttack and (nature == Natures.Adamant or nature == Natures.Impish or nature == Natures.Careful or nature == Natures.Jolly) 
        or statindex == Stats.SpecialDefense and (nature == Natures.Naughty or nature == Natures.Lax or nature == Natures.Rash or nature == Natures.Naive) 
        or statindex == Stats.Speed and (nature == Natures.Brave or nature == Natures.Relaxed or nature == Natures.Quiet or nature == Natures.Sassy)):
            return 0.9

        return 1

    class TrainerNature:
        Distant = "Distant"
        Moody = "Moody"
        Neutral = "Neutral"
        Friendly = "Friendly"
        Devoted = "Devoted"
        Special = "Special"