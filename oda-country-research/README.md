# oda-country-research

> ODA 수원국 연구 플러그인 — 교육 프로파일, 니즈 평가, 이해관계자 매핑, 정책 분석, 디지털 준비도, 기초선 조사

## 스킬 (6)

| 스킬 | 설명 |
|---|---|
| `country-education-profile` | 수원국 교육 프로파일 — 체계, 통계, ICT, 정책, 개발파트너 |
| `needs-assessment` | 니즈 평가 — 갭 분석, 우선순위, 수요-공급 매핑 |
| `stakeholder-mapping` | 이해관계자 분석 — Power×Interest, 소통 전략 |
| `policy-landscape` | 정책 환경 — 교육전략, ICT정책, 규제, 예산 |
| `digital-readiness` | 디지털 준비도 — 인프라, 기기, 교원역량, 콘텐츠, 정책 |
| `baseline-survey-design` | 기초선 조사 설계 — 방법론, 표본, 도구, 윤리 |

## 커맨드 (3)

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/research-country` | profile → policy → digital → needs | 국가 종합 연구 |
| `/map-stakeholders` | stakeholder-mapping (심화) | 이해관계자 분석 |
| `/assess-needs` | needs-assessment → baseline-survey-design | 니즈 + 기초선 |

## 국가별 참조 파일 (6개국)

카자흐스탄, 베트남, 캄보디아, 스리랑카, 우즈베키스탄, 필리핀

## 설치

```bash
claude plugin install oda-country-research@oda-skills
```
