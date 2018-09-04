class City:
    def __init__(self):
        self.cities = ['Brest', 'Hrodno']
        self.cities_brest = 'Brest'
        self.cities_hrodno = 'Hrodno'
        self.brest_name = 'Brest'
        self.hrodno_name = 'Hrodno'

    def view_city(self, city_name):
        if city_name == 'Brest':
            return self.brest_name
        elif city_name == 'Hrodno':
            return self.hrodno_name

    def view_city_of_region(self, region):
        if region == 'Brestreg':
            return self.cities_brest
        elif region == 'Hrodnoreg':
            return self.cities_hrodno
