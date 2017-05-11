class cell:
    def __init__(self,pos):
        self.pos = pos
        self.infected = False
        self.vaccinated = False
        self.new = False

    def infect(self):
        # checks if its not infinfected
        if self.vaccinated:
            return 2
        elif self.infected != True and self.new != True:
            self.infected = True
            self.new = True
            return 3
        elif self.infected:
            return 3

    def getpos(self):
        return self.pos
