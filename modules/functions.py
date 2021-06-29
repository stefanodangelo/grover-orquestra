from qiskit import IBMQ, Aer, assemble, transpile
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

def init(qc, qr):
    qc.h(qr)
    
    return qc

def mcz(qc, qr):
    last_qubit = len(qc.qubits) - 1
    
    # barriers only for visualization purposes
    qc.barrier(qr)
    qc.barrier(qr)
    
    qc.h(last_qubit)
    qc.mct(qr[:-1], qr[-1])  # multi-controlled-toffoli
    qc.h(last_qubit)
    
    # barriers only for visualization purposes
    qc.barrier(qr)
    qc.barrier(qr)
    
    return qc

def oracle(qc, qr):
    
    qc.x(qr)
    qc = mcz(qc, qr)
    qc.x(qr)

    
    return qc

def diffuser(qc, qr):
    qc.h(qr)
    qc.x(qr)
    qc = mcz(qc, qr)
    qc.x(qr)
    qc.h(qr)
    
    return qc

def add_measurements(qc, qr, cr):
    qc.measure(qr, cr)
    
    return qc
    
def find_all_mcz(metadata):
    mcz_positions = []
    mct_in_oracle = True # boolean telling whether the mct is in the oracle or not
    for i in range(len(metadata['gates'])):
        if (metadata['gates'][i]['name'] == 'MCT' or metadata['gates'][i]['name'] == 'CNOT' or metadata['gates'][i]['name'] == 'CCX'):
            if mct_in_oracle:
                mcz_positions.append(i)
                mct_in_oracle = False
            else:
                mct_in_oracle = True
    
    mcz_positions.sort(reverse=True) # sort in order not to affect the positions of the gates to remove
    
    return mcz_positions
    
def remove_x_gates(gates, mcz_position, element, n_qubits):
    """
        Removes the X gates before and after the MCZ gate. 
    """
    registers_without_gate = [i for i in range(len(element)) if element[i] == '1']
    gates_to_remove = []
    
    for index in registers_without_gate:
        """
            all the offsets summed and subtracted here have been properly chosen basing 
            on the number of barriers surrounding the oracle block
        """
        gates_to_remove.append(mcz_position + index + 4)
        gates_to_remove.append(mcz_position - n_qubits - 3 + index)
    
    gates_to_remove.sort(reverse=True) # sort in order not to affect the positions of the gates to remove
    
    for i in gates_to_remove:
        del gates[i]

def get_results_from_IBM(token):
    IBMQ.save_account(token)
    provider = IBMQ.load_account()
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= len(qc.qubits) and not x.configuration().simulator and x.status().operational == True))

    # Run circuit on the least busy backend. Monitor the execution of the job in the queue
    transpiled_grover_circuit = transpile(qc, backend, optimization_level=3)
    qobj = assemble(transpiled_grover_circuit)
    job = backend.run(qobj)
    job_monitor(job, interval=2)

    # Get the results from the computation
    return job.result()

def get_simulation_results(backend):
    qc.measure_all()
    sim = Aer.get_backend(backend)
    qobj = assemble(qc)
    result = sim.run(qobj).result()
    return result.get_counts()