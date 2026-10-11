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

- 참여자: 방승규(@Beda28)
- 상황: feature/bsg-revert-demo에서 test.txt에 임시 문구를 추가한 커밋 0712894를 먼저 push한 뒤, 공유된 변경을 취소했습니다.
- 실행 명령어:
  1. git revert --no-edit 0712894
  2. git push origin feature/bsg-revert-demo
- 결과: 취소 커밋 1404e0d가 생성되고 임시 문구가 제거되었습니다. 파일은 실습 전으로 복구되었으며 두 커밋 모두 원격 이력에 남았습니다.
- 선택 이유 및 주의점: 이미 공유한 이력을 유지하려고 reset 대신 revert를 사용했습니다. revert는 기존 커밋을 삭제하지 않고 반대 변경을 새 커밋으로 기록합니다. 이후 같은 부분이 수정되었다면 충돌이 발생할 수 있습니다.
- 증빙: [추가 0712894](https://github.com/Beda28/B2-2.Team/commit/07128946f5431684333de54de746d974f38558b3), [취소 1404e0d](https://github.com/Beda28/B2-2.Team/commit/1404e0d1a80c3f28a7f0f90a9d0a4d48abe30bf0)

## 4. git stash / git stash pop

- 참여자: 김준원(@jwyssey)
- 상황: feature/kjw-list-utils에서 리스트 유틸을 커밋 전 작업하던 중(README.md 수정, 새 파일 src/list_utils.py), 최신 main에서 stash 기록용 브랜치를 만들어야 했습니다. 미완성 작업을 커밋하지 않고 브랜치를 전환하려고 stash를 사용했습니다.
- 실행 명령어:
  1. git status --short
  2. git stash push -u -m "wip: list utils before creating stash docs branch"
  3. git stash list
  4. git status --short
  5. git switch main
  6. git pull --ff-only
  7. git switch -c feature/kjw-stash-docs
  8. git switch feature/kjw-list-utils
  9. git stash pop
  10. git status --short
  11. git stash list
- 실행 결과(2026-10-11, 주요 출력):

  ```txt
  $ git status --short
   M README.md
  ?? src/list_utils.py
  $ git stash push -u -m "wip: list utils before creating stash docs branch"
  Saved working directory and index state On feature/kjw-list-utils: wip: list utils before creating stash docs branch
  $ git stash list
  stash@{0}: On feature/kjw-list-utils: wip: list utils before creating stash docs branch
  $ git status --short
  (출력 없음)
  $ git stash pop
  Dropped refs/stash@{0} (d7f4ccb41a87285046d1cff8277741b6eeae8eb3)
  $ git status --short
   M README.md
  ?? src/list_utils.py
  $ git stash list
  (출력 없음)
  ```

- 결과: stash 직후 git status --short 출력이 비어 브랜치를 전환할 수 있었고, pop 후 README.md 수정과 src/list_utils.py가 그대로 복원되었습니다. 보관 항목 d7f4ccb는 pop과 함께 삭제되어 stash 목록이 비었습니다. 복원한 작업은 커밋 후 PR #22로 올렸습니다.
- 선택 이유 및 주의점: 미완성 작업을 wip 같은 의미 없는 커밋으로 남기지 않으려고 stash를 사용했습니다. 새 파일(untracked)은 -u 없이 보관되지 않고 작업 디렉터리에 남아 전환한 브랜치로 따라오므로 -u를 붙였습니다. stash는 로컬에만 저장되어 팀원과 공유되지 않으며, pop 중 충돌이 나면 stash가 삭제되지 않으므로 충돌 해결 후 git stash drop으로 정리합니다.
- 증빙: [Issue #20](https://github.com/Beda28/B2-2.Team/issues/20), [PR #23](https://github.com/Beda28/B2-2.Team/pull/23), [복원 후 커밋 9f63c26](https://github.com/Beda28/B2-2.Team/commit/9f63c26dfce4a3385b45ada0e307c486ee71ea68)
