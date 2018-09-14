class City:
    def __init__(self, cityname=None):
        if cityname is not None:
            if cityname == 'Brest':
                self.nameofcity = 'Brest'
            elif cityname == 'Hrodno':
                self.nameofcity = 'Hrodno'
        else:
            self.cities = ['Brest', 'Hrodno']
