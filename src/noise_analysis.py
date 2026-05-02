import numpy as np
import pandas as pd
from pathlib import Path

from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit.quantum_info import DensityMatrix

from ansatz import simple_h2_ansatz
from vqe_runner import h2_pauli_hamiltonian
from exact_solver import exact_ground_state_energy
from hamiltonians import h2_hamiltonian


def build_simple_noise_model(single_qubit_error=0.001, two_qubit_error=0.01):
    """
    Build a simple depolarising noise model.

    single_qubit_error: error probability for 1-qubit gates
    two_qubit_error: error probability for 2-qubit gates
    """

    noise_model = NoiseModel()

    one_qubit_error = depolarizing_error(single_qubit_error, 1)
    two_qubit_error_obj = depolarizing_error(two_qubit_error, 2)

    noise_model.add_all_qubit_quantum_error(
        one_qubit_error,
        ["x", "ry", "h"]
    )

    noise_model.add_all_qubit_quantum_error(
        two_qubit_error_obj,
        ["cx"]
    )

    return noise_model


def noisy_energy_expectation(theta_value, noise_model):
    """
    Run the ansatz through a noisy density-matrix simulator
    and calculate <H>.
    """

    circuit, theta = simple_h2_ansatz()
    bound_circuit = circuit.assign_parameters({theta: theta_value})
    bound_circuit.save_density_matrix()

    simulator = AerSimulator(
        method="density_matrix",
        noise_model=noise_model
    )

    result = simulator.run(bound_circuit).result()
    rho = result.data(0)["density_matrix"]

    density_matrix = DensityMatrix(rho)
    hamiltonian = h2_pauli_hamiltonian()

    energy = np.real(density_matrix.expectation_value(hamiltonian))

    return energy


if __name__ == "__main__":
    exact_energy, _ = exact_ground_state_energy(h2_hamiltonian())

    # Optimal theta from ideal VQE run
    optimal_theta = -0.22343281

    noise_model = build_simple_noise_model(
        single_qubit_error=0.001,
        two_qubit_error=0.01
    )

    noisy_energy = noisy_energy_expectation(
        theta_value=optimal_theta,
        noise_model=noise_model
    )

    absolute_error = abs(noisy_energy - exact_energy)

    print("\nExact H2 Ground-State Energy:")
    print(exact_energy)

    print("\nNoisy Simulator Energy:")
    print(noisy_energy)

    print("\nAbsolute Error:")
    print(absolute_error)

    output_path = Path("results/data/noisy_simulator_results.csv")

    df = pd.DataFrame([{
        "system": "H2",
        "method": "VQE",
        "backend": "density_matrix_noisy_simulator",
        "noise_model": "simple_depolarizing",
        "single_qubit_error": 0.001,
        "two_qubit_error": 0.01,
        "exact_energy_hartree": exact_energy,
        "noisy_energy_hartree": noisy_energy,
        "absolute_error_hartree": absolute_error,
        "theta_used": optimal_theta,
    }])

    df.to_csv(output_path, index=False)

    print(f"\nResults saved to {output_path}")