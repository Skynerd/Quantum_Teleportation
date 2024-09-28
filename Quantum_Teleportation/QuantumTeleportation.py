from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram,circuit_drawer
from qiskit.quantum_info import Statevector

# Create a quantum circuit with 3 qubits and 3 classical bits (to store measurements)
qc = QuantumCircuit(3, 3)

# Create an entangled pair between Qubit 1 and Qubit 2
qc.h(1)  # Hadamard gate on Qubit 1
qc.cx(1, 2)  # CNOT gate between Qubit 1 and Qubit 2

# Apply CNOT gate between Qubit 0 and Qubit 1, and a Hadamard gate on Qubit 0
qc.cx(0, 1)
qc.h(0)

# Apply CNOT gate between Qubit 0 and Qubit 1, and a Hadamard gate on Qubit 0
qc.cx(0, 1)
qc.h(0)

# Measure qubits 0 and 1
qc.measure([0, 1], [0, 1])

# Apply corrections based on classical measurements
qc.cx(1, 2)
qc.cz(0, 2) 


# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
result = simulator.run(qc).result()

# Get the result counts
counts = result.get_counts(qc)
print(counts)


# Visualize the results
plot_histogram(counts)

# Draw the circuit
qc.draw(output='mpl')
plt.show()













