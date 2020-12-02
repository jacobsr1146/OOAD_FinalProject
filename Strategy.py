from __future__ import annotations
from abc import ABC, abstractmethod
import random
import PlayerFactory
from Players import Center, Goalie, RightWinger, LeftWinger, Defenseman, Teams
#from Simulate_Season import order

def getPlayer(pos, team):
    for i in range(len(team)):
        if team[i].position == pos:
            return team[i]

class Game():
    """
    The Game defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Game accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Game maintains a reference to one of the Strategy objects. The
        Game does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Game allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def play(self, team1, team2):
        results = self._strategy.do_algorithm(team1, team2)
        return results

class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Game uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, team1, team2):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Game.
"""


class StrategyA(Strategy):                  #Based on scoring power
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
            goalProb1 = 20
        elif team1score < 460:
            goalProb1 = 30
        elif team1score < 480:
            goalProb1 = 40
        elif team1score < 500:
            goalProb1 = 60
        else:
            goalProb1 = 75

        team2score = team2score + center2.last_points/center2.last_gamesPlayed
        team2score = team2score + leftwinger2.last_points/leftwinger2.last_gamesPlayed
        team2score = team2score + rightwinger2.last_points/rightwinger2.last_gamesPlayed
        team2score = team2score + defensemanA2.last_points/defensemanA2.last_gamesPlayed
        team2score = team2score + defensemanB2.last_points/defensemanB2.last_gamesPlayed
        team2score = team2score + (goalie2.last_winPercent * 2)
        team2score = team2score * 100
        if team2score < 440:
            goalProb2 = 20
        elif team2score < 460:
            goalProb2 = 30
        elif team2score < 480:
            goalProb2 = 40
        elif team2score < 500:
            goalProb2 = 50
        else:
            goalProb2 = 60

        team1goals = 0
        team2goals = 0
        team1shots = 0
        team2shots = 0
        for i in range(6):
            if random.randint(1, 100) < goalProb1:
                team1goals = team1goals + 1
            if random.randint(1, 100) < goalProb2:
                team2goals = team2goals + 1

        if team1goals == team2goals:
            if team1score > team2score:
                team2goals = team2goals - 1
            else:
                team1goals = team1goals - 1

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


class StrategyB(Strategy):                  #Based on physical power...?
    def do_algorithm(self, team1, team2):
        print("Strategy 2:")
        return team2, team1

class StrategyC(Strategy):                  #Based on chemistry...?
    def do_algorithm(self, team1, team2):
        print("Strategy 2:")
        return team2, team1


def testing():
    from Update_Players_List import importFile
    undraftedPlayers, undraftedGoalies = importFile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")
    factory = PlayerFactory.createPlayerFactory
    team1 = Teams("Dallas Stars")
    team2 = Teams("Colorado Avalanche")

    newPlayer = factory.createPlayer(undraftedPlayers[1])
    team1.playersOnTeam.append(newPlayer)
    '''
    newPlayer = factory.createPlayer(undraftedPlayers[2])
    team2.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[7])
    team1.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[3])
    team2.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[4])
    team1.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[6])
    team2.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[131])
    team1.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[130])
    team2.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[132])
    team1.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedPlayers[133])
    team2.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedGoalies[2])
    team1.playersOnTeam.append(newPlayer)
    newPlayer = factory.createPlayer(undraftedGoalies[1])
    team2.playersOnTeam.append(newPlayer)
    '''

    print("Team 1: ", team1.teamName)
    for i in range(len(team1.playersOnTeam)-1):
        print("     ", team1.playersOnTeam[i].name)
    print("Team 2: ", team2.teamName)
    for i in range(len(team2.playersOnTeam)-1):
        print("     ", team2.playersOnTeam[i].name)

    # The client code picks a concrete strategy and passes it to the Game.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.
    '''
    team1 = "Stars"
    team2 = "Ducks"
    Game = Game(StrategyA())
    print("Client: Strategy is set to normal sorting.")
    Game.play(team1, team2)
    print()

    print("Client: Strategy is set to reverse sorting.")
    Game.strategy = StrategyB()
    Game.play(team1, team2)
    '''

    #*********************** IMPORTANT *****************************
    # *********** Updating Points ***********
    teams = [team1, team2]
    teamgoals = [team1goals, team2goals]
    for x in range(len(teams)-1):
        teamplayers = []
        for i in range(len(teams[x].playersOnTeam)-1):
            if teams[x].playersOnTeam[i][4] != "G":
                teamplayers.append(teams[x].playersOnTeam[i])

        # Goals and assist:
        for i in range(teamgoals[x]-1):
            goalScorer = random.choices(order(teamplayers, "Goals"), weights=(50, 40, 30, 20, 10))[0]      # choosing goal scorers
            for j in range(len(teams[x].playersOnTeam)-1):
                if teams[x].playersOnTeam[j] == goalScorer:
                    teams[x].playersOnTeam[j].curr_goals = teams[x].playersOnTeam[j].curr_goals + 1   # updating goal scorer's curr_goals
            assist = random.choices(order(teamplayers, "Assist"), weights=(50, 40, 30, 20, 10), k=2)   # finding assist for each goal
            if goalScorer in assist:
                assist.remove(goalScorer)
            if assist[0] == assist[1]:
                assist.pop()
            for k in range(len(assist)-1):
                for j in range(len(teams[x].playersOnTeam)-1):
                    if teams[x].playersOnTeam[j] == assist[k]:
                        teams[x].playersOnTeam[j].curr_assist = teams[x].playersOnTeam[j].curr_assist + 1     # updating assisters curr_assist
        # +/-:
        if x == 0:
            for i in range(len(teams[x].playersOnTeam)-1):
                teams[x].playersOnTeam[i].curr_plusMinus = teams[x].playersOnTeam[i].curr_plusMinus + teamgoals[x] - teamgoals[x+1]
        if x == 1:
            for i in range(len(teams[x].playersOnTeam)-1):
                teams[x].playersOnTeam[i].curr_plusMinus = teams[x].playersOnTeam[i].curr_plusMinus + teamgoals[x] - teamgoals[x-1]
        # games played:
        for i in range(len(teams[x].playersOnTeam)-1):
            teams[x].playersOnTeam[i].curr_gamesPlayed = teams[x].playersOnTeam[i].curr_gamesPlayed + 1




#testing()
