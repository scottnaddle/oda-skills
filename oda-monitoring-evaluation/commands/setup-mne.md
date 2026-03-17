---
description: M&E 체계를 초기 설계한다. 성과 프레임워크 설계 → 지표 상세 정의를 체이닝한다.
argument-hint: "[사업명. 로지컬 프레임워크 또는 PDM이 있으면 첨부]"
---

# /setup-mne

사업 착수 단계에서 M&E 체계 전체를 설계하는 워크플로우.

## 실행 흐름

### Step 1: 성과 프레임워크 설계 (design-results-framework)

사업의 변화이론과 성과 체인을 구조화한다.
- Theory of Change 서술
- 성과 체인 구성 (투입→활동→산출→성과→영향)
- DAC 기준 매핑
- 데이터 수집 계획 초안
- M&E 일정 수립

사용자에게 프레임워크를 제시하고 확인받은 후 다음 단계로 진행한다.

### Step 2: 지표 상세 정의 (define-indicators)

각 성과 수준의 지표를 SMART 기준으로 상세 정의한다.
- 지표 시트(Indicator Reference Sheet) 작성
- 기초선 확보 전략 수립
- 목표치 설정 및 근거
- 데이터 수집 캘린더 확정

## 완료 후 산출물

```
# M&E 체계 설계서: [사업명]

## Part 1: 성과 프레임워크
[변화이론, 성과 체인, DAC 매핑, M&E 일정]

## Part 2: 성과지표 정의서
[지표 요약표, 지표별 상세 시트, 기초선 계획, 수집 캘린더]
```

## 완료 후 제안

- 베이스라인 조사를 설계하려면: → `/assess-needs` (oda-country-research 플러그인)
- 착수보고서에 포함하려면: → `/write-inception` (oda-project-execution 플러그인)
- 제안서 로지컬 프레임워크와 연동하려면: → `/build-logframe` (oda-proposal-writing 플러그인)
