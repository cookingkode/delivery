class Executive():
    yaml_tag = u'!DE'
    def __init__(self, id, lat, long):
        self.id = id
        self.lat = lat
        self.long = long

    def __hash__(self):
        return hash(self.id)

    def get_latlong(self):
        return (self.lat, self.long)
