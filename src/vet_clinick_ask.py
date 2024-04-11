class Poll:
     answer = {
        "breed": '',
        "name": '',
        "age": '',
     }

     def __init__(self):
         self.ask()
         print("Это {} по кличке {}. Возраст: {}".format(self.answer["breed"], self.answer["name"], self.answer["age"]))
         print("Спасибо за прохождение опроса! Доствидания!")

     def ask(self):
      breed = input("\033[37mКакой вид и порода у вашего питомца? (Нажмите enter для отказа от прохождения отпроса)\n Ваш ответ: ")
      if breed:
         self.answer["breed"] = breed
         name = input("\033[37mКакая кличка у вашего питомца? (Нажмите enter для отказа от прохождения отпроса)\n Ваш ответ: ")
      if name:
         self.answer["name"] = name
         age = input("\033[37mКакой возраст у вашего питомца? (Нажмите enter для отказа от прохождения отпроса)\n Ваш ответ: ")
      if age:
         self.answer["age"] = age
      else:
         self.answer = "Вы отказались пройти отпрос. Досвидания!"

