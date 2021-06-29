from zquantum.core.circuit import Circuit, save_circuit
from modules.utils import *
from modules.functions import *
import json 


def expand_oracle(circuit, element_to_search, save_path="expanded-circuit.json"):
    element_to_search = element_to_search[::-1] # reverse the string in order to correctly apply the oracle function
    
    # load circuit data
    with open(circuit, 'r') as f:
        metadata = json.load(f)
    
    # remove X gates where not needed 
    mcz_positions = find_all_mcz(metadata)
    
    for position in mcz_positions:
        remove_x_gates(metadata['gates'], position, element_to_search, len(element_to_search))  
    
    # save modified .json
    save_circuit(Circuit.from_dict(metadata), save_path)