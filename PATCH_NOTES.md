# Patch Notes — 跨文件合規修復

> v1 修復紀錄（0A–SUP-C、Zone-B 補丁、0C1/0D1/3B1 格式修正）已封存至 git history。
> 見 commit `0f4a843` 以前的版本。

---

<!-- 新的修復紀錄從此處開始 -->

---

## 0C 卷完整稽核與後處理（2026-05-29）

**目標檔案**：`0C_六大水體 seasonal 評估.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：V0C-01–14　**Carry_Forward 數**：CF0C-01–16（第二輪稽核後新增 CF0C-15/16）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | A2 翻轉觸發條件、異重流深度、C2 藍綠菌藻華三項結構性缺口 | 送 Gemini 修正 prompt |
| Round 2 | ✅ Go | 三項缺口全數補入 Section 4/5/6 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 10 件 | Waterbody-1 Eh 矛盾、B3 TN/導電度缺失、A2 非夏季溫躍層缺失等 |
| P2 輸出區塊 | ⚠️ 4 件 | Inherited_Baseline 空白、Metadata 未填、Open_Assumptions/Unresolved 結構缺失 |
| P3 引用鏈 | ⚠️ 2 件 | Section 1 數值無 V0A/V0B 碼；Carry_Forward 未回溯 0A/0B 原始碼 |
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ⚠️ 3 件 | TN、導電度、非夏季溫躍層 → 送 Q-SUP 補充 |

**Phase 6 第一輪判定**：⚠️ Claude 結構重建（總分 18，結構分 75%）

補充 Q-SUP 後第二輪稽核：P5 缺口全數關閉，最終判定 ⚠️ 局部補充（11 分，全部 Claude 項目）→ **進入最終後處理**。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-0C-01 | Inherited_Baseline 從空佔位建立為完整 15 條 V0A/V0B 引用列表 |
| FIX-0C-02 | Metadata Core_Parameters / Key_Mechanisms 填入實際研究數值區間 |
| FIX-0C-03 | Open_Assumptions_0C 從 2 條無結構 → 5 條含 (a)(b)(c) |
| FIX-0C-04 | Unresolved_Dependencies 從 1 條無結構 → 3 條含下游影響與資料來源 |
| FIX-0C-05 | Waterbody-1 Eh 矛盾修正：正文改為「夏季底層局部 -50 to 0 mV」，表格夏季 Eh 欄同步更新並補 Fe²⁺ 季節性釋放說明 |
| FIX-0C-08 | Waterbody-6 水質：補入有機物含量閾值 >3.5–5.5%（乾重）為 H₂S 觸發有機碳門檻 |
| FIX-0C-09 | Waterbody-4/6 溫度：補入冬季冷氣團表水降溫速率 1.0–1.9°C/day（V0A-08）；修正 Waterbody-6 冬季表格「降幅大」→量化數值 |
| FIX-0C-10 | Waterbody-4 溫度：補入夏季表底溫差 3.5–5.5°C |
| FIX-0C-11 | Waterbody-6 溫度：補入停機後溫度分層恢復時間 1.5–2.5 hr |
| FIX-0C-12 | Waterbody-4 水質：補入夜間 DO 最低值時刻 04:00–05:30 |
| FIX-0C-13 | 移除三處模糊描述：「充足的亞鐵沉澱庫」「高度藻華風險」「強烈的內部營養鹽負載」→ 各替換為量化數值與 V-code |
| FIX-0C-14 | Section 1 Zone-A/B/C 描述補入 V0A/V0B 引用碼（V0A-02/03/04/09/10、V0B-01/02/12） |
| FIX-0C-新-01 | V0C-13 標題澄清（「南部野生埤塘」→「南部 Zone-C 限定 TN + 三區 EC」）；CF0C-13 標題同步修正 |
| FIX-0C-新-02 | V0C-13 信心等級「高」→「TN 估算—中（文獻外推）；EC 量測—高」 |

### 不受影響的確認正確數值

- Stokes 三 pH 情境：pH 4.5→145.8 cm/hr；pH 5.5→9.11 cm/hr；pH 7.0→1.458 cm/hr
- 深水水庫翻轉臨界：ΔT ≥ 6.0–8.0°C、U ≥ 6.5–8.5 m/s、t ≥ 36–48 hr（Ri < 0.25）
- 北部水庫翻轉：11月中–12月下；南部水庫：1月中–2月下
- 異重流：底部 >25 m（SS 5,000–15,000 mg/L）；中層 8.5–18.2 m（SS ~1,000 mg/L）
- 南部管理池夏季 H₂S：0.15–0.85 mg/L（停機 3–4 hr，Eh -150 to -250 mV）
- 南部春末藻華：野生埤塘 10–15 cm（15–25 天）；水庫庫灣 30–50 cm（10–18 天）
- 南部野生埤塘春雨回淹釋磷：25–45 μg/L（5–9 天）
- 南部水庫颱風後 TP：+15–35 μg/L（7–14 天）

### 第二輪稽核補丁（2026-05-29，twbass-audit 重審）

Phase 6 判定：✅ 不需重跑（1 分）。以下 6 條由 Claude 直接修補。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-0C-R2-01 | Metadata、§三-2、V0C-02、W1 溫度描述、Table W1 冬季欄、CF0C-03 | Zone-A/B 熱阻阻尼值拆分：CF0C-03 拆為 CF0C-03a（Zone-A 17–23 hr，C_v=3.215）與 CF0C-03b（Zone-B 18–24 hr，C_v=3.411）；Table W1 冬季欄補入 V0A-08 Zone-A/B 降溫幅度 |
| FIX-0C-R2-02 | Waterbody-1 溫度動態第一句 | 刪除「熱慣性適中」模糊描述，替換為 Zone-A/B C_v 量化值與 hr 範圍 |
| FIX-0C-R2-03 | §六/七 章節標題 | 補充研究章節由「七」更正為「六」；參考文獻由「六」更正為「七」 |
| FIX-0C-R2-04 | Carry_Forward_To_0D 末端 | 新增 CF0C-15（北部管理池停機透明度窗口 50–80 cm，引 V0C-11）與 CF0C-16（南部管理池夏季水溫峰值 34–35°C，表底差 4–5°C，引 V0C-12） |
| FIX-0C-R2-05 | Waterbody-2 水文段 | 北部水庫回淹 TP <3 μg/L 補標「理論估算：V0B-02 Q_max = 780–1,250 mg/kg」 |
| FIX-0C-R2-06 | Waterbody-1 溶氧與水質段 | 夏季 DO 光合 0.4–0.8 mg/L/hr、呼吸 0.2–0.5 mg/L/hr 補標「文獻估算：亞熱帶淺水湖沼學外推」 |

**git commit**：`e11c9f1`（fix(0C): 套用六條 FIX 稽核修正）
