import copy

from Design_pattrens.prototype.Mosntor import Monstor



class sword:
    def __init__(self, val):
        self.val =val


class Zombie(Monstor):
    def __init__(self, health, sword):
        self.health = health
        self.sword = sword

    def attack(self):
        print("Attack")

    def clone(self):
        return copy.deepcopy(self)
