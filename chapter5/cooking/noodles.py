class Noodle:
    thickness = 1
    source = "밀가루"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class UdonNoodle(Noodle):
    thickness = 2
    pass


class DangNoodle(Noodle):
    source = "녹말"
