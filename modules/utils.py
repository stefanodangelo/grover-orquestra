from zquantum.core.circuit import save_circuit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from math import sqrt
import json

from qiskit import IBMQ, Aer, assemble, transpile
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

def to_zap(circuit, save_path):
    with open(save_path,'w') as f:
        f.write(json.dumps(circuit, indent=2)) # Write message to file as this will serve as output artifact