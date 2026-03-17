# oda-proposal-writing

> ODA 사업 제안서 작성 플러그인 — 기술제안서, 로지컬 프레임워크, 예산서, 워크플랜, 전문가 배치, TOR, 품질 검토

## 스킬 (7)

| 스킬 | 설명 |
|---|---|
| `write-technical-proposal` | 기술제안서 8섹션 작성 — 사업이해, 목표, 방법론, 활동, 인력, 관리, 범분야, 지속가능성 |
| `write-logical-framework` | PCM 기반 로지컬 프레임워크(PDM) — 목표 체계, OVI, MoV, 가정 |
| `write-budget` | 예산서 작성 — 발주처별 비목 체계, 단가 산정, 비목 배분 |
| `write-workplan` | 워크플랜 수립 — WBS, 간트차트, 마일스톤, 인력 투입 일정 |
| `expert-roster` | 전문가 투입 계획 — 팀 구성, M/M 산정, CV 전략 |
| `write-tor` | TOR 작성 — 사업 TOR, 전문가 TOR, KOICA/ADB 양식 |
| `proposal-quality-check` | 제안서 품질 검토 — RFP 충족도, 논리 일관성, 차별화, 가독성 |

## 커맨드 (4)

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/draft-proposal` | write-technical-proposal → write-logical-framework → write-workplan → expert-roster | 제안서 초안 전과정 |
| `/build-logframe` | write-logical-framework (심화) | 로지컬 프레임워크 집중 작성 |
| `/plan-budget` | write-budget → write-workplan | 예산서 + 워크플랜 연계 |
| `/review-proposal` | proposal-quality-check → bid-scoring* | 품질 검토 + 자가 평가 |

## 발주처별 참조 파일

| 발주처 | 파일 | 위치 |
|---|---|---|
| KOICA | 제안서 양식 | `write-technical-proposal/references/koica-proposal-template.md` |
| KOICA | 예산 규칙 | `write-budget/references/koica-budget-rules.md` |
| ADB | 제안서 양식 | `write-technical-proposal/references/adb-proposal-template.md` |
| ADB | 비목 가이드 | `write-budget/references/adb-cost-categories.md` |
| 공통 | PCM 로지컬 프레임워크 | `write-logical-framework/references/pcm-logframe-guide.md` |
| 공통 | TOR 양식 | `write-tor/references/tor-template.md` |

## 사용 예시

```
# 제안서 전과정 작성
/draft-proposal 카자흐스탄 디지털 교육 혁신 역량강화 — KOICA 기술협력

# 로지컬 프레임워크 집중 작성
/build-logframe 스리랑카 TVET 커리어 플랫폼 구축

# 예산서 작성
/plan-budget 우즈베키스탄 간호교육 역량강화 — 총 15억원, 3년

# 제안서 검토
/review-proposal [제안서 파일 첨부]

# 스킬 직접 사용 (자동 트리거)
이 사업의 로지컬 프레임워크를 만들어줘
전문가 팀 구성을 어떻게 하면 좋을까?
이 제안서에서 빠진 게 없는지 검토해줘
```

## 설치

```bash
claude plugin install oda-proposal-writing@oda-skills
```
