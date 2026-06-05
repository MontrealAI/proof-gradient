import json
import sys
from pathlib import Path

def audit(cert):
    findings = []
    if cert.get("decision") in {"promote", "approve_canary"} and not cert.get("rollback_plan", {}).get("rollback_target"):
        findings.append("release decision without rollback target")
    if cert.get("decision") == "promote" and cert.get("canary_plan", {}).get("canary_required"):
        findings.append("promote decision should not still require canary")
    if cert.get("challenge_record", {}).get("challenge_status") == "unresolved":
        findings.append("decision with unresolved challenge")
    if not cert.get("claim_boundary", {}).get("does_not_support"):
        findings.append("missing not-claimed boundary")
    return findings

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python selection_gate_audit.py certificate.json")
        raise SystemExit(2)
    cert = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    findings = audit(cert)
    if findings:
        print("audit findings:")
        for f in findings:
            print(f"- {f}")
        raise SystemExit(1)
    print("audit passed")
