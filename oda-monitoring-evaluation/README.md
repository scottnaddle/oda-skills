# oda-monitoring-evaluation

> ODA 사업 모니터링 & 평가 플러그인 — 성과 프레임워크, 지표 설계, 중간/종료 평가, 영향 평가, 설문 분석, 데이터 품질

## 스킬 (7)

| 스킬 | 설명 |
|---|---|
| `design-results-framework` | 성과 프레임워크 설계 — 변화이론, 성과 체인, DAC 매핑, M&E 일정 |
| `define-indicators` | 성과지표 정의 — SMART 검증, 지표 시트, 기초선/목표치, 수집 계획 |
| `midterm-evaluation` | 중간평가 — 평가 TOR, 평가 매트릭스, 보고서 (발견-결론-제언) |
| `endline-evaluation` | 종료평가 — DAC 6대 기준별 분석, 종합 등급, 교훈, 후속 제언 |
| `impact-assessment` | 영향평가 방법론 — 사전-사후 비교, 기여도 분석, MSC, 준실험 설계 |
| `survey-analysis` | 설문 분석 — 기술통계, 교차분석, 만족도, 사전-사후, 텍스트 분석 |
| `data-quality-check` | 데이터 품질 점검 — 완전성, 정확성, 일관성, 적시성, 신뢰성 |

## 커맨드 (4)

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/setup-mne` | design-results-framework → define-indicators | M&E 체계 초기 설계 |
| `/run-midterm` | midterm-evaluation → data-quality-check → survey-analysis | 중간평가 전과정 |
| `/run-endline` | endline-evaluation → impact-assessment → survey-analysis | 종료평가 전과정 |
| `/analyze-survey` | data-quality-check → survey-analysis | 설문 데이터 분석 |

## 참조 파일

| 파일 | 위치 |
|---|---|
| PCM 성과지표 가이드 (표준 지표 라이브러리 포함) | `design-results-framework/references/pcm-indicators-guide.md` |

## 사용 예시

```
# M&E 체계 설계
/setup-mne 카자흐스탄 디지털 교육 혁신 사업

# 중간평가 실행
/run-midterm 스리랑카 TVET 사업 — 기존 진도보고서와 설문 데이터 참조

# 설문 분석
/analyze-survey [설문 CSV 파일 첨부]

# 스킬 직접 사용 (자동 트리거)
이 사업의 성과지표를 SMART 기준으로 검토해줘
DAC 기준에 맞춰 종료평가 프레임워크를 잡아줘
이 데이터 품질에 문제가 없는지 점검해줘
사업의 영향을 어떻게 측정하면 좋을까?
```

## 설치

```bash
claude plugin install oda-monitoring-evaluation@oda-skills
```
