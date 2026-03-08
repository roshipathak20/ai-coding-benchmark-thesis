from typing import Any
import requests


def fetch_json(url: str) -> Any:
    response: requests.Response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main() -> None:
    url: str = "https://api.github.com"
    try:
        data: Any = fetch_json(url)
        print(data)
    except requests.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    main()