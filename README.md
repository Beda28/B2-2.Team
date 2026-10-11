# 1. 프로젝트 소개

Codyssey AI/SW 기초 과정의 Python·Git 협업 프로젝트입니다.
GitHub Flow를 사용해 작업별 브랜치에서 개발하고, PR 리뷰 후 main에 병합하여 변경 이력과 검토 과정을 기록합니다.

# 2. 팀원 소개

- 방승규 @Beda28: 협업 규칙, 문자열 유틸 함수
- 노신용 @ShinyongNoh: 공백 정리, 대소문자 변환
- 김세윤 @sy364: 사칙연산 함수·테스트, amend 실습
- 김준원 @jwyssey: 리스트 유틸 함수·테스트, stash 실습

# 3. 유틸 함수

| 작성자 | 파일 | 함수 | 사용 예시와 반환값 |
| --- | --- | --- | --- |
| 방승규 | [src/string_utils.py](src/string_utils.py) | normalize_spaces, count_words | normalize_spaces("  hello   world  ") → "hello world", count_words("hello world") → 2 |
| 노신용 | [src/whitespace_utils.py](src/whitespace_utils.py) | normalize_whitespace | normalize_whitespace("  hello   world  ") → "hello world" |
| 노신용 | [src/case_conversion_utils.py](src/case_conversion_utils.py) | to_uppercase, to_lowercase | to_uppercase("Hello") → "HELLO", to_lowercase("Hello") → "hello" |
| 김세윤 | [src/math_utils.py](src/math_utils.py) | add, subtract, multiply, divide | add(3, 2) → 5, subtract(3, 2) → 1, multiply(3, 2) → 6, divide(3, 2) → 1.5 |
| 김준원 | [src/list_utils.py](src/list_utils.py) | unique_items, chunk_list | unique_items([3, 1, 3, 2, 1]) → [3, 1, 2], chunk_list([1, 2, 3, 4, 5], 2) → [[1, 2], [3, 4], [5]] |

외부 라이브러리 없이 실행합니다. divide는 두 번째 인자가 0이면 ValueError가 발생합니다. chunk_list는 size가 1 미만이면 ValueError가 발생합니다.

# 4. 실행 및 검증

Python 3.10 이상에서 프로젝트 루트를 기준으로 실행합니다.

- 문자열 실행 예시: python -m src.string_utils
- 리스트 실행 예시: python -m src.list_utils
- 수학·리스트 테스트: python -m unittest discover -s tests -v

Python 3.14.6에서 수학 테스트 5개, 문자열 입력 6종 검증과 모듈 실행 예시가 모두 통과했습니다.
Python 3.13.5에서 리스트 테스트 5개를 포함한 전체 테스트 10개와 리스트 실행 예시가 통과했습니다.

# 5. 주요 문서

- [협업 가이드](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [Git 트러블슈팅 기록](docs/troubleshooting-log.md)
- [제출 증빙](SUBMISSION.md)
