#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
cat=yaml.safe_load((ROOT/'docs/data/goalos_catalog.yml').read_text(encoding='utf-8'))
errors=[]
for item in cat['product_ladder']:
    needle=[item['price'], item['name'], item['version']]
    for n in needle:
        if n not in (ROOT/'README.md').read_text(encoding='utf-8'):
            errors.append(f'README missing catalog value: {n}')
    page=ROOT/'site/products'/item['slug']/'index.html'
    if not page.exists(): errors.append(f'Missing product page: {page.relative_to(ROOT)}'); continue
    text=page.read_text(encoding='utf-8')
    for n in needle:
        if n not in text: errors.append(f'{page.relative_to(ROOT)} missing catalog value: {n}')
for p in (ROOT/'site').rglob('*.html'):
    if '_archive' in p.parts: continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    rel=p.relative_to(ROOT)
    if '<title>' not in text: errors.append(f'{rel} missing title')
    if not re.search(r"name=[\"']description[\"']", text): errors.append(f'{rel} missing description')
    if 'QUEBEC.AI' not in text or '⚜️✨' not in text: errors.append(f'{rel} missing QUEBEC.AI ⚜️✨ identity')
    if 'quebecaisealv5.png' not in text: errors.append(f'{rel} missing seal reference')
    if text.count('data-goalos-v10-nav')>1: errors.append(f'{rel} has more than one canonical nav')
    if text.count('data-goalos-v10-footer')>1: errors.append(f'{rel} has more than one canonical footer')
    if re.search(r'GOALOS-COMPLETE-NAV|GOALOS-COMPLETE-FOOTER|GOALOS-PRODUCT-LADDER-NAV|GOALOS-PRODUCT-LADDER-FOOTER|GOALOS-UNIFIED-SHELL|GOALOS-UNIFIED-FOOTER|GOALOS-CLOUD-MVP', text): errors.append(f'{rel} has old shell marker')

    for match in re.finditer(r'href=["\'](/proof-gradient/[^"\'#?]*)', text):
        url=match.group(1)
        rel_url=url[len('/proof-gradient/'):]
        if not rel_url:
            continue
        target=ROOT/'site'/rel_url
        ok=(target/'index.html').exists() if url.endswith('/') else (target.exists() or target.with_suffix('.html').exists())
        if not ok:
            errors.append(f'{rel} has broken internal link: {url}')
for req in ['site/assets/quebecaisealv5.png','site/favicon.png','site/assets/apple-touch-icon.png','site/assets/icon-192.png','site/assets/icon-512.png','site/site.webmanifest','site/assets/brand-assets-v10.json','site/brand/visual-system/index.html']:
    if not (ROOT/req).exists(): errors.append(f'Missing required asset/page: {req}')
if cat['safe_boundary_en'] not in (ROOT/'README.md').read_text(encoding='utf-8'): errors.append('README missing safe-boundary language')
if errors:
    print('GoalOS catalog validation failed:'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print('✅ GoalOS catalog, public pages, shell, seal, and safe boundary validate.')
