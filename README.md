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
| 0D | `0D_基底資料矩陣與極端事件整合.md` | B0-01–22；Zone-A/B/C 三區並列；補入 B0-20/21/22（Zone-B 春季超前、Eh 首觸）（2026-06-03） |
| 1A | `1A_短時間環境觸發與生理限制.md` | V1A-01–12；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-01） |
| 1B | `1B_六大水域棲位模型與風生流.md` | V1B-01–13；Zone-A/B/C 三區並列；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-01） |
| 2A | `2A_覓食偏好、印記與反射咬餌.md` | V2A-01–12；Zone-A/B/C 三區並列；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-01） |
| 2B | `2B_側線、內耳與水下聲學傳遞.md` | V2B-01–13；2 輪 plan review + Q-SUP-01/02 補充研究（EPS 聲學衰減三成分分解、Stokes 振盪球近場修正）+ 第二輪 5-Phase 稽核 + Claude 後處理完成（2026-06-02） |
| 2C | `2C_視線軸向、攻擊角度與假餌操作.md` | V2C-01–12；Zone-A/B/C 三區並列；2 輪 plan review + Q-SUP-01/02 補充研究（Up-Strike 溫度/DO/深度門檻三區分列、全視野視敏度 CPD 換算）+ 第二輪 5-Phase 稽核 + Claude 後處理完成（2026-06-02） |
| 3A | `3A_高壓舊魚心理機制與誘咬本質.md` | V3A-01–13；2 輪 plan review + 深度學理推導 + 5-Phase 稽核 + Claude 後處理完成（2026-06-03）；VSUP-A 補丁：CFF 多溫度點、ART Q₁₀ 2.0 矩陣、Schreckstoff Zone 分離（2026-06-03） |
| 3B | `3B_極端情境高壓策略推演.md` | V3B-01–27；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-03）；VSUP-A 補丁：V3A 條目更新、V3B-12/13/19 皮質醇基線對齊、新增 V3B-27（H₂S 水車重啟，數值待 SUP-B 確認）（2026-06-03） |
| 4A | `4A：繁衍地球化學與水文干擾.md` | V4A-01–15；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-03）；補入 B0-22 + VSUP-B08（H₂S 巢穴死亡區）（2026-06-03） |
| 4B | `4B：棲位競爭、容載量與護巢防禦.md` | V4B-01–15；Zone-A/B/C 三區並列；1 輪 plan review + Q-SUP 三項（V4B-13/14/15）+ 5-Phase 稽核 + Claude 後處理完成（2026-06-03）；第二輪稽核 6 條補丁（FIX-4B-07~12：VSUP-B06 H₂S 閾值更正、VSUP-B08 非批准上游標注、V4B-05 信心等級修正、α₁₂ 缺口補入 Unresolved）完成（2026-06-04） |
| SUP-A | `SUP-A：感官生理閾值補充研究.md` | VSUP-A01–09；3 輪 plan review + 5-Phase 稽核 + Claude 後處理（11 條 FIX）完成（2026-06-03） |
| SUP-B | `SUP-B：底棲水化學梯度補充研究報告.md` | VSUP-B01–14；2 輪 plan review + 5-Phase 稽核 + Claude 後處理完成（2026-06-04）；V3B-27 H₂S 水車重啟衝突解決 |
| SUP-C | `SUP-C_黑鱸毒區迴避實證與冒險覓食決策機制.md` | VSUP-C01–12；2 輪 plan review + 5-Phase 稽核 + Claude 後處理（FIX-SUPC-01~04：V-code 版本漂移標注、4A V4A-10 [確認] CI 補入）完成（2026-06-04） |
| SUP-D-A | `SUP-D-A_食性選擇性與感官匹配優先序.md` | VSUP-DA01–11；2 輪 plan review + 5-Phase 稽核 + Claude 後處理（14 條 FIX-SDA-01~14）完成（2026-06-04）；Zone-B NTU 標注補入；Unresolved_Dependencies 補入 3 項 instruction 必列優先缺口 |
| SUP-D-B | `SUP-D-B_多模態獵物辨識與追擊序列.md` | VSUP-DB01–12；3 輪 plan review + 第一輪 5-Phase 稽核（FIX-SUPDB-01~09）+ **第二輪 5-Phase 稽核（FIX-SDB-01~11：禁詞修正、信心等級降調 ×4、DB09/DB11 理論估算補標、Carry_Forward 補 2B 條目、Correction_Instructions 補 3B 確認）** 完成（2026-06-04）；Carry_Forward 8 組；Correction_Instructions 4 條 |
| SUP-D-C | `SUP-D-C_水中漂流偵測與策略切換.md` | VSUP-DC01–14；2 輪 plan review + 5-Phase 稽核 + Claude 後處理（7 條 FIX-DC-01~07）完成（2026-06-04）；Carry_Forward 5 組；Unresolved_Dependencies 5 項 |
| SUP-E | ⏳ 待跑 | 與 SUP-D-A/B/C 平行（instruction.md 已更新卷號引用） |

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

- **SUP-B：底棲水化學梯度補充研究**（✅ 完成 2026-06-04）
  - 聚焦：Schreckstoff × CDOM 死區半徑修正（Zone-A/B/C 三區）、Fick 擴散精算 Fe²⁺/H₂S 安全距離、水車重啟瞬態 H₂S 擴散
  - Correction_Instructions 覆蓋：V1B-CF-04（北部 Fe²⁺ 上修）、V1B-10（H₂S 確認上界）、V3A-12（Schreckstoff 死區 Zone 分野）
  - V3B-27 H₂S 水車重啟衝突已解決（VSUP-B11 支撐）

- **SUP-C：黑鱸毒區迴避實證與冒險覓食決策機制**（✅ 完成 2026-06-04）
  - 聚焦：H₂S/DO 迴避行為實證、個體差異（75–85% 立即逃逸 vs 15–25% 靜止容忍）、Foraging Forays（15–25 s 時間窗口、單日安全上限）、比較毒理學（M. salmoides vs P. mexicana/K. marmoratus）、3D 行為決策矩陣
  - 上游繼承：0D（B0-11）、4A（V4A-10）、3A（皮質醇）、SUP-A（VSUP-A09 ART）、SUP-B（VSUP-B09/B11 安全距離）
  - Correction_Instructions 覆蓋：V1B-10（H₂S 安全高度確認）、V3A-12（COX 重置補充）、V3A-09（皮質醇基線修正）、VSUP-B11（確認）、V4A-10（確認）
  - 下游整合至：3A（V3A-06 皮質醇解讀）、3B（Foraging Forays、靜止容忍）

- **SUP-D-A：食性選擇性與感官匹配優先序**（✅ 完成 2026-06-04）
  - 聚焦：Chesson's α / Ivlev's E 食性選擇指數；NTU 視覺失效閾值（三水體）；感官匹配優先序矩陣；LVF vs HVF Reaction Strike 觸發概率差異（HVF 65–80%、LVF 15–30%）
  - 上游繼承：2A、2B、0D、3A
  - 輸出（VSUP-DA01–11）整合至：2A（食性選擇指數補充）、3A/3B（LVF 觸發差異）；同時作為 SUP-D-C 上游

- **SUP-D-B：多模態獵物辨識與追擊序列**（✅ 完成 2026-06-04）
  - 聚焦：活體蛙 vs 落葉 vs 假餌入水衝擊聲壓波（Hz/dB/ms）；追擊序列各階段時間窗口；Commit 觸發加速度閾值；Dead Stop 效果（%）
  - 上游繼承：2A（V2A-06/07/11）、2B（V2B-01/02/03）、0D（B0-06/11）、3A（V3A-05/09）
  - 輸出（VSUP-DB01–12）整合至：2B（入水聲壓頻率與側線感知頻段配對）、3A/3B（追擊序列時間窗口、Commit ≥2.5 m/s²、Dead Stop HVF +30–50%/LVF −40–60%）；Correction_Instructions 覆蓋 2A/3A/3B；同時作為 SUP-D-C 上游

- **SUP-D-C：水中漂流偵測與策略切換**（✅ 完成 2026-06-04）
  - 聚焦：生物微振動振幅 15–40 μm/s（1–5 Hz）；Bio-Drift 側線辨識距離（六大水體 12–80 cm）；Tilt 視覺偵測距離 80–120 cm；搜索映像 LTP 1500–2500 ms；LVF vs HVF Reaction Strike 差距 35–65 個百分點；策略切換 12–24 hr 窗口
  - 上游繼承：2A（V2A-05/06/07）、2B（V2B-01/02）、3A（V3A-09）、SUP-D-A（VSUP-DA01/05/08/09/11）、SUP-D-B（VSUP-DB01/02/03/07/10）
  - 輸出（VSUP-DC01–14）整合至：2A（漂流偵測數值）、2B（側線辨識距離補充）、3A/3B（策略切換閾值、LVF 衰退曲線、Dead Drift 感官通道排序）
  - Correction_Instructions：V2A-07/12（確認+補充 NTU 閾值）、V3A-09/10（LVF 衰退曲線中間數據點）、V3B-04/12（Dead Drift 材質量化、Match the Hatch 切換時序）

- **SUP-E：台灣六大水體獵物群落時空圖譜——魚蝦兩棲昆蟲爬蟲類季節性爆量月曆與假餌映射**（⏳ 待跑，**與 SUP-D-A/B/C 平行**）
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
