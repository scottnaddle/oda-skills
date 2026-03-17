---
description: 종료보고서를 작성하고 교훈을 추출한다. 종료보고 → 교훈 도출을 체이닝한다.
argument-hint: "[사업명. 기존 진도보고서, 성과 데이터가 있으면 첨부]"
---

# /write-completion

사업 종료 단계에서 최종 보고서와 교훈을 작성하는 워크플로우.

## 실행 흐름

### Step 1: 종료보고서 (completion-report)

전체 사업 성과를 종합하는 최종 보고서를 작성한다.
- PDM 지표별 최종 달성 현황
- 예산 최종 정산
- DAC 기준 자체 평가
- 지속가능성 평가

### Step 2: 교훈 추출 (lessons-learned — oda-knowledge-management 연계)

사업 경험에서 체계적으로 교훈을 도출한다.
- 성공 요인 분석
- 개선 필요 사항 분석
- 교훈의 일반화 가능성
- 향후 적용 제언

## 완료 후 제안

- 성공사례를 작성하려면: → `/write-case-study` (oda-knowledge-management 플러그인)
- 후속사업을 기획하려면: → `/plan-follow-on` (oda-knowledge-management 플러그인)
