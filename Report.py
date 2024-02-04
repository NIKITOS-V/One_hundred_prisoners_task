from Settings import *
from datetime import datetime

class Report:
    Tab = '\t'
    NL = '\n'

    def __init__(self):
        self.ReportForTextFile = ''
        self.ReportForCmd = ''
        self.Report = ''

    def SavePrisonerResult(self, PrisonerResult):
        PrisonerReport = PrisonerResult[1].split()

        String = f'{self.NL + self.Tab}Номер заключённого: {PrisonerReport[0]}{self.NL}'

        for BoxAndList in PrisonerReport[1:]:
            Box, List = BoxAndList.split(':')
            String += f"{self.NL + self.Tab * 2}Номер коробки: {Box}, Номер на листе: {List}"

        String += f'{self.NL * 2 + self.Tab}{"Номер найден" if PrisonerResult[0] else "Номер не найден"}{self.NL * 2}'
        self.Report += String

    def SaveExperimentResult(self, Result):
        if Result:
            self.Report += f'{self.NL}Эксперимент завершён удачно{self.NL*2}'

        else:
            self.Report += f'{self.NL}Эксперимент завершён неудачно{self.NL*2}'

    def SaveSimulationResult(self, GoodResult):
        SimulationResult = (f'Номер тактики: {Tactic_Number}'
                            f'{self.NL*2}Кол-во экспериментов: {Number_Experiments}'
                            f'{self.NL*2}Удачных исходов: {GoodResult}'
                            f'{self.NL*2}Неудачных исходов: {Number_Experiments - GoodResult}'
                            f'{self.NL*2}Шанс На успех: {GoodResult/Number_Experiments * 100} %')

        if Full_Report_In_Cmd:
            self.ReportForCmd = (f'{self.Report}{self.NL}'
                                 f'{self.NL}{"-"*20}{self.NL*4}'
                                 f'{self.NL}{SimulationResult}')
        else:
            self.ReportForCmd = SimulationResult

        if Full_Report_In_Text_File:
            self.ReportForTextFile = (f'{SimulationResult}{self.NL*4}{"-"*20}{self.NL}'
                                      f'{self.NL}{self.Report}')
        else:
            self.ReportForTextFile = SimulationResult

    def PrintReport(self):
        if Print_In_Cmd:
            print(self.ReportForCmd)

        if Create_Text_File:
            NowTime = datetime.now()
            FileName = f'{NowTime.year}-{NowTime.month}-{NowTime.day}_{NowTime.hour}-{NowTime.minute}-{NowTime.second}'

            with open(f'Results\\{FileName}.txt', 'w', encoding='UTF-8') as File:
                File.write(self.ReportForTextFile)
