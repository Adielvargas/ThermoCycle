from .equipment import Equipment

class Pump(Equipment):
    def __init__(self, name):
        super().__init__(name)
        self.work = 0.0

    def calculate(self):
        self.work = - self.enthalpy_balance
