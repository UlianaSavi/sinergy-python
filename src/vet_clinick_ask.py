import sys

class Poll:
     answer = {
        "breed": '',
        "name": '',
        "age": '',
     }

     def __init__(self):
         self.ask()
         print("\n\033[32mЭто {} по кличке {}. Возраст: {}".format(self.answer["breed"], self.answer["name"], self.answer["age"]))
         print("\033[32mСпасибо за прохождение опроса! Доствидания!\n")

     def ask(self):
      try:
        breed = input("\033[35mКакой вид и порода у вашего питомца? \033[37m(Нажмите enter для отказа от прохождения отпроса)\n Ваш ответ: ")
        if breed:
            self.answer["breed"] = breed
            name = input("\033[35mКакая кличка у вашего питомца? \033[37m(Нажмите enter для отказа от прохождения отпроса)\n Ваш ответ: ")
        if name:
            self.answer["name"] = name
            age = input("\033[35mКакой возраст у вашего питомца? \033[37m(Нажмите enter для отказа от прохождения отпроса)\n Ваш ответ: ")
        if age:
            self.answer["age"] = age
      except KeyboardInterrupt:
         print("\n\033[33mВы отказались пройти отпрос. Досвидания!\n")
         sys.exit()
      except:
         print("\n\033[33mВы отказались пройти отпрос. Досвидания!\n")
         sys.exit()

