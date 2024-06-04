from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

# number of qubits
n = 6
# create circuit 
qc = QuantumCircuit(n)
# apply hadamard
qc.h(0)
# insert controlled not gate (cx)
for i in range(n-1):
    qc.cx(0, i+1)
# apply not gate on qubit 1
qc.x(1)

sv = Statevector.from_instruction(qc)
plot_state_qsphere(sv, show_state_labels=False)
