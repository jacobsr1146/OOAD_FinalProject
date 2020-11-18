import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import datetime

def importFile(playersFile, goaliesFile):
    with open(playersFile) as f:
        encode = f.encoding

    with open(goaliesFile) as f:
        encode = f.encoding

    # NHLplayersstats_2019-20: ['Name', 'Team', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-', 'TOI', 'ES', 'PP', 'SH', 'ESG', 'PPG', 'SHG', 'GWG', 'OTG', 'ESA', 'PPA', 'SHA', 'GWA', 'OTA', 'ESP', 'PPP', 'SH
    # P', 'GWP', 'OTP', 'PPP%', 'G/60', 'A/60', 'P/60', 'ESG/60', 'ESA/60', 'ESP/60', 'PPG/60', 'PPA/60', 'PPP/60', 'G/GP', 'A/GP', 'P/GP', 'SHOTS', 'SH%', 'HITS', 'BS', 'FOW', 'FOL', 'FO%'

    # NHLgoaliestats_2019-20: ['Name', 'Team', 'Salary', 'Age', 'Pos', 'GP', 'W', 'L', 'W%', 'SO', 'GAA', 'SV%']

    playerdf = pd.read_csv(playersFile, sep=',', encoding = encode, low_memory=False) # read in NHLplayerstats_2019-20.csv file
    goaliedf = pd.read_csv(goaliesFile, sep=',', encoding = encode, low_memory=False) # read in NHLgoaliestats_2019-20.csv file

    players = list(map(list, playerdf.to_numpy()))
    goalies = list(map(list, goaliedf.to_numpy()))

    for x in range(len(players)):
        players[x].pop(0)

    for x in range(1, len(players)):        #cleaning players data
        for y in range(len(players[x])):
            if type(players[x][y]) == str:
                players[x][y] = players[x][y].replace('%', '')
                if y > 1 and y!=4:
                    if players[x][y].find(':') != -1:
                        if len(players[x][y]) == 5:
                            players[x][y] = datetime.time(0, int(players[x][y][0] + players[x][y][1]), int(players[x][y][3] + players[x][y][4]))
                        elif len(players[x][y]) == 4:
                            players[x][y] = datetime.time(0, int(players[x][y][0]), int(players[x][y][2] + players[x][y][3]))
                    elif players[x][y].find('.') != -1 or y == 2:
                        players[x][y] = float(players[x][y])
                    else:
                        players[x][y] = int(players[x][y])

    for x in range(1, len(goalies)):        #cleaning goalies data
        for y in range(len(goalies[x])):
            if type(goalies[x][y]) == str:
                goalies[x][y] = goalies[x][y].replace('%', '')
                if y > 1 and y!=4:
                    if goalies[x][y].find('.') != -1:
                        goalies[x][y] = float(goalies[x][y])
                    else:
                        goalies[x][y] = int(goalies[x][y])

    #print(players[0]) #players list key
    #print(players[1]) #first player
    #print(goalies[0]) #goalies list key
    #print(goalies[1]) #first goalie



    # Template to re-order players list based on a statistic (stat)
    """
    stat = #str of statistic
    for i in range(len(players[0])):        #finds index of statistic
        if players[0][i] == stat:
            index = i
    
    newPlayers = []
    while len(players) != 0:
        high = 0
        for x in range(len(players)):       #re-orders list based on statistic
            curr = players[x][index]
            if curr > high:
                high = curr
                index = x
        newPlayers.append(players[index])
        players.pop(index)
    
    
    for x in range(10):
        print(newPlayers[x])
    
    """
    return players, goalies


players, goalies = importFile("NHLplayerstats_2019-20.csv", "NHLgoaliestats_2019-20.csv")


