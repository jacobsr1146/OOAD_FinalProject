import random
import time
import PlayerFactory
from Players import Center, Goalie, RightWinger, LeftWinger, Defenseman, Teams
from Update_Players_List import importFile
from Simulate_Season import simulateSeason
from tkinter import *
from tkinter import ttk

def getPlayer(pos, team, num):
    count = 0
    for i in range(len(team)):
        if team[i].position == pos:
            count = count + 1
            if count == num:
                return team[i]

def sort(lst, stat, key):
    for i in range(len(lst[0])):        # finds index of statistic
        if lst[0][i] == stat:
            index = i

    newList = []
    newList.append(lst[0])
    for i in range(len(lst)):
        if lst[i][index] == key:
            newList.append(lst[i])
    return newList

def order(lst, stat):
    for i in range(len(lst[0])):        # finds index of statistic
        if lst[0][i] == stat:
            index = i

    newList = []
    newList.append(lst[0])
    lst.pop(0)
    while len(lst) != 0:
        high = 0
        for x in range(len(lst)):       # re-orders list based on statistic
            curr = lst[x][index]        # use for List Dictionary
            if curr > high:
                high = curr
                highIndex = x
        newList.append(lst[highIndex])
        lst.pop(highIndex)

    return newList

def checkInput(res, correctList):   # checks if res is inside of list correctList
    check = False                   # Used for checking if user input is acceptable
    while check == False:
        if res in correctList:
            check = True
        else:
            res = input("Unacceptable input. Please try again: ")
    return res

def UserChoosePlayer(needPositions, undraftedPlayers, undraftedGoalies):
    print("********** IT IS YOUR TURN TO PICK **********")
    print("You need to fill one of the following positions:", needPositions)
    time.sleep(2)
    topCenters = order(sort(undraftedPlayers, 'Pos', "C"), 'P')
    topLeftWingers = order(sort(undraftedPlayers, 'Pos', "LW"), 'P')
    topRightWingers = order(sort(undraftedPlayers, 'Pos', "RW"), 'P')
    topDefenseman = order(sort(undraftedPlayers, 'Pos', "D"), 'P')
    topGoalies = order(undraftedGoalies.copy(), 'W')
    if "C" in needPositions:
        print("Top available Centers:")
        length = 6
        if len(needPositions) == 1:
            length = len(topCenters)
        for i in range(length):
            print("     ", topCenters[i])
    time.sleep(1)
    if "LW" in needPositions:
        print("Top available Left Wingers:")
        length = 6
        if len(needPositions) == 1:
            length = len(topLeftWingers)
        for i in range(length):
            print("     ", topLeftWingers[i])
    time.sleep(1)
    if "RW" in needPositions:
        print("Top available Right Wingers:")
        length = 6
        if len(needPositions) == 1:
            length = len(topRightWingers)
        for i in range(length):
            print("     ", topRightWingers[i])
    time.sleep(1)
    if "D" in needPositions:
        print("Top available Defenseman:")
        length = 6
        if len(needPositions) == 1:
            length = len(topDefenseman)
        for i in range(length):
            print("     ", topDefenseman[i])
    time.sleep(1)
    if "G" in needPositions:
        print("Top available Goalies:")
        length = 6
        if len(needPositions) == 1:
            length = len(topGoalies)
        for i in range(length):
            print("     ", topGoalies[i])
    time.sleep(1)

    check = ["c", "lw", "rw", "d", "g"]
    for i in range(len(needPositions)):
        check.append(needPositions[i])
    print("Which position would you like to pick from?")
    print("Options: ", needPositions)
    position = checkInput(input("Input: "), check)
    print(" ")
    print("Which Player would you like to pick? (1-5)")
    if "C" == position or "c" == position:
        print("Top available Centers:")
        print("     ", undraftedPlayers[0])
        length = 6
        if len(needPositions) == 1:
            length = len(topCenters)
        for i in range(1, length):
            print(i, ".    ", topCenters[i])
    elif "LW" == position or "lw" == position:
        print("Top available Left Wingers:")
        print("     ", undraftedPlayers[0])
        length = 6
        if len(needPositions) == 1:
            length = len(topLeftWingers)
        for i in range(1, length):
            print(i, ".    ", topLeftWingers[i])
    elif "RW" == position or "rw" == position:
        print("Top available Right Wingers:")
        print("     ", undraftedPlayers[0])
        length = 6
        if len(needPositions) == 1:
            length = len(topRightWingers)
        for i in range(1, length):
            print(i, ".    ", topRightWingers[i])
    elif "D" == position or "d" == position:
        print("Top available Defenseman:")
        print("     ", undraftedPlayers[0])
        length = 6
        if len(needPositions) == 1:
            length = len(topDefenseman)
        for i in range(1, length):
            print(i, ".    ", topDefenseman[i])
    elif "G" == position or "g" == position:
        print("Top available Goalies:")
        print("     ", undraftedGoalies[0])
        length = 6
        if len(needPositions) == 1:
            length = len(topGoalies)
        for i in range(1, length):
            print(i, ".    ", topGoalies[i])
    check = []
    for i in range(length):
        check.append(str(i))
    index = int(checkInput(input("Input: "), check))
    if "C" == position or "c" == position:
        player = topCenters[index]
        position = "C"
    elif "LW" == position or "lw" == position:
        player = topLeftWingers[index]
        position = "LW"
    elif "RW" == position or "rw" == position:
        player = topRightWingers[index]
        position = "RW"
    elif "D" == position or "d" == position:
        player = topDefenseman[index]
        position = "D"
    elif "G" == position or "g" == position:
        player = topGoalies[index]
        position = "G"


    return player, position

def playGame():
    undraftedPlayers, undraftedGoalies = importFile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")

    for i in range(len(undraftedPlayers)):
        undraftedPlayers[i] = undraftedPlayers[i][0:12]     # first 12 stats
    for i in range(len(undraftedGoalies)):
        undraftedGoalies[i] = undraftedGoalies[i][0:12]     # first 12 stats

    teamsList = ["Anaheim Ducks", "Arizona Coyotes", "Boston Bruins", "Buffalo Sabres", "Calgary Flames",
                 "Carolina Hurricanes", "Chicago Blackhawks", "Colorado Avalanche", "Columbus Blue Jackets",
                 "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers", "Florida Panthers", "Los Angeles Kings",
                 "Minnesota Wild", "Montreal Canadiens", "Nashville Predators", "New Jersey Devils", "New York Islanders",
                 "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Pittsburgh Penguins", "San Jose Sharks",
                 "Seattle Kraken", "St Louis Blues", "Tampa Bay Lightning", "Toronto Maple Leafs", "Vancouver Canucks",
                 "Vegas Golden Knights", "Washington Capitals", "Winnipeg Jets"]

    print("NHL be a GM simulator")      # basic instructions (not complete)
    time.sleep(.3)
    print("Overview:")
    print("In this simulator you will be put into a snake draft with 32 other cpu teams to select a total of 6 players each.")
    time.sleep(.1)
    print("-1 Center")
    time.sleep(.1)
    print("-1 Left Wing")
    time.sleep(.1)
    print("-1 Right Wing")
    time.sleep(.1)
    print("-2 Defenseman")
    time.sleep(.1)
    print("-1 Goalie")
    time.sleep(.1)
    print("You may fill these positions in any order you like.")
    print("You will draft your team with a certain salary cap in mind, as each player you draft will cost a certain amount.")
    time.sleep(.1)
    print("Keep in mind once you draft a player there is no turning back.")
    print("Once the draft is over the season will begin simulating each game one by one until the season is over.")
    time.sleep(.1)
    print("Once the season has finished you will be able to evaluate how your team preformed.")
    time.sleep(5)
    print("Are you ready to begin? (y)")
    input("(Press any key to continue)")
    print("*************** Pick your Team ***************")     # pick team name
    print("Input a number 1-32 or the letter 'r' for random")
    i = 0
    while i < len(teamsList):                                                                          # prints list of teams
        print(i+1, ". ", teamsList[i], "     ", i+2, ". ", teamsList[i+1], "     ", i+3, ". ",
              teamsList[i+2], "     ", i+4, ". ", teamsList[i+3], "     ",)
        i = i+4
    check = []
    for i in range(1, 33):
        check.append(str(i))
    userTeam = int(checkInput(input("Input: "), check)) - 1                     # index of teamsList that user picked
    # teamsList[userTeam] = team name
    # *********** User Chooses DRAFT PICK ***********
    print("*************** Pick you starting draft spot ***************")       # pick draft spot
    print("input a number 1-32 or the letter 'r' for random")
    draftNum = input("Input: ")
    check = []
    for i in range(1, 33):
        check.append(str(i))
    check.append('r')
    draftNum = checkInput(draftNum, check)                  # draft pick user picked

    satisfied = False
    if draftNum == 'r':
        while satisfied == False:
            draftNum = random.randint(1, 32)                # random draft pick
            print("Random Position: ", draftNum)
            res = input("Is this position ok? (y/n): ")
            res = checkInput(res, ['y', 'Y', 'n', 'N'])
            if res in ['y', 'Y']:
                satisfied = True
    else:
        draftNum = int(draftNum)

    # *********** DRAFT ***********
    print("Draft Number = ", draftNum)              # prints user's choices
    print("Draft team = ", teamsList[userTeam])

    randTeam = [userTeam]                   # randomizes draft order except for user's choice
    draftOrder = []
    while len(draftOrder) < 32:
        if len(draftOrder)+1 == draftNum:
            draftOrder.append(teamsList[userTeam])
            randTeam.append(userTeam)
        else:
            while True:
                rando = random.randrange(0, 32)
                if rando not in randTeam:
                    break
            draftOrder.append(teamsList[rando])
            randTeam.append(rando)

    print("*************** Draft Order ***************", flush=True)
    print(draftOrder, flush=True)
    time.sleep(1)

    print("*************** Draft Begins ***************", flush=True)
    time.sleep(.1)
    poslst = ['C', 'LW', 'RW', 'D', 'D', 'G']
    pos = []
    while len(pos) < 32:        # creates a list for each team of what positions they need
        pos.append(poslst)

    teamRosters = []                  # creates empty teamRosters lists
    while len(teamRosters) < 32:
        teamRosters.append([])
    draft = []
    for i in range(6):      # creates entire snake draft
        if i % 2 == 0:
            for j in range(len(draftOrder)):
                draft.append(draftOrder[j])
        else:
            for j in range(len(draftOrder)):
                draft.append(draftOrder[::-1][j])

    for i in range(len(draft)):   # loops through the entire draft order and simulates draft
        print("***********************************************", flush=True)
        print("Team:", draft[i], flush=True)

        if draft[i] == teamsList[userTeam]:       # if current team drafting is Users team
            for k in range(len(teamsList)):    # finds index of current team drafting
                if teamsList[k] == draft[i]:
                    j = k

            player, position = UserChoosePlayer(pos[j], undraftedPlayers, undraftedGoalies) # Player chooses function

            temp = []
            found = False
            for k in range(len(pos[j])):    # removes position that was selected from undrafted positions list pos[]
                if pos[j][k] != position or found is True:
                    temp.append(pos[j][k])
                if pos[j][k] == position:
                    found = True
            pos[j] = temp
            player.append((len(teamRosters[j])+1, (i + 1) - (32 * (len(teamRosters[j])))))
            print("Player Selected:", position, player[0])
            teamRosters[j].append(player)     # adds player to team's players list
            if position == "G":
                undraftedGoalies.remove(player)  # removes player from undrafted list
            else:
                undraftedPlayers.remove(player)  # removes player from undrafted list

        else:
            for k in range(len(teamsList)):    # finds index of current team drafting
                if teamsList[k] == draft[i]:
                    j = k
            position = random.choice(pos[j])    # chooses random position out of undrafted positions for that team
            temp = []
            found = False
            for k in range(len(pos[j])):    # removes position that was selected from undrafted positions list pos[]
                if pos[j][k] != position or found is True:
                    temp.append(pos[j][k])
                if pos[j][k] == position:
                    found = True
            pos[j] = temp
            if position == 'G':             # case for goalie
                player = order(undraftedGoalies.copy(), 'W')[1]
                player.append((len(teamRosters[j])+1, (i + 1) - (32 * (len(teamRosters[j])))))
                print("Player Selected:", position, player[0], flush=True)
                teamRosters[j].append(player)     # adds player to team's players list
                undraftedGoalies.remove(player)  # removes player from undrafted list

            else:                           # case for any other player position
                player = order(sort(undraftedPlayers, 'Pos', position), 'P')[1]
                player.append((len(teamRosters[j])+1, (i + 1) - (32 * (len(teamRosters[j])))))
                print("Player Selected:", position, player[0], flush=True)
                teamRosters[j].append(player)     # adds player to team's players list
                undraftedPlayers.remove(player)  # removes player from undrafted list
            time.sleep(.25)
    print(" ")
    print("********** Draft Results **********")
    print(teamsList[userTeam], ": ", flush=True)
    time.sleep(1)
    for y in range(len(teamRosters[userTeam])):
        time.sleep(.1)
        print("    ", teamRosters[userTeam][y][4], teamRosters[userTeam][y][0], flush=True)

    print("Would you like to see the Draft results for the rest of the league? (y/n)")
    res = checkInput(input("Input: "), ["Y", "y", "N", "n"])
    if res in ["Y", "y"]:
        time.sleep(.5)
        for x in range(len(teamRosters)):         # prints each teams' full roster (just names)
            print(teamsList[x], ": ", flush=True)
            time.sleep(.5)
            for y in range(len(teamRosters[x])):
                time.sleep(.1)
                print("    ", teamRosters[x][y][4], teamRosters[x][y][0], flush=True)

    factory = PlayerFactory.createPlayerFactory         # Create factory
    teamObjectList = []
    for i in range(len(teamRosters)-1):
        teamsRosterList = []                            # list of players begin added to teamsList[i]
        for j in range(len(teamRosters[i])):
            if teamRosters[i][j][4] == 'C':
                newCenter = factory.createPlayer(teamRosters[i][j])
                teamsRosterList.append(newCenter)
            if teamRosters[i][j][4] == 'LW':
                newLeftWinger = factory.createPlayer(teamRosters[i][j])
                teamsRosterList.append(newLeftWinger)
            if teamRosters[i][j][4] == 'RW':
                newRightWinger = factory.createPlayer(teamRosters[i][j])
                teamsRosterList.append(newRightWinger)
            if teamRosters[i][j][4] == 'D':
                newDefenseman = factory.createPlayer(teamRosters[i][j])
                teamsRosterList.append(newDefenseman)
            if teamRosters[i][j][4] == 'G':
                newGoalie = factory.createPlayer(teamRosters[i][j])
                teamsRosterList.append(newGoalie)
        teamObj = Teams(teamsList[i], teamsRosterList)       # Creating team object with team's name and list of players
        for j in range(len(teamObj.playersOnTeam)):
            teamObj.playersOnTeam[j].currentTeam = teamsList[i]     # Updating each player's currentTeam
        teamObjectList.append(teamObj)                         # adding team object to a list of all of the team objects

    print("Would you like to see the results of each of your team's games? (y/n)")
    res = checkInput(input("Input: "), ["Y", "y", "N", "n"])

    simulateSeason(teamObjectList, teamsList[userTeam], res)

    print("**************** End of Season Results ****************")
    teamObjectList[userTeam].printTeamPlayers()

    print("Would you like to see the season results of each team in the league? (y/n)")
    res = checkInput(input("Input: "), ["Y", "y", "N", "n"])
    if res in ["Y", "y"]:
        for i in range(len(teamObjectList)):        #printing end of season statistics
            teamObjectList[i].printTeamPlayers()
            time.sleep(.25)
            print("*************************************")
    print("Would you like to see a list of every team's record? (y/n)")
    res = checkInput(input("Input: "), ["Y", "y", "N", "n"])
    if res in ["Y", "y"]:
        winsList = []
        curr_high = 0
        while len(winsList) < 10:
            high = 0
            for i in range(len(teamObjectList)):
                if teamObjectList[i].wins > high and teamObjectList[i] not in winsList:
                    curr_high = teamObjectList[i]
                    high = teamObjectList[i].wins
            winsList.append(curr_high)
        print("Rank:  Team:      Record:")
        for i in range(len(winsList)):
            print(i+1, winsList[i].teamName, ": ", winsList[i].wins, "-", winsList[i].loses)

    print("Would you like to see a list of the top 10 points leaders in the league? (y/n)")
    res = checkInput(input("Input: "), ["Y", "y", "N", "n"])
    if res in ["Y", "y"]:
        pointsList = []
        curr_high = 0
        while len(pointsList) < 10:
            high = 0
            for i in range(len(teamObjectList)):
                for j in range(len(teamObjectList[i].playersOnTeam)):
                    if teamObjectList[i].playersOnTeam[j].position != "G":
                        if teamObjectList[i].playersOnTeam[j].curr_points > high and teamObjectList[i].playersOnTeam[j] not in pointsList:
                            curr_high = teamObjectList[i].playersOnTeam[j]
                            high = teamObjectList[i].playersOnTeam[j].curr_points
            pointsList.append(curr_high)
        print("Rank:  Name:      Points:    Team:")
        for i in range(len(pointsList)):
            print(i+1, pointsList[i].name, ": ", pointsList[i].curr_points, "  ", pointsList[i].currentTeam)



    '''
    teamsList = list of each team's name in alphabetical order
    teamRosters = list of each teamm's roster
        ex: teamsList[0] = "Anahiem Ducks" 
            teamRosters[0] = [[Ducks player1 name, former team, salary, age, position,....other statistics],
                        [Ducks player2 name, former team, salary, age, position,....other statistics],
                        [Ducks player3 name, former team, salary, age, position,....other statistics],
                        [Ducks player4 name, former team, salary, age, position,....other statistics],
                        [Ducks player5 name, former team, salary, age, position,....other statistics],
                        [Ducks player6 name, former team, salary, age, position,....other statistics],
    
    For now just read in the following stats until I figure out which other stats I want to use:
    ['Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-']
    Those are just the first 11 stats of the list. Therefor: teamRosters[0][0] = 'Name'
                                                                ...
                                                             teamRosters[0][10] = '+/-'
    '''

def exitGame():
    print("exiting game")
    exit()

root = Tk()
root.title("Be a GM")
root.geometry('450x400')
frame = ttk.Frame(root, width=300, height=300).grid(column=0, row=0)
image = PhotoImage(file='BeGMimg.png')
label = ttk.Label(frame, text='start img')
label['image'] = image
label.grid(column=0, row=0, columnspan=2)
startGame = ttk.Button(frame, text="Start Game", command=playGame).grid(column=0, row=1, padx=10, pady=10)
exitGame = ttk.Button(frame, text="ExitGame", command=exitGame).grid(column=1, row=1, padx=10)

root.mainloop()

