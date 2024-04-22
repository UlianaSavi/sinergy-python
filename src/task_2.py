import sys
import collections


class VetClinic:
    pets = {
        1: {
            "Кики": {
                "breed": "Собака",
                "age": 9,
                "ownerName": "Зоя",
            },
        },
        2: {
            "Каа": {
                "breed": "желторотый питон",
                "age": 19,
                "ownerName": "Саша",
            },
        },
    }

    def __init__(self):
        print("\033[32mПривет!\n")
        self.ask()
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            commands = ["create", "read", "update", "delete", "stop"]
            command = commands[0]
            while command != commands[4]:  # stop
                inputRes = input(
                    "\033[35mВведите одну из команд для взаимодействия с базой - create, read, update, delete: "
                )
                command = inputRes
                if command == commands[0]:
                    self.create(self.inputDataForNewItem())
                if command == commands[1]:
                    name = input(
                        "\033[35mВведите кличку питомца для получения информации: "
                    )
                    self.read(name)
                if command == commands[2]:
                    name = input(
                        "\033[35mВведите кличку питомца для обновления информации: "
                    )
                    self.update(name, self.inputDataForNewItem(name))
                if command == commands[3]:
                    name = input(
                        "\033[35mВведите кличку питомца для удаления информации о нем: "
                    )
                    self.delete(name)
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def create(self, newPet={}):
        last = collections.deque(self.pets, maxlen=1)[0]  # последний ключ
        self.pets[last + 1] = newPet

    def read(self, name=""):
        pet = self.pets[name]
        print(
            "Это {} по кличке {}. age: {}. ownerName: {}".format(
                pet["breed"], name, self.getAgeSuffix(pet["age"]), pet["ownerName"]
            )
        )

    def update(self, name, petValue):  # TODO
        arr = self.petsList()
        self.pets.update({name: petValue})

    def delete(self, name=""):  # TODO
        arr = self.petsList()
        arr.pop(id)

    def getPet(self, id=""):  # TODO
        return self.pets[id] if id in self.pets.keys() else False

    def getAgeSuffix(self, age=0):
        ageTypes = ["год", "года", "лет"]
        currAgeType = ageTypes[0]
        lastDigit = int(repr(age)[-1])  # смотрим последнюю цифру числа
        if lastDigit == 1:
            currAgeType = ageTypes[0]
        if lastDigit == 2 or lastDigit == 3 or lastDigit == 4:
            currAgeType = ageTypes[1]
        if lastDigit == 0 or lastDigit == 5:
            currAgeType = ageTypes[2]
        return str(age) + " " + currAgeType

    def inputDataForNewItem(name=False):
        pet = {}
        if name == False:
            name = input("\033[35mКакая кличка у вашего питомца? Ваш ответ: ")
        if name:
            breed = input("\033[35mКакой вид и порода у вашего питомца? Ваш ответ: ")
        if breed:
            age = int(input("\033[35mКакой возраст у вашего питомца? Ваш ответ: "))
        if age:
            ownerName = input("\033[35mКак вас зовут? Ваш ответ: ")
        if bool(age) and bool(breed) and bool(name) and bool(ownerName):
            pet[name] = dict(age=age, breed=breed, ownerName=ownerName)
        return pet

    def petsList(self):
        return list(self.pets.values())


newEx = VetClinic()
