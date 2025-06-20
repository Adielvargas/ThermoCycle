from .equipment import Equipment

class Turbine(Equipment):
    def __init__(self, name, y):
        super().__init__(name)
        self.heat = 0.0
        self.y = y

    def calculate(self):
        m_in = self.properties_in[0].mass_flow_rate
        m_out1 = m_in * self.y
        m_out2 = m_in * (1 - self.y)

        self.properties_out[0].mass_flow_rate = m_out1  
        self.properties_out[1].mass_flow_rate = m_out2  

        h_in = self.properties_in[0].H
        h_out1 = self.properties_out[0].H
        h_out2 = self.properties_out[1].H

        self.work = -m_in * (h_in - (self.y * h_out1 + (1 - self.y) * h_out2))
