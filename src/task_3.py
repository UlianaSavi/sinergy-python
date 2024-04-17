import sys
import math


class getBoads:
    answer = 0

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.answer))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            maxMass = int(
                input(
                    "\033[35mВведите число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка: "
                )
            )
            peopleNum = int(
                input("\033[35mВведите число n (1 ≤ n ≤ 100) - количество рыбаков: ")
            )
            weights = []
            i = 0
            while i < peopleNum:
                i += 1
                weightItem = int(input("\033[35mВес {} путешественника: ".format(i)))
                if weightItem <= 0 or weightItem > maxMass:
                    raise ValueError
                weights.append(weightItem)
            self.answer = math.ceil(sum(weights) / maxMass)
        except ValueError:
            print(
                "\n\033[33mВы ввели неверные значения (1 ≤ вес ≤ m), попробуйте снова!\n"
            )
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()


newEx = getBoads()
