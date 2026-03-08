def is_even(n: int) -> bool:
    return n % 2 == 0


def main() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 6]

    for n in numbers:
        print(f"{n} is even: {is_even(n)}")


if __name__ == "__main__":
    main()