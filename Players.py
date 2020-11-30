# Make the Players "abstract"
# Then make the classes for each of the positions
import collections
import sys
import PlayerFactory


class Teams:
    playersOnTeam = []
    lastSeasonPlayers = []  # Keep stats of last season, only populates when newSeasonPlayerStats is called

    def __init__(self, teamName):
        self.teamName = teamName

    # make a function that takes a team and then sets all the stats to 0 besides name and former team
    def newSeasonPlayerStats(self):
        for player in self.playersOnTeam:
            self.lastSeasonPlayers.append(player)  # Populate the lastSeasonPlayers list 
            Players.makeStatsZero(player)  # set new stats, for now set to 0

    # Print all players on any team and show stats
    def printTeamPlayers(self):
        print(self.teamName + " :\n\nPlayers:\n")
        for player in self.playersOnTeam:
            print(player.displayData())


# Stats for players need to be
# 'Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-'
class Players:
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim, plusMinus):
        self.points = points
        self.name = name
        self.goals = goals
        self.assists = assists
        self.plusMinus = plusMinus
        self.formerTeam = formerTeam
        self.salary = salary
        self.age = age
        self.position = position
        self.gamesPlayed = gamesPlayed
        self.pim = pim

    def displayData(self):
        print("Position: " + self.__class__.__name__ + ", Name: " + str(self.name) + ", Points: " + str(
            self.points) + ", Goals: " + str(self.goals) + ", Assists: " + str(self.assists) + ", Plus/Minus: " + str(
            self.plusMinus) + " Former Team: " + str(self.formerTeam))

    def makeStatsZero(self):
        # This Function will be how to set the new season stats, for now set player stats to 0
        # To change it so that new stats can be entered we will need to change the paramaters 
        self.points = 0
        self.goals = 0
        self.assists = 0
        self.plusMinus = 0
        self.salary = 0
        self.gamesPlayed = 0
        self.pim = 0


class Center(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim, plusMinus):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim,
                         plusMinus)


class LeftWinger(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim, plusMinus):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim,
                         plusMinus)


class RightWinger(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim, plusMinus):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim,
                         plusMinus)


class Defenseman(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim, plusMinus):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim,
                         plusMinus)


# need to add the variables stored in goalie, such as save percent and GAA
# As of right now goalies have the same stats as normal players, will be changed in the second sprint
class Goalie(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim, plusMinus):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim,
                         plusMinus)


def main():
      #'Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-'
#     # playerData = ["Solis", "Knights", 1200, 23, "Center", 5, 4, 3, 7, 6, .8]
#     # leftWing = ["Solis", "Knights", 1200, 23, "LeftWinger", 5, 4, 3, 7, 6, .8]
#     # 
#     # factory = PlayerFactory.createPlayerFactory
#     # newCenter = factory.createPlayer(playerData)
#     # newCenter.displayData()
#     # newLW = factory.createPlayer(playerData)
#     # 
#     # Anahiem = Teams("Anahiem")
#     # Anahiem.playersOnTeam.append(newCenter)
#     # Anahiem.playersOnTeam.append(newLW)
#     # Anahiem.newSeasonPlayerStats()
#     # Anahiem.playersOnTeam[0].displayData()
#     # Anahiem.playersOnTeam[1].displayData()


if __name__ == "__main__":
    main()
