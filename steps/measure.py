from modules.utils import *
from modules.functions import *
import json


def run_and_measure(circuit, backend='qasm_simulator', save_path = 'measurements.json', token="f1b53e81357761bafbbb2d7a71eaa26cfc0d9df4eeb53513096c5cee90ec01bcc8ba6fa547ea4988a1b9136f2abf8090a133546389581b3c51a1471dad8749e6"):
    
    qc = from_json(circuit)
    measurements = {}
    measurements['schema'] = ""

    if backend == 'ibm':
        results = get_results_from_IBM(token)
        measurements['results'] = results.get_counts(qc)
    else:
        results = get_simulation_results(backend)

        # <--- code used only for plot task --->
        old_keys = list(results.keys())
        new_keys = list(map(lambda x: x[-len(qc.qubits):], old_keys))  # needed because otherwise keys would be repated
        
        measurements['results'] = {new_keys[i]: results[old_keys[i]] for i in range(len(new_keys))}

    with open(save_path, 'w') as f:
        json.dump(measurements, f)
       