class Mixer:
    def __init__(self, name):
        self.name = name
        self.connectors_in = []
        self.connectors_out = []
        self.properties_in = []
        self.properties_out = []

    def add_connectors_in(self, connector):
        self.connectors_in.append(connector)

    def add_connectors_out(self, connector):
        self.connectors_out.append(connector)

    def energy_balance(self):
        p_in1 = self.properties_in[0]
        p_in2 = self.properties_in[1]
        p_out = self.properties_out[0]

        m1 = p_in1.mass_flow_rate
        m2 = p_in2.mass_flow_rate
        m_total = m1 + m2

        p_out.mass_flow_rate = m_total
        p_out.H = (m1 * p_in1.H + m2 * p_in2.H) / m_total
        p_out.P = p_in1.P

        p_out.calculate()

    def calculate(self):
        pass

