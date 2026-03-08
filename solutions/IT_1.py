from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7]
    target = 4
    result = binary_search(numbers, target)
    print(f"Index of {target}: {result}")


if __name__ == "__main__":
    main()