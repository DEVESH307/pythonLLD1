from Builder import ComputerBuilder
from compter import Computer


class GamingBuilder(ComputerBuilder):
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.disk = None
        self.gpu = None

    def set_gpu(self, gpu):
        if gpu == None:
            raise Exception("No GPU specified")
        self.gpu = gpu

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_disk(self, disk='256 SSD'):
        if disk == "HDD":
            raise Exception("No ssd specified")
        self.disk = disk

    def set_ram(self, ram):
        self.ram = ram

    def validate(self):
        if self.ram < 8:
            raise Exception("less ram")

    def build(self):

        return Computer(self.cpu, self.ram, self.disk, self.gpu)


class OfficeBuilder(ComputerBuilder):
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.disk = None
        self.gpu = None

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_disk(self, disk='256 HDD'):
        self.disk = disk

    def set_ram(self, ram):
        self.ram = ram

    def validate(self):
        if self.ram > 16:
            raise Exception("more ram")

    def build(self):
        self.validate()
        return Computer(self.cpu, self.ram, self.disk, self.gpu)
