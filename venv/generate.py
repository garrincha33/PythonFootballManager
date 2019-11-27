import os
import random


class Manager:
    # TODO add manager stats ect
    def __init__(self, name):
        self.team = my_team
        self.name = name
        self.league = League()

    # ###########################functions
    def get_name(self):
        return self.name

    def get_league(self):
        return self.league

    def set_team(self, my_team):
        pass

    def get_team(self):
        return self.team
    # ###########################


class League:
    def __init__(self):
        self.team_list = []
        lines = [line.rstrip('\n') for line in open('db/teams.txt')]
        random.shuffle(lines)
        # makes list of teams from my text file

        for n in range(10):
            if n < 2:
                prestige = 0
            elif n < 5:
                prestige = 1
            elif n < 8:
                prestige = 2
            elif n < 10:
                prestige = 3
            self.team_list.append(Team(lines.pop()), prestige)
            random.shuffle(self.team_list)

        self.games_played = 0

    # ###########################functions
    def game_played(self):
        if self.games_played < 40
            self.games_played += 1
        else:
            #TODO end season logic
            self.games_played = 0

class Team():
    def __init__(self, name, prestige):
        self.name = name
        self.prestige = prestige

        if self.prestige == 0:
            wealth = random.randint(1000000, 2500000)
        elif self.prestige == 1:
            wealth = random.randint(2500001, 5000000)
        elif self.prestige == 2:
            wealth = random.randint(5000001, 10000000)
        elif self.prestige == 3:
            wealth = random.randint(10000001, 20000000)
        se;f.wealth = wealth
        self.stadium = self.name + 'Stadium'

        gen_players()

    def gen_players(self):
        self.player_list = []
        lines = [line.rstrip('n')for line in open('../db/players.txt')]
        random.shuffle(lines)
        # TODO finish players generate



