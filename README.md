# ODA Skills Marketplace

> **해외사업부 ODA 사업관리를 위한 AI 스킬 마켓플레이스**
> 수주 → 제안 → 실행 → 평가 → 확산 — ODA 사업 라이프사이클 전 과정 지원

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## 시작하기

수주 기회를 분석하고 싶다면 → `/bid-analyze`
제안서를 작성하고 싶다면 → `/draft-proposal`
진도보고서를 쓰고 싶다면 → `/write-progress`
로지컬 프레임워크를 만들고 싶다면 → `/build-logframe`

---

## 왜 ODA Skills인가

일반적인 AI는 텍스트를 준다. ODA Skills는 **구조**를 준다.

각 스킬은 ODA 사업관리의 검증된 프레임워크 — PCM, 로지컬 프레임워크, DAC 평가기준, KOICA/ADB 양식 — 를 내장하고 단계별로 가이드한다. 제안서 한 건을 쓰든, 수주 분석을 하든, 발주처가 요구하는 구조와 품질을 갖춘 산출물이 나온다.

---

## 구조: Skills, Commands, Plugins

**Skills** — 도메인 지식. 각 스킬은 특정 ODA 업무(RFP 분석, 로지컬 프레임워크 작성, 리스크 관리 등)에 대한 프레임워크와 절차를 제공한다. 대화 맥락에 맞게 자동으로 로드된다.

**Commands** — 워크플로우. `/bid-analyze` 같은 슬래시 커맨드로 여러 스킬을 체이닝하여 end-to-end 프로세스를 실행한다.

**Plugins** — 도메인 패키지. 관련 스킬과 커맨드를 하나의 설치 단위로 묶는다.

---

## 설치

### Claude Cowork

1. **Customize** → **Browse plugins** → **Personal** → **+**
2. **Add marketplace from GitHub**
3. 입력: `scottnaddle/oda-skills`

### Claude Code

```bash
# 마켓플레이스 등록
claude plugin marketplace add scottnaddle/oda-skills

# 개별 플러그인 설치
claude plugin install oda-bid-intelligence@oda-skills
claude plugin install oda-proposal-writing@oda-skills
claude plugin install oda-project-execution@oda-skills
```

### 다른 AI 도구 (스킬만 사용)

```bash
# Gemini CLI
for plugin in oda-*/; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done

# Cursor / Codex CLI
for plugin in oda-*/; do
  cp -r "$plugin/skills/"* .cursor/skills/ 2>/dev/null
done
```

---

## 플러그인 목록

### Phase 1 — MVP ✅

**1. [oda-bid-intelligence](oda-bid-intelligence/)** — 수주 정보 분석 (6 skills, 3 commands)

RFP/TOR 분석, 경쟁사 매핑, 컨소시엄 전략, 입찰 자가평가, 조달공고 모니터링, ODA 시장 환경 분석.

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/bid-analyze` | analyze-rfp → competitor-mapping → consortium-strategy → bid-scoring | RFP 전체 수주 분석 |
| `/scan-procurement` | procurement-monitor → oda-landscape | 공고 스캔 + 시장 분석 |
| `/assess-competition` | competitor-mapping → consortium-strategy | 경쟁 분석 + 컨소시엄 |

**2. [oda-proposal-writing](oda-proposal-writing/)** — 제안서 작성 (7 skills, 4 commands)

기술제안서, 로지컬 프레임워크, 예산서, 워크플랜, 전문가 배치, TOR, 품질 검토.

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/draft-proposal` | write-technical-proposal → write-logical-framework → write-workplan → expert-roster | 제안서 초안 전과정 |
| `/build-logframe` | write-logical-framework (심화) | 로지컬 프레임워크 집중 |
| `/plan-budget` | write-budget → write-workplan | 예산 + 워크플랜 연계 |
| `/review-proposal` | proposal-quality-check → bid-scoring* | 품질 검토 + 자가 평가 |

**3. [oda-project-execution](oda-project-execution/)** — 사업 실행 관리 (8 skills, 6 commands)

착수보고, 진도보고, 종료보고, 회의록, 출장보고, 전문가 파견, 조달, 리스크 관리.

| 커맨드 | 체이닝 | 설명 |
|---|---|---|
| `/write-inception` | inception-report → risk-register → expert-dispatch | 착수보고 패키지 |
| `/write-progress` | progress-report (심화) | 분기/반기 진도보고 |
| `/write-completion` | completion-report → lessons-learned* | 종료보고 + 교훈 |
| `/log-meeting` | meeting-minutes | 회의록 / 전사본 변환 |
| `/plan-mission` | mission-report + travel-logistics* | 출장 계획 / 보고 |
| `/manage-risks` | risk-register (업데이트) | 리스크 등록부 관리 |

### Phase 2 — 확장 (예정)

4. **oda-country-research** — 수원국 연구 (6 skills)
5. **oda-monitoring-evaluation** — 모니터링 & 평가 (7 skills)
6. **oda-toolkit** — 유틸리티 (7 skills)

### Phase 3 — 완성 (예정)

7. **oda-partnership** — 파트너십 & 협력 (6 skills)
8. **oda-knowledge-management** — 지식관리 & 확산 (6 skills)

---

## 대응 발주처 & 수원국

**발주처**: KOICA, ADB, UNESCO, NIPA, NIA — 각 발주처별 양식/평가기준이 `references/`에 번들링

**수원국**: 카자흐스탄, 베트남, 캄보디아, 스리랑카, 우즈베키스탄, 필리핀 (확장 가능)

---

## 사업 라이프사이클 워크플로우

```
수주 전     /scan-procurement → /bid-analyze → /research-country
   ↓
제안서      /draft-proposal → /plan-budget → /review-proposal
   ↓
착수        /write-inception
   ↓
실행        /write-progress → /log-meeting → /plan-mission → /manage-risks
   ↓
종료        /write-completion → /write-case-study → /plan-follow-on
   ↓
후속사업 → 재수주 (↑ 순환)
```

---

## 현황

| 구분 | 수량 |
|---|---|
| 플러그인 (Phase 1) | 3개 |
| 스킬 | 21개 |
| 커맨드 | 13개 |
| 참조 파일 (references) | 14개 |
| 대응 발주처 | 5개 (KOICA, ADB, UNESCO, NIPA, NIA) |

---

## 기여

버그, 오타 → PR 직접 제출
새 스킬, 커맨드 → Issue로 먼저 논의

**원칙:**
- Skills는 명사 (도메인 지식), Commands는 동사 (워크플로우)
- 모든 스킬은 frontmatter에 `name`과 `description` 필수
- SKILL.md는 500줄 이내, 상세 참조는 `references/`로 분리
- 스킬 이름은 디렉토리명과 일치, 소문자-하이픈

---

## 라이선스

MIT
