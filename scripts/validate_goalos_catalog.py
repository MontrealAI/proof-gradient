#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/'docs/data/goalos_catalog.yml'
SHOP='https://www.quebecartificialintelligence.com/shop'
PRODUCTS=[('$49','GoalOS AI Efficiency Sprint Kit'),('$199','GoalOS RSI Lite'),('$997','GoalOS Proof Room Lite / Department Pack'),('$2,500+','GoalOS RSI Sprint Workshop'),('$9,500+','GoalOS Proof Room Implementation Sprint'),('$49,000+','GoalOS Enterprise RSI Pilot')]
BAD_PHRASES=['guaranteed ROI','guaranteed revenue','price target','passive income','guaranteed resale value','profit promise','revenue share','yield farming']
def read(p): return p.read_text(encoding='utf-8',errors='ignore') if p.exists() else ''
def main():
    errors=[]
    if not CAT.exists(): errors.append('missing docs/data/goalos_catalog.yml')
    cat=read(CAT); readme=read(ROOT/'README.md')
    docs='\n'.join(read(p) for p in (ROOT/'docs').rglob('*.md')) if (ROOT/'docs').exists() else ''
    corpus=readme+'\n'+docs
    for price,name in PRODUCTS:
        if price not in cat or name not in cat: errors.append(f'catalog missing product {price} {name}')
        if price not in readme or name not in readme: errors.append(f'README missing product {price} {name}')
    required=['GoalOS does not modify base AI models','$JOBS is additive','does not replace the GoalOS product ladder','not audited','not mainnet authorized','Base Sepolia first','not legally approved','not tax reviewed','not guaranteed non-security','Proof Card 001','autonomous GitHub Actions','Do not manually bypass','not full enterprise SaaS yet','mainnet gate']
    for phrase in required:
        if phrase.lower() not in corpus.lower(): errors.append(f'missing required language: {phrase}')
    if SHOP not in corpus: errors.append('missing shop URL')
    unsafe=[r'audited\s+and\s+mainnet',r'\bis\s+guaranteed\s+non-security',r'full\s+enterprise\s+SaaS\s+is\s+complete',r'\bis\s+legally\s+approved',r'tax\s+reviewed\s+and\s+approved']
    for pat in unsafe:
        if re.search(pat, corpus, re.I): errors.append(f'unsafe or contradictory claim pattern: {pat}')
    for p in (ROOT/'site').rglob('*.zip') if (ROOT/'site').exists() else []:
        rel=p.relative_to(ROOT/'site').as_posix()
        if not re.fullmatch(r'standards/AEP-\d{3}/complete-package\.zip', rel): errors.append(f'paid/private zip in public deploy root: site/{rel}')
    for p in [ROOT/'README.md', *(ROOT/'docs').rglob('*.md')]:
        text=read(p)
        for m in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target=m.split()[0].strip('<>')
            if target.endswith('.zip') and 'standards/AEP-' not in target: errors.append(f'public paid-product zip link in {p.relative_to(ROOT)}: {target}')
    if errors:
        print('GoalOS catalog validation failed:', file=sys.stderr)
        print('\n'.join('- '+e for e in errors), file=sys.stderr); return 1
    print('GoalOS catalog validation passed.'); return 0
if __name__=='__main__': raise SystemExit(main())
