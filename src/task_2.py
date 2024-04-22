import sys
import collections


class VetClinic:
    pets = {
        1: {
            "Кики": {
                "breed": "Собака",
                "age": 4,
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
                    data = self.inputDataForNewItem()
                    self.create(data)
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

    def create(self, newPet={}):
        last = collections.deque(self.pets, maxlen=1)[0]  # последний ключ
        self.pets[last + 1] = newPet
        print(
            "\033[32mНовый элемент в словарь добавлен благополучно: \n{}".format(
                self.pets
            )
        )

    def read(self, name=""):
        petInArr = self.getPet(name)
        if petInArr:
            res = petInArr
            print(
                "Это {} по кличке {}. Возраст питомца: {}. Имя владельца: {}".format(
                    res["breed"], name, self.getAgeSuffix(res["age"]), res["ownerName"]
                )
            )
        else:
            print(
                "\033[33mПитомца с такой кличкой нет в нашей клинике. Проверьте правильность написания клички питомца."
            )
            print("\033[33mВы ввели: {}".format(name))

    def update(self, name, petValue):
        petInArr = self.getPet(name)
        if petInArr:
            self.pets.update(
                {name: petValue}
            )  # TODO тут нужно получить idшник для обновления типа 1, 2 и тд
        else:
            print(
                "\033[33mПитомца с такой кличкой нет в нашей клинике. Проверьте правильность написания клички питомца."
            )
            print("\033[33mВы ввели: {}".format(name))

    def delete(self, name=""):  # TODO
        arr = self.petsList()
        arr.pop(id)

    def getPet(self, name=""):
        arr = self.petsList()
        res = False
        for i in arr:
            if name == list(i.keys())[0]:
                res = list(i.values())[0]
        return res

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
        return str(age) + " " + currAgeType

    def inputDataForNewItem(self, name=False):
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
