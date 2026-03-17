# oda-knowledge-management

> ODA 지식관리 & 확산 플러그인 — 교훈, 성공사례, 사례연구, 성과확산, 후속사업, 역량이전

## 스킬 (6)

| 스킬 | 설명 |
|---|---|
| `lessons-learned` | 교훈 추출 — 성공/개선 요인, 일반화, 적용 계획 |
| `success-story` | 성공사례 — 수혜자 스토리텔링, 변화 전후, 홍보 양식 |
| `case-study` | 사례연구 — 연구 질문, 맥락, 분석, 교훈, 학술+실무 균형 |
| `dissemination-plan` | 성과확산 — 대상별 채널, 메시지, 자료, 일정 |
| `follow-on-concept` | 후속사업 개념서 — 확대/심화/복제, 성과 기반 기획 |
| `capacity-transfer-plan` | 역량이전 — 4단계 이전, 자립 기준, 출구전략, 인수인계 |

## 커맨드 (3)

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/extract-lessons` | lessons-learned → capacity-transfer-plan | 교훈 + 역량이전 |
| `/write-case-study` | case-study → success-story | 사례연구 + 성공사례 |
| `/plan-follow-on` | follow-on-concept → dissemination-plan | 후속사업 + 확산 |

## 사용 예시

```
/extract-lessons 카자흐스탄 KSP 디지털 교육 사업
/write-case-study 스리랑카 TVET 플랫폼 — 여성 수혜자 변화 사례
/plan-follow-on 우즈베키스탄 간호교육 사업 — 2기 확대

# 스킬 직접 사용
이 사업에서 배운 교훈을 정리해줘
성공사례를 KOICA 홍보 양식으로 써줘
역량이전 계획을 세워야 하는데 도와줘
```

## 설치

```bash
claude plugin install oda-knowledge-management@oda-skills
```
