from Players import Center, Goalie, RightWinger, LeftWinger, Defenseman


# 'Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-'


class createPlayerFactory:  # Input will be a list of data where type[0] is the position
    @staticmethod
    def createPlayer(type):
        if type[4] == "G":
            return Goalie(type[0] ,type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10], type[11], type[12])
        if type[4] == "C":
            return Center(type[0],type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10], type[11], type[12])
        if type[4] == "RW":
            return RightWinger(type[0],type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10], type[11], type[12])
        if type[4] == "LW":
            return LeftWinger(type[0],type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10], type[11], type[12])
        if type[4] == "D":
            return Defenseman(type[0],type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10], type[11], type[12])
