import sys


class countDivisor:
    answer = 2  # 1 и само число

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print(
            "\n\033[32mКоличество натуральных делителей числа X: {}".format(self.answer)
        )
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            x = int(input("\n\033[32mВведите натуральное число X: "))
            if x == 1:
                self.answer = 1
                return
            for i in range(2, int(x / 2) + 1):
                if x % i == 0:
                    self.answer += 1
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = countDivisor()
