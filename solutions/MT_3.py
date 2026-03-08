from typing import TypeVar, Iterable, List, Set

T = TypeVar("T")


def unique_preserve_order(items: Iterable[T]) -> List[T]:
    seen: Set[T] = set()
    result: List[T] = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def main() -> None:
    data: List[int] = [1, 2, 2, 3, 1, 4, 3, 5]
    unique_items: List[int] = unique_preserve_order(data)
    print("Original:", data)
    print("Unique (order preserved):", unique_items)


if __name__ == "__main__":
    main()