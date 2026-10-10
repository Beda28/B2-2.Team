# Git 트러블슈팅 기록

## 1. git commit --amend

- **참여자:** 김세윤

- **발생 상황:**
  - `feature/seyun-amend-demo` 브랜치에서 실습 파일 `amend-demo.txt`를 생성함.
  - 최초 커밋 메시지를 `update`로 작성했으나, 변경 내용을 구체적으로 알 수 없어 수정이 필요했음.

- **사용 명령어:**
  ```bash
  echo "Git amend practice" > amend-demo.txt
  git add amend-demo.txt
  git commit -m "update"
  git log -1 --oneline

  git commit --amend -m "docs: add Git amend practice example"
  git log -1 --oneline
  git push -u origin feature/seyun-amend-demo
  ```

- **결과:**
  - 수정 전: `94d54b8` (`update`)
  - 수정 후: `4f7346f` (`docs: add Git amend practice example`)
  - 파일 내용은 유지하면서 커밋 메시지를 수정함.
  - 커밋 해시가 변경되는 것을 확인했고, 원격 저장소에 push까지 완료함.

- **선택 이유 및 주의점:**
  - `git commit --amend`는 최근 커밋의 메시지나 내용을 수정할 때 사용함.
  - 기존 커밋을 수정하는 대신 새로운 커밋으로 대체하므로 커밋 해시가 변경됨.
  - 이미 원격에 공유한 커밋을 수정하면 다른 팀원의 작업에 영향을 줄 수 있으므로, push하기 전 로컬 커밋에서 사용하는 것이 안전함.

## 2. git reset --soft HEAD~1

- 참여자:
- 발생 상황:
- 사용 명령어:
- 결과:
- 선택 이유 및 주의점:

## 3. git revert

- 참여자:
- 발생 상황:
- 사용 명령어:
- 결과:
- 선택 이유 및 주의점:

## 4. git stash / git stash pop

- 참여자:
- 발생 상황:
- 사용 명령어:
- 결과:
- 선택 이유 및 주의점:
