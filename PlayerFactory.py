from Players import Center, Goalie, RightWinger, LeftWinger, Defenseman


# 'Name', 'FTeam', 'Salary', 'Age', 'Pos', 'GP', 'G', 'A', 'P', 'PIM', '+/-'


class createPlayerFactory:  # Input will be a list of data where type[0] is the position
    @staticmethod
    def createPlayer(type):
        if type[4] == "Goalie":
            print("Goalie")
            return Goalie(type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10])
        if type[4] == "Center":
            print("Center")
            return Center(type[0] ,type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10])
        if type[4] == "RightWinger":
            print("RightWinger")
            return RightWinger(type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10])
        if type[4] == "LeftWinger":
            print("LeftWinger")
            return LeftWinger(type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10])
        if type[4] == "Defenseman":
            print("Defenseman")
            return Defenseman(type[1], type[2], type[3], type[4], type[5], type[6], type[7], type[8], type[9], type[10])
