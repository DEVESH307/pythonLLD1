from Builder import ComputerBuilder
from compter import Computer


class GamingBuilder(ComputerBuilder):
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.disk = None
        self.gpu = None

    def set_gpu(self, gpu='NVIDIA'):
        if gpu == None:
            raise Exception("No GPU specified")
        self.gpu = gpu
        return self

    def set_cpu(self, cpu='1 core'):
        self.cpu = cpu
        return self

    def set_disk(self, disk='256 SSD'):
        if disk == "HDD":
            raise Exception("No ssd specified")
        self.disk = disk
        return self


    def set_ram(self, ram=10):
        self.ram = ram
        return self


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

    def set_gpu(self, gpu=None):
        self.gpu = gpu
        return self

    def set_cpu(self, cpu=1):
        self.cpu = cpu
        return self

    def set_disk(self, disk='256 HDD'):
        self.disk = disk
        return self

    def set_ram(self, ram=6):
        self.ram = ram
        return self

    def validate(self):
        if self.ram > 16:
            raise Exception("more ram")

    def build(self):
        self.validate()
        return Computer(self.cpu, self.ram, self.disk, self.gpu)
