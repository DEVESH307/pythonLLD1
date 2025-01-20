
class GateRepo:
    def __init__(self):
        self.gates_map = {}

    def findGateById(self, gateId):
        return self.gates_map.get(gateId, None)