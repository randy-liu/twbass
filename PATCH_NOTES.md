# Patch Notes — 跨文件合規修復

> v1 修復紀錄（0A–SUP-C、Zone-B 補丁、0C1/0D1/3B1 格式修正）已封存至 git history。
> 見 commit `0f4a843` 以前的版本。

---

<!-- 新的修復紀錄從此處開始 -->

---

## senior 月相段改寫＋褪黑激素術語卡（2026-06-16）

**性質**：可讀性改寫＋新增術語卡（lux 機制降為背景）。
**目標檔案**：`台灣大嘴黑鱸白皮書-senior.md`、`build.py`、`台灣大嘴黑鱸白皮書-expert.md`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| senior 月相重寫 | 改成「月光夠亮騙魚以為白天」白話＋**現場三條件（滿月＋晴夜＋清水，要同時成立）**；0.01/0.064/0.0015 lux（人眼判不出）降為背景；保留夜間 19:30–23:30／曙光 05:00–06:00／白天 07:30–15:30 規避時段 |
| 新增褪黑激素卡 | GLOSSARY 加 `melatonin 褪黑激素` 卡並自動連結，把 lux 機制（0.01 半抑制、清水 0.064 壓 90% vs 濁水 0.0015 僅 9%）收進卡當背景 |
| expert | 診斷表「月相隔日閉口」行的動作格補「月相限滿月＋晴夜＋清水才成立」 |
| junior | 未提月相、未動 |

---

## senior/expert 光照「上午關機」去窄化＋現場判讀（2026-06-16）

**性質**：可讀性改寫＋去窄化（數值保留為背景，無數值衝突）。
**目標檔案**：`台灣大嘴黑鱸白皮書-senior.md`、`台灣大嘴黑鱸白皮書-expert.md`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| senior 重寫 | 「上午關機」段：機制（明暗適應 30–45 min＋20,000 lux 飽和致盲，於「魚所在水層」）＋觸發＝天空亮（仰角×雲量）×水透光×深度（破除固定鐘點窄化）＋現場判讀（無照度計、戴偏光鏡：太陽影子／偏光鏡看水底曬亮=該撤離亮淺灘改打深水陰影／咬口斷掉）＋晴天時段降為基準並補陰天・冬天調整。lux／時段全保留為背景 |
| expert 校準段 | 第四部承 L135（斷崖機制）補一段：斷崖線＝仰角×雲量×透光×深度、非固定鐘點、陰天冬天位移、現場讀法（影子／偏光鏡／咬口）；診斷表「清水 07:30」加「晴天」 |
| junior | L39 本就白話（大晴天閃瞎、陰天好咬）、無鐘點無 lux，未動 |

---

## 新增三術語卡＋「閾值」改白話「門檻」（2026-06-16）

**性質**：可讀性/可點性（內容不變，術語卡鏡射正文）。
**目標檔案**：`build.py`、`台灣大嘴黑鱸白皮書-{senior,expert}.md`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| 新增術語卡 | GLOSSARY 加 `魚鰾`（含大物/小物：50 vs 35 cm 魚鰾膨脹 2.5 倍、大物棄淺潛深 24–48 hr）、`斯涅爾窗`（含光線機制：直射光雜光多 vs 散射光邊緣對比 +35–50%）、`rheotaxis 逆流定向`；正文自動連結（魚鰾出現 3 處最受益）|
| 閾值→門檻 | 「閾值」（一般讀者少見）全面改白話「門檻」：senior 6、expert 2、GLOSSARY 8 處；junior 本無此詞、未動 |

---

## 術語連結與排序標題釐清（2026-06-16）

**性質**：可讀性/可點性修正（內容不變）。
**目標檔案**：`build.py`、`台灣大嘴黑鱸白皮書-senior.md`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| Stokes 術語連結擴充 | `build.py` TERM_PATTERNS 由只認「Stokes 沉降」擴成「Stokes 沉降/定律/計算」→ senior「Stokes 定律」、expert「Stokes 計算」現在都連到 `stokes` 術語卡 |
| senior 排序標題去歧義 | 「缺氧速度（快→慢）」→「**多快崩到缺氧（越前面越快崩）**」（原文易被誤解成恢復速度，實為 onset）；「澄清速度（快→慢）」→「**多快變清（越前面越快清）**」 |
| 其他等級 | junior 為白話無排序句、expert 為明確天數清單，無歧義；未動 |

---

## 暴雨澄清（絮凝）段改寫易讀（2026-06-16）

**性質**：可讀性改寫（數值不變）。
**目標檔案**：`台灣大嘴黑鱸白皮書-senior.md`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| senior 絮凝段重寫 | §三「暴雨後澄清」段改清楚：①點明「北部本來就偏酸（pH 4.5–5.5）、暴雨是把酸性極育土逕流沖進來」而非「雨把水變酸」；②「沉速 100 倍」標明來自 Stokes 半徑平方（2→20 μm）；③「清＝退回平常茶褐色中等清澈、非清澈見底」（CDOM／藻沉不掉）。數值全保留 |
| junior/expert 未動 | junior（白話「土讓泥巴抱團沉底」）、expert（「酸性絮凝澄清 1–2 天，硬」）為簡版、無誤導，維持原樣 |

---

## 翻水/缺氧/鋒面三點釐清補入三篇（2026-06-16）

**性質**：內容補充（釐清常被誤推的觀念，無數值衝突）。
**目標檔案**：`台灣大嘴黑鱸白皮書-{junior,senior,expert}.md`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| ①靜水才適用離底高度 | 明確界定「離底避毒高度」只在**靜水分層**成立；風/翻水/水車混柱後 H₂S 散佈全柱、垂直避難失效→全池缺氧/中毒（南部低鐵致命、北部 FeS 多為缺氧），對策改為含氧進水口/撤退等再分層 |
| ②缺氧是一次性脈衝 | 翻水 DO 崩潰是靜水累積量「一次釋放」的脈衝（數小時–2 天）；脈衝後**持續風＝復氧**（亂流＋冷水高溶氧），連續鋒面≠連續缺氧 |
| ③鋒面分冬夏 | 冬·東北季風多日＝限制在低溫低活性（氧足）；夏·梅雨滯留鋒/颱風後西南流＝降溫常為利多、氧靠風維持，限制轉為濁度（側線）＋分層池單次攪翻脈衝，前置降壓期為爆咬窗 |
| 等級放置 | senior §二正文三點清單；junior 難關四後白話破除迷思盒；expert 劇本六後精簡校準段 |

---

## 南部 H₂S／避毒高度段改寫易讀（2026-06-16）

**性質**：可讀性改寫（內容/數值不變）。
**目標檔案**：`台灣大嘴黑鱸白皮書-{junior,senior,expert}.md`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| senior 主段重排 | 「南部弱育土含鐵低…」改成因果鏈（低鐵→毒多高 0.15–0.85→魚扛不住只能離底 0.002→避毒高度→北部 FeS 反例）；把「深槽 150 公分」明寫成「最深、最不流動、爛泥最厚的深坑／深溝要離底 ~150 cm」避免被誤讀成水深；數值全保留，後面「現場怎麼分」鼻判句保留 |
| junior 講白「深水槽底」 | 兩處把「深水槽底」定義為「池子最深、最不流動、爛泥最厚的坑／溝（常在最深處或出水口附近）」，beginner 不放數值 |
| expert 劇本二補深坑 | 「餌離底 ≥100 cm」補上「最深最滯爛泥最厚的深坑／溝毒帶更高、需 ≥150 cm 或乾脆放棄」 |

---

## 交叉引用改用頁內錨點跳轉（2026-06-16）

**性質**：UX 修正（取代 06-15 的術語彈窗做法）。
**目標檔案**：`台灣大嘴黑鱸白皮書-senior.md`、`build.py`、`docs/index.html`

| 項目 | 說明 |
|------|------|
| 交叉引用改回錨點跳轉 | senior「見〈不用儀器判讀溶氧〉」改為**頁內錨點跳轉**（`<a id="senior-do-field">` ＋ `[…↓](#senior-do-field)`），連到 §二同名框、點擊捲過去、看完捲回來。因來源與目標同部、相距僅十餘行，06-15 的術語彈窗做法多餘又重複內容，已捨棄 |
| 還原 do 術語卡 | `build.py` `do` 卡還原為原始定義（移除 06-15 為彈窗補的「現場判讀法」，避免與 §二框重複）|
| 新增跳轉連結樣式 | `build.py` CSS 加 `#content a[href^="#"]`（主題色＋底線），讓頁內跳轉連結看起來可點、與術語的 dotted 底線區分 |

---

## 白皮書改名與南部清水/翻水概化修正（2026-06-15）

**性質**：檔名清理 + 內容修正（在既有三階白皮書上做針對性編輯，非如 2026-06-12 從研究報告重新綜合）。
**目標檔案**：`台灣大嘴黑鱸白皮書-{junior,senior,expert}.md`、`build.py`、`README.md`、`docs/index.html`

### 內容

| 項目 | 說明 |
|------|------|
| 檔名清理 | 三份白皮書去除 `featFable5` 尾綴：`…featFable5-{junior,senior,expert}.md` → `…-{junior,senior,expert}.md`（已成正式交付物，不再於檔名標示模型來源）。同步更新 `build.py` VERSIONS 與 `README.md` 檔案表的引用；以 `git mv` 保留歷史 |
| 內容修正 | 清澈度與翻水改以**水體類型/季節**為主軸，南北僅作修飾：月相、上午關機、反射咬臨界速度不再寫「南部清水 vs 北部濁水」，改依透光度/水色；junior 難關二、senior、expert 劇本五補上南部管理池冷休克翻水的 H₂S 毒性版本（原僅寫北部翻水）|
| 術語表同步 | `build.py` GLOSSARY 隨正文修正：`lux` 詞條改依透光清水（深水庫冷季）vs 染色濁水（高 CDOM／爆藻／管理池）；`翻水` 詞條移除「南部幾乎不發生」，補上南部深水庫季節翻轉（延至 1 月中–2 月下）與管理池冷休克翻水為毒性最高型 |
| 翻水卡數值 | `build.py` GLOSSARY `翻水` 卡 H₂S 危險高度由 v1 廢棄值「86–160 cm」改為 VSUP-B11 現行值（停機 ~100／深槽 ~150／水車重啟瞬態 120–160／高釋放全池致死），消除術語卡與正文（~100 cm）的衝突 |
| 路亞術語清理 | junior／senior 路亞名稱：移除非標準的「羽狂貝」→「Crawler 羽根系」；「橡皮頭 Jig」→「Rubber Jig」（expert 本就用通用名） |
| Zone 代碼可讀性 | senior（內文 19 處）／expert（13 處）的 `Zone-A/B/C` 代碼改用地名（台北/基隆/宜蘭、桃竹苗、高雄/台南/屏東）；senior L19 定義句保留代碼當圖例；junior 本無代碼 |
| Eh 現場判讀 | 三篇＋GLOSSARY `eh` 卡新增「不用儀器判讀 Eh／爛底」：靠搆得到的泥（岸邊/船錨/竿尾戳底）黑又臭＋自然冒泡（甲烷＝厭氧，需配合臭味才確認游離 H₂S，單顆會動多半是魚）＋岸邊水面；**裸鉛墜拖回會被水洗淨故不採**；深水以季節（盛夏）＋滯水推定；南北鼻判（南部游離 H₂S 黑又臭／北部 FeS 黑不臭）。等級調整：junior 感官盒、senior 毒區段＋定義、expert 環境型診斷區；mV 僅作背景、不進讀者決策流 |
| 數值補單位 | senior（8 處）／expert（3 處）補上漏標的單位：溶氧讀數一律加 mg/L（「下限 3」→「下限 3 mg/L」、「4.5+/3/1.5」「DO 1.6–2.0」「<1.5/<0.5」「DO ≥5」等）；expert 仰攻閘門「水溫 <10」補 °C；junior 本就不丟裸數字、未動 |
| 交叉引用可點 | senior「見〈不用儀器判讀溶氧〉」由「叫讀者自己找」改為**可點術語連結**（手動 `<span class="gl-trigger" data-term="do">`，靠 `#content` 事件委派觸發），點開浮出溶氧術語卡、關掉回原位；`build.py` `do` 術語卡補上完整「現場判讀法」（時間/水溫/擾動/藻華/浮頭＋4.5/3/1.5 mg/L 門檻），讓彈窗有料 |

---

## 讀者向分級白皮書與網站建置（2026-06-12）

**性質**：新增交付物（非研究報告合規修復）；讀者向產出線首次納入版本控制。
**目標檔案**：`台灣大嘴黑鱸白皮書featFable5-{junior,senior,expert}.md`、`build.py`、`docs/index.html`

### 內容

| 項目 | 說明 |
|------|------|
| 三階白皮書 | 以全部 `*_*.md` 研究報告＋四份淡水沿岸獵物報告為素材，重新綜合（不沿用舊 featFable5）；junior／senior／expert 三級，受眾與密度遞進，非單純堆疊 |
| 科普規範 | 科學詞彙一律國中程度白話、章節開頭宣告一次；senior／expert 加「💡 深入一點（可跳過）」opt-in 側欄（亮度對數尺度、Eh/H₂S 門檻非斜坡、Q10），主文不加深 |
| 網站 | `build.py` 改為三版合一頁輸出 `docs/index.html`：等級分頁、亮暗雙主題、術語速查（搜尋＋自動連結）、襯線標題；單一自含檔 |

### 後續補充

| 編號 | 修改內容 |
|------|---------|
| FIX-WP-溶氧-01 | 三份各補「不用儀器判讀溶氧」段，依等級調整深度：junior 五個免費判斷法（時間／水溫／擾動／藻華／浮頭）；senior 將 4.5/3/1.5 mg/L 落地為現場長相；expert 五代理指標並標信心等級（日週期、溫度×擾動、浮頭 ASR 為硬，藻華為中，分層底死區為推定軟）。修補「給了釣手無法現場量測的數字」缺口 |

---

## SUP-E 卷完整稽核與後處理（2026-06-09）

**目標檔案**：`SUP-E_台灣六大水體獵物群落時空圖譜——魚蝦兩棲昆蟲爬蟲類季節性爆量月曆與假餌映射.md`
**執行流程**：twbass-audit 5-Phase（第一輪）→ Q-SUP 補充研究（Gemini）→ twbass-audit 5-Phase（第二輪）→ Claude 後處理
**最終 Findings 數**：VSUP-E01–E27（含 Q-SUP 補充後新增 VSUP-E26/E27）
**Carry_Forward 區塊**：2 組（Carry_Forward_To_SUPDC、Carry_Forward_To_2A）
**Correction_Instructions**：CI-SUPE-01~04

### 稽核輪次紀錄

| 輪次 | Phase 6 判定 | 分數 | 主要缺口 | 處置 |
|------|-------------|------|---------|------|
| Round 1 | ⚠️ 多輪 Q-SUP 補充 | 15 分 | 三星攀鱸量化數值缺失、熊蟬側線觸發距離缺失、稻蝗水面運動缺失、VSUP-E15 拒咬反射 80 ms 未標推測依據、VSUP-E25 SMR 122.26 mg O₂/kg/hr 引用錯誤（應為 65.2，Díaz et al. 2007，原值為 RMR 誤引） | 送 Q-SUP-01~05 至 Gemini |
| Round 2 | ✅ 不需重跑 | 4 分 | 全 5 項 Q-SUP 缺口已填補；新增 4 項結構問題（FIX-SUPE-18~21：VSUP-E21-B/E22-C 編號不規範、Carry_Forward 錯誤 Hz、缺 E26/E27 數據、Zone 標注混用） | 進入最終 Claude 後處理 |

### 5-Phase 稽核結果（第二輪）

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 1 件 | VSUP-E16 幼龜 T_h > 15 s 缺推測依據標注 |
| P2 輸出區塊 | ⚠️ 2 件 | CI 缺 3A 確認條目；VSUP-E21-B/E22-C 編號不符規範 |
| P3 引用鏈 | ⚠️ 1 件 | Carry_Forward 「水蠆 20–30 Hz」無 VSUP-E19 文本支撐 |
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 6 項完整 |

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-SUPE-01 | VSUP-E15 蟾蜍蝌蚪拒咬反射時間改為 80–120 ms，加入 [類比推估] 標注（Kasumyan 2003 推算）（Q-SUP 補充） |
| FIX-SUPE-02 | VSUP-E16 幼龜 T_h > 15 s 加入 [理論估算；詳見 Unresolved_Dependencies #5] |
| FIX-SUPE-03 | VSUP-E25 SMR 修正：122.26 → 65.2 mg O₂/kg/hr（Díaz et al. 2007 直接實測；原值為 Q10=2.3 外推之 RMR 誤引） |
| FIX-SUPE-04 | 日曆欄位標題「中部峰值」改為「Zone-B 桃竹苗背風面」；介紹文字明確三區名稱 |
| FIX-SUPE-05 | Correction_Instructions 加入 CI-SUPE-01~03 正式編號 |
| FIX-SUPE-06~09 | Hatch_Equivalent_Calendar 補入 7 行缺失物種：澤蛙蝌蚪、小雨蛙透明蝌蚪、牛蛙巨型蝌蚪（Zone-C）、鰷條幼魚、草條田中鰟鮍、蓋斑鬥魚、極樂吻鰕虎 |
| FIX-SUPE-10 | 新增 CI-SUPE-04：確認 3A 報告 OFT 機制與 VSUP-E25 閾值相容，無需修改 |
| FIX-SUPE-11 | VSUP-E06/E12/E14/E16/E17/E20/E21/E25 加入 [覆蓋 fallback 假設：來自 XX 輔助報告] 標注 |
| FIX-SUPE-12 | VSUP-E01/E05/E11/E14/E20/E21 Zone-A/B 物候時間分離（依 B0-02 提前 12–18 天） |
| FIX-SUPE-13 | VSUP-E19 加入「感知機制詳見 SUP-D-B」Scope 連結 |
| FIX-SUPE-14 | Q-SUP 補入 VSUP-E03 三星攀鱸：繁殖期三區分列、幼魚 TL 30–60 mm、游速 0.05–0.15 m/s（[地理外推]） |
| FIX-SUPE-15 | Q-SUP 補入 VSUP-E26（原 VSUP-E21-B）熊蟬/薄翅蟬側線觸發半徑：60–90 cm / 30–50 cm（[類比推估]） |
| FIX-SUPE-16 | Q-SUP 補入 VSUP-E27（原 VSUP-E22-C）中華稻蝗：后足划水 2–3 Hz，推進速度 0.10–0.13 m/s |
| FIX-SUPE-17 | VSUP-E22 颱風脈衝持續時窗拆分為 4 組分：蚯蚓 12–24 hr、昆蟲 6–18 hr、兩棲類 24–48 hr、溪蟹 24–72 hr（各附理論依據）|
| FIX-SUPE-18 | VSUP-E21-B → VSUP-E26；VSUP-E22-C → VSUP-E27；Finding 總數更新為 27 |
| FIX-SUPE-19 | Carry_Forward_To_SUPDC 新增 VSUP-E26 熊蟬（5–12 Hz，半徑 60–90 cm）、薄翅蟬（8–15 Hz，30–50 cm）、VSUP-E27 稻蝗（2–3 Hz，0.10–0.13 m/s）三條機械波資料 |
| FIX-SUPE-20 | Carry_Forward_To_SUPDC 移除「水蠆 20–30 Hz」（無 VSUP-E19 文本支撐），改為速度突變描述（ΔV ≥ 0.40 m/s；Hz 待補充） |
| FIX-SUPE-21 | VSUP-E26 月份峰值由「Zone-A/B（北部/中部）8 月中旬峰」拆為 Zone-A 8月中旬、Zone-B 8月上旬（B0-02）、Zone-C 7月下旬三行 |

---

## SUP-E instruction.md 格式稽核修補（2026-06-05）

**目標檔案**：`SUP-E：台灣六大水體獵物群落時空圖譜——魚蝦兩棲昆蟲爬蟲類季節性爆量月曆與假餌映射-instruction.md`
**執行流程**：twbass-instruction-audit 8 項格式檢查
**同步加入 repo**：台灣淡水與沿岸四類生態輔助報告（甲殼類、兩棲類、水生爬蟲類、水生昆蟲）

| FMT 編號 | 檢查項目 | 修改內容 |
|---------|---------|---------|
| FMT-SUPE-01 | C2 + C6 | Finding 編號去方括號：`[VSUP-E01]` → `VSUP-E01`（⚠️ 前置區塊 item 2 + Section 八 SUPE_Findings 兩處，含格式範例行） |
| FMT-SUPE-02 | C6 | `Carry_Forward_To_SUPDC_2A` 拆分為 `Carry_Forward_To_SUPDC`（供 SUP-D-C 引用振動頻率 / 事件時序 / OFT 閾值）與 `Carry_Forward_To_2A`（供 2A 引用獵物能量密度 / 物種尺寸 / 假餌映射）兩個獨立區塊；⚠️ 前置區塊總數「六個」→「七個」 |
| FMT-SUPE-03 | C4 Point 4 | 推測標示補充說明：`[地理外推]`（等同「基於〔亞熱帶亞洲近緣物種研究〕之地理外推」） |

---

## SUP-D-B 卷完整稽核與後處理（2026-06-04）

**目標檔案**：`SUP-D-B_多模態獵物辨識與追擊序列.md`
**執行流程**：gemini-plan-review（3 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：VSUP-DB01–12　**Carry_Forward 區塊**：7 組（著水聲壓特徵、追擊序列時間窗口、接近最小速度、搜索映像排名、印記魚異化係數、Commit 觸發閾值、Dead Stop 效果）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | 5 項結構性缺口：Q3-3 游向距離、Q3-5 先天/習得分類、飼料印記魚量化、Q4-2 最小速度閾值、Q4-3 維度排名；V2A-07 速度值矛盾、V3A-09 皮質醇值偏移、V3A-03 Dead Stop 引用無效 | 送修正 prompt |
| Round 2 | ⚠️ Hold | 全部結構性缺口已補；V2A-11 新 V-code 解決速度衝突；V3A-03 Dead Stop 引用仍具幻覺風險 | 送修正 prompt（僅 V3A-03 處理說明） |
| Round 3 | ✅ Go | V3A-03 改為條件式驗證處理（有文獻列 Inherited_Baseline，無文獻列 VSUP-DB 新發現）；所有結構性缺口清零 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 1 件 | V2A-07 視頂蓋啟動潛伏期 30–50 ms 未列入 Inherited_Baseline（僅有 12–25 ms 快速通路） |
| P2 輸出區塊 | ⚠️ 1 件（格式） | Findings 計 13 條，超出 instruction 上限 12 條 |
| P3 引用鏈 | ⚠️ 6 件 | V2A-07 潛伏期缺失；V2A-11 非 Upstream_Required 列出之 V-code（待驗證）；V3A-03 於 CI 中被「確認」但 VSUP-DB11 自標「本卷推導值」矛盾；V2A-11 誤引於 VSUP-DB10 加速度計算；CI-2 引用未定義 V3A-10；CI-1 Carry_Forward_To_2C（2C 非本卷下游目標） |
| P4 Scope | Scope Note | VSUP-DB09 引用 OFT/LDH 為概念援引，非推導，不計違規 |
| P5 研究缺口 | ⚠️ 3 件 | Unresolved_Dependencies 缺 instruction 明定 3 項優先缺口：M. salmoides 入水聲壓辨識實驗、LVF 老魚行為遙測、Commit 加速度直接實測 |

**Phase 6 判定**：⚠️ Claude 結構重建（總分 19，結構分 73.7%，Q 覆蓋完整型）
所有 Q 問題均有研究段落；缺口集中在 Carry_Forward 遺漏、V-code 引用訂正與 Unresolved 補條目，無需 Gemini 補研究。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-SUPDB-01 | Carry_Forward 新增第 6 條：Commit 觸發閾值 ≥ 2.5 m/s²（來源 VSUP-DB10），下游 SUP-D-C / 3A / 3B |
| FIX-SUPDB-02 | Carry_Forward 新增第 7 條：Dead Stop 效果（HVF +30–50%，LVF −40–60%，最短 1.5–2.5 s，來源 VSUP-DB11），下游 SUP-D-C / 3A / 3B |
| FIX-SUPDB-03 | Inherited_Baseline V2A-07 補入「視頂蓋啟動潛伏期 30–50 ms」 |
| FIX-SUPDB-04 | V2A-11 全文加〔待驗證 2A 報告確認〕；VSUP-DB10 逃跑加速度描述移除 V2A-11 引用，改標「理論估算值」 |
| FIX-SUPDB-05 | Correction_Instructions 第 3 條改標題為「新增建議」，措辭從「[確認] V3A-03」改為「[新增] VSUP-DB11 推導值，V3A-03 確認待驗證」 |
| FIX-SUPDB-06 | Unresolved_Dependencies 補入第 4–6 條（instruction 優先缺口：M. salmoides 聲壓辨識實驗、LVF 行為遙測、Commit 加速度直接實測） |
| FIX-SUPDB-07 | 舊 VSUP-DB12（水質老化化學線索干擾）刪除，核心數值（2.0 m → <0.3 m）移入 VSUP-DB09 第 4 項附注；舊 VSUP-DB13 改編號 VSUP-DB12（总 Findings 12 條） |
| FIX-SUPDB-08 | Correction_Instructions 第 2 條移除 V3A-10（未定義 V-code） |
| FIX-SUPDB-09 | Correction_Instructions 第 1 條 Carry_Forward_To_2C 改為 Carry_Forward_To_2A |

### 待驗證項目（需對照上游報告）

| 項目 | 本卷使用值 | instruction 期望值 | 需確認報告 |
|------|-----------|-------------------|-----------|
| V2A-11 是否存在 | ≥1.5 m/s（Zone-A） | 指令未列此 V-code | 2A |
| V2A-07 速度閾值歸屬 | 1.2 m/s（V2A-07 一般基準） | 1.5–1.8 m/s（instruction 期望 V2A-07） | 2A |
| V3A-03 是否含 Dead Stop 計時 | 本卷標為「推導值」 | instruction 未列 V3A-03 含此數值 | 3A |

---

## SUP-D-C 卷完整稽核與後處理（2026-06-04）

**目標檔案**：`SUP-D-C_水中漂流偵測與策略切換.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：VSUP-DC01–14　**Carry_Forward 區塊**：5 組（Kármán 尾流頻率與攻擊率、各水體側線辨識距離、LVF vs HVF 觸發概率基線與衰退曲線、飼料印記消退參數、Match the Hatch 策略切換機制）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | 2 項結構性缺口：側線辨識距離未按各水體類型分列、LVF 衰退曲線缺中間數據點；Q5-3 範圍過寬風險（颱風/慈鯛仔魚易拉入 SUP-E）；LVF/HVF 概率預填值無上游引用 | 送修正 prompt |
| Round 2 | ✅ Go | 所有結構性缺口已補；Q5-3 明確限縮為純機制研究；V2A-05/06 引用確認交 Claude 後處理 | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 2 件（潛在） | Reaction Strike 潛伏期（12–25 ms vs instruction 預期 30–50 ms）；最小觸發速度（1.2 m/s vs instruction 預期 1.5–1.8 m/s）——兩者均對照 2A 報告後確認為真實值（詳見下方驗證表） |
| P2 輸出區塊 | ⚠️ 1 件 | LVF vs HVF Reaction Strike 基線差異（instruction 第 8 個必要核心數值）未以 VSUP-DC 獨立 Finding 呈現，僅繼承於 Inherited_Baseline |
| P3 引用鏈 | ⚠️ 5 件 | 第一條 V2A-06 應為 V2A-05（皮質醇 80–180 ng/mL）；V2A-05 91% 缺陷無正式 V-code 引用；孤兒引用：VSUP-DA09、VSUP-DB02、VSUP-DB03 未列入 Inherited_Baseline |
| P4 Scope | ✅ OK | 無嚴重越界；B0-10/11 未被任何 Finding 引用（冗餘，已清除） |
| P5 研究缺口 | ⚠️ 1 件 | 搜索映像 LTP 時間窗口（ms）直接電生理實驗值缺口未列為獨立 Unresolved 項目（instruction 優先列出項） |

**Phase 6 判定**：✅ 不需重跑（4 分）→ 直接 Claude 後處理

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-DC-01 | Inherited_Baseline 第一條 V2A-06 改標為 **V2A-05**，皮質醇值從 `>150 ng/mL` 修正為 `80–180 ng/mL`，補入「消退需 48–96 hr」（對照 2A 報告 V2A-05 實際內容） |
| FIX-DC-02 | Inherited_Baseline 新增 **VSUP-DA09**（台灣獵物水動力波：魚類 2–15 Hz / C-start 25–50 Hz / 蝦類 30–60 Hz） |
| FIX-DC-03 | Inherited_Baseline 新增 **VSUP-DB02**（靜止後 LVF 中止追擊 90%、HVF 45%、活蛙 25%）與 **VSUP-DB03**（LVF 拒絕率 75–90%；金屬閃光 85–95% > 線影 70–85% > 幾何對稱 50–65%） |
| FIX-DC-04 | Inherited_Baseline 移除 **B0-10**（H₂S）與 **B0-11**（DO 崩跌）——未被任何 Finding 引用的冗餘條目 |
| FIX-DC-05 | SUPDC_Findings 末尾新增 **[VSUP-DC14]**：LVF 15–30% vs HVF 65–80%，差距 35–65 個百分點，補齊 instruction 第 8 個必要核心數值 |
| FIX-DC-06 | Carry_Forward #3 更新：補入 HVF 基線 65–80%、LVF 基線 15–30%，來源新增 VSUP-DC14（基線）+ VSUP-DC09（衰退曲線） |
| FIX-DC-07 | Unresolved_Dependencies 新增第 5 項：**LTP 神經時間窗口（ms）直接電生理實驗值缺口** |

### 2A 報告驗證結果（解決 P1 潛在矛盾）

| 參數 | SUP-D-C 使用值 | 2A 實際 Finding | 結論 |
|------|---------------|----------------|------|
| Reaction Strike 潛伏期 | 12–25 ms（V2A-06） | V2A-06：12–25 ms（快速視覺通路，直接實驗證據） | ✅ 數值正確；instruction 預期 30–50 ms 為 fallback，非 2A 實際輸出 |
| 最小觸發速度 | Vcrit ≥ 1.2 m/s（V2A-07） | V2A-07：Vcrit ≥ 1.2 m/s（Zone-B 基準）| ✅ 數值正確；instruction 預期 1.5–1.8 m/s 為 Zone-A 閾值（V2A-11） |
| 皮質醇峰值 | 原標 V2A-06 >150 ng/mL | V2A-05：80–180 ng/mL | ✅ 已修正為 V2A-05（FIX-DC-01） |

### 不受影響的確認正確數值

- 活體蛙著水：100–300 Hz、95–105 dB、15–30 ms
- 落葉著水：>1000 Hz、<70 dB、無脈衝
- 硬式假餌著水：500–2000 Hz、115–125 dB、50–100 ms
- 追擊序列窗口：Detect 0–100 ms / Identify 100–500 ms / Approach 500 ms–2 s / Evaluate 2–5 s / Commit 5–5.1 s
- Commit 逃跑加速度閾值：≥2.5 m/s²
- Dead Stop：HVF +30–50%，LVF −40–60%，最短 1.5–2.5 s（推導值）
- LVF 學習過濾建立速度：3–5 次暴露後過濾率 +80%

---

## SUP-D-B 卷 v2 二次稽核後處理（2026-06-04）

**目標檔案**：`SUP-D-B_多模態獵物辨識與追擊序列.md`（Gemini 2 次校正後版本）
**執行流程**：twbass-audit 完整 5-Phase（Phase 6 included）→ Claude 後處理
**Phase 6 判定**：✅ 不需重跑（總分 4 分，Q 覆蓋完整型，所有 Core_Parameters 已有值）

### 5-Phase 稽核結果

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化一致性 | ⚠️ 6 件 | 禁詞 ×2、信心等級膨脹 ×4 |
| P2 輸出區塊 | ✅ OK | 5 必要區塊齊全，Findings 12 條在範圍內 |
| P3 引用鏈 | ⚠️ 4 件 | 數值缺源 ×2、Carry_Forward 命名含 2B 但無 2B 條目 ×1、外推物種未標 ×1 |
| P4 Scope | ✅ OK | 無嚴重越界 |
| P5 研究缺口 | ⚠️ 1 件 | Correction_Instructions 缺 3B 確認建議 |

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-SDB-01 | VSUP-DB02：「概率呈現顯著分化」→「概率在三類目標間相差 25%–98%，分化如下」（移除禁詞「顯著」） |
| FIX-SDB-02 | VSUP-DB11：「Dead Stop 創造了極佳的能量划算窗口」→ 替換為 OFT 追逐成本量化描述（移除禁詞「極佳」） |
| FIX-SDB-03 | VSUP-DB01 信心等級：高 → 中-高（理論估算+類比推估，缺 M. salmoides 直接數據） |
| FIX-SDB-04 | VSUP-DB05 信心等級：高 → 中-高（補標 Lepomis macrochirus 外推依據） |
| FIX-SDB-05 | VSUP-DB06 信心等級：高 → 中（Centrarchidae 類比推估） |
| FIX-SDB-06+10 | VSUP-DB12 信心等級：高 → 中-高（補標 Lepomis macrochirus 外推依據） |
| FIX-SDB-07 | VSUP-DB09：「清水 2.0 m」補標「理論估算，基於分子擴散係數與嗅覺偵測閾值模型」；範圍改為「1.5–2.5 m」 |
| FIX-SDB-08 | VSUP-DB11：「壁面無滑移梯度 60–80%，決策窗口 50%」補標「理論估算，no-slip 邊界條件與 CNs 加速度響應模型，缺直接實驗驗證」 |
| FIX-SDB-09 | Carry_Forward 新增第 8 條：輸往 2B，含著水主頻與掙扎剪切流頻率對 V2B-01/V2B-03 感知範圍的配對說明（VSUP-DB01、DB02） |
| FIX-SDB-11 | Correction_Instructions 新增第 4 條：3B Topwater 段落確認建議，涵蓋 VSUP-DB01/03/10/11 四組數值 |

---

## SUP-D-A 卷完整稽核與後處理（2026-06-04）

**目標檔案**：`SUP-D-A_食性選擇性與感官匹配優先序.md`
**執行流程**：gemini-plan-review（2 輪）→ twbass-audit 5-Phase → Claude 後處理
**最終 Findings 數**：VSUP-DA01–11　**Carry_Forward 區塊**：4 組（α 矩陣、NTU 閾值、獵物振動 Hz、LVF vs HVF 觸發率）

### Plan Review 輪次紀錄

| 輪次 | 信號 | 主要缺口 | 處置 |
|------|------|---------|------|
| Round 1 | ⚠️ Hold | 6 項結構性缺口：Q2.1 視覺維度排序、溫度/DO 選擇性抑制、Prey Switching 三維度、各獵物振動 Hz、振頻咬餌率比較、季節變化 | 送修正 prompt |
| Round 2 | ✅ Go | 全數 6 項補入；新增 2 條 scope guard（OFT 邊界、Prey Switching 不量化豐度閾值） | 進入執行 |

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化 | ⚠️ 4 件（待驗證） | V2A-07 潛伏期（30–50 ms vs 12–25 ms）、最小觸發速度（1.5–1.8 vs 1.2–1.5 m/s）、大肚魚能量密度（0.85 vs 1.10 kcal/g）、HVF 皮質醇（≈6 vs 10–15 ng/mL）；均需對照 2A/3A 原報告確認 |
| P2 輸出區塊 | ⚠️ 1 件 | CI 格式使用 file:// 本地連結 |
| P3 引用鏈 | ⚠️ 2 件 | CI-3 引用 VSUP-DA02（應為 V3A-02）；Inherited_Baseline 缺 V3A ART 溫度矩陣 |
| P4 Scope | ⚠️ 1 件 | CI-3 CFF 操餌速度修正屬 2A/2C 範疇，超出本卷 scope |
| P5 研究缺口 | ⚠️ 6 件 | 3 項 instruction 必列 Unresolved 完全缺失；Zone-B NTU 未明確標示；VSUP-DA02/DA07 信心等級標注偏高 |

**Phase 6 判定**：⚠️ Claude 結構重建（總分 15，結構分 100%，Q 覆蓋完整型）
所有缺口均為格式補充、引用訂正、Zone-B 注釋與 Unresolved 補條目，無需 Gemini 補研究。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-SDA-01 | Inherited_Baseline V2A-07 末尾加 ⚠️ 待驗證標注（潛伏期 fallback 30–50 ms vs 12–25 ms） |
| FIX-SDA-02 | Inherited_Baseline V2A-07 觸發速度待驗證標注（1.5–1.8 m/s vs VSUP-DA07 1.2–1.5 m/s） |
| FIX-SDA-03 | Inherited_Baseline V2A-02 末尾加 ⚠️ 待驗證標注（大肚魚 0.85 vs 1.10 kcal/g） |
| FIX-SDA-04 | Inherited_Baseline V3A-09 末尾加 ⚠️ 待驗證標注（HVF ≈6 vs 10–15 ng/mL） |
| FIX-SDA-05 | CI-1 / CI-2 格式修正：移除 file:// 本地連結，改為純文字段落描述 |
| FIX-SDA-06 | CI-3 引用訂正（隨 FIX-SDA-08 一併處理，CI-3 已移除） |
| FIX-SDA-07 | Inherited_Baseline 補入 V3A（VSUP-A04）ART 溫度矩陣（Q₁₀=2.0，20°C 基準 24.0 hr） |
| FIX-SDA-08 | 刪除 CI-3（CFF 操餌速度，Scope 超出本卷）；移至 Unresolved_Dependencies 第 7 條備忘，待 2C 後續稽核發出 CI-2C |
| FIX-SDA-09 | Unresolved_Dependencies 補入第 1 優先項：台灣管理池 LVF 魚實際食性選擇指數（缺胃內容物分析） |
| FIX-SDA-10 | Unresolved_Dependencies 補入第 2 優先項：M. salmoides 直接 Chesson's α 實測數據 |
| FIX-SDA-11 | Unresolved_Dependencies 補入第 3 優先項：台灣各濁度類型 NTU 閾值現場實測值 |
| FIX-SDA-12 | VSUP-DA08 水體標籤：腐植酸褐水（Zone-A）→（Zone-A/B）；Carry_Forward 第 2 項同步補 Zone-B 注釋 |
| FIX-SDA-13 | VSUP-DA02 信心等級：高 → 中（依據為類比推估，缺 M. salmoides 受控飢餓實驗） |
| FIX-SDA-14 | VSUP-DA07 信心等級：高 → 中（依據為理論估算，缺直接行為實驗驗證） |

### 待驗證項目（需對照上游報告）

| 項目 | 本卷使用值 | instruction fallback | 需確認報告 |
|------|-----------|---------------------|-----------|
| V2A-07 視頂蓋潛伏期 | 12–25 ms | 30–50 ms | 2A |
| V2A-07 最小觸發速度 | 1.2–1.5 m/s | 1.5–1.8 m/s | 2A |
| V2A-02 大肚魚能量密度 | 1.10 kcal/g | 0.85 kcal/g | 2A |
| V3A-09 HVF 皮質醇基線 | 10–15 ng/mL | ≈6 ng/mL | 3A |

### 不受影響的確認正確數值

- Chesson's α（常溫）：吳郭魚 0.65 / 大肚魚 0.25 / 蝌蚪 0.10
- 飢餓 5 天以上：α 全收斂至 0.33，E → 0.0
- NTU 視覺失效閾值：褐水（Zone-A/B）35 / 綠水（Zone-C）45 / 灰水 60 NTU
- 感官模式 100% 切換平均值：40 NTU（褐水 30 / 綠水 40 / 灰水 50）
- 魚類 C-start 振動 25–50 Hz / 蝦類 Tail-flip 30–60 Hz / 蝌蚪逃逸 8–12 Hz
- LVF 觸發率 15–30%；HVF 65–80%；相對減損 70–80%

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
- ~~重度 ART：6–8 hr（30°C）/ 24–30 hr（15°C）~~ → **已修正（見下方雙向引用稽核）**
- 連投間隔：≥ 3–5 min（30°C）/ ≥ 10–15 min（15°C）

---

## 3A 卷雙向引用稽核（2026-06-09）

**目標檔案**：`3A_高壓舊魚心理機制與誘咬本質.md`
**稽核範圍**：Inherited_Baseline（0D B0-XX + 1A V1A-XX + 2A V2A-XX + 2B V2B-XX）、Findings V3A-01~13、Carry_Forward_To_3B；SUP-A CI 套用確認；SUP-C Carry_Forward_To_3A 確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ⚠️ 3 件 | B0-CF-02/03 非標準 ID；4-tier ART tier 1（6.0 ng/mL 基線）誤標 12.0 hr → 應為 6.3 hr；"全場驚嚇" 6-8 hr/24-30 hr 使用 HVF 值而非 LVF 值 |
| P2 輸出區塊 | ✅ OK | Findings 13 條，Carry_Forward/Open_Assumptions 均完整 |
| P3 引用鏈 | ⚠️ 3 件 | B0-CF-02 × 2 處（Inherited + body text）；B0-CF-03 × 1 處；Open_Assumptions item 4 引用 Q₁₀ = 2.4，與正文 Q₁₀ = 2.0 矛盾 |
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ✅ OK | SUP-A VSUP-A09 已閉合 Open_Assumption 4；VSUP-C 確認 V3A-12 值正確 |

**Phase 6 判定**：✅ 不需重跑（SUP-A/C 均已確認 3A ART 數值正確性）

### Claude 後處理修改清單（雙向引用稽核，2026-06-09）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-3A-CITE-01 | Inherited_Baseline item B0-CF-02 | `B0-CF-02` → `B0-07`（冷氣團降溫熱惰性滯後，Zone-B 18-24 hr / Zone-A 17-23 hr / Zone-C 6-12 hr）[來源：0D-Baseline_Facts] |
| FIX-3A-CITE-02 | Inherited_Baseline item B0-CF-03 | `B0-CF-03` → `B0-18`（冷氣團後水溫回升物理 Lag，Zone-C 1.5-2.5 天 / Zone-B 3.0-4.0 天 / Zone-A 5.0-7.0 天）[來源：0D-Baseline_Facts] |
| FIX-3A-CITE-03 | Q3.4 body text | `B0-CF-02` → `B0-07` |
| FIX-3A-CITE-04 | Q3.1.3 四層級 ART tier 1（6.0 ng/mL 自然基準）| 30°C ART **12.0 hr** → **6.3 hr（正常範圍 6-8 hr）**；15°C ART → **21.7 hr（生理實質外推 36-42 hr）**（依據：VSUP-A07；此為 HVF 自然基準值，非 LVF 管理池老魚值） |
| FIX-3A-CITE-05 | Q3.2 "全場驚嚇" 正文 | "6–8 hr（夏季）或 24–30 hr（冬季）" → **"12.0 hr（夏季，30°C）或 36-42 hr（冬季，15°C）"**（LVF 高壓老魚值，依據：VSUP-A09, V3A-12） |
| FIX-3A-CITE-06 | Carry_Forward 4.1 急性應激閉口期 | "6–8 hr（30°C）；24–30 hr（15°C）" → **"12.0 hr（30°C）；36-42 hr（15°C）"**（引用 V3A-10, V3A-11；VSUP-A09 確認） |
| FIX-3A-CITE-07 | Open_Assumptions item 4 | "Q₁₀ = 2.4（Barton 2002）" → "Q₁₀ = 2.0（已由 VSUP-A09 確認）"；說明 ART 矩陣不確定性已解決，半衰期 6.2 hr 對應 Q₁₀ ≈ 2.28 的輕微偏差不影響 ART 矩陣 |
| FIX-3A-CITE-08 | Inherited_Baseline 新增第 5 節 | 補入 SUP-A 補充數值：VSUP-A06（LVF 慢性皮質醇 35-45 ng/mL 確認）、VSUP-A07（4-tier ART 動力學）、VSUP-A08（H₂S 行為覆蓋窗口 80-120 min）、VSUP-A09（ART 溫度矩陣對齊確認） |

### 修正後正確的 ART 值

| 魚隻類別 | 30°C ART | 15°C ART | 來源 |
|---------|---------|---------|------|
| 自然基準（HVF, 6.0 ng/mL 基線） | 6.3 hr（6-8 hr） | 21.7 hr → 36-42 hr | VSUP-A07 |
| LVF 輕度慢性（15 ng/mL） | 13.6 hr | 46.0 hr | VSUP-A07 |
| LVF 中度慢性（30 ng/mL，管理池典型） | 13.8 hr | 46.6 hr | VSUP-A07 |
| **VSUP-A09 標準 ART（LVF 模型）** | **12.0 hr** | **36-42 hr** | VSUP-A09, V3A-10 |
| 全場警報（LVF 舊魚，V3A-12） | **12.0 hr** | **36-42 hr** | V3A-12, VSUP-A09 |

**注意**：Carry_Forward 至 3B 的閉口期數值應使用 LVF 標準 ART（12.0 hr / 36-42 hr）。

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

## 3B 卷雙向引用稽核（2026-06-09）

**目標檔案**：`3B_極端情境高壓策略推演.md`
**稽核範圍**：Inherited_Baseline B0-XX / V1A-XX / V1B-XX / V2A-XX / V2B-XX / V3A-XX 引用正確性；SUP-A/B Carry_Forward_To_3B 接收確認；V3B-27 VSUP-B11 衝突狀態確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | V3A-10/V3A-11/V3B-12 ART 數值（36-42 hr at 15°C）與 VSUP-A09 一致 |
| P2 輸出區塊 | ⚠️ 1 件 | Inherited_Baseline 缺 SUP-A/B 兩節（V3B-13 引用 VSUP-A07、V3B-27 引用 VSUP-B11，但無對應 Inherited_Baseline 條目） |
| P3 引用鏈 | ⚠️ 7 件 | 5 個 "B0-XX/B0-CF-YY" 雙格式 ID（Inherited_Baseline）；V3B-09 body text B0-CF-02；V3B-24/25 body text B0-CF-11（×2）|
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ✅ OK | V3B-27 vs VSUP-B11 矛盾已解決（2026-06-04，memory 記錄確認） |

**V3B-27 衝突狀態**：✅ 已解決（VSUP-B11 方向確認：水車開啟後 H₂S 危險帶向上擴展，V3B-27「120-160 cm 瞬態」方向正確）

**Phase 6 判定**：✅ 不需重跑

### Claude 後處理修改清單（雙向引用稽核，2026-06-09）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-3B-CITE-01 | Inherited_Baseline 第 1 節（5 處）| "B0-04/B0-CF-08"→"B0-04"；"B0-07/B0-CF-02"→"B0-07"；"B0-12/B0-CF-05"→"B0-12"；"B0-16/B0-CF-10"→"B0-16"；"B0-17/B0-CF-11"→"B0-17" |
| FIX-3B-CITE-02 | V3B-09 機制來源 | `B0-CF-02` → `B0-07`（冷氣團底泥熱惰性保溫滯後） |
| FIX-3B-CITE-03 | V3B-24 / V3B-25 機制來源（×2） | `B0-CF-11` → `B0-17`（暴雨能見度恢復物理 Lag） |
| FIX-3B-CITE-04 | Inherited_Baseline 新增第 7/8 節 | 補入 SUP-A（VSUP-A06/07/09）與 SUP-B（VSUP-B11）Inherited_Baseline 條目，與 V3B-13/V3B-27 body text 引用對齊 |

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

## 4A 卷雙向引用稽核（2026-06-10）

**目標檔案**：`4A_繁衍地球化學與水文干擾.md`
**稽核範圍**：Inherited_Baseline B0-CF-XX 清理；SUP-B VSUP-B08 實際內容比對；V4A-05 B0-CF-01 修正

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ⚠️ 1 件 | Inherited_Baseline item 6「VSUP-B08：底棲 H₂S 廢棄巢穴死亡區半徑 r=1.6-2.3 m」與 SUP-B 實際 VSUP-B08 內容完全不符（VSUP-B08 為 Fe²⁺ 濃度垂直剖面，無此 r 值） |
| P2 輸出區塊 | ✅ OK | 區塊完整 |
| P3 引用鏈 | ⚠️ 3 件 | Item 5 標頭 B0-CF-01/02/03 非標準 ID；V4A-05 body text B0-CF-01；B0-07 引用缺失（熱慣性阻尼 18-24 hr 未標引用） |
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ✅ OK | |

**SUP-B CI 驗證**：SUP-B Correction_Instructions 針對 1B（Fe²⁺/H₂S 安全距離）與 3A（Schreckstoff 死區），無直接 4A-specific CI。VSUP-B08/09/11 值已確認（Fe²⁺ 梯度 + Fe²⁺ 成魚安全距離 + H₂S 成魚安全距離）。

**Phase 6 判定**：✅ 不需重跑

### Claude 後處理修改清單（雙向引用稽核，2026-06-10）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-4A-CITE-01 | Inherited_Baseline item 5 標頭 | "B0-CF-01, B0-CF-02, B0-CF-03, B0-18" → "B0-21, B0-07, B0-18"（B0-CF-01=B0-21 春季 12-18 天時序差；B0-CF-02=B0-07 熱慣性；B0-CF-03=B0-18 回升 Lag；消除重複的 B0-18） |
| FIX-4A-CITE-02 | V4A-05 body text | "引用 B0-CF-01" → "引用 B0-21"；補入 "B0-07" 引用（熱慣性保溫阻尼 18-24 hr） |
| FIX-4A-CITE-03 | Inherited_Baseline item 6 VSUP-B08 | 刪除虛假的「H₂S 廢棄巢穴死亡區半徑 r=1.6-2.3 m」（此值不存在於 SUP-B 任何 Finding）；改為正確的 VSUP-B08（Fe²⁺ 垂直濃度剖面）+ VSUP-B09（Fe²⁺ 成魚安全距離）+ VSUP-B11（H₂S 成魚安全距離）三條正確內容 |

### 虛假值確認

| 虛假引用 | 問題說明 |
|---------|---------|
| "VSUP-B08：H₂S 廢棄巢穴死亡區半徑 r=1.6-2.3 m" | VSUP-B08 實為 Fe²⁺ 濃度垂直剖面（Fick 第一定律解算），無橫向 H₂S 半徑概念；"r=1.6-2.3 m" 在 SUP-B 全文中不存在 |

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

---

## 3B V3B-02 SMR 數值修正（2026-06-08）

**目標檔案**：`3B_極端情境高壓策略推演.md`
**觸發原因**：V3B-02 原採用 SMR = 122.26 mg O₂/kg/hr，係由常溫基線依 Q₁₀=2.3 外推的急性高溫衝擊值（RMR 等級），不應作為觸發條件的馴化 SMR 使用。Díaz et al. (2007) 提供 *M. salmoides* 於 32°C 實際馴化條件下的 SMR 直接實測值 65.2 mg O₂/kg/hr，替換原外推值。

| FIX 編號 | 修改位置 | 原值 | 新值 |
|---------|---------|------|------|
| FIX-3B-R2-01 | V3B-02 觸發條件 SMR | 122.26 mg O₂/kg/hr（Q₁₀=2.3 外推 RMR） | 60–70 mg O₂/kg/hr（馴化 SMR；實測值 65.2 mg O₂/kg/hr，Díaz et al. 2007） |
| FIX-3B-R2-02 | V3B-02 機制來源 | `V1B-01`、`V2A-01` | `Díaz et al., 2007`、`V2A-01` |
| FIX-3B-R2-03 | V3B-02 信心等級 | 中（近緣物種類比推估） | 高（直接 *M. salmoides* 馴化實測） |
| FIX-3B-R2-04 | Unresolved_Dependencies 第 1 條 | 「SMR_32 = 122.26 mg O₂/kg/hr 係 Q₁₀=2.3 理論估算」 | 更新為「已採用 Díaz et al. 2007 馴化值 65.2 mg O₂/kg/hr；122.26 值為 Q₁₀=2.3 外推之 RMR/急性衝擊值，已廢棄」 |
| FIX-3B-R2-05 | 參考文獻 | 缺 Beamish 1970、Díaz et al. 2007 | 新增第 8 條（Beamish 1970）、第 11 條（Díaz et al. 2007）；原 8–18 條順延為 9–20 條 |

### 不受影響的核心數值

- V3B-02 Scope for Activity `<31 mg O₂/kg/hr`（降幅 >85%）維持不變（依 Díaz et al. 2007 好氧範圍上限計算，結論一致）
- V3B-02 操作規則（<15 cm/s、停頓 3.0–5.0 s）維持不變

---

## 4B 卷雙向引用稽核（2026-06-10）

**目標檔案**：`4B_棲位競爭、容載量與護巢防禦.md`
**稽核範圍**：Inherited_Baseline V1B-05/10/11 H₂S 引用正確性；VSUP-B08 虛假值清查；跨卷數值一致性

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ⚠️ 2 件 | (1) Inherited_Baseline V1B-05 行「VSUP-B06 覆蓋」標注錯誤——v2 VSUP-B06 實為 Schreckstoff C&R 等待時間，非 H₂S 安全距離；(2) H₂S 值「≥86 cm（上限 100 cm）」與 VSUP-B11 精算值 ~100 cm 不一致 |
| P2 輸出區塊 | ✅ OK | 無缺損 |
| P3 引用鏈 | ⚠️ 2 件 | (1) "[VSUP-B06 覆蓋...]" 應改為 "[VSUP-B11 確認...]"；(2) Inherited_Baseline VSUP-B08 備注項「H₂S 廢棄巢穴死亡區半徑 r=1.6-2.3 m」在 SUP-B 全文中不存在——VSUP-B08 實為 Fe²⁺ 垂直濃度剖面（與 4A 相同的虛假值） |
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ✅ OK | |

**B0-02 Cross_Volume_Boundaries 確認**：Zone-A 野生埤塘「春雨低溫陰雨熱遲滯（B0-02）」引用正確——B0-02 含三區春季熱遲滯量化值（Zone-A -1.2 to -2.2 °C/週），citation 無誤。

**Phase 6 判定**：✅ 不需重跑

### Claude 後處理修改清單（雙向引用稽核，2026-06-10）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-4B-CITE-01 | Inherited_Baseline B0-22 後備注項 | 刪除「[備注] VSUP-B08：H₂S 廢棄巢穴死亡區半徑 r=1.6-2.3 m」（此值在 SUP-B 全文中不存在；VSUP-B08 實為 Fe²⁺ 垂直濃度剖面）；改為正確的 VSUP-B11 H₂S 安全距離數值（Stagnant ~100 cm；Mixed 低端 186.8 cm） |
| FIX-4B-CITE-02 | Inherited_Baseline V1B-05/10/11 行（原 FIX-4B-07 更新） | "[VSUP-B06 覆蓋 V1B-05 舊下限 60 cm，舊值廢棄]" → "[VSUP-B11 確認；舊值 ≥86 cm 廢棄]"；H₂S 值 "≥86 cm（上限 100 cm）" → "~100 cm（靜水 Stagnant 精算 99.7–100.0 cm）" |
| FIX-4B-CITE-03 | V4B-09 有效防禦半徑注釋 | "V1B-05 Zone-C H₂S 化學安全高度 ≥86 cm" → "V1B-10 Zone-C H₂S 化學安全高度 **~100 cm**（VSUP-B11 精算；舊值 V1B-05 ≥86 cm 已廢棄）" |
| FIX-4B-CITE-04 | Inherited_Baseline V1B-04 描述行（補完，2026-06-10） | "黑鱸垂直向上避毒位移 60–100 cm" → "黑鱸垂直向上避毒至安全高度 **~100 cm**（精算 99.7–100.0 cm，VSUP-B11；原估 60–100 cm 廢棄）"（V1B-04 在 1B 本文已同步更新，3B 已修正，4B 本次補完） |

### 虛假值確認

| 虛假引用 | 問題說明 |
|---------|---------|
| "VSUP-B08：H₂S 廢棄巢穴死亡區半徑 r=1.6-2.3 m"（4B 備注項） | 與 4A 同一虛假值：VSUP-B08 實為 Fe²⁺ 濃度垂直剖面（Fick 第一定律解算）；r=1.6-2.3 m 在 SUP-B 全文任何 Finding 中均不存在 |
| VSUP-B06 作為 H₂S 安全距離來源 | v2 VSUP-B06 = Schreckstoff C&R 等待時間（10-15 min 北部 / 30-45 min 南部）；H₂S 安全距離精算在 VSUP-B11 |

---

## 1B 卷雙向引用稽核（2026-06-10）

**目標檔案**：`1B_六大水域棲位模型與風生流.md`
**稽核範圍**：SUP-B CI-01~06 套用確認（V1B-CF-04 Fe²⁺ 修正 + V1B-10 H₂S 精算）；Inherited_Baseline B0-XX 標準化確認；Carry_Forward 數值一致性

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ⚠️ 2 件 | (1) V1B-10 body text「60 至 100 cm」與 VSUP-B11 精算值 ~100 cm 不一致（V1B-CF-03 已正確更新，V1B-10 本文未同步）；(2) V1B-CF-04 Zone-C H₂S「60–100 cm」與底部注釋「99.7–100.0 cm」自相矛盾 |
| P2 輸出區塊 | ✅ OK | Inherited_Baseline / Findings / Carry_Forward / Unresolved 完整 |
| P3 引用鏈 | ✅ OK | Inherited_Baseline 全部使用標準 B0-XX 格式（無 B0-CF-XX 非標準 ID）；V1B-CF-04 已含「[修正，VSUP-B09]」標注 |
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 3 條已標注 |

**SUP-B CI 套用狀態**：
- V1B-CF-04 Fe²⁺ 北部（VSUP-B09）：✅ 已套用（Zone-B 25.7–32.7 cm；Zone-A 56.5–67.2 cm）
- V1B-CF-03 H₂S 停機情境（VSUP-B11）：✅ 已套用（Stagnant 99.7–100.0 cm；h=150 cm→149.0 cm）
- V1B-CF-04 Zone-C H₂S（VSUP-B11）：⚠️ 未完全套用（注釋有值但主文未更新）
- V1B-10 body H₂S 精算（VSUP-B11）：⚠️ 未套用（仍顯示 60–100 cm 原估）
- V1B-11 Fe²⁺ 閾值（VSUP-B09）：✅ 已套用（0.10 mg/L 行為避忌；標注「[修正，VSUP-B09]」）

**Phase 6 判定**：✅ 不需重跑

### Claude 後處理修改清單（雙向引用稽核，2026-06-10）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-1B-CITE-01 | V1B-10 安全距離結論句 | "至少 **60 至 100 cm** 的最小安全高度（本卷 V1B-10 擴散模型計算值）" → "至少 **~100 cm** 的最小安全高度（V1B-10 初估 60–100 cm；VSUP-B11 採嚴格閾值 0.002 mg/L 精算，Stagnant h=100 cm 確認 **99.7–100.0 cm**）" |
| FIX-1B-CITE-02 | V1B-CF-04 Zone-C H₂S 主文 | "南部（Zone-C）底泥 H₂S 安全高度 **60–100 cm**" → "南部（Zone-C）底泥 H₂S 安全高度 **~100 cm**（精算 99.7–100.0 cm，VSUP-B11；原估 60–100 cm 廢棄）" |

> **套用狀態確認（2026-06-10）**：FIX-1B-CITE-02 → V1B-CF-04 已正確套用（line 170 已為 ~100 cm），無需重改。FIX-1B-CITE-01 及新發現問題實際套用：
>
> | 實際套用 FIX | 修改位置 | 修改內容 |
> |---------|---------|---------|
> | FIX-1B-CITE-01（實際套用） | V1B-10 finding line 130「60–100 cm」 | 改為 "**~100 cm**（精算 99.7–100.0 cm，VSUP-B11；原估 60–100 cm 廢棄）" |
> | FIX-1B-NEW-01 | V1B-05 finding line 68「避毒高度達 60–100 cm」 | 改為 "避毒高度達 **~100 cm**（精算 99.7–100.0 cm，VSUP-B11；原估 60–100 cm 廢棄）" |

---

## SUP-C Carry_Forward 補接（3A + 3B，2026-06-10）

**觸發原因**：雙向引用稽核發現 SUP-C Carry_Forward_To_3A_3B 的 4 組量化參數（低氧迴避閾值、冒險覓食觸發條件、靜止容忍特徵、皮質醇抑制閾值）在 3A 和 3B 的 Inherited_Baseline 中均未出現任何 VSUP-C 引用，屬於遺漏接收。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-3A-SUPC | 3A Inherited_Baseline 末端 | 新增 **Section 6（毒區迴避與冒險覓食決策，引用自卷 SUP-C）**：VSUP-C03（低氧閾值 2.2-2.5/1.5-1.8 mg/L, H₂S 0.002 mg/L）、VSUP-C05（獵物密度觸發 ≥3.5×, 飢餓後 2.0-2.5×）、VSUP-C10（皮質醇 >150 ng/mL 阻斷; LVF 20-40 ng/mL → 觸發門檻升 ≥6.0×）|
| FIX-3B-SUPC | 3B Inherited_Baseline 末端 | 新增 **Section 9（毒區迴避與冒險覓食決策，引用自卷 SUP-C）**：VSUP-C01/03（低氧迴避）+ VSUP-C04/05/07（Foraging Forays 全套觸發條件）+ VSUP-C02/11（靜止容忍）+ VSUP-C10（皮質醇抑制）|

---

## 0A 卷雙向引用稽核與後處理（2026-06-05）

**目標檔案**：`0A_台灣四季氣候 forcing 與區域差異.md`
**執行流程**：twbass-audit 5-Phase（雙向引用稽核輪）→ Claude 後處理
**最終 Findings 數**：V0A-01–11（不變）　**修正項目**：2 條

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化一致性 | ✅ OK | 所有 Core_Parameters 均有三區量化值，無模糊描述 |
| P2 輸出區塊 | ⚠️ 1 件 | `Unresolved_Dependencies` 區塊缺失（instruction §八要求）；內容已隱含於 Open_Assumptions |
| P3 引用鏈 | ✅ OK | CF0A-01~08 全部引用來源 V0A-XX 存在 |
| P4 Scope | ✅ OK | 無越界（0B/0C 跨卷指向均為指引說明，非核心發現） |
| P5 研究缺口 | ⚠️ 1 件 | Zone-B 春季遲滯率（-0.6 to -1.1 °C/週）存在主文但未收入任何 Finding；CF0A-02 錯誤標注同一數值適用 Zone-A 及 Zone-B |

**Phase 6 判定**：✅ 不需重跑（2 分）。Claude 後處理即可。

### Claude 後處理修改清單

| FIX 編號 | 修改內容 |
|---------|---------|
| FIX-0A-01 | Open_Assumptions_0A 末段後補充獨立 `Unresolved_Dependencies` 區塊（缺口 1：τ_crit 實測值，影響 0C/0D；缺口 2：Zone-C 輻射冷卻極端低溫頻率分布，影響 0C/0D）|
| FIX-0A-02 | V0A-03 補入三區分列遲滯率：Zone-A **-1.2 to -2.2 °C/週**；Zone-B **-0.6 to -1.1 °C/週**；Zone-C **< -0.1 °C/週**（可忽略）；CF0A-02 同步更新為三區分列格式，移除「適用於 Zone-A 及 Zone-B 同一數值」之錯誤標注 |

### 不受影響的確認正確數值

- V0A-04：Zone-B 春季 22°C 跨越提前 12–18 天
- V0A-06：颱風直接風應力 0.915–2.342 Pa；間接 0.146–0.586 Pa
- V0A-08：冷氣團降幅 Zone-A 4.8–6.2°C / Zone-B 5.2–6.8°C / Zone-C 2.2–4.2°C
- V0A-09：回溫天數 Zone-A 3.8 天 / Zone-B 3.0 天 / Zone-C 2.2 天
- V0A-10：Zone-C 旱季蒸發赤字 -415.3 mm
- V0A-05：梅雨水量替換率 7.5–33.2%/day

---

## 0B 卷雙向引用稽核與後處理（2026-06-09）

**目標檔案**：`0B_南北成土母質與地球化學基底.md`
**執行流程**：twbass-audit 5-Phase（雙向引用稽核輪）→ Claude 後處理
**最終 Findings 數**：V0B-01–12（不變）　**修正項目**：3 條

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化一致性 | ✅ OK | Stokes Law 計算、Cv 計算、蒸發濃縮倍率全部驗算正確；Q₁₀ = 2.2–2.6 vs 加速倍率 2.2–2.8× 輕微內部不一致，不影響下游傳遞值，列觀察項 |
| P2 輸出區塊 | ⚠️ 1 件 | `Inherited_Baseline` 區塊缺失（最上游層應標注「無上游引用」）|
| P3 引用鏈 | ⚠️ 1 件 | CF0B-06 傳遞「北部 = 3.411 J/(cm³·K)」，但 Zone-A（台北/宜蘭）正確值為 3.215，應三區分列；V0B-12 中 Zone-A 值亦缺失 |
| P4 Scope | ✅ OK | 無魚類行為、氣候 forcing、六大水體季節評估越界 |
| P5 研究缺口 | ✅ OK | Open_Assumptions 與 Unresolved_Dependencies 合理標注；野生埤塘 SRR 原位數據缺口已明確 |

**Phase 6 判定**：✅ 不需重跑（3 分）。Claude 後處理即可。

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-0B-01 | 報告正文（Inherited_Baseline 區塊） | 在標題後、第一節前新增 `Inherited_Baseline` 區塊，標注「本卷為最上游層，無上游引用（B0-XX / V-XX）」|
| FIX-0B-02 | V0B-12 Finding | 原文僅列「北部（孔隙率 60%）= 3.411」與「南部 = 3.122」；補入 Zone-A（孔隙率 50%，文獻估算）= **3.215 J/(cm³·K)**；補入 Zone-A vs Zone-C 差異：熱容高 2.98%、溫度波動幅度小 2.89% |
| FIX-0B-03 | CF0B-06 | 將「北部 = 3.411，南部 = 3.122」更新為三區分列：Zone-B **3.411**、Zone-A **3.215**（文獻估算）、Zone-C **3.122**；補入 Zone-A 阻尼係數 **+2.98%**，調整標題為「三區底泥多孔介質體積熱容」|

### 不受影響的確認正確數值

- V0B-01：Zone-B 黏粒含量 42.3%–53.8%（高嶺石 58%–67%）
- V0B-02：Zone-B Fe_d 48.5–124.0 g/kg；磷最大固定量 780–1,250 mg P/kg
- V0B-04：Stokes 2 μm→102.9 hr / 20 μm→1.03 hr；100× 放大
- V0B-07：保守離子濃縮 1.88×；TP 濃縮 1.18–1.38×
- V0B-08：Eh 逆轉 5–9 天（+450 → -100 to -220 mV）
- V0B-09：各還原帶建立時序（1–2 / 3–5 / 7–12 天）；鐵還原速率 5.0–18.0 mmol/m²/day
- V0B-10：Q₁₀ = 2.2–2.6；夏季加速 2.2–2.8×（以 Q₁₀ = 2.4 擬合）
- V0B-11：Zone-C H₂S = 0.15–0.85 mg/L（亞鐵屏障耗盡後）
- V0B-12（修正後）：Zone-B = 3.411 / Zone-A = 3.215 / Zone-C = 3.122 J/(cm³·K)

---

## 0C 卷雙向引用稽核與後處理（2026-06-09）

**目標檔案**：`0C_六大水體 seasonal 評估.md`
**執行流程**：twbass-audit 5-Phase（雙向引用稽核輪）→ Claude 後處理
**最終 Findings 數**：V0C-01–14（不變）　**修正項目**：5 條

### 5-Phase 稽核結果

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化一致性 | ✅ OK | 所有數值計算正確；Zone-A 熱阻 2.98%/2.89%（與 FIX-0B 修正後一致） |
| P2 輸出區塊 | ✅ OK | Inherited_Baseline、V0C-01~14、CF0C-01~16、Open_Assumptions（5 條）、Unresolved_Dependencies（3 條）齊全 |
| P3 引用鏈 | ⚠️ 6 件 | Inherited_Baseline 中 V0B 引用多處錯位；正文兩處引用錯誤 Finding ID |
| P4 Scope | ✅ OK | 無魚類行為越界 |
| P5 研究缺口 | ✅ OK | 缺口合理標注，不影響下游必要傳遞值 |

**Phase 6 判定**：✅ 不需重跑（P3 純結構/引用 ID 修補，數值正確）。Claude 後處理即可。

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 問題描述 | 修正方向 |
|---------|---------|---------|---------|
| FIX-0C-01 | Inherited_Baseline V0A-03 | 僅列 Zone-A 遲滯率 -1.2 to -2.2 °C/週，缺 Zone-B（-0.6 to -1.1）和 Zone-C（< -0.1） | 更新為三區分列（繼承 FIX-0A-02 修正結果）|
| FIX-0C-02 | Inherited_Baseline V0B 區塊 | V0B-02 誤含 Zone-C Fe_d 資料（屬 V0B-06）；V0B-06 誤描述 Eh 逆轉（屬 V0B-08）和 Q₁₀（屬 V0B-10）；V0B-07 出現非 V0B-07 的絕對 TP 值；V0B-10 誤描述鐵還原速率（屬 V0B-09）；缺 V0B-03、V0B-04、V0B-08、V0B-09 條目 | 重寫整個 V0B Inherited_Baseline 區塊，補入 V0B-03/04/08/09，修正各條描述與來源 |
| FIX-0C-03 | Waterbody-1 季節表 春季欄 | 春雨遲滯僅顯示 Zone-A 值（-1.2 to -2.2 °C/週），未分列 Zone-B（-0.6 to -1.1 °C/週） | 補入 Zone-B 值 |
| FIX-0C-04 | 正文 Waterbody-4（南部野生埤塘） | Eh 逆轉條件引用「（V0B-06）」→ V0B-06 是磷固定量，應為 V0B-08 | 改為（V0B-08）|
| FIX-0C-05 | 正文 Waterbody-6（南部管理池） | Zone-C Fe_d 引用「（V0B-02）」→ V0B-02 是 Zone-B 數據，應為 V0B-06 | 改為（V0B-06）|

### 不受影響的確認正確數值

- V0C-01：北部暴雨澄清 1–2 天；南部澄清 5–8 天
- V0C-02：Zone-B 熱阻 18–24 hr；Zone-A 17–23 hr；Zone-C 6–12 hr；三區 Cv 正確
- V0C-05：南部春雨回淹釋磷 25–45 μg/L；Eh 5–9 天逆轉（數值正確，引用 ID 已修正）
- V0C-06/07：深水水庫翻轉臨界及南北時序差
- V0C-09：南部春末藻華能見度驟降值
- CF0C-01~16：全部 Carry_Forward 數值正確

---

## 卷 0D 雙向引用稽核（2026-06-09）

**目標檔案**：`0D_基底資料矩陣與極端事件整合.md`
**稽核範圍**：Inherited_Baseline（0A/0B/0C）、Baseline_Facts B0-01~22、Carry_Forward、Open_Assumptions

### 稽核結果摘要

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化矛盾 | ⚠️ 2 件 | V0A-03/B0-02 僅列 Zone-A 熱遲滯值；V0B-02 誤含 Zone-C Fe_d 資料 |
| P2 輸出區塊 | ⚠️ 1 件 | Baseline_Facts 標頭宣稱「19 條」，實際為 22 條 |
| P3 引用鏈 | ⚠️ 2 件 | B0-05 引用漏 V0B-06；V0B-06/V0B-07 未列入 Inherited_Baseline |
| P4 Scope 違規 | ✅ OK | — |
| P5 研究缺口 | ✅ OK | Open_Assumptions 3 項已適當標注 |

**Phase 6 判定**：✅ 不需重跑（純引用 ID 與三區補全，數值主體正確）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 問題描述 | 修正方向 |
|---------|---------|---------|---------|
| FIX-0D-01 | Inherited_Baseline V0A-03 | 僅列 Zone-A 熱遲滯率（-1.2 to -2.2 °C/週），缺 Zone-B（-0.6 to -1.1）和 Zone-C（<-0.1） | 更新為三區分列（繼承 FIX-0A-02 修正結果）|
| FIX-0D-02 | Inherited_Baseline V0B 區塊 | V0B-02 誤含 Zone-C Fe_d 資料（屬 V0B-06）；V0B-06 和 V0B-07 完全缺漏 | 修正 V0B-02 僅保留 Zone-B 資料；補入 V0B-06（Zone-C Fe_d）與 V0B-07（濃縮倍率）條目 |
| FIX-0D-03 | B0-02 Baseline Fact | 熱遲滯值「-1.2 to -2.2 °C/週」未標明僅為 Zone-A，缺 Zone-B/C 三區分列 | 改為三區分列：Zone-A -1.2 to -2.2；Zone-B -0.6 to -1.1；Zone-C <-0.1 °C/週 |
| FIX-0D-04 | B0-05 Baseline Fact 引用 | `[V0B-01, V0B-02]` — Zone-C Fe_d 資料來自 V0B-06，引用未列 | 改為 `[V0B-01, V0B-02, V0B-06]` |
| FIX-0D-05 | Baseline_Facts 區塊標頭 | 「以下為本冊輸出的 19 條…」實際 B0-01~22 共 22 條 | 改為 22 條 |

### 不受影響的確認正確數值

- B0-03~B0-04、B0-06~B0-19：量化值與引用 ID 均正確
- B0-07：三區體積熱容（Zone-B 3.411、Zone-A 3.215、Zone-C 3.122 J/(cm³·K)）正確
- B0-08/B0-09：Zone-C Eh 逆轉（5-9 天降至 -100 to -220 mV）、還原帶時序正確
- B0-20~B0-22：Zone-B 22°C 超前量、Eh 首觸時間正確
- Waterbody_Model_Table：8 水體三區分列均正確
- Carry_Forward B0-CF-01~12：全部數值正確

---

## 卷 1A 雙向引用稽核（2026-06-09）

**目標檔案**：`1A_短時間環境觸發與生理限制.md`
**稽核範圍**：Inherited_Baseline（0D B0-XX）、Findings V1A-01~12、Carry_Forward_To_3A/3B

### 稽核結果摘要

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化矛盾 | ⚠️ 2 件 | B0-07 Zone-A/B 保溫滯後合併為「17–24 hr」；B0-09 Q₁₀ 引用 2.4（單值）而 B0-09 原文為 2.2–2.6 |
| P2 輸出區塊 | ✅ OK | Inherited_Baseline/Findings/Carry_Forward/Unresolved_Dependencies 均存在 |
| P3 引用鏈 | ⚠️ 3 件 | Inherited_Baseline B0-04 描述夏季水溫（非 B0-04 內容）；引用 B0-11 用於 53 hPa 氣壓降（B0-11 是 DO 崩潰時間）；intro「B0-01 至 B0-19」應為 B0-22 |
| P4 Scope 違規 | ✅ OK | — |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 2 項已適當標注 |

**Phase 6 判定**：✅ 不需重跑（純引用 ID/三區補全/數值範圍修正，研究內容正確）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 問題描述 | 修正方向 |
|---------|---------|---------|---------|
| FIX-1A-01 | Inherited_Baseline B0-07 | 「17–24 hr」合併 Zone-A（17-23）與 Zone-B（18-24）；缺 Zone-C（6-12 hr）分列 | 改為三區分列：Zone-B 18-24 hr；Zone-A 17-23 hr；Zone-C 6-12 hr |
| FIX-1A-02 | Inherited_Baseline B0-09 | 引用「Q₁₀ = 2.4」（單值），但 B0-09 原文為「Q₁₀ = 2.2–2.6」範圍值 | 改為 Q₁₀ = 2.2–2.6，計算使用中值 2.4 |
| FIX-1A-03 | Inherited_Baseline B0-04 | 描述「南部水體夏季水溫 28–32°C」但 B0-04 是旱季蒸發濃縮內容 | 改引 B0-11（明確記載「夏季 30–32°C」的管理池 DO 崩潰條目）|
| FIX-1A-04 | 正文第一章開頭（53 hPa 計算） | 「氣壓降幅達 53 hPa，見 B0-11」— B0-11 是 DO 崩潰時間，非氣壓資料 | 移除 B0-11 引用，53 hPa 作為颱風通用物理參數直接陳述 |
| FIX-1A-05 | Intro 正文第二段 | 「B0-01 至 B0-19」—0D 現為 22 條（B0-22） | 改為「B0-01 至 B0-22」|

### 不受影響的確認正確數值

- V1A-01~V1A-12：所有 Findings 數值（CH₄ 氣泡速度、H₂S 閾值 0.05 mg/L、魚鰾膨脹計算、Lockjaw 時序）正確
- B0-06：酸性絮凝澄清時間（北部 24-48 hr；南部 5-8 天）正確
- B0-10：H₂S 峰值 0.15–0.85 mg/L；北部 <0.02 mg/L 正確
- B0-12：深水水庫翻轉條件（ΔT ≥6.0-8.0°C；U ≥6.5-8.5 m/s；36-48 hr）正確
- Carry_Forward_To_3A/3B 引用 V1A 編號和數值均正確

---

## 卷 1B 雙向引用稽核（2026-06-09）

**目標檔案**：`1B_六大水域棲位模型與風生流.md`
**稽核範圍**：Inherited_Baseline（0D B0-XX）、Findings V1B-01~13、Carry_Forward_To_3B/4B；SUP-B CI-01/02 套用確認

### 稽核結果摘要

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化矛盾 | ⚠️ 1 件 | B0-02 熱遲滯只列 Zone-A (-1.2 to -2.2 °C/週)；SUP-B CI-01/02 尚未套用（Fe²⁺ 閾值/安全距離需更新）|
| P2 輸出區塊 | ✅ OK | Inherited_Baseline/Findings/Carry_Forward/Unresolved_Dependencies 均存在 |
| P3 引用鏈 | ⚠️ 2 件 | SUP-B CI 對 V1B-11（閾值）與 V1B-CF-04（北部安全距離）尚未套用 |
| P4 Scope 違規 | ✅ OK | — |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 3 項已適當標注 |

**Phase 6 判定**：✅ 不需重跑（P1/P3 均為數值修補，Research content 正確）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 問題描述 | 修正方向 |
|---------|---------|---------|---------|
| FIX-1B-01 | Inherited_Baseline B0-02 | 熱遲滯僅列 Zone-A（-1.2 to -2.2 °C/週），缺 Zone-B/C 三區分列 | 更新為三區分列：Zone-A -1.2~-2.2；Zone-B -0.6~-1.1；Zone-C <-0.1 °C/週 |
| FIX-1B-02 | V1B-11（Fe²⁺ 閾值）| 「亞致死避忌閾值 0.5 mg/L」；SUP-B 精算後應為 鰓損傷 0.35 mg/L / 行為避忌 0.10 mg/L | 更新閾值，標注 [修正，VSUP-B09] |
| FIX-1B-03 | V1B-CF-04（北部 Fe²⁺ 安全距離）| 「北部無排除帶，10-20 cm」；SUP-B 確認北部確有排除帶 | 更新為 Zone-B 25.7-32.7 cm；Zone-A 56.5-67.2 cm，標注 [修正，VSUP-B09] |
| FIX-1B-04 | V1B-CF-03（南部 H₂S 安全距離細化）| 缺深水槽情境（h=150 cm）VSUP-B11 細化資料 | 補入 Stagnant h=150 cm 深槽：行為避忌 149.0 cm，標注 [細化，VSUP-B11] |

### 不受影響的確認正確數值

- V1B-01~V1B-09：所有季節棲位深度範圍、異重流計算、翻水臨界條件正確
- V1B-10：南部 H₂S 安全距離 60-100 cm（由 VSUP-B11 確認上界 100 cm 正確）
- V1B-12/13：風生流速 9.0-18.0 cm/s、迎風岸富集範圍 3-15 m、OFT 切換 20 cm/s 正確
- Carry_Forward_To_4B（V1B-CF-08~10）：底質偏好排序與化學屏障對比值正確

---

## 卷 2A 雙向引用稽核（2026-06-09）

**目標檔案**：`2A_覓食偏好、印記與反射咬餌.md`
**稽核範圍**：Inherited_Baseline（0D B0-XX + 1A V1A-XX）、Findings V2A-01~12、Carry_Forward_To_2C/3A_3B；SUP-D-A CI + CI-SUPE-01 套用確認

### 稽核結果摘要

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化矛盾 | ⚠️ 1 件 | B0-CF-02 為非標準 ID（應為 B0-07）；Carry_Forward 也引用錯誤 ID |
| P2 輸出區塊 | ✅ OK | 全部輸出區塊存在，Findings 12 條齊全 |
| P3 引用鏈 | ⚠️ 3 件 | B0-CF-02 不存在；SUP-D-A CI（V2A-12 NTU補充）未套用；CI-SUPE-01（V2A-01 軟殼蝦補充）未套用 |
| P4 Scope 違規 | ✅ OK | — |
| P5 研究缺口 | ✅ OK | 3 項 Unresolved_Dependencies 已正確標注 |

**Phase 6 判定**：✅ 不需重跑（均為補充數值，研究主體正確）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 問題描述 | 修正方向 |
|---------|---------|---------|---------|
| FIX-2A-01 | Inherited_Baseline 第 3 條 + Carry_Forward_To_3B 引用 | 「B0-CF-02」為非標準混合 ID，不存在於 0D Baseline_Facts 命名體系 | 改為正確 ID「B0-07」；來源標注改為「0D-Baseline_Facts」 |
| FIX-2A-02 | V2A-12（視覺失效臨界）| 僅有 SD ≤ 15 cm 指標；SUP-D-A CI 指示補充 NTU 對應閾值 | 補入 VSUP-DA08 NTU 閾值：褐水 35 NTU；綠水 45 NTU；灰水 60 NTU；平均切換點 40 NTU |
| FIX-2A-03 | V2A-01（OFT 能效矩陣）| 日本沼蝦僅列一般個體 0.034 kcal/s；CI-SUPE-01 指示補充軟殼/抱卵母蝦 | 補入：軟殼個體 0.25–0.45 kcal/s（$T_h$ 降至 0.2 s）；抱卵母蝦 1.15 kcal/g（來源：VSUP-E06, E07） |
| FIX-2A-04 | Carry_Forward_To_3A_3B 第 4 項 | 缺 VSUP-E25 OFT 選擇性切換門檻（3A/3B 需要）| 補入切換閾值：相對豐度 65%–80% 或 ≥2.5 enc/min；低溫（<18°C）切換閾值升至 >90% |

### 不受影響的確認正確數值

- V2A-02~V2A-12（修正前）：所有神經通路、臨界速度、波長衰減係數數值正確
- V1A-06/10/11/12 在 Inherited_Baseline 的三區視距值正確（28/36/40 cm）
- Carry_Forward_To_2C：斯涅爾窗視距矩陣（28/36/40/120 cm 高對比值）正確
- B0-06、B0-11 引用數值正確

---

## 卷 2B 雙向引用稽核（2026-06-09）

**目標檔案**：`2B_側線、內耳與水下聲學傳遞.md`
**稽核範圍**：Inherited_Baseline（0D B0-XX）、Findings V2B-01~13、Carry_Forward_To_3A_3B；B0-CF-XX 混合 ID 修正

### 稽核結果摘要

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化矛盾 | ⚠️ 5 件 | B0-CF-02/04/05/08 均為非標準 ID；B0-04 引用錯誤（內容為春末藻華，應為 B0-15） |
| P2 輸出區塊 | ✅ OK | Findings 13 條，Carry_Forward/Open_Assumptions/Unresolved_Dependencies 均存在 |
| P3 引用鏈 | ⚠️ 9 處 | B0-CF-XX 出現在 Inherited_Baseline、V2B-09、正文段落、Carry_Forward 共 9 處需修正 |
| P4 Scope 違規 | ✅ OK | — |
| P5 研究缺口 | ✅ OK | 2 項 Unresolved_Dependencies 已標注 |

**Phase 6 判定**：✅ 不需重跑（均為 ID 格式修正，無內容缺失）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 問題描述 | 修正方向 |
|---------|---------|---------|---------|
| FIX-2B-01 | Inherited_Baseline（4 條）| B0-04/B0-CF-08, B0-06/B0-CF-04, B0-07/B0-CF-02, B0-12/B0-CF-05 均含非標準混合 ID | B0-04→B0-15（春末藻華應引用 B0-15）；其餘 /B0-CF-XX 部分全部移除；B0-12 補入 B0-14（中層異重流深度） |
| FIX-2B-02 | 第六章正文 EPS 黏度描述 | "`B0-CF-08`" 非標準 ID | 改為 "`B0-15`" |
| FIX-2B-03 | V2B-09 Finding 括號引用 | "（B0-04, B0-CF-08）" 雙重錯誤 | 改為 "（B0-15）" |
| FIX-2B-04 | Carry_Forward 第 1 項（濁水感官切換）| "`B0-CF-04`" 非標準 | 改為 "`B0-06`" |
| FIX-2B-05 | Carry_Forward 第 2 項（南部藻華假餌頻率）| "`B0-CF-08`" 非標準 | 改為 "`B0-15`" |
| FIX-2B-06 | Carry_Forward 第 4 項（聲折射棲位戰術）| "`B0-CF-05`" 非標準 | 改為 "`B0-14`"（中層異重流深度 8.5–18.2 m 出自 B0-14） |

### 不受影響的確認正確數值

- V2B-01~V2B-13：所有側線頻率響應、聲速、阻抗、衰減斜率、有效距離數值正確
- B0-03（冷氣團降溫幅度）、B0-15（春末藻華持續天數）引用後均正確
- 假餌比較表中 Zone-A/B 合併說明已標注「待 v2 re-run 拆分」為合規標注

---

## 卷 2C 雙向引用稽核（2026-06-09）

**目標檔案**：`2C_視線軸向、攻擊角度與假餌操作.md`
**稽核範圍**：Inherited_Baseline（0D B0-XX + 1A V1A-XX + 2A V2A-XX + 2B V2B-XX）、Findings V2C-01~12、Carry_Forward_To_3A_3B

### 稽核結果摘要

| Phase | 結果 | 發現數 |
|-------|------|-------|
| P1 量化矛盾 | ✅ OK | 所有數值與上游吻合：視距矩陣（28/36/40/120 cm Zone A/B/C/水庫高對比），Reaction Strike 速度（1.5/1.2/1.1/1.0 m/s），DO 門檻（2.5/2.8/3.0 mg/L 三區分列）均正確 |
| P2 輸出區塊 | ✅ OK | Findings 12 條，Inherited_Baseline/Carry_Forward/Unresolved_Dependencies 均完整 |
| P3 引用鏈 | ✅ OK | 無 B0-CF-XX 非標準 ID；B0-06/B0-15/B0-03 引用正確；V1A-XX/V2A-XX/V2B-XX 全部正確引用且數值一致 |
| P4 Scope 違規 | ✅ OK | 不含側線詳細機制（2B 範疇）或護巢行為（4B 範疇） |
| P5 研究缺口 | ✅ OK | 3 項 Unresolved_Dependencies 已標注 |

**Phase 6 判定**：✅ 不需重跑，0 項修正

### 確認正確的關鍵數值

- 2A Carry_Forward_To_2C 視距矩陣（Zone-A 28/39 cm；Zone-B 36/50 cm；Zone-C 40/55 cm；水庫 120/165 cm）在 2C Sightline_Trigger_Table 完整接收 ✅
- V2C-07 三區 DO 門檻（Zone-A 2.5；Zone-B 2.8；Zone-C 3.0 mg/L）與水溫門檻（Zone-A/B <12°C；Zone-C <14°C）分列正確 ✅
- V2C-10 Follower Rejection 近點 13.5–24 cm（成魚）正確 ✅

---

## SUP-D Carry_Forward 補接（3A + 3B，2026-06-10）

**觸發原因**：雙向引用稽核確認 3A 和 3B 均無任何 VSUP-D 引用，但 SUP-D-A/B/C 三卷的 Carry_Forward 均明確指向 3A/3B。補接模式與 SUP-C 相同。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-3A-SUPD | 3A Inherited_Baseline section 6 後 | 新增 **Section 7（多模態感官辨識與追擊序列，引用自卷 SUP-D-A/B/C）**：VSUP-DA11（HVF 65-80% / LVF 15-30% Reaction Strike 觸發率）、VSUP-DA10（振頻咬餌率矩陣）、VSUP-DB01（著水衝擊物理特徵）、VSUP-DB06（印記魚行為異化）、VSUP-DB10（Commit 閾值 ≥2.5 m/s²）、VSUP-DB11（Dead Stop +30-50% HVF / -40-60% LVF）、VSUP-DC14/DC09（C&R 衰退曲線）、VSUP-DC10（印記消退 50 天）|
| FIX-3B-SUPD | 3B Inherited_Baseline section 9 後 | 新增 **Section 10（多模態感官辨識與追擊序列，引用自卷 SUP-D-A/B/C）**：同上 + VSUP-DB09（Evaluate 拒絕權重）+ VSUP-DC02/04（Dead Drift Kármán 尾流）+ VSUP-DC03（各水體 SNR 有效距離）+ VSUP-DC08/11-13（Match the Hatch 策略切換）|
| FIX-3B-H2S-01 | 3B V3B-03 戰術規則 | H₂S 安全高度由舊值 "60–100 cm" 更新為 **"≥100 cm（精算 99.7–100.0 cm，VSUP-B11）"**；機制來源由 V1B-05 更新為 V1B-10/VSUP-B11 |
| FIX-3B-H2S-02 | 3B Inherited_Baseline section 2 V1B-05/V1B-10 行 | H₂S 安全高度更新為 **~100 cm（VSUP-B11）**；Fe²⁺ 安全高度更新為 VSUP-B09 三區精算值（Zone-B 25.7–32.7 cm；Zone-A 56.5–67.2 cm）；廢棄舊一行式 "60-100 cm / 30-50 cm" 格式 |
| FIX-3B-H2S-03 | 3B Carry_Forward_To_SUPA V3B-03 驗證項目 | 預期避毒高度由舊值 "60–100 cm" 更新為 **"≥100 cm（VSUP-B11 精算；原估 60–100 cm 廢棄）"** |

---

## SUP-D Carry_Forward 補接（2A + 2B，2026-06-10）

**觸發原因**：2A 和 2B 均缺少 SUP-D-A/B/C 的正式 Inherited_Baseline 引用段落，而 SUP-D-A Section 1/2/3 和 SUP-D-B Section 2/8 分別明確指向 2A/2B 作為下游。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-2A-SUPD | 2A Inherited_Baseline 末端 | 新增 **Section 3（食性選擇性與感官辨識補充，引用自卷 SUP-D-A/B/C）**：VSUP-DA01~04（Chesson's α 矩陣）、VSUP-DA08（NTU 視覺失效閾值 35/45/60 NTU）、VSUP-DB08（最小啟動速度 1.5–3.0 cm/s）、VSUP-DC02/04（Dead Drift 攻擊率降 60–75%）|
| FIX-2B-SUPD | 2B 九、Inherited_Baseline 末端 | 新增 **補充小節（獵物生物機械振動特徵，引用自卷 SUP-D-A/B）**：VSUP-DA09（各獵物游泳/逃逸頻率特徵）、VSUP-DB01/02（Topwater 感官接力時序 <100 ms 聲學 → 100 ms–3 s 側線）|
| FIX-SUPE-B0CF | SUP-E Inherited_Baseline 第 41 行 | `V1A-06 / B0-CF-04` 中的 `B0-CF-04`（暴雨濁度恢復時間常數，與視距 28 cm 無關）移除 → 改為單純 `V1A-06` |

---

## SUP-D Carry_Forward 補接（2C，2026-06-10）

**觸發原因**：SUP-D-B Carry_Forward Section 2 明確指向 2C 作為下游（「下游引用卷：`2A` / `2C`」），但 2C 的 Inherited_Baseline 完全無 VSUP-D 引用。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-2C-SUPD | 2C Inherited_Baseline 第 17 條（V2B-01）之後 | 新增第 18 條：**VSUP-DB08**（明視覺條件下啟動 Orientation 及接近行為的最小移動速度邊界 **≥ 1.5 至 3.0 cm/s**；低於此速度的假餌漂移不觸發主動接近）|

---

## 0C 雙向引用稽核（2026-06-10）

**觸發原因**：0A/0B/0C 系統性正向引用核查，發現 0C 內有 2 條錯誤引用（V0B-06 被引用兩次，一次該用 V0B-10，一次該用 V0B-09），以及 1 條 Inherited_Baseline 缺失與 1 條 V0A-11 格式問題。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-0C-01 | 0C 南部管理池水質描述（原 Waterbody-6 夏季行） | `（$Q_{10} = 2.4$，V0B-06）` → `（$Q_{10} = 2.4$，**V0B-10**）`：Q10 加速係數應引用 V0B-10（溫度係數），而非 V0B-06（游離鐵/磷固定量）|
| FIX-0C-02 | 0C Open_Assumptions #3 保守假設值行 | `（V0B-06 推算）` → `（**V0B-09** 推算）`：有機碳 >3.5% 硫酸鹽還原啟動條件在 V0B-09，而非 V0B-06 |
| FIX-0C-03 | 0C Inherited_Baseline 0B 區塊 V0B-05 前 | 新增 **V0B-05**（Zone-C 弱育土乾旱龜裂深 **10–35 cm**，寬 **2–5 cm**；蒙脫石吸水膨脹率 2.0–4.2 倍）：0C Waterbody-4 冬季描述直接使用此值，但 Inherited_Baseline 原本缺漏 |
| FIX-0C-04 | 0C Q-SUP-02 石門水庫秋季描述行 | `（0A-11）` → `（**V0A-11**）`：格式修正，補 V 前綴 |

---

## 0D 雙向引用稽核（2026-06-10）

**觸發原因**：0D Inherited_Baseline 缺少 V0C-14 登錄（雖然 B0-13 引用了它），且 B0-22 引用了 Zone-C 專屬的 V0B-08（乾濕逆轉），而 B0-22 描述的是 Zone-B 的 Eh 首觸時序。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-0D-01 | 0D Inherited_Baseline 0C 區塊 V0C-13 之後 | 新增 **V0C-14**（石門/曾文水庫春秋溫躍層深度與梯度強度）：B0-13 引用了 V0C-14，但 Inherited_Baseline 原本遺漏此條目 |
| FIX-0D-02 | 0D B0-22 來源欄 | `[來源：V0B-08]` → `[來源：**V0A-04**（Zone-B 4月中旬跨 22°C）、**V0B-09**（鐵還原帶 3–5 天建立）]`：V0B-08 為 Zone-C 乾濕逆轉動力學，不適用於 Zone-B 春季首觸 Eh <0 的機制推算 |

---

## 1A 雙向引用稽核補丁（2026-06-10）

**觸發原因**：前一輪稽核（2026-06-09）FIX-1A-04 未實際套用至原文；本輪核查另發現兩項新問題。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-1A-04b | 正文 Q2-1 氣壓計算段落（原 `B0-11` 引用） | `見 \`B0-11\`` → `見 \`V0A-11\``：B0-11 是 DO 崩潰時間常數，不含氣壓資料；V0A-11 明確記載颱風中心過境最低氣壓 920–965 hPa（蘇迪勒 962.4 hPa 例）|
| FIX-1A-06 | Inherited_Baseline 第 4–6 條 | 合併重複的 B0-11 條目（原 item 4 與 item 6 內容相同）：整合為一條，保留 30–32°C 溫度說明與 Henry's Law 基準備注，調整後 B0-09 與 B0-21 順序前移為 item 6–7 |
| FIX-1A-07 | Carry_Forward_To_3B 第 1 條標題與條件行 | 標題加入 V1A-03；條件描述補充：「加上 V1A-03 之 MOx 耗氧速率 0.19–0.53 mg O₂/L/hr 疊加放大，全池溶氧在 2.5–3.5 hr 內徹底歸零（較基線 B0-11 水車關閉 3.0–4.0 hr 更快）」，明確說明 2.5–3.5 hr 是 B0-11 基線 + V1A-03 加速的合成值 |

---

## 3B + 1B 雙向引用稽核補丁（2026-06-10）

**觸發原因**：3B 稽核發現 V1B-04 的 H₂S 避毒高度在 1B 本文與 3B Inherited_Baseline 均仍顯示舊估算值「60–100 cm」（V1B-05/V1B-10 已在前次 FIX-1B-NEW-01/CITE-01 中更新，但 V1B-04 遺漏）；另 3B section 4 缺少 V2A-09（Zone-B）視距矩陣。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-1B-V04 | 1B V1B-04 finding body text（南部停機效應段落） | "至少 **60–100 cm**（遠離底泥毒性帶）" → "至安全高度 **~100 cm**（精算 99.7–100.0 cm，Stagnant h=100 cm，VSUP-B11；原估 60–100 cm 廢棄）" |
| FIX-3B-CITE-05 | 3B Inherited_Baseline 第 2 節 V1B-04 描述行 | "引發急性垂直避毒上移 **60–100 cm**" → "引發急性垂直避毒上移至安全高度 **~100 cm**（精算 99.7–100.0 cm，VSUP-B11；原估 60–100 cm 廢棄）" |
| FIX-3B-CITE-06 | 3B Inherited_Baseline 第 4 節（2A）V2A-08 之後 | 新增 **V2A-09**（Zone-B 北部背風面 SD 45 cm 視距矩陣：晴天高對比 36 cm / 低對比 98 cm；陰天 50/135 cm；暴雨期 <5 cm；紅光穿透 92 cm） |

---

## 2A 正式 Inherited_Baseline 補接 SUP-D/E 引用（2026-06-10）

**觸發原因**：2A 在早期 overview 段落（lines 15–42）已含 VSUP-DA/DB/DC/E 引用，但正式輸出區塊 `Inherited_Baseline`（line 236+）原本僅列 B0-06/B0-11/B0-07/V1A-06/V1A-10/V1A-11/V1A-12，缺少 SUP-D 和 SUP-E 的正式引用條目，導致正式輸出與實際使用數值不符。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-2A-SUPD（正式區塊） | 2A 正式 Inherited_Baseline 末端（item 7 後） | 新增 items 8–14：VSUP-DA01~04（Chesson's α 矩陣：吳郭魚 0.65 > 大肚魚 0.25 > 澤蛙蝌蚪 0.10；飢餓 3 天 0.36；低 DO 0.55–0.58；冬季 0.45）、VSUP-DA08（NTU 失效閾值：褐水 35；綠水 45；灰水 60；切換點 40 NTU）、VSUP-DB08（最小啟動速度 ≥1.5–3.0 cm/s）、VSUP-DC02/DC04（Dead Drift 攻擊率降 60%–75%）、VSUP-E06（沼蝦軟殼 T_h 0.2 s，能效 0.25–0.45 kcal/s）、VSUP-E07（抱卵母蝦 1.15 kcal/g；Zone-C 螯蝦 0.35 kcal/s）、VSUP-E25（OFT 切換閾值 65%–80% / ≥2.5 enc/min；低溫 >90%；高溫 50%–60%）|

---

## 3A Open_Assumptions 標題修正（FIX-3A-CITE-07 補完，2026-06-10）

**觸發原因**：FIX-3A-CITE-07（3A 雙向引用稽核 2026-06-09）指定更新 Open_Assumptions item 4 的 Q₁₀ 衝突描述。前次修補只更新了 body text（缺口說明＋下游影響），但 **標題行**仍保留舊文字「ART 計算使用 Q₁₀ = 2.4...之潛在衝突」。

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-3A-CITE-07-HDR | 3A Open_Assumptions item 4 標題行 | 舊標題：「**ART 計算使用 Q₁₀ = 2.4（廣泛硬骨魚類外推）與預期 VSUP-A04（Q₁₀ = 2.0）之潛在衝突**」→ 新標題：「**ART 計算 Q₁₀ = 2.0（VSUP-A09 確認）——半衰期 15°C = 6.2 hr 與嚴格推算值（5.1 hr）存在 ~21% 偏差（Q₁₀ ≈ 2.28），但不影響 ART 矩陣有效性**」 |

---

## SUP-A 卷雙向引用稽核補丁（2026-06-10）

**目標檔案**：`SUP-A_感官生理閾值補充研究.md`
**稽核範圍**：Inherited_Baseline 引用正確性（V3A-XX 逆向查驗）；Carry_Forward 與 Correction_Instructions 結構確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | VSUP-A01~A09 數值與 3A 引用一致 |
| P2 輸出區塊 | ✅ OK | Carry_Forward（4 項）/ Correction_Instructions（3A 4 條 + 3B 4 條）/ Unresolved_Dependencies（4 條）完整 |
| P3 引用鏈 | ⚠️ 1 件 | Inherited_Baseline 第 4 條「Alert Reset Time（H₂S 環境）: 80–120 hr」引用「V3A-10 / V3A-12」——V3A-12 為 Schreckstoff（驚嚇化學警報素），與 H₂S 生理 ART 無關；正確應引 V3A-11（含 LVF 延長因子 2.0–2.5×，應用至 V3A-10 15°C 基準 36–42 hr → 推算值 72–105 hr ≈ 80–120 hr） |
| P4 Scope | ✅ OK | 無越界 |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 4 條已正確標注 |

**Phase 6 判定**：✅ 不需重跑（1 件引用 ID 修正）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-SUPA-CITE-01 | Inherited_Baseline 第 4 條來源欄 | `V3A-10 / V3A-12` → `V3A-10 / V3A-11`；備注欄補充說明：「V3A-11 LVF 延長因子 2.0–2.5× 應用至 15°C 基準 36–42 hr，推算值 72–105 hr ≈ 80–120 hr；V3A-12 為驚嚇素，與 H₂S 生理 ART 無關」 |

---

## SUP-B 卷雙向引用稽核補丁（2026-06-10）

**目標檔案**：`SUP-B_底棲水化學梯度補充研究.md`
**稽核範圍**：Inherited_Baseline 引用正確性；VSUP-B01~B14 完整性；Carry_Forward 與 Correction_Instructions CI 套用狀態確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | VSUP-B01~B14 數值內部一致；Carry_Forward 5 項值正確 |
| P2 輸出區塊 | ⚠️ 1 件 | Inherited_Baseline 及正文共 5 處使用非標準 ID「4A-10」（應為 V4A-10）|
| P3 引用鏈 | ✅ OK | Correction_Instructions CI 3 條（3A V3A-12、1B V1B-CF-04 Fe²⁺、1B V1B-10/V1B-CF-03 H₂S）均已套用（per FIX-SUPB-01~05 及後續 1B/3B 稽核補丁）；Carry_Forward 下游接收已確認 |
| P4 Scope | ✅ OK | 皮質醇分析嚴格限於 H₂S 直接毒理；繁殖排除語正確 |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 3 條已標注（H3NO 滴定缺口、Fe²⁺ 直接行為實驗缺口、低 DO+H₂S 雙重壓力交互作用缺口）|

**Phase 6 判定**：✅ 不需重跑（1 件格式修正）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-SUPB-CITE-01 | Inherited_Baseline、正文（×5 處）| `4A-10` → `V4A-10`（Finding ID 補 V 前綴，標準化為 V{卷號}-NN 格式；影響 metadata 行、Inherited_Baseline 第 3 條兩處、VSUP-B09 段、Correction_Instructions 第 3 條）|

---

## SUP-C 卷雙向引用稽核補丁（2026-06-10）

**目標檔案**：`SUP-C_黑鱸毒區迴避實證與冒險覓食決策機制.md`
**稽核範圍**：Inherited_Baseline 引用正確性；VSUP-C01~C12 完整性；Carry_Forward 與 Correction_Instructions CI 套用狀態確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | VSUP-C01~C12 數值內部一致；B0-10/B0-11 繼承值正確 |
| P2 輸出區塊 | ⚠️ 1 件 | Inherited_Baseline 第 2 條及 Correction_Instructions CI-1 共 2 處使用非標準 ID「4A-10」（應為 V4A-10）；metadata Upstream_Required 行及 CI-5 已正確使用 V4A-10 |
| P3 引用鏈 | ✅ OK | Correction_Instructions 5 條（CI-1 1B V1B-10、CI-2 3A V3A-12、CI-3 3A V3A-09、CI-4 SUP-B VSUP-B11、CI-5 4A V4A-10）均已套用（per FIX-SUPC-01~04 補丁）；Carry_Forward 4 項下游接收已確認 |
| P4 Scope | ✅ OK | 毒理機制嚴格限於迴避行為與 OFT 能量決策；機制/神經生理詳述已歸屬 SUP-D；繁殖議題排除 |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 3 條已標注（H₂S 亞致死慢性 ART 量化缺口、雙重壓力交互作用缺口、Zone-B 精算缺口）|

**Phase 6 判定**：✅ 不需重跑（1 件格式修正）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-SUPC-CITE-01 | Inherited_Baseline 第 2 條、Correction_Instructions CI-1（×2 處）| `4A-10` → `V4A-10`（Finding ID 補 V 前綴，標準化為 V{卷號}-NN 格式；具體位置：line 23「V4A-07 / 4A-10」→「V4A-07 / V4A-10」；line 118「依據更嚴格的 4A-10 行為迴避閾值」→「依據更嚴格的 V4A-10 行為迴避閾值」）|

---

## SUP-D-A 卷雙向引用稽核補丁（2026-06-10）

**目標檔案**：`SUP-D-A_食性選擇性與感官匹配優先序.md`
**稽核範圍**：Inherited_Baseline 引用正確性；VSUP-DA01~DA11 完整性；Carry_Forward 與 Correction_Instructions CI 套用狀態確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | VSUP-DA01~DA11 數值內部一致；V2A/V2B/V3A 繼承值正確 |
| P2 輸出區塊 | ⚠️ 1 件 | Inherited_Baseline 最後一條引用格式「V3A（VSUP-A04）」非標準 Finding ID，正確源頭為 VSUP-A04（SUP-A ART Q₁₀=2.0 溫度矩陣精算值） |
| P3 引用鏈 | ✅ OK | Correction_Instructions 2 條（CI-1→2A V2A-12、CI-2→3A V3A-09）格式正確；Carry_Forward 4 項（α矩陣、NTU閾值、獵物振頻特徵、LVF/HVF 觸發率）完整 |
| P4 Scope | ✅ OK | 食性選擇性指數與感官匹配矩陣，未跨入多模態入水辨識（SUP-D-B）或漂流偵測/策略切換（SUP-D-C） |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 7 條已標注（台灣 LVF 現場胃內容物、M. salmoides 直接 α 實測、NTU 現場驗證、化學感受性、藻毒素神經毒性、Bifurcation point、CFF 速度限制移交 2C）|

**Phase 6 判定**：✅ 不需重跑（1 件引用格式修正）

### Claude 後處理修改清單

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-SUPDA-CITE-01 | Inherited_Baseline 最後一條（ART 溫度矩陣引用）| `V3A（VSUP-A04）` → `VSUP-A04`（移除無效的 V3A 混合引用格式；VSUP-A04 為 SUP-A 最終精算矩陣，為 ART 數值的正式來源）|

---

## SUP-D-B 卷雙向引用稽核補丁（2026-06-10）

**目標檔案**：`SUP-D-B_多模態獵物辨識與追擊序列.md`
**稽核範圍**：Inherited_Baseline 引用正確性；VSUP-DB01~DB12 完整性；Carry_Forward 與 Correction_Instructions CI 套用狀態確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | VSUP-DB01~DB12 數值內部一致；著水聲壓/追擊時序/Commit 閾值均已量化 |
| P2 輸出區塊 | ✅ OK | 全部輸出區塊完整；12 Findings / 8 Carry_Forward / 4 CI / 6 Unresolved_Dependencies |
| P3 引用鏈 | ⚠️ 1 件（待驗證）| V2A-06 內容衝突：SUP-D-A 將 V2A-06 定義為「皮質醇強化迴避學習（C&R 後 >150 ng/mL）」，SUP-D-B 將 V2A-06 定義為「Reaction Strike 12–25 ms 快速視覺通路」；無法在不讀取 2A 原報告的情況下確定哪個 finding 編號正確 |
| P4 Scope | ✅ OK | 多模態辨識與追擊序列；未跨入食性選擇指數（SUP-D-A）或漂流/策略切換（SUP-D-C）|
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 6 條已標注（Dead Stop 實驗驗證、LTP 衰退常數、化學配體動力學常數、聲壓辨識實驗、行為遙測驗證、Commit 加速度閾值量測）|

**Phase 6 判定**：✅ 不需重跑（1 件 V2A-06/07 引用編號待 2A 審核時確認）

### 待處理項目（需 2A 審核時解決）

| 項目 | 描述 | 動作 |
|------|------|------|
| PENDING-SUPDB-CITE-01 | V2A-06 內容衝突：SUP-D-A（cortisol/C&R）vs SUP-D-B（Reaction Strike 12–25 ms）| 讀取 2A 報告確認 V2A-06/V2A-07 實際內容，修正 SUP-D-A 或 SUP-D-B Inherited_Baseline 中錯誤的引用編號 |

---

## SUP-D-C 卷雙向引用稽核補丁（2026-06-10）

**目標檔案**：`SUP-D-C_水中漂流偵測與策略切換.md`
**稽核範圍**：Inherited_Baseline 引用正確性；VSUP-DC01~DC14 完整性；Carry_Forward 與 Correction_Instructions CI 套用狀態確認

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | VSUP-DC01~DC14 數值內部一致（跨 SUP-D-A/B 繼承值正確）|
| P2 輸出區塊 | ✅ OK | 全部輸出區塊完整；14 Findings / 5 Carry_Forward / 3 CI / 5 Unresolved_Dependencies |
| P3 引用鏈 | ⚠️ 3 件（待驗證）| V2A finding 編號系統性衝突：V2A-03 / V2A-05 / V2A-06 在 SUP-D-C 內及跨 SUP-D-A/B 各卷定義不一致（詳見待處理項目）|
| P4 Scope | ✅ OK | 漂流偵測（Kármán、微振動）、搜索映像 LTP、策略切換神經生理；Topwater 入水衝擊已歸屬 SUP-D-B |
| P5 研究缺口 | ✅ OK | Unresolved_Dependencies 5 條已標注（生物微振動電生理缺口、Dead Stop 交互作用矩陣、遙測衰減曲線、飼料印記分子標記、LTP 電生理時間窗口）|

**Phase 6 判定**：✅ 不需重跑（V2A-XX 引用編號待 2A 審核時全批解決）

### 待處理項目（需 2A 審核時解決）

| 項目 | 描述 | 動作 |
|------|------|------|
| PENDING-SUPDC-CITE-01 | V2A-03 文件內衝突：Inherited_Baseline（line 19）= 落水聽覺制約記憶 >12 個月；VSUP-DC10（line 81）= 飼料印記消退半衰期 50 天（這兩個內容不能都是 V2A-03）| 讀取 2A，確認 V2A-03/V2A-05 實際內容，修正其中一處錯誤引用 |
| PENDING-SUPDC-CITE-02 | V2A-06 文件內衝突：Inherited_Baseline（line 21）= Reaction Strike 12–25 ms；VSUP-DC09（line 75）= C&R 後皮質醇 >150 ng/mL（SUP-D-A 亦將 V2A-06 定義為 cortisol/C&R，但 SUP-D-B/D-C 將其定義為 Reaction Strike）| 讀取 2A，確認 V2A-05/V2A-06 實際內容，全批修正 SUP-D-A/B/C 中不一致的引用編號 |
| PENDING-SUPDC-CITE-03 | V2A-05 跨卷衝突：SUP-D-A（line 32）= 飼料印記 91% 競爭劣勢/50 天半衰期；SUP-D-C（line 20）= C&R 後皮質醇 80–180 ng/mL | 同上，一併在 2A 審核時解決 |

---

## 雙向引用稽核 — SUP-D-A V2A 引用編號修正（FIX-SUPDA-CITE-02~04）

**稽核日期**：2026-06-10
**依據**：讀取 `2A_覓食偏好、印記與反射咬餌.md` lines 253–268 確認 V2A-01~V2A-12 authoritative content

**PENDING 解決結果**：

| PENDING 項目 | 結論 | 2A 確認值 |
|-------------|------|----------|
| PENDING-SUPDC-CITE-01（V2A-03 雙重引用）| ✅ 已解決：V2A-03 同時包含「操作制約半衰期 50 天」AND「聽覺古典制約記憶 >12 個月」，SUP-D-C 兩處引用均正確，無需修正 | V2A-03 包含兩項內容 |
| PENDING-SUPDB-CITE-01 + PENDING-SUPDC-CITE-02（V2A-06 定義衝突）| ✅ 已解決：V2A-06 = Reaction Strike 12–25 ms（SUP-D-B/C 正確；SUP-D-A 錯誤）| V2A-06 = Reaction Strike 12–25 ms |
| PENDING-SUPDC-CITE-03（V2A-05 跨卷衝突）| ✅ 已解決：V2A-05 = 皮質醇 C&R 80–180 ng/mL（SUP-D-C/SUP-E 正確；SUP-D-A 錯誤）| V2A-05 = 皮質醇 C&R 80–180 ng/mL |

**V2A-01~V2A-07 authoritative 對照表（來自 2A lines 257–263）**：

| Finding ID | 2A 實際內容 |
|-----------|------------|
| V2A-01 | OFT 各獵物能效值（kcal/s）；吳郭魚幼魚最優 |
| V2A-02 | 大肚魚視角不過 1.5° 閾值 → 神經生物學忽略機制 |
| V2A-03 | 操作制約半衰期 50 天（3–6 個月消退）+ 聽覺古典制約記憶殘留 >12 個月 |
| V2A-04 | 路亞落水聲 300–1500 Hz + 古典制約觸發通路 |
| V2A-05 | C&R 後皮質醇 80–180 ng/mL + Lure-shyness 48–96 hr |
| V2A-06 | Reaction Strike 12–25 ms 快速視覺通路 |
| V2A-07 | Vcrit ≥ 1.2 m/s 速度閾值（慢速認知通路 150–350 ms） |

---

### [FIX-SUPDA-CITE-02] SUP-D-A Inherited_Baseline V2A-05 → V2A-03

- **問題**：SUP-D-A line 32 將「飼料印記 91% 競爭劣勢，半衰期 50 天」標注為 V2A-05。實際上 2A 的 V2A-05 = 皮質醇 C&R 80–180 ng/mL；飼料印記/半衰期內容在 V2A-03。
- **修正**：`**V2A-05**：養殖飼料印記魚放流後初期…` → `**V2A-03**：養殖飼料印記魚放流後初期…`
- **影響**：引用編號正確；內容描述（91%、50 天）不變

---

### [FIX-SUPDA-CITE-03] SUP-D-A Inherited_Baseline V2A-06 → V2A-05

- **問題**：SUP-D-A line 33 將「皮質醇強化迴避學習，C&R 後 >150 ng/mL」標注為 V2A-06。實際上 2A 的 V2A-06 = Reaction Strike 12–25 ms；皮質醇 C&R 內容在 V2A-05。
- **修正**：`**V2A-06**：皮質醇強化迴避學習…` → `**V2A-05**：皮質醇強化迴避學習…`
- **影響**：引用編號正確；內容描述不變

---

### [FIX-SUPDA-CITE-04] SUP-D-A Inherited_Baseline V2A-07 → V2A-06（並移除待驗證注記）

- **問題**：SUP-D-A line 34 將「Reaction Strike 12–25 ms 視頂蓋啟動潛伏期」標注為 V2A-07，並附「⚠️ [待驗證：instruction fallback 為 30–50 ms]」。實際上 2A 的 V2A-06 = Reaction Strike 12–25 ms；V2A-07 = Vcrit ≥ 1.2 m/s 速度閾值。
- **修正**：`**V2A-07**：Reaction Strike…⚠️ [待驗證…]` → `**V2A-06**：Reaction Strike…（覆蓋 instruction fallback 30–50 ms；2A 原報告確認值）`
- **影響**：引用編號正確；12–25 ms 數值已由 2A 確認，移除待驗證狀態

---

## 雙向引用稽核 — SUP-D-C VSUP-DC09 V2A-06 → V2A-05（FIX-SUPDC-CITE-01）

**稽核日期**：2026-06-10

### [FIX-SUPDC-CITE-01] SUP-D-C VSUP-DC09 line 75 皮質醇引用編號修正

- **問題**：SUP-D-C line 75 在 VSUP-DC09 正文中寫「受 >150 ng/mL 急性皮質醇應激主導，V2A-06」。實際上 2A 的 V2A-06 = Reaction Strike 12–25 ms；皮質醇 C&R 內容在 V2A-05。
- **修正**：`V2A-06，為期 48–96 hr` → `V2A-05，為期 48–96 hr`
- **影響**：引用編號正確；與 Inherited_Baseline（line 21）V2A-06 = Reaction Strike 的正確標注一致，文件內部不再矛盾

---

## 雙向引用稽核 — 2B 卷（首次）

**稽核日期**：2026-06-10
**對象文件**：`2B_側線、內耳與水下聲學傳遞.md`

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | V2B-01~V2B-13 數值內部一致；Medwin 方程計算值驗證正確 |
| P2 輸出區塊 | ✅ OK | 全部輸出區塊完整；13 Findings / 4 Carry_Forward / N/A CI / 3 Open_Assumptions / 2 Unresolved_Dependencies |
| P3 引用鏈 | ⚠️ 1 件（待 0D 稽核時解決）| B0-15 在 Inherited_Baseline 中出現兩次，各指向不同內容（藻華 EPS + 曾文水庫能見度）；需對照 0D 確認是否同屬 B0-15 或有誤 |
| P4 Scope | ✅ OK | 側線、聽石、聲學傳遞完全在 2B 範疇；未越入視覺系統（2A/2C）或覓食決策（2A）|
| P5 研究缺口 | ✅ OK | Open_Assumptions 3 條、Unresolved_Dependencies 2 條均已標注 |

**反向核查（Backward Check）**：
- B0-03/06/07/12/14: 0D baseline 引用，待 0D 稽核核實
- **B0-15**：line 309 = "南部 Zone-C 春末藻華期 EPS 動力黏度增加 10%"；line 313 = "曾文水庫局部靜水庫灣能見度降至 30–50 cm（持續 10–18 天）" — 兩筆均標 B0-15，但內容指向不同現象，需 0D 驗證
- **VSUP-DA09**: ✅ 已驗證 — SUP-D-A line 76 VSUP-DA09 內容（各台灣獵物水動力波特徵）完全對應 2B Inherited_Baseline line 315-316
- **VSUP-DB01/02**: ✅ 已驗證 — SUP-D-B Carry_Forward 指定 "(d) 下游引用卷：2B"，內容（Topwater 入水感官接力時序）完全對應 2B line 316-317

**待處理項目解決紀錄（2026-06-10）**：

| 項目 | 解決狀態 | 說明 |
|------|---------|------|
| PENDING-2B-CITE-01 | ✅ 已解決（部分需補修正）| 讀取 0D line 87：B0-15 確實同時包含「南部野生埤塘能見度驟降至 10–15 cm」與「曾文水庫局部靜水庫灣能見度降至 30–50 cm」，兩筆能見度引用均正確。但 line 309 所附「EPS 動力黏度（η）增加 10%」並非 B0-15 內容，B0-15 僅涵蓋能見度資料，無 EPS 黏度數值。→ 加入 `[外部文獻推算；非 B0-15 內容]` 標注（FIX-2B-CITE-01）|

### 追加修正（PENDING-2B-CITE-01 解決時）

| FIX 編號 | 修改位置 | 修改內容 |
|---------|---------|---------|
| FIX-2B-CITE-01 | Inherited_Baseline line 309 | 「EPS 使動力黏度（η）增加 10%」後補注 `[外部文獻推算；非 B0-15 內容]`，明確區分 B0-15 提供的能見度資料（正確）與額外 EPS 黏度值（無 B0 引用碼）|

**Phase 6 判定**：✅ 不需重跑

---

## 雙向引用稽核 — 2C 卷（首次）

**稽核日期**：2026-06-10
**對象文件**：`2C_視線軸向、攻擊角度與假餌操作.md`

### 稽核結果摘要

| Phase | 結果 | 主要發現 |
|-------|------|---------|
| P1 量化矛盾 | ✅ OK | V2C-01~V2C-12 數值內部一致；三區 Zone-A/B/C 各自獨立列出 |
| P2 輸出區塊 | ✅ OK | 全部輸出區塊完整；12 Findings / 5 Carry_Forward / N/A CI / 3 Unresolved_Dependencies |
| P3 引用鏈 | ⚠️ 1 件（已修正）| V2C-10 及 Carry_Forward 以「V2A-07」標注 Follower Rejection 近點 13.5-24 cm，但 V2A-07 = Vcrit ≥1.2 m/s 速度閾值，並未包含光學近點距離值 |
| P4 Scope | ✅ OK | 視線軸向、攻擊角度、假餌操作映射；未越入側線聲學（2B）或護巢行為（4B）|
| P5 研究缺口 | ✅ OK | 3 條 Unresolved_Dependencies 均已標注 |

**反向核查（Backward Check）**：
- B0-06/B0-15/B0-03: 0D baseline，待 0D 稽核核實
- V1A-06/10/11/12: 1A findings，待 1A 稽核核實
- V2A-01/02/04/05/06/07/11/12: ✅ 均已通過本輪稽核（2A 已讀取並確認 V2A-01~V2A-12 內容正確）
- V2A-08/09/10: 光譜消光係數（三區），在 2A 各自確立 ✅
- **V2B-01**: ✅ V2B-01 = 側線頻率 1-200 Hz，最敏感 5-10 Hz，2C line 244 正確引用
- **VSUP-DB08**: ✅ 已驗證 — SUP-D-B line 94 VSUP-DB08 = 最低移動速度 ≥1.5-3.0 cm/s，完全對應 2C line 245

---

### [FIX-2C-CITE-01] V2C-10 及 Carry_Forward 的 Follower Rejection 近點引用修正

- **問題**：
  - 2C line 267（V2C-10 正文）：「13.5-24 cm 近點範圍（即 Follower Rejection 近點，V2A-07）」
  - 2C line 305（Carry_Forward 第 1 項）：「近點 13.5-24 cm 內（即 Follower Rejection 近點，V2A-07）」
  - V2A-07 = Vcrit ≥1.2 m/s 速度閾值；其中提及「游速慢於 0.5 m/s 則大幅增加 Follower 拒咬機率」，但**不包含 13.5-24 cm 光學近點距離值**
  - 13.5-24 cm 近點是晶狀體牽引肌光學限制，應源自 2C 自身的晶狀體機制分析（V2C-04）

- **修正**：
  - 原：`（即 Follower Rejection 近點，V2A-07）`
  - 改為：`（即 Follower Rejection 近點，V2A-07 / V2C-04）`
  - V2A-07 = 速度條件觸發（<0.5 m/s 進入慢速分析路徑）；V2C-04 = 晶狀體光學近點物理機制

- **影響**：使 13.5-24 cm 的光學近點有明確的本卷（V2C-04）來源依據，而非純引用 V2A-07 速度閾值
