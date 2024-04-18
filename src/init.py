# шаблон для скрипта
import sys


class ClassName:
    answer = ""

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input("\033[35mВопрос ")
            self.answer = inputRes
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
