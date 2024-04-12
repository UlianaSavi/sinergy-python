import sys

class Test:
     developmentalStagesLen = 6 # константное число стадий развития человека

     answer = ''
     tryNum = 0
     inputArr = []

     def __init__(self):
         print("\033[32mПривет! Вам предстоит пройти тест по биологии: нужно последовательно ввести стадии развития человека, начнем!\n")
         self.ask()
         print("\n\033[32mВаш ответ: {}".format(self.answer))
         print("\033[32mСпасибо за прохождение теста! Доствидания!\n")
         sys.exit()

     def ask(self):
      try:
        inputRes = input("\033[35mКакая стадия распложилась под номером {} ?\n Ваш ответ: ".format(self.tryNum + 1))
        if inputRes:
           self.inputArr.append(inputRes)
           self.tryNum += 1
           if self.tryNum < self.developmentalStagesLen:
              self.ask()
           else:
              result = ' => '.join(self.inputArr)
              self.answer = result
        else:
           sys.exit() 

      except KeyboardInterrupt:
         print("\n\033[33mВы отказались пройти тест. Досвидания!\n")
         sys.exit()
      except:
         print("\n\033[33mВы отказались пройти тест. Досвидания!\n")
         sys.exit() 

newTest = Test()
