def unique_items(items: list) -> list:
    """순서를 유지하면서 중복 항목을 제거한 새 리스트를 반환한다. 항목은 해시 가능해야 한다."""
    return list(dict.fromkeys(items))


def chunk_list(items: list, size: int) -> list[list]:
    """리스트를 size개씩 나눈 리스트를 반환한다. 마지막 묶음은 size보다 짧을 수 있다."""
    if size < 1:
        raise ValueError("size는 1 이상이어야 합니다.")
    return [items[i:i + size] for i in range(0, len(items), size)]


if __name__ == "__main__":
    print(f"중복 제거: {unique_items([3, 1, 3, 2, 1])}")
    print(f"2개씩 분할: {chunk_list([1, 2, 3, 4, 5], 2)}")
