import datetime


def Birthdate(year: int, month: int, day: int):
    return tuple([year, month, day])

class Age:

    def __init__(self, birthdate: tuple):
        self.birthdate = birthdate

    def ageFinder(self):
        now = datetime.datetime.now()
        yeardif = now.year - self.birthdate[0]
        if now.month < self.birthdate[1]:
            if now.day < self.birthdate[2]:
                yeardif = yeardif - 1
        return yeardif

    def __export__(self):
        return str({
            "birthdate": self.birthdate
        })

