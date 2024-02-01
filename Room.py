from numpy.random import shuffle


class Room:
    def __init__(self, RandomNumbers):
        self.RandomNumbers = RandomNumbers
        self.Field = {}

    def GeneraneField(self):
        shuffle(self.RandomNumbers)
        self.Field = {box+1: number for box, number in enumerate(self.RandomNumbers)}

