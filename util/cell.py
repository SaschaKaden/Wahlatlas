from util.reader import SinusType


class Cell:
    def __init__(self, id_value):
        self.id_value = id_value
        self.pixel = -1
        self.potential = 0.0
        self.sinus = SinusType.UNDEFINED
        self.x = 99999999
        self.y = 99999999



