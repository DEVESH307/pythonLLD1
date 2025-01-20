from abc import ABC, abstractmethod

from parkinglot.models.models import VehicleType, Slot, ParkingLot


class SlotStrgy(ABC):

    @abstractmethod
    def get_slots(self, vehicleType: VehicleType, parkingLot: ParkingLot) ->Slot:
        pass