import sys

class Test:
     answer = ''

     def __init__(self):
         self.ask()
         print("\n\033[32mВаш ответ: {}".format(self.answer))
         print("\033[32mСпасибо за прохождение теста! Доствидания!\n")

     def ask(self):
      try:
        # TODO: добавить тест по биологии
        ask = input("\033[35mВопрос 1)\n Ваш ответ: ")
        print(ask)
      except KeyboardInterrupt:
         print("\n\033[33mВы отказались пройти тест. Досвидания!\n")
         sys.exit()
      except:
         print("\n\033[33mВы отказались пройти тест. Досвидания!\n")
         sys.exit()

