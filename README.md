# Gemini Deep Research 使用說明

這個資料夾同時保留兩套 prompt：

1. **母版 `0-4`**
   - 用來保存原始章節設計與完整 scope
   - 適合當總規格、總參考
   - **不建議直接拿去給 Gemini App 跑整卷 deep research**

2. **Gemini 專用 split 版本**
   - `0A-0D`
   - `1A-1B`
   - `2A-2B-2C`
   - `3A-3B`
   - `4A-4B`
   - 這套是實際給 Gemini App Deep Research 使用的版本

---

## 執行狀態

Zone-B（桃竹苗）已納入所有卷 instruction，v2 全面重跑中。三區並列（Zone-A/B/C）為標準輸出格式，新產出報告將內建，無需另行補丁。

| 卷 | 現行版本 | 說明 |
|----|---------|------|
| 0A | `0A_台灣四季氣候 forcing 與區域差異.md` | Zone-A/B/C 三區並列已完成 |
| 0B | `0B_南北成土母質與地球化學基底.md` | 地球化學與物理底質特徵已完成 |
| 0C | `0C_六大水體 seasonal 評估.md` | Zone-A/B/C 三區並列；V0C-01–14；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-05-29） |
| 0D | `0D_基底資料矩陣與極端事件整合.md` | B0-01–19；Zone-A/B/C 三區並列已完成 |
| 1A | `1A_短時間環境觸發與生理限制.md` | V1A-01–12；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-01） |
| 1B | `1B_六大水域棲位模型與風生流.md` | V1B-01–13；Zone-A/B/C 三區並列；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-01） |
| 2A | `2A_覓食偏好、印記與反射咬餌.md` | V2A-01–12；Zone-A/B/C 三區並列；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-01） |
| 2B | `2B_側線、內耳與水下聲學傳遞.md` | V2B-01–13；2 輪 plan review + Q-SUP-01/02 補充研究（EPS 聲學衰減三成分分解、Stokes 振盪球近場修正）+ 第二輪 5-Phase 稽核 + Claude 後處理完成（2026-06-02） |
| 2C | `2C_視線軸向、攻擊角度與假餌操作.md` | V2C-01–12；Zone-A/B/C 三區並列；2 輪 plan review + Q-SUP-01/02 補充研究（Up-Strike 溫度/DO/深度門檻三區分列、全視野視敏度 CPD 換算）+ 第二輪 5-Phase 稽核 + Claude 後處理完成（2026-06-02） |
| 3A | `3A_高壓舊魚心理機制與誘咬本質.md` | V3A-01–13；2 輪 plan review + 深度學理推導 + 5-Phase 稽核 + Claude 後處理完成（2026-06-03） |
| 3B | `3B_極端情境高壓策略推演.md` | V3B-01–26；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-03） |
| 4A | `4A：繁衍地球化學與水文干擾.md` | V4A-01–15；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-03） |
| 4B | ⏳ 待跑 | |
| SUP-A | ⏳ 待跑 | |
| SUP-B | ⏳ 待跑 | |
| SUP-C | ⏳ 待跑 | |
| SUP-D-A | ⏳ 待跑 | instruction.md 已建立 |
| SUP-D-B | ⏳ 待跑 | instruction.md 已建立 |
| SUP-D-C | ⏳ 待跑 | 建議在 A/B 後執行；instruction.md 已建立 |
| SUP-E | ⏳ 待跑 | 與 SUP-D 平行 |

---

## 核心原則

### 1. `0A` 和 `0B` 是平行基底
- `0A`：氣候 forcing
- `0B`：成土母質與地球化學基底
- **兩者互不依賴**
- 跑 `0B` 時 **不需要** 上傳 `0A`

### 2. `0C` 才開始合流
- `0C` 會把 `0A + 0B` 代入六大水體
- 跑 `0C` 時，請上傳：
  - `0A` 的 deep research 報告
  - `0B` 的 deep research 報告

### 3. `0D` 是後續各卷的主要共通基底
- `0D` 不只是摘要，而是整合卷
- 它會把 `0A-0C` 整理成：
  - `Baseline_Facts`
  - `Waterbody_Model_Table`
  - `Open_Assumptions`
- **後續 1-4 卷原則上優先引用 `0D`**

### 4. 後續各卷不需要一直回頭吃全部上游
- 一般情況只要吃主要上游
- 只有需要額外細節時，才補上更早的子卷

---

## 建議執行順序

### 第一層：卷 0 基底建構

1. `0A：台灣四季氣候 forcing 與區域差異-instruction.md`
   - **上傳需求：無**
   - ⚠️ **v2 修訂（2025-05）**：原版只有「北部迎風面（台北）」與「南部背風面（高雄）」兩區。v2 新增 **Zone-B 北部背風面（桃園/新竹/苗栗，代表站：桃園 CWA）**，所有量化輸出改為三區並列。重跑時請使用更新後的 prompt，並通知 `0D` 也需重跑以繼承更新。

2. `0B：南北成土母質與地球化學基底-instruction.md`
   - **上傳需求：無**
   - ⚡ **1 和 2 無相依，可同時開兩個 Deep Research 並行執行**

3. `0C：六大水體 seasonal 評估-instruction.md`
   - **上傳需求：`0A` 報告 + `0B` 報告**

4. `0D：基底資料矩陣與極端事件整合-instruction.md`
   - **上傳需求：`0A` 報告 + `0B` 報告 + `0C` 報告**

---

### 第二層：卷 1 與卷 2

5. `1A：短時間環境觸發與生理限制-instruction.md`
   - **主要上傳：`0D`**

6. `1B：六大水域棲位模型與風生流-instruction.md`
   - **主要上傳：`0D`**；可選補充：`0C`
   - ⚡ **5 和 6 無相依，可並行執行**

7. `2A：覓食偏好、印記與反射咬餌-instruction.md`
   - **主要上傳：`0D`**
   - **可選補充：`1A`**

8. `2B：側線、內耳與水下聲學傳遞-instruction.md`
   - **主要上傳：`0D`**
   - ⚡ **7 和 8 無相依，可並行執行（但 2C 要等 2A 完成）**

9. `2C：視線軸向、攻擊角度與假餌操作-instruction.md`
   - **主要上傳：`0D`**
   - **必要補充：`2A`**（視覺波長衰減與 Reaction Strike 觸發結論）

---

### 第三層：卷 3

10. `3A：高壓舊魚心理機制與誘咬本質-instruction.md`
    - **主要上傳：`0D` + `1A` + `2A` + `2B`**
    - **可選補充：`2C`**（視線軸向操作機制）

11. `3B：極端情境高壓策略推演-instruction.md`
    - **主要上傳：`0D` + `1B` + `2A` + `2B` + `3A`**
    - **可選補充：`2C`**（在極端情境下視線軸向對應的假餌選擇）

---

### 補充卷：SUP-A / SUP-B / SUP-C（待跑）

> 主鏈完成後，針對特定數據缺口補跑的 Gemini Deep Research。

- **SUP-A：感官生理閾值補充研究**（⏳ 待跑）
  - 聚焦：閃光融合頻率（CFF）、聽覺閾值、感覺恢復時間（ART）
  - 下游整合至：3A `Open_Assumptions`、3B `Unresolved_Dependencies`

- **SUP-B：底棲水化學梯度補充研究**（⏳ 待跑）
  - 聚焦：Fick 擴散精算 H₂S / Fe²⁺ 安全距離、H₂S 三維死亡區、CDOM 化學竊聽
  - 下游整合至：1B、3B、4A

- **SUP-C：黑鱸毒區迴避實證與冒險覓食決策機制**（⏳ 待跑）
  - 聚焦：H₂S/低溶氧耐受行為、FIE（Fisheries-Induced Evolution）、LVF/HVF 族群分類、Foraging Forays（毒區覓食短突）
  - 上游繼承：0D、4A、SUP-A、SUP-B
  - 下游整合至：3A、3B

- **SUP-D-A：食性選擇性與感官匹配優先序**（⏳ 待跑，**可與 SUP-D-B 平行**）
  - 聚焦：Chesson's α / Ivlev's E 食性選擇指數；NTU 視覺失效閾值（三水體）；感官匹配優先序矩陣；LVF vs HVF Reaction Strike 觸發概率差異
  - 上游繼承：2A、2B、0D、3A
  - 輸出（VSUP-DA01–XX）整合至：2A（食性選擇指數補充）、3A/3B（LVF 觸發差異）；同時作為 SUP-D-C 上游

- **SUP-D-B：多模態獵物辨識與追擊序列**（⏳ 待跑，**可與 SUP-D-A 平行**）
  - 聚焦：活體蛙 vs 落葉 vs 假餌入水衝擊聲壓波（Hz/dB/ms）；追擊序列各階段時間窗口；Commit 觸發加速度閾值；Dead Stop 效果（%）
  - 上游繼承：2A、2B、0D、3A
  - 輸出（VSUP-DB01–XX）整合至：2B（入水辨識聲學特徵）、3A/3B（追擊序列與 Commit 觸發）；同時作為 SUP-D-C 上游

- **SUP-D-C：水中漂流偵測與策略切換**（⏳ 待跑，**建議在 A/B 後執行**）
  - 聚焦：生物微振動振幅 μm/s；Bio-Drift 偵測距離；搜索映像 LTP 時間窗口 ms；Match the Hatch vs Reaction Strike 神經生理切換條件；LVF 學習速度
  - 上游繼承：2A、2B、0D、3A；建議同時提供 SUP-D-A/B 報告
  - ⚡ **三卷均可與 SUP-E 平行執行**
  - 輸出（VSUP-DC01–XX）整合至：2A（漂流偵測）、3A/3B（策略切換條件）

- **SUP-E：台灣六大水體獵物群落時空圖譜——魚蝦兩棲昆蟲爬蟲類季節性爆量月曆與假餌映射**（⏳ 待跑，**與 SUP-D 平行**）
  - 聚焦：台灣六大水體 × 北中南三區 × 12 個月的獵物爆量月曆；五大獵物類群（魚、甲殼類、兩棲類、水生昆蟲、爬蟲）；北美 Hatch Equivalent 台灣化對應；OFT 切換豐度閾值（Q6）；假餌映射建議
  - 上游繼承：0A（三區月均水溫）、0C（六大水體基準）、0D
  - ⚡ **可與 SUP-D 平行執行**：獨立生態調查；本卷量化「外在豐度條件」，SUP-D 量化「內在神經迴路機制」，兩者下游合用
  - 輸出預計整合至：2A（台灣獵物能量表補充）、1B（六大水體獵物棲位補充）、3B（與 SUP-D 合用構建完整台灣情境決策矩陣）

---

### 第四層：卷 4

12. `4A：繁衍地球化學與水文干擾-instruction.md`
    - **主要上傳：`0D`**
    - **可選補充：`0B`**

13. `4B：棲位競爭、容載量與護巢防禦-instruction.md`
    - **主要上傳：`0D` + `1B` + `4A`**

---

## 最簡引用圖

```text
0A ─┐
    ├─> 0C ──> 0D
0B ─┘

0D ──> 1A / 1B / 2A / 2B
0D + 2A ──> 2C
0D + 1A + 2A + 2B (+ 2C) ──> 3A
0D + 1B + 2A + 2B + 3A (+ 2C) ──> 3B
0D + 4A (+ 1B) ──> 4B

SUP-A ──> 3A（Open_Assumptions）／3B（Unresolved_Dependencies）
SUP-B ──> 1B（V1B-05/06 精算）／3B（Unresolved 標記）／4A（CI-03/04）
SUP-C ──> 3A（LVF/HVF 分類、V3A-06 皮質醇解讀）／3B（Foraging Forays、毒區容忍度）
SUP-D-A ∥ SUP-D-B ──> SUP-D-C（A/B 先完成或用 Fallback）
SUP-D-A + SUP-D-B + SUP-D-C ──> 2A（食性選擇指數、漂流偵測）／2B（入水辨識聲學）／3A（策略切換、Commit 觸發）／3B（戰術切換條件）
SUP-E ──> 2A（台灣獵物補充）／1B（六大水體獵物棲位）／3B（戰術切換生態事實）

SUP-D-A ∥ SUP-D-B ∥ SUP-E（三卷平行，無相依；SUP-D-C 在 A/B 後執行）
```

> 括號 `(+ 卷)` 表示可選補充，不上傳也能完成。

---

## 實際操作建議

### 如果你要用 Gemini App

每跑一份 split prompt，都建議：

1. 開一個新的 Deep Research
2. 上傳該卷需要的上游報告
3. 貼上對應的 split prompt
4. 檢查 Gemini 生成的 plan 是否有：
   - 跑出本卷 scope
   - 忽略上游報告
   - 漏掉固定輸出區塊
5. 若沒有上述問題，就直接開始 research

---

## 什麼情況下要再拆？

### 優先觀察 `0C`

如果 Gemini 之後仍然出現：
- 六大水體只寫成北部/南部總論
- 四季時間軸被壓扁
- A/B/C 三面向有漏項

那下一個最值得再拆的是：
- `0C-北部三水體`
- `0C-南部三水體`

**不要先拆整套其他卷。**

---

## 母版與 split 版的角色分工

### 母版 `0-4`
- 保存原始設計
- 用來檢查整體關聯性
- 用來做總規格與回查

### split 版
- 真正拿去給 Gemini App 跑
- 降低單次 deep research 的廣度
- 盡量保留原本的 inheritance 與引用鏈

---

## 最後一句

如果你忘記順序，記這句就夠了：

> **先做 `0A + 0B`，再做 `0C`，再做 `0D`；後面大多數卷優先吃 `0D`。**

---

## 授權條款

本作品採用 [創用CC 姓名標示－非商業性－相同方式分享 4.0 國際授權條款](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hant)。

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hant)

- **姓名標示**：使用或引用本作品須標示原作者
- **非商業性**：禁止將本作品用於商業目的
- **相同方式分享**：衍生作品須採用相同授權條款釋出
