# oda-bid-intelligence

> ODA 사업 수주 정보 분석 플러그인 — RFP 분석부터 경쟁사 매핑, 컨소시엄 전략, 입찰 자가평가까지

## 스킬 (6)

| 스킬 | 설명 |
|---|---|
| `analyze-rfp` | RFP/TOR 문서 분석 — 요구사항, 배점, 자격요건, 리스크 추출 |
| `competitor-mapping` | 경쟁사 역량 비교 분석 — 실적, 인력, 네트워크, 가격 매트릭스 |
| `consortium-strategy` | 컨소시엄 구성 전략 — 역할 배분, 지분율, 파트너 평가 |
| `bid-scoring` | 제안서 자가평가 — 배점표 기반 채점, Go/No-Go 판단 |
| `procurement-monitor` | 조달공고 모니터링 — 핵심정보 추출, 적합성 판단 |
| `oda-landscape` | ODA 시장 환경 분석 — 트렌드, 발주처 전략, 기회 식별 |

## 커맨드 (3)

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/bid-analyze` | analyze-rfp → competitor-mapping → consortium-strategy → bid-scoring | RFP 수령 후 전체 수주 분석 |
| `/scan-procurement` | procurement-monitor → oda-landscape | 공고 스캔 + 시장 맥락 분석 |
| `/assess-competition` | competitor-mapping → consortium-strategy | 경쟁 분석 + 컨소시엄 전략 |

## 발주처별 참조 파일

| 발주처 | 파일 | 위치 |
|---|---|---|
| KOICA | RFP 분석 가이드 | `analyze-rfp/references/koica-rfp-guide.md` |
| KOICA | 전략 분석 | `oda-landscape/references/koica-strategy.md` |
| ADB | RFP 분석 가이드 | `analyze-rfp/references/adb-rfp-guide.md` |
| ADB | 전략 분석 | `oda-landscape/references/adb-strategy.md` |
| UNESCO | 전략 분석 | `oda-landscape/references/unesco-strategy.md` |
| 공통 | 배점표 기준 | `bid-scoring/references/scoring-criteria.md` |

## 사용 예시

```
# RFP를 첨부하여 전체 수주 분석
/bid-analyze [RFP 파일 첨부]

# 특정 사업의 경쟁 환경 분석
/assess-competition 카자흐스탄 디지털 교육 혁신 사업

# 조달공고 스캔
/scan-procurement [공고 텍스트 붙여넣기]

# 스킬 직접 사용 (자동 트리거)
이 KOICA 공고에서 평가기준 배점표를 정리해줘
예상 경쟁사를 분석해줘
컨소시엄을 어떻게 구성하면 좋을까?
```

## 설치

```bash
# 마켓플레이스에서 설치
claude plugin install oda-bid-intelligence@oda-skills

# 로컬 테스트
claude --plugin-dir ./oda-bid-intelligence
```
