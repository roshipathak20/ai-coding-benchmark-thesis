from typing import Sequence


def average(values: Sequence[float]) -> float:
    if len(values) == 0:
        return 0.0
    return sum(values) / len(values)


def main() -> None:
    nums1: list[float] = [1, 2, 3, 4, 5]
    nums2: list[float] = []

    print("Average of nums1:", average(nums1))
    print("Average of nums2:", average(nums2))


if __name__ == "__main__":
    main()