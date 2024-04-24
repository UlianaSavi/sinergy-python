class Transport:

    def __init__(self, name, maxSpeed, mileage):

        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage

    def seatingCapacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


class Autobus(Transport):
    def seatingCapacity(self, capacity=50):
        return super().seatingCapacity(capacity)


test = Autobus("Renaul Logan", 180, 12)
str = test.seatingCapacity()
print(str)
