from typing import Sequence
import matplotlib.pyplot as plt


def save_line_plot(values: Sequence[float], output_path: str) -> None:
    plt.figure()
    plt.plot(values)
    plt.savefig(output_path)
    plt.close()


def main() -> None:
    sample_values: Sequence[float] = [1, 3, 2, 5, 7, 6]
    output_path: str = "line_plot.png"
    save_line_plot(sample_values, output_path)
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    main()