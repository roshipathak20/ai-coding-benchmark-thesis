from typing import List, Optional, Tuple


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement: int = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

    return None


def main() -> None:
    nums: List[int] = [2, 7, 11, 15]
    target: int = 9

    result: Optional[Tuple[int, int]] = two_sum(nums, target)
    print(f"nums={nums}, target={target} -> {result}")


if __name__ == "__main__":
    main()