from qiskit import IBMQ, Aer, assemble, transpile
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor
from modules.utils import *
import json


def run_and_measure(circuit = None, backend=None, save_path = 'measurements.json'):
    answer = {}
    answer['schema'] = ""
    answer['message'] = 'ciao'
    

    token = IBMQ.stored_accounts()[0]['token']
    url = IBMQ.stored_accounts()[0]['url']
    IBMQ.enable_account(token,url)
    """
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= len(qc.qubits) and 
                         not x.configuration().simulator and x.status().operational==True))
    # Run our circuit on the least busy backend. Monitor the execution of the job in the queue
    transpiled_grover_circuit = transpile(qc, backend, optimization_level=3)
    qobj = assemble(transpiled_grover_circuit)
    job = backend.run(qobj)
    job_monitor(job, interval=2)

    # Get the results from the computation
    results = job.result()
    answer = results.get_counts(qc)
    """
    with open(save_path, 'w') as f:
        json.dump(answer, f)
       