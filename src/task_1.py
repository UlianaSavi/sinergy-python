class Transport:

    def __init__(self, name, maxSpeed, mileage):

        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage


Autobus = Transport("Renaul Logan", 180, 12)
print(
    f"Название автомобиля: {Autobus.name} Скорость: {Autobus.maxSpeed} Пробег: {Autobus.mileage}"
)
