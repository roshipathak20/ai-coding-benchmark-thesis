from typing import List


def has_extension(filename: str, extension: str) -> bool:
    if "." not in filename:
        return False
    ext: str = filename.rsplit(".", 1)[1]
    return ext.lower() == extension.lower()


def main() -> None:
    files: List[str] = [
        "photo.jpg",
        "archive.tar.gz",
        "README",
        "document.PDF",
        "notes.txt"
    ]

    ext: str = "gz"
    for f in files:
        print(f"{f} has .{ext}: {has_extension(f, ext)}")


if __name__ == "__main__":
    main()