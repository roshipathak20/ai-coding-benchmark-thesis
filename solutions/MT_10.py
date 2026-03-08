from typing import Final


def sum_range(n: int) -> int:
    if n <= 0:
        return 0

    total: int = 0
    for i in range(1, n + 1):
        total += i
    return total


def main() -> None:
    tests: list[int] = [5, 1, 0, -3]

    for t in tests:
        print(f"sum_range({t}) = {sum_range(t)}")


if __name__ == "__main__":
    main()