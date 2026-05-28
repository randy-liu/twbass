"""
執行這個腳本來把 Skill 打包成 .skill 檔案。
打包完就可以在 Cowork 裡點選「Save skill」安裝。
"""
import zipfile
import os
import pathlib

base = pathlib.Path(__file__).parent

skills = [
    'twbass-audit',           # 研究卷審查（主要技能）
    'twbass-pipeline-manager', # Pipeline 管理
    'gemini-plan-review',     # Gemini plan 審查
    # 'twbass-tactical-advisor' # 已棄用，改用 MCP 方式
]

for skill_name in skills:
    src_dir = base / skill_name
    out_file = base / (skill_name + '.skill')

    if not src_dir.exists():
        print(f'找不到目錄：{src_dir}')
        continue

    with zipfile.ZipFile(out_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in src_dir.rglob('*'):
            if file_path.is_file():
                arcname = file_path.relative_to(base)
                zf.write(file_path, arcname)
                print(f'  加入：{arcname}')

    print(f'✅ 已打包：{out_file.name}')

print('\n完成！請在 Cowork 裡點選 .skill 檔案來安裝。')
input('按 Enter 關閉...')
