"""Fill in YouTube links after upload.
1. Put each video ID (the part after watch?v=) into tools/links.json, e.g. "E05": "dQw4w9WgXcQ".
2. Run from the repo root:  python3 tools/set_links.py
Placeholders YOUTUBE_ID_E## in guides/, docs/ and README.md are replaced. Run it again whenever you add IDs."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
cfg = json.loads((root / 'tools' / 'links.json').read_text())
pairs = {f'YOUTUBE_ID_{k}': v for k, v in cfg['videos'].items() if v}
if cfg.get('github_user') and cfg['github_user'] != 'GITHUB_USER':
    pairs['GITHUB_USER'] = cfg['github_user']
n = 0
for p in list(root.glob('guides/*.md')) + list(root.glob('docs/**/*.html')) + [root / 'README.md']:
    t = p.read_text(encoding='utf-8'); u = t
    for a, b in pairs.items(): u = u.replace(a, b)
    if u != t: p.write_text(u, encoding='utf-8'); n += 1
print(f'updated {n} files')
