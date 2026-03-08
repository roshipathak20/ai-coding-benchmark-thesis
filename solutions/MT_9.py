from typing import List, Dict, Any


def sort_by_age(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(records, key=lambda x: x["age"])


def main() -> None:
    people: List[Dict[str, Any]] = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 25},
    ]

    sorted_people: List[Dict[str, Any]] = sort_by_age(people)
    print("Sorted by age:", sorted_people)


if __name__ == "__main__":
    main()