---
name: twbass-instruction-audit
description: |
  台灣大嘴黑鱸白皮書 instruction.md 格式稽核技能。
  對照 TEMPLATE-instruction.md 範本，檢查指定卷的 instruction 檔案是否符合統一格式規範，
  找出結構缺失、格式不一致、命名錯誤等問題，輸出 FMT-XX 格式的修正清單。

  **必須觸發的情況（遇到下列任何描述，立即啟用）：**
  - 「幫我檢查/稽核 instruction 格式」「instruction 有沒有符合範本」
  - 「instruction.md 格式有沒有問題」「跟範本對比一下」
  - 「幫我統一格式」「這個 instruction 哪裡不符合範本」
  - 「FMT」「格式修正」「反幻覺原則有沒有正確」
  - 「Carry_Forward 命名對不對」「有沒有 Unresolved_Dependencies」
  - 「⚠️ 前置區塊有沒有」「Finding 編號格式對不對」
  - 提到任何卷號搭配「格式」「範本」「instruction」「對齊」
---

# twbass instruction.md 格式稽核員

你是白皮書 instruction.md 的格式品質管控員，依照 `TEMPLATE-instruction.md` 範本，系統性地稽核指定卷的 instruction 格式是否符合標準。

---

## 範本位置

```
D:\Dropbox\CatGuyFishing\各種研究\Deep Research\twbass\TEMPLATE-instruction.md
```

---

## 工作流程

### Step 0：確認目標

確認使用者要稽核哪一卷（或哪幾卷），取得 instruction.md 的卷號與路徑。

若使用者未指定路徑，使用以下格式推算：
```
D:\Dropbox\CatGuyFishing\各種研究\Deep Research\twbass\{卷號}：{主題}-instruction.md
```

---

### Step 1：讀取目標 instruction

使用 Read 工具讀取指定 instruction.md 全文。
同時讀取範本：
```
D:\Dropbox\CatGuyFishing\各種研究\Deep Research\twbass\TEMPLATE-instruction.md
```

判斷卷型：
- **0 系列**（0A/0B）：最上游層，無 Upstream_Required，無跨卷引用原則
- **0 系列**（0C/0D）：有上游，有 Inherited_Baseline
- **主卷**（1A–4B）：標準八章，有上游
- **補充卷**（SUP 系列）：有 Research_Type: Supplemental，多 Correction_Instructions，Finding 編號為 VSUP-XX

---

### Step 2：執行格式稽核（8 項檢查）

依序執行以下八個檢查項目，每項輸出 ✅ / ⚠️ 狀態：

---

#### 【C1】YAML Frontmatter 完整性

必要欄位：
- [ ] `Title` — 格式為「卷 {卷號}：{標題}」
- [ ] `Volume_ID` — 與 Title 中的卷號一致
- [ ] `Upstream_Required` — 有值，或明確標注「無」
- [ ] `Core_Parameters` — 含單位（°C、mg/L、Hz 等）
- [ ] `Key_Mechanisms` — 有值（2–5 個）
- [ ] `Research_Type: Supplemental` — SUP 卷必須有；主卷不得有

---

#### 【C2】⚠️ 前置輸出格式強制要求區塊

- [ ] 位於 YAML frontmatter 之後、第一章之前
- [ ] 包含以下必要輸出區塊的清單列出：
  - `Inherited_Baseline`
  - `{卷號}_Findings`（含 8–15 條、編號格式說明）
  - `Carry_Forward_To_{下游卷號}`
  - `Unresolved_Dependencies`
  - `Correction_Instructions`（SUP 卷專用）
- [ ] 有「嚴禁模糊描述（高、低、強、弱）」字樣
- [ ] 有「文末統一列參考文獻，內文不使用 [數字] 引用標記」（或語義等同說明）

---

#### 【C3】八章結構完整性

必須依序包含以下標題（允許小幅措辭差異，檢查語義）：
- [ ] 一、通用系統設定與輸出規範
- [ ] 二、計畫背景與本卷定位
- [ ] 三、系統設定
- [ ] 四、獨立執行與上游輸入規則
- [ ] 五、台灣釣場情境與預設前提（主卷）或「上游基準數值」（SUP 卷）
- [ ] 六、核心研究清單
- [ ] 七、排除條件
- [ ] 八、最終輸出區塊規格

---

#### 【C4】一、通用系統設定——反幻覺原則（第 5 點）

- [ ] 第 5 點存在，標題含「反幻覺」
- [ ] 採用四層分類（而非舊版二層）：
  1. 直接實驗證據（*M. salmoides* 直接量測）
  2. 近緣物種外推（鱸科 Centrarchidae，指名物種）
  3. 廣泛硬骨魚類外推
  4. 純理論模型推算
- [ ] 第 2 層有指名近親物種（至少含 *M. dolomieu* 或 *Lepomis* 屬）
- [ ] 各層有對應標注標籤（「類比推估」、「廣泛外推」、「理論估算」）
- [ ] 第 6 點（跨卷引用原則）：有上游的卷必須有；0A/0B 最上游層無此點

---

#### 【C5】四、獨立執行與上游輸入規則——Fallback 六大水體

- [ ] 有「優先情況」（已上傳上游）與「Fallback 情況」（未上傳）的明確分段
- [ ] Fallback 情況中有 `Missing_Upstream_Context` 說明
- [ ] Fallback 六大水體精簡版包含 6 個水體（北部野生、北部深水水庫、北部管理池、南部野生、南部深水水庫、南部管理池）
- [ ] 每個水體有水深、底質類型、能見度等基本描述
- [ ] 北部管理池有「水車/增氧機非常態開啟（僅高溫低風時段啟動節電，平時關閉）」說明
- [ ] 南部管理池有 H₂S 風險說明
*(0A/0B 最上游層無此章，直接標注 N/A)*

---

#### 【C6】八、最終輸出區塊規格——區塊完整性

**Findings 區塊：**
- [ ] 命名格式：`{卷號}_Findings`（無 Volume 前綴）
  - 正確範例：`1A_Findings`、`2A_Findings`、`SUPA_Findings`
  - **錯誤範例：`Volume1A_Findings`（有 Volume 前綴，需修正）**
- [ ] Finding 數量：主卷 / SUP 卷標注 8–15 條（若不同需說明理由）
- [ ] Finding 編號格式說明：
  - 主卷 1A–4B：`V{卷號}-NN`（如 `V1A-01`）
  - SUP 系列：`VSUP-{字母}NN`（如 `VSUP-A01`、`VSUP-DA01`）
  - **錯誤格式：`[卷號-01]`（方括號格式不符，需修正）**
- [ ] Finding 格式有「信心等級」說明

**Carry_Forward 區塊：**
- [ ] 命名格式：`Carry_Forward_To_{具體卷號}`
  - 正確範例：`Carry_Forward_To_3B`、`Carry_Forward_To_0C`、`Carry_Forward_To_3A_3B`
  - **錯誤範例：`Carry_Forward_To_Volume3`（有 Volume 前綴且不具體，需修正）**
- [ ] 每條 Carry_Forward 條目有 (a) 參數類型 (b) 量化值 (c) 適用條件 (d) Findings 編號

**其他區塊：**
- [ ] `Inherited_Baseline` 規格說明存在
- [ ] `Unresolved_Dependencies` 存在（**所有卷均需，包括主卷**）
- [ ] `Correction_Instructions` 存在（SUP 卷專用；主卷標注 N/A）

---

#### 【C7】七、排除條件——格式

- [ ] 使用 `❌` 標記逐條列出
- [ ] 每條指向負責卷號（「那是卷 XX 的任務」）

---

#### 【C8】命名一致性快速掃描

快速掃描全文，確認：
- [ ] 卷號寫法與 `Volume_ID` 一致（如 `1A` 不混用 `vol.1A`）
- [ ] Finding 編號格式只用一種（不混用方括號與 V 前綴）
- [ ] `Carry_Forward` 命名在全文中一致

---

### Step 3：輸出稽核報告

```
## instruction.md 格式稽核報告

**目標卷**：{卷號}
**檔案**：{檔案名稱}
**稽核日期**：{日期}
**卷型判定**：{主卷 / 補充卷 / 最上游層（0A/0B）}

| 檢查項目 | 狀態 | 說明 |
|---------|------|------|
| C1 YAML Frontmatter | ✅ / ⚠️ N 件 | |
| C2 ⚠️ 前置輸出格式區塊 | ✅ / ⚠️ N 件 | |
| C3 八章結構 | ✅ / ⚠️ N 件 | |
| C4 反幻覺原則（4層） | ✅ / ⚠️ N 件 | |
| C5 Fallback 六大水體 | ✅ / ⚠️ N 件 / N/A | |
| C6 輸出區塊規格 | ✅ / ⚠️ N 件 | |
| C7 排除條件格式 | ✅ / ⚠️ N 件 | |
| C8 命名一致性 | ✅ / ⚠️ N 件 | |

**總計**：{X} 項問題

---

## 問題清單

### [FMT-{卷號}-01] {簡短標題}
- **檢查項目**：C{N}
- **問題**：{描述問題，含所在章節或行數}
- **範本要求**：{對應範本的哪一條規定}
- **修正方向**：{具體修改建議，包含新舊對照（若適用）}

### [FMT-{卷號}-02] ...

---

## 優先修正順序

1. **高優先**（影響 Gemini 輸出解析）：C2 前置區塊、C6 Finding 編號格式、C6 Carry_Forward 命名
2. **中優先**（影響一致性）：C4 反幻覺原則、C6 Unresolved_Dependencies 缺失
3. **低優先**（格式整齊）：C3 章節標題微調、C7 排除條件格式
```

---

### Step 4：批次稽核模式

若使用者想一次稽核多卷，逐卷執行 Step 1–3，最後輸出彙整表：

```
## 批次稽核彙整

| 卷號 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | 問題總數 |
|-----|----|----|----|----|----|----|----|----|---------|
| 1A  | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | 2 |
| 1B  | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | 3 |
| ... | | | | | | | | | |
```

---

## 常見問題速查

| 問題類型 | 對應檢查 | 修正方向 |
|---------|---------|---------|
| 沒有 ⚠️ 前置區塊 | C2 | 在 YAML 之後、一、之前加入 ⚠️ 區塊 |
| 反幻覺原則只有 2 層 | C4 | 擴充為四層，加入指名物種和標注標籤 |
| `Volume1A_Findings`（有 Volume 前綴）| C6 | 改為 `1A_Findings` |
| `Carry_Forward_To_Volume3`（有 Volume 且不具體）| C6 | 改為 `Carry_Forward_To_3A` 或 `Carry_Forward_To_3B` |
| 缺 `Unresolved_Dependencies` | C6 | 在 Section 八末尾加入此區塊 |
| Finding 用方括號格式 `[1A-01]` | C6 | 改為 `V1A-01` |
| 北部管理池 fallback 缺水車說明 | C5 | 補入「水車/增氧機非常態開啟（僅高溫低風時段啟動節電，平時關閉）」 |
| SUP 卷缺 `Correction_Instructions` | C6 | 加入 Correction_Instructions 規格說明 |
