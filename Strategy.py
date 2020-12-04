from __future__ import annotations
from abc import ABC, abstractmethod
import random
import PlayerFactory
from Players import Center, Goalie, RightWinger, LeftWinger, Defenseman, Teams
#from Simulate_Season import order

'''
STRATEGY PATTERN
'''

def getPlayer(pos, team):
    for i in range(len(team)):
        if team[i].position == pos:
            return team[i]

class Game():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def play(self, team1, team2):
        results = self._strategy.do_algorithm(team1, team2)
        return results

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, team1, team2):
        pass


class StrategyA(Strategy):                  # Based on scoring power
    def do_algorithm(self, team1, team2):
        team1score = 0
        team2score = 0
        center1 = getPlayer("C", team1.playersOnTeam)
        leftwinger1 = getPlayer("LW", team1.playersOnTeam)
        rightwinger1 = getPlayer("RW", team1.playersOnTeam)
        defensemanA1 = getPlayer("D", team1.playersOnTeam)
        temp = team1.playersOnTeam.copy()
        team1.playersOnTeam.remove(defensemanA1)
        defensemanB1 = getPlayer("D", team1.playersOnTeam)
        team1.playersOnTeam = temp.copy()
        goalie1 = getPlayer("G", team1.playersOnTeam)
        center2 = getPlayer("C", team2.playersOnTeam)
        leftwinger2 = getPlayer("LW", team2.playersOnTeam)
        rightwinger2 = getPlayer("RW", team2.playersOnTeam)
        defensemanA2 = getPlayer("D", team2.playersOnTeam)
        temp = team2.playersOnTeam.copy()
        team2.playersOnTeam.remove(defensemanA2)
        defensemanB2 = getPlayer("D", team2.playersOnTeam)
        team2.playersOnTeam = temp.copy()
        goalie2 = getPlayer("G", team2.playersOnTeam)

        team1score = team1score + center1.last_points/center1.last_gamesPlayed
        team1score = team1score + leftwinger1.last_points/leftwinger1.last_gamesPlayed
        team1score = team1score + rightwinger1.last_points/rightwinger1.last_gamesPlayed
        team1score = team1score + defensemanA1.last_points/defensemanA1.last_gamesPlayed
        team1score = team1score + defensemanB1.last_points/defensemanB1.last_gamesPlayed
        team1score = team1score + (goalie1.last_winPercent * 2)
        team1score = team1score * 100
        if team1score < 440:
            goalProb1 = 10
        elif team1score < 460:
            goalProb1 = 20
        elif team1score < 480:
            goalProb1 = 30
        elif team1score < 500:
            goalProb1 = 40
        else:
            goalProb1 = 50

        team2score = team2score + center2.last_points/center2.last_gamesPlayed
        team2score = team2score + leftwinger2.last_points/leftwinger2.last_gamesPlayed
        team2score = team2score + rightwinger2.last_points/rightwinger2.last_gamesPlayed
        team2score = team2score + defensemanA2.last_points/defensemanA2.last_gamesPlayed
        team2score = team2score + defensemanB2.last_points/defensemanB2.last_gamesPlayed
        team2score = team2score + (goalie2.last_winPercent * 2)
        team2score = team2score * 100
        if team2score < 440:
            goalProb2 = 10
        elif team2score < 460:
            goalProb2 = 20
        elif team2score < 480:
            goalProb2 = 30
        elif team2score < 500:
            goalProb2 = 40
        else:
            goalProb2 = 50

        team1goals = 0
        team2goals = 0
        team1shots = 0
        team2shots = 0
        for i in range(4):
            if team1goals == 0:
                goalProb1temp = goalProb1 + 40
            else:
                goalProb1temp = goalProb1
            if team2goals == 0:
                goalProb2temp = goalProb2 + 40
            else:
                goalProb2temp = goalProb2
            if random.randint(1, 100) < goalProb1temp:
                team1goals = team1goals + 1
            if random.randint(1, 100) < goalProb2temp:
                team2goals = team2goals + 1

        if team1goals == team2goals:
            if team1score > team2score:
                team1goals = team1goals + 1
            else:
                team2goals = team2goals + 1

        if team1goals < 2:
            team1shots = random.randint(13, 28)
        elif team1goals < 4:
            team1shots = random.randint(21, 36)
        else:
            team1shots = random.randint(30, 47)

        if team2goals < 2:
            team2shots = random.randint(13, 28)
        elif team2goals < 4:
            team2shots = random.randint(21, 36)
        else:
            team2shots = random.randint(30, 47)

        return [team1goals, team2goals, team1shots, team2shots]


class StrategyB(Strategy):                  # Defense
    def do_algorithm(self, team1, team2):
        team1score = 0
        team2score = 0
        center1 = getPlayer("C", team1.playersOnTeam)
        leftwinger1 = getPlayer("LW", team1.playersOnTeam)
        rightwinger1 = getPlayer("RW", team1.playersOnTeam)
        defensemanA1 = getPlayer("D", team1.playersOnTeam)
        temp = team1.playersOnTeam.copy()
        team1.playersOnTeam.remove(defensemanA1)
        defensemanB1 = getPlayer("D", team1.playersOnTeam)
        team1.playersOnTeam = temp.copy()
        goalie1 = getPlayer("G", team1.playersOnTeam)
        center2 = getPlayer("C", team2.playersOnTeam)
        leftwinger2 = getPlayer("LW", team2.playersOnTeam)
        rightwinger2 = getPlayer("RW", team2.playersOnTeam)
        defensemanA2 = getPlayer("D", team2.playersOnTeam)
        temp = team2.playersOnTeam.copy()
        team2.playersOnTeam.remove(defensemanA2)
        defensemanB2 = getPlayer("D", team2.playersOnTeam)
        team2.playersOnTeam = temp.copy()
        goalie2 = getPlayer("G", team2.playersOnTeam)

        team1score = team1score + (goalie1.last_winPercent * 3)
        team1score = team1score + (10 - goalie1.last_goalsAgainst)
        team1score = team1score + (goalie1.last_savePercent * 3)
        team1score = team1score + goalie1.last_shutOuts
        team1score = team1score + ((defensemanA1.last_assists/defensemanA1.last_gamesPlayed) * 4)
        team1score = team1score + ((defensemanB1.last_assists/defensemanB1.last_gamesPlayed) * 4)
        team1score = team1score * 10

        if team1score < 160:
            goalProb2 = 50
        elif team1score < 175:
            goalProb2 = 40
        elif team1score < 185:
            goalProb2 = 30
        elif team1score < 200:
            goalProb2 = 20
        else:
            goalProb2 = 10

        team2score = team2score + (goalie2.last_winPercent * 3)
        team2score = team2score + (10 - goalie2.last_goalsAgainst)
        team2score = team2score + (goalie2.last_savePercent * 3)
        team2score = team2score + goalie2.last_shutOuts
        team2score = team2score + ((defensemanA2.last_assists/defensemanA2.last_gamesPlayed) * 4)
        team2score = team2score + ((defensemanB2.last_assists/defensemanB2.last_gamesPlayed) * 4)
        team2score = team2score * 10

        if team2score < 160:
            goalProb1 = 50
        elif team2score < 175:
            goalProb1 = 40
        elif team2score < 185:
            goalProb1 = 30
        elif team2score < 200:
            goalProb1 = 20
        else:
            goalProb1 = 10

        team1goals = 0
        team2goals = 0
        team1shots = 0
        team2shots = 0
        for i in range(3):
            if team1goals == 0:
                goalProb1temp = goalProb1 + 40
            else:
                goalProb1temp = goalProb1
            if team2goals == 0:
                goalProb2temp = goalProb2 + 40
            else:
                goalProb2temp = goalProb2
            if random.randint(1, 100) < goalProb1temp:
                team1goals = team1goals + 1
            if random.randint(1, 100) < goalProb2temp:
                team2goals = team2goals + 1

        if team1goals == team2goals:
            if team1score > team2score:
                team1goals = team1goals + 1
            else:
                team2goals = team2goals + 1

        if team1goals < 2:
            team1shots = random.randint(13, 28)
        elif team1goals < 4:
            team1shots = random.randint(21, 36)
        else:
            team1shots = random.randint(30, 47)

        if team2goals < 2:
            team2shots = random.randint(13, 28)
        elif team2goals < 4:
            team2shots = random.randint(21, 36)
        else:
            team2shots = random.randint(30, 47)

        return [team1goals, team2goals, team1shots, team2shots]

class StrategyC(Strategy):                  # Special Teams
    def do_algorithm(self, team1, team2):
        team1score = 0
        team2score = 0
        center1 = getPlayer("C", team1.playersOnTeam)
        leftwinger1 = getPlayer("LW", team1.playersOnTeam)
        rightwinger1 = getPlayer("RW", team1.playersOnTeam)
        defensemanA1 = getPlayer("D", team1.playersOnTeam)
        temp = team1.playersOnTeam.copy()
        team1.playersOnTeam.remove(defensemanA1)
        defensemanB1 = getPlayer("D", team1.playersOnTeam)
        team1.playersOnTeam = temp.copy()
        goalie1 = getPlayer("G", team1.playersOnTeam)
        center2 = getPlayer("C", team2.playersOnTeam)
        leftwinger2 = getPlayer("LW", team2.playersOnTeam)
        rightwinger2 = getPlayer("RW", team2.playersOnTeam)
        defensemanA2 = getPlayer("D", team2.playersOnTeam)
        temp = team2.playersOnTeam.copy()
        team2.playersOnTeam.remove(defensemanA2)
        defensemanB2 = getPlayer("D", team2.playersOnTeam)
        team2.playersOnTeam = temp.copy()
        goalie2 = getPlayer("G", team2.playersOnTeam)

        team1score = team1score + center1.last_PPG
        team1score = team1score + leftwinger1.last_PPG
        team1score = team1score + rightwinger1.last_PPG
        team1score = team1score + defensemanA1.last_PPG
        team1score = team1score + defensemanB1.last_PPG
        team1score = team1score * 10
        if team1score < 190:
            goalProb1 = 10
        elif team1score < 230:
            goalProb1 = 20
        elif team1score < 270:
            goalProb1 = 30
        elif team1score < 310:
            goalProb1 = 40
        else:
            goalProb1 = 50

        team2score = team2score + center2.last_PPG
        team2score = team2score + leftwinger2.last_PPG
        team2score = team2score + rightwinger2.last_PPG
        team2score = team2score + defensemanA2.last_PPG
        team2score = team2score + defensemanB2.last_PPG
        team2score = team2score * 10

        if team2score < 190:
            goalProb2 = 10
        elif team2score < 230:
            goalProb2 = 20
        elif team2score < 270:
            goalProb2 = 30
        elif team2score < 310:
            goalProb2 = 40
        else:
            goalProb2 = 50

        team1goals = 0
        team2goals = 0
        team1shots = 0
        team2shots = 0
        for i in range(4):
            if team1goals == 0:
                goalProb1temp = goalProb1 + 40
            else:
                goalProb1temp = goalProb1
            if team2goals == 0:
                goalProb2temp = goalProb2 + 40
            else:
                goalProb2temp = goalProb2
            if random.randint(1, 100) < goalProb1temp:
                team1goals = team1goals + 1
            if random.randint(1, 100) < goalProb2temp:
                team2goals = team2goals + 1

        if team1goals == team2goals:
            if team1score > team2score:
                team1goals = team1goals + 1
            else:
                team2goals = team2goals + 1

        if team1goals < 2:
            team1shots = random.randint(13, 28)
        elif team1goals < 4:
            team1shots = random.randint(21, 36)
        else:
            team1shots = random.randint(30, 47)

        if team2goals < 2:
            team2shots = random.randint(13, 28)
        elif team2goals < 4:
            team2shots = random.randint(21, 36)
        else:
            team2shots = random.randint(30, 47)

        return [team1goals, team2goals, team1shots, team2shots]


