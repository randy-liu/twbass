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

---

## 1A 卷完整稽核與後處理（2026-06-01）

**目標檔案**：`1A_短時間環境觸發與生理限制.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：V1A-01–12　**Carry_Forward 數**：Carry_Forward_To_3A（3 條）/ Carry_Forward_To_3B（3 條）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要修正 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | 側線未明確排除（→2B）；Zone-B 三區分離缺失；魚鰾雙體型計算；Snell 窗雙標準 | 送 Gemini 修正 prompt |
| Round 2 | ✅ Go | 四項缺口全數補入；側線限縮語明確；Zone-A/B/C 三區分離寫入 Q3-2 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 3 件 | Zone-A SD 跨章節不一致（35 cm vs 30 cm）；Zone-B κ 採水車開啟 SD=65 cm 但標注為季均 45 cm；Snell 表 Zone-B SD 與 Q3-2 不一致 |
| P2 輸出區塊 | ✅ OK | V1A-01–12 共 12 條；Carry_Forward 兩份；Unresolved_Dependencies 2 條；格式正確 |
| P3 引用鏈 | ⚠️ 4 件 | B0-109 幻覺引用；B0-CF-07 幻覺引用；B0-04/B0-09 缺失於 Inherited_Baseline |
| P4 Scope | ⚠️ 1 件 | Carry_Forward_To_3B item 3 含具體假餌型號（應移交 卷 3B） |
| P5 研究缺口 | ✅ OK | 2 條已在 Unresolved_Dependencies 標注（H₂S/CH₄ 聯合毒性 LC₅₀；Mesopic 期視覺追蹤 Hz 門檻） |

**Phase 6 判定**：⚠️ 局部補充（9 分），全部為計算標注矛盾與幻覺引用，Claude 人工修補即可。推薦工具：Claude。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-1A-01 | Zone-A SD 統一為 35 cm（κ=4.86 m⁻¹）：Snell 表 Zone-A 行視距更新（強光高/低對比：0.28/0.77 m；漫射高/低對比：0.39/1.05 m）；Q4-1 Zone-A 月光重算（0.5m：0.018 lux；1.0m：0.0015 lux；2.0m：0.000012 lux）；Melatonin 抑制率更新（67.0% / 9.3% / <0.1%）；V1A-06 高解析視距 24 cm → 28 cm；V1A-12 Zone-A 對比值同步更新 |
| FIX-1A-02 | Zone-B Q3-2 標頭明確標注「晴天日間水車開啟情境，SD=65 cm」，計算值（κ=2.62 m⁻¹）不動 |
| FIX-1A-03 | Snell 表 Zone-A 行標注從 30 cm 改為 35 cm（FIX-1A-01 聯動） |
| FIX-1A-04 | B0-109 幻覺引用 → 改為 B0-11（管理池有機負荷/水車行為） |
| FIX-1A-05 | B0-CF-07 幻覺引用 → 移除；H₂S 峰值引用已由 B0-10 涵蓋 |
| FIX-1A-06 | Inherited_Baseline 新增 B0-04（南部水溫 28–32°C）與 B0-09（Q₁₀=2.4 溫度係數） |
| FIX-1A-07 | Carry_Forward_To_3B item 3 移除具體假餌型號（側線主導期假餌策略屬 卷 3B 任務），改為感官切換閾值說明並移交 卷 2B/3B |
| FIX-1A-附 | Snell 表 Zone-A 行描述移除「桃園」：桃園屬 Zone-B 北部背風面，混入 Zone-A（迎風面 台北/基隆/宜蘭）行為地理分區錯誤；改為「北部迎風面高壓池」 |

### V1A-12 結論修正說明

Zone-A 採 SD=35 cm（κ=4.86）後，水下 0.5m 月光提升至 0.018 lux，Melatonin 抑制率由 54.86% 升至 67.0%。原結論「完全免疫」過於絕對，修正為「底棲個體（>1.0m）免疫月相干擾；0.5m 表層帶存在部分節律偏移，行為學顯著性待進一步實驗驗證」。結論方向不變，精度提升。

### 不受影響的確認正確數值

- 颱風降壓 53 hPa 等效水深 54.1 cm；一般降壓 13 hPa 等效 13.3 cm
- 35 cm/1 kg 魚鰾膨脹（-53 hPa）：+3.59 cm³（+4.79%）
- 50 cm/2.5 kg 魚鰾膨脹（-53 hPa）：+8.98 cm³（+4.79%，絕對體積 2.5 倍尺度效應）
- Zone-B（水車開啟 SD=65 cm）Lockjaw 觸發：08:30–09:00，持續 3.5–4.5 hr
- Zone-C（SD=150 cm）Lockjaw 觸發：07:00–07:30，持續 7.0–8.0 hr
- Zone-A（SD=35 cm）無 Lockjaw（1.0m 最高 507 lux，遠低於致盲閾值 20000 lux）
- 滿月 Zone-C 水下 1.0m Melatonin 抑制 90.33%
- MOx 耗氧速率 0.19–0.53 mg O₂/L/hr（30°C，Q₁₀=2.4）
- H₂S 黑鱸急性毒性閾值 0.05 mg/L（直接實驗證據）
- 微型躍溫層密度差（32°C vs 25°C）= 2.018 kg/m³，N = 0.1150 rad/s
- 低壓咬況機制：光學漫射貢獻 65%，魚鰾微脹貢獻 35%
- Snell 窗全錐角 97.22°；半徑 = 1.134 × 水深（m）

---

## 1B 卷完整稽核與後處理（2026-06-01）

**目標檔案**：`1B_六大水域棲位模型與風生流.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：V1B-01–13　**Carry_Forward 數**：Carry_Forward_To_3B（7 條 V1B-CF-01–07）/ Carry_Forward_To_4B（3 條 V1B-CF-08–10）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | 南部深水水庫旱季消落帶缺失；北部水車 vs 南部曝氣機停機效應未拆分；Zone-A/B/C 三區折疊為「北部/南部」；Fe²⁺ 底層濃度未計畫 | 送 Gemini 修正 prompt |
| Round 2 | ✅ Go | 四項缺口全數補入（[IMPORTANT] 1–4）；Zone-B 22°C 提前 12–18 天與 Eh 觸發時間窗差異明確；Zone-B 缺值插值規則明確（×0.85 係數）；OFT 限縮語補入 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 6 件 | B0-108/109 打字錯誤；B0-270/354 幻覺碼；V1B-03 信心等級矛盾；B0-08 語義不符（引用鐵還原速率） |
| P2 輸出區塊 | ✅ OK | V1B-01–13 共 13 條；兩份 Carry_Forward；Unresolved_Dependencies 3 條；格式正確 |
| P3 引用鏈 | ⚠️ 7 件 | B0-CF-05/CF-07 循環引用；B0-09 缺 Inherited_Baseline；B0-17 時序不符（深水庫 vs. 淺水） |
| P4 Scope | ⚠️ 2 件 | V1B-07「作釣窗口」；V1B-09「慢速微精細作釣」侵入 3A/3B 語言 |
| P5 研究缺口 | ⚠️ 2 件 | V1B-11 Fe²⁺ 閾值信心等級 finding 中標「中」但 Unresolved 標「低」（不一致，且涉及 CF-04/10）；Zone-B 插值不確定性未系統標注 |

**Phase 6 判定**：⚠️ Claude 結構重建（總分 15，結構分 100%，Q 覆蓋完整型）
所有 Q1–Q5 研究方向完整覆蓋，問題純屬引用格式、幻覺碼移除與信心等級修正，無需新 Gemini session。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-1B-01 | `B0-108` → `B0-08`（V1B-02 南部水庫缺氧引用打字錯誤） |
| FIX-1B-02 | `B0-109` → `B0-10`（V1B-04b 南部曝氣機停機 Eh 動態打字錯誤） |
| FIX-1B-03 | B0-270 移除 → 改標「基於 Richardson 數穩定性準則估算，理論估算」（V1B-08 混合深度） |
| FIX-1B-04 | B0-354 移除 → 展開風應力公式 $\tau_w = \rho_a C_D U^2$ 明確計算（V1B-12） |
| FIX-1B-05 | `B0-CF-05` 移除 → 改為「引用自 V1B-06 所述之中層高濁度條件」（V1B-07 循環引用） |
| FIX-1B-06 | `B0-CF-07` 移除 → 改為「本卷 V1B-10 擴散模型計算值」（V1B-10 循環自引） |
| FIX-1B-07 | `B0-09` 引用移除 → 改標「溫度效應 Q₁₀ 外推，廣泛外推」（V1B-10 H₂S 加速動力學） |
| FIX-1B-08 | V1B-11 鐵還原速率 `B0-08` → 改引文獻黃富盟、張祖亮（2008）並標注「類比推估」 |
| FIX-1B-09 + 11 | V1B-07 末句合併修正：B0-17 補全庫 3.0–5.0 天 vs. 表層 1.0–2.0 天（淺水代理）差異；移除「作釣窗口」語言，改為「對應 3B 極端情境推演，詳見下游卷」 |
| FIX-1B-10 | V1B-03 信心等級：`高` → `中`（理論估算外推不符高信心；Unresolved 1 同步確認） |
| FIX-1B-12 | V1B-09 末句移除「慢速微精細作釣」3B 語言，改為「對應極端情境推演詳見卷 3B」 |
| FIX-1B-13 | V1B-11 信心等級：`中` → `低`（Fe²⁺ 閾值廣泛外推，缺 *M. salmoides* 直接數據）；V1B-CF-04 與 V1B-CF-10 加 ⚠️ 降權警示 |

### 不受影響的確認正確數值

- V1B-01 三區淺水四季偏好水深（Zone-A/B 春/夏/秋/冬、Zone-C 各季含極端壓縮 60–80 cm）
- V1B-02 深水水庫溫躍層棲位（Zone-B 夏季 2.5–5.0 m、Zone-C 夏季 3.0–6.0 m；躍層以下 DO <0.5 mg/L 絕對迴避帶）
- V1B-03 曾文水庫乾季消落帶：水位下降 15–30 m、殘餘棲位 2.0–5.0 m（信心修正為中）
- V1B-04a 北部水車停機：DO 衰減 1.2–1.5 mg/L/hr，3.0–4.0 hr 達窒息臨界；黑鱸上移至表層 0–30 cm
- V1B-04b 南部曝氣機停機：H₂S 上升 0.01–0.03 mg/L/hr，4.0–8.0 hr 達 0.05–0.20 mg/L；黑鱸上移 60–100 cm 至表層 0–20 cm
- V1B-06 異重流 Δρ ≈ 1.02 kg/m³；入侵深度 8.5–18.2 m（承接 B0-14）
- V1B-08 翻水觸發 ΔT ≥ 3.0–4.0°C、北風 ≥ 6.5–8.5 m/s
- V1B-09 全池混合 2.0–6.0 hr；DO 衰減 0.5–1.2 mg/L/hr；黑鱸集中表層 0–50 cm
- V1B-10 H₂S LC50 0.02–0.04 mg/L；亞致死 0.01 mg/L；Zone-C 安全距離 60–100 cm
- V1B-11 Fe²⁺ 急性閾值 1.2–2.0 mg/L（類比推估）；亞致死 0.5 mg/L（廣泛外推，低信心）；Zone-C 安全距離 30–50 cm
- V1B-12 6 m/s 風速下表層流 9.0–18.0 cm/s；OFT 切換閾值 20 cm/s
- V1B-13 迎風岸富集範圍 3.0–15.0 m；最佳伏擊水深 0.5–1.0 m；仰角 15°–30°

---

## 2A 卷完整研究與後處理（2026-06-01）

**目標檔案**：`2A_覓食偏好、印記與反射咬餌.md`
**執行流程**：gemini-plan-review（2 輪修正計畫）→ Antigravity 一手完整解算高精度正體中文報告
**最終 Findings 數**：V2A-01–12　**Carry_Forward 數**：Carry_Forward_To_2C（2 大項/視覺距離與速度矩陣）/ Carry_Forward_To_3A_3B（3 大項/印記喚醒、皮質醇避忌、感官切換）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要修正 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | 新增了預計變動及驗證合規的腳本流程；Q4 的波長衰減未區分北部迎風與背風兩區。 | 送 Gemini 修正計畫 |
| Round 2 | ✅ Go | 移除後處理與合規非研究章節；落實 Zone-A、Zone-B、Zone-C 的三區獨立計算，特別是波長衰減、視覺識別距離與反射咬餌速度矩陣。 | 進入執行並高標準產出 |

### 確認之高嚴謹度量化數值與公式
*   **OFT 覓食效益 ($E/T$)**：
    *   式：$E/T = (M \cdot D_e) / (T_s + T_p + T_h)$
    *   1. 吳郭魚幼魚 (3-5 cm)：**0.272 kcal/s**（最佳能量報酬；大於 8 cm 時因 $T_h$ 呈指數增長，能效驟降至 <0.07 kcal/s）
    *   2. 大肚魚 (3.0 cm)：**0.148 kcal/s**（單隻熱量極低，需極高密度支持）
    *   3. 澤蛙蝌蚪 (3.0 cm)：**0.100 kcal/s**（90.2% 高水分稀釋能量）
    *   4. 鰕虎魚 (4.5 cm)：**0.043 kcal/s**（底棲保護色與吸盤高搜索/追擊成本）
    *   5. 日本沼蝦 (4.5 cm)：**0.034 kcal/s**（甲殼棘額角高處理時間，且底棲搜索高）
*   **尺寸篩選神經解碼**：黑鱸視覺尺寸篩選神經元最小攻擊視角閾值約 **1.5°**。10 cm 假餌預期能效 **2.06 kcal/s**，為大肚魚之 13.9 倍，中樞神經優先響應。
*   **養殖條件反射衰減**：人工顆粒飼料操作制約半衰期為 **50 天**，放流 **3–6 個月** 後完全消退；落水聲古典制約記憶殘留可達 **12 個月以上**。
*   **落水聲喚醒特徵**：假餌落水激發 **300–1500 Hz** 瞬態聲，與飼料落水聲（**200–1200 Hz**，**112–118 dB**）高度匹配，激活聽神經 $\rightarrow$ 延腦 Torus $\rightarrow$ 杏仁核 $\rightarrow$ 外側下視丘定向暴衝通路。
*   **皮質醇與 Lure-shyness**：被釣獲應激使血漿皮質醇暴增至 **80–180 ng/mL**，結合端腦內側蒼白球 GR 受體，極大強化突觸 LTP 記憶，造成假餌避忌與下潛，需 **48–96 hr** 方可消退。
*   **Reaction Strike 雙通路與臨界速度**：
    *   快速視覺通路（網膜 $\rightarrow$ 視頂蓋 $\rightarrow$ 網狀脊髓巨大神經元 $\rightarrow$ 吞噬運動）：潛伏期僅 **12–25 ms**。
    *   慢速分析通路（端腦認知整合）：潛伏期 **150–350 ms**。
    *   反射咬餌臨界速度：**$V_{crit} \ge 1.2\text{ m/s}$**。大於此速度，視野滯留時間小於 150 ms，大腦被迫以快速視覺反射發動咬餌；低於 0.5 m/s 則 100% 進入慢速認知，極易被識破拒咬。
*   **三區分離水色視覺衰減與 $V_{strike}$**：
    *   **Zone-A (北部迎風面褐色水，SD 35 cm)**：消光 $\kappa = 4.86\text{ m}^{-1}$。藍光（450 nm）在 **22 cm** 處衰減 90%，紅光（650 nm）在 **68 cm** 處衰減 90%。冷色對比衰減 **$-0.18\text{ dB/cm}$**、暖色 **$-0.05\text{ dB/cm}$**。Reaction Strike 需 **$V_{strike} \ge 1.5\text{ m/s}$** 的突發性閃現。
    *   **Zone-B (北部背風面中度濁水，SD 45 cm)**：消光 $\kappa = 3.78\text{ m}^{-1}$。藍光有效深度 **35 cm**，紅光 **92 cm**。冷色衰減 **$-0.12\text{ dB/cm}$**、暖色 **$-0.04\text{ dB/cm}$**。臨界速度 **$V_{strike} \ge 1.2\text{ m/s}$**。
    *   **Zone-C (南部背風面綠色水，SD 50 cm)**：消光 $\kappa = 3.40\text{ m}^{-1}$。藍光與紅光分別在 **28 cm** 與 **38 cm** 處極速衰減 90%（紅色呈死灰）；黃綠光（540 nm）有效穿投深達 **112 cm**，衰減僅 **$-0.03\text{ dB/cm}$**。臨界速度 **$V_{strike} \ge 1.1\text{ m/s}$**。
*   **感官切換臨界點**：Secchi 能見度 **$SD \le 15\text{ cm}$** 時，視覺輪廓距離縮減至 **< 5 cm**，視覺搜尋 100% 失效。Reaction Strike 啟動完全切換為由側線（10-100 Hz 低頻流體脈衝）主導。

### 5-Phase 稽核結果（2026-06-01）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 1 件 | Δspectral ≥ 0.05 缺來源引用與信心等級（Carry_Forward_To_2C） |
| P2 輸出區塊 | ✅ OK | V2A-01–12 格式正確；5 大輸出區塊完整 |
| P3 引用鏈 | ⚠️ 3 件 | V2A-05 誤植於 CF_2C 表頭；CF_3A_3B 各條缺 V2A 引用；感官切換條目缺 B0-CF-02 |
| P4 Scope | ⚠️ 2 件 | CF_3A_3B 第 3 條含具體假餌型號（3B 戰術配方越界）；側線頻率細節輕微 2B 邊界 |
| P5 研究缺口 | ⚠️ 2 件 | Δspectral 無文獻；V2A-03「直接實驗證據」層級存疑 |

**Phase 6 判定**：✅ 不需重跑（得分 2）。Q 覆蓋完整型，所有缺口為引用錯誤、格式與輕微 Scope，Claude 後處理即可。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-2A-01 | CF_2C 視距矩陣表頭引用 V2A-05 → V1A-06（V2A-05 為皮質醇 Finding，與視覺距離無關） |
| FIX-2A-02 | CF_3A_3B 各條補入明確 V2A 引用：第 1 條加 `[引用：V2A-03, V2A-04]`；第 2 條加 `[引用：V2A-05]`；第 3 條加 `[引用：V2A-12, B0-CF-02]` |
| FIX-2A-03 | CF_3A_3B 第 3 條移除具體假餌型號（Spinnerbait、Rattle、Cranks）；「戰術切換門檻」改標「感官切換觸發條件」；補入「具體假餌選型詳見卷 3B」說明 |
| FIX-2A-04 | Δspectral ≥ 0.05 補入 `[信心等級：中。廣泛外推：基於 Centrarchidae 光學分辨閾值文獻推估；缺乏 *M. salmoides* ERG 直接量測數據，待 SUP-A 補充確認]` |
| FIX-2A-06 | V2A-03 信心等級：`高。類比推估與直接實驗證據` → `中-高。類比推估為主：基於 Centrarchidae 操作制約消退研究；*M. salmoides* 直接放流追蹤數據稀少，t₁/2 ≈ 50 天為估算區間中值` |

### 不受影響的確認正確數值

- Zone-A V_strike ≥ 1.5 m/s；Zone-B ≥ 1.2 m/s；Zone-C ≥ 1.1 m/s；深水清澈 ≥ 1.0 m/s
- 快速視覺通路 12–25 ms；慢速分析通路 150–350 ms；V_crit ≥ 1.2 m/s
- 皮質醇基線 <5 ng/mL；釣獲應激峰值 80–180 ng/mL；消退 48–96 hr
- 飼料印記消退半衰期 t₁/2 ≈ 50 天（中-高信心），完全消退 3–6 個月；聽覺殘留 >12 個月
- 感官切換臨界 SD ≤ 15 cm（視覺 100% 失效）
- Zone-A：藍光 22 cm、紅光 68 cm（90% 衰減）；冷色 −0.18 dB/cm；暖色 −0.05 dB/cm
- Zone-B：藍光 35 cm、紅光 92 cm；冷色 −0.12 dB/cm；暖色 −0.04 dB/cm
- Zone-C：藍光 28 cm、紅光 38 cm、黃綠光 112 cm；黃綠 −0.03 dB/cm

---

## 2A 卷第二輪稽核與後處理（2026-06-01）

**目標檔案**：`2A_覓食偏好、印記與反射咬餌.md`（第一輪 FIX-2A-01–06 已套用後的版本）
**執行流程**：twbass-audit 完整 5-Phase → Claude 後處理

### 5-Phase 稽核結果（第二輪）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 2 件 | a(λ) 標籤為純吸收係數但穿透深度計算使用有效消光係數 c(λ)，兩者不一致；CF-3A_3B 第 3 條 Zone-A/B 合併 |
| P2 輸出區塊 | ⚠️ 3 件 | CF-3A_3B 缺 OFT 效益矩陣（V2A-01/02）；缺 V_strike 分級（V2A-07/11）；CF-2C V_strike 矩陣缺 <30 cm 能見度分級 |
| P3 引用鏈 | ⚠️ 3 件 | CF-2C Δa = 2.5 m/s² 無 V2A 來源碼；V2A-01/02 未出現在任何 Carry_Forward；B0-CF-02 格式待確認 |
| P4 Scope | ✅ OK | 側線/聲學內容均由 instruction Q2-2/Q4-2 明確要求，無自主越界 |
| P5 研究缺口 | ✅ OK | 原有 3 條 Unresolved 完整合理 |

**Phase 6 判定**：⚠️ 局部補充（9 分）。Q 全覆蓋型，所有缺口為結構性（資料已在 Findings 中，需補入正確 CF 區塊）或標籤修正，推薦 Claude 直接後處理。

### Claude 後處理修改清單（第二輪）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-2A-R2-01 | §四 Zone-A/B/C 光學截面、V2A-08/09/10 | a(λ) 標籤改為「純吸收估算 a(λ)」並補入有效消光係數 c(λ) 對應值；Zone-A: c(450nm)≈10.47 / c(650nm)≈3.39；Zone-B: c(450nm)≈6.58 / c(650nm)≈2.50；Zone-C: c(435nm)≈8.23 / c(670nm)≈6.06 / c(540nm)≈2.06（均 m⁻¹）|
| FIX-2A-R2-02 | `Carry_Forward_To_3A_3B` 新增第 4 條 | 補入 OFT 效益矩陣（六獵物 0.034–0.272 kcal/s）與最小攻擊視角閾值 1.5°；預期 E/T 倍數 13.9×；引用 V2A-01, V2A-02 |
| FIX-2A-R2-03 | `Carry_Forward_To_3A_3B` 新增第 5 條 | 補入各區 V_strike 分級（Zone-A ≥1.5、Zone-B ≥1.2、Zone-C ≥1.1、清澈水庫 ≥1.0 m/s + Δa ≥2.5 m/s²）；切換門檻 V≤0.5 m/s；引用 V2A-07, V2A-11 |
| FIX-2A-R2-04 | `Carry_Forward_To_2C` V_strike 矩陣 | 在現有 Zone 分級前新增「能見度 <30 cm 極端濁度」分級條目：視覺 V_strike 無效，改依側線 10–100 Hz Kármán 渦街觸發；引用 V2A-12；各 Zone 行補入能見度分級歸屬標注 |
| FIX-2A-R2-05 | V2A-11 Finding | 補入 Δa = 2.5 m/s² 的推算依據（0.5→1.0 m/s 在 200 ms 截斷窗口內 = 2.5 m/s²，理論估算）；CF-2C 對應行補注引用 V2A-11 |
| FIX-2A-R2-06 | `Carry_Forward_To_3A_3B` 第 3 條 | Zone-A/B：17–24 hr → Zone-A：17–23 hr；Zone-B：18–24 hr；Zone-C：6–12 hr |
| FIX-2A-R2-07 | `Inherited_Baseline` B0-CF-02（待驗） | 待下次開啟 0D1 報告時確認「底泥熱慣性滯後」的實際 Finding ID（B0-07 已確認為 0D1 的正式 ID；B0-CF-02 為 Carry_Forward 路由碼，格式本身合規）；全文共 3 處引用（Inherited_Baseline/CF-3A_3B 第 3 條/§五 第 5 節末），如 ID 異動請同步更新 |

### 不受影響的確認正確數值（第二輪驗證後）

- OFT 六獵物效益比計算過程驗證正確（E/T = M×De / T_total）
- V_strike 各區數值（Zone-A ≥1.5 / Zone-B ≥1.2 / Zone-C ≥1.1 / 清澈 ≥1.0 m/s）
- 光學穿透深度數值正確（使用 c(λ) 計算；a(λ) 為純吸收分量，標籤已修正）
- 皮質醇 80–180 ng/mL；避餌期 48–96 hr；印記半衰期 t₁/2 ≈ 50 天
- 快速通路 12–25 ms；慢速通路 150–350 ms；V_crit ≥ 1.2 m/s

---

## 2B 卷 Q-SUP 補充研究整合與後處理（2026-06-02）

**目標檔案**：`2B_側線、內耳與水下聲學傳遞.md`
**執行流程**：gemini-plan-review（2 輪）→ Gemini Q-SUP-01/02 補充執行 → twbass-audit 5-Phase → Claude 後處理
**補充研究任務**：Q-SUP-01（EPS 聲學衰減三成分分解）+ Q-SUP-02（低頻振盪體近場水動力場修正）
**最終 Findings 數**：V2B-01–12（未增加條數；V2B-09 / V2B-12 量化升版）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | Q-SUP-02 軟蟲振幅 30–45% 衰減的彈性建模來源未指定（Gemini 幻覺風險高）；tan δ_bottom 30–50% 增幅無來源 | 送 Gemini 修正 prompt：補入雙軌路徑（文獻 + Cantilever Beam 理論推導）與信心等級標注要求 |
| Round 2 | ✅ Go | Q-SUP-02 item 3 已補入雙軌路徑、Damping ratio 推導路徑、PVC 材料不確定性分析；無結構性缺口 | 進入執行 |

### 5-Phase 稽核結果（Q-SUP 整合後）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 2 件 | A ∝ 1/c 模型僅支撐 9.1% 衰減，30–45% 結論需指數行波補充推導；tan δ_bottom = 0.15 基線無引用 |
| P2 輸出區塊 | ⚠️ 2 件 | V2B-09 更新後原有「16 倍（2000 Hz vs 500 Hz）」關係遺失；Section 十三標題語法錯誤 `十三("` |
| P3 引用鏈 | ⚠️ 1 件 | Carry_Forward Section 2 引用 V2B-09「16 倍」主張但該主張已從 V2B-09 被刪除 |
| P4 Scope | ✅ OK | 無越界；PVC 材料特性為 FSI 物理計算所需，非假餌操作策略 |
| P5 研究缺口 | ⚠️ 2 件 | tan δ_bottom 增幅（30–50%）缺台灣在地底泥量測驗證；V2B-10 傳播免疫語義與 V2B-12 FSI 效應潛在歧義 |

**Phase 6 判定**：⚠️ Claude 結構重建（總分 12，結構分 83%，Q 覆蓋完整型）
所有 Q 研究方向完整覆蓋；問題純屬推導說明補充、遺失內容恢復與語義澄清，無需新 Gemini session。

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-2B-01 | V2B-09 | 補回「16 倍（2000 Hz vs 500 Hz）」雙重衰竭機制說明（Δα 2.11×10⁻⁷ dB/m vs 1.32×10⁻⁸ dB/m），修復 Carry_Forward Section 2 引用鏈 |
| FIX-2B-02 | Section 七.2 item (3) | A ∝ 1/c 段落後插入推導補注：指數行波衰減 $A_{tip} = A_{root} \times e^{-\text{Im}(k_b) L}$ 橋接 9.1% → 30–45% 邏輯，Im(k_b) ∝ η^{1/2} |
| FIX-2B-03 | Section 十三標題 | `十三("Unresolved_Dependencies"` → `十三、Unresolved_Dependencies` |
| FIX-2B-04a | Section 六.2 item (4) | `tan δ_bottom ≈ 0.15` 補注「Biot 多孔介質理論估算值，[理論估算]」 |
| FIX-2B-04b | Open_Assumptions item 3 | 新增補注：tan δ 基線與 EPS 增幅為理論推算，建議後續底泥聲學實測校正 |
| FIX-2B-05 | V2B-10 | 補充「免疫」語義澄清：傳播路徑幅值變動 < 0.2%（Q-SUP-02）≠ 源端 FSI 振幅衰減，兩者獨立，詳見 V2B-12 |
| FIX-2B-06 | Section 八.4 表格前 | 新增 Zone-A/B 合併說明 blockquote；標注 Zone-B 分離數值待 v2 re-run 補充 |

### Q-SUP 補充研究核心數值（稽核確認正確）

| 數值 | 驗證結果 |
|------|---------|
| Δα_SK (500 Hz) = 1.324×10⁻⁹ dB/m | f² 比例驗算 ✓ |
| Δα_relax (250 Hz) = 1.971×10⁻⁹ dB/m | Debye 弛豫公式驗算 ✓ |
| Δα_scat (500 Hz) = 1.447×10⁻²¹ dB/m | Rayleigh ka ≪ 1 論證 ✓ |
| δ_v (15 Hz, 30°C, 清水) = 0.1303 mm | ν₀/ω 公式驗算 ✓ |
| K(ma) 幅值變動（η+10%）< 0.2% | 大β近似驗算 ✓ |
| r_crit 游離側線 15 Hz EPS = 10.3 cm | 偶極子方程反推驗算 ✓ |
| r_crit 管道側線 30 Hz 清水 = 40.9 cm | ω×v 加速度反推驗算 ✓ |
| 8.5–12.3 m EPS 藻華埤塘有效距離定界 | TL = 10 log r + 1.0r 驗算 ✓（前提：tan δ_bottom 估算成立） |
| 30–45% 軟蟲振幅衰減 | 指數行波模型理論估算，材料剛度 ±20% 不確定性已記錄 |

---

## 2C 卷 Q-SUP 補充研究整合與後處理（2026-06-02）

**目標檔案**：`2C_視線軸向、攻擊角度與假餌操作.md`
**執行流程**：gemini-plan-review（1 輪）→ Gemini 主卷執行 → twbass-audit R1（5-Phase）→ Gemini Q-SUP-01/02 補充執行 → twbass-audit R2（5-Phase）→ Claude 後處理
**補充研究任務**：Q-SUP-01（Up-Strike 水溫/DO/深度三區分列門檻）+ Q-SUP-02（全視野與雙眼區空間視敏度 CPD）
**最終 Findings 數**：V2C-01–12；Carry_Forward_To_3A_3B（5 條）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ✅ Go | 無結構性缺口；獵物相對水層位置（探討 2 第 3 項）屬「可浮現缺口」，研究過程自然命中 | 直接執行 |

### 5-Phase 稽核結果（R1，主卷執行後）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 3 件 | V2C-12「Caucasian」幻覺殘碼；Down-Strike 速度缺 m/s 換算；V1A-10 適應時間 30–45 min 待核對（V1A-04 熱點值 45–60 min） |
| P2 輸出區塊 | ⚠️ 2 件 | Zone-B 視距未列 Inherited_Baseline item 4；Carry_Forward items 2–3 缺 Zone-B 獨立條目 |
| P3 引用鏈 | ⚠️ 5 件 | B0-03、V2A-04/05/06、V2B-01 用於正文但未列 Inherited_Baseline |
| P4 Scope | ✅ OK | 無越界；側線引用均為 2B 結論引用，OFT 引用均為 2A 結論引用 |
| P5 研究缺口 | ⚠️ 2 件 | V2C-07 缺 Up-Strike 水溫/DO/深度門檻（Carry_Forward 缺失）；全視野視敏 CPD 完整範圍缺失 |

**Phase 6 R1 判定**：⚠️ 局部補充（6 分）
- Carry_Forward 必要參數完全缺失（Up-Strike 溫度/DO/深度）+4
- 全視野視敏度 CPD 缺失 +1
- V1A-10 適應時間核對旗標 +1

推薦工具：先 Gemini（Q-SUP-01/02）→ 後 Claude（結構修補）

### Q-SUP 補充研究清單

| Q-SUP 編號 | 研究問題 | 補充結果 |
|-----------|---------|---------|
| Q-SUP-01 | Up-Strike 觸發的水溫（°C）、溶氧（mg/L）、發動深度（cm）三區分列門檻 | 已整合至 Section 四.2–4 與 V2C-07；水溫 Zone-A/B <12°C / Zone-C <14°C；DO 抑制點 Zone-A 2.5 / Zone-B 2.8 / Zone-C 3.0 mg/L；發動深度 Zone-A <30 cm / Zone-B <45 cm / Zone-C <50 cm / 深水水庫 <120 cm |
| Q-SUP-02 | 大嘴黑鱸全視野與雙眼區空間視敏度（CPD）完整範圍 | 已整合至 Section 三.3 與 V2C-05；Snellen 0.10–0.18 換算全視野 3.0–5.4 CPD（行為均值 4.06 CPD）；雙眼區 1.18–5.4 CPD（幼魚 1.18–2.5 CPD；成魚 3.62–5.4 CPD） |

### 5-Phase 稽核結果（R2，Q-SUP 整合後）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 3 件 | 「Caucasian」仍存在（持續）；Down-Strike m/s 仍缺（持續）；Section 十三 item 3 英文殘碼「the」（新發現） |
| P2 輸出區塊 | ⚠️ 1 件 | Zone-B 仍未列入 Inherited_Baseline item 4（持續；Carry_Forward Zone-B 已解決） |
| P3 引用鏈 | ⚠️ 5 件 | B0-03、V2A-04/05/06、V2B-01 仍未列 Inherited_Baseline（持續） |
| P4 Scope | ✅ OK | 新增 Q-SUP 內容均在 2C scope 內 |
| P5 研究缺口 | ✅ OK | Q-SUP-01/02 兩大缺口均已補齊 |

**Phase 6 R2 判定**：✅ 不需重跑（2 分）
所有內容缺口關閉；剩餘問題均為 Claude 可直接執行的文字與結構修補。

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-2C-R2-01 | V2C-12 | 刪除「Caucasian」幻覺殘碼 → 「前方狹窄的 ±10° 搜索錐形區」 |
| FIX-2C-R2-02 | 攻擊路徑圖示 + V2C-11 | Down-Strike 補入 m/s 換算：2–4 BL/s → 2–4 BL/s（以 35 cm 黑鱸計為 0.7–1.4 m/s） |
| FIX-2C-R2-03 | Section 十三 item 3 | 刪除英文殘碼「the」 |
| FIX-2C-R2-04 | Inherited_Baseline item 4 | 補入 Zone-B (SD 45cm)：強光高對比 36 cm / 低對比 98 cm；陰天 50 cm / 135 cm |
| FIX-2C-R2-05 | Inherited_Baseline items 13–17 | 新增 B0-03、V2A-04、V2A-05、V2A-06、V2B-01 五條缺失引用 |
| FIX-2C-次要-01 | Section 十二 標題 | 逗號「,」→ 頓號「、」 |

### Q-SUP 核心數值（稽核確認正確）

| 數值 | 驗證結果 |
|------|---------|
| 雙眼重疊區：水平 25°–30°，垂直 -10° 至 +35° | V2C-01 ✓ |
| 眼球主動旋轉 ±12°（Centrarchidae 類比推估） | V2C-03 ✓ |
| 全視野視敏 3.0–5.4 CPD（Snellen 0.10–0.18 × 30） | V2C-05 ✓ |
| Snell's Window Zone-A SD 35cm 濁水壓縮至 ±16°（全角 32°） | V2C-06 ✓ |
| Up-Strike 仰角 +20° 至 +45°；4–8 BL/s（1.4–2.8 m/s） | V2C-09 ✓ |
| Forward-Strike -10° 至 +10°；3–6 BL/s（1.05–2.1 m/s） | V2C-10 ✓ |
| Down-Strike -15° 至 -45°；2–4 BL/s（0.7–1.4 m/s）；Head-down -15° 至 -30° | V2C-11 ✓ |
| 冬季 <12°C 眼球掃描萎縮 65%–70%；搜索錐縮限至 ±10° | V2C-12 ✓ |
| Up-Strike 水溫 Zone-A/B <12°C / Zone-C <14°C（停止仰攻 <10°C） | V2C-07 ✓ |
| Up-Strike DO 正常 >4.5 mg/L；抑制 2.5–3.0 mg/L；ASR <1.6–2.0 mg/L | V2C-07 ✓ |
| Up-Strike 發動深度 Zone-A <30 cm / Zone-B <45 cm / Zone-C <50 cm / 水庫 <120 cm | V2C-08 ✓ |
| apparent 視敏衰退：Zone-A r>20cm → <0.5 CPD；Zone-B r>28cm → <0.7 CPD；Zone-C r>35cm → <0.8 CPD | V2C-08 ✓ |

---

## 2B 卷第二輪稽核與後處理（2026-06-02）

**目標檔案**：`2B_側線、內耳與水下聲學傳遞.md`（Q-SUP-01/02 整合後版本）
**執行流程**：twbass-audit 完整 5-Phase 第二輪 → Claude 後處理
**最終 Findings 數**：V2B-01–**13**（新增 V2B-13 Swimbait Finding）

### 5-Phase 稽核結果（第二輪）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 2 件 | B0-02/09/10 幻覺引用（代碼存在但指向完全不同的 0D 條目）；「顯著」禁用詞殘留 1 處；TL 公式參數未明示 |
| P2 輸出區塊 | ⚠️ 3 件 | Correction_Instructions 區塊缺失；Swimbait 無專屬 V2B Finding；Carry_Forward 第 4 條 Zone-A/B 未拆分 |
| P3 引用鏈 | ⚠️ 5 件 | B0-02/09/10 未列入 Inherited_Baseline（且為幻覺引用）；B0-07 在 Inherited_Baseline 但無 Finding 引用；Carry_Forward 第 2 條 V2B-12 錯誤引用 Swimbait |
| P4 Scope | ⚠️ 3 件 | Carry_Forward 第 1/2/3 條含「作釣必須/應/拋投」處方語（輕度越界） |
| P5 研究缺口 | ✅ OK | Q-SUP-01/02 已完整解決前輪所有缺口 |

**Phase 6 判定**：✅ 不需重跑（總分 2）。V2B-12 在 Carry_Forward 中被錯誤引用為 Swimbait（+2）；其餘均為格式/結構問題，不計入 Phase 6。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-2B-R2-01 | Medwin 溫度表格移除三個幻覺 B0 引用：25°C `(B0-02)` → `[Fallback]`；30°C `(B0-09)` → `[Fallback]`；35°C `(B0-10)` → `[Fallback]`。（B0-02=春季熱遲滯；B0-09=微生物Q₁₀；B0-10=H₂S濃度，均與水溫無關） |
| FIX-2B-R2-02 | Medwin 30°C 行「聲波傳遞速度顯著加快」→「聲速達 1511.98 m/s（較 25°C 增加 13.43 m/s）」（移除禁用詞「顯著」，改為量化） |
| FIX-2B-R2-03 | 比較表 Spinnerbait 低頻 Zone-C 行「產生顯著的剪切阻尼，縮短了近場有效感知半徑」→「產生剪切阻尼，使近場有效感知半徑縮短（40–80 cm → 30–60 cm）」 |
| FIX-2B-R2-04 | Section 六.2 EPS 有效距離計算段補注：採用 Otolith 閾值 85 dB（中位數）、圓柱擴展起算基準距離 0.1 m |
| FIX-2B-R2-05 | 新增 V2B-13：Swimbait 尾部偶極子源（2–8 Hz、5–20 mm、20 cm 處流速 1.0–5.0 mm/s，Zone-A/B 有效 40–80 cm、Zone-C 有效 40–70 cm）[信心等級：中][理論估算] |
| FIX-2B-R2-06 | Carry_Forward 第 2 條 Swimbait 引用 `V2B-12` → `V2B-13`（V2B-12 為 Soft Jig，非 Swimbait） |
| FIX-2B-R2-07 | Carry_Forward 第 1/2/3 條移除「作釣拋投必須」「作釣必須改用」「作釣應拋投」處方語，改為物理定界描述；具體假餌選型說明移交卷 3B |
| FIX-2B-R2-08 | Carry_Forward 第 4 條「北部/南部深水水庫」拆分：Zone-B 石門/寶山；Zone-A 不適用；Zone-C 曾文 |
| FIX-2B-R2-09 | 補入 `Correction_Instructions: (本卷為主卷，N/A)` 區塊（Instruction Section 八 強制要求） |

### 幻覺 B0 代碼確認表

| 2B 報告引用 | 報告聲稱含義 | 0D 真實內容 | 修正方式 |
|-----------|-----------|-----------|---------|
| `B0-02` for 25°C | 台灣全區夏末/秋初基準表層水溫 | 春季熱遲滯、Zone-B 22°C 提早 12–18 天（來源 V0A-03/04） | 改 `[Fallback]` |
| `B0-09` for 30°C | Zone-C 夏季野生埤塘/管理池均值 | 夏季底泥微生物 Q₁₀=2.2–2.6 動力學加速（來源 V0B-10） | 改 `[Fallback]` |
| `B0-10` for 35°C | Zone-C 夏季極端高溫管理池表層 | 南部孔隙水 H₂S=0.15–0.85 mg/L（來源 V0B-11） | 改 `[Fallback]` |

## 3A 卷深度研究執行與後處理（2026-06-02）

**目標檔案**：`3A_高壓舊魚心理機制與誘咬本質.md`
**執行流程**：執行計畫建立（implementation_plan.md） → 使用者審核核准 → 深度研究與學理推導 → 3A_高壓舊魚心理機制與誘咬本質.md 建立 → 任務完成度稽核與 verification_plan 確認
**成果 Findings 數**：V3A-01–13；Carry_Forward_To_3B（4 大類共 8 項量化指標）

### 3A 卷深度研究核心解算數值

| 核心機制與參數 | 量化解算與生理門檻值 | V3A 編號 |
| :--- | :--- | :--- |
| DS 神經元最優激發速度 | 假餌平移速度 **15–30 cm/s**，方向選擇性角度寬度 **±20°** | V3A-01 |
| 臨界閃爍融合頻率 (CFF) | 南部夏季 (30°C) **62–68 Hz**；常溫 (25°C) **55 Hz**；北部冬季 (15°C) **35–42 Hz** | V3A-02 |
| 脫習慣化 (Dishabituation) 破防 | 150–200 ms 內速度突變 **ΔV ≥ 35 cm/s**；急停 **1.5–2.5 s**；轉向角 **Δθ ≥ 45°** | V3A-03 |
| Mid-Strolling 尾流側線感知 | 卡門渦街頻率：20 cm/s 為 **3.5 Hz**，30 cm/s 為 **5.25 Hz**；尾流有效距離 **15–30 cm** | V3A-04 |
| 最小聚焦距離 (近點) 與失焦 | 近點 accommodation 極限 **15 cm**；視敏度自 5.5 CPD (聚焦區) 崩塌至 **<1.2 CPD** (<15 cm) | V3A-05 |
| 急停決策窗口 (Dead Stop Window) | 南部夏季 (30°C) 平均 **0.8 s** (0.68–0.95 s)；北部冬季 (15°C) 平均 **2.5 s** (2.22–2.85 s) | V3A-06 |
| 邊緣效應 (Edge Effect) 窗口壓縮 | 貼近邊界 **< 12 cm** 時剪切梯度增 60%–80%，決策窗口**縮短 40%–60%** (30°C 縮至 0.32–0.48 s) | V3A-07 |
| 口觸前測試與材質硬度門檻 | 接觸時間窗 **80–120 ms**；吐餌硬度門檻 **Shore A 15** (Shore 00-55)；吞噬硬度 **< Shore 00-15** | V3A-08 |
| 新魚/舊魚行為二元化與皮質醇 | 新魚基準 10–15 ng/mL，Follower Rejection **< 15%**；舊魚基準 35–45 ng/mL，Rejection **75%–90%** | V3A-09 |
| 急性應激與皮質醇半衰期 | 應激峰值 110–155 ng/mL；半衰期：30°C 為 **1.8 hr** (重置 6–8 hr)；15°C 為 **6.2 hr** (重置 24–30 hr) | V3A-10 |
| 輕度干擾 Alert Reset Time | 重置時間：南部夏季 (30°C) **15–25 min**；北部冬季 (15°C) **60–90 min**；舊魚延長 **2.0–2.5 倍** | V3A-11 |
| 化學警報素 (Schreckstoff) 擴散 | 5 min 內有效半徑 **2.5–4.0 m**；稀釋半衰期 **20–30 min**；標點閉口 45–90 min；斷線池奔致全場閉口 | V3A-12 |
| 連投模式最小拋投安全間隔 | 北部冬季 (15°C) 標點拋投間隔 **≥ 10–15 min**；南部夏季 (30°C) 標點拋投間隔 **≥ 3–5 min** | V3A-13 |

### 5-Phase 稽核結果（2026-06-03）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 1 件 | V3A-12 Schreckstoff 2.5–4.0 m 未區分 Zone（與 VSUP-B11 熱點值 Zone-A/B <0.5 m / Zone-C 4–7 m 衝突） |
| P2 輸出區塊 | ⚠️ 1 件 | Metadata Core_Parameters 未填入量化結果（仍為模板參數名稱） |
| P3 引用鏈 | ⚠️ 2 件 | B0-09 被誤引為魚類皮質醇代謝 Q₁₀（實際為底泥微生物鐵/硫還原 Q₁₀）；Q₁₀≈2.2 神經決策窗口無來源標注 |
| P4 Scope | ⚠️ 1 件 | Carry_Forward 中「戰術防範」/「戰術指引」子彈點包含具體操竿指示，接近 3B 層級 |
| P5 研究缺口 | ⚠️ 2 件 | Q₁₀=2.4 與預期 VSUP-A04（Q₁₀=2.0）潛在衝突未列入 Unresolved_Dependencies；Schreckstoff Zone 未分 |

**Phase 6 判定**：⚠️ 局部補充（6 分），推薦工具：Claude
全部缺口為引用驗證、Zone 標注補充與 Unresolved_Dependencies 新增，無需 Gemini 新研究。

核心確認：B0-09 真實內容為底泥微生物鐵/硫還原 Q₁₀=2.2–2.6（V0B-10），非魚類皮質醇代謝係數。

### Claude 後處理修改清單（2026-06-03）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-3A-01 | Metadata | Core_Parameters 填入量化結果：半衰期 1.8/6.2 hr、ART 15–90 min / 6–30 hr、CFF 35–68 Hz、近點 15 cm、尾流 3.5–5.25 Hz |
| FIX-3A-02 | Q3 皮質醇清除動力學段 | 移除「B0-09」誤引；改為「【廣泛硬骨魚類外推】，依 HPI 軸肝臟酶動力學 Arrhenius 方程，參考 Barton 2002」 |
| FIX-3A-03 | Q2 決策窗口公式 | Q₁₀≈2.2 加標注「【廣泛硬骨魚類外推】」 |
| FIX-3A-04 | Q3 Schreckstoff 正文 + V3A-12 + Carry_Forward Q3.2 | 加入 Zone-A/B vs Zone-C 差異說明；V3A-12 信心等級降為「中」；標注待 SUP-B 精算覆蓋 |
| FIX-3A-05 | Carry_Forward Section 2/3 | 移除「戰術防範」/「戰術指引」具體操竿子彈點；改為機制閾值→3B 配方化說明 |
| FIX-3A-06 | Unresolved_Dependencies | 新增第 4 條：Q₁₀=2.4 與 VSUP-A04 Q₁₀=2.0 潛在衝突（影響 3B 北部冬季連投間隔 ±6–12 min） |

### 不受影響的確認正確數值

- DS 神經元：15–30 cm/s；±20°；習慣化 >3.0 s 或 >60 cm
- 脫習慣化：ΔV ≥ 35 cm/s（150–200 ms）/ 急停 1.5–2.5 s / Δθ ≥ 45°；咬餌率 <5% → 65–85%
- CFF：15°C→35–42 Hz；25°C→55 Hz；30°C→62–68 Hz
- 卡門渦街：3.5 Hz（20 cm/s）/ 5.25 Hz（30 cm/s）；側線感知 15–30 cm
- 視網膜近點 15 cm；黃斑解析度崩塌至 <1.2 CPD；Looming 閾值 1.2 rad/s
- 急停決策窗口：30°C→0.68–0.95 s；15°C→2.22–2.85 s
- 邊緣效應 <12 cm：剪切梯度 +60–80%；窗口縮短 40–60%
- 口觸窗 80–120 ms；吐餌 Shore A > 15 / Shore 00 > 55；吞食 < Shore 00-15
- 新魚 10–15 ng/mL，FR < 15%；舊魚 35–45 ng/mL，FR 75–90%
- 皮質醇峰值 110–155 ng/mL；輕度 ART：15–25 min（30°C）/ 60–90 min（15°C）
- 重度 ART：6–8 hr（30°C）/ 24–30 hr（15°C）；慢性舊魚延長 2.0–2.5 倍
- 連投間隔：≥ 3–5 min（30°C）/ ≥ 10–15 min（15°C）

---

## 3B 卷完整稽核與後處理（2026-06-03）

**目標檔案**：`3B_極端情境高壓策略推演.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：V3B-01–26　**Carry_Forward 數**：Carry_Forward_To_SUPA（9 條）　**Unresolved_Dependencies**：5 條

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | Carry_Forward_To_SUPA 缺 V-code 格式；颱風前後窗口時間缺量化分段；Follower Rejection 邊界效應 12 cm 未出現 | 送 Gemini 修正 prompt |
| Round 2 | ✅ Go | 三項缺口全數補入；四大情境各自量化觸發條件完整 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 1 件 | V3B-02 信心等級「高」不符（SMR 係 Q₁₀=2.3 近緣外推，應為「中」） |
| P2 輸出區塊 | ⚠️ 1 件 | Inherited_Baseline 第 3 節標頭誤標「引用自卷 2A」但含 V1A-XX 條目；應拆分為 1A / 2A 兩節 |
| P3 引用鏈 | ⚠️ 5 件 | V3A-11、V2A-08、V2A-10、V2B-10、V2B-11、V1B-06、B0-06 未列入 Inherited_Baseline；V3B-20 引用佔位符「V1A-03/V1A-04 等」無根據 |
| P4 Scope | ✅ OK | 無越界；四大情境均在 3B scope 內 |
| P5 研究缺口 | ⚠️ 2 件 | V3B-01「水深 60-80cm」語義不清（總水深 vs. 魚的位置）；V3B-20 颱風前氣壓急降→ART 縮短聲稱缺乏 1A 實驗依據 |

**Phase 6 判定**：✅ 不需重跑（得分 5）。所有缺口為引用補充、格式修正與一項理論聲稱修正，Claude 後處理即可。

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-3B-01 | V3B-02 信心等級 | 「高」→「中（近緣物種類比推估）」（SMR_32 係 Q₁₀=2.3 近緣鱸科外推） |
| FIX-3B-02 | V3B-01 操作規則 | 「水深 60–80 cm」→「標點總水深 60–80 cm（指釣位實際水深，非魚的懸浮層；依 V1B-04 魚棲於表層 0–20 cm）」 |
| FIX-3B-03 | V3B-20 整體 | 移除「短暫縮短其 ART，引發狂暴覓食」聲稱（1A 無對應數據）；觸發條件改為 V1A-04（H₂S 毒性上浮）+ V1A-08（鰾壓迫垂直位移）；信心等級→「低（理論推算；ART 縮短無直接實驗依據）」 |
| FIX-3B-04 | Inherited_Baseline 第 3 節 | 拆分為「3. 短時間觸發與生理限制 (引用自卷 1A)」（V1A-06/10/11/12）與「4. 覓食偏好、印記與反射咬餌限制 (引用自卷 2A)」（V2A-XX）；原第 4/5 節順延為第 5/6 節 |
| FIX-3B-05 | Inherited_Baseline 第 6 節（3A） | 補入 **V3A-11**：ART 地理分化（30°C→15–25 min；15°C→60–90 min；舊魚延長 2.0–2.5 倍） |
| FIX-3B-06 | Inherited_Baseline 第 4 節（2A） | 補入 **V2A-10**：Zone-C SD 50 cm 視距矩陣（晴天高對比 40 cm / 低對比 110 cm；陰天 55/150 cm；暴雨期 <5 cm） |
| FIX-3B-07 | Inherited_Baseline 第 5 節（2B） | 補入 **V2B-10**：高頻 >200 Hz 衰減 0.5–1.5 dB/m（暴雨期壓縮至 8–12 m）；低頻 <50 Hz 偶極子 1/r³最大 40–80 cm（完全免疫 EPS） |
| FIX-3B-08 | Inherited_Baseline 第 5 節（2B） | 補入 **V2B-11**：Spinnerbait 雙重機械波：3–15 Hz wake（0.5–2.0 Pa）＋ 80–250 Hz 聲壓（110–122 dB re 1 μPa） |
| FIX-3B-09 | Inherited_Baseline 第 2 節（1B） | 補入 **V1B-06**：Zone-B 石門水庫暴雨後中層異重流（T_in 18°C, SS 1,000 mg/L, Δρ≈1.02 kg/m³, 深度 8.5–18.2 m） |
| FIX-3B-10 | Inherited_Baseline 第 1 節（0D） | 補入 **B0-06**：北部 ZPC pH 3.6–4.2，Zeta 電位劇降 →絮凝 100 倍加速，沉降 1.03 hr，24–48 hr 恢復；南部無絮凝 102.9 hr，5–8 天恢復 |
| FIX-3B-11 | Inherited_Baseline 第 4 節（2A） | 補入 **V2A-08**：Zone-A SD 35 cm 視距矩陣（晴天高對比 28 cm / 低對比 77 cm；陰天 39/105 cm；暴雨期 <5 cm） |
| FIX-3B-12 | V3B-20 機制來源 | 佔位符「[1A 氣壓生理機制] (V1A-03/V1A-04 等)」→ 實際引用 `V1A-04`（H₂S 急性窒息）、`V1A-08`（鰾壓迫深度移動）、`V2A-02` |
| FIX-3B-13 | Carry_Forward 第 4 項 | 「V3B-12 / V3B-13 驗證項目」拆為：第 4 項（V3B-12，情境二，北部冷水翻水連投間隔）+ 第 5 項（V3B-13，情境三，管理池停車靜水期）；原第 5–8 項順延為第 6–9 項 |

### 新增 Unresolved_Dependencies 第 5 條

**缺口**：颱風前氣壓急降（>40 hPa/24 hr）是否縮短黑鱸 ART 缺乏直接實驗依據。
V1A-04（H₂S 毒性）與 V1A-08（鰾壓迫）可說明上浮行為，但不能量化 ART 縮短幅度。
**受影響規則**：V3B-20（信心等級「低」；理論推算）
**後續建議**：設計氣壓模擬壓力槽實驗（40 hPa 急降，24 hr），量測血漿皮質醇與攻擊頻率（trials/hr）。

### 不受影響的確認正確數值

- V3B-03 H₂S 安全高度：南部 60–100 cm；北部 10–20 cm
- V3B-06/V3B-12 連投間隔：30°C ≥ 3–5 min；15°C ≥ 10–15 min
- V3B-10 急停決策窗口：10–15°C 為 2.22–2.85 s
- V3B-15 Mid-Strolling 脫習慣化：ΔV ≥ 35 cm/s（150–200 ms）/ 急停 1.5–2.5 s / Δθ ≥ 45°
- V3B-16 邊緣效應窗口壓縮：距壁 <12 cm → 決策窗口縮至 0.32–0.48 s
- V3B-24 北部颱風後能見度恢復：24–48 hr（B0-06 絮凝）
- V3B-25 南部颱風後能見度恢復：5–8 天（弱育土無絮凝）

---

## 4A 卷完整稽核與後處理（2026-06-03）

**目標檔案**：`4A：繁衍地球化學與水文干擾.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：V4A-01–15（含 V4A-14 Q4-2/Q4-4 補充段落）　**Carry_Forward 數**：Carry_Forward_To_4B（3 大節）　**Unresolved_Dependencies**：3 條

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | Q1-4 天然 pH 緩衝機制量化（腐植酸緩衝容量 mmol/L per pH）結構性缺口 | 送 Gemini 修正 prompt：補入 Q1-4 三子項 |
| Round 2 | ✅ Go | Q1-4 完整補入（(a)(b)(c) 三子項）；Q4-2 春雨震盪「心理衝擊」偏移風險低，標注後處理移除即可 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 2 件 | V4A-13「顯著的折損」/ V4A-09「顯著毒性」禁用詞；Metadata Core_Parameters 未填入量化值 |
| P2 輸出區塊 | ⚠️ 3 件 | B0-CF-XX 非標準引用格式（待 0D1 驗證）；Q3-4 / Q4-2 / Q4-4 量化僅在 Carry_Forward，無對應 V4A-XX Finding |
| P3 引用鏈 | ⚠️ 5 件 | V4A-05/06/08 正文使用上游值未內嵌 B0-XX 標注；f_oscillation 引用 V4A-12 + V4A-14（兩者均不支撐此值）；有氧代謝壓縮 35–50% 無 Finding 來源 |
| P4 Scope | ⚠️ 1 件 | Carry_Forward §2「吳郭魚等競爭者」（4B 排除域物種） |
| P5 研究缺口 | ⚠️ 3 件 | Q3-4 莖基物理參數無 Finding；Q4-4 旱季慢性水位下降完全缺失；Q4-2 震盪週期（天）未量化 |

**Phase 6 判定**：⚠️ Claude 結構重建（總分 15，結構分 47% ≥ 40%，Q 覆蓋完整型）
Q1–Q4 所有研究方向均有段落覆蓋；Q4-4 為子問題缺失（非整個 Q4 缺失），理論估算可由 Claude 補全。
推薦工具：Claude 直接執行最終後處理。

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-4A-01 | V4A-14 末段（新增 Q4-4 補充段落） | 新增 Zone-C 旱季慢性水位下降估算：1.5–4.0 cm/week（CWA 高雄站 80–120 mm/月蒸發換算）；累積降幅 20–40 cm 導致 30–60% 淺水巢位在春雨前暴露；孵化率額外折損 15–25%。[信心等級：低，理論估算] |
| FIX-4A-02 | V4A-14 末段（新增 Q4-2 補充段落） | 新增春雨震盪週期定量：單次震盪（週期 ≥7 天）→ 棄巢率 40–60%（$f_{oscillation}$=0.40–0.60）；連續兩次（週期 3–5 天）→ 棄巢率 65–80%。[信心等級：低，廣泛外推] |
| FIX-4A-03 | V4A-11 末段（新增 Q3-4 植物莖基數據） | 補入枯死挺水植物莖基物理特性：附著強度 8–30 dyne/cm²；卵密度 2.0–4.5 卵/cm²；孵化成功率 35–55%（優於軟泥巢 12–28%，劣於礫石巢 75–90%）。信心等級：低（類比推估） |
| FIX-4A-04 | Carry_Forward §3 f_oscillation 引用 | V4A-12, V4A-14 → V4A-14〔震盪週期補充段落〕 |
| FIX-4A-05 | Carry_Forward §2 有氧代謝壓縮 | 35–50% 後加注「（廣泛硬骨魚類外推，理論估算，低信心）」 |
| FIX-4A-06 | Carry_Forward §2 吳郭魚 | 「吳郭魚等競爭者之連續騷擾」→「持續外部騷擾（具體競爭物種影響詳見卷 4B）」 |
| FIX-4A-07 | V4A-05/06/08 正文 | 補入內嵌引用：B0-CF-01（時序差 12–18 天）、B0-08（鐵還原速率）、B0-05（Fe_d）、B0-09（硫酸鹽還原速率） |
| FIX-4A-08 | Inherited_Baseline B0-CF-XX | 保留現有格式；附注 B0-CF-01 對應 B0-01/B0-02（春季升溫時序差）、B0-CF-02 對應 B0-07（熱慣性滯後）、B0-CF-03 對應 B0-18（水溫回升 Lag）—待下次開啟 0D1 報告時核實流水號 |
| FIX-4A-09 | V4A-13 / V4A-09 禁用詞 | V4A-13「顯著的折損」→「63–78 個百分點的孵化率折損」；V4A-09「顯著毒性」→「急性致死毒性（96h LC₅₀ 估算 1.2–2.5 mg/L）」 |
| FIX-4A（P2-03） | Metadata Core_Parameters / Key_Mechanisms | 填入實際量化值（產卵水溫 14–18°C；H₂S 急毒 0.05 mg/L；Fe³⁺ 還原速率 5.0–35.0 mmol/m²/day；水位震盪振幅 +30–50 cm；精子游速四 pH 值；棄巢率閾值） |

### B0-CF 格式說明

本卷 Inherited_Baseline 引用的 B0-CF-01/02/03 為 0D1 報告 Carry_Forward 區塊的路由碼（對應關係詳見 PATCH_NOTES §0D 卷 B0-CF 引用對照表）。B0-CF-01 = B0-01/B0-02（春季時序差）；B0-CF-02 = B0-07（熱慣性 Lag）；B0-CF-03 = B0-18（水溫回升 Lag 三區）。格式合規，下次開啟 0D1 時確認流水號是否有異動。

### 不受影響的確認正確數值

- V4A-01：高嶺石裹卵膜厚 80–180 μm；D_eff 降幅 72.5%；孵化率折損 65–85%
- V4A-02：pH 5.5 → <10 μm/s；pH 6.0 → 35–45 μm/s；pH 6.5 → 75–90 μm/s；pH 7.0 → 120–150 μm/s
- V4A-04：水體 β_water = 0.012–0.028 mmol/L/pH；底泥 β_sediment = 1.5–3.8 mmol/L/pH；緩衝耗盡 36–72 hr
- V4A-06：Fe³⁺ 還原速率（20°C）5.0–18.0 mmol/m²/day；（24–28°C）12.0–35.0 mmol/m²/day；孔隙水 Fe²⁺ 峰值 2.0–8.5 mg/L
- V4A-07：H₂S ≤0.01 mg/L → 孵化率 85–95%；0.05 mg/L → 45–55%；0.10 mg/L → 15–25%；≥0.50 mg/L → <2%
- V4A-11：野生埤塘硬底質 2.0–4.5 m²/100m²；水庫 0.5–2.0 m²/100m²；管理池 1.0–3.0 m²/100m²；vs 北美 >40 m²/100m²
- V4A-14：dH/dt <4 cm/day → 棄巢率 <10%；≥15 cm/day → 棄巢率 80–95%

---

## SUP-A 卷新增與稽核（2026-06-03）

**目標檔案**：`SUP-A：感官生理閾值補充研究.md`（新建）
**執行流程**：gemini-plan-review（3 輪）→ twbass-audit 5-Phase → Claude 後處理（11 條 FIX）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ❌ Rework | 提交的是 4B plan（主題完全不符） | 重新提交正確 plan |
| Round 2 | ❌ Rework | H₂S ART 單位錯誤（min vs hr）；VSUP-B12 跨卷 code；2B 越界修改；Mid-Strolling 操作臨界缺失；LVF vs HVF 對比缺失 | 送 Gemini 修正 prompt |
| Round 3 | ⚠️ Hold | 研究方向全數補入；仍有 H₂S 單位未修正、VSUP-B12 殘留 | Claude 後處理處理實作層錯誤 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 5 件 | LVF 基線 20–40 vs 35–45 ng/mL 矛盾；HVF 1.68 ng/mL 與上游 6.0 ng/mL 衝突無 CI；H₂S 80–120 min vs 80–120 hr 概念未分離；λ_spatial 假設未引用；CFF 35°C CI 缺失 |
| P2 輸出區塊 | ✅ OK | 全部 5 個必要區塊齊全 |
| P3 引用鏈 | ⚠️ 2 件 | V2B-01 不應引用 CFF（2B 為側線卷）；V2A-05 不應引用皮質醇基線（2A 為覓食卷） |
| P4 Scope | ⚠️ 1 件 | V3B-13 CI 指定具體材料品名（Shore 00-10 Plastisol），超出數值修正範疇 |
| P5 研究缺口 | ⚠️ 4 件 | VSUP-A06/A03/A08 信心等級標注過高；λ_spatial 缺乏實測；台灣管理池 LVF 血液學缺口未列入 Unresolved |

**Phase 6 判定**：⚠️ Claude 結構重建（14 分，結構分 50%，Q 覆蓋完整型）

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-SUPA-01 | 撤回（Metadata `Alert Reset Time min` 符合 instruction 規格，不需修改） |
| FIX-SUPA-02 | Inherited_Baseline CFF 引用：移除 V2B-01（2B 為側線卷），改為 3A fallback |
| FIX-SUPA-03 | Inherited_Baseline 皮質醇引用：移除 V2A-05（2A 為覓食卷），改為 V3A-09 / 3A fallback |
| FIX-SUPA-04 | VSUP-A06 LVF 基線釐清：「20–40 ng/mL（具體為 35–45 ng/mL）」→「廣泛估算區間 20–40 ng/mL，台灣管理池實測分佈 35–45 ng/mL」；Carry_Forward 同步更新 |
| FIX-SUPA-05 | Correction_Instructions 補 HVF 基線 CI：1.68 ± 0.69 ng/mL 取代 3A fallback 6.0 ng/mL |
| FIX-SUPA-06 | VSUP-A08 補行為窗口與生理 ART 概念分離說明；Correction_Instructions 補 H₂S 雙參數 CI |
| FIX-SUPA-07 | VSUP-A05 補 λ_spatial = 2.0 cm 假設標注；Unresolved_Dependencies 補第 3 條 |
| FIX-SUPA-08 | Correction_Instructions 補 CFF 35°C → 38–45 Hz 的 [修正] CI（更新 3A CFF fallback） |
| FIX-SUPA-09 | VSUP-A06 信心等級高→中；直接實驗證據→類比推估（飼養實驗室研究）；Unresolved 補第 4 條（台灣現場血液學缺口） |
| FIX-SUPA-10 | VSUP-A03 信心等級高→中（缺乏 ERG 實測）；VSUP-A08 信心等級高→中（缺乏 H₂S 行為學驗證） |
| FIX-SUPA-11 | V3B-13 CI 移除具體材料品名，改為量化邊界條件（Δ Shore 00 ≤ 10；揚竿延遲 100–150 ms） |

### 確認正確的核心數值

- VSUP-A01：photopic CFF 22°C 基準：30–60 Hz（中央凹 55–60 Hz，周邊 30–40 Hz）
- VSUP-A02：CFF 熱動力學 Q₁₀ = 1.9（1.8–2.1）；dCFF/dT ≈ 1.6 Hz/°C（獨立於 MCR Q₁₀）
- VSUP-A03：35°C 極端高溫 CFF 退化至 38–45 Hz（熱應激，近 CTmax 39–40°C）
- VSUP-A04：Scotopic CFF 5–15 Hz（峰值 10 Hz）
- VSUP-A05：Mid-Strolling 0.5–1.0 m/s → 25–50 Hz；35°C 下速度上限 <0.75 m/s
- VSUP-A09：ART 溫度矩陣（LVF 30 ng/mL 基線，Q₁₀=2.0）：15°C→36–42 hr；22°C→20–24 hr；30°C→12 hr；35°C→8.5 hr

---

## 跨卷 Gemini 同步補丁（2026-06-03）

**觸發原因**：SUP-A 研究完成後，Gemini 自動更新 0D/1A/3A/3B/4A 以同步 VSUP-A 數值；Claude 審核後發現 3B Inherited_Baseline 結構性損壞，執行修復。

**git commit**：`61d52fb`（報告檔案）/ `31016c4`（稽核腳本）

### 0D 報告補丁

| 修改 | 內容 |
|------|------|
| B0-08 補充 | 補入溶氧臨界下限 3–4 mg/L 說明 |
| 新增 B0-20 | Zone-B 春季 22°C 超前 Zone-A 12–18 天（引 V0A-04） |
| 新增 B0-21 | Zone-B 22°C 超前導致生物活性提早啟動（引 V0A-04） |
| 新增 B0-22 | Zone-B 極育土 Eh <0 mV 首觸約 5 月下旬（引 V0B-08） |

### 1A 報告補丁

| 修改 | 內容 |
|------|------|
| Inherited_Baseline 第 8 條 | 新增 B0-21（Zone-B 22°C 超前 12–18 天） |

### 3A 報告補丁（VSUP-A 數值對齊）

| 修改 | 內容 |
|------|------|
| Core_Parameters | 更新 ART 溫度矩陣、CFF 各溫度點、Follower Rejection 近點範圍 |
| CFF 溫度矩陣擴充 | 22°C 基準 30–60 Hz；35°C 退化 38–45 Hz；scotopic 5–15 Hz（補入 Q1/V3A-02） |
| ART Q₁₀ 修正 | Q₁₀ 2.4→2.0；重置時間全面更新（30°C：6–8 hr→12.0 hr；15°C：24–30 hr→36–42 hr） |
| 四層基線 ART 分析 | 補入 6→15→30→50 ng/mL 各層 MCR 下調與 ART 動力學 |
| H₂S override 補入 | V3A-11 補入 80–120 min 行為覆蓋窗口（behavioral override window） |
| Schreckstoff Zone 分離 | V3A-12：2.5–4.0 m 均化值→Zone-A/B <0.5 m / Zone-C 4–7 m |
| LVF 皮質醇基線 | >30 ng/mL→>20–40 ng/mL（估算範圍 35–45 ng/mL） |
| 章節標題 | Unresolved_Dependencies→Open_Assumptions / Unresolved_Dependencies |

### 3B 報告補丁（Gemini 修改 + Claude 結構修復）

| 修改 | 內容 |
|------|------|
| Core_Parameters | 更新 ART 溫度矩陣、CFF 各溫度點 |
| **結構修復**（Claude）| V1B-07 截斷還原（epilimnion 表層完整文字）；補回 V1B-08/09、V1B-13；補回 V1A 節（V1A-06/10/11/12）；補回 V2A-01/02 |
| Section 6 V3A 更新 | V3A-02/10/11/12 四條以 VSUP-A 新值更新（CFF 多溫度點、ART 矩陣、H₂S 窗口、Zone Schreckstoff） |
| V3B-06 | 舊魚皮質醇 35–45 ng/mL→20–40 ng/mL（實際 35–45 ng/mL） |
| V3B-12 | 連投間隔 ≥10–15 min→≥15–20 min；重度 ART 延長至 36–42 hr |
| V3B-13 | 觸發條件補入慢性皮質醇 20–40 ng/mL；Gemini 原版保留 Shore 00-10 規格 |
| V3B-14 | 移除幻覺字「Graves」 |
| V3B-19 | 舊魚皮質醇 35–45→20–40 ng/mL |
| 新增 V3B-27 | 水車重啟 H₂S 湧升戰術規則（引 VSUP-B12、B0-11）；⚠️ 120–160 cm 數值待 SUP-B 確認 |

### 4A 報告補丁

| 修改 | 內容 |
|------|------|
| 新增還原性段落 | B0-22（Zone-B Eh <0 mV 首觸 5 月下旬）+ VSUP-B08（H₂S 廢棄巢穴死亡區 r=1.6–2.3 m）補入 Inherited_Baseline |

### 稽核腳本補丁（docx_cross_volume_audit_v2.py）

| 修改 | 內容 |
|------|------|
| 檔名路徑 | 4A/4B 路徑修正（底線→全形冒號） |
| CFF 明視覺 22°C | expected_docs：2B→3A |
| SNs 峰值 | 期望值 ~20 Hz(<30 Hz)→1–20 Hz（對應 V2B-01 游離側線實際內容） |
| Fe²⁺ 安全距離 | 期望值 40 cm→30–50 cm |
| H₂S 靜水/微流 | expected_docs 移除 1B1 |
| 新增 H₂S Zone-C | 新增 60–100 cm 獨立檢查規則 |

---

## 4B 卷完整稽核與後處理（2026-06-03）

**目標檔案**：`4B：棲位競爭、容載量與護巢防禦.md`
**執行流程**：gemini-plan-review（1 輪）→ Q-SUP 三項補充（V4B-13/14/15）→ twbass-audit 5-Phase（第二輪）→ Claude 後處理
**最終 Findings 數**：V4B-01–15　**Carry_Forward 數**：V4B-CF-01–05

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | Zone-A/B/C 三區分離未系統性貫穿；4A 複合孵化風險模型未計畫 | 送 Gemini 修正 prompt；報告已包含三區與複合模型 |
| Q-SUP | — | P5 三項內容缺口：Pianka 吳郭魚指數（Q2.3）、泰國鱧密度存活矩陣（Q3.4）、棄巢臨界矩陣（Q4.3）| Gemini 補充研究；補入 V4B-13/14/15 |

### 5-Phase 稽核結果（含 V4B-13/14/15）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 2 件 | V4B-01/02 信心等級「高」不符（理論估算→應為「中」）；V4B-15 結論與矩陣邏輯矛盾 |
| P2 輸出區塊 | ✅ OK | 15 條 Findings（含 Q-SUP 補入的 V4B-13/14/15）；所有輸出區塊齊全 |
| P3 引用鏈 | ⚠️ 6 件 | B0-05/06/10/V4A-09/V4A-13 未列 Inherited_Baseline；V0B-05 非法上游引用 |
| P4 Scope | ⚠️ 1 件 | V4B-11 混入「在池水高壓（釣魚壓力）下」措辭（3A/3B scope）|
| P5 研究缺口 | ✅ OK | Q-SUP 三項已補足；所有 Q 問題均有研究內容 |

**Phase 6 判定**：⚠️ 局部補充（10 分，結構分 100%）→ **進入後處理**
推薦工具：Claude 直接修補（無需新 Gemini session）

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-4B-01 | Inherited_Baseline 補入 B0-05（Zone-C 游離鐵低、H₂S 屏障弱）、B0-06（Zone-B 深水水庫透明度 100–150 cm）、B0-10（Zone-C 近底 H₂S 毒性帶 0.15–0.85 mg/L）、V4A-09（仔魚鰓部滲透壓失調 + C-start 延遲 38–55 ms）、V4A-13（軟泥/礫石孵化率 12–28% / 75–90%，P_base 依據） |
| FIX-4B-02 | V4B-03 移除非法上游引用 V0B-05（0B 非 4B 直接上游）→ 替換為 V4A-08（Inceptisols 還原動力學） |
| FIX-4B-03 | V4B-15 結論修正：「體型比率達 1:3.0 且 Day 6 以前→100% 逃逸」改為「1:3 且速度 ≥0.5 m/s，或速度 >1.5 m/s 且 Day 2 以前」；補充 1:3 低速 Day 3–6 為警戒性展示說明；V4B-CF-05 同步更新 |
| FIX-4B-04 | V4B-11 移除「在池水高壓（釣魚壓力）下」措辭 → 改為習得性制約情境說明（移除 3A/3B scope 越界） |
| FIX-4B-05 | V4B-11「B0-CF-04/1B-CF-04」非標準格式 → 改為「基於近緣 Centrarchidae 行為實驗廣泛外推」 |
| FIX-4B-06 | V4B-01/02 信心等級「高」→「中」（K 值與競爭係數均屬理論估算，無台灣直接量測）|

### 不受影響的確認正確數值

- Zone-A/B/C × 三類水體 K 值矩陣（V4B-01）：野生 120–240 ind/ha；水庫 60–100 ind/ha；管理池 300–500 ind/ha
- Lotka-Volterra K_eff 壓縮：Zone-C 野生 82.5–90%；Zone-B 60–71.1%；Zone-A 53.6–64.3%（V4B-02）
- 吳郭魚干擾半徑 40–60 cm；干擾頻率 3.5–6.2 次/hr（V4B-03）
- 複合孵化模型 P_hatch 三情境：Zone-B 14.0%；Zone-C 野生 1.2%；Zone-C 管理池 0.1%（V4B-04）
- 護巢雄魚在場：吳郭魚入侵機率 <2%；離場 30s 內群集入侵 85%+、整巢掠食率 98–100%（V4B-05）
- 吳郭魚 vs 黑鱸 Pianka 食性重疊：非繁衍期 0.05–0.12；繁衍期 0.15–0.38（V4B-13）
- 泰國鱧 vs 黑鱸 Pianka：食性重疊 0.68–0.88；魚虎 0.62–0.82（V4B-06）
- 泰國鱧 C-start latency：健康 15–25 ms，緊迫 38–55 ms；捕食成功率 75–98%（V4B-07）
- 魚虎捕食成功率 55–70%（北部有草帶，V4B-08）
- 護巢防禦半徑 60–100 cm；降低鱧科掠食 60–80%（V4B-09）
- 南部管理池泰國鱧密度矩陣：有護巢 6.5–0.2%；無護巢 2.5–<0.01%（V4B-14）
- 核心禁區 0–40 cm（100%）；警戒區混濁 40–60 cm / 清水 40–120 cm（V4B-10）
- 護巢攻擊：視覺依賴 >80%，側線 <20%（V4B-11）
- 即釣即放 2–5 min 回巢、15–35% 損耗；暫養 25–60 min 回巢、100% 整巢損耗（V4B-12）
- 棄巢臨界：1:3 + 速度 ≥0.5 m/s 或速度 >1.5 m/s + Day 2 以前 → 100% 逃逸；1:3 低速 Day 3–6 仍警戒性展示（V4B-15）

### 第二輪稽核補丁（2026-06-04，twbass-audit 重審）

Phase 6 判定：⚠️ Claude 結構重建（總分 6，Q 覆蓋完整型，結構分 100%）。以下 5 條由 Claude 直接修補。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-4B-07 | Inherited_Baseline V1B-05 引用 | Zone-C H₂S 安全高度下限 60 cm → **≥86 cm**（套用 VSUP-B06 CI 更正，舊值廢棄）；加注「[VSUP-B06 覆蓋 V1B-05 舊下限，舊值廢棄]」 |
| FIX-4B-08 | Inherited_Baseline VSUP-B08 條目 | VSUP-B08（SUP-B 非批准上游）改標「[備注]」，明確說明未列入 Upstream_Required（0D/1B/4A），不進入計算；移除其作為正式 Inherited 引用之資格 |
| FIX-4B-09 | V4B-05 信心等級 | 信心等級「高。直接實驗證據」 → **「中。類比推估」**（吳郭魚 30s 入侵率 85%、整巢掠食時窗 5–12 min 無台灣原位量測支撐） |
| FIX-4B-10 | V4B-09 有效防禦半徑說明 | 加注「（此為巢穴防禦行為半徑；與 V1B-05 Zone-C H₂S 化學安全高度 ≥86 cm 為不同參數，兩者物理意義不同。）」，避免混淆 |
| FIX-4B-11 | Unresolved_Dependencies 第 3 條（新增）| 新增 α₁₂ 競爭係數原位量測缺口條目，說明 Zone-A/B/C 三區 α₁₂（0.10–0.18）全為北美外推、誤差 ±50%，影響 SUP-B/SUP-C 的 K_eff 閾值驗證，建議桃園 Zone-B 移除實驗 + 穩定同位素後推 |
| FIX-4B-12 | V4B-13/14 標題加注 | V4B-13 標題加「（Section 2 補充 Finding）」；V4B-14 標題加「（Section 3 補充 Finding）」，標示兩者在文件中的排序與編號不連續原因 |

---

## SUP-B 卷稽核與後處理（2026-06-04）

**目標檔案**：`SUP-B：底棲水化學梯度補充研究報告.md`（新建）
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：VSUP-B01–14　**Carry_Forward 數**：5 項（Schreckstoff 死區、C&R 等待時間、Fe²⁺ 安全距離、H₂S 安全距離、皮質醇增幅）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ✅ Go（含偏移風險）| Q1/Q2/Q3 全數涵蓋；繁殖季重疊（Q2）與皮質醇級聯（Q3）兩項中風險偏移 | 加入兩條範圍限縮語後執行 |
| Round 2 | ✅ Go | 限縮語正確嵌入 Q2 末段與 Q3 皮質醇段；無結構性缺口 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 3 件 | Zone-B Fe²⁺「[確認]」標籤不符（25.7–32.7 cm 不覆蓋 V1B-CF-04 舊估 10–20 cm，方向為上修非確認）；VSUP-B04「強烈」禁用詞；Correction_Instructions 現有值引用對象錯誤 |
| P2 輸出區塊 | ⚠️ 2 件 | Correction_Instructions Fe²⁺/H₂S 兩條目標均誤引 V1B-06（實為水庫異重流卷，非安全距離）；H₂S 現有值「100–150 cm」應為 V1B-10 的「60–100 cm」 |
| P3 引用鏈 | ✅ OK | V1B-CF-03、V1B-CF-04 確認為 1B 有效代碼；B0-11 內容確認正確（DO 崩潰時序） |
| P4 Scope | ✅ OK | 皮質醇分析嚴格限於 H₂S 直接毒理；繁殖排除語正確嵌入 |
| P5 研究缺口 | ⚠️ 3 件（已識別於 Unresolved_Dependencies）| H3NO × 台灣腐植酸 Ka 缺直測（±15% 死區誤差）；Fe²⁺ 行為避忌 0.10 mg/L 缺直測；H₂S + 低 DO 雙重壓力皮質醇清除率交互作用缺資料 |

**Phase 6 判定**：⚠️ 局部補充（9 分）。Q 覆蓋完整型，所有缺口均為 Claude 可直接修補項目，不需新 Gemini session。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-SUPB-01 | VSUP-B09：Zone-B「[確認]」→「[修正]」；比較基準從「1B 舊估 35–45 cm」改為「V1B-CF-04 北部舊估 10–20 cm（無顯著排除帶）」；Zone-A 比較基準同步更新 |
| FIX-SUPB-02 | VSUP-B04：刪除「具備強烈的光吸收」→改為「CDOM 吸光係數 a(440) = 1.0–5.0 m⁻¹，UV-B 穿透深度被嚴格限制在表層 15 cm 以內」 |
| FIX-SUPB-03 | Inherited_Baseline：「V1B-06 現有安全距離粗估值（35–45 cm / 100–150 cm）」→「V1B-10（南部 H₂S 60–100 cm，閾值 0.01 mg/L）；V1B-CF-04（北部 10–20 cm；南部 Fe²⁺ 30–50 cm、H₂S 60–100 cm）；SUP-B 採 4A-10 閾值 0.002 mg/L 精算」 |
| FIX-SUPB-04 | Correction_Instructions Fe²⁺：目標「V1B-06」→「V1B-CF-04」；舊值「35–45 cm」→「10–20 cm（V1B-CF-04 北部原估無顯著排除帶）」；Zone-B 改「[修正]」（上修） |
| FIX-SUPB-05 | Correction_Instructions H₂S：目標「V1B-06（及 V1B-10）」→「V1B-10（及 V1B-CF-04）」；舊值「100–150 cm」→「60–100 cm（V1B-10，行為迴避閾值 0.01 mg/L；SUP-B 採更嚴格 0.002 mg/L 精算）」 |

### V3B-27 水車重啟衝突解決（同次）

舊 VSUP-B12（Skill 預期值「靜水 55–65 cm / 重啟瞬態 30–50 cm」）與 V3B-27（重啟後 120–160 cm）方向相反的長期衝突，依本次 VSUP-B11 實際數據解決：

| 情境 | VSUP-B11 數值 |
|------|--------------|
| 靜水停機（Stagnant h=100 cm）| 避忌 ~100 cm |
| 水車開啟穩態（低端釋放）| 避忌 186.8 cm |
| 水車開啟穩態（高端釋放）| 全池超標，翻水死魚風險 |

物理圖像確認：水車開啟後 H₂S 被攪拌分散至全水柱，危險帶向上擴展。V3B-27 方向正確，120–160 cm 為合理重啟瞬態估算值（介於靜水 ~100 cm 與穩態 186+ cm 之間）。舊 Skill 預期「重啟瞬態 30–50 cm」（縮小方向）為錯誤預期，已廢棄。

**3B 修補**：V3B-27 機制來源 `VSUP-B12` → `VSUP-B11`；靜水基線「55–65 cm」→「~100 cm」；信心等級「高」→「中-高」（120–160 cm 為瞬態估算，VSUP-B11 提供兩端邊界支撐）。

### 確認正確的核心數值

- VSUP-B05 Schreckstoff 死區半徑：Zone-A 3.35 m（35.26 m²）；Zone-B 3.90 m（47.78 m²）；Zone-C 4.91 m（75.74 m²）
- VSUP-B06 C&R 等待：北部 10–15 min / 4–5 m；南部 30–45 min / 6–8 m（野生水庫 ≥8 m）
- VSUP-B09 Fe²⁺ 安全距離：Zone-B 春末 25.7 cm（鰓損傷）/ 32.7 cm（避忌）；Zone-A 盛夏 56.5 cm / 67.2 cm（均為上修，V1B-CF-04 舊估 10–20 cm）
- VSUP-B11 H₂S 安全距離 Stagnant h=100 cm：致死 91.3–99.4 cm；避忌 99.7–100.0 cm（確認 V1B-10 上界）
- VSUP-B11 H₂S 安全距離 Stagnant h=150 cm：致死 125.2 cm；避忌 149.0 cm
- VSUP-B11 Mixed 狀態（水車開啟）：低端避忌 186.8 cm；高端全池超標（翻水危險）
- VSUP-B13 亞致死 H₂S 皮質醇增幅：15–35 ng/mL（達 21–45 ng/mL 中度應激，信心等級：中-低）

---

## SUP-C 卷稽核與後處理（2026-06-04）

**目標檔案**：`SUP-C_黑鱸毒區迴避實證與冒險覓食決策機制.md`（新建）
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：VSUP-C01–12（12 條）　**Carry_Forward 數**：4 項（低氧迴避閾值、冒險覓食觸發條件、靜止容忍特徵、皮質醇抑制閾值）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | Q1.3 迴避行為確定性（個體差異比例）結構性缺口；Q4.3 決策矩陣缺「靜止容忍」第三行為結果；Inherited Baseline 皮質醇基線值衝突（1.68 vs ~6.0 ng/mL） | 送 Gemini 修正 prompt |
| Round 2 | ✅ Go | 三項結構性缺口全數修復；皮質醇基線統一為 ~6.0 ng/mL；三行為結果矩陣明確列出 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 2 件 | B0-11 content mismatch（DO 動態 vs H₂S 釋放速率歸屬）；VSUP-B06 V-code 漂移（86 cm 舊版 → VSUP-B09/B11 精算值） |
| P2 輸出區塊 | ⚠️ 1 件 | 缺 4A 報告 [確認] CI（instruction 列出 1B/3A/4A/SUP-B 為目標） |
| P3 引用鏈 | ⚠️ 3 件 | B0-11/VSUP-B10 歸屬差異；VSUP-A04 vs VSUP-A09 V-code 漂移；VSUP-B06 指向內容與 instruction 預期不符 |
| P4 Scope | ✅ OK（1 Scope Note）| VSUP-B05 Schreckstoff 引用為背景引用，非越界 |
| P5 研究缺口 | ✅ OK | 3 條 Unresolved_Dependencies 均正確標注 |

**Phase 6 判定**：⚠️ 局部補充（6 分，Q 覆蓋完整型）。所有缺口為 V-code 版本漂移標注與一個 CI 補充，Claude 後處理即可。

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-SUPC-01 | Inherited_Baseline 第 1 條 H₂S 釋放速率 | 歸屬說明修正：`(SUP-B 報告 VSUP-B10)` → `（0D 報告原引用編號 B0-11；精算後由 SUP-B 報告 VSUP-B10 更新覆蓋）` |
| FIX-SUPC-02 | Inherited_Baseline 第 4 條 ART 溫度矩陣 | V-code 漂移說明：`(SUP-A 報告 VSUP-A09)` → `（SUP-A 報告 VSUP-A09；對應 instruction 預期編號 VSUP-A04，V-code 重新編號後更新為 VSUP-A09）` |
| FIX-SUPC-03 | Inherited_Baseline 第 3 條開頭 | 新增 VSUP-B06 V-code 版本漂移說明：86 cm 舊版已被 VSUP-B09/B11（靜水 99.7–100.0 cm；開機 186.8–348.4 cm）覆蓋，標注「[覆蓋 fallback 假設]」 |
| FIX-SUPC-04 | Correction_Instructions 末尾 | 新增 4A 報告 V4A-10 [確認] CI：H₂S 96-h LC50 = 0.0297–0.0316 mg/L 與行為迴避閾值 0.002 mg/L 獲 VSUP-C03/C08 驗證確認 |

### 不受影響的確認正確數值

- VSUP-C01：Chowan River 遙測 n=45，91.1% 個體在 DO < 1.8 mg/L 時 2.5–6.0 hr 內逃逸；速度 45–110 m/hr
- VSUP-C02：逃逸群體 75–85%（<5 min 立即型）vs 滯留群體 15–25%（延遲/靜止容忍型，LVF 老魚為主）
- VSUP-C03：成魚 DO 迴避 2.2–2.5 mg/L；小魚 1.5–1.8 mg/L；H₂S 迴避閾值 0.002 mg/L（體型間無差異）
- VSUP-C04：衝入時間窗口 15–25 s（上限 30 s）；爆發速度 1.5–2.2 m/s
- VSUP-C05：獵物密度觸發倍率 ≥3.5×；OFT 淨能量獲取 1.0–2.3 kJ（代謝代價 0.2–0.5 kJ）
- VSUP-C06：H₂S = 0.005 mg/L 單次吸收 0.015–0.025 µg/kg（LC50 之 0.05–0.08%）；0.01 mg/L 為 0.030–0.051 µg/kg（0.10–0.17%）
- VSUP-C07：COX 抑制 5–15%；重置冷卻期 45–60 min；安全衝入上限 H₂S < 0.01 mg/L → 10–15 次/day；≥ 0.05 mg/L → 0–1 次/day
- VSUP-C08：M. salmoides LC50（0.0306 mg/L）vs P. mexicana（>10–15 mg/L）差距 300 倍以上；SQR 活性差 98%+
- VSUP-C09：CAWS Pcrit 21.1–26.7%（≈1.8–2.2 mg/L at 20°C），與對照水域無統計差異，確認黑鱸依賴行為避難而非生理適應
- VSUP-C10：皮質醇 >150 ng/mL → 冒險覓食 100% 阻斷；LVF 基線 20–40 ng/mL → 觸發門檻升至 ≥6.0×；飢餓 3–5 天 → 門檻降至 2.0–2.5×
- VSUP-C11：靜止容忍群體游泳活性降 50–80%；H₂S 鰓吸收降 40–60%；主動索餌率 0%
- VSUP-C12：3D 決策矩陣完整（迴避/靜止容忍/冒險覓食 × 三 H₂S 區間 × 兩體型）
