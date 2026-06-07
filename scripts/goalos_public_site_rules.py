#!/usr/bin/env python3
"""Shared GoalOS public-site validation rules.

This module is the single source of truth for public HTML classification,
AEP package allowlisting, paid/private artifact blocking, and reusable link /
brand checks. GitHub Actions should call validation scripts that import this
module instead of embedding duplicate shell or paid-file logic in YAML.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urlparse

PUBLIC_AEP_PACKAGE_RE = re.compile(
    r"^standards/AEP-[0-9]{3}/complete-package\.zip$",
    re.IGNORECASE,
)

STANDALONE_PROOF_RE = re.compile(
    r"^(rsi-ai-first-[a-z0-9-]+-proof\.html|proofs/.+\.html)$",
    re.IGNORECASE,
)

APP_PAGE_RE = re.compile(
    r"^app/goalos-cloud-mvp/(?:.+\.html|index\.html)$",
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
    ".webp", ".gif", ".avif",
}

CANONICAL_NAV_MARKER = "GOALOS-CANONICAL-SHELL:START"
CANONICAL_FOOTER_MARKER = "GOALOS-CANONICAL-FOOTER:START"
OLD_SHELL_MARKERS = re.compile(
    r"<!--\s*/?\s*GOALOS-(COMPLETE-NAV|COMPLETE-FOOTER|PRODUCT-LADDER-NAV|"
    r"PRODUCT-LADDER-FOOTER|UNIFIED-SHELL|UNIFIED-FOOTER|CLOUD-MVP(?:[^a-z0-9-]|$))",
    re.IGNORECASE,
)
LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
TITLE_RE = re.compile(r"<title\b[^>]*>\s*[^<]+\s*</title>", re.IGNORECASE | re.DOTALL)
META_DESCRIPTION_RE = re.compile(
    r"<meta\b(?=[^>]*\bname=[\"']description[\"'])(?=[^>]*\bcontent=[\"'][^\"']+[\"'])[^>]*>",
    re.IGNORECASE | re.DOTALL,
)
BLOCKED_CLAIM_RE = re.compile(
    r"\b(uncontrolled\s+model\s+self[-\s]?modification|self[-\s]?modifying\s+model)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ValidationError:
    rel: str
    reason: str
    suggestion: str

    def format(self) -> str:
        return f"{self.rel}: {self.reason}. Suggested fix: {self.suggestion}"


def normalize_rel(path: str | Path | PurePosixPath) -> str:
    return PurePosixPath(str(path).replace("\\", "/")).as_posix().lstrip("./")


def is_public_aep_package(rel: str | Path) -> bool:
    rel = normalize_rel(rel)
    return bool(PUBLIC_AEP_PACKAGE_RE.match(rel))


def has_standalone_marker(text: str) -> bool:
    return (
        "GOALOS-STANDALONE-PROOF" in text
        or 'name="goalos-page-type" content="standalone-proof"' in text
        or "data-goalos-standalone" in text
    )


def is_standalone_proof_page(rel: str | Path, text: str = "") -> bool:
    rel = normalize_rel(rel)
    return bool(STANDALONE_PROOF_RE.match(rel)) or has_standalone_marker(text)


def is_app_page(rel: str | Path) -> bool:
    rel = normalize_rel(rel)
    return bool(APP_PAGE_RE.match(rel))


def classify_public_path(rel: str | Path, text: str = "") -> str:
    rel = normalize_rel(rel)
    if is_public_aep_package(rel):
        return "aep_standard_package"
    if is_blocked_paid_or_private_artifact(rel):
        return "blocked_paid_artifact"
    if rel.lower().endswith(".html"):
        if is_app_page(rel):
            return "app_page"
        if is_standalone_proof_page(rel, text):
            return "standalone_proof_page"
        return "canonical_page"
    return "public_asset"


def requires_canonical_shell(rel: str | Path, text: str = "") -> bool:
    rel = normalize_rel(rel)
    if not rel.lower().endswith(".html"):
        return False
    if is_app_page(rel):
        return False
    if is_standalone_proof_page(rel, text):
        return False
    return True


def is_blocked_paid_or_private_artifact(rel: str | Path) -> bool:
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


def is_public_html_path(path: Path) -> bool:
    return path.suffix.lower() == ".html" and "_archive" not in path.parts


def discover_public_root(repo_root: Path) -> Path:
    site = repo_root / "site"
    if site.is_dir():
        return site
    public = repo_root / "public"
    if public.is_dir():
        return public
    raise FileNotFoundError("No public site root found. Expected site/ or public/.")


def has_title(text: str) -> bool:
    return bool(TITLE_RE.search(text))


def has_meta_description(text: str) -> bool:
    return bool(META_DESCRIPTION_RE.search(text))


def has_goalos_backlink(text: str) -> bool:
    lowered = text.lower()
    return "/proof-gradient/" in text or "goalos" in lowered or "proof gradient" in lowered


def has_quebec_ai_identity(text: str) -> bool:
    return "QUEBEC.AI" in text or "⚜️" in text or "✨" in text


def internal_proof_gradient_links(text: str) -> list[str]:
    links: list[str] = []
    for raw in LINK_RE.findall(text):
        if raw.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            continue
        parsed = urlparse(raw)
        if parsed.path.startswith("/proof-gradient/"):
            links.append(raw)
    return links


def site_target_exists(public_root: Path, url_path: str) -> bool:
    if not url_path.startswith("/proof-gradient/"):
        return True
    rel = url_path.removeprefix("/proof-gradient/").split("#", 1)[0].split("?", 1)[0]
    if rel == "":
        return (public_root / "index.html").exists()
    candidate = public_root / rel
    if candidate.is_file():
        return True
    if candidate.is_dir() and (candidate / "index.html").exists():
        return True
    if rel.endswith("/") and (public_root / rel / "index.html").exists():
        return True
    if (public_root / f"{rel}.html").exists():
        return True
    return False


def validate_required_brand_assets(public_root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    required = [
        ("assets/quebecaisealv5.png", "Restore the QUEBEC.AI seal copied from assets/quebecaisealv5.png."),
        ("favicon.png", "Generate favicon.png from the QUEBEC.AI seal."),
        ("assets/apple-touch-icon.png", "Generate apple-touch-icon.png from the QUEBEC.AI seal."),
    ]
    for rel, suggestion in required:
        if not (public_root / rel).exists():
            errors.append(ValidationError(rel, "required QUEBEC.AI seal/icon file is missing", suggestion))

    has_brand_assets = any((public_root / rel).exists() for rel, _ in required) or (public_root / "brand").exists()
    if has_brand_assets and not (public_root / "site.webmanifest").exists():
        errors.append(ValidationError("site.webmanifest", "brand assets exist but the web manifest is missing", "Restore site.webmanifest for the GoalOS / QUEBEC.AI public site."))
    manifest = public_root / "assets" / "brand-assets-v8.json"
    if has_brand_assets and not manifest.exists():
        errors.append(ValidationError("assets/brand-assets-v8.json", "brand assets exist but the brand manifest is missing", "Restore assets/brand-assets-v8.json or remove incomplete brand assets."))
    return errors
