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
    js=JS,
)

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"✓ 產生完成：{OUT}")
print(f"  TOC 項目：{len(toc_items)} 個（H2: {sum(1 for x in toc_items if x['level']==2)}，H3: {sum(1 for x in toc_items if x['level']==3)}）")
