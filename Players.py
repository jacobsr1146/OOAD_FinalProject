# Make the Players "abstract"
# Then make the classes for each of the positions
import collections
import sys
import PlayerFactory


class Teams:
    playersOnTeam = []

    def __init__(self, teamName):
        self.teamName = teamName


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
            self.plusMinus) + " Former Team: "+ str(self.formerTeam) )


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
    playerData = ["Solis", "Knights",1200, 23, "Center", 5, 4, 3, 7, 6, .8]

    factory = PlayerFactory.createPlayerFactory
    newCenter = factory.createPlayer(playerData)
    newCenter.displayData()

    Anahiem = Teams("Anahiem")
    Anahiem.playersOnTeam.append(newCenter)
    thisPlayer = Anahiem.playersOnTeam[0]
    thisPlayer.displayData()


if __name__ == "__main__":
    main()
