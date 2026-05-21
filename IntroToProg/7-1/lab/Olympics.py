from Events import event

class olympics():

    nYear = 0
    sLocation = ""
    bSummer = False
    lstEvents = []

    def __init__(self, year, location, summer):
        self.nYear = year
        self.sLocation = location
        self.bSummer = summer
        self.lstEvents = [] 

    def __str__(self):
        if self.bSummer:
            description = " Summer Olympic Games!"
        else:
            description = " Winter Olympic Games!"

        return str(self.nYear) + ": " + self.sLocation + description

    def AddEvent(self, venue, name):
        olympicEvent = event(venue, name)
        self.GetAthletes(olympicEvent)
        self.lstEvents.append(olympicEvent)

        return olympicEvent

    def AddEventFromFile(self, venue, name):
        olympicEvent = event(venue, name)
        self.lstEvents.append(olympicEvent)

        return olympicEvent

    def GetAthletes(self, event):
        athleteName = input("Please give us the name of an athlete ('quit' to quit): ")
        while athleteName != 'quit':
            athleteCountry = input ("Please give us the name of the athlete's country: ")
            event.AddAthlete(athleteName, athleteCountry)

            athleteName = input("Please give us the name of an athlete ('quit' to quit): ")

    def Advertise(self):
        print(self)

        for event in self.lstEvents:
            print(event)
