# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A Deep Research prompt system for a quantitative whitepaper on largemouth bass (*Micropterus salmoides*) fishing ecology in Taiwan. Each `*-instruction.md` file is a structured research prompt that forces strict scope, quantification, and output format compliance when executed as Deep Research.

## Build

```
python build.py
```

Reads `台灣大嘴黑鱸白皮書.md`, outputs `docs/index.html` (self-contained; no external assets except Google Fonts). Requires `markdown` package.

## Skills (Claude Code)

Skills live in `.claude/skills/{name}/SKILL.md`. After editing a SKILL.md, repackage:

```
python .claude/skills/打包技能.py
```

This re-zips each `SKILL.md` into a `.skill` file. The two active skills are:
- `twbass-audit` — 5-phase audit of research reports against instruction.md + Phase 6 re-run necessity scoring with Gemini/Claude tool recommendation
- `twbass-pipeline-manager` — pipeline status tracking and upstream dependency resolution

## File Naming Convention

| Pattern | Meaning |
|---------|---------|
| `{卷號}：{主題}-instruction.md` | Research prompt (scope/output source of truth) |
| `{卷號}_{主題}.docx` | Research report, original run (no number suffix) |
| `{卷號}{N}_{主題}.docx` | Research report, vN (e.g. `0A1`, `0D1` = Zone-B updated) |
| `0`–`4` (no letter suffix) | Master volume specs — reference only, **not for direct execution** |

Always use the highest-numbered version as upstream input. The README version table is authoritative for current valid versions.

## Pipeline Architecture

```
0A1 ─┐
     ├─> 0C1 ──> 0D1
0B  ─┘

0D1 ──> 1A / 1B1 / 2A / 2B         (1A ∥ 1B1 can run in parallel)
0D1 + 2A ──> 2C                     (2A ∥ 2B can run in parallel; 2C waits for 2A)
0D1 + 1A + 2A + 2B ──> 3A
0D1 + 1B1 + 2A + 2B + 3A ──> 3B1
0D1 + 4A ──> 4B

SUP-A ──> 3A (Open_Assumptions) / 3B1 (Unresolved_Dependencies)
SUP-B ──> 1B1 (V1B-05/06) / 3B1 / 4A (CI-03/04)
SUP-C ──> 3A (V3A-06) / 3B1 (Foraging Forays)
SUP-D ──> 2A / 2B / 3A / 3B1 (behavioral mechanism framework)
SUP-E ──> 2A / 1B1 / 3B1 (Taiwan ecological calendar + OFT threshold)
SUP-D ∥ SUP-E (parallel; no inter-dependency; downstream integration in 2A/3A/3B1)
```

- `0A` and `0B` are fully independent and can run in parallel
- Most volumes after `0D` only need `0D1` as primary upstream; add earlier sub-volumes only when extra detail is needed
- `2C` requires `2A` (visual wavelength attenuation conclusions)
- `3A/3B` can optionally supplement with `2C`

## Volume Scope Boundaries

Scope violations are tracked in `PATCH_NOTES.md`. Each volume has hard boundaries:

| Volume | Scope | Forbidden |
|--------|-------|-----------|
| 0A | 四季氣候物理量化、迎風/背風差異、冷氣團 | 土壤、水體、魚類行為 |
| 0B | 極育土/弱育土、pH、Eh、絮凝、Fe/H₂S | 氣候細節、魚類行為 |
| 0C | 六大水體四季溫度/溶氧/濁度動態 | 氣候重寫、魚類生態 |
| 0D | Baseline_Facts、Waterbody_Model_Table、Lag Effect | 不重寫 0A–0C 正文 |
| 1A | 懸浮、氣壓、光照、月相對行為的短時觸發 | 長期棲位模型 (→1B) |
| 1B | 非繁衍期棲位偏好、風生流、微循環 | 繁衍行為 |
| 2A | OFT、飼料印記、Reaction Strike、水色視覺衰減 | 側線/聲學 (→2B)、視線軸向細節 (→2C) |
| 2B | 側線頻率、內耳聽石、聲學阻抗、濁水衰減 | 視覺系統、覓食決策 |
| 2C | 眼睛解剖、視線觸發、攻擊角度、假餌水層操作 | 聲學、護巢行為 |
| 3A | Mid-Strolling、Follower Rejection、Alert Reset | 策略配方、地球化學 |
| 3B | 南部高溫爛底、北部翻水期、管理池、颱風前後四大極端情境戰術 | 機制理論重寫 |
| 4A | 築巢底質、孵化、Eh/Fe/H₂S、水位水溫擾動 | 競爭物種、護巢防禦細節 (→4B) |
| 4B | K 值、競爭物種、護巢防禦性攻擊 | 地球化學細節 |

Global: 0 series strictly excludes all fish behavior/physiology. Volumes 1–3 strictly exclude spawning/nest-guarding (4A/4B only).

## Global Output Rules (All Volumes)

Every research report must contain:
1. **Metadata block** — Volume_ID, Upstream_Required, Core_Parameters, Key_Mechanisms (actual values, not placeholders)
2. **Inherited_Baseline** — upstream values cited as `B0-XX` (from 0D) or `V{卷號}-NN`
3. **Findings** — uniquely numbered `V{卷號}-NN` (main) or `VSUP-{字母}NN` (SUP); bracket-only format like `[0A-01]` is non-compliant
4. **Carry_Forward_To_{下游卷}** — downstream parameters with source finding IDs
5. **Open_Assumptions** — high-uncertainty parameters, conservative values, verification directions

Prohibited in all volumes: vague descriptors (高/低/強/弱/顯著/明顯). All key parameters require numeric values or justified estimation ranges. Unit rules: temperature °C, DO mg/L, Eh mV, visibility cm, time hr/day — never mix specific heat with volumetric heat capacity.

## Three Climate Zones

Zone-B was added in v2 (2026-05). All quantitative outputs must list all three zones separately — never merge A+B as "北部":

| Code | Region | Representative Station |
|------|--------|----------------------|
| Zone-A | 北部迎風面 (台北/基隆/宜蘭) | CWA 台北 |
| Zone-B | 北部背風面 (桃園/新竹/苗栗) | CWA 桃園 |
| Zone-C | 南部背風面 (高雄/台南/屏東) | CWA 高雄 |

## Key Reference IDs

| Format | Source |
|--------|--------|
| `B0-XX` | Baseline facts from 0D1 |
| `V{卷號}-NN` | Findings from corresponding main volume |
| `VSUP-{字母}NN` | Findings from SUP volumes |
| `CI-XX` | Correction instructions issued by SUP volumes to patch existing volumes |

Critical cross-volume anchors: `B0-21` (Zone-B 22°C onset 12–18 days early), `B0-22` (Zone-B Eh <0 mV first contact late May), `VSUP-B04` (Fe²⁺ safe distance 40 cm north), `VSUP-B06` (H₂S safe distance ≥86 cm south).

## Modifying Instructions or Adding Volumes

- **Adding research items**: first assess which existing volume it belongs to; only create a new sub-volume when the topic spans multiple volumes or would compress an existing one
- **Modifying scope**: update both the master version (`0`–`4`) and the corresponding split version (`*-instruction.md`) to stay in sync; never delete content from master versions, only append
- **Creating a new sub-volume**: naming rule is `{卷號}{字母}：{主題}-instruction.md`; also update README.md execution order, pipeline diagram, the volume scope table in `.github/copilot-instructions.md`, and the Volume Scope Boundaries + Pipeline Architecture sections in this `CLAUDE.md`

## Pending Zone-B Patches

Volumes still needing Zone-B patches: **1A, 2C, 3A, 4A, 4B**. When editing these, flag Zone-B corrections with `CI-XX` format and note which Findings are affected. See README.md for the authoritative per-volume patch status table.
