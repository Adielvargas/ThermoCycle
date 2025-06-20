class Equipment():
    def __init__(self, name):
        self.name = name
        self.connectors_in = []
        self.connectors_out = []

        self.properties_in = []
        self.properties_out = []

        self.heat = None
        self.work = None

    def add_connectors_in(self, connector):
        self.connectors_in.append(connector)

    def add_connectors_out(self, connector):
        self.connectors_out.append(connector)

    def set_heat(self, heat):
        self.heat = heat

    def set_work(self, work):
        self.work = work

    def energy_balance(self):
        h_in = 0.0
        h_out = 0.0
        print(self.name)
        for property in self.properties_in:
            print('- IN:')
            print(property.resume)
            h_in += property.H * property.mass_flow_rate

        for property in self.properties_out:
            print('- OUT:')
            print(property.resume)
            h_out +=  property.H * property.mass_flow_rate

        self.enthalpy_balance = h_out - h_in

