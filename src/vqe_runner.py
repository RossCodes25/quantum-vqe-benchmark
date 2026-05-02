import numpy as np
from scipy.optimize import minimize
from qiskit.quantum_info import Statevector, SparsePauliOp

from ansatz import simple_h2_ansatz
from exact_solver import exact_ground_state_energy
from hamiltonians import h2_hamiltonian


def h2_pauli_hamiltonian():
    """
    Same H2 Hamiltonian as SparsePauliOp for Qiskit.
    """

    return SparsePauliOp.from_list([
        ("II", -1.052373245772859),
        ("IZ", 0.39793742484318045),
        ("ZI", -0.39793742484318045),
        ("ZZ", -0.01128010425623538),
        ("XX", 0.18093119978423156),
    ])


def energy_expectation(theta_value):
    """
    Compute <psi(theta)|H|psi(theta)> using an ideal statevector simulator.
    """

    circuit, theta = simple_h2_ansatz()
    bound_circuit = circuit.assign_parameters({theta: theta_value[0]})

    state = Statevector.from_instruction(bound_circuit)
    hamiltonian = h2_pauli_hamiltonian()

    energy = np.real(state.expectation_value(hamiltonian))

    return energy


def run_vqe():
    """
    Run basic VQE optimisation.
    """

    result = minimize(
        energy_expectation,
        x0=np.array([0.0]),
        method="COBYLA",
        options={"maxiter": 200},
    )

    return result


if __name__ == "__main__":
    exact_energy, _ = exact_ground_state_energy(h2_hamiltonian())
    result = run_vqe()

    print("\nExact H2 Ground-State Energy:")
    print(exact_energy)

    print("\nVQE Estimated Energy:")
    print(result.fun)

    print("\nOptimal theta:")
    print(result.x)

    print("\nAbsolute Error:")
    print(abs(result.fun - exact_energy))