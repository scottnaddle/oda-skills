# oda-project-execution

> ODA 사업 실행 관리 플러그인 — 착수보고, 진도보고, 종료보고, 회의록, 출장보고, 전문가 파견, 조달, 리스크 관리

## 스킬 (8)

| 스킬 | 설명 |
|---|---|
| `inception-report` | 착수보고서 — 착수미션 결과, 수정 PDM, 상세 실행계획, 베이스라인 조사 계획 |
| `progress-report` | 진도보고서 — 성과 달성, 활동 실적, 예산 집행, 이슈, 차기 계획 |
| `completion-report` | 종료보고서 — 성과 종합, DAC 자체평가, 교훈, 후속 제언 |
| `meeting-minutes` | 회의록 — 안건, 논의, 결정사항, Action Items. 전사본 자동 구조화 |
| `mission-report` | 출장보고서 — 일정, 면담, 현장관찰, 발견사항, 후속조치 |
| `expert-dispatch` | 전문가 파견 관리 — 파견 준비, 브리핑, 성과물 추적, 결과 보고 |
| `procurement-plan` | 조달계획 — 기자재/SW/서비스 조달 방법, 사양서, 일정 |
| `risk-register` | 리스크 등록부 — 식별, 확률×영향 매트릭스, 대응전략, 모니터링 |

## 커맨드 (6)

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/write-inception` | inception-report → risk-register → expert-dispatch | 착수보고 패키지 |
| `/write-progress` | progress-report (심화) | 분기/반기 진도보고 |
| `/write-completion` | completion-report → lessons-learned* | 종료보고 + 교훈 |
| `/log-meeting` | meeting-minutes (단독) | 회의록 작성/전사본 변환 |
| `/plan-mission` | mission-report + travel-logistics* | 출장 계획/보고 |
| `/manage-risks` | risk-register (업데이트) | 리스크 등록부 관리 |

## 발주처별 참조 파일

| 발주처 | 파일 | 위치 |
|---|---|---|
| KOICA | 분기보고 양식 | `progress-report/references/koica-quarterly-template.md` |
| ADB | 진도보고 양식 | `progress-report/references/adb-progress-template.md` |

## 사용 예시

```
# 착수보고서 작성
/write-inception 스리랑카 TVET 커리어 플랫폼 사업

# 분기 진도보고서
/write-progress 카자흐스탄 KSP — 2026년 1분기

# 회의록 (전사본에서)
/log-meeting [회의 전사본 첨부]

# 리스크 관리
/manage-risks LMS 서버 인프라 부족 이슈가 새로 발생했어

# 스킬 직접 사용 (자동 트리거)
이번 분기 진도보고서를 KOICA 양식으로 작성해줘
출장 보고서를 정리해줘
리스크 등록부를 업데이트하자
```

## 설치

```bash
claude plugin install oda-project-execution@oda-skills
```
