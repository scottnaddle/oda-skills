# oda-partnership

> ODA 파트너십 & 협력 플러그인 — 발주처 전략, 현지 파트너, MOU, 하도급, PSC 회의, 정부 대응

## 스킬 (6)

| 스킬 | 설명 |
|---|---|
| `donor-strategy` | 발주처 접근 전략 — KOICA/ADB/UNESCO 기관별 특성, 조달, 관계 구축 |
| `local-partner-mapping` | 현지 파트너 발굴 — 역량 평가, 듀딜리전스, 파트너십 구조 |
| `mou-draft` | MOU/MOA 초안 — 한영 이중언어, 핵심 조항, 표준 양식 |
| `subcontract-scope` | 하도급 범위서(SOW) — 업무, 성과물, 일정, 지불, 품질 |
| `psc-preparation` | PSC 회의 준비 — 안건, 현황, 의사결정 사항, 발표 자료 |
| `government-liaison` | 정부 대응 — 카운터파트 소통, 공식 서한, 승인 프로세스 |

## 커맨드 (3)

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/plan-partnership` | donor-strategy → local-partner → government-liaison | 파트너십 종합 전략 |
| `/draft-mou` | mou-draft (단독) | MOU/MOA 초안 작성 |
| `/prepare-psc` | psc-preparation → progress-report* | PSC 회의 준비 |

## 설치

```bash
claude plugin install oda-partnership@oda-skills
```
