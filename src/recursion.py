import sys


class Recursion:
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # дано по тз

    def __init__(self):
        self.tryNum = 1
        print("\033[32mПривет!\n")
        self.printList(self.tryNum)
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def printList(self, num):
        print(num)
        if self.tryNum >= (len(self.list) - 1):
            print("Конец списка, если выводить больше нечего.")
            return
        else:
            self.tryNum += 1
            self.printList(self.list[self.tryNum])


newEx = Recursion()
