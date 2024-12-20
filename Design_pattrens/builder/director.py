from Builder import ComputerBuilder
from ConcereteBuilders import GamingBuilder, OfficeBuilder


class Director:
    def __init__(self):
        self.gb = GamingBuilder()
    def construct_gaming(self, ram=None, cpu=None, gpu=None, disk=None):
        return (self.gb.set_gpu("10")
                .set_cpu(cpu)
                .set_ram(ram)
                .set_disk(disk).build())

    def construct_office(self, disk=None, cpu='1', storage=6):
        of = OfficeBuilder()
        return (of
                .set_cpu(cpu)
                .set_ram(storage)
                .set_disk(disk).build()
                )

