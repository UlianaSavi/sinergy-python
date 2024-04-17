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
            num = int(
                input(
                    "\033[35mВведите число N (Определяет длину массива; 1 ≤ N ≤ 10000): "
                )
            )
            if num <= 0 or num > 10000:
                raise ValueError
            i = 0
            while i < num:
                i += 1
                itemNum = int(input("\n\033[32mВведите целое число: "))
                if itemNum <= 0 or itemNum > 10000:
                    raise ValueError
                self.arr.append(itemNum)
            self.reversedArr = self.arr[::-1]
        except ValueError:
            print(
                "\n\033[33mВы ввели неверные значения (1 ≤ N ≤ 10000), попробуйте снова!\n"
            )
            self.arr = []
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышлииз скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышлииз скрипта. Досвидания!\n")
            sys.exit()


newEx = ReverseArray()
