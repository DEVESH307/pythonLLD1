
class SlotRepo:
    def __init__(self):
        self.slots = {}

    def update_slot_status(self, slot,  slotStatus):
        if slot.id not in self.slots:
            raise Exception("Slot does not exist")

        slot.parking_slot_status = slotStatus
        self.slots[slot.id] = slot
        return slot
