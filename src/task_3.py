import sys


class ClassName:
    answer = {}

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            arr = list(
                map(
                    int,
                    input(
                        "\033[35mВведите последовательность чисел через пробел: "
                    ).split(),
                )
            )
            for item in arr:
                repeatNum = arr.count(item)
                if repeatNum == 1:
                    print("{} --> NO".format(item))
                    self.answer[item] = "NO"
                else:
                    print("{} --> YES".format(item))
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = ClassName()
