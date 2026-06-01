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

---

## 0D 卷完整稽核與後處理（2026-06-01）

**目標檔案**：`0D_基底資料矩陣與極端事件整合.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 B0-XX 數**：B0-01–19　**Carry_Forward 數**：B0-CF-01–12

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | Zone-A/B/C 三區分離未系統性貫穿 Q2/Q3；Verification Plan python 腳本；Open Questions 待決事項未解 | 送 Gemini 修正 prompt |
| Round 2 | ✅ Go | 三區分離明確寫入 Q1–Q3 各子節；Verification Plan 移除；Open Questions 全數決策 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 1 件 | Core_Parameters 極端事件時間常數（緩衝時間 hr、DO 崩潰時間 hr、Lag day）在 Q2/Q3 分析段落中存在，但未以 B0-XX 格式輸出 |
| P2 輸出區塊 | ⚠️ 2 件 | Carry_Forward 使用自定義 B0-CF-XX 編號但未引用來源 B0-XX；Waterbody_Model_Table 擴展為 8 行（Zone-A/B 分離，符合 CLAUDE.md 三區規定，非錯誤） |
| P3 引用鏈 | ⚠️ 2 件 | B0-01–15 來源格式為 `0A-XX`（無 V 前綴），與 Inherited_Baseline 的 `V0A-XX` 格式不一致；Carry_Forward 各項缺少「(d) 引用的 B0-XX 編號」 |
| P4 Scope | ✅ OK | 無越界（Carry_Forward 下游標記屬路由 metadata，非正文魚類行為分析） |
| P5 研究缺口 | ⚠️ 1 件 | 颱風暴雨後 DO 崩潰時間、物理/地球化學 Lag、冷氣團後水溫/Eh 回升 Lag 均缺 B0-XX 條目 |

**Phase 6 判定**：⚠️ Claude 結構重建（總分 14，結構分 100%，Q 覆蓋完整型）
所有極端事件時間常數已在 Q2/Q3 分析體中存在，問題純屬結構性——數值需從分析段落提取並格式化為 B0-XX 條目。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-0D-01 | 新增 B0-16 至 B0-19：從 Q2-2/Q2-4/Q3-4/Q3-2 分析段落提取極端事件時間常數，補入 Baseline_Facts；B0-XX 標頭條目數更新為 19 條 |
| FIX-0D-02 | Carry_Forward B0-CF-01 至 B0-CF-09 各項末尾補入 `[引用：B0-XX]`；新增第 5 小節（B0-CF-10 至 B0-CF-12）對應 B0-16/B0-17/B0-19 |
| FIX-0D-03 | B0-01 至 B0-15 來源格式統一：`0A-XX` → `V0A-XX`、`0B-XX` → `V0B-XX`、`0C-XX` → `V0C-XX`（共 15 處） |

### B0-CF 引用對照表（完整版）

| B0-CF 編號 | 對應 B0-XX | 說明 |
|-----------|-----------|------|
| B0-CF-01 | B0-01, B0-02 | 春季升溫南北時序差 |
| B0-CF-02 | B0-07 | 淺水底層溫度遲滯時間 |
| B0-CF-03 | B0-18（新增） | 水溫回升 Lag（三區分離） |
| B0-CF-04 | B0-06 | 暴雨濁度恢復物理時間常數 |
| B0-CF-05 | B0-14 | 深水水庫中層濁度帶深度 |
| B0-CF-06 | B0-11 | 管理池夜間溶氧崩潰時間 |
| B0-CF-07 | B0-10 | 南部底泥游離 H₂S 化學緊迫 |
| B0-CF-08 | B0-08, B0-15 | 南部春雨回淹釋磷與藍綠菌藻華 |
| B0-CF-09 | B0-12 | 水庫季節性翻轉時序南北差 |
| B0-CF-10 | B0-16（新增） | 颱風暴雨後溶氧崩潰時間 |
| B0-CF-11 | B0-17（新增） | 颱風暴雨後物理 Lag + 地球化學 Lag |
| B0-CF-12 | B0-19（新增） | 冷氣團翻水後缺氧水影響時間 |

### 不受影響的確認正確數值

- B0-06：北部酸性絮凝沉降放大 100 倍，暴雨後 1–2 天恢復；南部中性 5–8 天
- B0-07：Zone-B 底層熱慣性 18–24 hr；Zone-A 17–23 hr；Zone-C 6–12 hr
- B0-11：管理池夜間停機 3–4 hr DO 崩潰（北部 <1.5 mg/L，南部 <0.5 mg/L）
- B0-12：深水水庫翻轉臨界（ΔT ≥6–8°C，U ≥6.5–8.5 m/s，持續 36–48 hr，Ri<0.25）；北部 11月中–12月下旬，南部 1月中–2月下旬
- B0-08：南部回淹後 5–9 天 Eh 從 +420/+540 mV 暴跌至 -100/-220 mV
- V0B-11：南部管理池 H₂S 峰值 0.15–0.85 mg/L；北部 <0.02 mg/L
