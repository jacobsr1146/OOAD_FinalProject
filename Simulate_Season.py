import random
import PlayerFactory
from Players import Center, Goalie, RightWinger, LeftWinger, Defenseman, Teams
from Strategy import Game, Strategy, StrategyA
from Update_Players_List import importFile

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

def orderGoals(lst):
    newList = []
    newList.append(lst[0])
    lst.pop(0)
    while len(lst) != 0:
        high = 0
        for x in range(len(lst)):       # re-orders list based on Goals statistic
            curr = lst[x].last_goals    # use for Player Objects in Teams.playersOnTeam list
            if curr > high:
                high = curr
                highIndex = x
        newList.append(lst[highIndex])
        lst.pop(highIndex)

    return newList

def orderAssist(lst):
    newList = []
    newList.append(lst[0])
    lst.pop(0)
    while len(lst) != 0:
        high = 0
        for x in range(len(lst)):       # re-orders list based on Assist statistic
            curr = lst[x].last_assists  # use for Player Objects in Teams.playersOnTeam list
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


def main():
    undraftedPlayers, undraftedGoalies = importFile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")

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

    print("*************** Draft Order ***************")
    print(draftOrder)

    print("*************** Draft Begins ***************")
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
        print("***********************************************")
        print("Team:", draft[i])

        Ready = False
        if draft[i] == userTeam or Ready is True:       # if current team drafting is Users team

            pass
             # ***** code for manually picking players goes here *****
             
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
                print("Player Selected:", position, player[0])
                teamRosters[j].append(player)     # adds player to team's players list
                undraftedGoalies.remove(player)  # removes player from undrafted list

            else:                           # case for any other player position
                player = order(sort(undraftedPlayers, 'Pos', position), 'P')[1]
                print("Player Selected:", position, player[0])
                teamRosters[j].append(player)     # adds player to team's players list
                undraftedPlayers.remove(player)  # removes player from undrafted list


    for x in range(len(teamRosters)):         # prints each teams' full roster (just names)
        print(teamsList[x], ": ")
        for y in range(len(teamRosters[x])):
            print("    ", teamRosters[x][y][0])

    for i in range(len(teamRosters)-1):                     # Changes which stats are loaded in
        for j in range(len(teamRosters[i])):
            teamRosters[i][j] = teamRosters[i][j][0:12]     # first 12 stats

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
    # ********** Creating Schedule **********
    scheduleList = []
    for i in range(len(teamObjectList)):    # creates list of each team 82 time (length = 82 * 32)
        count = 0
        while count < 82:
            scheduleList.append(teamObjectList[i])
            count = count + 1
    random.shuffle(scheduleList)            # shuffles list from above
    changes = 1
    while changes == 1:                     # loop goes through scheduleList and makes sure their are no doubles. ex: [a, b, b, c]
        changes = 0
        for i in range(len(scheduleList)-1):
            if scheduleList[i] == scheduleList[i+1]:
                randnum = random.randint(0, len(scheduleList)-1)
                temp = scheduleList[i]
                scheduleList[i] = scheduleList[randnum]
                scheduleList[randnum] = temp
                changes = 1
    schedule = []
    num = 0
    while num < len(scheduleList):                                  # groups every 2 teams together into tuples
        schedule.append((scheduleList[num], scheduleList[num+1]))
        num = num + 2

    # *********** BEGIN SEASON ************
    game = Game(StrategyA())                       # create game object
    for match in range(len(schedule)):
        team1 = schedule[match][0]
        team2 = schedule[match][1]


        game.strategy = StrategyA()                 # randomly picks a strategy to simulate the current game
        '''
        CODE NEEDED by Jacob
        '''

        gameResults = game.play(team1, team2)      # simulates game with strategy pattern
        team1goals = gameResults[0]
        team2goals = gameResults[1]
        team1shots = gameResults[2]
        team2shots = gameResults[3]

        # *********** Updating Statistics ***********
        teams = [team1, team2]
        teamgoals = [team1goals, team2goals]
        for x in range(len(teams)):             # creates temp list of current team without goalie
            teamplayers = []
            for i in range(len(teams[x].playersOnTeam)):
                if teams[x].playersOnTeam[i].position != "G":
                    teamplayers.append(teams[x].playersOnTeam[i])
            # Goals and assist:
            for i in range(teamgoals[x]):
                goalScorer = random.choices(orderGoals(teamplayers.copy()), weights=(50, 40, 30, 20, 10))[0]      # choosing goal scorers
                for j in range(len(teams[x].playersOnTeam)):
                    if teams[x].playersOnTeam[j] == goalScorer:
                        teams[x].playersOnTeam[j].curr_goals = teams[x].playersOnTeam[j].curr_goals + 1   # updating goal scorer's curr_goals
                        teams[x].playersOnTeam[j].curr_points = teams[x].playersOnTeam[j].curr_points + 1
                        if random.randint(1, 100) < 10:
                            teams[x].playersOnTeam[j].curr_PPG = teams[x].playersOnTeam[j].curr_PPG + 1   # updating goal scorer's curr_PPGs
                        if x == 0 and i == team2goals:
                            teams[x].playersOnTeam[j].curr_GWG = teams[x].playersOnTeam[j].curr_GWG + 1   # updating goal scorer's curr_GWGs
                        if x == 1 and i == team1goals:
                            teams[x].playersOnTeam[j].curr_GWG = teams[x].playersOnTeam[j].curr_GWG + 1   # updating goal scorer's curr_GWGs
                assist = []
                while len(assist) == 0:
                    assist = random.choices(orderAssist(teamplayers.copy()), weights=(50, 40, 30, 20, 10), k=2)   # finding assist for each goal
                    for num in range(len(assist)):
                        if goalScorer in assist:
                            assist.remove(goalScorer)
                if len(assist) > 1:
                    if assist[0] == assist[1]:
                        assist.pop()
                for k in range(len(assist)-1):
                    for j in range(len(teams[x].playersOnTeam)-1):
                        if teams[x].playersOnTeam[j] == assist[k]:
                            teams[x].playersOnTeam[j].curr_assists = teams[x].playersOnTeam[j].curr_assists + 1     # updating assister's curr_assist
                            teams[x].playersOnTeam[j].curr_points = teams[x].playersOnTeam[j].curr_points + 1

        # +/- and Games Played:
        for i in range(len(team1.playersOnTeam)):
            if team1.playersOnTeam[i].position != "G":
                team1.playersOnTeam[i].curr_plusMinus = team1.playersOnTeam[i].curr_plusMinus + team1goals - team2goals
            team1.playersOnTeam[i].curr_gamesPlayed = team1.playersOnTeam[i].curr_gamesPlayed + 1
        for i in range(len(team2.playersOnTeam)):
            if team2.playersOnTeam[i].position != "G":
                team2.playersOnTeam[i].curr_plusMinus = team2.playersOnTeam[i].curr_plusMinus + team2goals - team1goals
            team2.playersOnTeam[i].curr_gamesPlayed = team2.playersOnTeam[i].curr_gamesPlayed + 1
        # Team Records
        if team1goals > team2goals:
            team1.wins = team1.wins + 1
            team2.loses = team2.loses + 1
        else:
            team2.wins = team1.wins + 1
            team1.loses = team2.loses + 1
        # Goalie Statistics
        for i in range(len(team1.playersOnTeam)):       #finding goalies on each team
            if team1.playersOnTeam[i].position == "G":
                goalie1 = team1.playersOnTeam[i]
            if team2.playersOnTeam[i].position == "G":
                goalie2 = team2.playersOnTeam[i]
        # Wins and Loses
        if team1goals > team2goals:
            goalie1.curr_wins = goalie1.curr_wins + 1
            goalie2.curr_loses = goalie2.curr_loses + 1
        else:
            goalie2.curr_wins = goalie2.curr_wins + 1
            goalie1.curr_loses = goalie1.curr_loses + 1
        # Goals Against, Saves, and Win%
        goalie1.curr_goalsAgainst = goalie1.curr_goalsAgainst + team2goals
        goalie2.curr_goalsAgainst = goalie2.curr_goalsAgainst + team1goals
        goalie1.curr_saves = goalie1.curr_saves + (team2shots - team2goals)
        goalie2.curr_saves = goalie2.curr_saves + (team1shots - team1goals)
        goalie1.curr_winPercent = goalie1.curr_wins/goalie1.curr_gamesPlayed
        goalie2.curr_winPercent = goalie2.curr_wins/goalie2.curr_gamesPlayed
        if team1goals == 0:
            goalie2.curr_shutOuts = goalie2.curr_shutOuts + 1
        if team2goals == 0:
            goalie1.curr_shutOuts = goalie1.curr_shutOuts + 1

    # ********* END of SEASON **********
    for i in range(len(teamObjectList)):
        teamObjectList[i].printTeamPlayers()
        print("************")

main()



def testing():              #used for testing small samples. Ignore
    from Update_Players_List import importFile
    undraftedPlayers, undraftedGoalies = importFile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")
    print("C:", len(sort(undraftedPlayers, 'Pos', 'C')))
    print("LW:", len(sort(undraftedPlayers, 'Pos', 'LW')))
    print("RW:", len(sort(undraftedPlayers, 'Pos', 'RW')))
    print("D:", len(sort(undraftedPlayers, 'Pos', 'D')))
    print("G:", len(undraftedGoalies))

    teamsList = ["Anaheim Ducks", "Arizona Coyotes", "Boston Bruins", "Buffalo Sabres", "Calgary Flames",
                 "Carolina Hurricanes", "Chicago Blackhawks", "Colorado Avalanche", "Columbus Blue Jackets",
                 "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers", "Florida Panthers", "Los Angeles Kings",
                 "Minnesota Wild", "Montreal Canadiens", "Nashville Predators", "New Jersey Devils", "New York Islanders",
                 "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Pittsburgh Penguins", "San Jose Sharks",
                 "Seattle Kraken", "St Louis Blues", "Tampa Bay Lightning", "Toronto Maple Leafs", "Vancouver Canucks",
                 "Vegas Golden Knights", "Washington Capitals", "Winnipeg Jets"]

    central = ["Arizona Coyotes", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Minnesota Wild",
               "Nashville Predators", "St Louis Blues", "Winnipeg Jets"]
    pacific = ["Anaheim Ducks", "Calgary Flames", "Edmonton Oilers", "Los Angeles Kings",
                 "San Jose Sharks", "Seattle Kraken", "Vancouver Canucks", "Vegas Golden Knights"]
    metro = ["Carolina Hurricanes", "Columbus Blue Jackets", "New Jersey Devils", "New York Islanders",
             "New York Rangers", "Philadelphia Flyers", "Pittsburgh Penguins", "Washington Capitals"]
    atlantic = ["Boston Bruins", "Buffalo Sabres",  "Detroit Red Wings", "Florida Panthers", "Montreal Canadiens",
                "Ottawa Senators", "Tampa Bay Lightning", "Toronto Maple Leafs"]
    west = ["Arizona Coyotes", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Minnesota Wild",
             "Nashville Predators", "St Louis Blues", "Winnipeg Jets", "Anaheim Ducks", "Calgary Flames",
             "Edmonton Oilers", "Los Angeles Kings", "San Jose Sharks", "Seattle Kraken", "Vancouver Canucks",
             "Vegas Golden Knights"]
    east = ["Carolina Hurricanes", "Columbus Blue Jackets", "New Jersey Devils", "New York Islanders",
            "New York Rangers", "Philadelphia Flyers", "Pittsburgh Penguins", "Washington Capitals", "Boston Bruins",
            "Buffalo Sabres",  "Detroit Red Wings", "Florida Panthers", "Montreal Canadiens", "Ottawa Senators",
            "Tampa Bay Lightning", "Toronto Maple Leafs"]




def testing2():
    teamsList = ["Anaheim Ducks", "Arizona Coyotes", "Boston Bruins", "Buffalo Sabres", "Calgary Flames",
                 "Carolina Hurricanes", "Chicago Blackhawks", "Colorado Avalanche", "Columbus Blue Jackets",
                 "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers", "Florida Panthers", "Los Angeles Kings",
                 "Minnesota Wild", "Montreal Canadiens", "Nashville Predators", "New Jersey Devils", "New York Islanders",
                 "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Pittsburgh Penguins", "San Jose Sharks",
                 "Seattle Kraken", "St Louis Blues", "Tampa Bay Lightning", "Toronto Maple Leafs", "Vancouver Canucks",
                 "Vegas Golden Knights", "Washington Capitals", "Winnipeg Jets"]
    scheduleList = []
    for i in range(len(teamsList)):
        count = 0
        while count < 82:
            scheduleList.append(teamsList[i])
            count = count + 1

    random.shuffle(scheduleList)

    changes = 1
    while changes == 1:
        changes = 0
        for i in range(len(scheduleList)-1):
            if scheduleList[i] == scheduleList[i+1]:
                randnum = random.randint(0, len(scheduleList)-1)
                temp = scheduleList[i]
                scheduleList[i] = scheduleList[randnum]
                scheduleList[randnum] = temp
                changes = 1

    schedule = []
    num = 0
    while num < len(scheduleList):
        schedule.append((scheduleList[num], scheduleList[num+1]))
        num = num + 2

    print(len(schedule))
    for i in range(10):
        print("    ", schedule[i])

#testing()
#testing2()
