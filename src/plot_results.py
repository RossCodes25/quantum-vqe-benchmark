import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_convergence():
    df = pd.read_csv("results/data/energy_convergence.csv")

    output_path = Path("results/plots/energy_convergence.png")

    plt.figure(figsize=(8, 5))
    plt.plot(df["iteration"], df["energy_hartree"], marker="o", label="VQE energy")
    plt.axhline(
        df["exact_energy_hartree"].iloc[0],
        linestyle="--",
        label="Exact energy"
    )

    plt.xlabel("Iteration")
    plt.ylabel("Energy / Hartree")
    plt.title("VQE Energy Convergence for H2")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()

    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    plot_convergence()