def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1

    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main() -> None:
    try:
        print("factorial(5) =", factorial(5))
        print("factorial(0) =", factorial(0))
        print("factorial(-1) =", factorial(-1))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()