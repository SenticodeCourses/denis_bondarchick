class Country:
    def __init__(self):
        self.population = '~10M'
        self.dictation = 'yes'
        self.list = {'Belarus': 'Belarus'}

    def view_country(self, country):
        welcome = '    add "/region/" to URL'
        return self.list[country] + welcome
