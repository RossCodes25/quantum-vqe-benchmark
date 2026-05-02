from qiskit import QuantumCircuit
from qiskit.circuit import Parameter


def simple_h2_ansatz():
    """
    Simple 2-qubit ansatz for H2:
    prepares a parameterised state that can mix |01> and |10>.
    """

    theta = Parameter("theta")

    qc = QuantumCircuit(2)
    qc.x(0)
    qc.ry(theta, 1)
    qc.cx(1, 0)

    return qc, theta