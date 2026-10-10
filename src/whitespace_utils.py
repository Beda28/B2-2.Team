def normalize_whitespace(text: str) -> str:
    """문자열의 불필요한 공백을 정리한다."""
    return " ".join(text.split())