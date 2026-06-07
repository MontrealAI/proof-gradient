import json, sys
from pathlib import Path
FORBIDDEN = ["api_key", "password", "secret=", "BEGIN PRIVATE KEY", "raw prompt:", "full trace:", "ssn"]

def audit(report):
    issues=[]
    text=json.dumps(report).lower()
    for term in FORBIDDEN:
        if term.lower() in text:
            issues.append(f"forbidden leakage pattern found: {term}")
    for entry in report.get("redaction_ledger", []):
        if entry.get("after_disclosure_class") not in {"public","forbidden","embargoed"}:
            issues.append(f"redaction {entry.get('redaction_id')} not public-safe: {entry.get('after_disclosure_class')}")
    if report.get("publication_approval", {}).get("approval_status") != "approved":
        issues.append("publication approval is not approved")
    return issues

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python public_safe_redaction_audit.py report.json")
        raise SystemExit(2)
    report=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    issues=audit(report)
    if issues:
        print("Redaction audit failed:")
        for issue in issues: print(f"- {issue}")
        raise SystemExit(1)
    print("Redaction audit passed.")
