import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import guard_no_paid_product_files as guard


def test_no_forbidden_paid_product_zip_files():
    assert guard.find_offenders() == []


def test_releases_outside_aep001_are_public_guard_scope(tmp_path, monkeypatch):
    releases = tmp_path / "releases"
    releases.mkdir()
    (releases / "GoalOS_AI_Efficiency_Sprint.zip").write_bytes(b"forbidden")
    allowed = releases / "AEP-001"
    allowed.mkdir()
    (allowed / "GoalOS_AI_Efficiency_Sprint.zip").write_bytes(b"allowed public standard archive exception")

    monkeypatch.setattr(guard, "ROOT", tmp_path)

    assert guard.find_offenders() == [Path("releases/GoalOS_AI_Efficiency_Sprint.zip")]


def test_paid_zip_extension_matching_is_case_insensitive(tmp_path, monkeypatch):
    site = tmp_path / "site"
    docs = tmp_path / "docs"
    site.mkdir()
    docs.mkdir()
    (site / "GoalOS_AI_Efficiency_Sprint.ZIP").write_bytes(b"forbidden uppercase suffix")
    (docs / "GoalOS_SME_AI_Adoption.Zip").write_bytes(b"forbidden mixed-case suffix")

    monkeypatch.setattr(guard, "ROOT", tmp_path)

    assert guard.find_offenders() == [
        Path("docs/GoalOS_SME_AI_Adoption.Zip"),
        Path("site/GoalOS_AI_Efficiency_Sprint.ZIP"),
    ]
