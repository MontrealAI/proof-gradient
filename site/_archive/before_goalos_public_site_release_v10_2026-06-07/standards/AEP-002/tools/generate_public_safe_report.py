import json, sys
from pathlib import Path

def main(src, dst):
    data=json.loads(Path(src).read_text(encoding='utf-8'))
    report=data.get('public_safe_report') or {}
    cb=data.get('claim_boundary') or {}
    md = ['# Public-Safe Report', '']
    for key in ['what_was_tested','what_happened','evidence_summary']:
        md += [f'## {key.replace("_"," ").title()}', str(report.get(key,'Not provided.')), '']
    md += ['## What Is Claimed'] + [f'- {x}' for x in report.get('what_is_claimed', cb.get('supported_claims', []))] + ['']
    md += ['## What Is Not Claimed'] + [f'- {x}' for x in report.get('what_is_not_claimed', cb.get('not_claimed', []))] + ['']
    md += ['## Claim Boundary', cb.get('public_boundary','Not provided.'), '']
    Path(dst).write_text('\n'.join(md), encoding='utf-8')
    print(dst)

if __name__=='__main__':
    if len(sys.argv)!=3:
        print('usage: python generate_public_safe_report.py docket.json report.md')
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
