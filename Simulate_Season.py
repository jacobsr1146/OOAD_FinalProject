import random
from Players import Center, Goalie, RightWinger, LeftWinger, Defenseman, Teams
from Strategy import Game, Strategy, StrategyA



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


def simulateSeason(teamObjectList, userTeamName):
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
        #[], [], [], [], [], []
        gameStats = [[[], [], [], [], [], []], [[], [], [], [], [], []]]          # keeping track of current game statistics
        for i in range(len(team1.playersOnTeam)):       # [name, pos, goalsAgainst, saves]
            if team1.playersOnTeam[i].position == "G":
                gameStats[0][i].append([team1.playersOnTeam[i].name,
                                        team1.playersOnTeam[i].position,
                                        0, 0])
            else:                                       # [name, pos, points, goals, assist, PPG, GWG, +/-]
                gameStats[0][i].append([team1.playersOnTeam[i].name,
                                        team1.playersOnTeam[i].position,
                                        0, 0, 0, 0, 0, 0])
        for i in range(len(team2.playersOnTeam)):
            if team2.playersOnTeam[i].position == "G":
                gameStats[1][i].append([team2.playersOnTeam[i].name,
                                        team2.playersOnTeam[i].position,
                                        0, 0])
            else:
                gameStats[1][i].append([team2.playersOnTeam[i].name,
                                        team2.playersOnTeam[i].position,
                                        0, 0, 0, 0, 0, 0])

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
                        gameStats[x][j][0][3] = gameStats[x][j][0][3] + 1
                        teams[x].playersOnTeam[j].curr_points = teams[x].playersOnTeam[j].curr_points + 1
                        gameStats[x][j][0][2] = gameStats[x][j][0][2] + 1
                        if random.randint(1, 100) < 10:
                            teams[x].playersOnTeam[j].curr_PPG = teams[x].playersOnTeam[j].curr_PPG + 1   # updating goal scorer's curr_PPGs
                            gameStats[x][j][0][5] = gameStats[x][j][0][5] + 1
                        if x == 0 and i == team2goals:
                            teams[x].playersOnTeam[j].curr_GWG = teams[x].playersOnTeam[j].curr_GWG + 1   # updating goal scorer's curr_GWGs
                            gameStats[x][j][0][6] = gameStats[x][j][0][6] + 1
                        if x == 1 and i == team1goals:
                            teams[x].playersOnTeam[j].curr_GWG = teams[x].playersOnTeam[j].curr_GWG + 1   # updating goal scorer's curr_GWGs
                            gameStats[x][j][0][6] = gameStats[x][j][0][6] + 1
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
                            gameStats[x][j][0][4] = gameStats[x][j][0][4] + 1
                            teams[x].playersOnTeam[j].curr_points = teams[x].playersOnTeam[j].curr_points + 1
                            gameStats[x][j][0][2] = gameStats[x][j][0][2] + 1

        # +/- and Games Played:
        for i in range(len(team1.playersOnTeam)):
            if team1.playersOnTeam[i].position != "G":
                team1.playersOnTeam[i].curr_plusMinus = team1.playersOnTeam[i].curr_plusMinus + team1goals - team2goals
                gameStats[0][i][0][7] = gameStats[0][i][0][7] + team1goals - team2goals
            team1.playersOnTeam[i].curr_gamesPlayed = team1.playersOnTeam[i].curr_gamesPlayed + 1
        for i in range(len(team2.playersOnTeam)):
            if team2.playersOnTeam[i].position != "G":
                team2.playersOnTeam[i].curr_plusMinus = team2.playersOnTeam[i].curr_plusMinus + team2goals - team1goals
                gameStats[1][i][0][7] = gameStats[1][i][0][7] + team2goals - team1goals
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
                key1 = i
            if team2.playersOnTeam[i].position == "G":
                goalie2 = team2.playersOnTeam[i]
                key2 = i
        # Wins and Loses
        if team1goals > team2goals:
            goalie1.curr_wins = goalie1.curr_wins + 1
            goalie2.curr_loses = goalie2.curr_loses + 1
        else:
            goalie2.curr_wins = goalie2.curr_wins + 1
            goalie1.curr_loses = goalie1.curr_loses + 1
        # Goals Against, Saves, and Win%
        goalie1.curr_goalsAgainst = goalie1.curr_goalsAgainst + team2goals
        gameStats[0][key1][0][2] = gameStats[0][key1][0][2] + team2goals
        goalie2.curr_goalsAgainst = goalie2.curr_goalsAgainst + team1goals
        gameStats[1][key2][0][2] = gameStats[1][key2][0][2] + team1goals
        goalie1.curr_saves = goalie1.curr_saves + (team2shots - team2goals)
        gameStats[0][key1][0][3] = gameStats[0][key1][0][3] + (team2shots - team2goals)
        goalie2.curr_saves = goalie2.curr_saves + (team1shots - team1goals)
        gameStats[1][key2][0][3] = gameStats[1][key2][0][3] + (team1shots - team1goals)
        goalie1.curr_winPercent = goalie1.curr_wins/goalie1.curr_gamesPlayed
        goalie2.curr_winPercent = goalie2.curr_wins/goalie2.curr_gamesPlayed
        if team1goals == 0:
            goalie2.curr_shutOuts = goalie2.curr_shutOuts + 1
        if team2goals == 0:
            goalie1.curr_shutOuts = goalie1.curr_shutOuts + 1

        if team1.teamName == userTeamName or team2.teamName == userTeamName:
            for i in range(len(gameStats)):
                if i == 0:
                    print(team1.teamName, ": ")
                else:
                    print(team2.teamName, ": ")
                for j in range(len(gameStats[i])):
                    if gameStats[i][j][0][1] == "G":
                        print("    ", gameStats[i][j][0][0], gameStats[i][j][0][1], ":")
                        print("     Goals Against:", gameStats[i][j][0][2])
                        print("     Saves:", gameStats[i][j][0][3])
                        print(" ")
                    else:
                        print("    ", gameStats[i][j][0][0], gameStats[i][j][0][1], ":")
                        print("     Points:", gameStats[i][j][0][2])
                        print("     Goals:", gameStats[i][j][0][3])
                        print("     Assist:", gameStats[i][j][0][4])
                        print("     PPG:", gameStats[i][j][0][5])
                        print("     GWG:", gameStats[i][j][0][6])
                        print("     +/-:", gameStats[i][j][0][7])
                        print(" ")


            # ********* END of SEASON **********
    return




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
