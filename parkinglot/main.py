from parkinglot.controller.ticketController import TicketController
from parkinglot.dtos.IssueTokenRequest import IssueTokenRequest
from parkinglot.models.models import ParkingLot, VehicleType, SlotAssignmentStrategyEnum, FloorStatus, Floor, \
    ParkingLotStatus, Slot, SlotStatus, Gate, GateType, GateStatus
from parkinglot.repo.ParkingLotRepo import ParkingLotRepo
from parkinglot.repo.TicketRepo import TicketRepo
from parkinglot.repo.VehicleRepo import VehicleRepo
from parkinglot.repo.gateRepo import GateRepo
from parkinglot.repo.slotRepo import SlotRepo
from parkinglot.services.TicketService import TicketService


def admin(gateRepo, parkingRepo, slotsRepo):
    parking_lot = ParkingLot(
        id=1,
        name="Main Parking Lot",
        address="123 Main St",
        parking_floors=[],
        gates=[],
        allowed_vehicles=[VehicleType.CAR, VehicleType.BIKE],
        capacity=2,
        status=ParkingLotStatus.OPEN,
        slot_assignment_strategy=SlotAssignmentStrategyEnum.RANDOM
    )
    # Create Floor
    floor = Floor(
        id=1,
        parking_slots_list=[],
        floor_number=1,
        floor_status=FloorStatus.OPEN,
        allowed_vehicles=[VehicleType.CAR, VehicleType.BIKE]
    )

    slot1 = Slot(
        id=1,
        slot_number=1,
        vehicle_type=VehicleType.CAR,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor
    )
    slot2 = Slot(
        id=2,
        slot_number=2,
        vehicle_type=VehicleType.BIKE,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor
    )

    floor.parking_slots_list = [slot1, slot2]

    parking_lot.parking_floors = [floor]

    parkingRepo.parkingLots[parking_lot.id] = parking_lot

    gate = Gate(
        id=1,
        gate_number=1,
        gate_type=GateType.ENTRY,
        parking_lot=parking_lot,
        gate_status=GateStatus.OPEN
    )

    parking_lot.gates = [gate]
    gateRepo.gates_map[gate.id] = gate

    slotsRepo.slots[slot1.id] = slot1
    slotsRepo.slots[slot2.id] = slot2


if __name__ == '__main__':
    gate_repo = GateRepo()
    vehicleRepo = VehicleRepo()
    slotRepo = SlotRepo()
    ticketRepo = TicketRepo()
    parkingLotRepo = ParkingLotRepo()

    admin(gate_repo, parkingLotRepo, slotRepo)
    ticketService = TicketService(gate_repo, vehicleRepo, slotRepo, parkingLotRepo,
                                  ticketRepo)

    ticketController = TicketController(ticketService)

    request = IssueTokenRequest("123", "abc",
                                1, VehicleType.CAR)
    response = ticketController.issue_ticket(request)

    print(response.Status)

    request = IssueTokenRequest("1234", "abcd",
                                1, VehicleType.CAR)
    response = ticketController.issue_ticket(request)

    print(response.Status)

    request = IssueTokenRequest("1234", "abcd",
                                1, VehicleType.BIKE)
    response = ticketController.issue_ticket(request)

    print(response.Status)

    request = IssueTokenRequest("1234", "abcd",
                                5, VehicleType.BIKE)
    response = ticketController.issue_ticket(request)

    print(response.Status)

    request = IssueTokenRequest("1234", "abcd",
                                1, VehicleType.BIKE)
    response = ticketController.issue_ticket(request)

    print(response.Status)
