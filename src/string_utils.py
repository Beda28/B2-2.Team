def normalize_spaces(text: str) -> str:
    """양 끝 공백을 제거하고 연속된 공백 문자를 단일 공백으로 바꾼다."""
    return " ".join(text.split(" "))


def count_words(text: str) -> int:
    """공백 문자로 구분된 단어 수를 반환한다."""
    return len(text.split())


if __name__ == "__main__":
    for text in ["hello world", "", "   ", "  hello   world  ", "hello\tworld\nPython"]:
        print(f"입력: {text!r}")
        print(f"공백 정리: {normalize_spaces(text)!r}, 단어 수: {count_words(text)}")
