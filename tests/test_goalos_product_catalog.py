import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_goalos_products as validator


def test_goalos_catalog_has_exactly_nine_valid_products():
    products = validator.load_products()
    assert len(products) == 9
    assert validator.validate_catalog(products) == []
