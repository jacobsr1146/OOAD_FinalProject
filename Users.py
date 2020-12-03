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
    print("Overview:")
    print("In this simulator you will be put into a snake draft with 32 other cpu teams to select a total of 6 players each.")
    print("-1 Center")
    print("-1 Left Wing")
    print("-1 Right Wing")
    print("-2 Defenseman")
    print("-1 Goalie")
    print("You may fill these positions in any order you like.")
    print("You will draft your team with a certain salary cap in mind, as each player you draft will cost a certain amount.")
    print("Keep in mind once you draft a player there is no turning back.")
    print("Once the draft is over the season will begin simulating each game one by one until the season is over.")
    print("Once the season has finished you will be able to evaluate how your team preformed.")

    print("*************** Pick your Team ***************")     # pick team name
    print("Input a number 1-32")
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

        Ready = False    # Get rid of "Ready = False" once below is complete
        if draft[i] == userTeam or Ready is True:       # if current team drafting is Users team
                                        # Get rid of "or Ready is True" once below is complete
            '''
              ***** code for manually picking players goes here *****
              Paramenters:
                    pos[i] = list of user's team's undrafted positions
                    undraftedPlayers = list if undrafetd players with their stats
                    undraftedGoalies = list of undrafted goalies with their stats
              Return Values:
                    player = players that was chosen with their stats ex: [Ducks player1 name, former team, salary, age, position,....other statistics]
                    position = position of player that was chosen. ex: "C"
            '''
            # player, position = UserChoosePlayerFunction(pos[i], undraftedPlayers, undraftedGoalies)

            for k in range(len(teamsList)):    # finds index of current team drafting
                if teamsList[k] == draft[i]:
                    j = k
            temp = []
            for k in range(len(pos[j])):    # removes position that was selected from undrafted positions list pos[]
                if pos[j][k] != position or found is True:
                    temp.append(pos[j][k])
                if pos[j][k] == position:
                    found = True
            pos[j] = temp
            player.append((len(teamRosters[j])+1, (i + 1) - (32 * (len(teamRosters[j])))))
            print("Player Selected:", position, player[0])
            teamRosters[j].append(player)     # adds player to team's players list
            undraftedGoalies.remove(player)  # removes player from undrafted list

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
                undraftedGoalies = order(undraftedGoalies, 'W')
                player = undraftedGoalies[1]
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

    for x in range(len(teamRosters)):         # prints each teams' full roster (just names)
        print(teamsList[x], ": ", flush=True)
        for y in range(len(teamRosters[x])):
            print("    ", teamRosters[x][y][0], flush=True)
        time.sleep(1)

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

    simulateSeason(teamObjectList, teamsList[userTeam])



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
frame = ttk.Frame(root, width=300,height=300).grid(column=0,row=0)
image = PhotoImage(file='BeGMimg.png')
label = ttk.Label(frame, text='start img')
label['image'] = image
label.grid(column=0,row=0,columnspan=2)
startGame = ttk.Button(frame, text="Start Game", command=playGame).grid(column=0,row=1,padx=10,pady=10)
exitGame = ttk.Button(frame, text="ExitGame", command=exitGame).grid(column=1,row=1,padx=10)

root.mainloop()
