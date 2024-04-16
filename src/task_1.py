# шаблон для скрипта
import sys


class countZeros:
    answer = []

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[32mВ введенных вами числах нулевых: {}".format(len(self.answer)))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            num = int(input("\n\033[32mВведите целое число N: "))
            i = 0
            while i < num:
                i += 1
                itemNum = input("\n\033[32mВведите целое число {}: ".format(i))
                if int(itemNum) == 0:
                    self.answer.append(int(itemNum))
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


newEx = countZeros()
