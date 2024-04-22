import sys


class Poll:
    pets = {}

    def __init__(self):
        self.ask()
        keys = list(self.pets.keys())
        pet = self.pets[
            keys[0]
        ]  # используется чисто в рамках требования по тз задания. Получает единственного питомца из списка pets
        print(
            "Это {} по кличке {}. Возраст питомца: {}. Имя владельца: {}".format(
                pet["breed"], keys[0], self.getAgeSuffix(pet["age"]), pet["ownerName"]
            )
        )
        print("\033[32mСпасибо за прохождение опроса! Досвидания!\n")

    def ask(self):
        try:
            name = input("\033[35mКакая кличка у вашего питомца? Ваш ответ: ")
            if name:
                breed = input(
                    "\033[35mКакой вид и порода у вашего питомца? Ваш ответ: "
                )
            if breed:
                age = int(input("\033[35mКакой возраст у вашего питомца? Ваш ответ: "))
            if age:
                ownerName = input("\033[35mКак вас зовут? Ваш ответ: ")
            if bool(age) and bool(breed) and bool(name) and bool(ownerName):
                self.pets[name] = dict(age=age, breed=breed, ownerName=ownerName)
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def getAgeSuffix(self, age=0):
        ageTypes = ["год", "года", "лет"]
        currAgeType = ageTypes[0]
        lastDigit = int(repr(age)[-1])  # смотрим последнюю цифру числа
        if age > 20:
            if lastDigit == 1:
                currAgeType = ageTypes[0]
            if lastDigit == 2 or lastDigit == 3 or lastDigit == 4:
                currAgeType = ageTypes[1]
            if lastDigit == 0 or lastDigit == 5:
                currAgeType = ageTypes[2]
            if lastDigit >= 5 and lastDigit <= 9:
                currAgeType = ageTypes[2]
        else:
            if age == 1:
                currAgeType = ageTypes[0]
            if age >= 2 and age < 5:
                currAgeType = ageTypes[1]
            if age >= 5 and age <= 20:
                currAgeType = ageTypes[2]
        print(str(age) + " " + currAgeType)
        return str(age) + " " + currAgeType


newPoll = Poll()
