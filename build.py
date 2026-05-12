"""
build.py — 台灣大嘴黑鱸白皮書靜態網站產生器
用法: python build.py
輸出: docs/index.html（自含 HTML，無需外部資源除 Google Fonts）
"""
import re
import markdown
from pathlib import Path

SRC = Path(__file__).parent / "台灣大嘴黑鱸白皮書.md"
OUT = Path(__file__).parent / "docs" / "index.html"

# ── 術語速查資料 ──────────────────────────────────────────────────────────
# 每條: (id, term_display, zh_alias, description)
# zh_alias 為空字串代表無別名
GLOSSARY = [
    ("do",                  "DO",               "溶氧",         "溶氧量（Dissolved Oxygen），單位 mg/L。魚類最低生存需求約 2 mg/L；低於此值進入保命模式，無法主動覓食。"),
    ("eh",                  "Eh",               "",             "氧化還原電位（單位 mV 毫伏特）。正值=有氧健康底質；接近 0 = 開始耗氧；低於 −150 mV = 臭底危險區，H₂S 大量釋放。"),
    ("ph",                  "pH",               "",             "酸鹼值（0–14），中性 = 7。台灣北部水體偏酸（pH 5.5–6.5），南部偏鹼（pH 7–8）。影響化學物質溶解度與魚類感知閾值。"),
    ("h2s",                 "H₂S",              "硫化氫",       "硫化氫，Eh < −150 mV 時底泥產生的有毒氣體，具強烈臭蛋味。高濃度直接毒殺魚類，輕度也會驅趕魚群離開底層。"),
    ("fe",                  "Fe²⁺ / Fe³⁺",      "亞鐵/三價鐵", "亞鐵（Fe²⁺，可溶）/ 三價鐵（Fe³⁺，不可溶）。底泥開始缺氧時 Fe³⁺ 被還原為 Fe²⁺ 溶入水中，是底質惡化的早期指標。"),
    ("ntu",                 "NTU",              "濁度",         "濁度單位（Nephelometric Turbidity Unit）。清水約 1–5 NTU；台灣豪雨後可達數百 NTU；>40 時視覺有效距離大幅縮短。"),
    ("tss",                 "TSS",              "懸浮固體",     "懸浮固體總量（Total Suspended Solids），單位 mg/L。颱風過後短期內大量增加，壓制魚的視覺感知範圍。"),
    ("cod",                 "COD",              "化學需氧量",   "化學需氧量（Chemical Oxygen Demand）。測量水中有機廢物總量；乾淨水體 <5 mg/L，管理池 >20 mg/L 代表飼料殘渣與排泄物嚴重堆積，耗氧加速。"),
    ("cff",                 "CFF",              "臨界閃爍融合頻率", "臨界閃爍融合頻率（Critical Flicker Fusion），單位 Hz。超過此值，魚眼會把個別動作融合成連續影像（看不出節奏）。日間約 30–60 Hz，夜間 / 低溫下降至 10 Hz 以下。"),
    ("art",                 "Alert Reset Time", "ART・警覺重置時間", "魚被釣後，主動覓食驅力恢復所需時間。20°C 約 24 小時；10°C 約 48 小時；30°C 約 12 小時。只鎖住主動覓食——反射咬餌（Reaction Strike）在此期間仍可觸發。"),
    ("q10",                 "Q₁₀",              "溫度係數",     "溫度係數。每升降 10°C，生化反應速率約變 2 倍（升溫加快，降溫減半）。用於推算皮質醇清除速率（ART）與各種底棲化學反應速度。"),
    ("tuishui",             "推水",             "",             "路亞在水中移動時，擠壓前方水體產生的壓力波（低頻流體脈衝）。由魚的側線系統感知，在能見度極差的濁水環境中是最重要的感知信號。"),
    ("cr",                  "C&R",              "",             "Catch &amp; Release（釣放）。釣到後測量拍照再放回水中的行為。過程中皮質醇在 15–30 分鐘內飆升至 >150 ng/mL，啟動 ART 計時。"),
    ("pizichun",            "皮質醇",           "",             "壓力荷爾蒙（Cortisol），由 HPI 軸（Hypothalamic-Pituitary-Interrenal；下視丘—腦垂體—腎間腺軸，魚類壓力反應系統，等效哺乳類的 HPA 軸：下視丘—腦垂體—腎上腺軸）分泌。靜息濃度約 6 ng/mL；C&R 後飆升至 150–300+ ng/mL。促使魚對咬過的假餌建立負面記憶，是 Follower Rejection 的生化根源。"),
    ("oft",                 "OFT",              "最佳覓食理論", "最佳覓食理論（Optimal Foraging Theory）。魚優先選擇「淨能量獲取率最高」的目標：能量高、捕獲成本低。假餌必須在魚的成本估算中勝過真食物，才能觸發攻擊。"),
    ("hvf-lvf",             "HVF / LVF",        "",             "新魚（High Vulnerability Fish）/ 老魚（Low Vulnerability Fish）。HVF 皮質醇基線低，依賴視頂蓋反射，容易被釣；LVF 皮質醇慢性升高，端腦認知主導，對任何不自然訊號都會觸發 Follower Rejection。"),
    ("mid-strolling",       "Mid-Strolling",    "",             "以 0.5–1.0 m/s 的緩慢等速拖曳假餌。路亞產生 1–5 Hz 的低頻視覺脈衝，嚴格低於魚眼 CFF，誘發魚進入長距離跟隨的「視覺催眠」狀態。"),
    ("follower-rejection",  "Follower Rejection","",            "魚跟隨假餌到 13–24 cm 近距離後拒絕咬合。觸發原因：（1）假餌進入眼球近點，影像失焦；（2）端腦在 60–100 ms 內完成四項違和交叉比對（視覺失真、無味道、側線歸零、皮質醇記憶提取）。"),
    ("reaction-strike",     "Reaction Strike",  "",             "反射咬餌。假餌速度 >1.5 m/s 時，視頂蓋神經元直接發出攻擊指令（潛伏期僅 30–50 ms），繞過端腦的皮質醇記憶阻斷。ART 窗口內仍可觸發。"),
    ("schreckstoff",        "Schreckstoff",     "",             "受傷魚釋放的水溶性警報化學物質。觸發閾值極低（10⁻¹⁸ 稀釋）。南部中性水體擴散半徑可達 4–7 m，警報持續 12–36 小時；北部酸性水體因化學水解，有效範圍 <0.5 m。"),
    ("fie",                 "FIE",              "漁業誘發演化", "漁業誘發演化（Fisheries-Induced Evolution）。長期高壓垂釣使高皮質醇、高警覺的個體（老魚）存活優勢增加，逐漸在族群中佔主導，導致管理池整體難釣程度世代性提升。"),
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
    ("tss",                r'(?<![A-Za-z])TSS(?![A-Za-z])'),
    ("cod",                r'(?<![A-Za-z])COD(?![A-Za-z])'),
    ("cff",                r'(?<![A-Za-z])CFF(?![A-Za-z])'),
    ("art",                r'(?<![A-Za-z])ART(?![A-Za-z])'),
    ("q10",                r'Q₁₀'),
    ("tuishui",            r'推水'),
    ("cr",                 r'C&amp;R'),
    ("pizichun",           r'皮質醇'),
    ("oft",                r'(?<![A-Za-z])OFT(?![A-Za-z])'),
    ("hvf-lvf",            r'(?<![A-Za-z])(?:HVF|LVF)(?![A-Za-z])'),
    ("mid-strolling",      r'Mid-Strolling'),
    ("follower-rejection", r'Follower Rejection'),
    ("reaction-strike",    r'Reaction Strike'),
    ("schreckstoff",       r'Schreckstoff'),
    ("fie",                r'(?<![A-Za-z])FIE(?![A-Za-z])'),
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
  <dl class="gl-list">
{items_html}  </dl>
</div>
<button id="glossary-btn" aria-label="開啟術語速查">📖 術語</button>
<div id="glossary-overlay"></div>'''

glossary_html = build_glossary_html(GLOSSARY)

# ── 讀取 Markdown（utf-8-sig 處理 BOM）──────────────────────────────────
md_text = SRC.read_text(encoding="utf-8-sig")

# ── 轉換 Markdown → HTML ─────────────────────────────────────────────────
md = markdown.Markdown(
    extensions=["tables", "toc", "fenced_code", "nl2br", "sane_lists", "smarty"],
    extension_configs={
        "toc": {"permalink": False},
        "smarty": {"smart_quotes": False},
    },
)
content_html = md.convert(md_text)
content_html = inject_term_links(content_html)

# ── 解析 H2 / H3 建立 TOC 資料 ───────────────────────────────────────────
heading_re = re.compile(r'<h([23])[^>]*id="([^"]*)"[^>]*>(.*?)</h\1>', re.DOTALL)
toc_items = []
for m in heading_re.finditer(content_html):
    level, slug, raw_text = m.group(1), m.group(2), m.group(3)
    text = re.sub(r"<[^>]+>", "", raw_text).strip()
    toc_items.append({"level": int(level), "slug": slug, "text": text})

# ── 產生 TOC HTML ─────────────────────────────────────────────────────────
def build_toc_html(items):
    lines = ['<nav id="toc"><ul class="toc-root">']
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
            i += 1  # 跳過孤立 H3
    lines.append("</ul></nav>")
    return "\n".join(lines)

toc_html = build_toc_html(toc_items)

# ── HTML Template ─────────────────────────────────────────────────────────
CSS = r"""
:root {
  --bg:        #0d1117;
  --sidebar-bg:#010409;
  --surface:   #161b22;
  --border:    #30363d;
  --text:      #c9d1d9;
  --text-dim:  #8b949e;
  --heading:   #e6edf3;
  --accent:    #58a6ff;
  --accent2:   #39d0d8;
  --quote-border: #388bfd;
  --strong:    #f0f6fc;
  --code-bg:   #161b22;
  --progress:  #58a6ff;
  --sidebar-w: 260px;
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
#toc { padding: 8px 0 40px; flex: 1; }
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
  background: rgba(88,166,255,0.06);
}
.toc-h2 > .toc-link.active {
  color: var(--accent);
  border-left-color: var(--accent);
  background: rgba(88,166,255,0.08);
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

/* 術語面板開啟時：桌機推擠主內容讓位（無遮罩） */
body.glossary-open #main-wrapper {
  margin-right: 340px;
}

#content {
  max-width: 860px;
  margin: 0 auto;
}

/* ── 標題 ── */
#content h1 {
  font-size: 1.9rem;
  color: var(--heading);
  border-bottom: 2px solid var(--accent);
  padding-bottom: 12px;
  margin-bottom: 28px;
  line-height: 1.35;
}
#content h2 {
  font-size: 1.35rem;
  color: var(--heading);
  border-bottom: 1px solid var(--border);
  padding-bottom: 8px;
  margin-top: 56px;
  margin-bottom: 20px;
  scroll-margin-top: 24px;
}
#content h3 {
  font-size: 1.1rem;
  color: var(--accent);
  margin-top: 32px;
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
  padding: 12px 16px;
  border-left: 4px solid var(--quote-border);
  background: rgba(56,139,253,0.07);
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
#content tbody tr:nth-child(even) { background: var(--bg); }
#content tbody tr:hover { background: rgba(88,166,255,0.05); }

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
    background: rgba(0,0,0,0.5);
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
  background: rgba(22, 27, 34, 0.92);
  border: 1px solid var(--border);
  color: var(--accent);
  border-radius: 24px;
  padding: 8px 16px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
  transition: background 0.15s, box-shadow 0.15s;
  font-family: inherit;
}
#glossary-btn:hover {
  background: rgba(30, 58, 95, 0.95);
  box-shadow: 0 6px 20px rgba(88,166,255,0.2);
}

#glossary-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.45);
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
  background: #0d1117;
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
#glossary-close:hover { color: var(--heading); background: rgba(255,255,255,0.06); }

.gl-list {
  overflow-y: auto;
  flex: 1;
  margin: 0;
  padding: 12px 0 40px;
}
.gl-item {
  padding: 12px 18px;
  border-bottom: 1px solid rgba(48,54,61,0.6);
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
  background: rgba(255,255,255,0.05);
  border-radius: 3px;
  padding: 1px 5px;
  margin-left: 6px;
  vertical-align: middle;
  font-weight: normal;
  letter-spacing: 0.02em;
}
"""

JS = r"""
// ── 閱讀進度條 ───────────────────────────────────────────
const bar = document.getElementById('progress-bar');
window.addEventListener('scroll', () => {
  const total = document.documentElement.scrollHeight - window.innerHeight;
  bar.style.width = total > 0 ? (window.scrollY / total * 100) + '%' : '0%';
}, { passive: true });

// ── TOC: expand/collapse & active highlight ───────────────
const tocLinks = Array.from(document.querySelectorAll('.toc-link'));
const allHeadings = Array.from(document.querySelectorAll('#content h2, #content h3'));

// 點 H2 鏈結展開/收合子清單
document.querySelectorAll('.toc-h2.has-children > .toc-link').forEach(link => {
  link.addEventListener('click', e => {
    const li = link.closest('.toc-h2');
    li.classList.toggle('open');
  });
});

// 初始展開第一個 H2
const firstH2 = document.querySelector('.toc-h2.has-children');
if (firstH2) firstH2.classList.add('open');

// Intersection Observer：追蹤當前可見標題
let activeSlug = null;
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      activeSlug = e.target.id;
      updateActive();
    }
  });
}, { rootMargin: '-10% 0px -80% 0px', threshold: 0 });
allHeadings.forEach(h => observer.observe(h));

function updateActive() {
  tocLinks.forEach(a => a.classList.remove('active'));
  const active = tocLinks.find(a => a.getAttribute('href') === '#' + activeSlug);
  if (!active) return;
  active.classList.add('active');
  // 確保父 H2 也展開
  const parentLi = active.closest('.toc-h2');
  if (parentLi) {
    parentLi.classList.add('open');
    const parentLink = parentLi.querySelector(':scope > .toc-link');
    if (parentLink) parentLink.classList.add('active');
  }
}

// ── 手機選單 ─────────────────────────────────────────────
const sidebar  = document.getElementById('sidebar');
const overlay  = document.getElementById('sidebar-overlay');
const menuBtn  = document.getElementById('menu-btn');

menuBtn.addEventListener('click', () => {
  sidebar.classList.toggle('open');
  overlay.classList.toggle('open');
});
overlay.addEventListener('click', () => {
  sidebar.classList.remove('open');
  overlay.classList.remove('open');
});

// 點 TOC 鏈結後關閉手機側欄
tocLinks.forEach(a => {
  a.addEventListener('click', () => {
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
  });
});

// ── 表格加上橫向滾動包裝 ────────────────────────────────
document.querySelectorAll('#content table').forEach(t => {
  if (t.parentElement.classList.contains('table-wrap')) return;
  const wrap = document.createElement('div');
  wrap.className = 'table-wrap';
  t.parentNode.insertBefore(wrap, t);
  wrap.appendChild(t);
});

// ── 術語速查面板 ─────────────────────────────────────────
const glossaryPanel   = document.getElementById('glossary-panel');
const glossaryBtn     = document.getElementById('glossary-btn');
const glossaryClose   = document.getElementById('glossary-close');
const glossaryOverlay = document.getElementById('glossary-overlay');

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
  const item = document.getElementById('gl-' + termId);
  if (!item) return;
  if (activeGlItem) activeGlItem.classList.remove('gl-highlighted');
  activeGlItem = item;
  item.classList.add('gl-highlighted');
  item.scrollIntoView({ block: 'center', behavior: 'smooth' });
});
"""

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>台灣大嘴黑鱸釣魚生態白皮書</title>
  <meta name="description" content="台灣大嘴黑鱸（Micropterus salmoides）釣魚生態白皮書——氣候、水體、感官、行為全面量化分析">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
{css}
  </style>
</head>
<body>
  <div id="progress-bar"></div>
  <div id="sidebar-overlay"></div>
  <button id="menu-btn" aria-label="開啟目錄">☰</button>

  <aside id="sidebar">
    <div id="sidebar-header">
      <div class="site-title">台灣大嘴黑鱸</div>
      <div class="site-subtitle">釣魚生態白皮書</div>
    </div>
{toc}
  </aside>

  <div id="main-wrapper">
    <article id="content">
{content}
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
html = HTML_TEMPLATE.format(
    css=CSS,
    toc=toc_html,
    content=content_html,
    glossary=glossary_html,
    js=JS,
)

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"✓ 產生完成：{OUT}")
print(f"  TOC 項目：{len(toc_items)} 個（H2: {sum(1 for x in toc_items if x['level']==2)}，H3: {sum(1 for x in toc_items if x['level']==3)}）")
