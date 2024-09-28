# Quantum Teleportation Simulation with Qiskit

## Overview
This project simulates the **quantum teleportation** protocol using Qiskit. Quantum teleportation allows the transfer of an unknown quantum state from one qubit to another using quantum entanglement and classical communication. The project implements the core teleportation circuit and visualizes the quantum operations.

## Features
- **Quantum Teleportation Simulation**: Implements a 3-qubit quantum circuit that teleports the state of one qubit to another.
- **Entanglement Creation**: Uses entanglement between qubits to facilitate the teleportation process.
- **Classical Communication**: Demonstrates how classical bits are used to correct the quantum state after measurement.
- **Circuit Visualization**: Draws the quantum teleportation circuit using `matplotlib`.
- **Qiskit Integration**: Uses the Qiskit framework to simulate and visualize the teleportation process.

## Requirements
- **Python 3.11**
- **Qiskit 1.2.2**
- **Matplotlib 3.8.1**
- **pylatexenc** for drawing the quantum circuit.

## Installation
To get started, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/quantum-teleportation.git
   cd quantum-teleportation
   ```

2. **Set up the Python environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Libraries**:
   Install the dependencies listed in the `requirements.txt`:
   ```bash
   pip install qiskit matplotlib pylatexenc
   ```

4. **Verify Installation**:
   Ensure the correct versions of the libraries are installed:
   ```bash
   python -c "import qiskit, matplotlib; print(qiskit.__version__, matplotlib.__version__)"
   ```

## Usage
To simulate the quantum teleportation protocol, run the following Python script:

```bash
python QuantumTeleportation.py
```

In the script:
1. A quantum circuit is built with 3 qubits and 3 classical bits.
2. Qubits 1 and 2 are entangled using a Hadamard and CNOT gate.
3. Qubit 0, holding the state to be teleported, is measured in the Bell basis.
4. Based on Alice's measurement results, Bob applies corrections (X and Z gates) to retrieve the teleported state on Qubit 2.

### Example Command:
```bash
python QuantumTeleportation.py
```

## Example Output
- **Circuit Visualization**: The quantum circuit used for teleportation will be displayed using Matplotlib.
- **Simulation Results**: Output of the final quantum state and its teleportation will be printed to the console.
  
  Example:
  ```
  {'00': 0.5, '11': 0.5}  # Example measurement results from Alice's qubits
  ```

## Expected Measurement Counts (Qubit 0 and Qubit 1)
When performing quantum teleportation, the Bell-state measurement on qubits 0 and 1 will produce the following probabilities:
|Outcome|Probability|
|---|---|
|00|25%|
|01|25%|
|10|25%|
|11|25%|

Each of the four possible outcomes (00, 01, 10, 11) occurs with equal probability because the state of qubits 0 and 1 is fully entangled.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

---

This should give you a solid structure for the project, making it easy to install, run, and contribute to!
