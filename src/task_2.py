import sys


class GetListsCount:
    answer = ""
    maxListLen = 100000

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print(
            "\n\033[32mКоличество чисел в пересечении множеств: {}".format(self.answer)
        )
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        # try:
        list1 = set()
        list2 = set()
        list1Item = input(
            "\033[35mВведите целые числа ПЕРВОГО списка через пробел. Максимальное кол-во чисел - {} ".format(
                self.maxListLen
            ),
        )
        arr1 = map(int, list1Item.split())
        list1 = set(arr1)

        list2Item = input(
            "\033[35mВведите целые числа ВТОРОГО списка через пробел. Максимальное кол-во чисел - {} ".format(
                self.maxListLen
            ),
        )
        arr2 = map(int, list2Item.split())
        list2 = set(arr2)
        intersection = list1 & list2
        self.answer = len(intersection)

    # except KeyboardInterrupt:
    #     print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
    #     sys.exit()
    # except ValueError:
    #     print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
    #     self.ask()
    # except:
    #     print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
    #     sys.exit()


newEx = GetListsCount()
