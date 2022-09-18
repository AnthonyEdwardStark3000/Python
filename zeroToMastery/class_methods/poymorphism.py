class ComicBooks:
    def __init__(self, name, value):
        self.hero_name = name
        self.value = value
        self.hero_meter(self.hero_name, self.value)

    def hero_meter(self, name, range):
        print(f'Hero {name} has a value of {range} out of 10')


class Flash(ComicBooks):
    def __init__(self, name, val):
        self.hero_meter(name, val)


class SuperMan(ComicBooks):
    def __init__(self, name, val):
        self.hero_meter(name, val)


class BatMan(ComicBooks):
    def __init__(self, name, val):
        self.hero_meter(name, val)


bat = BatMan("Batman", 7)
supe = SuperMan("Superman", 9)
flash = Flash("Flash", 3)
