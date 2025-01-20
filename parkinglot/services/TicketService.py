import datetime

from parkinglot.models.models import Ticket, Vehicle
from parkinglot.repo.gateRepo import GateRepo


class TicketService:
    def __init__(self, gateRepo, vehicleRepo):
        self.GateRepo = gateRepo
        self.VehicleRepo = vehicleRepo

    def issueTicket(self, vehicleNumber, ownerName, gate_id, vehicleType):
        # create a ticket's object
        ticket = Ticket(-1, vehicleNumber, entry_time=datetime.datetime.now(),
                        vehicle=None, parking_slot=None, generated_gate=None)

        # Set info like:
        #  Gate No
        gate = self.GateRepo.findGateById(gate_id)
        if gate is None:
            raise Exception("Gate not found")

        ticket.generated_gate = gate
        # Vehicle Info and other info and time stamp..
        vehicle = self.VehicleRepo.findVehicleByNumber(vehicleNumber)
        if vehicle == None:
            vehicle = Vehicle(vehicleNumber, ownerName, vehicleType)
            self.VehicleRepo.saveVehicle(vehicle=vehicle)

        ticket.vehicle = vehicle

        # find a slot..

        # block the slot..

        # update parking lot counters..

        # assign slot to ticket

        # return ticket..
