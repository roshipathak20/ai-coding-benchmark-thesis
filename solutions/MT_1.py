from typing import Optional


def safe_divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def main() -> None:
    x: float = 10.0
    y: float = 2.0
    z: float = 0.0

    result1: Optional[float] = safe_divide(x, y)
    result2: Optional[float] = safe_divide(x, z)

    print("10 / 2 =", result1)
    print("10 / 0 =", result2)


if __name__ == "__main__":
    main()