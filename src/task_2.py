import math


class Turtle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.s = 2

    def goUp(self):
        self.y = self.y + self.s

    def goDown(self):
        self.y = self.y - self.s

    def goLeft(self):
        self.x = self.x - self.s

    def goRight(self):
        self.x = self.x + self.s

    def evolve(self):
        self.s = self.s + 1

    def degrade(self):
        num = self.s - 1
        if num <= 0:
            raise ValueError(
                f"s не может быть меньше или равна нулю! Сейчас s = {self.s}"
            )
        self.s = num

    def countMoves(self, x2, y2):
        num = math.ceil(abs(x2 - self.x) / self.s + abs(y2 - self.y) / self.s)
        print(f"Черепашка может добраться до {x2};{y2}; за {num} ходов")
        return num


newEx = Turtle()

newEx.countMoves(4, 4)
newEx.countMoves(2, 10)
newEx.countMoves(2.3, 10)
