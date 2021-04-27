val = 42


def add(a, b):
    return a + b


class Name:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "====" + self.name + "===="