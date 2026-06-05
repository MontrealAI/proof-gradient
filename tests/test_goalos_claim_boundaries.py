import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import repo_claim_boundary_check as claims


def test_goalos_public_claim_boundaries():
    assert claims.find_violations() == []
