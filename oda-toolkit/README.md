# oda-toolkit

> ODA 사업 유틸리티 플러그인 — 번역, 출장, 계약, 발표, 이메일, 통역, 교정

## 스킬 (7)

| 스킬 | 설명 |
|---|---|
| `translate-document` | ODA 문서 번역 — 한↔영, 전문 용어 일관성, 발주처별 표현 |
| `travel-logistics` | 출장 일정 관리 — 체크리스트, 일정표, 비용, 현지 유의사항 |
| `contract-review` | 계약서 검토 — 핵심 조항 체크, 리스크 포인트 식별 |
| `presentation-script` | 발표 대본 — 슬라이드별 스크립트, Q&A 준비, 통역 친화 문장 |
| `email-draft` | 업무 이메일 — 발주처/파트너/전문가별 한영 템플릿 |
| `interpreter-brief` | 통역 브리핑 — 용어 대조표, 약어, 예상 발언, 민감 사안 |
| `grammar-check-ko-en` | 한영 문법 교정 — 맞춤법, 스타일, 번역투, ODA 특화 표현 |

## 커맨드 (4)

| 커맨드 | 설명 |
|---|---|
| `/translate` | ODA 문서 번역 (한→영 / 영→한) |
| `/plan-travel` | 출장 계획 수립 |
| `/draft-email` | 업무 이메일 초안 |
| `/proofread` | 문법/스타일 교정 |

## 사용 예시

```
/translate 이 착수보고서를 영어로 번역해줘
/plan-travel 우즈베키스탄 타슈켄트 3/20~3/27 간호교육 사업 착수미션
/draft-email KOICA 담당자에게 분기보고서 제출 메일
/proofread [제안서 텍스트 붙여넣기]

# 스킬 직접 사용
이 계약서에서 리스크 포인트를 찾아줘
PSC 발표 대본을 써줘 — 통역 있는 상황
내일 통역사 브리핑 자료를 준비해줘
```

## 설치

```bash
claude plugin install oda-toolkit@oda-skills
```
