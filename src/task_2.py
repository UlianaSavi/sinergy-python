import sys


class ReverseArray:
    arr = []
    reversedArr = []
    inputNum = 0

    def __init__(self):
        print("\033[32mПривет! Этот скрипт разворачивает массив.\n")
        self.ask()
        print(
            "\n\033[32mВы ввели: {}, скрипт развернул: {}".format(
                self.arr, self.reversedArr
            )
        )
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            num = int(input("\033[35mВведите число N (Определяет длину массива): "))
            if num <= 0 or num > 100000:
                raise ValueError

            numItem = input("\033[35mВведите через пробел {} чисел (1 ≤ Ai ≤ 10e9): ")
            self.arr = [int(item) for item in numItem.split()]
            if len(self.arr) > num:
                raise ValueError
            for x in self.arr:
                if int(x) <= 0 or int(x) > 10e9:
                    raise ValueError
            self.moveToFirst()
        except ValueError:
            print(
                "\n\033[33mВы ввели неверные значения (1 ≤ N ≤ 10000) или ввели больше чисел, чем N({}), попробуйте снова!\n".format(
                    num
                )
            )
            self.arr = []
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышлииз скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышлииз скрипта. Досвидания!\n")
            sys.exit()

    def moveToFirst(self):
        self.reversedArr += self.arr
        self.reversedArr.insert(0, self.reversedArr.pop())


newEx = ReverseArray()
