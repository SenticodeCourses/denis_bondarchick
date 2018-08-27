import random

class Software:
    pass


class Hardware:
    def __init__(self):
        self.wear_degree = 100
        self.crashed = 0
        self.exist = 1
        self.dustiness = 0
        self.obsolescence = 1000

    def crash(self):
        if self.wear_degree == 0:
            self.crashed = 1
        if self.crashed == 0:
            if random.randint(0, 100) in range(round(10 - self.wear_degree**(1/2))):
                self.crashed = 1

    def is_exist(self):
        if random.randint(0, 100) == 50:
            self.exist = 0

    def dusting(self, grade=1):
        if self.dustiness < 900:
            self.dustiness += grade
        else:
            if random.randint(0, 20) == 10:
                self.crash = 1

    def work(self):
        self.wear_degree -= 1
        if self.crashed == 1:
            pass
        self.crash(self)
        self.is_exist(self)
        self.dusting()
        if self.obsolescence > 1:
            self.obsolescence -= 1
        else:
            self.crashed = 1


class Monitor(Hardware):
    def __init__(self):
        Hardware.__init__()
        self.name = 'Daliahliad ' + str(random.randint(1, 3))

    def work(self):
        self.wear_degree -= 1
        if self.crashed == 1:
            pass
        self.crash(self)
        self.is_exist(self)
        self.dusting(2)
        if self.obsolescence >1:
            self.obsolescence -= 2
        else:
            self.crash = 1


class System(Hardware):
    def __init__(self):
        Hardware.__init__()
        self.name = 'Vajavoda'

    def is_exist(self):
        if random.randint(0, 50) == 25:
            self.exist = 0

    def work(self):
        self.wear_degree -= 1
        if self.crashed == 1:
            pass
        self.crash(self)
        self.is_exist(self)
        self.dusting(5)
        if self.obsolescence > 1:
            self.obsolescence -= 5
        else:
            self.crash = 1



class Keyboard(Hardware):
    def __init__(self):
        Hardware.__init__()
        self.name = 'Aksamit ' + str(random.randint(1, 3))

    def work(self):
        self.wear_degree -= 2
        self.crash(self)
        self.is_exist(self)
        self.dusting(3)
        if self.obsolescence > 999:
            self.obsolescence -= 1
        else:
            self.crashed = 1
