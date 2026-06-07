import json
import sys
from pathlib import Path

REQUIRED_TOP = [
    'manifest','claims_matrix','commitment_record','execution_summary','evidence_inventory',
    'evaluation_results','selection_certificate','rollback_plan','claim_boundary'
]

def validate(path: str) -> int:
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    errors=[]
    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f'missing top-level field: {key}')
    manifest=data.get('manifest',{})
    if manifest.get('protocol')!='AEP-002':
        errors.append('manifest.protocol must be AEP-002')
    if not data.get('claims_matrix'):
        errors.append('claims_matrix must not be empty')
    cb=data.get('claim_boundary',{})
    if 'not_claimed' not in cb:
        errors.append('claim_boundary.not_claimed is required')
    if data.get('manifest',{}).get('confidentiality_class')=='public':
        for ev in data.get('evidence_inventory',[]):
            if ev.get('access_class') in ('private','protected','restricted') and ev.get('public_safe') is not True:
                errors.append(f'public docket contains non-public-safe evidence: {ev.get("evidence_id")}')
    if errors:
        print('AEP-002 docket invalid:')
        for e in errors: print('-',e)
        return 1
    print(f'AEP-002 docket valid: {path}')
    return 0

if __name__=='__main__':
    if len(sys.argv)!=2:
        print('usage: python validate_evidence_docket.py docket.json')
        raise SystemExit(2)
    raise SystemExit(validate(sys.argv[1]))
