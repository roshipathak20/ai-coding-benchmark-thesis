from typing import Union
import pandas as pd


def csv_average(file_path: str, column_name: str) -> float:
    df: pd.DataFrame = pd.read_csv(file_path)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the CSV file.")

    mean_value: Union[float, int] = df[column_name].mean()
    return float(mean_value)


def main() -> None:
    file_path: str = "example.csv"
    column_name: str = "value"

    try:
        avg: float = csv_average(file_path, column_name)
        print(f"Average of '{column_name}': {avg}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()