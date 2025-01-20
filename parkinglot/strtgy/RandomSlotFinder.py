from parkinglot.models.models import VehicleType, ParkingLot, Slot, SlotStatus
from parkinglot.strtgy.SlotStrgy import SlotStrgy


class RandomSlotFinder(SlotStrgy):

    def get_slots(self, vehicleType: VehicleType, parkingLot: ParkingLot) ->Slot:
        for floor in parkingLot.parking_floors:
            if vehicleType in floor.allowed_vehicles:
                for slot in floor.parking_slots_list:
                    if slot.vehicle_type == vehicleType and slot.parking_slot_status == SlotStatus.EMPTY:
                        return slot

        return None
