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