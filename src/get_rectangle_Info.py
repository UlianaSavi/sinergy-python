import sys


class GetRectangleInfo:
    sides = {"a": 0, "b": 0}
    activeSide = "a"  # "a" || "b"
    square = 0
    perimeter = 0

    def __init__(self):
        print(
            "\033[32mПривет! Я калькулятор площади и периметра прямоугольника.\nВведите стороны прямоугольника (в см) для произведения вычислений:\n"
        )
        self.ask()
        print(
            "\n\033[32mИтааак, результат! Площадь прямоугольника: {} см. Периметр прямоугольника: {} см.".format(
                round(self.square, 3), round(self.perimeter, 3)
            )
        )
        print("\033[32mСпасибо за использование! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            inputRes = input(
                "\033[35mСколько сантиметров сторона {} ?\n Ваш ответ: ".format(
                    self.activeSide
                )
            )
            isNumber = self.isDigit(inputRes)
            if isNumber:
                self.sides[self.activeSide] = (
                    float(inputRes) if isNumber == "float" else int(inputRes)
                )
                if self.activeSide == "a":
                    self.activeSide = "b"
                    self.ask()
                else:
                    square = self.getSquare()
                    perimeter = self.getPerimeter()
                    self.square = square
                    self.perimeter = perimeter
            else:
                print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
                self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из калькулятора. Досвидания!\n")
            sys.exit()
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()

    def getSquare(self):
        square = self.sides["a"] * self.sides["b"]
        return square

    def getPerimeter(self):
        perimeter = (self.sides["a"]) * 2 + (self.sides["b"]) * 2
        return perimeter

    def isDigit(self, string):
        if string.isdigit():
            return "int"
        else:
            try:
                float(string)
                return "float"
            except ValueError:
                return False


newTriangleInfo = GetRectangleInfo()
