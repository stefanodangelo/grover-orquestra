from zquantum.core.circuit import save_circuit
import json

def to_zap(circuit, save_path):
    with open(save_path,'w') as f:
        f.write(json.dumps(circuit, indent=2)) # Write message to file as this will serve as output artifact