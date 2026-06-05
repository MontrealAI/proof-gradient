import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import guard_no_paid_product_files as guard


def test_no_forbidden_paid_product_zip_files():
    assert guard.find_offenders() == []
