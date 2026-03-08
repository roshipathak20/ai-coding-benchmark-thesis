from typing import List


def parse_int_list(text: str) -> List[int]:
    result: List[int] = []
    for part in text.split(","):
        item: str = part.strip()
        try:
            value: int = int(item)
            result.append(value)
        except ValueError:
            continue
    return result


def main() -> None:
    text: str = "1, 2, three, 4, 5, six, 7"
    numbers: List[int] = parse_int_list(text)
    print("Parsed integers:", numbers)


if __name__ == "__main__":
    main()