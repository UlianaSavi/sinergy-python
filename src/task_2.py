import sys


class GetListsCount:
    answer = ""
    maxListLen = 100000

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print(
            "\n\033[32m{} чисел содержится одновременно как в первом списке, так и во втором.".format(
                self.answer
            )
        )
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            list1 = []
            list2 = []
            endedOne = False
            endedTwo = True
            while endedOne == False:
                list1Item = input(
                    "\033[35mВведите целые числа ПЕРВОГО списка (чтобы закончить ввод напишите end)). Максимальное кол-во чисел - {} ".format(
                        self.maxListLen
                    ),
                )
                if list1Item == "end":
                    endedOne = True
                    endedTwo = False
                    print("\n")
                else:
                    list1.append(int(list1Item))
            while endedTwo == False:
                list2Item = input(
                    "\033[35mВведите целые числа ВТОРОГО списка (чтобы закончить ввод напишите end)). Максимальное кол-во чисел - {} ".format(
                        self.maxListLen
                    ),
                )
                if list2Item == "end":
                    endedTwo = True
                else:
                    list2.append(int(list2Item))
                self.answer = len(list1) + len(list2)
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = GetListsCount()
