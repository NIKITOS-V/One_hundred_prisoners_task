from Settings import *
from Room import Room
from Prisoner import Prisoner
from CheckInput import CheckInput


class Experiment:

    RandomNumbers = [number for number in range(1, Number_Prisoners+1)]

    def __init__(self):
        self.CheckInput = CheckInput()

        self.NumberExperiments = Number_Experiments
        self.ExperimentMode = Experiment_Mode
        self.NumberPrisoners = Number_Prisoners
        self.NumberTry = Number_Try
        self.PrintInCmd = Print_In_Cmd
        self.CrateTextFile = Create_Text_File
        self.ReportInCmd = Full_Report_In_Cmd
        self.ReportInTextFile = Full_Report_In_Text_File

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
        if self.ExperimentMode == 0:
            for PrisonerNumber in range(1, self.NumberPrisoners+1):
                if not self.Prisoner.Choise_0(self.Room.Field, PrisonerNumber):
                    print('\nЭксперимент завершён неудачно')
                    return
            self.GoodResults += 1
            print('\nЭксперимент завершён удачно')

        elif self.ExperimentMode == 1:
            for PrisonerNumber in range(1, self.NumberPrisoners+1):
                if not self.Prisoner.Choise_1(self.Room.Field, PrisonerNumber):
                    print('\nЭксперимент завершён неудачно')
                    return
            self.GoodResults += 1
            print('\nЭксперимент завершён удачно')


Exp = Experiment()
