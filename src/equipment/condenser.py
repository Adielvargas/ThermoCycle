from .equipment import Equipment

class Condenser(Equipment):
    def __init__(self, name):
        super().__init__(name)
        self.work = 0.0

    def calculate(self):
        self.heat = self.enthalpy_balance
