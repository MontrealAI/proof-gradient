import json, sys
from pathlib import Path

LEVELS = {
    0: ['commitment_record','execution_summary','evidence_inventory','claim_boundary'],
    1: ['manifest','claims_matrix','commitment_record','execution_summary','evidence_inventory','evaluation_results','rollback_plan','claim_boundary'],
    2: ['tool_use_ledger','policy_approval_ledger','cost_latency_ledger','risk_ledger','selection_certificate'],
    3: ['rollout_canary_plan','public_safe_report'],
    4: ['private_appendix']
}

def main(path):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    level=0; report={}
    for lv, keys in LEVELS.items():
        ok=all(k in data for k in keys)
        report[f'level_{lv}']={'passed':ok,'required':keys}
        if ok: level=lv
    print(json.dumps({'conformance_level':level,'report':report}, indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main(sys.argv[1]))
