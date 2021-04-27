class Soup:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class PowderSoup(Soup):
    pass


class VegetableSoup(Soup):
    pass
