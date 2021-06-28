
class Cell:
    def __init__(self, lon, lat):
        self.pixel = 0
        self.id = ""
        self.potential_scale_wk = 0.0
        self.sinus = "UNDEFINED"
        self.lon = lon
        self.lat = lat
        self.gru_bt = 0

