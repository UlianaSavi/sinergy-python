import sys

class GetRectangleInfo:
     sides = { "a": 0, "b": 0 }
     activeSide = "a" # "a" || "b"
     square = 0
     perimeter = 0

     def __init__(self):
         print("\033[32mПривет! Я калькулятор площади и периметра прямоугольника.\nВведите стороны прямоугольника (в см) для произведения вычислений:\n")
         self.ask()
         print("\n\033[32mИтааак, результат! Площадь прямоугольника: {}. Периметр прямоугольника: {}.".format(self.square, self.perimeter))
         print("\033[32mСпасибо за использование! Досвидания!\n")
         sys.exit()

     def ask(self):
      try:
        inputRes = input("\033[35mСколько сантиметров сторона {} ?\n Ваш ответ: ".format(self.sides[self.activeSide]))
        if inputRes & (isinstance(inputRes, float) | isinstance(inputRes, int)): # проверяем является ли ввод числом
           self.sides[self.activeSide] = inputRes
           self.activeSide += "b"
           if self.activeSide != "b":
              self.ask()
           else:
              square = self.getSquare()
              perimeter = self.getPerimeter()
              self.square = square
              self.perimeter = perimeter
        else:
           print("\n\033[33mВведено не числовое значение, пожалуйста повторите ввод.\n")
           self.ask()

      except KeyboardInterrupt:
         print("\n\033[33mВы вышли из калькулятора. Досвидания!\n")
         sys.exit()
      except:
         print("\n\033[33mВы вышли из калькулятора. Досвидания!\n")
         sys.exit()

     def getSquare(self):
         square = self.sides["a"] * self.sides["b"]
         return square

     def getPerimeter(self):
         perimeter = (self.sides["a"] + self.sides["b"])**2
         return perimeter


newTriangleInfo = GetRectangleInfo()
