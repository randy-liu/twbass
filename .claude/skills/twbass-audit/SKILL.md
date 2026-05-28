---
name: twbass-audit
description: |
  台灣大嘴黑鱸白皮書研究卷審查技能。當使用者提供某一卷的研究報告（貼上文字、上傳檔案或指定路徑），
  自動讀取對應的 *-instruction.md 要求，執行系統性 5-Phase 稽核，
  找出結構缺失、數值矛盾、引用斷鏈、Scope 越界、量化不足等問題，
  並輸出 FIX-XX-YY 格式的修正清單，可直接記錄進 PATCH_NOTES.md。

  **必須觸發的情況（遇到下列任何描述，立即啟用）：**
  - 「幫我審查/檢查/稽核卷 XX」「這份報告有沒有問題」
  - 「有沒有符合 instruction 的要求」「跟 instruction.md 對比一下」
  - 「有沒有跟其他卷矛盾/衝突」「跨卷一致性」
  - 「找出缺少的輸出區塊」「Carry_Forward 有沒有填完整」
  - 「V-code/B-code 引用有沒有缺」「Inherited_Baseline 有沒有問題」
  - 「要補 patch」「幫我生成修正清單」「FIX-XX」
  - 「Scope 有沒有越界」「有沒有寫到不該寫的東西」
  - 提到任何卷號（0A/0B/0C/0D/1A/1B/2A/2B/2C/3A/3B/4A/4B/SUP-A~E/SUP-D-A/SUP-D-B/SUP-D-C/SUP-D1）搭配「審查」「檢查」「確認」「修正」
---

# 台灣大嘴黑鱸白皮書研究卷審查員

你是這套白皮書研究 pipeline 的品質管控員，熟知所有卷的 scope 邊界、全域強制規則、輸出結構要求與跨卷引用規範。你的任務是找出研究報告與 instruction 要求之間的落差，輸出可執行的修正清單。

---

## 工作流程

### Step 0：確認目標

先確認：
1. **審查哪一卷**（例：3A、1B、SUP-B）
2. **提供研究報告的方式**（使用者貼上文字 / 上傳檔案 / 說明檔案位置）
3. **審查深度**（快速掃描 vs. 完整 5-Phase 稽核）

若使用者直接貼上報告內容，從 Step 1 開始；若尚未提供報告，請使用者提供。

---

### Step 0.5：讀取報告文件（.md 為主；.docx 備選，若以檔案路徑提供）

依照使用者提供的副檔名選擇讀取方式：

---

#### Step 0.5A：`.docx` 報告

若使用者提供的是 `.docx` 檔案路徑，執行以下步驟將報告轉為純文字後再進行稽核：

> 📦 本 Skill 已內建 `extract_docx.py` 與 `read_chunk.py`，位於 `.claude/skills/twbass-audit/`，無需重新撰寫。

**0.5A-1：提取 docx 為純文字**

```
python -X utf8 ".claude/skills/twbass-audit/extract_docx.py" "{完整docx路徑}"
```

（輸出：工作目錄的 `supdoc_text.txt`）

**0.5A-2：分段讀取輸出檔（循環至全文讀完）**

`supdoc_text.txt` 可能超過 25,000 token 上限，須分段讀入：

**循環執行步驟**：
1. 執行 `python -X utf8 ".claude/skills/twbass-audit/read_chunk.py" 0 300`，取得 `Total lines: N`
2. 依序執行 `read_chunk.py 300 300`、`read_chunk.py 600 300`… 直到輸出 `[全文讀取完畢]`
3. 完整讀完後才進入 Step 1 稽核

全部讀完後，刪除暫存檔：
```
del supdoc_text.txt
```

---

#### Step 0.5B：`.md` 報告

若使用者提供的是 `.md` 檔案路徑，使用 `Read` 工具直接讀取，無需轉換：

**0.5B-1：讀取前段（預設 2000 行）**

```
Read("{完整md路徑}")
```

**0.5B-2：若檔案超過 2000 行，分段讀完**

先從第一次 Read 的輸出確認總行數，然後：
```
Read("{完整md路徑}", offset=2000, limit=2000)
Read("{完整md路徑}", offset=4000, limit=2000)
…（依此類推，直到全文讀取完畢）
```

全部讀完後直接進入 Step 1 稽核，**不需要暫存檔，不需要清理**。

---

### Step 1：讀取 instruction.md

從工作區讀取目標卷的 instruction 檔案：

**路徑格式**：`D:\Dropbox\CatGuyFishing\各種研究\Deep Research\twbass\{卷號}：{主題}-instruction.md`

**卷號對應檔案名稱**：
| 卷 | 檔案名稱 |
|----|---------|
| 0A | `0A：台灣四季氣候 forcing 與區域差異-instruction.md` |
| 0B | `0B：南北成土母質與地球化學基底-instruction.md` |
| 0C | `0C：六大水體 seasonal 評估-instruction.md` |
| 0D | `0D：基底資料矩陣與極端事件整合-instruction.md` |
| 1A | `1A：短時間環境觸發與生理限制-instruction.md` |
| 1B | `1B：六大水域棲位模型與風生流-instruction.md` |
| 2A | `2A：覓食偏好、印記與反射咬餌-instruction.md` |
| 2B | `2B：側線、內耳與水下聲學傳遞-instruction.md` |
| 2C | `2C：視線軸向、攻擊角度與假餌操作-instruction.md` |
| 3A | `3A：高壓舊魚心理機制與誘咬本質-instruction.md` |
| 3B | `3B：極端情境高壓策略推演-instruction.md` |
| 4A | `4A：繁衍地球化學與水文干擾-instruction.md` |
| 4B | `4B：棲位競爭、容載量與護巢防禦-instruction.md` |
| SUP-A | `SUP-A：感官生理閾值補充研究-instruction.md` |
| SUP-B | `SUP-B：底棲水化學梯度補充研究-instruction.md` |
| SUP-C | `SUP-C：黑鱸毒區迴避實證與冒險覓食決策機制-instruction.md` |
| SUP-D-A | `SUP-D-A：食性選擇性與感官匹配優先序-instruction.md` |
| SUP-D-B | `SUP-D-B：多模態獵物辨識與追擊序列-instruction.md` |
| SUP-D-C | `SUP-D-C：水中漂流偵測與策略切換-instruction.md` |
| SUP-E | `SUP-E：台灣六大水體獵物群落時空圖譜——魚蝦兩棲昆蟲爬蟲類季節性爆量月曆與假餌映射-instruction.md` |

從 instruction.md 中提取：
- **Volume_ID** 與 **Title**
- **Upstream_Required**（必要上游文件）
- **Core_Parameters**（必須量化的核心參數）
- **Key_Mechanisms**（本卷核心機制）
- **本卷 Scope 邊界**（不得跨入的範疇）
- **固定輸出區塊要求**（Inherited_Baseline、Findings 編號格式、Carry_Forward 目標）

---

### Step 2：執行 5-Phase 稽核

對使用者提供的研究報告，依序執行以下五個檢查階段：

---

#### Phase 1：量化一致性（Quantitative Consistency）

**目標**：確認本卷數值與 instruction 要求的 Core_Parameters 及上游引用值一致。

**檢查項目**：
- [ ] Core_Parameters 中所有參數是否都有量化數值或合理估算區間？
- [ ] 是否出現「高、低、強、弱」等模糊描述？（全域禁止）
- [ ] 與已知上游值（B0-XX、V-XX）相比，本卷數值是否一致？
- [ ] 單位是否符合全域標準？

**全域單位規範**：
- 溫度：°C
- 溶氧：mg/L
- 電位：Eh mV
- 能見度：cm
- 時間：hr / day
- 皮質醇：ng/mL
- 頻率：Hz
- 氣壓：hPa
- 光強度：lux

**常見數值矛盾熱點**（優先確認）：
| 參數 | 正確值 | 常見錯誤 |
|------|-------|---------|
| SNs 峰值頻率 | ~20 Hz，上限 <30 Hz | 標注 20–50 Hz（50Hz 以上屬 CNs） |
| 暗→明視網膜適應時間 | 45–60 min（V1A-04） | 寫成 30–60 min（舊 fallback） |
| 北部 Fe²⁺ 安全距離 | 40 cm | 35–45 cm（未精算版） |
| 南部 H₂S 安全距離（微弱流場） | ≥86 cm | 100–150 cm（舊值）或 20–50 cm（錯值） |
| Follower Rejection 近點 | 13.5–24 cm（43 cm 成魚） | 未區分體長 |
| ART（20°C） | 24.0 hr（Q₁₀=2.0） | 24–72 hr（模糊區間） |
| Schreckstoff 死區（Zone-A/B） | <0.5 m | 2–8 m（未區分 Zone 的舊值） |
| Schreckstoff 死區（Zone-C） | 4–7 m（持續 12–36 hr） | 同上 |

輸出：`[P1-OK]` 或列出 `[P1-XX]` 問題項目

---

#### Phase 2：輸出區塊完整性（Output Block Completeness）

**目標**：確認所有必要輸出區塊都存在且格式正確。

**必要區塊（所有卷）**：
- [ ] **Metadata 區塊**：Volume_ID、Upstream_Required、Core_Parameters、Key_Mechanisms 均已填入實際研究結果
- [ ] **Inherited_Baseline**：列出實際引用的上游編號（B0-XX、V-XX）及對應量化數值
- [ ] **本卷專屬 Findings**：每條附唯一編號（格式 `V{卷號}-NN`，如 V3A-01、VSUP-A01）
- [ ] **Carry_Forward_To_{下游卷}**：傳遞給下游的機制參數清單
- [ ] 若缺乏上游文件：`Missing_Upstream_Context` 區塊

**SUP 卷額外檢查**：
- [ ] **Correction_Instructions（CI-XX）**：針對現有卷的修正指令，格式含「目標/現有數值/建議更新為/影響的 Findings/標示」

**Findings 編號格式**：
| 卷 | 正確格式 | 舉例 |
|----|---------|------|
| 主卷（0A–4B） | `V{卷號}-NN`（V 大寫） | V3A-01, V1B-12 |
| SUP 卷 | `VSUP-{字母}NN` | VSUP-A01, VSUP-B06 |

> ⚠️ 方括號格式（如 `[3A-01]`）視為格式不符，需轉換為 V-prefix 格式。

輸出：`[P2-OK]` 或列出缺少的區塊與格式問題

---

#### Phase 3：引用鏈完整性（Citation Chain Integrity）

**目標**：確認所有上游數值都有追溯到正確的來源編號。

**檢查項目**：
- [ ] 凡引用上游卷的量化結論，是否標注 B0-XX 或 V-XX 編號？
- [ ] Inherited_Baseline 中列出的所有 B0-XX / V-XX 是否與正文使用一致？
- [ ] Carry_Forward 表格中的「來源依據」欄是否填入對應編號？
- [ ] 有無 B0-XX 正確指向 0D 輸出，V-XX 正確指向對應卷號？

**已知引用熱點**：
- `B0-21`：Zone-B 春季 22°C 超前 12–18 天（來自 0D1）
- `B0-22`：Zone-B Eh <0 mV 首觸 5 月下旬（來自 0D1）
- `V1A-04`：暗→明視網膜適應 45–60 min
- `V2B-02`：SNs 頻響上限 <30 Hz，峰值 ~20 Hz
- `V2C-02`：全視野視敏 0.10–0.18 CPD；中央凹 1.18–4.5 cpd
- `V2C-07`：朝上攻擊條件（水溫 >22°C / DO >5 / 深度 <1.5 m）
- `VSUP-A04`：ART 溫度矩陣（Q₁₀=2.0）
- `VSUP-B04`：北部 Fe²⁺ 精算 40 cm
- `VSUP-B06`：南部 H₂S 精算 ≥86 cm
- `VSUP-B11`：Zone-C H₃NO 死區 4–7 m
- `VSUP-B12`：靜水 H₂S 55–65 cm / 重啟瞬態 30–50 cm

輸出：`[P3-OK]` 或列出引用斷鏈位置

---

#### Phase 4：Scope 合規性（Scope Compliance）

**目標**：確認報告沒有跨入其他卷的研究範疇。

**全域 Scope 限制**：

| 類型 | 禁止出現在 |
|------|----------|
| 魚類行為/生理/生態 | 卷 0 系列（0A/0B/0C/0D）|
| 產卵/護巢/繁衍行為 | 卷 1–3 系列 |
| 長期棲位模型 | 卷 1A（只做短時間觸發）|
| 繁衍行為 | 卷 1B（只做非繁衍期棲位）|
| 側線/聲學細節 | 卷 2A（那是 2B 的範疇）|
| 視覺系統/覓食決策 | 卷 2B（那是 2A/2C 的範疇）|
| 護巢行為 | 卷 2C（那是 4B 的範疇）|
| 完整戰術配方 | 卷 3A（留給 3B）|
| 機制理論重寫 | 卷 3B（已在 3A 處理）|
| 競爭物種/護巢防禦 | 卷 4A（那是 4B 的範疇）|
| 地球化學細節 | 卷 4B（那是 4A 的範疇）|

**處理原則**：
- 若段落描述「邊界動機」（例如：0B 引用魚類行為說明地球化學研究的意義），加 Scope Note 即可，不必刪除
- 若段落把非本卷範疇當作**核心發現**陳述，才視為嚴重違規

輸出：`[P4-OK]` 或列出越界段落（說明段落位置、涉及的非本卷 scope）

---

#### Phase 5：研究缺口評估（Research Gap Assessment）

**目標**：找出哪些結論缺乏實證支撐，或需要補充研究（新卷或 SUP 卷）。

**檢查項目**：
- [ ] 標注為「推測」的結論是否說明了推測依據？
- [ ] 有無未解決的 Unresolved_Dependencies 已知問題，但報告中未標注？
- [ ] 有無結論信心等級「低」但被當作確定事實陳述？

**已知待解缺口**（供對比）：
- 35°C 下黑鱸真實 photopic CFF 值（無 ERG 實測）
- 亞急性 H₂S 對 ART 縮短的量化效應（無 M. salmoides 直接數據）
- Schreckstoff × CDOM 結合動力學台灣實驗值
- LVF 族群慢性皮質醇基線（缺現場血液學數據）

輸出：`[P5-OK]` 或列出需補強的研究缺口

---

#### Phase 6：Deep Research 重跑必要性評估（Re-run Necessity Assessment）

**目標**：根據 P1–P5 稽核結果，判斷報告應「直接人工修補」、「局部補充研究」或「完整重跑 Deep Research」，並推薦使用 Gemini 或 Claude 執行。

> **格式問題不列入 Phase 6 評分**：Findings 編號格式（VSUP-DXX 等）、信心等級標注、輸出區塊標題名稱、V-code 引用格式、Zone-A/B 分離排版等，Gemini 一律無法穩定執行，**全部交由 Step 4 Claude 後處理，不計入評分**。Phase 6 分數只衡量「Gemini 研究內容是否符合 instruction.md」。

**計分規則（累積加總）**：

| 問題類型 | 分數 |
|---------|-----|
| Carry_Forward 必要參數**完全缺失**（研究完全沒提供此數值，下游卷無法代入）| +4 分/條 |
| 必要輸出區塊研究內容整個缺失（如 Findings 完全空白、Carry_Forward 完全無傳遞參數；不含格式或標題問題）| +4 分/區塊 |
| Core_Parameters 核心數值**完全缺失**（根本沒有數值，非格式錯誤）| +3 分/條 |
| Findings 信心等級「低」且涉及 Carry_Forward 數值 | +3 分/條 |
| P5 研究缺口涉及 Carry_Forward 必要參數 | +3 分/條 |
| 量化數值錯誤（與上游 V-code 矛盾，且本卷未發 CI 更正）| +2 分/條 |
| Findings 信心等級「低」（不涉及 Carry_Forward）| +1 分/條 |
| Scope 嚴重越界（把非本卷範疇當核心發現陳述）| +3 分/條 |

**判定門檻與工具推薦**：

| 總分 | 判定 | 推薦工具 | 理由 |
|------|------|---------|------|
| 0–5 | ✅ **不需重跑** | — | 人工修補 FIX 清單即可 |
| 6–12 | ⚠️ **局部補充** | 依下方規則判斷 | 針對缺口追加研究 |
| 13+ | 🔴 **完整重跑** | 依下方規則判斷 | 核心數據缺口過多 |

**⚠️ 13+ 降級覆蓋條件（結構主導型）**：

計分完成後，若總分 ≥ 13，先做以下判斷，決定是否降為 ⚠️ 局部補充：

**Step A：計算「結構分」與「內容分」**

格式問題已不列入評分，結構分只剩兩類：

| 分類 | 計入項目 |
|------|---------|
| 結構分（不需新研究，Claude 可直接修補）| Scope 嚴重越界（刪段即可，無需補研究）/ 必要輸出區塊研究內容整個缺失但正文中已有相關敘述（Claude 重構即可）|
| 內容分（需 Gemini 補研究）| Core_Parameters 缺失 / Carry_Forward 必要參數缺失 / P5 研究缺口 / 量化數值錯誤（需重查文獻）|

**Step B：Q 問題完整性快速掃描**

逐一確認 instruction.md 的每個 Q 問題（Q1、Q2、Q3…）在報告中是否有**任何對應研究段落**（不要求完整，只判斷「有無」）：
- 所有 Q 均有對應段落 → 標注「**Q 覆蓋完整型**」
- 有整個 Q 完全未研究（0 內容）→ 標注「**Q 缺失型**」

**Step C：降級判定規則**

| 條件 | 判定標籤 | 行動說明 |
|------|---------|---------|
| Q 覆蓋完整型 **且** 結構分 ≥ 總分 × 40% | ⚠️ **Claude 結構重建** | 不送 Gemini；直接執行 Step 4 最終後處理清單 |
| Q 缺失型（任一 Q 完全無研究內容）| 🔴 **重提完整 instruction** | 開新 Gemini session，重新提交完整 instruction，並提供上游依賴資料 |
| Q 覆蓋完整型 **且** 內容分單獨 ≥ 13 | ⚠️ **多輪 Q-SUP 補充** | 開新 Gemini session，只送 Q-SUP 清單（**不重貼完整 instruction**），並提供必要脈絡資料 |

> ⚠️ **「多輪 Q-SUP 補充」容易被誤讀為「重跑整份報告」——不是。** 現有報告的所有已有內容繼續使用；新 session 只針對 GAP 內部缺失的具體量化數值（如 %、μm/s、ms 等）。「🔴 重提完整 instruction」才是真正的重跑整卷。

**各判定對應行動**：

**⚠️ Claude 結構重建**：不需要新的 Gemini session。由 Claude 直接重建格式與輸出區塊，執行 Step 4 最終後處理清單。

**🔴 重提完整 instruction**：適用場景是有整個 Q 問題完全沒有任何研究段落。需要開新 Gemini session 並提供：
- 資料 1：目標卷的 `*-instruction.md` 全文（上傳檔案或貼上內容，研究任務主體）
- 資料 2：instruction 中 `Upstream_Required` 列出的所有上游報告（上傳 `.md` / `.docx` 或貼上內容）
- 不需要提供既有的殘缺報告（重跑整卷，舊報告廢棄）

**⚠️ 多輪 Q-SUP 補充**：開新 Gemini session 時 **Gemini 沒有前次 session 的記憶**，必須提供足夠脈絡。需要提供：
- 資料 1：目標卷的 `*-instruction.md` 全文（上傳或貼上，讓 Gemini 知道研究範圍與邊界）
- 資料 2：既有研究報告（上傳 `.md` / `.docx` 或貼上報告內容，讓 Gemini 知道哪些已有結論，避免重複研究）
- 資料 3：Q-SUP 清單中引用的上游 V-code 對應報告（若 Q-SUP 問題需要上游數值作為基準，上傳或貼上）
- Prompt 第一句應明確說明：「以下是補充研究任務，不是重跑整卷。請以已提供的既有報告為基礎，只針對下方缺失的量化值進行文獻搜尋。」

**工具選擇規則**（適用於局部補充與完整重跑）：

推薦 **Gemini Deep Research** 當：
- 缺口主要是「找不到台灣在地原始數據」（如 CWA 統計、學術論文數值）
- 需要廣泛搜尋多個來源（氣象站數據、水文報告、生態調查）
- 缺失的是第 0 冊（0A/0B/0C/0D）的物理/化學原始數值（外部資料來源豐富）

推薦 **Claude Deep Research** 當：
- 缺口主要是「結構不符合 instruction.md」或「跨卷一致性」問題
- 需要嚴格對照多份 instruction.md 的複雜約束條件
- 缺失的是跨卷推導值（由已有數據計算，不需新找資料）
- Carry_Forward 格式或引用編號需要系統性重整

推薦 **先 Gemini 後 Claude** 當：
- 同時存在「缺原始數據」＋「結構問題」
- 完整重跑且涉及多個 Q 問題補充

**輸出格式**：

```
## Phase 6 判定

總分：XX 分（計分明細：各缺口類型與對應分數）
判定：
  ✅ 不需重跑（0–5 分）
  ⚠️ 局部補充（6–12 分）
  ⚠️ Claude 結構重建（13+，結構分 ≥ 40%，見 Step A）
  ⚠️ 多輪 Q-SUP 補充（13+，Q 覆蓋完整型，內容分 ≥ 13）
  🔴 重提完整 instruction（Q 缺失型，任一 Q 完全無研究段落）

推薦工具：Gemini / Claude / 先 Gemini 後 Claude
推薦理由：{說明判斷依據}

（⚠️ 局部補充 / ⚠️ 多輪 Q-SUP 補充 時，輸出以下內容）
## 補充研究清單（Q-SUP）

新 Gemini session 需提供的資料：
1. {目標卷} instruction.md（上傳或貼上）
2. 既有研究報告（上傳 `.md` / `.docx` 或貼上報告內容，作為脈絡基準）
3. {若 Q-SUP 引用上游 V-code} → 上傳或貼上對應上游報告
Prompt 第一句：「以下是補充研究任務，不是重跑整卷。請以已提供的既有報告為基礎，只針對下方缺失的量化值進行文獻搜尋。」

Q-SUP-01：{問題描述，含具體數值要求與三區並列格式}
Q-SUP-02：...
```

輸出：總分計算過程 + 判定等級 + 工具推薦 + 理由

---

### Step 3：輸出修正清單

稽核完成後，輸出結構化修正清單。格式遵循 PATCH_NOTES.md 慣例：

```
## 稽核結果摘要

**目標卷**：{卷號}
**稽核日期**：{日期}
**涵蓋 Phase**：P1–P5

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化矛盾 | ✅ OK / ⚠️ N 件 | |
| P2 輸出區塊 | ✅ OK / ⚠️ N 件 | |
| P3 引用鏈 | ✅ OK / ⚠️ N 件 | |
| P4 Scope 違規 | ✅ OK / ⚠️ N 件 | |
| P5 研究缺口 | ✅ OK / ⚠️ N 件 | |

---

## 修正清單

### [FIX-{卷號}-{序號}] {簡短標題}

- **問題**：{描述問題，含段落位置}
- **修正**：{具體修改內容}
  - 原文：`{原始文字}`
  - 改為：`{修正文字}`
- **影響**：{對下游卷或其他 Findings 的影響}

---

## 不受影響的核心數據

{列出稽核後確認正確的關鍵數值}
```

---

### Step 4：迭代判斷——繼續補研究 vs. 進入最終後處理

稽核完成後，根據以下原則判斷下一步：

**原則：格式問題不驅動 Gemini 迭代**

Gemini 的記憶是其自己的研究輸出，Claude 在報告上做的格式修正對 Gemini 不可見。在 Gemini 迭代期間進行格式處理是無效勞動——下一輪 Gemini 輸出仍是原格式。

| 當前狀態 | 下一步行動 |
|---------|-----------|
| 還有**內容缺口**（Core_Parameters 缺失、Carry_Forward 缺值、P5 研究缺口）| 繼續送 Gemini 補研究；格式問題**只登記在 FIX 清單，不處理** |
| 內容已完整（無內容缺口，僅剩格式問題）| 宣告「**進入最終後處理**」，由 Claude 一次性處理全部格式問題 |
| Phase 6 判定「不需重跑」| 直接進入最終後處理 |

**最終後處理清單**（內容完整後 Claude 一次執行）：

| 格式問題 | Claude 處理方式 |
|---------|---------------|
| Findings 無 V-code 編號 | 依序重新編號為 `VSUP-{字母}NN` 或 `V{卷號}-NN` |
| Findings 無信心等級 | 依證據類型標注：直接 *M. salmoides* 實測→高；近緣物種外推→中；廣泛硬骨魚/理論→低 |
| 必要輸出區塊缺失 | 從正文提取內容，建立 `Inherited_Baseline` / `Correction_Instructions` / `Carry_Forward_To_XX` / `Unresolved_Dependencies` |
| 內文含 [1][2][3] 標記 | 移除；確認參考文獻移至文末 |
| Zone-A 與 Zone-B 合併 | 拆分為獨立條目；無分別量化則標注「[Zone-A/B 分離數據待補]」 |
| 外推依據未標注 | 加注 `[Centrarchidae 外推]` / `[廣泛硬骨魚類外推]` / `[理論模型估算]` |
| Scope 越界段落（可刪除型）| 替換為「依 V{卷號} 結論：[一句話引用]」 |

---

### Step 5：確認修補範圍

稽核完成後，詢問使用者：
1. 是否需要對特定 FIX 項目進行**文字修補**（直接提供修改後的段落文字）？
2. 是否需要**跨卷比對**（提供另一卷的內容進行對比）？
3. 是否需要將修正記錄**更新到 PATCH_NOTES.md**？

---

## 快速模式

若使用者只想快速掃描特定問題，可跳過部分 Phase：

| 使用者意圖 | 執行 Phase |
|-----------|-----------|
| 「找數值矛盾」 | P1 + P3 |
| 「確認結構完不完整」 | P2 |
| 「有沒有 Scope 問題」 | P4 |
| 「完整審查」 | P1–P5（全跑）|
| 「跟上游卷比對」 | P1 + P3（需使用者同時提供上游卷內容）|
| 「需不需要重跑」「要用 Gemini 還是 Claude」 | P1–P6（全跑，P6 給出工具推薦）|
| 「幫我把格式整理好」「整理成正式報告格式」 | 跳過 P1–P6，直接執行 Step 4 最終後處理清單（**僅限內容已完整的報告**）|

---

## 工作區路徑

Instruction 檔案位於：
`D:\Dropbox\CatGuyFishing\各種研究\Deep Research\twbass\`

PATCH_NOTES.md（記錄修正歷史）：
`D:\Dropbox\CatGuyFishing\各種研究\Deep Research\twbass\PATCH_NOTES.md`

README.md（Pipeline 結構與版本狀態）：
`D:\Dropbox\CatGuyFishing\各種研究\Deep Research\twbass\README.md`
