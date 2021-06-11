
class Cell:
    def __init__(self, lon, lat):
        self.pixel = 0
        self.potential = 0.0
        self.potential_scale = 0.0
        self.potential_scale_wk = 0.0
        self.sinus = "UNDEFINED"
        self.lon = lon
        self.lat = lat
        self.gru_lt = 0
        self.gru_bt = 0

