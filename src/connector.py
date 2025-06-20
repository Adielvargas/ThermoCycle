class Connector:
    def __init__(self, name):
        self.name = name
        self.property_in = None
        self.property_out = None
        self.equipment_in = None
        self.equipment_out = None

    def add_equipment_in(self, equipment):
        self.equipment_in = equipment

    def add_equipment_out(self, equipment):
        self.equipment_out = equipment

    def set_properties_in(self, property):
        self.property_in = property

    def set_properties_out(self, property):
        self.property_out = property

    def calculate(self):
        self.property_out.mass_flow_rate = self.property_in.mass_flow_rate
        self.property_out.H = self.property_in.H
        self.property_out.P = self.property_in.P
        self.property_out.T = self.property_in.T
        self.property_out.calculate()
