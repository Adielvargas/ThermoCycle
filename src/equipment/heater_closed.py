class HeaterClosed:
    def __init__(self, name):
        self.name = name
        self.connectors_in = []
        self.connectors_out = []
        self.properties_in = []
        self.properties_out = []
        self.heat = 0.0

    def add_connectors_in(self, connector):
        self.connectors_in.append(connector)

    def add_connectors_out(self, connector):
        self.connectors_out.append(connector)

    def energy_balance(self):
        vapor = self.properties_in[0]
        liquido_in = self.properties_in[1]

        liquido_out = self.properties_out[0]
        vapor_out = self.properties_out[1]


        liquido_out.T = vapor.T
        liquido_out.P = liquido_in.P
        liquido_out.calculate()

        vapor_out.P = vapor.P
        vapor_out.T = vapor.T
        vapor_out.calculate()

        m_vapor = vapor.mass_flow_rate
        m_liquido = liquido_in.mass_flow_rate

        self.heat = m_liquido * (liquido_out.H - liquido_in.H)

    def calculate(self):
        pass

