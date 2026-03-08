from typing import Dict, Any
import json


def json_roundtrip(file_path: str, data: Dict[str, Any]) -> Dict[str, Any]:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    with open(file_path, "r", encoding="utf-8") as f:
        loaded: Dict[str, Any] = json.load(f)

    return loaded


def main() -> None:
    file_path: str = "example.json"
    sample_data: Dict[str, Any] = {
        "name": "Alice",
        "age": 30,
        "active": True
    }

    result: Dict[str, Any] = json_roundtrip(file_path, sample_data)
    print("Loaded data:", result)


if __name__ == "__main__":
    main()