# шаблон для скрипта
import sys

class ClassName:
    answer = ""
    inputNum = 0

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input("\033[35mВопрос ")
            print(inputRes)
        except KeyboardInterrupt:
            print("\n\033[33mВы отказались пройти тест. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы отказались пройти тест. Досвидания!\n")
            sys.exit()


newEx = ClassName()
