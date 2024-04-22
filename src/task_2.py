import sys
import collections


class VetClinic:
    pets = {
        "+71111111111": {
            "Кики": {
                "breed": "Собака",
                "age": 4,
                "ownerName": "Зоя",
            },
        },
        "+79999999999": {
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
            while command != commands[4]:
                number = input(
                    "\033[35mВведите ваш номер телефона для идентификации: "
                ).strip()
                registered = self.getPet(number)
                ownerName = (
                    list(self.getPet(number).values())[0]["ownerName"]
                    if registered
                    else "неизвестный"
                )
                print("Привет {}!".format(ownerName))
                if registered:
                    inputRes = input(
                        "\033[35mВведите одну из команд для взаимодействия с базой - create, read, update, delete: "
                    ).strip()
                else:
                    print(
                        "Введите одну из команд для взаимодействия с базой - create, read, update, delete:"
                    )
                    inputRes = input(
                        "\033[35mТак как вы не зарегистрированы в нашей базе данных, вам доступен только один метод - create. Введите его для продолжения: "
                    ).strip()
                command = inputRes
                if command == commands[0]:
                    newNumber = input(
                        "\033[35mВведите новый номер телефона для создания записи (запомните этот номер - по нему вы будете идентифицироваться): "
                    ).strip()
                    check = self.getPet(newNumber)
                    if check:
                        print(
                            "\033[33mПитомец зарегистрированный под этим номером уже есть. Пожалуйста, введите новую иформацию."
                        )
                        print("\033[33mВы ввели: {}".format(number))
                    else:
                        data = self.inputDataForNewItem()
                        self.create(newNumber, data)
                if registered:
                    if command == commands[1]:
                        self.read(number)
                    if command == commands[2]:
                        self.update(number, self.inputDataForNewItem())
                    if command == commands[3]:
                        self.delete(number)
            if command == commands[4]:
                raise KeyboardInterrupt("")
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def create(self, number, newPet={}):
        # last = collections.deque(self.pets, maxlen=1)[0]  # последний ключ
        # self.pets[last + 1] = newPet # по тз выглядело бы так
        self.pets[number] = newPet  # решение по id как number
        print("\033[32mНовый питомец благополучно добавлен!")
        print(self.pets)

    def read(self, number=""):
        pet = self.getPet(number)
        if pet:
            petVal = list(self.getPet(number).values())[0]
            petName = list(self.getPet(number).keys())[0]
            print(
                "Это {} по кличке {}. Возраст питомца: {}. Имя владельца: {}".format(
                    petVal["breed"],
                    petName,
                    self.getAgeSuffix(petVal["age"]),
                    petVal["ownerName"],
                )
            )
        else:
            print(
                "\033[33mПитомца записанного под таким номером не найдено. Проверьте правильность написания номера."
            )
            print("\033[33mВы ввели: {}".format(number))

    def update(self, id, newValue={}):
        self.pets[id] = newValue
        print("\033[32mИнформация успешно обновлена!")
        print(self.pets)

    def delete(self, number=""):
        self.pets.pop(number)
        print("\033[32mИнформация успешно удалена!")
        print(self.pets)

    def getPet(self, number=""):
        res = False
        if number in self.pets.keys():
            id = list(self.pets.keys()).index(number)
            res = list(self.pets.values())[id]
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

    def inputDataForNewItem(self):
        pet = {}
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

    def petsValuesList(self):
        return list(self.pets.values())


newEx = VetClinic()
