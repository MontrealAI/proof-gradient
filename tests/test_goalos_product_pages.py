import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_site_links
import validate_goalos_products as validator


def test_goalos_product_pages_exist_and_link_aep001():
    products = validator.load_products()
    assert validator.validate_pages(products) == []


def test_site_local_links_resolve():
    assert check_site_links.find_broken() == []
