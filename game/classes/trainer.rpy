init python:
    def MakeRed(number=1):
        trainer1 = Trainer("red", TrainerType.Player, playerparty, number=number)
        for mon in playerparty:
            mon.Owner = trainer1
        return trainer1

    class Trainer:
        def __init__(self, name, trainertype, team, number=1, isPokemon=False):
            self.Name = name#string
            self.Team = team#[Pokemon]
            self.Type = trainertype#TrainerType macro
            self.Number = number#1 for single battle, 2 for double, 3 for triple
            self.IsPokemon = isPokemon

        def GetIsPokemon(self):
            return self.IsPokemon

        def GetName(self):
            return self.Name

        def ReorderTeam(self):
            fainteds = []
            for mon in self.GetTeam():
                if (mon.GetHealthPercentage() <= 0):
                    fainteds.append(mon)
            self.Team = self.GetUnfaintedTeam() + fainteds

        def GetLead(self, addNones=True):
            leads = self.Team[:self.Number]
            if (addNones):
                for i in range(len(leads)):
                    if (leads[i].GetHealth() <= 0):
                        leads[i] = None
            else:
                removelist = []
                for mon in leads:
                    if (mon.GetHealth() <= 0):
                        removelist.append(mon)
                for mon in removelist:
                    leads.remove(mon)
            return leads

        def GetTeam(self):
            return self.Team

        def GetUnfaintedTeam(self):
            unfainteds = []
            for mon in self.GetTeam():
                if (mon.GetHealth() > 0):
                    unfainteds.append(mon)
            return unfainteds

        def GetType(self):
            return self.Type

        def ShiftTeam(self, swapto, swapfrom, force=False, positionswitch = False):
            swappingtomon = self.GetTeam()[swapto]
            swappingmon = self.GetTeam()[swapfrom]
            
            if (not positionswitch):
                if (swappingmon.GetHealth() <= 0):
                    renpy.say(None, "{} is fainted, and can't switch in!".format(swappingmon.GetNickname()))
                    return False
                elif (not CanSwitch(swappingmon, force)):
                    renpy.say(None, "Can't switch in!")
                    return False

                if (swappingtomon.GetHealthPercentage() > 0 and swappingtomon.HasAbility("Regenerator")):
                    swappingtomon.AdjustHealth(swappingtomon.GetStat(Stats.Health) * 0.33)
                    
                swappingtomon.ClearStatus(None, volatiles=True)

            self.GetTeam()[swapto], self.GetTeam()[swapfrom] = self.GetTeam()[swapfrom], self.GetTeam()[swapto]
            return True

        def HasMons(self):
            for mon in self.GetTeam():
                if (mon.GetHealth() != 0):
                    return True
            return False

        def GetNumber(self):
            return self.Number