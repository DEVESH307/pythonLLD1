from parkinglot.models.models import ParkingLotStatus


class ParkingLotRepo:
    def __init__(self):
        self.parkingLots = {}

    def decreaseParkingLotCount(self, parkingLot):
        if parkingLot.capacity >= 0:
            parkingLot.capacity -= 1
        if parkingLot.capacity == 0:
            parkingLot.status = ParkingLotStatus.FULL
        self.parkingLots[parkingLot.id] = parkingLot
        return parkingLot
