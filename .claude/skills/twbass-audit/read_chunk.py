"""
分段讀取 supdoc_text.txt，避免超過 token 上限。
用法：python -X utf8 read_chunk.py [start] [count]
預設：start=0, count=300
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')
start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
count = int(sys.argv[2]) if len(sys.argv) > 2 else 300

with open('supdoc_text.txt', encoding='utf-8') as f:
    lines = f.readlines()

total = len(lines)
end = min(start + count, total)
print(f'Total lines: {total} | Reading: {start}–{end}')
print(''.join(lines[start:end]))
if end < total:
    print(f'\n[繼續：python -X utf8 ".claude/skills/twbass-audit/read_chunk.py" {end} {count}]')
else:
    print('\n[全文讀取完畢]')
