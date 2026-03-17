---
description: ODA 문서를 번역한다. 한→영 또는 영→한. ODA 전문 용어 일관성 유지.
argument-hint: "[번역 방향(ko→en / en→ko), 문서 텍스트 또는 파일 첨부]"
---

# /translate

ODA 문서의 전문 번역을 실행하는 워크플로우.

## 실행 흐름

translate-document 스킬을 실행한다.

1. 번역 방향 확인 (한→영 / 영→한)
2. 문서 유형 파악 (제안서, 보고서, 서한, TOR 등)
3. 발주처별 선호 표현 적용
4. ODA 전문 용어 대조표 기반 일관성 유지
5. 번역 결과물 제시

## 완료 후 제안

- 문법 교정이 필요하면: → `/proofread`
- 통역 브리핑 자료가 필요하면: → interpreter-brief 스킬
