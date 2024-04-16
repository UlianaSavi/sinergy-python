# шаблон для скрипта
import sys


class DeleteSpaces:
    answer = ""
    inputNum = 0
    maxInputLen = 1000

    def __init__(self):
        print(
            "\033[32mПривет! Этот скрипт удалит все лишние пробелы из строки. Максимальная длина строки 1000 символов.\n"
        )
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input("\033[35mВведите строку для преобразования: ")
            if len(inputRes) > self.maxInputLen:
                raise ValueError("ValueError")
            self.answer = " ".join(inputRes.split())
        except ValueError:
            print(
                "\n\033[33mВы ввели неверные значения (строка превышает 1000 символов), попробуйте снова!\n"
            )
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = DeleteSpaces()
