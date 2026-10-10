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
- 실습일: 2026-10-10
- 발생 상황: 최신 main(856c92e)에서 feature/bsg-revert-demo를 생성했습니다. test.txt에 Temporary line for revert practice. 한 줄을 추가하고 원격에 push한 뒤, 공유된 변경을 취소하는 상황을 실습했습니다.

### 사용 명령어와 실행 순서

1. git switch main
2. git pull --ff-only origin main
3. git switch -c feature/bsg-revert-demo
4. git hash-object test.txt로 기존 파일 해시를 확인했습니다.
5. test.txt에 실습 문구 한 줄을 추가했습니다.
6. git add test.txt
7. git commit -m "docs: add temporary line for revert practice"
8. git push -u origin feature/bsg-revert-demo
9. git revert --no-edit 0712894
10. git log -3 --oneline과 git show --format=full HEAD로 이력을 확인했습니다.
11. git hash-object test.txt와 git diff --exit-code 856c92e HEAD -- test.txt로 파일 복구를 확인했습니다.
12. git diff --exit-code '0712894^' HEAD로 전체 파일 트리도 실습 전과 같은지 확인했습니다.
13. git push origin feature/bsg-revert-demo

### 결과

| 단계 | 커밋 | test.txt 내용 |
| --- | --- | --- |
| 실습 전 | 856c92e | Simple branch test. 한 줄 |
| 임시 문구 추가 및 push | 0712894 | 기존 문구와 Temporary line for revert practice. 두 줄 |
| revert 및 push | 1404e0d | Simple branch test. 한 줄로 복구 |

- revert는 충돌 없이 완료되었고, 한 줄을 삭제하는 새 커밋 1404e0d를 생성했습니다.
- 실습 전후 파일 해시는 cd2f830b28b552d0ef056019f541a73bd1f0641e로 같았습니다.
- 파일 비교와 전체 트리 비교 모두 출력 없이 종료 코드 0을 반환했습니다.
- 추가 커밋 0712894와 취소 커밋 1404e0d가 모두 이력에 남았고 일반 push에 성공했습니다. 강제 push나 reset은 사용하지 않았습니다.

### 결과가 나오는 이유와 선택 이유

git revert는 지정한 커밋이 만든 변경의 반대 패치를 현재 브랜치에 적용하고 새 커밋으로 기록합니다. 0712894가 한 줄을 추가했으므로 1404e0d는 그 한 줄을 삭제했습니다. 중간에 다른 변경이 없어 파일 내용과 전체 트리가 실습 전과 같아졌지만, 두 커밋이 추가되었으므로 HEAD와 이력은 실습 전과 다릅니다.

이미 원격에 공유한 변경을 이력 재작성 없이 취소하려고 revert를 선택했습니다. --no-edit는 기본 취소 메시지를 그대로 사용하는 옵션이며, 커밋 생성을 생략하지 않습니다. 이후 커밋이 같은 부분을 수정했다면 revert 과정에서도 충돌이 발생할 수 있습니다.

### 증빙

- [실습 브랜치 이력](https://github.com/Beda28/B2-2.Team/commits/feature/bsg-revert-demo/)
- [추가 커밋 0712894](https://github.com/Beda28/B2-2.Team/commit/07128946f5431684333de54de746d974f38558b3)
- [취소 커밋 1404e0d](https://github.com/Beda28/B2-2.Team/commit/1404e0d1a80c3f28a7f0f90a9d0a4d48abe30bf0)

## 4. git stash / git stash pop

- 증빙 확인 상태: 저장소·PR·제공된 스크린샷에서 실습 기록을 확인하지 못했습니다.
- 참여자:
- 발생 상황:
- 사용 명령어:
- 결과:
- 선택 이유 및 주의점:
