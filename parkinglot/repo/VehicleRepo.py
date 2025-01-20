class VehicleRepo:
    def __init__(self):
        self.vehicleMap = {}

    def findVehicleByNumber(self, number):
        if number not in self.vehicleMap:
            return None
        return self.vehicleMap[number]

    def saveVehicle(self, vehicle):
        self.vehicleMap[vehicle.id] = vehicle
