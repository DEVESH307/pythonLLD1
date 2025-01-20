import datetime

from parkinglot.models.models import Ticket, Vehicle, SlotStatus
from parkinglot.repo.gateRepo import GateRepo
from parkinglot.strtgy.SlotFactory import SlotFactory


class TicketService:
    def __init__(self, gateRepo, vehicleRepo, slotRepo,
                 parkingLotRepo, ticketRepo):
        self.GateRepo = gateRepo
        self.VehicleRepo = vehicleRepo
        self.slotRepo = slotRepo
        self.parkingLotRepo = parkingLotRepo
        self.ticketRepo = ticketRepo

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
        slotStrgy = SlotFactory.get_slot_stgy_obj(gate.parking_lot.slot_assignment_strategy)

        if slotStrgy is None:
            raise Exception("SlotStrgy not found")

        slot = slotStrgy.get_slots(vehicleType, gate.parking_lot)

        if slot is None:
            raise Exception("Slot not found")
        # assign slot to ticket
        ticket.parking_slot = slot

        # block the slot..

        self.slotRepo.update_slot_status(slot, SlotStatus.FILLED)

        # update parking lot counters..
        self.parkingLotRepo.decreaseParkingLotCount(gate.parking_lot)

        # return ticket..
        return self.ticketRepo.save_ticket(ticket)
