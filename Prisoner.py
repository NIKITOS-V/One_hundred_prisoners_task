from numpy.random import shuffle


class Prisoner:
    WT = ' '

    def __init__(self, RandomNumbers, NumberTry, ExperimentMode, DoFullReport):
        self.RandomNumbers = RandomNumbers
        self.NumberTry = NumberTry
        self.ExperimentMode = ExperimentMode
        self.DoFullReport = DoFullReport

        self.EnteringTheRoom = self.TacticsType()

    def EnteringTheRoom(self):
        pass

    def TacticsType(self):
        def Tactic_0(Field, PrisonerNumber):
            shuffle(self.RandomNumbers)
            for Box in self.RandomNumbers[0: self.NumberTry]:
                if Field[Box] == PrisonerNumber:
                    return 1
            return 0

        def Tactic_0_Report(Field, PrisonerNumber):
            shuffle(self.RandomNumbers)
            PrisonerReport = f'{PrisonerNumber}'

            for Box in self.RandomNumbers[0: self.NumberTry]:
                NumberIntoBox = Field[Box]
                PrisonerReport += f'{self.WT}{Box}:{NumberIntoBox}'

                if NumberIntoBox == PrisonerNumber:
                    return 1, PrisonerReport
            return 0, PrisonerReport

        def Tactic_1_Report(Field, PrisonerNumber):
            LastBoxNumber = PrisonerNumber
            PrisonerReport = f'{PrisonerNumber}'

            for Try in range(self.NumberTry):
                NumberIntoBox = Field[LastBoxNumber]
                PrisonerReport += f'{self.WT}{LastBoxNumber}:{NumberIntoBox}'

                if PrisonerNumber == NumberIntoBox:
                    return 1, PrisonerReport

                LastBoxNumber = Field[LastBoxNumber]

            return 0, PrisonerReport

        def Tactic_1(Field, PrisonerNumber):
            LastBoxNumber = PrisonerNumber

            for Try in range(self.NumberTry - 1):
                if PrisonerNumber == Field[LastBoxNumber]:
                    return 1

                LastBoxNumber = Field[LastBoxNumber]

            return 0

        TacticsTypesDict = {
            (1, False): Tactic_1,
            (1, True): Tactic_1_Report,
            (0, False): Tactic_0,
            (0, True): Tactic_0_Report
        }

        return TacticsTypesDict[(self.ExperimentMode, self.DoFullReport)]
