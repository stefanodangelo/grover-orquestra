from zquantum.core.circuit import save_circuit
from ._circuit import Circuit
import json
"""
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor
"""

def load_circuit(file):
    """Loads a circuit from a file.
    Args:
        file (str or file-like object): the name of the file, or a file-like object.
    Returns:
        circuit (core.Circuit): the circuit
    """

    if isinstance(file, str):
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = json.load(file)

    return Circuit.from_dict(data)

def to_zap(circuit, save_path):
    """
    converted_circuit = Circuit(circuit)
    save_circuit(converted_circuit, save_path)
    """
    with open(save_path,'w') as f:
        f.write(json.dumps(circuit, indent=2)) # Write message to file as this will serve as output artifact
    
def from_json(load_path):
    circuit = load_circuit(load_path)
    return circuit.to_qiskit() 