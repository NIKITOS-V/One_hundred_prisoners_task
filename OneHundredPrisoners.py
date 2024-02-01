from random import shuffle
from Git.One_hundred_prisoners_task.Experimet_Parameters import *


class Room:
    def __init__(self, RandomNumbers):
        self.RandomNumbers = RandomNumbers
        self.Field = {}

    def GeneraneField(self):
        shuffle(self.RandomNumbers)
        self.Field = {box+1: number for box, number in enumerate(self.RandomNumbers)}


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


class Experiment:

    RandomNumbers = [number for number in range(1, NumberPrisoners+1)]

    def __init__(self):
        self.NumberExperiments = NumberExperiments
        self.ExperimentMode = ExperimentMode
        self.NumberPrisoners = NumberPrisoners
        self.NumberTry = NumberTry
        self.CmdMode = CmdMode
        self.TextFileMode = TextFileMode
        self.ReportMode = ReportMode

        self.GoodResults = 0

        self.Room = Room(self.RandomNumbers)
        self.Prisoner = Prisoner(self.RandomNumbers, self.NumberTry)

        self.StartExperiment()

    def StartExperiment(self):
        for ExperimentNumber in range(1, self.NumberExperiments+1):
            print(f'\n\nНомер эксперимента: {ExperimentNumber}\n' )

            self.Room.GeneraneField()
            self.Experiment()

        print('\n')
        print(f'Шанс: {self.GoodResults / self.NumberExperiments * 100}%, '
              f'Хороших исходов: {self.GoodResults}, '
              f'Неудачных исходов {self.NumberExperiments - self.GoodResults}')

    def Experiment(self):
        if not self.ExperimentMode:
            for PrisonerNumber in range(1, self.NumberPrisoners+1):
                if not self.Prisoner.RandomChoise(self.Room.Field, PrisonerNumber):
                    print('\nЭксперимент завершён неудачно')
                    return
            self.GoodResults += 1
            print('\nЭксперимент завершён удачно')

        elif self.ExperimentMode:
            for PrisonerNumber in range(1, self.NumberPrisoners+1):
                if not self.Prisoner.NormalChoise(self.Room.Field, PrisonerNumber):
                    print('\nЭксперимент завершён неудачно')
                    return
            self.GoodResults += 1
            print('\nЭксперимент завершён удачно')


Exp = Experiment()

