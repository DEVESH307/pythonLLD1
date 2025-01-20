from parkinglot.models.models import SlotAssignmentStrategyEnum
from parkinglot.strtgy.RandomSlotFinder import RandomSlotFinder


class SlotFactory:

    @staticmethod
    def get_slot_stgy_obj(slotStrgyEnum):
        if slotStrgyEnum == SlotAssignmentStrategyEnum.RANDOM:
            return RandomSlotFinder()