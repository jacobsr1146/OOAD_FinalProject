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
    @staticmethod
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, pim, plusMinus):
        self.name = name
        self.position = position
        self.age = age
        self.formerTeam = formerTeam
        self.salary = salary

        self.last_points = points
        self.last_goals = goals
        self.last_assists = assists
        self.last_plusMinus = plusMinus
        self.last_gamesPlayed = gamesPlayed
        self.last_pim = pim

        self.currentTeam = formerTeam
        self.curr_points = 0
        self.curr_goals = 0
        self.curr_assists = 0
        self.curr_plusMinus = 0
        self.curr_gamesPlayed = 0
        self.curr_pim = 0

    def displayLastData(self):
        print("Position: " + self.__class__.__name__ + ", Name: " + str(self.name) + ", Points: " + str(
            self.last_points) + ", Goals: " + str(self.last_goals) + ", Assists: " + str(self.last_assists) + ", Plus/Minus: " + str(
            self.last_plusMinus) + " Former Team: "+ str(self.formerTeam) )

    def displayCurrData(self):
        print("Position: " + self.__class__.__name__ + ", Name: " + str(self.name) + ", Points: " + str(
            self.curr_points) + ", Goals: " + str(self.curr_goals) + ", Assists: " + str(self.curr_assists) + ", Plus/Minus: " + str(
            self.curr_plusMinus) + " Current Team: "+ str(self.formerTeam) )

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
    # 'Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-'
    playerData = ["Solis", "Knights", 1200, 23, "Center", 5, 4, 3, 7, 6, .8]

    factory = PlayerFactory.createPlayerFactory
    newCenter = factory.createPlayer(playerData)
    newCenter.displayData()

    Anahiem = Teams("Anahiem")
    Anahiem.playersOnTeam.append(newCenter)
    thisPlayer = Anahiem.playersOnTeam[0]
    thisPlayer.displayData()


if __name__ == "__main__":
    main()
