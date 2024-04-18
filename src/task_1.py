import sys


class FindUniqueNums:
    answer = 0
    maxNumbers = 100000

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            numbersLen = int(
                input(
                    "\033[35mВведите число N – количество чисел (1 ≤ N ≤ {}) ".format(
                        self.maxNumbers
                    )
                )
            )
            if numbersLen <= 0 or numbersLen > self.maxNumbers:
                raise ValueError

            arr = list(
                map(
                    int,
                    input(
                        "Введите {} чисел через пробел (каждое число не превышает 2*10e9 по модулю)".format(
                            numbersLen
                        )
                    ).split(),
                )
            )
            for numItem in arr:
                if numItem > 2 * 10e9:
                    raise ValueError
            if len(arr) != numbersLen:
                raise ValueError
            res = []
            for item in arr:
                if item not in res:
                    res.append(item)

            self.answer = len(res)
        except ValueError:
            print(
                "\n\033[33mВы ввели неверное значение или неверное кол-во значений, попробуйте снова!\n"
            )
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = FindUniqueNums()
