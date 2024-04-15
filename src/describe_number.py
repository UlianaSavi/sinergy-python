import re
import sys


class DescribeNumber:
    answer = ""
    inputNum = 0

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[36mЭто {} число.\n".format(self.answer))
        print(
            "\033[30mВ случае нечетных чисел вместо фразы <число не является четным> из тз используется приставка не/четное"
        )
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input("\033[35mВведите число: ")
            isNumber = self.isDigit(inputRes)
            if isNumber == "float":
                self.answer = self.getNumStats(float(inputRes))
            if isNumber == "int":
                self.answer = self.getNumStats(int(inputRes))
            if isNumber == False:
                print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
                self.ask()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def getNumStats(self, num):
        stats = {
            "positiveOrNegative": "",
            "evenOrOdd": "",
        }
        res = " "
        if num == 0:
            res = "нулевое"
        else:
            stats["positiveOrNegative"] = (
                "отрицательное" if num < 0 else "положительное"
            )
            stats["evenOrOdd"] = "четное" if (num % 2) == 0 else "нечетное"
        res = res.join(stats.values())

        return res

    def isDigit(self, string):
        if string.isdigit():
            return "int"
        else:
            try:
                float(string)
                return "float"
            except ValueError:
                return False


newDescribeNumber = DescribeNumber()
