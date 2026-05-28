---
name: gemini-plan-review
description: 審查 Gemini Deep Research 產出的研究計畫（plan），對照使用者提供的 prompt 檔案（.md），給出五類條列式建議：(1) prompt 涵蓋度 (2) plan 調整建議 (3) 是否需要拆分 prompt (4) 執行就緒信號 Go/Hold/Rework (5) 執行偏移風險。當使用者上傳或貼上一份研究計畫、研究大綱、Gemini plan，同時提及有 prompt 檔案要對照時，務必觸發此 skill。也適用於使用者說「幫我看這份 plan」、「這份計畫有沒有跑偏」、「prompt 是不是太大了」、「可以開工了嗎」、「還要繼續改嗎」等情境。
---

# Gemini Plan Review Skill

審查 Gemini Deep Research 產出的 plan，對照使用者的 prompt 檔案，輸出結構化的條列建議。

## 輸入

- **Prompt 檔案**：使用者提供的 `.md` 檔案，代表這次 Deep Research 的研究意圖與需求範圍
- **Gemini Plan**：使用者直接複製貼上的純文字 plan（Gemini Deep Research 在執行前產出的研究計畫）

## 工作流程

### Step 0：確認 prompt 來源

若使用者只提供 plan 而未指定 prompt 檔案，依序執行：

1. **查看本次對話中最近讀取過的 prompt 檔案**：若對話中已有讀取過的 `*-instruction.md` 內容，直接以該檔案作為對照基準，並告知使用者「將以 [檔名] 作為對照基準，如有不同請告知」，然後繼續分析。
2. **若對話中找不到已讀取的 prompt 內容**：主動要求使用者提供 prompt 檔案路徑或內容，再開始分析。

### Step 1：讀取 prompt 檔案

使用 `view` 或 `bash_tool` 讀取 prompt `.md` 檔案內容，萃取以下要素：
- 核心研究問題（main question）
- 子主題 / 子問題清單
- 指定的輸出範圍、格式、限制條件
- 任何明確排除的內容（exclusion list）

### Step 2：解析 Gemini Plan

將 plan 拆解為：
- 研究章節 / 階段列表
- 每個章節的目標與預計涵蓋的面向
- 每個章節的陳述範圍（stated scope）與隱含擴展方向
- plan 隱含的研究邊界（scope）

### Step 3：五維度分析

#### 維度 A — 涵蓋度（Coverage）
逐一比對 prompt 的每個要求，判斷 plan 中是否有對應章節或段落。

對每個 ⚠️ 項目，額外標注缺口類型：
- **[結構性缺口]**：Plan 完全沒有指向這個方向，Gemini 不會自己找到——**必須修正**
- **[可浮現缺口]**：研究方向已存在，Gemini 執行研究時自然會命中——**可以接受**

標記方式：
- 完全涵蓋 ✅
- 部分涵蓋 ⚠️[結構性] 或 ⚠️[可浮現]
- 未涵蓋 ❌

#### 維度 B — Gemini 修正 Prompt（Correction Prompt）

分析 Gemini plan 中需要修正的問題（結構性缺口、冗餘方向、越界章節、缺失章節），將所有修正需求整合成**一段可直接貼給 Gemini 的修正 prompt**。

分析面向：
- 哪些 instruction.md 要求的研究方向在 plan 中完全缺失（對應 Dimension A 的結構性缺口）
- 是否有重複或冗餘的研究方向
- 是否有偏離 instruction.md 意圖的章節（plan 有但 prompt 沒要求，且明顯超出範圍）

**輸出原則**：不固定格式，見招拆招。清楚以編號條列「第幾點要如何調整、針對 Gemini plan 的哪個章節、具體要補充或移除什麼」即可。語氣直接對 Gemini 說，讓使用者能複製後直接貼上。

**格式問題不納入 Gemini 修正 Prompt**：以下問題 Gemini 遵循率不穩定，強制要求容易卡住或輸出散文，一律不寫進修正指令，改在本維度末尾輸出「Claude 後處理備忘」提醒使用者：
- Findings 編號格式（VSUP-DXX、V-code 編號）
- 信心等級逐條標注
- 輸出區塊標題結構（Inherited_Baseline / Correction_Instructions / Carry_Forward / Unresolved_Dependencies）
- 移除內文數字引用標記 [1][2][3]
- Zone-A / Zone-B / Zone-C 三區分離排版
- 連續編號硬上限（如「VSUP-D19 to VSUP-D24」）

若 plan 或研究任務中有上述格式問題，在維度 B 末尾額外輸出：
```
📋 Claude 後處理備忘（Gemini 執行完畢後交由 Claude 處理）
- [列出需要 Claude 後處理的格式項目]
```

若 Dimension A 無結構性缺口且無越界問題，輸出：
`✅ 本輪無需修正，Gemini plan 可直接執行。`

#### 維度 C — 拆分判斷（Split Assessment）
判斷 plan 執行下去是否會讓研究失焦，需要將 prompt 拆分為更聚焦的子任務。

**判斷基準：以 prompt 為錨點，看 plan 有沒有跑出去**

拆分的核心問題是：「這份 plan 執行完，會不會有大量內容是我 prompt 沒要的？」

**建議拆分的情況：**
- Plan 新增了 prompt 完全沒提到的研究方向，且這些方向佔了相當篇幅（不只是背景補充）
- Plan 對某個子主題的展開深度，明顯超過其在 prompt 中的份量（prompt 只是帶到，plan 卻當主軸在做）
- Plan 把 prompt 中原本有關聯的子問題，拆解成彼此獨立、各自發展的研究線，導致整體失去連結

**不需要拆分的情況：**
- Prompt 本身有多個子問題，但 plan 都在 prompt 劃定的範圍內展開——這是正常的研究設計
- Plan 有少量背景補充或脈絡說明，但核心方向仍對齊 prompt

如果建議拆分，指出：
- 哪些範圍應該獨立成一份新 prompt（用章節名稱或主題指出即可，不需重新撰寫 prompt）
- 拆分的建議切割點

#### 維度 D — 執行就緒信號（Go / Hold / Rework）

**判斷原則：以「結構性缺口」為核心標準，不因「可浮現缺口」阻擋執行**

| 信號 | 觸發條件 |
|------|---------|
| ✅ **Go — 可以執行** | 無 ❌ 項目；所有 ⚠️ 均屬「可浮現缺口」；排除條件未被 plan 觸及 |
| ⚠️ **Hold — 建議補一輪** | 存在 ⚠️[結構性缺口]；或 Dimension E 發現高風險章節範圍過寬 |
| ❌ **Rework — 需要重寫** | 存在任何 ❌ 項目；或 plan 明確觸碰 prompt 的排除條件 |

輸出格式：
```
## 🚦 執行就緒信號

**[✅ Go / ⚠️ Hold / ❌ Rework]**

理由：[一句話說明判斷依據]

（若 Hold）需修正後才可執行：
- [結構性缺口]：[具體建議修法]
```

#### 維度 E — 執行偏移風險（Pre-flight Drift Check）

**前提認知**：Gemini Deep Research 拿到使用者的研究簡報後，會自行重組產出一份 plan。本維度審查的是 **Gemini 產出的 plan**，不是使用者原始的簡報措辭。Gemini 執行時會依照自己的 plan 章節展開研究，因此風險在於「Gemini 的 plan 章節範圍是否會把它引導到 prompt 排除的領域」。

依序執行以下三類檢查，全部針對 Gemini 生成的 plan 文字：

**檢查 1 — 章節範圍過寬（Section Scope Sprawl）**
審查 Gemini 的每個 plan 章節，判斷其陳述的研究範圍執行下去是否會自然拉入排除的領域：
- 章節標題或描述宣稱要涵蓋的範圍，是否已超出 prompt 劃定的邊界？
- 執行此章節時，Gemini 搜尋的資料方向是否必然觸及排除條件所指的鄰近主題？
- 常見例：chapter 標題為「台灣黑鱸覓食生態與環境」→ 執行時必然拉入屬平行卷的物種族群調查；chapter 描述「分析感官整合機制及其生態背景」→ 「生態背景」會觸發物種棲地研究
- 標注「⚠️ 範圍過寬風險」，指出會往哪個排除方向擴展，建議在下輪 prompt 中對此章節加限縮語

**檢查 2 — 禁忌詞出現（Forbidden Keywords）**
將 prompt 的排除條件（exclusion list）中的關鍵詞，逐一比對 Gemini plan 的章節標題與描述：
- 若排除條件的關鍵詞（主題名稱、機制名稱、物種/卷名）直接出現在 Gemini plan 的措辭中 → 標出具體章節與文字，標注「⚠️ Scope 越界風險」
- 常見例：Gemini plan 寫「OFT 能量最優化模型推導」但 prompt 已排除 OFT 推導；plan 寫「台灣水體獵物物種清單」但該主題屬 SUP-E 平行卷

**檢查 3 — 模糊觸發詞（Ambiguous Expansion Triggers）**
識別 Gemini plan 中措辭開放、執行時容易讓 Gemini 無邊界展開的短語：
- 觸發模式：「探討 X 的各種面向」「分析 Y 在台灣的情況」「調查 Z 相關研究」（無具體限定語，且 X/Y/Z 鄰近排除領域）
- 這類措辭不含禁忌詞本身，但執行時 Gemini 的資料搜尋方向會自然滑向排除的鄰近主題
- 標注「⚠️ 觸發擴展風險」，建議在下輪確認 plan 時要求 Gemini 補充限縮語，或在使用者的研究簡報中加更明確的邊界說明

輸出格式：
```
## ⚡ 執行偏移風險

### 章節範圍過寬
[內容或「✅ 無」]

### Scope 越界風險
[內容或「✅ 無」]

### 觸發擴展風險
[內容或「✅ 無」]
```

### Step 4：輸出格式

五個 Dimension 依序輸出：

```
## 📋 Prompt 涵蓋度

- ✅ [prompt 要求項目] → 對應 plan 章節：[章節名]
- ⚠️[可浮現] [prompt 要求項目] → plan 中 [章節名] 有提及但不完整，研究過程中可自然命中
- ⚠️[結構性] [prompt 要求項目] → plan 中 [章節名] 無此研究方向，Gemini 不會自己找到
- ❌ [prompt 要求項目] → Plan 中未見對應章節

---

## 🔧 Gemini 修正 Prompt

[可直接貼給 Gemini 的修正指令，以編號條列，針對其 plan 的具體章節說明要補充或移除什麼]

（若無需修正）✅ 本輪無需修正，Gemini plan 可直接執行。

---

## ⚖️ 拆分評估

**結論：建議拆分 / 不需拆分**

（若建議拆分）
- 建議將以下範圍獨立為新的 prompt：
  - [範圍 A]：涵蓋 [章節 X、章節 Y]
  - [範圍 B]：涵蓋 [章節 Z]
- 建議切割點：[說明拆分邏輯]

（若不需拆分）
- 理由：[簡短說明為何目前 prompt 範圍仍屬聚焦]

---

## 🚦 執行就緒信號

**[✅ Go / ⚠️ Hold / ❌ Rework]**

理由：[一句話說明判斷依據]

（若 Hold）需修正後才可執行：
- [結構性缺口]：[具體建議修法]

---

## ⚡ 執行偏移風險

### 章節範圍過寬
[內容或「✅ 無」]

### Scope 越界風險
[內容或「✅ 無」]

### 觸發擴展風險
[內容或「✅ 無」]
```

## 注意事項

- 涵蓋度分析以 **prompt 為基準**，不是以 plan 為基準——要問的是「prompt 說的有沒有被 plan 照顧到」，而不是「plan 做了哪些事」
- Gemini 修正 Prompt（Dimension B）輸出的是可直接貼給 Gemini 的指令，不是給使用者自己看的建議；必須具體指向 Gemini plan 的章節名稱，說明補充或移除什麼，讓 Gemini 能直接執行
- 拆分判斷要果斷：寧可多建議拆分，也不要讓使用者跑完 3 輪之後才發現失焦
- **執行就緒信號（Dimension D）是最重要的輸出**——使用者通常無法自行判斷何時該停止迭代，信號必須明確，不可模糊表達
- ⚠️[結構性] 缺口是阻擋執行的唯一理由；⚠️[可浮現] 缺口不應阻擋執行
- **Skill 的核心工作流程**：使用者把 instruction.md 文字貼給 Gemini → Gemini 生成 plan → 使用者把 plan 給我們 review → 找到缺口後給使用者一段 prompt 讓他貼回 Gemini 修正 → Gemini 重新調整 plan → 再 review。若多輪後 Gemini 涵蓋率不升反降，才評估拆分新的 instruction.md
- 執行偏移風險（Dimension E）審查的是 Gemini 生成的 plan 章節，判斷執行時是否會自然滑向 instruction.md 的排除領域
- 若使用者只提供 plan 未指定 prompt：**優先查看本次對話中最近讀取過的 `*-instruction.md`**，找到後告知使用者並繼續；找不到才主動要求使用者提供
