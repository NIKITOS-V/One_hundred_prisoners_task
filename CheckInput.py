from Settings import *


class CheckInput:
    def __init__(self):
        self.CheckType()
        self.CheckValue()

    def CheckType(self):
        try:
            int(Number_Experiments)
            int(Tactic_Number)
            int(Number_Prisoners)
            int(Number_Try)
            int(Print_In_Cmd)
            int(Create_Text_File)
            int(Full_Report_In_Cmd)
            int(Full_Report_In_Text_File)
        except ValueError:
            self.RaiseGenerate('Все значения должны быть целочисленными')

    def CheckValue(self):
        if type(Print_In_Cmd) != type(True):
            self.RaiseGenerate('Переменная Print_In_Cmd должна иметь логический тип данных')
        if Tactic_Number not in [0, 1]:
            self.RaiseGenerate('Переменная Experiment_Mode может принимать только значения: 0, 1')
        if type(Create_Text_File) != type(True):
            self.RaiseGenerate('Переменная Create_Text_File должна иметь логический тип данных')
        if type(Full_Report_In_Cmd) != type(True):
            self.RaiseGenerate('Переменная Full_Report_In_Cmd должна иметь логический тип данных')
        if type(Full_Report_In_Text_File) != type(True):
            self.RaiseGenerate('Переменная Full_Report_In_Text_File должна иметь логический тип данных')
        if Number_Try > Number_Prisoners:
            self.RaiseGenerate('Число попыток не должно быть больше числа заключённых')

    def RaiseGenerate(self, Message):
        raise ValueError(Message)
