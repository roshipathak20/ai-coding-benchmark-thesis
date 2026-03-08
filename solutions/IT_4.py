from typing import Dict

def word_frequency(text: str) -> Dict[str, int]:
    words = text.lower().split()
    freq: Dict[str, int] = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq


def main() -> None:
    sentence = "This is a test This is only a test"
    result = word_frequency(sentence)
    print(result)


if __name__ == "__main__":
    main()