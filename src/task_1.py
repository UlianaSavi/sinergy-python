class Transport:

    def __init__(self, name, maxSpeed, mileage):

        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage


class Autobus(Transport):
    def displayParentInfo(self):
        print(
            "Название автомобиля: {} Скорость: {} Пробег: {}".format(
                self.name, self.maxSpeed, self.mileage
            )
        )


n = Autobus("Renaul Logan ", 180, 12).displayParentInfo()
