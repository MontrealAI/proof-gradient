#!/usr/bin/env python3
"""Shared GoalOS public-site validation rules.

This module is the single source of truth for public deploy classification,
canonical shell requirements, standalone proof-page handling, and paid/private
artifact blocking. GitHub Actions and local validators should import these rules
instead of copying allowlists into workflow YAML.
"""
from __future__ import annotations

from pathlib import PurePosixPath
import re

PUBLIC_AEP_PACKAGE_RE = re.compile(
    r"^standards/AEP-[0-9]{3}/complete-package\.zip$",
    re.IGNORECASE,
)

STANDALONE_PROOF_RE = re.compile(
    r"^(rsi-ai-first-[a-z0-9-]+-proof\.html|proofs/.+\.html)$",
    re.IGNORECASE,
)

APP_PAGE_RE = re.compile(
    r"^app/goalos-cloud-mvp/.+\.html$",
    re.IGNORECASE,
)

PRIVATE_TERMS = [
    "buyer",
    "buyer_official",
    "complete_bundle",
    "delivery_kit",
    "seller_assets",
    "master_pack",
    "commercialization_ready",
    "quick_launch",
    "opulent_institutional",
    "institutional_boardroom",
    "implementation_sprint",
    "enterprise_rsi_pilot",
    "workshop_v",
    "buyer_facilitator",
    "private",
    "paid",
]

SAFE_PUBLIC_EXTENSIONS = {
    ".md",
    ".html",
    ".json",
    ".txt",
    ".yml",
    ".yaml",
    ".css",
    ".js",
    ".svg",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".avif",
}

CANONICAL_NAV_MARKER = "GOALOS-CANONICAL-SHELL:START"
CANONICAL_FOOTER_MARKER = "GOALOS-CANONICAL-FOOTER:START"
OLD_SHELL_MARKER_RE = re.compile(
    r"<!--\s*/?\s*GOALOS-(COMPLETE-NAV|COMPLETE-FOOTER|PRODUCT-LADDER-NAV|PRODUCT-LADDER-FOOTER|UNIFIED-SHELL|UNIFIED-FOOTER|CLOUD-MVP(?::START|(?:[^a-z0-9-]|$)))",
    re.IGNORECASE,
)
LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
TITLE_RE = re.compile(r"<title>\s*[^<\s][^<]*</title>", re.IGNORECASE | re.DOTALL)
META_DESCRIPTION_RE = re.compile(
    r"<meta\s+[^>]*name=[\"']description[\"'][^>]*content=[\"'][^\"']+[\"'][^>]*>",
    re.IGNORECASE | re.DOTALL,
)

BLOCKED_CLAIM_RE = re.compile(
    r"(uncontrolled\s+model\s+self[- ]modification|model\s+self[- ]modification|modif(?:y|ies|ied)\s+its\s+own\s+(?:weights|parameters)|guaranteed\s+investment\s+returns?)",
    re.IGNORECASE,
)

REQUIRED_ICON_PATHS = (
    "assets/quebecaisealv5.png",
    "favicon.png",
    "assets/apple-touch-icon.png",
)
BRAND_MANIFEST_PATH = "site.webmanifest"
BRAND_ASSET_MANIFEST_PATH = "assets/brand-assets-v8.json"


def normalize_rel(path: object) -> str:
    """Normalize a repository or public-root relative path to POSIX form."""
    rel = PurePosixPath(str(path).replace("\\", "/")).as_posix().lstrip("./")
    if rel.startswith("site/"):
        rel = rel.removeprefix("site/")
    elif rel.startswith("public/"):
        rel = rel.removeprefix("public/")
    return rel


def is_public_aep_package(rel: object) -> bool:
    rel = normalize_rel(rel)
    return bool(PUBLIC_AEP_PACKAGE_RE.match(rel))


def has_standalone_marker(text: str) -> bool:
    return (
        "GOALOS-STANDALONE-PROOF" in text
        or 'name="goalos-page-type" content="standalone-proof"' in text
        or "name='goalos-page-type' content='standalone-proof'" in text
        or "data-goalos-standalone" in text
    )


def is_standalone_proof_page(rel: object, text: str = "") -> bool:
    rel = normalize_rel(rel)
    return bool(STANDALONE_PROOF_RE.match(rel)) or has_standalone_marker(text)


def is_app_page(rel: object) -> bool:
    rel = normalize_rel(rel)
    return bool(APP_PAGE_RE.match(rel))


def page_class(rel: object, text: str = "") -> str:
    rel = normalize_rel(rel)
    if is_app_page(rel):
        return "app_page"
    if is_standalone_proof_page(rel, text):
        return "standalone_proof_page"
    if rel.lower().endswith(".html"):
        return "canonical_page"
    if is_public_aep_package(rel):
        return "aep_standard_package"
    if is_blocked_paid_or_private_artifact(rel):
        return "blocked_paid_artifact"
    return "public_asset"


def requires_canonical_shell(rel: object, text: str = "") -> bool:
    rel = normalize_rel(rel)
    if not rel.lower().endswith(".html"):
        return False
    if is_app_page(rel):
        return False
    if is_standalone_proof_page(rel, text):
        return False
    return True


def is_blocked_paid_or_private_artifact(rel: object) -> bool:
    rel = normalize_rel(rel)
    name = PurePosixPath(rel).name.lower()
    suffix = PurePosixPath(rel).suffix.lower()

    if is_public_aep_package(rel):
        return False

    if suffix == ".zip":
        return True

    if any(term in name for term in PRIVATE_TERMS):
        if suffix not in SAFE_PUBLIC_EXTENSIONS:
            return True

    return False


def has_title(text: str) -> bool:
    return bool(TITLE_RE.search(text))


def has_meta_description(text: str) -> bool:
    return bool(META_DESCRIPTION_RE.search(text))


def has_goalos_or_proof_gradient_escape(text: str) -> bool:
    lowered = text.lower()
    return "/proof-gradient/" in lowered and ("goalos" in lowered or "proof gradient" in lowered)


def has_quebec_ai_visible_brand(text: str) -> bool:
    return "QUEBEC.AI" in text or "QUEBEC AI" in text or "⚜️" in text


def contains_blocked_claim_language(text: str) -> bool:
    return bool(BLOCKED_CLAIM_RE.search(text))
