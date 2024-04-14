import sys


class NumericalManipulations:
    inputValueRequaredLen = 5  # пятизначное число
    resultValue = 0
    inputValue = 0

    def __init__(self):
        print(
            "\033[32mПривет! Чтобы произвести манипуляции, введите пятизначное число:\n"
        )
        self.resultValue = self.ask()
        if self.resultValue:
            print("\n\033[32mВаш результат: {}".format(self.resultValue))
            print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input("\033[35mВведите число ")
            if inputRes.isdigit() & (len(inputRes) == self.inputValueRequaredLen):
                return self.getNumber(inputRes)
            else:
                print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
                return self.ask()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def getNumber(self, input="12345"):
        tensOfThousands = int(input[0])  # десятки тысяч
        thousands = int(input[1])  # тысячи
        hundreds = int(input[2])  # сотни
        tens = int(input[3])  # десятки
        units = int(input[4])  # еденицы
        res = (tens**units) * hundreds / (tensOfThousands - thousands)
        return res


newNumericalManipulations = NumericalManipulations()
