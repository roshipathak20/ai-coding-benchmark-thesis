from typing import Optional
from bs4 import BeautifulSoup


def extract_title(html: str) -> str:
    soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
    title_tag: Optional = soup.title

    if title_tag is None or title_tag.string is None:
        return ""

    return title_tag.string.strip()


def main() -> None:
    html: str = """
    <html>
        <head>
            <title>Example Page</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """

    title: str = extract_title(html)
    print(f"Extracted title: '{title}'")


if __name__ == "__main__":
    main()