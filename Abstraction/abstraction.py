from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, number_of_tire):
        self.num_of_tires = number_of_tire

    @abstractmethod
    def start(self):
        pass

    # @abstractmethod
    # def stop(self):
    #     pass


# v = Vehicle(1)
#
# print(v.num_of_tires)


class Car(Vehicle):

    def __init__(self, number_of_tire, color):
        super().__init__(number_of_tire)
        self.color = color

    def start(self):
        print("Car is starting")


c = Car(2, "red")


class Bike(Vehicle):

    def __init__(self, number_of_tire, color):
        super().__init__(number_of_tire)
        self.color = color

    def start(self):
        print("bike is starting")


b = Bike(2, "blue")


class abcz(Vehicle):
    def start(self):
        print("abcz is start1")


abx = abcz(1)


def startVehicle(v: Vehicle):
    v.start()


for obj in (c, b, abx):
    startVehicle(obj)
