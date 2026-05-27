"""
從 .docx 提取純文字，輸出為 supdoc_text.txt（在當前工作目錄）。
用法：python -X utf8 extract_docx.py "{完整docx路徑}"
"""
import zipfile, re, sys

sys.stdout.reconfigure(encoding='utf-8')
if len(sys.argv) < 2:
    print('Usage: python -X utf8 extract_docx.py "<docx_path>"')
    sys.exit(1)

fname = sys.argv[1]
with zipfile.ZipFile(fname) as z:
    xml = z.read('word/document.xml').decode('utf-8')

text = re.sub(r'<w:p\b[^>]*>', '\n', xml)
text = re.sub(r'<[^>]+>', '', text)
lines = [l.strip() for l in text.splitlines() if l.strip()]
text = '\n'.join(lines)

with open('supdoc_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print('Done, lines:', len(lines), '  chars:', len(text))
