from typing import List


def search_users(users: List[str], query: str) -> List[str]:
    q: str = query.lower()
    return [u for u in users if q in u.lower()]


def main() -> None:
    users: List[str] = ["Alice", "bob", "Charlie", "ALBERT", "Bobby"]
    query: str = "al"
    matches: List[str] = search_users(users, query)
    print("Matches:", matches)


if __name__ == "__main__":
    main()