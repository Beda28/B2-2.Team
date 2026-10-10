# 1. 프로젝트 소개

Codyssey AI/SW 기초 과정의 Python·Git 협업 프로젝트입니다.
GitHub Flow를 사용해 작업별 브랜치에서 개발하고, PR 리뷰 후 main에 병합하여 변경 이력과 검토 과정을 기록합니다.

# 2. 팀원 소개

- 방승규 @Beda28: 협업 규칙, 문자열 유틸 함수
- 노신용 @ShinyongNoh: 공백 정리, 대소문자 변환
- 김세윤 @sy364: 사칙연산 함수·테스트, amend 실습

# 3. 유틸 함수

| 작성자 | 파일 | 함수 | 사용 예시와 반환값 |
| --- | --- | --- | --- |
| 방승규 | [src/string_utils.py](src/string_utils.py) | normalize_spaces, count_words | normalize_spaces("  hello   world  ") → "hello world", count_words("hello world") → 2 |
| 노신용 | [src/whitespace_utils.py](src/whitespace_utils.py) | normalize_whitespace | normalize_whitespace("  hello   world  ") → "hello world" |
| 노신용 | [src/case_conversion_utils.py](src/case_conversion_utils.py) | to_uppercase, to_lowercase | to_uppercase("Hello") → "HELLO", to_lowercase("Hello") → "hello" |
| 김세윤 | [src/math_utils.py](src/math_utils.py) | add, subtract, multiply, divide | add(3, 2) → 5, subtract(3, 2) → 1, multiply(3, 2) → 6, divide(3, 2) → 1.5 |

문자열 유틸의 반환값은 함수의 동작 예시입니다. 현재 src/string_utils.py는 불필요한 matplotlib import로 인해 표준 라이브러리만 설치한 환경에서 실행되지 않습니다. divide의 두 번째 인자가 0이면 ValueError가 발생합니다.

# 4. 실행 및 검증

Python 3.10 이상에서 프로젝트 루트를 기준으로 실행합니다.

- 문자열 실행 예시: python -m src.string_utils
- 수학 테스트: python -m unittest discover -s tests -v

문서 작성 시 Python 3.14.6으로 검증한 결과, 문자열 모듈은 matplotlib import에서 실패했고 수학 테스트는 5개 중 4개 통과·1개 실패했습니다. 충돌 실습 후 남은 문제는 [충돌 해결 기록](docs/conflict-resolution.md)에 정리했습니다.

# 5. 주요 문서

- [협업 가이드](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [Git 트러블슈팅 기록](docs/troubleshooting-log.md)
- [제출 증빙](SUBMISSION.md)
