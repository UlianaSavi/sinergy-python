# шаблон для скрипта
import sys


class Palindrome:
    answer = "no"  # no | yes
    inputNum = 0

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input("\033[35mВведите строку для проверки на палиндром: ")
            self.answer = self.isPalindrome(inputRes.replace(" ", ""))
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def isPalindrome(self, str=""):
        res = "no"
        reversedStr = str[::-1]
        if str == reversedStr:
            res = "yes"
        return res


newEx = Palindrome()
