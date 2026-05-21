from Medal import medal

class athlete():

    sName = ""
    sCountry = ""
    lstMedal = []

    def __init__(self, name, country):
        self.sName = name
        self.sCountry = country
        self.lstMedal = []

    def __str__(self):
        return  self.sCountry + ": " + self.sName + self.PrintMedals()

    def AddMedal(self, eventName, year, type):
        medalWon = medal(eventName, year, type)
        self.lstMedal.append(medalWon)

        return medalWon

    def PrintMedals(self):
        outString = ""
        for earnedMedal in self.lstMedal:
            outString += "\n\t\t" + str(earnedMedal)

        return outString