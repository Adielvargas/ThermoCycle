from .equipment.turbine import Turbine
from .equipment.heater import Heater
from .equipment.condenser import Condenser
from .equipment.pump import Pump
from .equipment.heater_closed import HeaterClosed
from .equipment.mixer import Mixer

import networkx as nx
import matplotlib.pyplot as plt


class ThermoCycle:
    def __init__(self):

        self.equipments = []
        self.connectors = []
        self.efficiency = None

    def add_equipment(self, equipment):
        self.equipments.append(equipment)

    def initialize(self):
        for equipment in self.equipments:
            for connector in equipment.connectors_in:
                connector.add_equipment_out(equipment)
                if connector not in self.connectors:
                    self.connectors.append(connector)
                equipment.properties_in.append(connector.property_out)

            for connector in equipment.connectors_out:
                connector.add_equipment_in(equipment)
                if connector not in self.connectors:
                    self.connectors.append(connector)
                equipment.properties_out.append(connector.property_in)

    def calculate(self):
        for connector in self.connectors:
            connector.calculate()

        for equipment in self.equipments:
            equipment.energy_balance()

        for equipment in self.equipments:
            equipment.calculate()

    def calculate_efficiency(self):
        W_net = 0.0
        Q_in = 0.0
        for equipment in self.equipments:
            if isinstance(equipment, Turbine):
                W_net += equipment.work
            elif isinstance(equipment, Pump):
                W_net += equipment.work
            elif isinstance(equipment, Heater):
                Q_in += equipment.heat

        self.efficiency = W_net / Q_in

    def draw(self, output_file):
        G = nx.DiGraph()

        for connector in self.connectors:
            G.add_edge(connector.equipment_in.name,
                       connector.equipment_out.name,
                       label=connector.name)

        plt.figure(figsize=(10, 8))
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', arrows=True, font_size=10)
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        plt.savefig(output_file, dpi=300)
        plt.close()
