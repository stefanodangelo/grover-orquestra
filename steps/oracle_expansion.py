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
    
    # save modified .json
    save_circuit(Circuit.from_dict(metadata), circuit_path)

def expand_oracle(circuit, element_to_search):
    element_to_search = element_to_search[::-1] # reverse the string in order to correctly apply the oracle function
    
    # oracle expansion
    #adapt_oracle(circuit, element_to_search)
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("circuit.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact