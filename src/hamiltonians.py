import numpy as np 

def h2_hamiltonian():
    """
    Two quibit reduced Hamiltonian for H2 
    near equilibrium bond distance

    Units: Hartree
    """
    I = np.eye(2)

    X = np.array([
        [0, 1],
        [1, 0]
    ])

    Z = np.array([
        [1, 0],
        [0, -1]
    ])

    H = (
        -1.052373245772859 * np.kron(I, I)
        + 0.39793742484318045 * np.kron(I, Z)
        - 0.39793742484318045 * np.kron(Z, I)
        - 0.01128010425623538 * np.kron(Z, Z)
        + 0.18093119978423156 * np.kron(X, X)
    )

    return H