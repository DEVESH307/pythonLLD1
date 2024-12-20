from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def ship(self):
        pass


# concrete products..
class Truck(Logistics):
    def ship(self):
        print("Truck Ship")


class Car(Logistics):
    def ship(self):
        print("Car Ship")


class Ship(Logistics):
    def ship(self):
        print("Ship via Ship")


#
# class LogisticFactory:
#
#     def create_logisitics(self, type):
#         if type == "ROAD":
#             return car()
#         if type == "SEA":
#             return Ship()


class Facroty(ABC):
    @abstractmethod
    def create_shipment(self, weight):
        pass


class RoadFactory(Facroty):
    def create_shipment(self, weight):
        if weight < 10:
            return Car()
        return Truck()


class SeaFactory(Facroty):
    def create_shipment(self, weight):
        return Ship()


if __name__ == '__main__':
    factory = SeaFactory()
    vehicle = factory.create_shipment(5)
    vehicle.ship()
