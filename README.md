# Quantum VQE Benchmark

Benchmarking the Variational Quantum Eigensolver (VQE) on simulators and IBM Quantum hardware.

## Aim

This project investigates how accurately VQE estimates the ground-state energy of small quantum systems, starting with the hydrogen molecule H₂.

The project compares:

- exact diagonalisation
- ideal simulation
- noisy simulation
- real IBM Quantum hardware

The goal is not just to run VQE, but to understand when it works, when it fails, and why.

## Research Questions

1. How close does VQE get to the exact ground-state energy?
2. How does real hardware differ from ideal simulation?
3. How strongly do noise, shot count, ansatz choice, and optimiser choice affect the result?
4. At what point does increasing circuit complexity stop helping?

## Initial System: H₂ Molecule

H₂ is used because it is small enough to simulate classically and run on real quantum hardware, while still being a standard benchmark problem in quantum computing.

## Methods

### Exact Diagonalisation

A classical exact solver gives the reference ground-state energy.

### VQE

A parameterised quantum circuit prepares trial states. A classical optimiser updates the parameters to minimise

E(θ) = <ψ(θ)|H|ψ(θ)>.

### Hardware Comparison

The same problem will be tested using:

- ideal simulator
- noisy simulator
- IBM Quantum backend

## Project Structure

```text
quantum-vqe-benchmark/
├── src/
│   ├── hamiltonians.py
│   ├── exact_solver.py
│   ├── ansatz.py
│   ├── vqe_runner.py
│   ├── ibm_backend.py
│   ├── noise_analysis.py
│   └── utils.py
├── notebooks/
│   ├── 01_h2_simulator.ipynb
│   ├── 02_h2_real_backend.ipynb
│   └── 03_results_analysis.ipynb
├── results/
│   ├── plots/
│   ├── data/
│   └── reports/
├── tests/
└── docs/

## Current Status

### First Successful Benchmark

Implemented exact diagonalisation and first ideal-statevector VQE simulation for H₂.

Results:

- Exact ground-state energy: -1.8572750302023795 Hartree
- VQE estimated energy: -1.8572750257726858 Hartree
- Absolute error: 4.43 × 10⁻⁹ Hartree

This confirms successful convergence of the first VQE implementation.
---

## Planned Analysis

The project will track:

- final energy error
- convergence behaviour
- number of optimiser iterations
- circuit depth
- shot noise
- hardware noise effects
- simulator vs hardware discrepancy

---

## Tools

- Python
- Qiskit
- Qiskit Aer
- Qiskit IBM Runtime
- NumPy
- SciPy
- Matplotlib
- Pandas
- Jupyter

---

## Future Extensions

Possible future work:

- LiH or HeH+
- transverse-field Ising model
- QAOA benchmarking
- error mitigation
- ansatz comparison
- quantum machine learning benchmarking

---

## Why This Project

This project is designed as a serious research portfolio project for:

- PhD applications
- quantum computing internships
- research scientist roles
- quantum software engineering roles

The focus is on reproducible results, strong methodology, and understanding the gap between ideal quantum algorithms and real quantum hardware.