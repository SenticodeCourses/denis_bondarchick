class Region:
    def __init__(self):
        self.region_list = ['Brestreg', 'Hrodnoreg']
        self.brestreg = 'Brestskaya voblast'
        self.hrodnoreg = 'Hrodnenskaya voblast'

    def view_region(self, region):
        welcome = '    add "/city/" to URL'
        if region == 'Hrodnoreg':
            return self.hrodnoreg + welcome
        elif region == 'Brestreg':
            return self.brestreg + welcome
