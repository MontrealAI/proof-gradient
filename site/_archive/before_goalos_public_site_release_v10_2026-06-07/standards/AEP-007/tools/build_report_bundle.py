import json, hashlib, sys
from pathlib import Path

def sha(path):
    h=hashlib.sha256(); h.update(Path(path).read_bytes()); return "sha256:"+h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python build_report_bundle.py out_bundle.json asset1 [asset2 ...]")
        raise SystemExit(2)
    assets=[]
    for p in sys.argv[2:]:
        assets.append({"path":str(p),"hash":sha(p),"type":Path(p).suffix.lstrip('.')})
    bundle={"bundle_id":"bundle_"+hashlib.sha256(json.dumps(assets, sort_keys=True).encode()).hexdigest()[:12],"schema":"AEP-007-REPORT-BUNDLE","schema_version":"1.2","report_id":"","report_hash":"","assets":assets,"created_at":"generated"}
    Path(sys.argv[1]).write_text(json.dumps(bundle, indent=2), encoding="utf-8")
    print(sys.argv[1])
