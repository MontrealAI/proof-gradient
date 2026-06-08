#!/usr/bin/env python3
"""Shared GoalOS public-site validation rules.

This module is the single source of truth for public deploy classification,
canonical shell requirements, standalone proof-page handling, public AEP package
allowlisting, and paid/private artifact blocking. GitHub Actions and local
validators should import these rules instead of copying validation regexes into
workflow YAML.
"""
from __future__ import annotations

from pathlib import Path, PurePosixPath
import re

PUBLIC_AEP_PACKAGE_RE = re.compile(
    r"^standards/AEP-[0-9]{3}/complete-package\.zip$",
    re.IGNORECASE,
)

STANDALONE_PROOF_RE = re.compile(
    r"^(?:proofs/.+\.html|rsi-[a-z0-9-]+\.html|[a-z0-9-]+-proof\.html|[a-z0-9-]*readiness[a-z0-9-]*\.html)$",
    re.IGNORECASE,
)

APP_PAGE_RE = re.compile(
    r"^app/goalos-cloud-mvp/.*\.html$",
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
    ".md", ".html", ".json", ".txt", ".yml", ".yaml",
    ".css", ".js", ".svg", ".png", ".jpg", ".jpeg",
    ".webp", ".gif", ".avif", ".xml", ".ico",
}

OLD_SHELL_MARKERS = [
    "GOALOS-COMPLETE-NAV",
    "GOALOS-COMPLETE-FOOTER",
    "GOALOS-PRODUCT-LADDER-NAV",
    "GOALOS-PRODUCT-LADDER-FOOTER",
    "GOALOS-UNIFIED-SHELL",
    "GOALOS-UNIFIED-FOOTER",
    "GOALOS-CLOUD-MVP:START",
    "GOALOS-CLOUD-MVP-V02:START",
]

CANONICAL_SHELL_MARKER = "GOALOS-CANONICAL-SHELL:START"
CANONICAL_FOOTER_MARKER = "GOALOS-CANONICAL-FOOTER:START"

# Compatibility aliases used by existing scripts.
CANONICAL_NAV_MARKER = CANONICAL_SHELL_MARKER

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


def normalize_rel(path: str | Path) -> str:
    rel = str(path).replace("\\", "/").lstrip("./")
    while rel.startswith("/"):
        rel = rel[1:]
    return PurePosixPath(rel).as_posix()


def strip_public_root(rel: str | Path) -> str:
    rel = normalize_rel(rel)
    for prefix in ("site/", "public/"):
        if rel.lower().startswith(prefix):
            return rel[len(prefix):]
    return rel


def is_public_aep_package(rel: str | Path) -> bool:
    return bool(PUBLIC_AEP_PACKAGE_RE.match(strip_public_root(rel)))


def has_standalone_marker(text: str) -> bool:
    return (
        "GOALOS-STANDALONE-PROOF" in text
        or 'name="goalos-page-type" content="standalone-proof"' in text
        or "name='goalos-page-type' content='standalone-proof'" in text
        or "data-goalos-standalone" in text
    )


def is_standalone_proof_page(rel: str | Path, text: str = "") -> bool:
    rel = strip_public_root(rel)
    return bool(STANDALONE_PROOF_RE.match(rel)) or has_standalone_marker(text)


def is_app_page(rel: str | Path) -> bool:
    return bool(APP_PAGE_RE.match(strip_public_root(rel)))


def requires_canonical_shell(rel: str | Path, text: str = "") -> bool:
    rel = strip_public_root(rel)
    if not rel.endswith(".html"):
        return False
    if is_app_page(rel):
        return False
    if is_standalone_proof_page(rel, text):
        return False
    return True


def is_blocked_paid_or_private_artifact(rel: str | Path) -> bool:
    rel = strip_public_root(rel)
    rel_lower = rel.lower()
    name = PurePosixPath(rel_lower).name
    suffix = PurePosixPath(rel_lower).suffix

    if is_public_aep_package(rel):
        return False

    if suffix == ".zip":
        return True

    if any(term in rel_lower or term in name for term in PRIVATE_TERMS):
        if suffix not in SAFE_PUBLIC_EXTENSIONS:
            return True

    return False


def classify_html_page(rel: str | Path, text: str = "") -> str:
    rel = strip_public_root(rel)
    if is_app_page(rel):
        return "app_page"
    if is_standalone_proof_page(rel, text):
        return "standalone_proof_page"
    if rel.endswith(".html"):
        return "canonical_page"
    return "other"


def page_class(rel: str | Path, text: str = "") -> str:
    """Classify public HTML pages and public artifacts for diagnostics."""
    rel = strip_public_root(rel)
    html_class = classify_html_page(rel, text)
    if html_class != "other":
        return html_class
    if is_public_aep_package(rel):
        return "aep_standard_package"
    if is_blocked_paid_or_private_artifact(rel):
        return "blocked_paid_artifact"
    return "public_asset"


def has_old_shell_marker(text: str) -> bool:
    return any(marker in text for marker in OLD_SHELL_MARKERS)


def has_title(text: str) -> bool:
    return bool(TITLE_RE.search(text))


def has_meta_description(text: str) -> bool:
    return bool(META_DESCRIPTION_RE.search(text))


def has_goalos_or_proof_gradient_escape(text: str) -> bool:
    lowered = text.lower()
    return "/proof-gradient/" in lowered and ("goalos" in lowered or "proof gradient" in lowered)


def has_quebec_ai_visible_brand(text: str) -> bool:
    return "QUEBEC.AI" in text or "QUEBEC AI" in text or "⚜️✨" in text or "quebecaisealv5" in text


def contains_blocked_claim_language(text: str) -> bool:
    return bool(BLOCKED_CLAIM_RE.search(text))
