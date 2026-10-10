# Git 트러블슈팅 기록

## 1. git commit --amend

- 참여자: 김세윤(@sy364)
- 발생 상황: feature/seyun-amend-demo에서 amend-demo.txt를 만들고 최초 커밋 메시지를 update로 작성해 변경 목적이 드러나지 않았습니다.
- 사용 명령어:
  1. echo "Git amend practice" > amend-demo.txt
  2. git add amend-demo.txt
  3. git commit -m "update"
  4. git log -1 --oneline
  5. git commit --amend -m "docs: add Git amend practice example"
  6. git log -1 --oneline
  7. git push -u origin feature/seyun-amend-demo
- 결과: 파일 내용은 유지하고 메시지를 수정했습니다. 커밋은 94d54b8(update)에서 4f7346f(docs: add Git amend practice example)로 바뀌었으며 원격 push 후 PR #18이 병합되었습니다.
- 선택 이유 및 주의점: 최근 커밋의 메시지만 수정하기 위해 사용했습니다. 기존 커밋을 새 커밋으로 대체하므로 해시가 바뀌며, 공유한 커밋에 적용하면 팀원에게 영향을 줄 수 있어 push 전에 사용합니다.
- 증빙: [Issue #17](https://github.com/Beda28/B2-2.Team/issues/17), [PR #18](https://github.com/Beda28/B2-2.Team/pull/18), [수정 후 커밋](https://github.com/Beda28/B2-2.Team/commit/4f7346f), [팀원 작성 기록](https://github.com/Beda28/B2-2.Team/commit/ed552b2)

## 2. git reset --soft HEAD~1

- 증빙 확인 상태: 저장소·PR·제공된 스크린샷에서 실습 기록을 확인하지 못했습니다.
- 참여자:
- 발생 상황:
- 사용 명령어:
- 결과:
- 선택 이유 및 주의점:

## 3. git revert

- 증빙 확인 상태: 저장소·PR·로컬 reflog에서 revert 실행 및 되돌림 커밋을 확인하지 못했습니다. ba3409c(fix: return)는 반환식 변경 커밋으로, revert 증빙이 아닙니다.
- 참여자:
- 발생 상황:
- 사용 명령어:
- 결과:
- 선택 이유 및 주의점:

## 4. git stash / git stash pop

- 증빙 확인 상태: 저장소·PR·제공된 스크린샷에서 실습 기록을 확인하지 못했습니다.
- 참여자:
- 발생 상황:
- 사용 명령어:
- 결과:
- 선택 이유 및 주의점:
