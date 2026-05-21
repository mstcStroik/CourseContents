from Athletes import athlete

class event():

    sVenue = ""
    sName = ""
    lstAthletes = []

    def __init__(self, venue, name):
        self.sName = name
        self.sVenue = venue
        self.lstAthletes = []

    def __str__(self):
        return self.sName + "(" + self.sVenue + ")" + self.PrintAthletes()

    def AddAthlete(self, name, country):
        athleteToAdd = athlete(name, country)
        self.lstAthletes.append(athleteToAdd)

        return athleteToAdd

    def PrintAthletes(self):
        outString = ""
        for athl in self.lstAthletes:
            outString += "\n\t" + str(athl)
        return outString