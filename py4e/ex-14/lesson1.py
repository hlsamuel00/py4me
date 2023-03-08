class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name) -> None:
        self.name = name
        print(self.name, 'was constructed!')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'Points:', self.points)

an = PartyAnimal('Anne')

an.party()
an.party()
an.party()

j = FootballFan('Jason')
j.party()
j.touchdown()
