import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import guard_no_paid_product_files as guard


def test_no_forbidden_paid_product_zip_files():
    assert guard.find_offenders() == []


def test_forbidden_paid_zip_under_releases_is_reported(tmp_path, monkeypatch):
    fake_root = tmp_path
    releases = fake_root / "releases"
    releases.mkdir()
    offender = releases / "GoalOS_AI_Efficiency_Sprint_TEST.zip"
    offender.write_bytes(b"not a real paid package")

    allowed = releases / "AEP-001"
    allowed.mkdir()
    allowed_archive = allowed / "GoalOS_AI_Efficiency_Sprint_ALLOWED.zip"
    allowed_archive.write_bytes(b"allowed standards archive exception")

    monkeypatch.setattr(guard, "ROOT", fake_root)
    assert guard.find_offenders() == [Path("releases/GoalOS_AI_Efficiency_Sprint_TEST.zip")]
