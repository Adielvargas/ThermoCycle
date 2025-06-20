from CoolProp.CoolProp import PropsSI

class ThermoProperty:
    def __init__(self, name, fluid):
        self.name = name
        self.fluid = fluid
        self.mass_flow_rate = None

        self.T = None
        self.P = None
        self.H = None
        self.S = None
        self.Q = None

        self.resume = None

    def set_mass_flow_rate(self, mass_flow_rate):
        self.mass_flow_rate = mass_flow_rate



    def set_temperature(self, T):
        self.T = T + 273.15

    def set_pressure(self, P):
        self.P = P

    def set_enthalpy(self, H):
        self.H = H

    def set_entropy(self, S):
        self.S = S

    def set_quality(self, Q):
        self.Q = Q

    def calculate(self):
        if self.P is not None and self.T is not None:
           self.H = PropsSI('H', 'P', self.P, 'T', self.T, self.fluid)
           self.S = PropsSI('S', 'P', self.P, 'T', self.T, self.fluid)

        elif self.P is not None and self.Q is not None:
             self.H = PropsSI('H', 'P', self.P, 'Q', self.Q, self.fluid)
             self.S = PropsSI('S', 'P', self.P, 'Q', self.Q, self.fluid)
             self.T = PropsSI('T', 'P', self.P, 'Q', self.Q, self.fluid)

        elif self.P is not None and self.S is not None:
             self.T = PropsSI('T', 'P', self.P, 'S', self.S, self.fluid)
             self.H = PropsSI('H', 'P', self.P, 'S', self.S, self.fluid)

        self.resume = (f"--- {self.name} ---\n"
                       f"P = {self.P / 1e3:.2f} Pa\n"
                       f"T = {self.T - 273.15:.2f} °k\n"
                       f"H = {self.H / 1e3:.2f} J/kg\n"
                       f"S = {self.S / 1e3:.4f} J/kg.K\n")

