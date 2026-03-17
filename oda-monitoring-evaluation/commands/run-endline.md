---
description: 종료평가 전과정을 실행한다. 평가 설계 → 영향평가 → 설문 분석 체이닝.
argument-hint: "[사업명. 기존 보고서, 설문 데이터, 베이스라인 자료 등 첨부]"
---

# /run-endline

사업 종료 시점의 종합 평가를 설계하고 실행하는 워크플로우.

## 실행 흐름

### Step 1: 종료평가 설계 (endline-evaluation)

DAC 6대 기준에 따른 종합 평가를 설계한다.
- 평가 질문 및 판단 기준 설정
- 평가 매트릭스 작성
- 데이터 수집 계획

### Step 2: 영향평가 방법론 (impact-assessment)

사업의 인과적 기여를 입증하기 위한 방법론을 설계한다.
- 사전-사후 비교 설계
- 기여도 분석(Contribution Analysis) 적용
- MSC(Most Significant Change) 스토리 수집 계획

### Step 3: 설문 분석 (survey-analysis)

엔드라인 설문 데이터를 분석한다.
- 베이스라인 대비 변화 분석
- 효과 크기(Effect Size) 산출
- 집단별 차이 분석

## 완료 후 산출물

종료평가 보고서 (DAC 기준별 분석 + 교훈 + 제언)

## 완료 후 제안

- 종료보고서에 통합하려면: → `/write-completion` (oda-project-execution 플러그인)
- 사례연구를 작성하려면: → `/write-case-study` (oda-knowledge-management 플러그인)
- 후속사업을 기획하려면: → `/plan-follow-on` (oda-knowledge-management 플러그인)
