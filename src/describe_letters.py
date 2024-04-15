import sys


class DescribeLetters:
    answer = {
        "a": False,
        "e": False,
        "i": False,
        "o": False,
        "u": False,
        "y": False,
        "consonant": False,
    }
    letters = ["a", "e", "i", "o", "u", "y"]
    inputNum = 0

    def __init__(self):
        print(
            "\033[32mПривет! Это скрипт, который найдет количество английских гласных и согласных букв, написанных в нижнем регистре в строке\n"
        )
        self.ask()
        print("\n\033[36mОтвет: {}.\n".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input("\033[35mВведите строку: ")
            if inputRes:
                self.getLetters(inputRes)
            else:
                print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
                self.ask()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def getLetters(self, str=""):
        for letter in str:
            if letter in self.letters:
                self.answer[letter] += 1
            else:
                self.answer["consonant"] += 1


newDescribeLetters = DescribeLetters()
