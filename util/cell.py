from util.reader import SinusType


class Cell:
    def __init__(self, pixel, potential, sinus, x, y):
        self.pixel = pixel
        self.potential = potential
        self.sinus = sinus
        self.hash_value = str(pixel) + str(potential) + str(self.sinus)
        self.x = x
        self.y = y

    pixel = -1
    potential = 0.0
    sinus = SinusType.UNDEFINED
    x = 99999999
    y = 99999999


