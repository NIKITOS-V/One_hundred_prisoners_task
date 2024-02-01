from numpy.random import shuffle


class Prisoner:
    def __init__(self, RandomNumbers, NumberTry):
        self.RandomNumbers = RandomNumbers
        self.NumberTry = NumberTry

    def RandomChoise(self, Field, PrisonNumber):
        shuffle(self.RandomNumbers)
        for Box in self.RandomNumbers[0: self.NumberTry]:
            if Field[Box] == PrisonNumber:
                return 1
        return 0

    def NormalChoise(self, Field, PrisonNumber):
        LastNumber = PrisonNumber
        print(f'\nНомер заключённого: {PrisonNumber}')
        for Try in range(self.NumberTry-1):
            print(f"    номер коробки: {LastNumber}, Номер на листе: {Field[LastNumber]}")
            if PrisonNumber == Field[LastNumber]:
                print(f'    номер найден')
                return 1
            LastNumber = Field[LastNumber]
        print(f'    номер не найден')
        return 0