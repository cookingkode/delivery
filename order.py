class Order:
    def __init__(self, id, lat, long, value):
        self.id = id
        self.lat = lat
        self.long = long
        self.value = value

    def __hash__(self):
        return hash(self.id)

    def get_latlong(self):
        return (self.lat, self.long)

    # def __repr__(self):
    #     return "%s(name=%r, hp=%r, sp=%r)" % (
    #         self.__class__.__name__, self.id, self.lat, self.long)
