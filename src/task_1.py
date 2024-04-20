import sys
import math


class FactorialList:
    factorial = 0
    num = 0
    list = []

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print(
            "\n\033[32mСписок факториалов от числа {} - {}".format(self.num, self.list)
        )
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            num = int(input("\033[35mВведите число, факториал которого будем искать: "))
            self.num = num
            self.getFactorialList(num)
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def getFactorialList(self, num=0):
        self.factorial = math.factorial(num)
        print("\n\033[32mФакториал числа {} это {}".format(self.num, self.factorial))
        list = []
        n = self.factorial
        while n > 0:
            list.append(math.factorial(n))
            n -= 1
        self.list = list
        return list


newEx = FactorialList()
