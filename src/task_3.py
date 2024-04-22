import sys


class countDivisor:
    answer = []

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print(
            "\n\033[32mВсе четные числа на заданном отрезке: {}".format(
                " ".join(self.answer)
            ),
        )
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            a = int(input("\n\033[32mВведите целое число A: "))
            b = int(
                input("\n\033[32mВведите целое число B (должно быть больше числа A): ")
            )
            if a >= b:
                raise ValueError("ValueError")
            for i in range(a, b + 1, 2):
                evenNum = i % 2 + i
                if evenNum != b and evenNum <= b:
                    self.answer.append(str(evenNum))
            if b % 2 == 0:
                self.answer.append(str(b))
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except ValueError:
            print(
                "\n\033[33mВы ввели неверные значения (либо A < B либо вы ввели строку), попробуйте снова!\n"
            )
            self.ask()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = countDivisor()
