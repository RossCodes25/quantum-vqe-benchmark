import numpy as np
from hamiltonians import h2_hamiltonian


def exact_ground_state_energy(H):
    """
    Diagonalise Hamiltonian and return
    exact ground-state energy + state
    """

    eigenvalues, eigenvectors = np.linalg.eigh(H)

    ground_energy = eigenvalues[0]
    ground_state = eigenvectors[:, 0]

    return ground_energy, ground_state


if __name__ == "__main__":
    H = h2_hamiltonian()

    energy, state = exact_ground_state_energy(H)

    print("\nExact H2 Ground-State Energy:")
    print(energy)

    print("\nGround-State Vector:")
    print(state)