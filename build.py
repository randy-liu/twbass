"""
build.py — 台灣大嘴黑鱸白皮書靜態網站產生器
用法: python build.py
輸出: docs/index.html（自含 HTML，無需外部資源除 Google Fonts）
"""
import re
import sys
import markdown
from pathlib import Path

# Windows 主控台預設 cp950，無法輸出 ✓ 與部分中文；強制 stdout 走 UTF-8
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OUT = Path(__file__).parent / "docs" / "index.html"

# ── 術語速查資料 ──────────────────────────────────────────────────────────
# 每條: (id, term_display, zh_alias, description)
# zh_alias 為空字串代表無別名
GLOSSARY = [
    ("do",                  "DO",               "溶氧",         "溶氧量（Dissolved Oxygen），單位 mg/L。魚類最低生存需求約 2 mg/L；低於此值進入保命模式，無法主動覓食。<br><br><strong>關鍵門檻</strong>：4.5 mg/L 以上全力活動、3 mg/L 覓食下限、1.5 mg/L 保命線。<br><br><strong>不用儀器的現場判讀</strong>（把 mg/L 換成「現場長相」）：<ul class=\"gl-list-inner\"><li><strong>時間</strong>：水草藻類白天產氧、午後最高，整夜耗到清晨 4–6 點觸底（清晨缺氧、午後足氧）</li><li><strong>水溫</strong>：越熱溶解度越低，悶熱無風盛夏淺水雙重夾擊</li><li><strong>擾動</strong>：風皺水面／入水口／水車＝正在復氧；死角、靜水、停機＝往下崩</li><li><strong>藻華</strong>：濃綠水日夜落差最大，清晨谷最深、最危險</li><li><strong>浮頭</strong>：雜魚水面一張一合吸氣＝已跌破約 2 mg/L，黑鱸同步閉口</li></ul>"),
    ("eh",                  "Eh",               "",             "氧化還原電位（單位 mV 毫伏特）。正值=有氧健康底質；接近 0 = 開始耗氧；低於 −150 mV = 臭底危險區，H₂S 大量釋放。<strong>現場不用儀器判斷</strong>：搆得到的底泥（岸邊淺灘、船錨帶起、竿尾戳底）黑又臭（臭雞蛋味）、或水面自然冒泡，即代表底質已落入低 Eh 還原態、在產硫化氫（拖回程的鉛墜會被水洗淨、不宜只聞它；冒泡多為甲烷、只證厭氧，需配合臭味才確認游離 H₂S，單顆移動的泡常是魚）；深水搆不到則由季節（盛夏最毒）與滯水程度推定。南部低鐵呈「黑泥＋強臭」（游離 H₂S 真危險），北部高鐵呈「黑但不臭」（被鎖成 FeS 相對安全）。"),
    ("ph",                  "pH",               "",             "酸鹼值（0–14），中性 = 7。台灣北部水體偏酸（pH 5.5–6.5），南部偏鹼（pH 7–8）。影響化學物質溶解度與魚類感知閾值。"),
    ("h2s",                 "H₂S",              "硫化氫",       "硫化氫，Eh < −150 mV 時底泥產生的有毒氣體，具強烈臭蛋味。高濃度直接毒殺魚類，輕度也會驅趕魚群離開底層。"),
    ("fe",                  "Fe²⁺ / Fe³⁺",      "亞鐵/三價鐵", "亞鐵（Fe²⁺，可溶）/ 三價鐵（Fe³⁺，不可溶）。底泥開始缺氧時 Fe³⁺ 被還原為 Fe²⁺ 溶入水中，是底質惡化的早期指標。"),
    ("ntu",                 "NTU",              "濁度",         "濁度單位（Nephelometric Turbidity Unit）。清水約 1–5 NTU；台灣豪雨後可達數百 NTU；>40 時視覺有效距離大幅縮短。"),
    ("lux",                 "lux",              "照度",         "照度單位（勒克斯），測量光到達表面的強度（1 lux = 每平方公尺 1 流明）。晴天戶外可達 100,000 lux；滿月夜地表約 0.3 lux；魚類褪黑激素受光抑制的閾值僅 0.01 lux。月光在透光清水（如深水水庫冷季）1.5 m 深仍保有 0.039 lux（超過閾值，魚被「誤判為白天」繼續活躍）；染色或濁水（高 CDOM 茶色水、爆藻綠水、管理池）同深度僅剩 0.0005 lux（低於閾值，月光失效）。攻擊上衝時，魚從 1.5 m 至 0.5 m 光強可暴增 70 倍（17→1197 lux），導致閃光致盲而縮回。"),
    ("tss",                 "TSS",              "懸浮固體",     "懸浮固體總量（Total Suspended Solids），單位 mg/L。颱風過後短期內大量增加，壓制魚的視覺感知範圍。"),
    ("cod",                 "COD",              "化學需氧量",   "化學需氧量（Chemical Oxygen Demand）。測量水中有機廢物總量；乾淨水體 <5 mg/L，管理池 >20 mg/L 代表飼料殘渣與排泄物嚴重堆積，耗氧加速。"),
    ("fanshui",             "翻水",             "",             "水體翻轉（Turnover）。表底層水密度差消失後，含 H₂S、Fe²⁺ 的缺氧底部毒水被翻攪至全水層。<br><br><strong>觸發機制（三種）</strong><ul class=\"gl-list-inner\"><li>①溫度驅動：冷鋒帶來 2–4°C 降溫 + 持續 ≥48 小時</li><li>②風力驅動：風速 &gt;5 m/s 持續；桃竹苗常態季風 6–10 m/s 極易觸發</li><li>③颱風／強降雨：25–40 m/s 陣風或暴雨可在數小時內強制全層混合（Ekman 混合深度 &gt;15 m）；管理池水車停機遇冷鋒同觸發（&lt;12 hr）</li></ul><strong>水質衝擊</strong><ul class=\"gl-list-inner\"><li>DO 崩至 &lt;2 mg/L</li><li>Eh 跌破 −150 mV → H₂S 大量釋放，危險帶向上擴展（停機 ~100 cm、深槽 ~150 cm；水車重啟瞬態 120–160 cm；高釋放時全池 &gt;1.2 m 超標致死）</li><li>Fe²⁺ 於 Eh &lt; 0 mV 即開始釋放（影響離底 ≥40 cm）</li></ul><strong>魚的應對</strong>：完全停食，逃往有清水注入的淺灣氧氣庇護區，懸浮離底 ≥40–160 cm。<br><br><strong>恢復時程</strong>：Eh 回到 &gt;+200 mV 需 10–15 天，魚群才回正常棲位。<br><br><strong>地區型態與頻率</strong><ul class=\"gl-list-inner\"><li>台北／宜蘭：深水庫季節翻轉 1–2 次／年，首次約 12 月</li><li>桃竹苗：2–4 次／年，首次約 11 月（東北季風強，早一個月）</li><li>南部：冬季風力弱、風生翻水少，但深水庫季節翻轉照樣發生（延至 1 月中–2 月下）；淺水管理池的冷休克翻水更是毒性最高的一型（捲起底泥 H₂S）</li></ul>"),
    ("cdom",               "CDOM",             "有色溶解有機物", "有色溶解有機物（Colored Dissolved Organic Matter）。由有機質分解產生的棕褐色水溶性有機化合物，主要成分為<strong>腐植酸（humic acids）</strong>與<strong>黃腐酸（fulvic acids）</strong>。<br><br><strong>南部水體與 CDOM</strong><br>台灣南部弱育土（Inceptisol）有機質分解率高，水體 CDOM 濃度顯著高於北部極育土水域。<br><br><strong>與 Schreckstoff 的交互作用（保護套效應）</strong><ul class=\"gl-list-inner\"><li>CDOM 分子包裹住 Schreckstoff（H₃NO）化學警報物質，阻止紫外線光解</li><li>同時形成緩慢釋放機制，使信號持續時間大幅延長</li></ul><strong>北南量化差異</strong><ul class=\"gl-list-inner\"><li>北部（低 CDOM、酸性）：Schreckstoff 有效半徑 &lt;0.5 m，持續數分鐘即水解</li><li>南部（高 CDOM、中性）：有效半徑 4–7 m，警報可持續 12–36 小時</li></ul>南部中魚或跑魚後，該釣點可能整天失效；換點距離需 ≥8 m。"),
    ("fenceng",            "分層",             "熱分層",       "熱分層（Thermal Stratification）。水體因溫度差（密度差）形成穩定的垂直分層結構，由上至下：<strong>表水層</strong>（Epilimnion，溫暖、混合良好）→ <strong>躍溫層</strong>（Thermocline，密度急變界面；台灣水庫夏季約在 3–5 m 深）→ <strong>深水層</strong>（Hypolimnion，低溫低氧、Eh 偏負）。<br><br><strong>對黑鱸棲位的影響</strong><br>黑鱸偏好卡在躍溫層上方到中層結構帶：溫度尚未過高、DO 仍充足、餌魚也沿分層線聚集。<br><br><strong>管理池的分層風險</strong><br>管理池停機 4–6 小時即可重新分層，底層快速缺氧（DO 崩至 &lt;2 mg/L），此時黑鱸全數上浮但停食。"),
    ("yizhongliu",         "異重流",           "",             "密度流（Density Current）。暴雨後大量高含沙、低溫的重泥冷水沿水庫底部潛入，因密度差驅動的水下流動。<br><br><strong>台灣水庫量化特徵</strong><ul class=\"gl-list-inner\"><li>TSS &gt;3000 mg/L</li><li>水溫約 20°C（比原水體冷）</li><li>密度差 5.55 kg/m³，足以直搗 25 m 深槽</li></ul><strong>對黑鱸的衝擊</strong><br>原本棲居 10–15 m 的魚被迫一次性向上逃竄 10–15 m，是水庫魚位最劇烈的突發性位移誘因。<br><br><strong>北南濁期差異</strong><ul class=\"gl-list-inner\"><li>北部（高嶺石主體）：48–72 小時回清</li><li>南部（有機膠體懸浮力強）：濁期可拖 14–30 天</li></ul>"),
    ("cff",                 "CFF",              "臨界閃爍融合頻率", "臨界閃爍融合頻率（Critical Flicker Fusion），單位 Hz。超過此值，魚眼會把個別動作融合成連續影像（看不出節奏）。日間約 30–60 Hz，夜間 / 低溫下降至 10 Hz 以下。"),
    ("art",                 "Alert Reset Time", "ART・警覺重置時間", "魚被釣後，主動覓食驅力恢復所需時間。20°C 約 24 小時；10°C 約 48 小時；30°C 約 12 小時。只鎖住主動覓食——反射咬餌（Reaction Strike）在此期間仍可觸發。"),
    ("q10",                 "Q₁₀",              "溫度係數",     "溫度係數。每升降 10°C，生化反應速率約變 2 倍（升溫加快，降溫減半）。用於推算皮質醇清除速率（ART）與各種底棲化學反應速度。"),
    ("tuishui",             "推水",             "",             "路亞在水中移動時，擠壓前方水體產生的壓力波（低頻流體脈衝）。由魚的側線系統感知，在能見度極差的濁水環境中是最重要的感知信號。"),
    ("cr",                  "C&R",              "",             "Catch &amp; Release（釣放）。釣到後測量拍照再放回水中的行為。過程中皮質醇在 15–30 分鐘內飆升至 >150 ng/mL，啟動 ART 計時。"),
    ("pizichun",            "皮質醇",           "",             "壓力荷爾蒙（Cortisol），由 HPI 軸（Hypothalamic-Pituitary-Interrenal；下視丘—腦垂體—腎間腺軸，魚類壓力反應系統，等效哺乳類的 HPA 軸：下視丘—腦垂體—腎上腺軸）分泌。<br><br><strong>三個重要基線</strong><ul class=\"gl-list-inner\"><li>HVF 自然靜息基線：<strong>1.68±0.69 ng/mL</strong>（健康範圍 ≤6 ng/mL）</li><li>LVF 慢性基線：<strong>20–40 ng/mL</strong>（HPI 軸長期重塑）</li><li>C&amp;R 急性飆升：<strong>&gt;150 ng/mL</strong>（15–30 分鐘內達峰）</li></ul>促使魚對咬過的假餌建立負面記憶，是 Follower Rejection 的生化根源。"),
    ("oft",                 "OFT",              "最佳覓食理論", "最佳覓食理論（Optimal Foraging Theory）。魚優先選擇「淨能量獲取率最高」的目標：能量高、捕獲成本低。假餌必須在魚的成本估算中勝過真食物，才能觸發攻擊。"),
    ("hvf-lvf",             "新鱸 / 老鱸",     "HVF / LVF",    "新鱸（HVF，High Vulnerability Fish）/ 老鱸（LVF，Low Vulnerability Fish）。新鱸（HVF）自然靜息皮質醇基線：<strong>1.68±0.69 ng/mL</strong>（健康範圍 ≤6 ng/mL），依賴視頂蓋反射，容易被釣；老鱸（LVF）慢性皮質醇長期維持在 <strong>20–40 ng/mL</strong>，端腦認知主導，對任何不自然訊號都會觸發 Follower Rejection。⚠️ 老鱸（LVF）在任何 H₂S 存在條件下幾乎不發動底層衝入（冒險覓食突進被端腦完全抑制）。"),
    ("mid-strolling",       "Mid-Strolling",    "",             "以 0.5–1.0 m/s 的緩慢等速拖曳假餌。路亞產生 1–5 Hz 的低頻視覺脈衝，嚴格低於魚眼 CFF，誘發魚進入長距離跟隨的「視覺催眠」狀態。"),
    ("follower-rejection",  "Follower Rejection","",            "魚跟隨假餌到 13–24 cm 近距離後拒絕咬合。觸發原因：（1）假餌進入眼球近點，影像失焦；（2）端腦在 60–100 ms 內完成四項違和交叉比對（視覺失真、無味道、側線歸零、皮質醇記憶提取）。"),
    ("reaction-strike",     "Reaction Strike",  "",             "反射咬餌。假餌速度 >1.5 m/s 時，視頂蓋神經元直接發出攻擊指令（潛伏期僅 30–50 ms），繞過端腦的皮質醇記憶阻斷。ART 窗口內仍可觸發。"),
    ("schreckstoff",        "Schreckstoff",     "",             "受傷魚釋放的水溶性警報化學物質。觸發閾值極低（10⁻¹⁸ 稀釋）。南部中性水體擴散半徑可達 4–7 m，警報持續 12–36 小時；北部酸性水體因化學水解，有效範圍 <0.5 m。"),
    ("fie",                 "FIE",              "漁業誘發演化", "漁業誘發演化（Fisheries-Induced Evolution）。長期高壓垂釣使高皮質醇、高警覺的個體（老魚）存活優勢增加，逐漸在族群中佔主導，導致管理池整體難釣程度世代性提升。"),
    ("lockjaw",             "Lockjaw",          "絕對拒咬",     "魚的主動覓食驅力完全關閉的狀態，不願追也不願咬。觸發原因：劇烈氣壓驟降（Ebullition 啟動後）、C&R 後皮質醇飆升（ART 計時中）、翻水後 0–24 hr 水質惡化。<br><br><strong>與 Follower Rejection 的區別</strong><ul class=\"gl-list-inner\"><li>Lockjaw：連「跟隨」都不出現；魚感知到假餌但完全無覓食反應</li><li>Follower Rejection：魚跟到 13–24 cm 近點後拒絕最後咬合</li></ul><strong>唯一突破方式</strong>：Reaction Strike（>1.5 m/s）直打視頂蓋反射，但 Ebullition 啟動期或水質極度惡化時連 Reaction Strike 也無效。"),
    ("tl",                  "TL",               "全長",         "全長（Total Length），魚體從嘴尖到尾鰭末端的直線距離，是研究描述魚體比例的標準單位。OFT 最佳獵物大小以自身 TL 比例表示：<ul class=\"gl-list-inner\"><li>一般健康成魚：最佳獵物 <strong>22–29% TL</strong>（35 cm 鱸魚偏好 7.7–10.1 cm 獵物）</li><li>老魚（LVF）高壓池：偏好縮至 <strong>0.22–0.29 TL</strong>（更保守）</li><li>超過 <strong>0.30 TL</strong>：肌肉 LDH 活化代謝代價超過獵物熱量約 20%，老魚不啟動攻擊</li></ul>"),
    ("ldh",                 "LDH",              "乳酸脫氫酶",   "乳酸脫氫酶（Lactate Dehydrogenase），肌肉在無氧爆發衝刺時啟動的關鍵酵素，負責乳酸生成與無氧能量轉換。黑鱸追擊超過 <strong>0.30 TL</strong> 的大型獵物時，肌肉 LDH 活化代謝代價可超過獵物熱量約 <strong>20%</strong>（能量虧損）。老魚（LVF）OFT 計算下不啟動攻擊；新魚（HVF）因皮質醇基線低，仍可能出手。"),
    ("ebullition",          "Ebullition",       "氣泡釋放",     "底泥孔隙水中長期累積的溶解氣體（CO₂、CH₄）因外部壓力驟降而快速以氣泡形式逸出的現象。<br><br><strong>颱風觸發機制</strong><ul class=\"gl-list-inner\"><li>颱前 12–24 小時氣壓可驟降 <strong>53 hPa</strong>（1013 → 960 hPa）</li><li>壓差引發底泥黏彈性破裂（viscoelastic-fracture），溶氣大量逸出</li><li>底泥劇烈翻攪：能見度趨零，側線感知同時受氣泡干擾</li></ul><strong>對魚的影響</strong>：啟動後魚進入完全 Lockjaw，強行作釣無效；應在 Ebullition 出現前撤退（颱前 0–12 hr 爆吃窗口已過）。"),
    ("zeta",                "Zeta 電位",        "",             "水中懸浮顆粒表面電荷的量化指標（mV）。絕對值越大，顆粒間靜電斥力越強，越難絮凝沉降，水色越久濁不清。<br><br><strong>台灣南北差異</strong><ul class=\"gl-list-inner\"><li><strong>北部</strong>（高嶺石，礦物顆粒）：Zeta <strong>-15 ~ -40 mV</strong>，斥力弱 → 颱後 48–72 小時回清</li><li><strong>南部</strong>（有機膠體）：Zeta <strong>-42 ~ -52 mV</strong>，DDL 排斥效率高 → 颱後 14–30 天才回清</li></ul>"),
    ("ddl",                 "DDL",              "擴散雙層",     "擴散雙層（Diffuse Double Layer）。帶電顆粒表面吸附的反離子雲，形成靜電斥力屏障，阻止顆粒碰撞絮凝。DDL 厚度與 Zeta 電位絕對值正相關：南部有機膠體 Zeta -42 ~ -52 mV，DDL 排斥力強，即使靜置也難以自然絮凝，這是颱後長濁期（14–30 天）的根本原因。"),
    ("stokes",              "Stokes 沉降",      "",             "根據 Stokes 定律計算的顆粒在靜水中沉降速率，與顆粒半徑平方成正比、與液體黏度成反比。<br><br><strong>台灣颱後南北差異</strong><ul class=\"gl-list-inner\"><li><strong>北部</strong>（高嶺石，Zeta -15~-40 mV）：沉降速 <strong>3 cm/s</strong>（0.108 m/hr），48–72 小時回清 → 切回視覺餌</li><li><strong>南部</strong>（有機膠體，Zeta -42~-52 mV）：沉降速 <strong>0.35 m/day</strong>，14–30 天才回清 → 持續低頻震動路亞</li></ul>"),
    ("mo2",                 "MO₂",              "靜態代謝耗氧率", "靜態代謝耗氧率（Metabolic Oxygen consumption rate）。魚在靜止狀態下每公斤體重每小時消耗的溶氧量（mg O₂/kg/h）。<br><br><strong>黑鱸 MO₂ 隨溫度</strong><ul class=\"gl-list-inner\"><li>20°C：約 <strong>48.8 mg/kg/h</strong></li><li>33°C：約 <strong>69.4 mg/kg/h</strong>（比 20°C 高約 42%）</li></ul>高溫時 MO₂ 飆升（需更多氧）而 DO 飽和上限下降（32°C = 7.55 mg/L；35°C = 6.94 mg/L），雙重擠壓導致魚幾乎不追餌。"),
    ("pcrit",               "Pcrit",            "臨界低氧點",   "臨界溶氧濃度（Critical Oxygen Partial Pressure）。DO 低於此值時，魚無法維持有氧代謝，被迫切換保命模式：大幅降低活動量、停止主動覓食。<br><br><strong>黑鱸參考值</strong><ul class=\"gl-list-inner\"><li>15°C：≈ <strong>1.15 mg/L</strong></li><li>20°C：≈ <strong>1.12 mg/L</strong></li></ul>DO 趨近 Pcrit 時咬餌機率接近零。離場信號：DO <strong>&lt;1.5 mg/L</strong> + Eh <strong>&lt;−150 mV</strong> = 停釣。"),
    ("acoustic-masking",    "Acoustic Masking", "聲學遮蔽",     "水中高強度噪音掩蓋魚類側線與內耳感知的現象，使路亞訊號沉沒在背景噪音中。<br><br><strong>管理池水車情境</strong><ul class=\"gl-list-inner\"><li>水車噪聲：<strong>125–135 dB re 1 μPa</strong>，頻率 <strong>25–1,000 Hz</strong></li><li>有效遮蔽管狀神經丘（30–100 Hz）與內耳（100–600 Hz）感知</li><li>對策：大型 Swimbait、Spinnerbait 等<strong>大推水強震動</strong>路亞突破遮蔽閾值</li></ul>水車停機後噪音消失，但老魚端腦警戒上升，需改用細線微物低干擾策略。"),
    ("sns",                 "SNs",              "表淺神經丘",   "表淺神經丘（Superficial Neuromasts）。側線系統的表層感測單元，直接暴露於水流，對 <strong>1–30 Hz</strong> 低頻流速變化最敏感。<br><br><strong>與管狀神經丘（CNs）比較</strong><ul class=\"gl-list-inner\"><li>SNs（表淺神經丘）：偏好 <strong>1–30 Hz</strong>，感知穩定流速方向（穩定水流、大面積推水）</li><li>CNs（管狀神經丘）：偏好 <strong>30–100+ Hz</strong>，感知加速度與壓力梯度（快速振動、尾擺）</li></ul>颱後渾水期視覺失效時，SNs 是魚感知 Spinnerbait 等低頻大推水路亞的主要感知通道。"),
    ("optic-tectum",        "Optic Tectum",     "視頂蓋",       "中腦的關鍵視覺處理中樞，負責快速運動偵測與定向反射（潛伏期僅 30–50 ms）。<br><br><strong>觸發條件</strong>：假餌速度突變 ΔV <strong>&gt;30 cm/s</strong>（角速度突變）→ 視頂蓋的定向反射神經元強制重啟 → 魚重新進入「獵物逃竄」的攻擊迴路，<strong>繞過端腦的皮質醇記憶否決審查</strong>。<br><br><strong>與 Reaction Strike 的關係</strong><ul class=\"gl-list-inner\"><li>路亞速度 &gt;1.5 m/s 時，視頂蓋直接下攻擊指令，端腦插不了手</li><li>ART 計時中（魚被驚嚇後）仍可透過視頂蓋反射觸發咬餌</li></ul><strong>操作技巧</strong>：用竿身橫向快速揮帶（不是加快收線）在近點製造 ΔV &gt;30 cm/s 突變，可用來破解 Follower Rejection。"),
    ("foraging-forays",     "Foraging Forays",  "覓食突進",     "非 LVF 中小型黑鱸在底層獵物密度超出表層 <strong>3.5–5.0 倍</strong>時，從含氧表層短暫衝入底層毒區（&lt; 30 秒）發動攻擊後迅速返回的冒險覓食行為。<br><br><strong>生理極限</strong><ul class=\"gl-list-inner\"><li>單次安全衝入時間：<strong>15–25 秒</strong>（絕對上限 30 秒）</li><li>單日有效突進次數：<strong>10–15 次</strong>（H₂S ≤ 0.01 mg/L，12 小時覓食期）</li><li>每次突進後強制 COX 重置冷卻期：<strong>45–60 分鐘</strong></li></ul><strong>限制條件</strong><ul class=\"gl-list-inner\"><li>H₂S &lt; 0.05 mg/L 且非 LVF 個體才可能觸發</li><li>LVF 舊魚（皮質醇 ≥ 20 ng/mL）：即使底層獵物密度達 10 倍，端腦仍完全抑制突進反射</li><li>超額突進會導致 ROS 階梯累積與延遲性器官損傷</li></ul>⚠️ 超過 10–15 次額度後，標點進入強制冷卻，底層誘咬失效。"),
    ("cox",                 "COX",              "細胞色素 c 氧化酶", "粒線體電子傳遞鏈最末端的酵素，全名 Cytochrome c Oxidase（細胞色素 c 氧化酶，複合體 IV）。負責將電子從細胞色素 c 傳遞至分子氧，是有氧 ATP 生產的最後一道關卡。<br><br><strong>H₂S 如何攻擊 COX</strong><ul class=\"gl-list-inner\"><li>H₂S 直接鎖住 COX 核心的鐵—銅雙核中心（Heme a₃–CuB），阻斷電子傳遞</li><li>有氧 ATP 生產瞬間停擺 → 即使水中含氧充足，魚仍陷入「<strong>組織毒性缺氧</strong>」</li><li>堵塞的電子傳遞鏈大量洩漏，產生 ROS（活性氧），對細胞膜造成脂質過氧化損傷</li></ul><strong>可逆性與冷卻期</strong><ul class=\"gl-list-inner\"><li>短暫暴露後抑制是<strong>動態可逆</strong>的（魚返回含氧水層後 H₂S 逐漸脫離結合位點）</li><li>每次突進底層後，COX 活性需 <strong>45–60 分鐘</strong>才能完全恢復至基準線（COX 重置冷卻期）</li><li>超頻突進 → ROS 階梯累積 → 延遲性器官損傷</li></ul><strong>大嘴黑鱸的脆弱性</strong>：黑鱸保留脊椎動物標準易感構象，無 SQR 去毒基因過度表現，無法像 <em>Poecilia mexicana</em> 硫泉族群那樣靠分子免疫抵抗 H₂S，完全依賴「短時空間迴避」存活。"),
    ("lc50",                "LC₅₀",             "半致死濃度",   "半致死濃度（Lethal Concentration 50%）：在標準測試條件下，使受試族群中 <strong>50%</strong> 個體死亡的水中化學物質濃度。<br><br><strong>標準測試規格</strong><ul class=\"gl-list-inner\"><li>暴露時間：<strong>96 小時</strong>（96-h LC₅₀，硬骨魚類急性毒性標準試驗）</li><li>測試條件：靜止水體、控溫、無食物</li><li>結果單位：mg/L</li></ul><strong>大嘴黑鱸對 H₂S 的精確值</strong><ul class=\"gl-list-inner\"><li>96-h LC₅₀ = <strong>0.0297–0.0316 mg/L</strong>（ASTM 標準測試，精確測量值）</li><li>台灣南部爛底水體底層 H₂S 峰值：<strong>8.5 mg/L</strong> → 超出 LC₅₀ 約 <strong>270 倍</strong></li></ul>⚠️ LC₅₀ 是「50% 會死」的濃度，不是安全閾值。行為迴避閾值（魚開始主動逃離）約為 <strong>0.002 mg/L</strong>，已比 LC₅₀ 低一個數量級以上。"),
    # ── 新版（初/中/專）補充術語 ──────────────────────────────────────────
    ("match-the-hatch",     "Match the Hatch",  "仿餌匹配",     "模仿當下水域正在大量出現的獵物——<strong>種類、大小、動作節奏、頻率指紋</strong>——來選擇對應假餌的核心思路。台灣全年獵物物候不同（春季搖蚊／孑孓、初夏甲殼<strong>軟殼期</strong>、夏季吳郭魚苗、秋季溪哥…），<strong>對的月份綁對的餌</strong>，往往比換顏色更關鍵。"),
    ("qiwei",               "棲位",             "Habitat",     "魚當下所處的位置 ＝ <strong>深度 ＋ 平面點位</strong>（結構、水層）。找對棲位幾乎等於找到魚。由溶氧、毒區、水溫、風生流與結構共同決定：南部夏天魚常離底懸浮（避 H₂S），北部沒毒氣則敢貼底埋伏。不管哪區哪季，倒木、石堆、水草邊緣、橋墩、陡坎、進出水口都是高機率棲位。"),
    ("ghrelin",             "Ghrelin",          "飢餓素",       "飢餓荷爾蒙。長期飢餓會<strong>短路皮質醇對覓食的抑制</strong>（解開神經閘門），所以久封的池子一開放，連高警覺老魚（LVF）都會在頭幾竿『炸口』。對策：把握黃金期，用大亮色、高效率搜索餌，在窗口內最大化 OFT 收益。"),
    ("dead-stop",           "Dead Stop",        "死停",         "把假餌完全靜止不動。<br><br>靜止給了老魚<strong>端腦慢通路（認知審查）</strong>充足時間做違和交叉比對，反而容易被識破——所以對老魚（LVF）別輕易死停，除非餌已貼結構 <strong>&lt;12 cm</strong>、用空間壓縮牠的決策窗口。新魚（HVF）反射主導，停頓誘咬仍常有效。"),
    ("thermocline",         "溫躍層",           "Thermocline", "水體垂直方向溫度（密度）急變的界面，台灣水庫夏季約在 <strong>3–5 m</strong> 深，上為溫暖表水層、下為低溫低氧深水層。黑鱸常卡在<strong>躍溫層上方到中層結構帶</strong>（溫度適中、DO 仍足、餌魚也沿分層線聚集）。延伸見『分層』條目。"),
    ("volumetric-heat-capacity", "體積熱容",     "",            "底泥的『保溫棉厚度』，單位 J/cm³·K。<ul class=\"gl-list-inner\"><li>北部紅泥 <strong>3.411</strong> ＞ 南部 <strong>3.122</strong></li><li>數字越大＝寒流時底層降溫越慢、保溫滯後越久（Zone-A 17–23 hr、Zone-B 18–24 hr，南部僅 6–12 hr）</li></ul>實戰：北部寒流第一天 0–24 hr 底層比表層高 <strong>2–3°C</strong>，貼底還有黃金窗口；南部底層降溫陡峭、沒有這個緩衝。"),
    ("algal-bloom",         "藻華",             "",            "優養水體藻類爆量。白天光合產氧、<strong>夜間與陰天大量耗氧</strong>，使 DO 劇烈擺盪、清晨崩到保命線以下；同時改變水色與能見度（綠濁），壓縮視覺有效距離。南部野塘春末常見，直接影響選色與打法（偏向側線系、慢、貼近）。"),
    ("wind-driven-current", "風生流",           "",            "風推動表層水往下風（迎風）岸堆積形成的水流，把浮游與小型獵物集中到<strong>迎風岸</strong>，魚跟去結構後方逆流伏擊——<strong>迎風岸常是黃金帶</strong>。風太大時魚退入結構後方靜水區定點等，需把餌慢慢送進那個靜水角落。"),
    ("asr",                 "ASR",              "水表呼吸",     "水表呼吸（Aquatic Surface Respiration）。DO 低到約 <strong>1.6–2.0 mg/L</strong> 時，魚貼上水面吸取表層含氧較高薄水層的保命行為。<br><br>此時已進入<strong>環境型關機</strong>，仰攻（上攻）幾乎 100% 被拒絕；正解是改超慢表層微氧帶，或直接撤點換水體，硬解無效。"),
    ("short-bite",          "短口",             "",            "魚有反應、會碰餌，但沒真正吞下、刺不中。代表<strong>『想吃但有顧慮』</strong>，通常卡在神經決策環節（口觸測試判定假餌太硬／異物感），不是環境問題。對策：換超軟餌（如 Shore 00–15）、延長接觸 <strong>≥100 ms</strong> 再揚竿。"),
    ("limiting-variable",   "限制變數",         "",            "今天卡住魚不咬的那<strong>一個</strong>主因。分兩型：<ul class=\"gl-list-inner\"><li><strong>環境型</strong>：缺氧、毒區、水太濁、低溫關機——再厲害的操竿也救不回，該換層／換時段／換水體</li><li><strong>神經型</strong>：被釣怕、看穿餌——魚在這、想吃、有顧慮，才是技術能介入的戰場</li></ul>專家逆向診斷的目標：用最少試誤鎖定它、<strong>只調它</strong>，而非盲目輪餌輪點。"),
    ("reverse-inference",   "逆向診斷",         "reverse inference", "專家的核心方法。機制是『因 → 果』（這個水溫 → 魚會這樣），但現場拿到的是『果』（只跟不咬、短口、浮頭、突然閉口），要<strong>反推『因』</strong>（哪一環在卡），然後只調那一個變數。落地前先用『驗水層 → 驗活性 → 驗 NTU』三動作分流<strong>環境型 vs 神經型</strong>，再下注。"),
]

# ── 術語在 HTML text node 中的搜尋 pattern ─────────────────────────────────
# 英文縮寫用 (?<![A-Za-z])…(?![A-Za-z]) 避免 partial match；
# C&R 在 HTML 中為 C&amp;R；HVF/LVF 用 alternation 一起 link 同一個 id
TERM_PATTERNS = [
    ("do",                 r'(?<![A-Za-z])DO(?![A-Za-z])'),
    ("eh",                 r'(?<![A-Za-z])Eh(?![A-Za-z])'),
    ("ph",                 r'pH'),
    ("h2s",                r'H₂S'),
    ("fe",                 r'Fe[²³][⁺]'),
    ("ntu",                r'(?<![A-Za-z])NTU(?![A-Za-z])'),
    ("lux",                r'(?<![A-Za-z])lux(?![A-Za-z])'),
    ("tss",                r'(?<![A-Za-z])TSS(?![A-Za-z])'),
    ("cod",                r'(?<![A-Za-z])COD(?![A-Za-z])'),
    ("cdom",               r'(?<![A-Za-z])CDOM(?![A-Za-z])'),
    ("fenceng",            r'分層'),
    ("yizhongliu",         r'異重流'),
    ("cff",                r'(?<![A-Za-z])CFF(?![A-Za-z])'),
    ("art",                r'Alert Reset Time'),
    ("art",                r'(?<![A-Za-z])ART(?![A-Za-z])'),
    ("q10",                r'Q₁₀'),
    ("tuishui",            r'推水'),
    ("fanshui",            r'翻水'),
    ("cr",                 r'C&amp;R'),
    ("pizichun",           r'皮質醇'),
    ("oft",                r'(?<![A-Za-z])OFT(?![A-Za-z])'),
    ("hvf-lvf",            r'(?<![A-Za-z])(?:HVF|LVF)(?![A-Za-z])'),
    ("hvf-lvf",            r'新鱸'),
    ("hvf-lvf",            r'老鱸'),
    ("mid-strolling",      r'Mid-Strolling'),
    ("follower-rejection", r'Follower Rejection'),
    ("reaction-strike",    r'Reaction Strike'),
    ("schreckstoff",       r'Schreckstoff'),
    ("fie",                r'(?<![A-Za-z])FIE(?![A-Za-z])'),
    ("lockjaw",            r'Lockjaw'),
    ("tl",                 r'(?<![A-Za-z])TL(?![A-Za-z])'),
    ("ldh",                r'(?<![A-Za-z])LDH(?![A-Za-z])'),
    ("ebullition",         r'Ebullition'),
    ("ebullition",         r'氣泡釋放'),
    ("zeta",               r'Zeta 電位'),
    ("ddl",                r'(?<![A-Za-z])DDL(?![A-Za-z])'),
    ("stokes",             r'Stokes 沉降'),
    ("mo2",                r'MO₂'),
    ("pcrit",              r'Pcrit'),
    ("acoustic-masking",   r'Acoustic Masking'),
    ("acoustic-masking",   r'聲學遮蔽'),
    ("sns",                r'(?<![A-Za-z])SNs(?![A-Za-z])'),
    ("optic-tectum",       r'Optic Tectum'),
    ("optic-tectum",       r'視頂蓋'),
    ("foraging-forays",    r'Foraging Forays'),
    ("foraging-forays",    r'覓食突進'),
    ("cox",                r'(?<![A-Za-z])COX(?![A-Za-z])'),
    ("cox",                r'細胞色素 c 氧化酶'),
    ("cox",                r'COX 重置冷卻期'),
    ("lc50",               r'LC₅₀'),
    ("lc50",               r'半致死濃度'),
    # ── 新版（初/中/專）補充術語 ──
    ("match-the-hatch",    r'Match the Hatch'),
    ("qiwei",              r'棲位'),
    ("ghrelin",            r'Ghrelin'),
    ("dead-stop",          r'Dead Stop'),
    ("thermocline",        r'溫躍層'),
    ("volumetric-heat-capacity", r'體積熱容'),
    ("algal-bloom",        r'藻華'),
    ("wind-driven-current", r'風生流'),
    ("asr",                r'(?<![A-Za-z])ASR(?![A-Za-z])'),
    ("short-bite",         r'短口'),
    ("limiting-variable",  r'限制變數'),
    ("reverse-inference",  r'逆向診斷'),
]

# 預先編譯 combined regex，single-pass replacement per text node
_gl_combined = re.compile(
    '|'.join(f'(?P<g{i}>{pat})' for i, (_, pat) in enumerate(TERM_PATTERNS))
)
_gl_id_map = {f'g{i}': tid for i, (tid, _) in enumerate(TERM_PATTERNS)}

def _gl_replace(m):
    for gname, tid in _gl_id_map.items():
        if m.group(gname) is not None:
            return f'<span class="gl-trigger" data-term="{tid}">{m.group(0)}</span>'
    return m.group(0)

def inject_term_links(html):
    """在 HTML text node 中將術語包成可點擊的 .gl-trigger span。
    只處理 text node（以 re.split 分離 HTML tag），不改動 tag 本身。"""
    parts = re.split(r'(<[^>]+>)', html)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 0 and part:  # text node
            part = _gl_combined.sub(_gl_replace, part)
        result.append(part)
    return ''.join(result)


def build_glossary_html(terms):
    items_html = ""
    for tid, term, zh_alias, desc in terms:
        alias_html = f' <span class="gl-alias">{zh_alias}</span>' if zh_alias else ""
        items_html += (
            f'<div class="gl-item" id="gl-{tid}">'
            f'<dt class="gl-term">{term}{alias_html}</dt>'
            f'<dd class="gl-desc">{desc}</dd>'
            f'</div>\n'
        )
    return f'''<div id="glossary-panel" role="dialog" aria-modal="true" aria-label="術語速查">
  <div class="gl-header">
    <span class="gl-title">📖 術語速查</span>
    <button id="glossary-close" aria-label="關閉術語面板">✕</button>
  </div>
  <div class="gl-search-wrap">
    <input id="glossary-search" type="search" placeholder="搜尋術語…（名稱／別名／解說）" autocomplete="off" aria-label="搜尋術語">
  </div>
  <dl class="gl-list">
{items_html}  </dl>
  <div class="gl-noresult" hidden>找不到相符的術語</div>
</div>
<button id="glossary-btn" aria-label="開啟術語速查">📖 術語</button>
<div id="glossary-overlay"></div>'''

glossary_html = build_glossary_html(GLOSSARY)

# ── 版本設定 ──────────────────────────────────────────────────────────────
# (id, 顯示標籤, markdown 檔名)
VERSIONS = [
    ("junior", "初階", "台灣大嘴黑鱸白皮書-junior.md"),
    ("senior", "中階", "台灣大嘴黑鱸白皮書-senior.md"),
    ("expert", "專業", "台灣大嘴黑鱸白皮書-expert.md"),
]
DEFAULT_VERSION = "junior"
BASE = Path(__file__).parent

# H2 / H3 解析（id 已前綴）
heading_re = re.compile(r'<h([23])[^>]*id="([^"]*)"[^>]*>(.*?)</h\1>', re.DOTALL)

_title_re  = re.compile(r'^[ \t]*#[ \t]+(.*?)[ \t]*$', re.M)
_demote_re = re.compile(r'^(#{1,6}) ', re.M)
_id_re     = re.compile(r'(<h[1-6][^>]*\bid=")([^"]*)(")')

def prepare_markdown(raw, vid):
    """抽出第一行 H1 當版本標題並從正文移除；其餘標題整體降一級
    （# → ##、## → ###、…），使「章→H2、節→H3」沿用既有 TOC 解析。"""
    m = _title_re.search(raw)
    title = m.group(1).strip() if m else vid
    body = (raw[:m.start()] + raw[m.end():]) if m else raw
    body = _demote_re.sub(lambda mm: "#" + mm.group(0), body)
    return title, body

def prefix_heading_ids(html, vid):
    """標題 id 前綴 {vid}-，確保三版合於一頁時 id 全域唯一（錨點不衝突）。"""
    return _id_re.sub(lambda m: f"{m.group(1)}{vid}-{m.group(2)}{m.group(3)}", html)

# ── 產生 TOC HTML ─────────────────────────────────────────────────────────
def build_toc_html(items):
    lines = ['<nav class="toc"><ul class="toc-root">']
    i = 0
    while i < len(items):
        item = items[i]
        if item["level"] == 2:
            # 收集此 H2 下的 H3 子項
            children = []
            j = i + 1
            while j < len(items) and items[j]["level"] == 3:
                children.append(items[j])
                j += 1
            if children:
                lines.append(
                    f'<li class="toc-h2 has-children">'
                    f'<a href="#{item["slug"]}" class="toc-link">{item["text"]}</a>'
                    f'<ul class="toc-children">'
                )
                for c in children:
                    lines.append(
                        f'<li class="toc-h3">'
                        f'<a href="#{c["slug"]}" class="toc-link">{c["text"]}</a>'
                        f"</li>"
                    )
                lines.append("</ul></li>")
                i = j
            else:
                lines.append(
                    f'<li class="toc-h2">'
                    f'<a href="#{item["slug"]}" class="toc-link">{item["text"]}</a>'
                    f"</li>"
                )
                i += 1
        else:
            # 孤立 H3（出現在任何 H2 之前，如「導讀」「開始之前」）→ 當作頂層項目
            lines.append(
                f'<li class="toc-h2">'
                f'<a href="#{item["slug"]}" class="toc-link">{item["text"]}</a>'
                f"</li>"
            )
            i += 1
    lines.append("</ul></nav>")
    return "\n".join(lines)

# ── 逐版本轉換 ────────────────────────────────────────────────────────────
versions_data = []
for vid, vlabel, vfile in VERSIONS:
    raw = (BASE / vfile).read_text(encoding="utf-8-sig")
    vtitle, body = prepare_markdown(raw, vid)

    md = markdown.Markdown(
        extensions=["tables", "toc", "fenced_code", "nl2br", "sane_lists", "smarty"],
        extension_configs={
            "toc": {"permalink": False},
            "smarty": {"smart_quotes": False},
        },
    )
    content_html = md.convert(body)
    content_html = prefix_heading_ids(content_html, vid)
    content_html = inject_term_links(content_html)
    # 重新加回被抽掉的書名（以 H1 呈現於該版頂部）
    content_html = f'<h1 class="doc-title">{vtitle}</h1>\n{content_html}'

    toc_items = []
    for m in heading_re.finditer(content_html):
        level, slug, raw_text = m.group(1), m.group(2), m.group(3)
        text = re.sub(r"<[^>]+>", "", raw_text).strip()
        toc_items.append({"level": int(level), "slug": slug, "text": text})

    versions_data.append({
        "id": vid,
        "label": vlabel,
        "title": vtitle,
        "content": content_html,
        "toc": build_toc_html(toc_items),
        "n_h2": sum(1 for x in toc_items if x["level"] == 2),
        "n_h3": sum(1 for x in toc_items if x["level"] == 3),
    })

# ── HTML Template ─────────────────────────────────────────────────────────
CSS = r"""
:root {
  /* ── 亮色（學術白皮書）＝預設 ── */
  --bg:        #fbfaf7;
  --sidebar-bg:#f5f3ed;
  --surface:   #f1efe8;
  --border:    #e3ded2;
  --border-soft:  #ece8de;
  --text:      #2b2d2c;
  --text-dim:  #6b7180;
  --heading:   #15211d;
  --accent:    #0f5e57;
  --accent2:   #0c746b;
  --accent-dim:   rgba(15,94,87,0.10);
  --accent-soft:  rgba(15,94,87,0.06);
  --accent-soft2: rgba(15,94,87,0.10);
  --quote-border: #0f5e57;
  --quote-bg:  rgba(15,94,87,0.06);
  --row-hover: rgba(15,94,87,0.05);
  --strong:    #111312;
  --code-bg:   #efece4;
  --progress:  #0f5e57;
  --panel-bg:  #ffffff;
  --float-bg:       rgba(255,255,255,0.94);
  --float-bg-hover: rgba(241,239,232,0.98);
  --hover-tint: rgba(0,0,0,0.05);
  --chip-bg:    rgba(0,0,0,0.05);
  --scrim:      rgba(20,22,26,0.38);
  --shadow:       0 4px 16px rgba(20,30,28,0.12);
  --shadow-hover: 0 6px 20px rgba(15,94,87,0.18);
  --font-serif: "Noto Serif TC", Georgia, "Times New Roman", serif;
  --sidebar-w: 260px;
}

html[data-theme="dark"] {
  /* ── 精煉深色（炭灰）── */
  --bg:        #14161a;
  --sidebar-bg:#0f1114;
  --surface:   #1c1f24;
  --border:    #2a2e35;
  --border-soft:  #23272d;
  --text:      #c8ccd2;
  --text-dim:  #8b9099;
  --heading:   #eceef1;
  --accent:    #2db6a6;
  --accent2:   #45d6c6;
  --accent-dim:   rgba(45,182,166,0.16);
  --accent-soft:  rgba(45,182,166,0.08);
  --accent-soft2: rgba(45,182,166,0.13);
  --quote-border: #2db6a6;
  --quote-bg:  rgba(45,182,166,0.08);
  --row-hover: rgba(45,182,166,0.06);
  --strong:    #f5f6f8;
  --code-bg:   #1c1f24;
  --progress:  #2db6a6;
  --panel-bg:  #14161a;
  --float-bg:       rgba(28,31,36,0.92);
  --float-bg-hover: rgba(40,55,52,0.95);
  --hover-tint: rgba(255,255,255,0.06);
  --chip-bg:    rgba(255,255,255,0.05);
  --scrim:      rgba(0,0,0,0.5);
  --shadow:       0 4px 16px rgba(0,0,0,0.4);
  --shadow-hover: 0 6px 20px rgba(45,182,166,0.2);
}

*, *::before, *::after { box-sizing: border-box; }

html { scroll-behavior: smooth; font-size: 16px; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei",
               system-ui, sans-serif;
  line-height: 1.8;
  display: flex;
  transition: background 0.25s ease, color 0.25s ease;
}

/* ── 進度條 ── */
#progress-bar {
  position: fixed;
  top: 0; left: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  z-index: 1000;
  transition: width 0.1s linear;
}

/* ── 側欄 ── */
#sidebar {
  width: var(--sidebar-w);
  min-width: var(--sidebar-w);
  height: 100vh;
  position: sticky;
  top: 0;
  background: var(--sidebar-bg);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  z-index: 100;
}

#sidebar-header {
  padding: 20px 16px 12px;
  border-bottom: 1px solid var(--border);
}

#sidebar-header .site-title {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  line-height: 1.4;
}

#sidebar-header .site-subtitle {
  font-size: 0.7rem;
  color: var(--text-dim);
  margin-top: 4px;
}

/* ── TOC ── */
#toc-container { flex: 1; }
.toc { padding: 8px 0 40px; }
.toc-pane:not(.active) { display: none; }
.toc-root { list-style: none; margin: 0; padding: 0; }

.toc-h2 > .toc-link {
  display: block;
  padding: 6px 16px;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text-dim);
  text-decoration: none;
  border-left: 3px solid transparent;
  transition: color 0.15s, border-color 0.15s, background 0.15s;
  line-height: 1.4;
}
.toc-h2 > .toc-link:hover {
  color: var(--heading);
  background: var(--accent-soft);
}
.toc-h2 > .toc-link.active {
  color: var(--accent);
  border-left-color: var(--accent);
  background: var(--accent-soft2);
}

.toc-children {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  max-height: 0;
  transition: max-height 0.25s ease;
}
.toc-h2.open .toc-children { max-height: 2000px; }

.toc-h3 > .toc-link {
  display: block;
  padding: 4px 16px 4px 28px;
  font-size: 0.73rem;
  color: var(--text-dim);
  text-decoration: none;
  border-left: 3px solid transparent;
  line-height: 1.4;
  transition: color 0.15s, border-color 0.15s;
}
.toc-h3 > .toc-link:hover { color: var(--text); }
.toc-h3 > .toc-link.active {
  color: var(--accent2);
  border-left-color: var(--accent2);
}

/* ── 主內容 ── */
#main-wrapper {
  flex: 1;
  min-width: 0;
  padding: 48px 32px 80px;
  transition: margin-right 0.28s cubic-bezier(0.4,0,0.2,1);
}

/* ── 等級分頁標籤 ── */
#level-tabs {
  display: flex;
  gap: 4px;
  max-width: 800px;
  margin: 0 auto 28px;
  border-bottom: 1px solid var(--border);
  overflow-x: auto;
}
.level-tab {
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--text-dim);
  font-family: inherit;
  font-size: 0.92rem;
  font-weight: 600;
  padding: 10px 20px;
  cursor: pointer;
  white-space: nowrap;
  margin-bottom: -1px;
  transition: color 0.15s, border-color 0.15s;
}
.level-tab:hover { color: var(--heading); }
.level-tab.active { color: var(--accent); border-bottom-color: var(--accent); }
.level-tab .lvl-en {
  font-size: 0.7em;
  color: var(--text-dim);
  margin-left: 5px;
  letter-spacing: 0.04em;
}
.level-tab.active .lvl-en { color: var(--accent2); }

/* ── 版本內容切換 ── */
.content-pane:not(.active) { display: none; }
.doc-title { /* 書名沿用 #content h1 樣式 */ }

/* 術語面板開啟時：桌機推擠主內容讓位（無遮罩） */
body.glossary-open #main-wrapper {
  margin-right: 340px;
}

#content {
  max-width: 800px;
  margin: 0 auto;
}

/* ── 標題 ── */
#content h1 {
  font-family: var(--font-serif);
  font-size: 2rem;
  font-weight: 700;
  color: var(--heading);
  border-bottom: 2px solid var(--accent);
  padding-bottom: 14px;
  margin-bottom: 30px;
  line-height: 1.35;
  letter-spacing: 0.01em;
}
#content h2 {
  font-family: var(--font-serif);
  font-size: 1.45rem;
  font-weight: 600;
  color: var(--heading);
  border-bottom: 1px solid var(--border);
  padding-bottom: 10px;
  margin-top: 60px;
  margin-bottom: 22px;
  scroll-margin-top: 24px;
  letter-spacing: 0.01em;
}
#content h3 {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--accent);
  margin-top: 34px;
  margin-bottom: 12px;
  scroll-margin-top: 24px;
}
#content h4 {
  font-size: 0.95rem;
  color: var(--accent2);
  margin-top: 24px;
  margin-bottom: 8px;
}

/* ── 段落與清單 ── */
#content p { margin: 0 0 1rem; }
#content ul, #content ol { padding-left: 1.6em; margin: 0.5rem 0 1rem; }
#content li { margin-bottom: 0.3rem; }
#content strong { color: var(--strong); font-weight: 700; }
#content em { color: var(--accent2); font-style: normal; }

/* ── 引用塊 ── */
#content blockquote {
  margin: 1.2rem 0;
  padding: 12px 18px;
  border-left: 4px solid var(--quote-border);
  background: var(--quote-bg);
  color: var(--text);
  border-radius: 0 6px 6px 0;
}
#content blockquote p { margin: 0; }

/* ── 程式碼 ── */
#content code {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 0.87em;
  font-family: "JetBrains Mono", "Consolas", "Monaco", monospace;
  color: var(--accent2);
}
#content pre {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  overflow-x: auto;
}
#content pre code {
  background: none;
  border: none;
  padding: 0;
  font-size: 0.85em;
  color: var(--text);
}

/* ── 表格 ── */
.table-wrap {
  overflow-x: auto;
  margin: 1.2rem 0;
  border-radius: 8px;
  border: 1px solid var(--border);
}
#content table {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.88rem;
  min-width: 400px;
}
#content thead {
  background: var(--surface);
  position: sticky;
  top: 0;
}
#content th {
  padding: 10px 14px;
  text-align: left;
  color: var(--heading);
  font-weight: 600;
  border-bottom: 2px solid var(--border);
  white-space: nowrap;
}
#content td {
  padding: 8px 14px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
  line-height: 1.6;
}
#content tr:last-child td { border-bottom: none; }
#content tbody tr:nth-child(odd)  { background: var(--surface); }
#content tbody tr:nth-child(even) { background: transparent; }
#content tbody tr:hover { background: var(--row-hover); }

/* ── 水平線 ── */
#content hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 40px 0;
}

/* ── 手機漢堡按鈕 ── */
#menu-btn {
  display: none;
  position: fixed;
  top: 12px;
  left: 12px;
  z-index: 200;
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: 6px;
  padding: 8px 10px;
  cursor: pointer;
  font-size: 1.1rem;
  line-height: 1;
}

/* ── 亮暗主題切換鈕 ── */
#theme-btn {
  position: fixed;
  top: 14px;
  right: 18px;
  z-index: 280;
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--float-bg);
  border: 1px solid var(--border);
  color: var(--accent);
  border-radius: 50%;
  cursor: pointer;
  font-size: 1.05rem;
  line-height: 1;
  backdrop-filter: blur(8px);
  box-shadow: var(--shadow);
  transition: background 0.15s, box-shadow 0.15s, color 0.15s;
}
#theme-btn:hover { background: var(--float-bg-hover); box-shadow: var(--shadow-hover); }

/* ── RWD ── */
@media (max-width: 768px) {
  body { display: block; }

  #menu-btn { display: block; }

  #sidebar {
    position: fixed;
    top: 0; left: 0;
    height: 100%;
    transform: translateX(-100%);
    transition: transform 0.25s ease;
    z-index: 150;
    width: 280px;
    min-width: unset;
  }
  #sidebar.open { transform: translateX(0); }

  #sidebar-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: var(--scrim);
    z-index: 140;
  }
  #sidebar-overlay.open { display: block; }

  #main-wrapper { padding: 52px 18px 60px; }
  #content h1 { font-size: 1.4rem; }
  #content h2 { font-size: 1.15rem; }

  /* 手機：恢復 overlay；取消桌機 margin 推擠 */
  #glossary-overlay.open { display: block; }
  body.glossary-open #main-wrapper { margin-right: 0; }

  /* 手機：底部 bottom sheet */
  #glossary-panel {
    top: auto !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 70vh !important;
    max-height: 70vh !important;
    border-radius: 16px 16px 0 0 !important;
    transform: translateY(100%) !important;
  }
  #glossary-panel.open {
    transform: translateY(0) !important;
  }
  #glossary-btn {
    bottom: 16px !important;
    right: 16px !important;
  }
}

/* ── 術語速查面板 ── */
#glossary-btn {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 300;
  background: var(--float-bg);
  border: 1px solid var(--border);
  color: var(--accent);
  border-radius: 24px;
  padding: 8px 16px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  backdrop-filter: blur(8px);
  box-shadow: var(--shadow);
  transition: background 0.15s, box-shadow 0.15s;
  font-family: inherit;
}
#glossary-btn:hover {
  background: var(--float-bg-hover);
  box-shadow: var(--shadow-hover);
}

#glossary-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: var(--scrim);
  z-index: 290;
}
/* overlay only shown on mobile (see @media block below) */

#glossary-panel {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 340px;
  max-width: 92vw;
  z-index: 310;
  background: var(--panel-bg);
  border-left: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.28s cubic-bezier(0.4,0,0.2,1);
  overflow: hidden;
}
#glossary-panel.open {
  transform: translateX(0);
}

.gl-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}
.gl-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--heading);
  letter-spacing: 0.03em;
}
#glossary-close {
  background: none;
  border: none;
  color: var(--text-dim);
  cursor: pointer;
  font-size: 1rem;
  padding: 4px 6px;
  border-radius: 4px;
  transition: color 0.15s, background 0.15s;
}
#glossary-close:hover { color: var(--heading); background: var(--hover-tint); }

.gl-list {
  overflow-y: auto;
  flex: 1;
  margin: 0;
  padding: 12px 0 40px;
}
.gl-item {
  padding: 12px 18px;
  border-bottom: 1px solid var(--border-soft);
}
.gl-item:last-child { border-bottom: none; }
.gl-term {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 4px;
  font-style: normal;
}
.gl-desc {
  font-size: 0.8rem;
  color: var(--text-dim);
  line-height: 1.65;
  margin: 0;
}
.gl-desc strong { color: var(--text); }
.gl-list-inner { margin: 3px 0 8px 0; padding-left: 1.2em; }
.gl-list-inner li { margin-bottom: 3px; }
/* ── 術語觸發連結 ── */
.gl-trigger {
  color: var(--accent);
  text-decoration: underline dotted;
  text-underline-offset: 3px;
  cursor: pointer;
  border-radius: 2px;
  padding: 0 1px;
  transition: background 0.15s;
}
.gl-trigger:hover { background: var(--accent-dim); }
/* ── 術語 highlight（持久，直到換術語或關閉面板）── */
.gl-highlighted { background: rgba(251,191,36,0.18); border-radius: 4px; }
/* ── 術語別名標籤 ── */
.gl-alias {
  font-size: 0.72em;
  color: var(--text-dim);
  background: var(--chip-bg);
  border-radius: 3px;
  padding: 1px 5px;
  margin-left: 6px;
  vertical-align: middle;
  font-weight: normal;
  letter-spacing: 0.02em;
}
/* ── 速查搜尋框 ── */
.gl-search-wrap {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}
#glossary-search {
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text);
  font-family: inherit;
  font-size: 0.82rem;
  padding: 7px 10px;
  outline: none;
  transition: border-color 0.15s;
}
#glossary-search:focus { border-color: var(--accent); }
#glossary-search::placeholder { color: var(--text-dim); }
.gl-noresult {
  padding: 24px 18px;
  text-align: center;
  color: var(--text-dim);
  font-size: 0.82rem;
}
"""

JS = r"""
// ── 閱讀進度條 ───────────────────────────────────────────
const bar = document.getElementById('progress-bar');
window.addEventListener('scroll', () => {
  const total = document.documentElement.scrollHeight - window.innerHeight;
  bar.style.width = total > 0 ? (window.scrollY / total * 100) + '%' : '0%';
}, { passive: true });

// ── 亮暗主題切換 ─────────────────────────────────────────
const themeBtn = document.getElementById('theme-btn');
function applyThemeIcon() {
  const dark = document.documentElement.dataset.theme === 'dark';
  themeBtn.textContent = dark ? '☀' : '🌙';
  themeBtn.setAttribute('aria-label', dark ? '切換為亮色主題' : '切換為深色主題');
}
applyThemeIcon();
themeBtn.addEventListener('click', () => {
  const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  try { localStorage.setItem('twbass-theme', next); } catch (e) {}
  applyThemeIcon();
});

// ── 手機側欄元素 ─────────────────────────────────────────
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('sidebar-overlay');
const menuBtn = document.getElementById('menu-btn');

// ── 版本（等級）切換 ─────────────────────────────────────
const STORAGE_KEY     = 'twbass-level';
const DEFAULT_VERSION = 'junior';
const tabs         = Array.from(document.querySelectorAll('#level-tabs .level-tab'));
const contentPanes = Array.from(document.querySelectorAll('.content-pane'));
const tocPanes     = Array.from(document.querySelectorAll('.toc-pane'));
const validVids    = tabs.map(t => t.dataset.version);

// 每個 TOC pane 的展開/收合與手機關閉行為（一次性綁定）
tocPanes.forEach(pane => {
  pane.querySelectorAll('.toc-h2.has-children > .toc-link').forEach(link => {
    link.addEventListener('click', () => link.closest('.toc-h2').classList.toggle('open'));
  });
  const firstH2 = pane.querySelector('.toc-h2.has-children');
  if (firstH2) firstH2.classList.add('open');
  pane.querySelectorAll('.toc-link').forEach(a => {
    a.addEventListener('click', () => {
      sidebar.classList.remove('open');
      overlay.classList.remove('open');
    });
  });
});

// 包裝所有版本的表格（隱藏的 pane 也先包好）
document.querySelectorAll('.content-pane table').forEach(t => {
  if (t.parentElement.classList.contains('table-wrap')) return;
  const wrap = document.createElement('div');
  wrap.className = 'table-wrap';
  t.parentNode.insertBefore(wrap, t);
  wrap.appendChild(t);
});

const getActivePane    = () => document.querySelector('.content-pane.active');
const getActiveTocPane = () => document.querySelector('.toc-pane.active');

// 目前可見標題 → 高亮對應 TOC 連結
function updateActive(activeSlug) {
  const tocPane = getActiveTocPane();
  if (!tocPane) return;
  const links = Array.from(tocPane.querySelectorAll('.toc-link'));
  links.forEach(a => a.classList.remove('active'));
  const active = links.find(a => a.getAttribute('href') === '#' + activeSlug);
  if (!active) return;
  active.classList.add('active');
  const parentLi = active.closest('.toc-h2');
  if (parentLi) {
    parentLi.classList.add('open');
    const parentLink = parentLi.querySelector(':scope > .toc-link');
    if (parentLink) parentLink.classList.add('active');
  }
}

// 每次切版重建 IntersectionObserver，只觀察目前版本的標題
let observer = null;
function rebuildObserver() {
  if (observer) observer.disconnect();
  const pane = getActivePane();
  if (!pane) return;
  observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) updateActive(e.target.id); });
  }, { rootMargin: '-10% 0px -80% 0px', threshold: 0 });
  pane.querySelectorAll('h2, h3').forEach(h => observer.observe(h));
}

function selectVersion(vid, persist) {
  if (!validVids.includes(vid)) vid = DEFAULT_VERSION;
  tabs.forEach(t => t.classList.toggle('active', t.dataset.version === vid));
  contentPanes.forEach(p => p.classList.toggle('active', p.dataset.content === vid));
  tocPanes.forEach(p => p.classList.toggle('active', p.dataset.toc === vid));
  if (persist) { try { localStorage.setItem(STORAGE_KEY, vid); } catch (e) {} }
  rebuildObserver();
  window.scrollTo({ top: 0 });
}

tabs.forEach(tab => tab.addEventListener('click', () => selectVersion(tab.dataset.version, true)));

// 初始版本：localStorage → 預設初階
let initialVid = DEFAULT_VERSION;
try { const saved = localStorage.getItem(STORAGE_KEY); if (saved) initialVid = saved; } catch (e) {}
selectVersion(initialVid, false);

// ── 手機選單 ─────────────────────────────────────────────
menuBtn.addEventListener('click', () => {
  sidebar.classList.toggle('open');
  overlay.classList.toggle('open');
});
overlay.addEventListener('click', () => {
  sidebar.classList.remove('open');
  overlay.classList.remove('open');
});

// ── 術語速查面板 ─────────────────────────────────────────
const glossaryPanel   = document.getElementById('glossary-panel');
const glossaryBtn     = document.getElementById('glossary-btn');
const glossaryClose   = document.getElementById('glossary-close');
const glossaryOverlay = document.getElementById('glossary-overlay');
const glossarySearch  = document.getElementById('glossary-search');
const glItems         = Array.from(document.querySelectorAll('.gl-item'));
const glNoResult      = document.querySelector('.gl-noresult');

// 全文過濾（術語名＋別名＋解說內文）
function filterGlossary() {
  const q = (glossarySearch.value || '').trim().toLowerCase();
  let shown = 0;
  glItems.forEach(it => {
    const hit = !q || it.textContent.toLowerCase().includes(q);
    it.style.display = hit ? '' : 'none';
    if (hit) shown++;
  });
  if (glNoResult) glNoResult.hidden = (shown !== 0);
}
glossarySearch.addEventListener('input', filterGlossary);

function openGlossary() {
  glossaryPanel.classList.add('open');
  glossaryOverlay.classList.add('open');
  glossaryBtn.setAttribute('aria-expanded', 'true');
  document.body.classList.add('glossary-open');
}
function closeGlossary() {
  glossaryPanel.classList.remove('open');
  glossaryOverlay.classList.remove('open');
  glossaryBtn.setAttribute('aria-expanded', 'false');
  document.body.classList.remove('glossary-open');
  if (activeGlItem) { activeGlItem.classList.remove('gl-highlighted'); activeGlItem = null; }
  if (glossarySearch && glossarySearch.value) { glossarySearch.value = ''; filterGlossary(); }
}

glossaryBtn.addEventListener('click', () => {
  glossaryPanel.classList.contains('open') ? closeGlossary() : openGlossary();
});
glossaryClose.addEventListener('click', closeGlossary);
glossaryOverlay.addEventListener('click', closeGlossary);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeGlossary(); });

// ── 術語點擊連動（事件委派）────────────────────────────────
let activeGlItem = null;
document.getElementById('content').addEventListener('click', e => {
  const trigger = e.target.closest('.gl-trigger');
  if (!trigger) return;
  const termId = trigger.dataset.term;
  openGlossary();
  // 清掉搜尋過濾，確保目標條目可見
  if (glossarySearch && glossarySearch.value) { glossarySearch.value = ''; filterGlossary(); }
  const item = document.getElementById('gl-' + termId);
  if (!item) return;
  if (activeGlItem) activeGlItem.classList.remove('gl-highlighted');
  activeGlItem = item;
  item.classList.add('gl-highlighted');
  item.scrollIntoView({ block: 'center', behavior: 'smooth' });
});
"""

HEAD_SCRIPT = r"""    (function () {
      try {
        var t = localStorage.getItem('twbass-theme');
        document.documentElement.dataset.theme = (t === 'dark' || t === 'light') ? t : 'light';
      } catch (e) { document.documentElement.dataset.theme = 'light'; }
    })();"""

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>台灣大嘴黑鱸釣魚生態白皮書</title>
  <meta name="description" content="台灣大嘴黑鱸（Micropterus salmoides）釣魚生態白皮書——氣候、水體、感官、行為全面量化分析">
  <script>
{head_script}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;600;700&family=Noto+Serif+TC:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
{css}
  </style>
</head>
<body>
  <div id="progress-bar"></div>
  <div id="sidebar-overlay"></div>
  <button id="menu-btn" aria-label="開啟目錄">☰</button>
  <button id="theme-btn" aria-label="切換亮暗主題">🌙</button>

  <aside id="sidebar">
    <div id="sidebar-header">
      <div class="site-title">台灣大嘴黑鱸</div>
      <div class="site-subtitle">釣魚生態白皮書</div>
    </div>
    <div id="toc-container">
{toc_panes}
    </div>
  </aside>

  <div id="main-wrapper">
    <div id="level-tabs" role="tablist" aria-label="釣手等級">
{level_tabs}
    </div>
    <article id="content">
{content_panes}
    </article>
  </div>

{glossary}

  <script>
{js}
  </script>
</body>
</html>
"""

# ── 組合並輸出 ────────────────────────────────────────────────────────────
def _active(vid):
    return " active" if vid == DEFAULT_VERSION else ""

level_tabs = "\n".join(
    f'<button class="level-tab{_active(v["id"])}" data-version="{v["id"]}" role="tab">'
    f'{v["label"]}<span class="lvl-en">{v["id"].capitalize()}</span></button>'
    for v in versions_data
)
toc_panes = "\n".join(
    f'<div class="toc-pane{_active(v["id"])}" data-toc="{v["id"]}">\n{v["toc"]}\n</div>'
    for v in versions_data
)
content_panes = "\n".join(
    f'<div class="content-pane{_active(v["id"])}" data-content="{v["id"]}">\n{v["content"]}\n</div>'
    for v in versions_data
)

html = HTML_TEMPLATE.format(
    css=CSS,
    head_script=HEAD_SCRIPT,
    level_tabs=level_tabs,
    toc_panes=toc_panes,
    content_panes=content_panes,
    glossary=glossary_html,
    js=JS,
)

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"✓ 產生完成：{OUT}")
for v in versions_data:
    print(f"  [{v['label']} {v['id']}] TOC：{v['n_h2'] + v['n_h3']} 項（H2: {v['n_h2']}，H3: {v['n_h3']}）")
