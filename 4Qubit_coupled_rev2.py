
from qiskit_metal.qlibrary.terminations.launchpad_wb import LaunchpadWirebond

from qiskit_metal.qlibrary.tlines.mixed_path import RouteMixed

from qiskit_metal.qlibrary.qubits.transmon_cross_fl import TransmonCrossFL

from qiskit_metal.qlibrary.tlines.straight_path import RouteStraight

from qiskit_metal.qlibrary.tlines.meandered import RouteMeander

from qiskit_metal.qlibrary.couplers.coupled_line_tee import CoupledLineTee

from qiskit_metal import designs, MetalGUI

design = designs.DesignPlanar()

gui = MetalGUI(design)


LT1 = CoupledLineTee(
design,
name='LT1',
options={'pos_y': '2000.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




LT2 = CoupledLineTee(
design,
name='LT2',
options={'pos_x': '2000um', 'pos_y': '2000um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




P1 = LaunchpadWirebond(
design,
name='P1',
options={'orientation': '90.0',
 'pos_y': '-1000.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




P2 = LaunchpadWirebond(
design,
name='P2',
options={'orientation': '90.0',
 'pos_x': '2000.0um',
 'pos_y': '-1000.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)





            # WARNING
#options_connection_pads failed to have a value
Q1 = TransmonCrossFL(
design,
name='Q1',
options={'connection_pads': {'a': {'claw_gap': '6um',
                           'claw_length': '30um',
                           'claw_width': '10um',
                           'connector_location': '90',
                           'connector_type': '0',
                           'ground_spacing': '5um'}},
 'pos_x': '000um'}
)




RM3 = RouteMeander(
design,
name='RM3',
options={'_actual_length': '2.5 mm',
 'fillet': '0.03',
 'pin_inputs': {'end_pin': {'component': 'LT1',
                            'pin': 'second_end'},
                'start_pin': {'component': 'Q1',
                              'pin': 'a'}},
 'total_length': '2.5mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)





            # WARNING
#options_connection_pads failed to have a value
Q2 = TransmonCrossFL(
design,
name='Q2',
options={'connection_pads': {'a': {'claw_gap': '6um',
                           'claw_length': '30um',
                           'claw_width': '10um',
                           'connector_location': '90',
                           'connector_type': '0',
                           'ground_spacing': '5um'}},
 'pos_x': '2000.0um'}
)




RM4 = RouteMeander(
design,
name='RM4',
options={'_actual_length': '2.500000000000001 '
                   'mm',
 'fillet': '0.03',
 'pin_inputs': {'end_pin': {'component': 'LT2',
                            'pin': 'second_end'},
                'start_pin': {'component': 'Q2',
                              'pin': 'a'}},
 'total_length': '2.5mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




RouteStraight825 = RouteStraight(
design,
name='RouteStraight825',
options={'_actual_length': '1.7999999999999998 '
                   'mm',
 'pin_inputs': {'end_pin': {'component': 'LT2',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'LT1',
                              'pin': 'prime_end'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




P3 = LaunchpadWirebond(
design,
name='P3',
options={'orientation': '270.0',
 'pos_x': '-500.0um',
 'pos_y': '2250.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




P4 = LaunchpadWirebond(
design,
name='P4',
options={'orientation': '270.0',
 'pos_x': '6500.0um',
 'pos_y': '2250.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




RM5 = RouteMixed(
design,
name='RM5',
options={'_actual_length': '0.5391592653589794 '
                   'mm',
 'fillet': '0.2',
 'pin_inputs': {'end_pin': {'component': 'LT1',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'P3',
                              'pin': 'tie'}},
 'total_length': '0.7mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




LT3 = CoupledLineTee(
design,
name='LT3',
options={'pos_x': '4000.0um',
 'pos_y': '2000.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




LT4 = CoupledLineTee(
design,
name='LT4',
options={'pos_x': '6000.0um',
 'pos_y': '2000.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)





            # WARNING
#options_connection_pads failed to have a value
Q4 = TransmonCrossFL(
design,
name='Q4',
options={'connection_pads': {'a': {'claw_gap': '6um',
                           'claw_length': '30um',
                           'claw_width': '10um',
                           'connector_location': '90',
                           'connector_type': '0',
                           'ground_spacing': '5um'}},
 'pos_x': '6000.0um'}
)




RM7 = RouteStraight(
design,
name='RM7',
options={'_actual_length': '1.7999999999999998 '
                   'mm',
 'pin_inputs': {'end_pin': {'component': 'LT3',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'LT2',
                              'pin': 'prime_end'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




RM8 = RouteStraight(
design,
name='RM8',
options={'_actual_length': '1.8000000000000007 '
                   'mm',
 'pin_inputs': {'end_pin': {'component': 'LT4',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'LT3',
                              'pin': 'prime_end'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




RM10 = RouteMeander(
design,
name='RM10',
options={'_actual_length': '2.4999999999999964 '
                   'mm',
 'fillet': '0.03',
 'pin_inputs': {'end_pin': {'component': 'LT4',
                            'pin': 'second_end'},
                'start_pin': {'component': 'Q4',
                              'pin': 'a'}},
 'total_length': '2.5',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




RM1 = RouteStraight(
design,
name='RM1',
options={'_actual_length': '0.7164999999999999 '
                   'mm',
 'pin_inputs': {'end_pin': {'component': 'P1',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q1',
                              'pin': 'flux_line'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




RM2 = RouteStraight(
design,
name='RM2',
options={'_actual_length': '0.7164999999999999 '
                   'mm',
 'pin_inputs': {'end_pin': {'component': 'P2',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q2',
                              'pin': 'flux_line'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




P5 = LaunchpadWirebond(
design,
name='P5',
options={'orientation': '90.0',
 'pos_x': '4000.0um',
 'pos_y': '-1000.0um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




P6 = LaunchpadWirebond(
design,
name='P6',
options={'orientation': '90',
 'pos_x': '6000.0um',
 'pos_y': '-1000um'},

component_template={'falseparam1': {'falseparam2': 'false-param', 'falseparam3': 'false-param'}},
)




RM11 = RouteStraight(
design,
name='RM11',
options={'_actual_length': '0.7164999999999999 '
                   'mm',
 'pin_inputs': {'end_pin': {'component': 'Q4',
                            'pin': 'flux_line'},
                'start_pin': {'component': 'P6',
                              'pin': 'tie'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)





            # WARNING
#options_connection_pads failed to have a value
Q3 = TransmonCrossFL(
design,
name='Q3',
options={'connection_pads': {'a': {'claw_gap': '6um',
                           'claw_length': '30um',
                           'claw_width': '10um',
                           'connector_location': '90',
                           'connector_type': '0',
                           'ground_spacing': '5um'}},
 'pos_x': '4000.0um'}
)




RouteStraight495 = RouteStraight(
design,
name='RouteStraight495',
options={'_actual_length': '0.7164999999999999 '
                   'mm',
 'pin_inputs': {'end_pin': {'component': 'P5',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q3',
                              'pin': 'flux_line'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




RouteMixed201 = RouteMixed(
design,
name='RouteMixed201',
options={'_actual_length': '0.5391592653589797 '
                   'mm',
 'fillet': '0.2',
 'pin_inputs': {'end_pin': {'component': 'P4',
                            'pin': 'tie'},
                'start_pin': {'component': 'LT4',
                              'pin': 'prime_end'}},
 'total_length': '0.7mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




RouteMeander472 = RouteMeander(
design,
name='RouteMeander472',
options={'_actual_length': '2.499999999999999 '
                   'mm',
 'fillet': '0.03',
 'pin_inputs': {'end_pin': {'component': 'LT3',
                            'pin': 'second_end'},
                'start_pin': {'component': 'Q3',
                              'pin': 'a'}},
 'total_length': '2.5mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)



gui.rebuild()
gui.autoscale()
        