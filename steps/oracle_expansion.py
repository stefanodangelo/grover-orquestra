from zquantum.core.circuit import Circuit, save_circuit
from qiskit import QuantumCircuit, QuantumRegister
from modules.utils import *
import json

def remove_x_gates(gates, mct_position, element, n_qubits):
    registers_without_gate = [i for i in range(len(element)) if element[i] == '1']
    gates_to_remove = []
    
    for index in registers_without_gate:
        gates_to_remove.append(mct_position + index + 4)
        gates_to_remove.append(mct_position - n_qubits - 3 + index)
    
    gates_to_remove.sort(reverse=True) # sort in order not to affect the positions of the gate to remove
    
    for i in gates_to_remove:
        del gates[i]

def adapt_oracle(circuit_path, element):
    # load circuit data
    with open(circuit_path, 'r') as f:
        metadata = json.load(f)
    metadata = list(metadata.values())[0]['circuit']
    
    # remove x gates where not needed 
    mct_positions = []
    mct_in_oracle = True # boolean telling whether the mct is in the oracle or not
    for i in range(len(metadata['gates'])):
        if (metadata['gates'][i]['name'] == 'MCT' or metadata['gates'][i]['name'] == 'CNOT' or metadata['gates'][i]['name'] == 'CCX'):
            if mct_in_oracle:
                mct_positions.append(i)
                mct_in_oracle = False
            else:
                mct_in_oracle = True
    
    mct_positions.sort(reverse=True) # sort in order not to affect the positions of the gate to remove
    
    for position in mct_positions:
        remove_x_gates(metadata['gates'], position, element, len(element))  
        
    # save modified .json
    save_circuit(Circuit.from_dict(metadata), "expanded-circuit.json")

    
def expand_oracle(circuit, element_to_search):
    element_to_search = element_to_search[::-1] # reverse the string in order to correctly apply the oracle function
    
    # oracle expansion
    #adapt_oracle(circuit, element_to_search)
    message = "EMPTY MESSAGE"
    try:
        with open(circuit, 'r') as f:
            metadata = json.load(f)
        message = "LOADED SUCCESSFULLY"
    except:
        message = "ERROR"
    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("expanded-circuit.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact    