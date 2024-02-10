from Settings import *
from Room import Room
from Prisoner import Prisoner
from CheckInput import CheckInput
from Report import Report


class Experiment:

    RandomNumbers = [number for number in range(1, Number_Prisoners+1)]

    def __init__(self):
        self.NumberExperiments = Number_Experiments
        self.NumberPrisoners = Number_Prisoners

        self.GoodResults = 0
        self.DoFullReport = Full_Report_In_Text_File or Full_Report_In_Cmd

        self.Room = Room(self.RandomNumbers)
        self.Prisoner = Prisoner(self.RandomNumbers, Number_Try, Tactic_Number, self.DoFullReport)
        self.Report = Report()

        self.StartExperiment()

    def StartExperiment(self):
        if self.DoFullReport:
            self.Experiment = self.ExperimentWithReport
        else:
            self.Experiment = self.ExperimentWithOutReport

        for ExperimentNumber in range(1, self.NumberExperiments+1):
            self.Room.GenerateField()
            self.Experiment()

        self.Report.SaveSimulationResult(self.GoodResults)
        self.Report.PrintReport()

    def ExperimentWithReport(self):
        for PrisonerNumber in range(1, self.NumberPrisoners+1):
            PrisonerResult = self.Prisoner.EnteringTheRoom(self.Room.Field, PrisonerNumber)

            self.Report.SavePrisonerResult(PrisonerResult)

            if not PrisonerResult[0]:
                self.Report.SaveExperimentResult(0)
                return

        self.GoodResults += 1

        self.Report.SaveExperimentResult(1)

    def ExperimentWithOutReport(self):
        for PrisonerNumber in range(1, self.NumberPrisoners+1):
            PrisonerResult = self.Prisoner.EnteringTheRoom(self.Room.Field, PrisonerNumber)

            if not PrisonerResult:
                return

        self.GoodResults += 1


ChkInp = CheckInput()
Exp = Experiment()
