from typing import List, TypeVar

T = TypeVar("T")


def merge_sorted_lists(a: List[T], b: List[T]) -> List[T]:
    i: int = 0
    j: int = 0
    merged: List[T] = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged


def main() -> None:
    list_a: List[int] = [1, 3, 5, 7]
    list_b: List[int] = [2, 4, 6, 8]
    result = merge_sorted_lists(list_a, list_b)
    print("Merged list:", result)


if __name__ == "__main__":
    main()