import sys


class ClassName:
    answer = {}

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        for key in self.answer:
            print("\036 {}: {}".format(key, self.answer[key]))
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
            res = []
            for item in arr:
                if item not in res:
                    res.append(item)
                    self.answer[item] = "NO"
                else:
                    self.answer[item] = "YES"
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
