---
Title: 卷 3A：台灣管理釣場高壓舊魚心理機制與誘咬本質
Volume_ID: 3A
Upstream_Required: 0D 報告:0D_基底資料矩陣與極端事件整合.md（Baseline_Facts, Waterbody_Model_Table）；1A 報告:1A_短時間環境觸發與生理限制.md（感官觸發臨界值）；2A 報告:2A_覓食偏好、印記與反射咬餌.md（OFT 決策、Reaction Strike）；2B 報告:2B_側線、內耳與水下聲學傳遞.md（側線頻率響應）
Core_Parameters: 皮質醇半衰期 hr、Alert Reset Time min、CFF 頻率 Hz、視網膜焦距 cm、尾流頻率 Hz
Key_Mechanisms: Mid-Strolling 視覺催眠（CFF 神經同步）、Follower Rejection 近場焦距失焦決策、Alert Reset Time 皮質醇動力學、新魚/舊魚行為二元化、急停觸覺觸發門檻
---

# 一、通用系統設定與輸出規範

1. **Metadata 區塊**：研究報告輸出時必須在最上方重現上述 Metadata 格式並填入實際研究結果。
2. **單位標準（全卷強制）**：溫度 °C、溶氧 mg/L、Eh mV、能見度 cm、時間 hr/day、皮質醇 ng/mL、皮質醇半衰期 hr、Alert Reset Time min、頻率 Hz。
3. **量化要求**：Mid-Strolling CFF（Hz）、Follower Rejection 急停決策窗口（s）、Alert Reset Time 最小間隔（min）、皮質醇峰值/基準值（ng/mL）均需量化或給出合理估算區間；嚴禁使用「高、低、強、弱」等模糊描述。
4. **推測標示**：缺乏台灣直接實證須標示為「基於 OOO 理論之推測」。
5. **章節分離原則**：「機制論證」（神經生理學理）與「作釣涵義映射」需分節書寫，嚴禁混寫；完整戰術配方留給卷 3B。
6. **跨卷引用**：凡引用 0D/1A/2A/2B 數值，必須標注來源編號（如 `B0-07`、`V1A-03`）；覆蓋 fallback 時標注「[覆蓋 fallback 假設]」。

---

# 二、計畫背景與本卷定位

本卷為《台灣大嘴黑鱸釣魚環境生態白皮書》**卷 3A**，隸屬**第 3 冊：高壓釣場心理與戰術推演**。

**白皮書總範疇：** 研究對象為台灣封閉/半封閉淡水水體（埤塘、水庫、管理池）中大嘴黑鱸（*Micropterus salmoides*）的生態與釣魚環境。全書分為五冊：第 0 冊（0A–0D）物理基底層、第 1 冊（1A–1B）魚類生理與棲位、第 2 冊（2A–2C）掠食心理與感官、第 3 冊（3A–3B）高壓釣場戰術、第 4 冊（4A–4B）繁殖生態。

**本卷定位：** 本卷聚焦台灣**封閉管理釣場**（計費式埤塘）中長期受高捕撈壓力的「舊魚（conditioned resident fish）」的神經生理與心理機制。台灣管理池的關鍵特徵是每週/月補放孵化場新魚，形成**新魚（naïve）/ 舊魚（conditioned）行為二元化結構**，造成刺激-反應動力學高度分歧。本卷建立此分歧的機制基礎，供 3B 映射至三個極端情境。

**本卷對下游的貢獻：**
- 3B 完全依賴本卷 `Carry_Forward_To_3B` 中的 Alert Reset Time、Follower Rejection 窗口與 Mid-Strolling 脫習慣化條件
- 本卷的新魚/舊魚皮質醇二元標準（ng/mL）是 3B 三種情境選策的分叉依據

本卷**不直接開具體戰術配方**（留給 3B）；**不重寫 1A/2A/2B 的底層感官機制**（只引用結論）；**不處理繁衍期護巢防禦**（4B）。

---

# 三、系統設定

**你的角色：** 你現在是一位結合「魚類神經行為學家」、「皮質醇動力學研究者」與「高壓管理釣場生態分析師」背景的 AI 專家。請針對【卷 3A：台灣管理釣場高壓舊魚心理機制與誘咬本質】進行深度搜尋與學理分析。

**Gemini Deep Research 執行規則：**
1. 你會先根據本 prompt 生成 research plan；本檔所有條件都視為強制約束，不得在 plan 階段自行擴張、改寫或跨出本卷 scope。
2. **若使用者已上傳 `0D`**，優先引用 `Baseline_Facts`、`Waterbody_Model_Table` 與 `Lag_Effect` 作為環境基底。
3. **若已上傳 `1A`**，引用其光觸發閾值（lux）、氣壓反應（hPa）、溫差閾值（°C）。
4. **若已上傳 `2A`**，引用 OFT 能效公式（E_gain/E_cost 比）、Reaction Strike 觸發速度（m/s）、孵化場皮質醇印記機制。
5. **若已上傳 `2B`**，引用側線振動頻率響應（Hz）、近場/遠場感知臨界距離（cm）。
6. 若你的預設 research plan 與本 prompt 衝突，以本 prompt 的 scope 規則為優先。
7. 在 research plan 中，請先明確列出：本卷研究邊界、要繼承的上游區塊、核心問題、來源類型、固定輸出區塊。

---

# 四、獨立執行與上游輸入規則

1. **本卷可獨立執行**；若提供 `0D`，優先引用其共通基底；若提供 `1A`/`2A`/`2B`，分別引用對應感官觸發參數。
2. 若未提供上游文件，先列出 `Missing_Upstream_Context`，再以保守假設完成分析。
3. 本卷只處理高壓舊魚的心理/神經/感官機制；戰術配方轉發至 3B。
4. 除正文外，文件結尾必須額外輸出：
   - `Inherited_Baseline`：列出實際引用的上游編號（如 `B0-07`, `V1A-03`）及量化數值。
   - `Volume3A_Findings`：8–15 條，每條附唯一編號（格式 `V3A-01`）。
   - `Carry_Forward_To_3B`：後續卷 3B 應繼承的機制參數清單。

---

# 五、台灣釣場情境與預設前提

**台灣管理釣場新魚/舊魚行為二元化背景：**

台灣計費管理池通常以週/月頻率補放孵化場魚苗，造成行為二元結構：
- **新補放魚（naïve hatchery fish）**：孵化場印記維持低皮質醇基準（估算 10–15 ng/mL），OFT 能效邊界寬鬆（E_gain/E_cost 閾值低），Reaction Strike 閾值低（觸發速度 <0.3 m/s）。
- **歷史舊魚（conditioned resident fish）**：多次 catch-and-release 或反覆假餌暴露後，皮質醇慢性升高（估算靜息基準 >30 ng/mL），OFT 能效邊界收緊，Reaction Strike 閾值升高，出現 Following 不咬（Follower Rejection）。

**六大水體壓力情境分類（精簡版）：**
1. **北部野生埤塘**（<3m，極育土褐色水）：低壓、舊魚比例低；冬季低溫延長 Alert Reset Time
2. **北部深水埤塘/水庫**（>10m，微酸性極育土）：自然壓力低；寒流短暫衝擊觸發棲位壓縮
3. **北部管理池**（<2m，極育土）：**高壓核心場景**；新舊魚二元明顯，水車/增氧機間歇性背景噪聲（僅高溫低風時段開啟）干擾側線基準；停車靜水期為側線感知高敏窗口
4. **南部野生埤塘**（<2m，弱育土）：低壓；夏季 >32°C 高溫關機（主動覓食停止）
5. **南部深水埤塘/水庫**（>10m，弱育土）：自然壓力低；旱季消落帶棲位強烈壓縮
6. **南部管理池**（<2m，弱育土）：**高壓核心場景**；高溫迫使低代謝，高有機物 H₂S 壓力加劇 Alert Reset 延長

---

# 六、核心研究清單

**Q1：Mid-Strolling 視覺催眠效應與神經同步機制**

「Mid-Strolling」指假餌以中速穩定平移時，魚出現長距離跟隨、頭部固定、眼球凝視而不咬的狀態。

1. 穩定移動刺激如何在魚類視覺皮層觸發「持續跟蹤放電（sustained tracking discharge）」——optic tectum 的 direction-selective neuron 最佳觸發速度（cm/s）與方向選擇寬度（°）。
2. 假餌反射閃光頻率（Hz）在何範圍最可能觸發視網膜 flicker fusion 臨界（critical flicker fusion frequency, CFF）附近的神經同步？量化 CFF 估算值（Hz）。
3. 高壓舊魚是否因長期暴露產生「習慣化（habituation）」？Dishabituation（脫習慣化）機制（突然加速或停頓）能否重啟跟蹤放電？量化脫習慣化所需速度突變 Δcm/s 或急停持續時間（s）。
4. Mid-Strolling 假餌尾流（von Kármán vortex street）如何觸發側線感知——尾流頻率（Hz）與距假餌尾部的感知有效距離（cm）。
5. 打破 Mid-Strolling 狀態的操作轉換條件：速度突變閾值（Δcm/s）、急停持續時間（s）、角度偏轉（°）與對應咬餌觸發機率的估算。

**Q2：Follower Rejection 視網膜焦距評估決策模型**

「Follower Rejection」指魚跟至極近距離（<30 cm）後突然回頭不咬的狀態。

1. 鱸魚視網膜在極近距離（<20 cm）的空間解析度（cycles/degree）變化——是否因近場焦距過短造成假餌細節失焦，反向觸發威脅迴避（antipredator response）？量化失焦距離臨界（cm）。
2. 舊魚「急停決策窗口」：從假餌停止到魚做出咬/不咬決定的持續時間估算（s），及影響此窗口長度的因素（水溫 °C、假餌尺寸比、邊緣效應有無）。
3. 「邊緣效應（Edge Effect）」：假餌在障礙物旁（落差邊、水草邊緣）如何利用邊界層（boundary layer）改變水動力場，縮短 Follower Rejection 決策窗口，量化效果距離（cm）。
4. 「觸覺觸發（tactile trigger）」閾值：軟質假餌（Shore A 硬度差異）在極近距離是否激發口觸前測試咬——觸發所需口接觸時間（ms）與材質硬度差異閾值。
5. 新魚 vs 舊魚的 Follower Rejection 比率差異估算，及其與皮質醇基準值（ng/mL）的相關性。

**Q3：Alert Reset Time 皮質醇動力學與最短投擲間隔**

「Alert Reset Time」指魚被驚擾後恢復正常搜食狀態所需的時間。

1. 大嘴黑鱸急性應激後皮質醇峰值（ng/mL）的估算區間，與皮質醇血液半衰期（hr）——直接推算「最短有效投擲間隔（min）」。
2. 水溫對皮質醇代謝速率的影響：高溫（>28°C）vs 低溫（<15°C）的半衰期差異估算（hr），及台灣夏季南部管理池 vs 冬季北部管理池的實際最小間隔（min）。
3. 「局部驚嚇 vs 全場驚嚇」的 Alert Reset Time 差異：鉤中逃竄是否觸發 Alarm Substance（皮膚傷害素）擴散？靜水擴散半徑（m）與稀釋半衰期（min）。
4. 高壓舊魚「慢性壓力恆定升高（chronic stress hyperactivation）」：靜息皮質醇基準（ng/mL）的合理範圍，與急性重置時間的區分方法。
5. 台灣管理池「連投模式」涵義：根據皮質醇半衰期，推算北部冬季（水溫 15°C）與南部夏季（水溫 30°C）的科學最小投擲間隔（min）。

---

# 七、排除條件

- 不直接開具體戰術配方（假餌型號、操作動作序列）；機制分析後以精簡映射表呈現作釣涵義，完整戰術配方留給 3B。
- 不重寫 1A/2A/2B 底層感官機制正文；只引用發現編號。
- 不處理繁衍期護巢防禦性攻擊（4B scope）。
- 不討論低壓野生埤塘的一般覓食行為；若提及，標示為對比背景。

---

# 八、最終輸出區塊規格

### `Inherited_Baseline`
列出實際引用的上游編號（如 `B0-07`、`V1A-03`、`V2A-05`、`V2B-04`）及對應量化數值。若為 fallback，標示「[Fallback]」。

### `Volume3A_Findings`
8–15 條，每條附唯一編號（格式 `V3A-01`、`V3A-02`…）。必須涵蓋：Mid-Strolling CFF 頻率估算（Hz）、Follower Rejection 急停窗口（s）與失焦臨界距離（cm）、Alert Reset Time 皮質醇半衰期（hr）及南部夏季/北部冬季最小投擲間隔（min）、新魚/舊魚皮質醇二元分離門檻（ng/mL）。

### `Carry_Forward_To_3B`
列出卷 3B 極端情境推演應直接繼承的參數，含：
- Mid-Strolling 觸發 CFF 頻率範圍（Hz）與脫習慣化操作條件（Δcm/s 或急停 s）
- Follower Rejection 急停窗口長度（s）與邊緣效應有效距離（cm）
- Alert Reset Time 分情境最小間隔：南部夏季（水溫 ~30°C）vs 北部冬季（水溫 ~15°C）
- 新魚/舊魚行為二元分離皮質醇門檻（ng/mL）
