from typing import Any


def is_palindrome(text: str) -> bool:
    normalized: str = text.replace(" ", "").lower()
    return normalized == normalized[::-1]


def main() -> None:
    examples: list[str] = [
        "Race car",
        "Hello",
        "Never odd or even",
        "Python",
    ]

    for text in examples:
        result: bool = is_palindrome(text)
        print(f'"{text}" -> {result}')


if __name__ == "__main__":
    main()