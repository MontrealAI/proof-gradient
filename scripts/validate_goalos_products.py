#!/usr/bin/env python3
"""Validate the GoalOS product catalog and generated public pages."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "goalos_products.json"
SITE = ROOT / "site"
REQUIRED_FIELDS = {
    "id", "name_en", "name_fr", "price_public", "audience_en", "audience_fr",
    "promise_en", "promise_fr", "delivery_en", "delivery_fr", "cta_type",
    "cta_label_en", "cta_label_fr", "cta_url_placeholder", "public_page_slug",
    "claim_boundary_level",
}
BILINGUAL_FIELDS = ["name", "audience", "promise", "delivery", "cta_label"]
URL_SAFE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BUY_NOW_TERMS = re.compile(r"\b(buy now|add to cart|checkout now|get the sprint|get the team pack|obtenir le sprint|obtenir le team pack)\b", re.I)
HIGH_TICKET_LEVELS = {"service", "enterprise", "sovereign", "sovereign_empire"}


def load_products() -> list[dict]:
    with CATALOG.open(encoding="utf-8") as fh:
        return json.load(fh)


def validate_catalog(products: list[dict]) -> list[str]:
    errors: list[str] = []
    if len(products) != 9:
        errors.append(f"Expected exactly 9 products; found {len(products)}")
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    for index, product in enumerate(products, start=1):
        missing = sorted(REQUIRED_FIELDS - product.keys())
        if missing:
            errors.append(f"Product {index} missing fields: {', '.join(missing)}")
        for base in BILINGUAL_FIELDS:
            for suffix in ("en", "fr"):
                key = f"{base}_{suffix}"
                if not str(product.get(key, "")).strip():
                    errors.append(f"Product {index} missing bilingual field {key}")
        product_id = product.get("id", "")
        slug = product.get("public_page_slug", "")
        if not URL_SAFE.match(product_id):
            errors.append(f"Product {index} id is not URL-safe: {product_id}")
        if not URL_SAFE.match(slug):
            errors.append(f"Product {index} public_page_slug is not URL-safe: {slug}")
        if product_id in seen_ids:
            errors.append(f"Duplicate product id: {product_id}")
        if slug in seen_slugs:
            errors.append(f"Duplicate public_page_slug: {slug}")
        seen_ids.add(product_id)
        seen_slugs.add(slug)
        if product.get("cta_type") not in {"buy", "inquiry"}:
            errors.append(f"Product {index} has invalid cta_type: {product.get('cta_type')}")
        if product.get("claim_boundary_level") in HIGH_TICKET_LEVELS and product.get("cta_type") != "inquiry":
            errors.append(f"High-ticket product {product_id} must use inquiry CTA type")
        if product.get("claim_boundary_level") in HIGH_TICKET_LEVELS:
            cta_text = f"{product.get('cta_label_en', '')} {product.get('cta_label_fr', '')}"
            if BUY_NOW_TERMS.search(cta_text):
                errors.append(f"High-ticket product {product_id} uses buy-now CTA language: {cta_text}")
    return errors


def validate_pages(products: list[dict]) -> list[str]:
    errors: list[str] = []
    hub = SITE / "products" / "index.html"
    if not hub.exists():
        errors.append("Missing product hub page: site/products/index.html")
    for product in products:
        page = SITE / "products" / product["public_page_slug"] / "index.html"
        if not page.exists():
            errors.append(f"Missing product page: {page.relative_to(ROOT)}")
            continue
        text = page.read_text(encoding="utf-8")
        if "standards/AEP-001/" not in text:
            errors.append(f"Product page missing AEP-001 link: {page.relative_to(ROOT)}")
        if "Claim boundary" not in text and "Limite des revendications" not in text:
            errors.append(f"Product page missing claim boundary: {page.relative_to(ROOT)}")
        if product.get("claim_boundary_level") in HIGH_TICKET_LEVELS and BUY_NOW_TERMS.search(text):
            # Ignore shared labels for Product 1/2 that may appear in navigation? Individual high-ticket pages should not contain them.
            errors.append(f"High-ticket page contains buy-now CTA language: {page.relative_to(ROOT)}")
    return errors


def run() -> int:
    products = load_products()
    errors = validate_catalog(products) + validate_pages(products)
    if errors:
        print("GoalOS product validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("GoalOS product catalog and pages validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
