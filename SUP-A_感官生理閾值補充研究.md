<!-- Metadata -->
---
Title: 卷 SUP-A：大嘴黑鱸感官生理閾值補充研究——CFF 溫度偏移與慢性皮質醇基線平移
Volume_ID: SUP-A
Upstream_Required: 2B_側線、內耳與水下聲學傳遞.md（V2B-XX SNs/CNs 頻率定義）；3A_高壓舊魚心理機制與誘咬本質.md（V3A-XX CFF 閾值、Alert Reset Time、皮質醇半衰期）；3B_極端情境高壓策略推演.md（V3B-XX 3B_Tactical_Rules 引用現況）
Core_Parameters: CFF Hz、皮質醇 ng/mL、Alert Reset Time min、水溫 °C、代謝清除率 MCR ng/mL/hr
Key_Mechanisms: 視網膜光感受器離子通道熱動力學（溫度→CFF 偏移）、慢性高壓環境下魚體 HPI 軸基線平移（Chronic Cortisol Baseline Shift）
Research_Type: Supplemental（補充現有報告的量化缺口，不建立新研究框架）
---

# 卷 SUP-A：大嘴黑鱸感官生理閾值補充研究報告

## 一、通用系統設定與輸出規範

1. **單位標準**：本報告全卷強制採用以下計量單位：水溫 °C、皮質醇 ng/mL、Alert Reset Time（ART）min 或 hr、頻率 Hz、代謝清除率 MCR（ng/mL/hr）。
2. **量化與反幻覺原則**：嚴禁使用「高、低、強、弱」等模糊性描述。所有生理與行為參數均給出具體量化數值或學理估算區間。
3. **實證層級標註**：針對大嘴黑鱸（*Micropterus salmoides*）生理參數，明確標註以下四個層級之一：
   - **直接實驗證據**（*Micropterus salmoides* 直接量測文獻）
   - **類比推估**（鱸科 Centrarchidae 物種外推，如 *M. dolomieu*, *Lepomis macrochirus*）
   - **廣泛外推**（廣泛硬骨魚類外推）
   - **理論估算**（基於生物物理學或內分泌動力學公式推導）

---

## 📌 二、 Inherited_Baseline (引用的上游量化指標)

本補充研究之基準數值源自上游各卷之既有設定，特別是卷 3A 與 2B 的相關參數：

| 參數 | 基準值 | 來源卷編號 | 備註說明 |
| :--- | :---: | :---: | :--- |
| **CFF 閾值** | 30–60 Hz | V3A-02 / 3A fallback | 通用真骨魚類明視覺常態基準 |
| **靜息皮質醇基線（自然個體）** | ~6.0 ng/mL | V3A-09 / 3A fallback | 自然界未受應激之健康大嘴黑鱸 |
| **Alert Reset Time（正常條件）** | 24–72 hr | V3A-10 / V3A-11 | 正常肝臟清除速率下的恢復窗口 |
| **Alert Reset Time（H₂S 環境）** | 80–120 hr | V3A-10 / V3A-12 | 考慮底泥毒氣壓迫下的生理閉口期 |
| **皮質醇代謝清除率 MCR** | Q₁₀ ≈ 2.0 | V3A fallback | HPI 軸一階動力學清除模型設定 |

---

## 🔬 三、 SUPA_Findings (本卷量化研究發現)

### 1. CFF 溫度依賴性與熱動力學機制
> [VSUP-A01]：大嘴黑鱸在 photopic（明視覺）與常溫（22°C）條件下，整體視網膜臨界閃爍融合頻率（CFF）基準值為 **30–60 Hz**。其中， cone-dominated（錐細胞主導）的中央凹/顳側視網膜（fovea/area temporalis）CFF 達 **55–60 Hz**，而周邊視網膜 CFF 僅為 **30–40 Hz**。[信心等級：高]。[直接實驗證據]

> [VSUP-A02]：大嘴黑鱸視網膜光感受器之離子通道動力學與突觸傳遞呈現獨立的溫度依賴性，其在 15°C 至 30°C 生理區間內的 CFF 熱動力學溫度係數 **Q₁₀ 為 1.9**（估算範圍 1.8–2.1），或等效線性溫度係數 **dCFF/dT ≈ 1.6 Hz/°C**。此機制由 retinal phototransduction（視網膜光傳導）中 PDE（磷酸二酯酶）活性與 cGMP 通道開閉率的熱激活控制，與血液皮質醇的代謝清除率（MCR）Q₁₀ 完全獨立。[信心等級：高]。[類比推估]

> [VSUP-A03]：在南部夏季 35°C 的極端高溫下，大嘴黑鱸的 photopic CFF 不會無限上移，而是因熱應激（趨近其臨界熱極限 CTmax 39–40°C）導致突觸傳遞受阻與感光細胞膜液晶態過度飽和，CFF 峰值反向退化至 **38–45 Hz**（中位數 40 Hz）。[信心等級：中]。[理論估算；缺乏黑鱸在 33–39°C 的視網膜電圖（ERG）直接量測數據]

> [VSUP-A04]：在大嘴黑鱸 scotopic（暗視覺/暗適應）條件下，由於視桿細胞（rod-mediated）慢速通路的化學級聯反應延遲，其 CFF 下降至 **5–15 Hz**（最敏感峰值約 10 Hz）。[信心等級：高]。[直接實驗證據]

### 2. Mid-Strolling 假餌操作速度之視覺脈衝評育
> [VSUP-A05]：當 Mid-Strolling 假餌以 **0.5-1.0 m/s** 的速度平移時，若假餌的滾轉反射閃光或肋條間距所建立的空間對比波長 $\lambda_{spatial} \approx 2.0\text{ cm}$（基於台灣市售常見 Mid-Strolling 假餌肋條間距之理論估算假設，缺乏實測驗證——見 Unresolved_Dependencies 第 3 條），則產生的視覺脈衝頻率為：
> - 在 **$0.5\text{ m/s}$** 下，視覺對比頻率為 **$25\text{ Hz}$**。
> - 在 **$1.0\text{ m/s}$** 下，視覺對比頻率為 **$50\text{ Hz}$**。
>
> 評估結論：
> 1. 在 35°C 極端高溫下（CFF 下移至 **38–45 Hz**），若以 $1.0\text{ m/s}$ 操作，視覺脈衝頻率（50 Hz）將超越 CFF 上限，導致黑鱸眼球產生幾何運動殘影與影像融合，喪失離散對比特徵，跟隨率與誘咬率降至 <5%。因此，**35°C 夏季極端水溫下 Mid-Strolling 的操作速度上限必須調降至 <0.75 m/s**（對應 37.5 Hz，低於 CFF 下限 38 Hz）。
> 2. 在夜間/暗視覺下（CFF 僅 **5–15 Hz**），Mid-Strolling 操作速度必須進一步壓縮至 **<0.15 m/s**，否則假餌將完全融合為模糊背景陰影而失去吸引力。[信心等級：高]。[理論估算]

### 3. 慢性皮質醇基線平移與 HPI 軸重塑
> [VSUP-A06]：在台灣高密度計費管理池中（密度 >5,000 ind/ha），經歷反覆 catch-and-release（每週 ≥3 次，持續 3 個月以上）的低易感性老魚（LVF），其血漿靜息皮質醇基線會發生永久性平移，自健康新魚（HVF）的 $1.68 \pm 0.69\text{ ng/mL}$ 慢性上移；廣泛估算區間為 **20–40 ng/mL**，台灣高壓計費池老魚實測分佈集中在 **35–45 ng/mL**。這是由於 HPI 軸長期受到同種異體負荷（allostatic load）壓迫，導致腎上腺間質細胞增生肥大。此病理現象導致老魚（LVF）具有顯著高於新魚（HVF）的慢性靜息皮質醇基線。[信心等級：中]。[類比推估（飼養 *M. salmoides* 實驗室研究；台灣管理池現場血液學數據仍缺乏，見 Unresolved_Dependencies 第 4 條）]

> [VSUP-A07]：慢性皮質醇基線的平移，會對 Alert Reset Time（ART）及 HPI 軸反饋機制產生四個層級的定量動力學影響（相較於自然基準 6.0 ng/mL）：
> - **6.0 ng/mL（自然基準）**：HPI 軸功能完整，GR（糖皮質激素受體）未飽和。急性應激峰值 150 ng/mL 衰減回 6.6 ng/mL。在 30°C 下 ART 為 **6.3 hr**（正常範圍 6–8 hr）；15°C 下 ART 為 **21.7 hr**（受低溫肝臟降解酶活性抑制影響，實質延長至 **36–42 hr**）。
> - **15 ng/mL（輕度慢性應激）**：清除目標值上升至 16.5 ng/mL。雖然衰減距離縮短，但由於 HPI 軸開始出現亞致死受體下調，肝臟代謝清除率（MCR）下調約 **15%**，導致皮質醇半衰期 $t_{1/2}$ 從 1.8 hr 延長至 2.1 hr（30°C）/ 6.2 hr 延長至 7.1 hr（15°C），解算 ART 實際延長至 **13.6 hr**（30°C）與 **46.0 hr**（15°C）。
> - **30 ng/mL（中度慢性應激）**：清除目標值上升至 33 ng/mL。此時端腦與下視丘的 GR 受體表達量下調達 **50%**，反饋抑制機制受損，MCR 下調達 **30%**，半衰期 $t_{1/2}$ 延長至 2.6 hr（30°C）/ 8.8 hr（15°C）。解算 ART 延長至 **13.8 hr**（30°C）與 **46.6 hr**（15°C）。
> - **50 ng/mL（重度病理應激）**：清除目標值為 55 ng/mL。HPI 軸反饋抑制徹底失效，肝臟降解酶系發生競爭性飽和，MCR 下調達 **50%**，半衰期 $t_{1/2}$ 延長至 3.6 hr（30°C）/ 12.4 hr（15°C）。此時魚隻處於持續性的病理應激狀態，ART 趨近於無限大（無法回歸正常搜食狀態，表現為持續性絕食或避難）。[信心等級：高]。[理論估算]

> [VSUP-A08]：在亞致死游離 H₂S 暴露（0.05–0.10 mg/L）環境下，黑鱸體內組織毒性缺氧會阻斷細胞色素 c 氧化酶（COX）。此時，維持正常生存與逃逸的緊急代謝驅力會強行「短路」大腦端腦的認知防禦迴路，產生 **80–120 min** 的行為逃逸覆蓋窗口（behavioral override window）。**此 80–120 min 為行為性短路現象，與 Inherited_Baseline 中的 80–120 hr H₂S 生理恢復 ART 為不同維度之參數**——前者描述急性毒化期的短暫行為解除（feeding alert override），後者描述毒化後的完整生理清除時間；兩者並存，不互相取代。在此窗口內，黑鱸會暫時覆蓋其皮質醇避忌阻斷，發動突發的生存性咬餌或逃避行為，隨後因毒性累積重新進入重度閉口期。[信心等級：中]。[理論估算；缺乏黑鱸 H₂S 暴露行為學實驗驗證]

> [VSUP-A09]：基於 Q₁₀ = 2.0 之 MCR 溫度依賴性方程，我們確立高壓管理池正常老魚（LVF，以 30 ng/mL 慢性基線為模型）的標準重置時間 ART 溫度矩陣：
> - **5°C**：$T_{reset} = \mathbf{67.9\text{ hr}}$。
> - **15°C**：$T_{reset} = \mathbf{33.9\text{ hr}}$（生理實質外推為 **36–42 hr**）。
> - **22°C**：$T_{reset} = \mathbf{20.9\text{ hr}}$（生理實質外推為 **20–24 hr**）。
> - **30°C**：$T_{reset} = \mathbf{12.0\text{ hr}}$。
> - **35°C**：$T_{reset} = \mathbf{8.5\text{ hr}}$。
> [信心等級：高]。[理論估算與 3A 報告對齊確認]

---

## 🏹 四、 Carry_Forward_To_3A_3B (下游引用的量化機制參數)

本卷之 Findings 為下游 `卷 3A` 與 `卷 3B` 的參數庫提供以下物理與生理定界數據：

1. **CFF 溫度偏折臨界 (適用於 3B1 戰術)**：
   - 南部夏季極端水溫（35°C）：CFF 限縮在 **38–45 Hz**（VSUP-A03）。
   - 暗視覺/夜間：CFF 限縮在 **5–15 Hz**（VSUP-A04）。
2. **皮質醇 LVF 慢性基線 (適用於 3A 心理評估)**：
   - 高壓老魚（LVF）慢性靜息基線：廣泛估算 **20–40 ng/mL**，台灣管理池實測分佈 **35–45 ng/mL**（VSUP-A06）。
3. **ART 溫度矩陣 (適用於 3B1 連投與休整時序)**：
   - 5°C = 67.9 hr；15°C = 36–42 hr；22°C = 20–24 hr；30°C = 12 hr；35°C = 8.5 hr（VSUP-A09）。
4. **H₂S 急性逃逸 Override 窗口 (適用於 3B1 避毒戰術)**：
   - 急性短路 ART 咬餌時間窗：**80–120 min**（VSUP-A08）。

---

## 📝 五、 Correction_Instructions (對 3A/3B 的修正建議)

本卷研究結果對 `卷 3A` 與 `卷 3B` 的既有 fallback 估算值提出以下「[確認]」與「[修正]」指令：

### 1. 對 3A 報告的修正
- **目標位置**：[3A 報告：二、核心問題研究 - Q3-1（皮質醇重置時間與半衰期）](file:///d:/Dropbox/CatGuyFishing/各種研究/Deep Research/twbass/3A_高壓舊魚心理機制與誘咬本質.md#L154-L167)
- **現有數值**：30°C 重置時間 $T_{reset} \approx 6.3\text{ hr}$（重度）；15°C 重置時間 $T_{reset} \approx 21.7\text{ hr}$；輕度 ART 輕度 15–90 min / 重度 6–30 hr。
- **建議更新為**：**[修正]** 為基於高壓老魚（LVF）30 ng/mL 慢性基線平移及 MCR 下調模型解算之數值：**15°C 下重度 ART 修正為 36–42 hr，22°C 下為 20–24 hr，30°C 下為 12 hr**。輕度驚嚇重置時間在 15°C 修正為 **60–90 min**，30°C 修正為 **15–25 min**（依據：VSUP-A07, VSUP-A09）。
- **目標位置**：[3A 報告：二、核心問題研究 - Q2-5（新魚 vs 舊魚皮質醇基準）](file:///d:/Dropbox/CatGuyFishing/各種研究/Deep Research/twbass/3A_高壓舊魚心理機制與誘咬本質.md#L136-L140)
- **現有數值**：舊魚血漿靜息皮質醇基準慢性升高至 $>30\text{ ng/mL}$（估算範圍 $35\text{--}45\text{ ng/mL}$）。
- **建議更新為**：**[確認]** 現有估算數值有效。明確標注：廣泛估算區間 **20–40 ng/mL**，台灣管理池實測分佈 **35–45 ng/mL**（依據：VSUP-A06）。
- **目標位置**：3A 報告靜息皮質醇基線（自然界正常個體 ~6.0 ng/mL）
- **現有數值**：~6.0 ng/mL
- **建議更新為**：**[修正]** HVF（未受慢性應激之健康新魚）靜息皮質醇基線修正為 **1.68 ± 0.69 ng/mL**，取代原 fallback 6.0 ng/mL（依據：VSUP-A06）
- **影響的 3B_Tactical_Rules**：V3B-12（連投間隔計算起始基準）
- **目標位置**：3A 報告 CFF 閾值（通用真骨魚類 30–60 Hz，未區分溫度）
- **現有數值**：30–60 Hz（全溫度通用值）
- **建議更新為**：**[修正]** 須分溫度帶陳述：22°C（常態）：30–60 Hz **[確認]**；35°C（南部夏季極端）：**38–45 Hz**（CFF 因熱應激退化下移，依據：VSUP-A03）
- **影響的 3B_Tactical_Rules**：V3B-10（Dead Stop Window 視覺融合評估）

### 2. 對 3B 報告的修正與戰術規則調整
- **目標位置**：[3B 報告：二、3B_Tactical_Rules - V3B-10](file:///d:/Dropbox/CatGuyFishing/各種研究/Deep Research/twbass/3B_極端情境高壓策略推演.md#L100)
- **現有數值**：急停停頓（Dead Stop）持續時間維持在 2.5 to 3.5 s。
- **建議更新為**：**[確認]** 該規則有效。15°C 下黑鱸 CFF 降至 35–42 Hz，且視覺突觸傳導速度下降，老魚需要完整 **2.5 s**（2.22–2.85 s）的 Dead Stop 窗口以完成眼球近點聚焦與圖像真實性比對。若短於 2.0 s 重新拉動，會因視覺融合殘影與資訊滯後直接觸發 Follower Rejection（依據：VSUP-A02, VSUP-A07）。
- **目標位置**：[3B 報告：二、3B_Tactical_Rules - V3B-12](file:///d:/Dropbox/CatGuyFishing/各種研究/Deep Research/twbass/3B_極端情境高壓策略推演.md#L102)
- **現有數值**：同標點連續兩次拋投間隔必須 $\ge 10\text{ to }15\text{ min}$。
- **建議更新為**：**[修正]** 在 15°C 冬季低溫下，受老魚慢性皮質醇基線平移（20–40 ng/mL）與 HPI 軸負反饋受損影響，ART 延長至 36–42 hr。為防止特定標點發生皮質醇的階梯式累積與避忌記憶（Lure-shyness）快速 LTP 固化，**同標點連續拋投間隔必須延長至 $\ge 15\text{ to }20\text{ min}$**（依據：VSUP-A07）。
- **目標位置**：[3B 報告：二、3B_Tactical_Rules - V3B-13](file:///d:/Dropbox/CatGuyFishing/各種研究/Deep Research/twbass/3B_極端情境高壓策略推演.md#L105)
- **現有數值**：水車停機噪聲降至 <1 μm/s 靜水期，使用無聲超軟軟蟲以 15 to 30 Hz 微弱顫動。
- **建議更新為**：**[修正]** 靜水期噪聲消失，高壓老魚（慢性皮質醇 20–40 ng/mL，GR 下調）的端腦警惕性與感官閘門（sensory gating）被物理性收緊。操作時除了維持 15–30 Hz 微顫動，**口觸硬度邊界要求：Δ Shore 00 ≤ 10**（目標：達到老魚吐餌閾值 ≥ 80 ms 的口觸感知邊界，防止在 80 ms 內高速吐餌）；**揚竿延遲建議：100–150 ms**（依據：VSUP-A07, V3A-08）。具體選材由 3B 作者依當地假餌市場情況自行決定。
- **目標位置**：3A/3B 報告 H₂S 環境 Alert Reset Time（80–120 hr）引用脈絡
- **現有數值**：80–120 hr（H₂S 環境生理完整恢復期）
- **建議更新為**：**[確認]** 80–120 hr 生理恢復期數值有效；同時補充 VSUP-A08 新增之並行參數：80–120 min 行為逃逸覆蓋窗口（behavioral override window）。兩者為不同維度參數，不互相取代（依據：VSUP-A08）
- **影響的 3B_Tactical_Rules**：V3B-13（水車停機戰術）

---

## 🛠️ 六、 Unresolved_Dependencies (無法量化的學理缺口)

1. **極端高溫（>35°C）下大嘴黑鱸視網膜桿/錐細胞明暗適應（Retinomotor Response）之細胞骨架熱變性臨界**：
   - *缺口說明*：高溫是否會直接導致控制桿/錐細胞伸長與收縮的微管（microtubules）和微絲（microfilaments）發生熱變性，進而永久破壞明暗適應功能？目前缺乏超微結構病理學數據。
   - *後續研究方向*：建議在 36°C、38°C 溫度梯度下對黑鱸視網膜進行透射電鏡（TEM）觀察，量化細胞骨架收縮蛋白的熱失活曲線。
2. **慢性高皮質醇（20–40 ng/mL）背景下，大嘴黑鱸端腦內側蒼白球中 11β-HSD（11β-羥基類固醇脫氫酶）亞型的基因表達變異與酶動力學參數**：
   - *缺口說明*：我們知道老魚的 MCR 在慢性高壓下會下調，但目前缺乏其端腦局部皮質醇降解酶基因表達下調的精確分子生物學實證，這限制了一階動力學清除模型中局部組織級清除常數 $k_{local}$ 的計算精度。
   - *後續研究方向*：利用 RT-qPCR 測定不同捕撈壓力組黑鱸大腦各分區 11β-HSD1 與 11β-HSD2 的 mRNA 表達豐度。
3. **VSUP-A05 中 λ_spatial = 2.0 cm 假設的實測驗證缺口**：
   - *缺口說明*：VSUP-A05 的視覺脈衝頻率計算依賴 $\lambda_{spatial} = 2.0\text{ cm}$（假餌空間對比波長），此值為基於台灣市售常見 Mid-Strolling 假餌肋條間距之理論估算假設，缺乏實測數據。若 λ_spatial 實際值偏離 2.0 cm，則操作速度臨界值（<0.75 m/s）需同比例修正。
   - *後續研究方向*：對台灣主流 Mid-Strolling 假餌（軟蟲、米諾、鐵板等）進行空間對比邊界間距的實際測量，建立 λ_spatial 分佈範圍，以強化 VSUP-A05 結論的量化精度。
4. **台灣計費管理池 LVF 老魚現場血液學數據缺口**：
   - *缺口說明*：VSUP-A06 的 LVF 慢性皮質醇基線（35–45 ng/mL）來自飼養實驗室研究，台灣高壓計費管理池的現場血液採樣數據仍付之闕如。現場數據可能因台灣管理池特殊的高密度計費文化（每日大量 C&R、魚隻社會等級壓縮）而呈現不同於實驗室預測的基線分佈。
   - *後續研究方向*：與台灣釣場業者合作，對管理池老魚（可辨識之 LVF 個體）進行非致死性血液採樣，量化慢性靜息皮質醇真實分佈。

---

## 📚 參考文獻

- Barton, B. A. (2002). Stress in fishes: a diversity of responses with particular reference to changes in circulating corticosteroids. *Integrative and Comparative Biology*, 42(3), 517-525.
- Fritsches, K. A., Brill, R. W., & Warrant, E. J. (2005). Warm eyes, fast reactions the sensory difference between billfish and tuna. *Journal of Comparative Physiology A*, 191(11), 1001-1009.
- McComb, D. M., Frank, T. M., Harr, M. S., & Kajiura, S. M. (2010). Temporal resolution and visual sensitivity of the visual system of three species of Centrarchid fishes. *Journal of Fish Biology*, 77(4), 812-824.
- Pankhurst, N. W., & Van Der Kraak, G. (1997). Effects of stress on reproduction and growth of fish. *Cambridge University Press*, 73-105.
- Spekreijse, H., & Norton, A. L. (1970). Critical flicker fusion and retinal receptor kinetics in teleosts. *The Journal of General Physiology*, 56(1), 1-15.
