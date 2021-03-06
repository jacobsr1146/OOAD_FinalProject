# Make the Players "abstract"
# Then make the classes for each of the positions
import collections
import sys
import PlayerFactory


class Teams:
    def __init__(self, teamName, Lst):
        self.teamName = teamName
        self.playersOnTeam = Lst
        self.lastSeasonPlayers = []  # Keep stats of last season, only populates when newSeasonPlayerStats is called
        self.wins = 0
        self.loses = 0

    # make a function that takes a team and then sets all the stats to 0 besides name and former team
    def newSeasonPlayerStats(self):
        for player in self.playersOnTeam:
            self.lastSeasonPlayers.append(player)  # Populate the lastSeasonPlayers list
            Players.makeStatsZero(player)  # set new stats, for now set to 0

    # Print all players on any team and show stats
    def printTeamPlayers(self):
        print(" ")
        print(self.teamName + " :", self.wins, "-", self.loses)
        for player in self.playersOnTeam:
            player.displayCurrData()

    def printLastTeamPlayers(self):
        print(self.teamName + " :\n\nPlayers:\n")
        for player in self.lastSeasonPlayers:
            player.displayLastData()
            print("\n")

# Stats for players need to be
# 'Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', '+/-', 'PPG', 'GWG'
class Players:
    @staticmethod
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick):   # twefthStat = GWG
        if position == "G":
            # name, former ,salary, age, position, games played, wins, loses, win%, Shutouts, goals agnst, save percent
            self.name = name
            self.position = position
            self.age = age
            self.formerTeam = formerTeam
            self.salary = salary

            self.last_winPercent = points
            self.last_wins = goals
            self.last_loses = assists
            self.last_goalsAgainst = PPG
            self.last_gamesPlayed = gamesPlayed
            self.last_shutOuts = plusMinus
            self.last_savePercent = twefthStat
            self.last_draftPick = draftPick

            self.currentTeam = formerTeam
            self.curr_winPercent = 0
            self.curr_wins = 0
            self.curr_loses = 0
            self.curr_goalsAgainst = 0
            self.curr_gamesPlayed = 0
            self.curr_shutOuts = 0
            self.curr_saves = 0
            self.curr_draftPick = 0

        else:
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
            self.last_PPG = PPG
            self.last_GWG = twefthStat
            self.last_draftPick = draftPick

            self.currentTeam = formerTeam
            self.curr_points = 0
            self.curr_goals = 0
            self.curr_assists = 0
            self.curr_plusMinus = 0
            self.curr_gamesPlayed = 0
            self.curr_PPG = 0
            self.curr_GWG = 0
            self.curr_draftPick = 0

    def displayLastData(self):
        if self.__class__.__name__ == "Goalie":
            self.displayLastGoalieStats()
        else:
            print("Position: " + self.__class__.__name__ + ", Name: " + str(self.name) + ", \nPoints: " + str(
                self.last_points) + ", \nGoals: " + str(self.last_goals) + ", \nAssists: " + str(self.last_assists) + ", \nPlus/Minus: " + str(
                self.last_plusMinus) + " \nFormer Team: "+ str(self.formerTeam) )

    def displayCurrData(self):
        if self.__class__.__name__ == "Goalie":
            self.displayCurrGoalieStats()
        else:
            print("    ", self.name, self.position, ":")
            print("       ", "Points:", self.curr_points)
            print("       ", "Goals:", self.curr_goals)
            print("       ", "Assist:", self.curr_assists)
            print("       ", "Plus/Minus:", self.curr_plusMinus)
            print("       ", "PPG:", self.curr_PPG)
            print("       ", "GWG:", self.curr_GWG)

    def makeStatsZero(self):
        # This Function will be how to set the new season stats, for now set player stats to 0
        # To change it so that new stats can be entered we will need to change the paramaters
        self.points = 0
        self.goals = 0
        self.assists = 0
        self.plusMinus = 0
        self.salary = 0
        self.gamesPlayed = 0
        self.PPG = 0
        self.GWG = 0


class Center(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick)


class LeftWinger(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick)


class RightWinger(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick)


class Defenseman(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick)


# need to add the variables stored in goalie, such as save percent and GAA
# As of right now goalies have the same stats as normal players, will be changed in the second sprint

'''
DECORATOR PATTERN
'''

class Goalie(Players):
    def __init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick):
        Players.__init__(self, name, formerTeam, salary, age, position, gamesPlayed, goals, assists, points, plusMinus, PPG, twefthStat, draftPick)

    def displayCurrGoalieStats(self):
        print("    ", self.name, self.position, ":")
        print("       ", "Wins:", self.curr_wins)
        print("       ", "Loses:", self.curr_loses)
        print("       ", "Games Played:", self.curr_gamesPlayed)
        print("       ", "Win %:", self.curr_winPercent)
        print("       ", "Shutouts:", self.curr_shutOuts)
        print("       ", "GAA:", self.curr_goalsAgainst/self.curr_gamesPlayed)
        print("       ", "Save %:", self.curr_saves/(self.curr_saves+self.curr_goalsAgainst))

    def displayLastGoalieStats(self):
        print("Goalie Stats:::\nName: " + self.name + "\nTeam: " + str(self.formerTeam) + "\nGames Played: " + str(
            self.last_gamesPlayed) + "\nWins: " + str(self.last_wins) +
              "\nLosses: " + str(self.last_loses) + "\nWin Percentage: " + str(
            self.last_winPercent) + "\nShutOuts: " + str(self.last_shutOuts) + "\nGoals Against: " + str(
            self.last_goalsAgainst)
              + "\nSave Percent: " + str(self.last_savePercent)+ "\nDraft Pick: " + str(self.last_draftPick) )

def main():
    # name, former ,salary, age, position, games played, wins, loses, win%, Shutouts, goals agnst, save percent'
    goalie = ["Tormum", "Knights", 1200, 23, "G", 5, 4, 1, .75, 3, 1, .98, 3]
    factory = PlayerFactory.createPlayerFactory
    newGoalie = factory.createPlayer(goalie)
    playerData = ["Solis", "Knights", 1200, 23, "C", 5, 4, 3, 7, 6, .8,12, 1]
    leftWing = ["Solis", "Knights", 1200, 23, "LW", 5, 4, 3, 7, 6, .8,12, 2]
    newCenter = factory.createPlayer(playerData)
    newLW = factory.createPlayer(leftWing)
    newGoalie.displayLastData()
    #Anahiem = Teams("Anahiem")
    #Anahiem.playersOnTeam.append(newCenter)
    #Anahiem.playersOnTeam.append(newLW)
    #Anahiem.playersOnTeam.append(newGoalie)
    #Anahiem.printLastTeamPlayers()



    return 0
#      #Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-'
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
