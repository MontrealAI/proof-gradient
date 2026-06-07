#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
roots=[ROOT/'site', ROOT/'public']
blocked=re.compile(r'(buyer|buyer_official|complete_bundle|delivery_kit|seller_assets|master_pack|commercialization_ready|quick_launch|opulent_institutional|institutional_boardroom|implementation_sprint|enterprise_rsi_pilot|workshop_v|buyer_facilitator|private|paid|internal)', re.I)
errors=[]
for root in roots:
    if not root.exists(): continue
    for p in root.rglob('*'):
        if not p.is_file() or '_archive' in p.parts: continue
        rel=p.relative_to(ROOT).as_posix()
        allowed_zip=bool(re.fullmatch(r'site/standards/AEP-\d{3}/complete-package\.zip', rel))
        if p.suffix.lower()=='.zip' and not allowed_zip:
            errors.append(f'Blocked ZIP outside public AEP package exception: {rel}')
        if blocked.search(p.name) and not allowed_zip:
            errors.append(f'Blocked paid/private-looking filename: {rel}')
if errors:
    print('Paid/private artifact guard failed:')
    print('\n'.join(f'- {e}' for e in errors))
    sys.exit(1)
print('✅ No paid/private public artifacts found. Public AEP complete-package.zip files are allowed.')
