from qiskit_ibm_runtime import QiskitRuntimeService


def save_ibm_account(token: str):
    """
    Save IBM Quantum account token locally.
    Only run this once.
    """

    QiskitRuntimeService.save_account(
        channel="ibm_quantum",
        token=token,
        overwrite=True
    )


def get_service():
    """
    Load saved IBM Quantum account.
    """

    return QiskitRuntimeService(channel="ibm_quantum")


def list_available_backends():
    """
    List available IBM Quantum backends.
    """

    service = get_service()

    backends = service.backends(
        simulator=False,
        operational=True
    )

    print("\nAvailable IBM Quantum backends:\n")

    for backend in backends:
        print(backend.name)


if __name__ == "__main__":
    list_available_backends()