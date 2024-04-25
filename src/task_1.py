import math


class CashRegister:

    def __init__(self):
        self.money = 10000

    def topUp(self, x: int) -> int:
        newSum = self.money + x
        if x < 0:
            raise ValueError("Вы ввели отрицательное значение.")
        self.money = newSum
        print(f"Вы добавили в кассу {x}, теперь в кассе: {newSum}")
        return newSum

    def countThousand(self) -> int:
        res = math.floor(self.money / 1000)
        print(f"В кассе {res} целых тысяч")
        return res

    def takeAway(self, x: int) -> int:
        ostatok = self.money - x
        if ostatok < 0:
            raise ValueError("В кассе недостаточно денег.")
        self.money = ostatok
        print(f"Вы забрали из кассы {x}, осталось: {ostatok}")
        return ostatok


cash = CashRegister()
cash.topUp(20)
cash.takeAway(10)
cash.countThousand()
