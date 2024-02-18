from Settings import *


class CheckInput:
    def __init__(self):

        def RaiseGenerate(Message):
            raise ValueError(Message)

        def BoolMessageGenerate(var):
            return f'Переменная {var} должна иметь логический тип данных'

        def IntMessageGenerate(var):
            return f'Переменная {var} должна иметь целочисленное значение'

        if type(Number_Experiments) != int:
            RaiseGenerate(IntMessageGenerate('Number_Experiments'))

        if type(Tactic_Number) != int:
            RaiseGenerate(IntMessageGenerate('Tactic_Number'))

        if type(Number_Prisoners) != int:
            RaiseGenerate(IntMessageGenerate('Number_Prisoners'))

        if type(Number_Try) != int:
            RaiseGenerate(IntMessageGenerate('Number_Try'))

        if Number_Experiments <= 0:
            RaiseGenerate('Значение переменной Number_Experiments должно быть больше нуля')

        if Tactic_Number not in [0, 1]:
            RaiseGenerate('Переменная Experiment_Mode может принимать только значения: 0, 1')

        if Number_Try > Number_Prisoners:
            RaiseGenerate('Значение переменной Number_Try не должно быть больше значения переменной Number_Prisoners')

        elif Number_Try < 0:
            RaiseGenerate('Значение переменной Number_Try должно быть неотрицательным')

        if type(Print_In_Cmd) != bool:
            RaiseGenerate(BoolMessageGenerate('Print_In_Cmd'))

        if type(Create_Text_File) != bool:
            RaiseGenerate(BoolMessageGenerate('Create_Text_File'))

        if type(Full_Report_In_Cmd) != bool:
            RaiseGenerate(BoolMessageGenerate('Full_Report_In_Cmd'))

        if type(Full_Report_In_Text_File) != bool:
            RaiseGenerate(BoolMessageGenerate('Full_Report_In_Text_File'))
