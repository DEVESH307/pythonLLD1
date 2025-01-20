from parkinglot.dtos.IssueTokenRequest import IssueTokenRequest
from parkinglot.dtos.TicketResponse import TicketResponse
from parkinglot.services.TicketService import TicketService


class TicketController:
    def __init__(self, ticketService: TicketService):
        self.ticketService = ticketService

    def issue_ticket(self, request: IssueTokenRequest) -> TicketResponse:
        response= TicketResponse()
        try:
            ticket = self.ticketService.issueTicket(request.vehicleNumber,
                                                request.ownerName, request.gateId,
                                                request.vehicleType)
            response.TicketNumber = ticket.number
            response.SlotNumber = ticket.parking_slot
            response.Vehicle = ticket.vehicle.id
            response.EntryTime = ticket.entry_time
            response.Status = "SUCCESS"
            response.Floor = ticket.parking_slot.parking_floor
            return response
        except Exception as e:
            response.Status = "Failed" + "-" + str(e)
            return response
