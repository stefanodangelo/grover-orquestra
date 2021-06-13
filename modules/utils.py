from zquantum.core.circuit import save_circuit
from ._circuit import Circuit
import json
"""
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor
"""

def load_circuit(filename):
    """Loads a circuit from a file.
    Args:
        file (str or file-like object): the name of the file, or a file-like object.
    Returns:
        circuit (core.Circuit): the circuit
    """
    data = {}
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except IOError:
            print(f'Error: Could not open {filename}')
    
    return Circuit.from_dict(data['circuit'])

def to_zap(circuit, save_path):
    converted_circuit = Circuit(circuit)
    save_circuit(converted_circuit, save_path)
    
def from_json(load_path):
    circuit = load_circuit(load_path)
    return circuit.to_qiskit()