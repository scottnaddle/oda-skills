---
description: ODA 출장 일정을 수립한다. 체크리스트, 일정표, 비용 추정, 현지 유의사항.
argument-hint: "[출장지, 기간, 목적]"
---

# /plan-travel

현지 출장 전체 계획을 수립하는 워크플로우.

## 실행 흐름

travel-logistics 스킬을 실행한다.

1. 출장 개요 확인 (목적, 출장지, 기간, 출장자)
2. 사전 준비 체크리스트 생성
3. 현지 일정표 작성
4. 국가별 유의사항 정리
5. 비용 추정

## 완료 후 제안

- 출장 보고서를 작성하려면: → `/plan-mission` (oda-project-execution 플러그인)
- 통역 브리핑을 준비하려면: → interpreter-brief 스킬
