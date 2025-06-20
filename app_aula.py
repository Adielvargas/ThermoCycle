from src.thermoProperty import ThermoProperty
from src.connector import Connector
from src.equipment.turbine import Turbine
from src.equipment.heater import Heater
from src.equipment.condenser import Condenser
from src.equipment.pump import Pump
from src.equipment.heater_closed import HeaterClosed
from src.equipment.mixer import Mixer
from src.thermoCycle import ThermoCycle


fluid = "Water"
mass_flow_rate = 1.0
y = 0.318  #fração extraída para AAA fechado
z = 0.682  #fração extraída para condensador


prop_1 = ThermoProperty("prop_1", fluid)
prop_1.set_mass_flow_rate(z)
prop_1.set_pressure(17e3)
prop_1.set_quality(0)


prop_2 = ThermoProperty("prop_2", fluid)
prop_2.set_mass_flow_rate(z)
prop_2.set_pressure(3e6)
prop_2.set_temperature(56.59)


prop_3 = ThermoProperty("prop_3", fluid)
prop_3.set_mass_flow_rate(y)
prop_3.set_pressure(6e5)
prop_3.set_quality(0)


prop_4 = ThermoProperty("prop_4", fluid)
prop_4.set_mass_flow_rate(y)
prop_4.set_pressure(3e6)
prop_4.set_temperature(159)


prop_5 = ThermoProperty("prop_5", fluid)
prop_5.set_mass_flow_rate(mass_flow_rate)
prop_5.set_pressure(3e6)
prop_5.set_temperature(210)



prop_6 = ThermoProperty("prop_6", fluid)
prop_6.set_mass_flow_rate(mass_flow_rate)
prop_6.set_pressure(3e6)
prop_6.set_temperature(350)



prop_7 = ThermoProperty("prop_7", fluid)
prop_7.set_mass_flow_rate(y)
prop_7.set_pressure(6e5)
prop_7.set_temperature(159)



prop_8 = ThermoProperty("prop_8", fluid)
prop_8.set_mass_flow_rate(z)
prop_8.set_pressure(17e3)
prop_8.set_temperature(57)



prop_9 = ThermoProperty("prop_9", fluid)
prop_9.set_mass_flow_rate(z)
prop_9.set_pressure(3e6)
prop_9.set_quality(0)


pipe_1 = Connector("pipe_1")
pipe_1.set_properties_in(prop_6)
pipe_1.set_properties_out(prop_6)


pipe_2 = Connector("pipe_2")
pipe_2.set_properties_in(prop_7)
pipe_2.set_properties_out(prop_7)


pipe_3 = Connector("pipe_3")
pipe_3.set_properties_in(prop_8)
pipe_3.set_properties_out(prop_8)


pipe_4 = Connector("pipe_4")
pipe_4.set_properties_in(prop_1)
pipe_4.set_properties_out(prop_1)


pipe_5 = Connector("pipe_5")
pipe_5.set_properties_in(prop_2)
pipe_5.set_properties_out(prop_2)


pipe_6 = Connector("pipe_6")
pipe_6.set_properties_in(prop_3)
pipe_6.set_properties_out(prop_3)


pipe_7 = Connector("pipe_7")
pipe_7.set_properties_in(prop_9)
pipe_7.set_properties_out(prop_9)


pipe_8 = Connector("pipe_8")
pipe_8.set_properties_in(prop_4)
pipe_8.set_properties_out(prop_4)


pipe_9 = Connector("pipe_9")
pipe_9.set_properties_in(prop_5)
pipe_9.set_properties_out(prop_5)



pump1 = Pump("pump1")
pump2 = Pump("pump2")
heater = Heater("heater")
turbine = Turbine("turbine" , y)
condenser = Condenser("condenser")
heater_closed = HeaterClosed("heaterClosed")
mixer = Mixer("mixer")



pump1.add_connectors_in(pipe_4)
pump1.add_connectors_out(pipe_5)


pump2.add_connectors_in(pipe_6)
pump2.add_connectors_out(pipe_8)


heater.add_connectors_in(pipe_9)
heater.add_connectors_out(pipe_1)


turbine.add_connectors_in(pipe_1)
turbine.add_connectors_out(pipe_2)
turbine.add_connectors_out(pipe_3)


heater_closed.add_connectors_in(pipe_5)
heater_closed.add_connectors_in(pipe_2)
heater_closed.add_connectors_out(pipe_7)
heater_closed.add_connectors_out(pipe_6)


condenser.add_connectors_in(pipe_3)
condenser.add_connectors_out(pipe_4)


mixer.add_connectors_in(pipe_7)
mixer.add_connectors_in(pipe_8)
mixer.add_connectors_out(pipe_9)


rankine_power_cycle = ThermoCycle()
rankine_power_cycle.add_equipment(pump1)
rankine_power_cycle.add_equipment(pump2)
rankine_power_cycle.add_equipment(turbine)
rankine_power_cycle.add_equipment(condenser)
rankine_power_cycle.add_equipment(heater)
rankine_power_cycle.add_equipment(heater_closed)
rankine_power_cycle.add_equipment(mixer)

rankine_power_cycle.initialize()
rankine_power_cycle.calculate()
rankine_power_cycle.calculate_efficiency()
rankine_power_cycle.draw("app_aula.png")


#print(f"Eficiencia del ciclo: {rankine_power_cycle.efficiency * 100:.2f}%")

#props = [prop_1, prop_2, prop_3, prop_4, prop_5, prop_6, prop_7, prop_8, prop_9]
#for p in props:
 #   print(f"\nPropiedades de {p.name}:")
 #   print(p.resume)

#print(f"Trabajo Turbina: {turbine.work/1000:.2f} kW")
#print(f"Trabajo Bomba 1: {pump1.work/1000:.2f} kW")
#print(f"Trabajo Bomba 2: {pump2.work/1000:.2f} kW")
#print(f"Calor en Heater: {heater.heat/1000:.2f} kW")

