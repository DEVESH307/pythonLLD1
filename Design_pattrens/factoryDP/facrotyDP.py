from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def ship(self):
        pass

class Packaging(ABC):
    @abstractmethod
    def package(self):
        pass


class Paper(Packaging):
    def package(self):
        print("package via paper")

class plastic(Packaging):
    def package(self):
        print("package via plastic")

class bubble(Packaging):
    def package(self):
        print("package via bubble")

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


class PackingFacroty(ABC):
    @abstractmethod
    def pack(self, weight):
        pass

class RoadPackageFacroty(PackingFacroty):
    def pack(self, weight):
        if weight < 10:
            return Paper().package()
        return bubble().package()

class RoadTransportFactory(Facroty):
    def create_shipment(self, weight):
        if weight < 10:
            return Car()
        return Truck()


class RoadFactory:
    def create_shipment(self, weight):
        RoadTransportFactory.create_shipment()

    def pack(self, weight):
        return RoadPackageFacroty().pack(weight)


class SeaFactory(Facroty):
    def create_shipment(self, weight):
        return Ship()

    def pack(self, weight):
        return plastic().package()


if __name__ == '__main__':
    factory = RoadFactory()
    weight = 10
    factory.pack(weight)
    vehicle = factory.create_shipment(weight)
    vehicle.ship()
