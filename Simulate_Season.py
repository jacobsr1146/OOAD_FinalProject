import random


def sort(lst, stat, key):
    for i in range(len(lst[0])):        #finds index of statistic
        if lst[0][i] == stat:
            index = i

    newList = []
    newList.append(lst[0])
    for i in range(len(lst)):
        if lst[i][index] == key:
            newList.append(lst[i])
    return newList

def order(lst, stat):
    for i in range(len(lst[0])):        #finds index of statistic
        if lst[0][i] == stat:
            index = i

    newList = []
    newList.append(lst[0])
    lst.pop(0)
    while len(lst) != 0:
        high = 0
        for x in range(len(lst)):       #re-orders list based on statistic
            curr = lst[x][index]
            if curr > high:
                high = curr
                highIndex = x
        newList.append(lst[highIndex])
        lst.pop(highIndex)

    return newList

def checkInput(res, correctList):
    check = False
    while check == False:
        if res in correctList:
            check = True
        else:
            res = input("Unacceptable input. Please try again: ")
    return res

def main():
    from Update_Players_List import importFile
    playersList, goaliesList = importFile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")

    teamsLst = ["Anaheim Ducks", "Arizona Coyotes", "Boston Bruins", "Buffalo Sabres", "Calgary Flames",
                "Carolina Hurricanes", "Chicago Blackhawks", "Colorado Avalanche", "Columbus Blue Jackets",
                "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers", "Florida Panthers", "Los Angeles Kings",
                "Minnesota Wild", "Montreal Canadiens", "Nashville Predators", "New Jersey Devils", "New York Islanders",
                "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Pittsburgh Penguins", "San Jose Sharks",
                "Seattle Kraken", "St Louis Blues", "Tampa Bay Lightning", "Toronto Maple Leafs", "Vancouver Canucks",
                "Vegas Golden Knights", "Washington Capitals", "Winnipeg Jets"]

    print("NHL be a GM simulator")
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

    print("*************** Pick your Team ***************")
    print("Input a number 1-32 or the letter 'r' for random")
    i = 0
    while i < len(teamsLst):
        print(i+1, ". ", teamsLst[i], "     ", i+2, ". ", teamsLst[i+1], "     ", i+3, ". ", teamsLst[i+2], "     ", i+4, ". ", teamsLst[i+3], "     ",)
        i = i+4
    check = []
    for i in range(1, 33):
        check.append(str(i))
    draftTeam = int(checkInput(input("Input: "), check)) - 1

    print("*************** Pick you starting draft spot ***************")
    print("input a number 1-32 or the letter 'r' for random")
    draftNum = input("Input: ")
    check = []
    for i in range(1, 33):
        check.append(str(i))
    check.append('r')
    draftNum = checkInput(draftNum, check)

    satisfied = False
    if draftNum == 'r':
        while satisfied == False:
            draftNum = random.randint(1, 32)
            print("Random Position: ", draftNum)
            res = input("Is this position ok? (y/n): ")
            res = checkInput(res, ['y', 'Y', 'n', 'N'])
            if res in ['y', 'Y']:
                satisfied = True
    else:
        draftNum = int(draftNum)

    #*********** DRAFT ***********
    print("Draft Number = ", draftNum)
    print("Draft team = ", teamsLst[draftTeam])
    randTeam = [draftTeam]
    draftOrder = []
    while len(draftOrder) < 32:
        if len(draftOrder)+1 == draftNum:
            draftOrder.append(teamsLst[draftTeam])
            randTeam.append(draftTeam)
        else:
            while True:
                rando = random.randrange(0, 32)
                if rando not in randTeam:
                    break
            draftOrder.append(teamsLst[rando])
            randTeam.append(rando)

    print("*************** Draft Order ***************")
    print(draftOrder)

    print("*************** Draft Begins ***************")
    lst = ['C', 'LW', 'RW', 'D', 'D', 'G']
    pos = []
    while len(pos) < 32:
        pos.append(lst)
    Teams = []
    while len(Teams) < 31:
        Teams.append([])
    draft = []
    while len(pos[0]) > 0:
        if len(pos[0])%2 == 0:
            draft = draftOrder
            for i in range(len(draft)):
                position = random.choice(pos[i])
                pos[i].remove(position)
                if position == 'G':
                    player = order(goaliesList, 'W')[1]
                else:
                    player = order(sort(playersList, 'Pos', position), 'P')[1]
                    print(player[0])
                    Teams[i].append(player[0])
                    playersList.remove(player)

        else:

            draft = draftOrder.reverse()
            for i in range(len(draft)):
                i_ = 31-i
                position = random.choice(pos[i_])
                pos[i_].remove(position)
                if position == 'G':
                    player = order(goaliesList, 'W')[1]
                else:
                    player = order(sort(playersList, 'Pos', position), 'P')[1]
                    print(player[0])
                    Teams[i_].append(player[0])
                    playersList.remove(player)

    for x in range(len(Teams)):
        print(draftOrder[x], ": ")
        for y in range(len(Teams[x])):
            print("    ", Teams[x][y][0])








main()

def testing():
    from Update_Players_List import importFile
    playersList, goaliesList = importFile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")
    print("C:", len(sort(playersList, 'Pos', 'C')))
    print("LW:", len(sort(playersList, 'Pos', 'LW')))
    print("RW:", len(sort(playersList, 'Pos', 'RW')))
    print("D:", len(sort(playersList, 'Pos', 'D')))
    print("G:", len(goaliesList))


#testing()

