import sys


class Invest:
    answer = 0
    minInvestSum = 0
    q = {
        "Введите минимальную сумму инвестиций (больше инвестировать можно сколько угодно). Мин. сумма: (в долларах) ": 0,
        "Введите размер инвестиции инвестора 1 (в долларах): ": 0,
        "Введите размер инвестиции инвестора 2 (в долларах): ": 0,
    }

    def __init__(self):
        print("\033[32mПривет! Для произведения расчетов необходимо:")
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        print("\033[37m")
        sys.exit()

    def ask(self):
        try:
            for question in self.q.keys():
                inputRes = input("\033[35m{}".format(question))
                self.q[question] = int(inputRes)

            self.answer = self.analyse()

        except KeyboardInterrupt:
            print(
                "\n\033[33mВы отказались пройти оценку возможностей инвестирования. Досвидания!\n"
            )
            sys.exit()
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except:
            print(
                "\n\033[33mВы отказались пройти оценку возможностей инвестирования. Досвидания!\n"
            )
            sys.exit()

    def isDigit(self, string):
        if string.isdigit():
            return "int"
        else:
            try:
                float(string)
                return "float"
            except ValueError:
                return False

    def analyse(self):
        # Who can invest:
        # 0 - <no one> |
        # 1 - <only together> |
        # 2 - <everyone> |
        # Name - <name of person who has ability to invest>
        arr = list(self.q.values())
        x = arr[0]  # invest min sum
        a = arr[1]  # first person's money
        b = arr[2]  # second person's money
        if x > a and x > b and x >= (a + b):
            return 0
        if x > a and x > b and x <= (a + b):
            print(123)
            return 1
        if x < a and x < b:
            return 2
        if x < a and x > b:
            return "Первый инвестор"
        if x < b and x > a:
            return "Второй инвестор"
        return 0


newInvest = Invest()
