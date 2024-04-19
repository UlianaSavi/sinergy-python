import sys


class GenerateDict:
    answer = {}

    def __init__(self):
        print("\033[32mПривет! Давайте сгенерируем словарь.\n")
        print(
            "\033[35mЗначениями ключей будут сами ключи возведённые в степень чисел ключей.\n"
        )
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            start = int(
                input("\033[35mВведите начальное число генерируемого словаря: ")
            )
            if start:
                end = int(
                    input("\033[35mВведите конечное число генерируемого словаря: ")
                )
            if bool(start) and bool(end):
                i = start
                while i <= end:
                    self.answer[i] = i**i
                    i += 1
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = GenerateDict()
